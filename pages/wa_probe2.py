#!/usr/bin/env python3
"""
wa_probe.py -- discover the real Species template field names.

World Anvil's Swagger docs are JS-rendered and the Codex only lists *display*
names ("Growth Rate & Stages"), not the JSON keys the API actually accepts.
Guessing them would mean silently dropping content into fields that don't
exist, so this asks the API instead.

Method: create one throwaway Species article in the ASTROLAN (private, GM)
world, PATCH it with a batch of candidate keys each carrying a unique marker,
read it back, and report which markers survived. Surviving key == real field.

Writes only to Astrolan. Never touches the public world.
Run with --cleanup afterwards to delete the probe article.

    python wa_probe.py            # create + probe + report
    python wa_probe.py --cleanup  # delete the probe article
"""
import sys, json, argparse
from pathlib import Path

from wa_config import load_config, ConfigError

PROBE_TITLE = "ZZ_API_PROBE_SAFE_TO_DELETE"
STATE = Path.home() / ".config" / "sideros" / "probe_state.json"

# Candidate JSON keys, derived from the Species template's display names.
# Marker values are unique so we can tell which key each one landed in.
CANDIDATES = [
    # --- round 1 corrections: real keys learned from the API dump --------
    "traits", "growthrate", "ecology", "diet", "biocycle",
    "socialstructure", "geographicalOrigin", "symbiotic",
    "relationshipsIdeals", "dresscode", "mythsAndLegends",
    # --- extras worth having, seen in the returned key list --------------
    "ancenstry", "averageHeight", "averageLength", "averagePhysique",
    "averageWeight", "behaviour", "conservation", "discoverer",
    "firstnamesFemale", "firstnamesMale", "lastnames", "majorReligions",
    "skinHairColor", "pronunciation", "trinominal", "authornotes",
    "sidebarcontentbottom", "sidepanelcontent", "snippet", "footnotes",
    "credits", "prompt", "datasheet",
]


def build_client(cfg):
    from pywaclient.api import BoromirApiClient
    return BoromirApiClient(
        "sideros-canon-sync",
        "https://github.com/mckamw99/sideros",
        "0.1.0",
        cfg.application_key,
        cfg.auth_token,
    )


def cleanup(client):
    if not STATE.exists():
        print("No probe state found -- nothing to clean up.")
        return
    aid = json.loads(STATE.read_text())["id"]
    client.article.delete(aid)
    STATE.unlink()
    print(f"Deleted probe article {aid}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cleanup", action="store_true")
    args = ap.parse_args()

    try:
        cfg = load_config()
    except ConfigError as exc:
        print(f"CONFIG ERROR\n{exc}", file=sys.stderr)
        sys.exit(2)

    if not cfg.world_astrolan:
        print("WA_WORLD_ASTROLAN is not set. Refusing to probe against the "
              "public world.", file=sys.stderr)
        sys.exit(2)

    client = build_client(cfg)

    if args.cleanup:
        cleanup(client)
        return

    # ---- 1. reuse the existing probe article if we already made one ------
    if STATE.exists():
        aid = json.loads(STATE.read_text())["id"]
        print(f"[1/4] Reusing existing probe article {aid}")
        return _probe(client, aid)

    print(f"[1/4] Creating probe article in Astrolan ({cfg.world_astrolan[:8]}…)")
    created = client.article.put({
        "title": PROBE_TITLE,
        "templateType": "species",
        "world": {"id": cfg.world_astrolan},
        "content": "Throwaway article created by wa_probe.py. Safe to delete.",
        "state": "private",
    })
    aid = created.get("id") or created.get("entity", {}).get("id")
    print(f"      id: {aid}")
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"id": aid}))

    return _probe(client, aid)


def _probe(client, aid):
    # ---- 2. patch every candidate with a unique marker -------------------
    print(f"[2/4] Patching {len(CANDIDATES)} candidate fields…")
    markers = {k: f"PROBEMARKER-{i:03d}-{k}" for i, k in enumerate(CANDIDATES)}
    accepted, rejected = [], []
    for key, val in markers.items():
        try:
            client.article.patch(aid, {key: val})
            accepted.append(key)
        except Exception as exc:                      # noqa: BLE001
            rejected.append((key, type(exc).__name__))

    # ---- 3. read back at full granularity --------------------------------
    print("[3/4] Reading article back (granularity=2)…")
    full = client.article.get(aid, 2)

    # ---- 4. report --------------------------------------------------------
    real = [k for k in CANDIDATES
            if isinstance(full.get(k), str) and markers[k] in full.get(k, "")]
    missing = [k for k in CANDIDATES if k not in real]

    print("\n" + "=" * 62)
    print(f"CONFIRMED FIELDS ({len(real)})")
    print("=" * 62)
    for k in real:
        print(f"  {k}")
    print(f"\nNOT PERSISTED ({len(missing)}): {', '.join(missing) or 'none'}")
    if rejected:
        print(f"\nPATCH ERRORS: {rejected}")

    extra = sorted(set(full) - set(CANDIDATES))
    print(f"\nOTHER KEYS RETURNED BY THE API ({len(extra)}):")
    print("  " + ", ".join(extra))

    out = Path("wa_species_schema_round2.json")
    out.write_text(json.dumps(
        {"confirmed": real, "not_persisted": missing, "all_keys": sorted(full)},
        indent=2))
    print(f"\nSchema written to {out}")
    print("Run `python wa_probe.py --cleanup` to delete the probe article.")


if __name__ == "__main__":
    main()
