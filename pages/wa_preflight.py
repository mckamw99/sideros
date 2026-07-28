#!/usr/bin/env python3
"""
World Anvil preflight check — READ ONLY. Makes no writes of any kind.

Run this first, before anything else touches the API.

    python3 wa_preflight.py                 # verify credentials
    python3 wa_preflight.py --list-worlds   # verify + list world UUIDs
    python3 wa_preflight.py --diagnose      # add network/Cloudflare diagnosis

Exit codes:
    0  credentials valid
    2  configuration problem (missing .env, missing keys)
    3  authentication rejected by World Anvil
    4  network or Cloudflare blocked the request
"""

from __future__ import annotations

import argparse
import sys

from wa_config import ConfigError, build_client, load_config, redact


def probe_reachability() -> tuple[bool, str]:
    """
    Determine whether worldanvil.com is reachable at all, independent of
    credentials. An egress proxy reports its refusal in a response header,
    which never reaches the client exception — so we look for it directly.

    Returns (reachable, detail).
    """
    import urllib.error
    import urllib.request

    # Cloudflare rule 1010 blocks on browser signature: a default
    # "Python-urllib/3.x" User-Agent is rejected at the edge before World Anvil
    # ever sees the request, which looks identical to a network failure.
    # pywaclient sets a real UA, so the probe must too or it disagrees with the
    # very client it is meant to be vetting.
    import os as _os
    _ua = "{} / {} ({})".format(
        _os.environ.get("WA_APP_NAME", "sideros-canon-sync"),
        _os.environ.get("WA_APP_VERSION", "0.1.0"),
        _os.environ.get("WA_APP_URL", "https://github.com/mckamw99/sideros"),
    )
    req = urllib.request.Request(
        "https://www.worldanvil.com/api/external/boromir/user",
        headers={"Accept": "application/json", "User-Agent": _ua},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return True, f"reachable (HTTP {resp.status} without credentials)"
    except urllib.error.HTTPError as err:
        deny = err.headers.get("x-deny-reason") if err.headers else None
        if deny:
            return False, f"egress proxy refused: x-deny-reason={deny}"
        body = ""
        try:
            body = err.read(600).decode("utf-8", "replace").lower()
        except Exception:  # noqa: BLE001
            pass
        if "just a moment" in body or "cf-" in body or "cloudflare" in body:
            return False, "Cloudflare bot challenge returned instead of JSON"
        # A 401/403 from WA itself means the host IS reachable
        return True, f"reachable (HTTP {err.code} without credentials — expected)"
    except Exception as err:  # noqa: BLE001
        return False, f"could not connect: {type(err).__name__}: {err}"


def diagnose_failure(exc: Exception) -> tuple[int, str]:
    """Turn an opaque exception into an actionable message."""
    text = f"{type(exc).__name__}: {exc}"
    low = text.lower()

    # Before blaming credentials, check whether the request even left the box.
    reachable, detail = probe_reachability()
    if not reachable:
        if "x-deny-reason" in detail:
            return 4, (
                f"Request never left this machine — {detail}\n"
                "  You are inside a sandbox with a domain allowlist.\n"
                "  Fix: add worldanvil.com to the allowed domains in your\n"
                "       network settings, or run this on your local machine.\n"
                "  Your credentials were NOT tested and may be perfectly fine."
            )
        return 4, (
            f"Could not reach worldanvil.com — {detail}\n"
            "  Your credentials were NOT tested."
        )

    if "host_not_allowed" in low:
        return 4, (
            "Blocked by an egress proxy before the request left this machine.\n"
            "  You are running inside a sandbox with a domain allowlist.\n"
            "  Fix: add worldanvil.com to the allowed domains in your network\n"
            "       settings, or run this script on your local machine instead."
        )
    if "just a moment" in low or "cloudflare" in low or "challenge" in low:
        return 4, (
            "Cloudflare returned a bot-challenge page instead of JSON.\n"
            "  This is a known Boromir API issue, not a credential problem.\n"
            "  Fix: retry; if persistent, raise it in the #api-development\n"
            "       channel on the World Anvil Discord."
        )
    if "403" in low or "forbidden" in low:
        return 3, (
            "403 Forbidden. Two likely causes:\n"
            "  1. The application key is not yet active on your account.\n"
            "  2. Cloudflare intercepted the request (see above).\n"
            "  Check: is your account Grandmaster tier or above?"
        )
    if "401" in low or "unauthor" in low:
        return 3, (
            "401 Unauthorized — the auth token was rejected.\n"
            "  Fix: regenerate the User Authentication Token on World Anvil\n"
            "       and update WA_AUTH_TOKEN in .env."
        )
    if "404" in low:
        return 3, (
            "404 Not Found. The endpoint or resource ID does not exist.\n"
            "  If this is the /user call, the API version may have moved."
        )
    if any(w in low for w in ("timeout", "timed out", "connection", "resolve", "dns")):
        return 4, "Network failure — could not reach worldanvil.com at all."

    return 3, f"Unrecognised failure.\n  {text}"


def main() -> int:
    ap = argparse.ArgumentParser(description="World Anvil read-only preflight")
    ap.add_argument("--list-worlds", action="store_true",
                    help="list your worlds and their UUIDs")
    ap.add_argument("--diagnose", action="store_true",
                    help="print extra diagnostic detail on failure")
    ap.add_argument("--env", default=None, help="path to a specific .env file")
    args = ap.parse_args()

    # ---- 1. Load config -------------------------------------------------
    print("[1/3] Loading credentials…")
    try:
        cfg = load_config(env_path=args.env)
    except ConfigError as exc:
        print(f"\nCONFIG ERROR\n{exc}", file=sys.stderr)
        return 2

    print(f"      source        : {cfg.source}")
    print(f"      application key: {redact(cfg.application_key)}")
    print(f"      auth token     : {redact(cfg.auth_token)}")
    print(f"      dry run        : {cfg.dry_run}")

    # ---- 2. Build client ------------------------------------------------
    print("[2/3] Building client…")
    try:
        client = build_client(cfg)
    except ConfigError as exc:
        print(f"\nCONFIG ERROR\n{exc}", file=sys.stderr)
        return 2

    # ---- 3. Single read-only call ---------------------------------------
    print("[3/3] Calling /user (read-only)…")
    try:
        identity = client.user.identity()
    except Exception as exc:  # noqa: BLE001 - we classify below
        code, message = diagnose_failure(exc)
        print(f"\nFAILED\n{message}", file=sys.stderr)
        if args.diagnose:
            import traceback
            print("\n--- raw traceback ---", file=sys.stderr)
            traceback.print_exc()
        return code

    username = identity.get("username") or identity.get("id") or "<unknown>"
    print(f"\n  AUTHENTICATED as: {username}")

    # ---- Optional: list worlds -----------------------------------------
    if args.list_worlds:
        print("\n  Worlds on this account:")
        try:
            worlds = list(client.user.worlds(identity["id"]))
        except Exception as exc:  # noqa: BLE001
            code, message = diagnose_failure(exc)
            print(f"  could not list worlds:\n  {message}", file=sys.stderr)
            return code

        if not worlds:
            print("    (none yet — create Sideros and Astrolan in the WA UI)")
        for w in worlds:
            print(f"    {w.get('id')}   {w.get('title')}")
        print("\n  Paste the relevant UUIDs into .env as")
        print("    WA_WORLD_SIDEROS=…    (public, player-facing)")
        print("    WA_WORLD_ASTROLAN=…   (private, GM-only)")

    print("\nPreflight OK. No writes were performed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
