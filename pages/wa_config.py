#!/usr/bin/env python3
"""
World Anvil credential loader for the Sideros project.

Design goals:
  - Credentials live in .env, never in source, never in argv, never printed.
  - Same code path works on a local machine or in a sandbox.
  - Fails loudly and early with an actionable message.
  - No third-party dependency for .env parsing.

Usage:
    from wa_config import load_config, build_client, redact

    cfg = load_config()
    client = build_client(cfg)
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# .env discovery and parsing
# ---------------------------------------------------------------------------

ENV_FILENAME = ".env"

# Searched in order. First hit wins.
SEARCH_PATHS = [
    Path.cwd(),
    Path(__file__).resolve().parent,
    Path.home() / ".config" / "sideros",
]


def find_env_file(explicit: str | None = None) -> Path | None:
    """Locate the .env file, or return None if there isn't one."""
    if explicit:
        p = Path(explicit).expanduser().resolve()
        return p if p.is_file() else None
    for base in SEARCH_PATHS:
        candidate = base / ENV_FILENAME
        if candidate.is_file():
            return candidate
    return None


def parse_env_file(path: Path) -> dict[str, str]:
    """
    Minimal .env parser. Supports KEY=value, # comments, blank lines,
    and single- or double-quoted values. Deliberately not clever.
    """
    out: dict[str, str] = {}
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            print(f"  ! {path.name}:{lineno} ignored (no '='): {line[:40]}",
                  file=sys.stderr)
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip()
        # strip surrounding quotes if balanced
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        out[key] = value
    return out


def _truthy(value: str | None, default: bool = False) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in ("1", "true", "yes", "on")


# ---------------------------------------------------------------------------
# Config object
# ---------------------------------------------------------------------------

@dataclass
class WAConfig:
    application_key: str = field(repr=False)
    auth_token: str = field(repr=False)
    app_name: str = "sideros-canon-sync"
    app_url: str = "https://github.com/mckamw99/sideros"
    app_version: str = "0.1.0"
    world_sideros: str = ""
    world_astrolan: str = ""
    dry_run: bool = True
    require_clean_scan: bool = True
    source: str = "unknown"

    def __str__(self) -> str:
        return (
            f"WAConfig(source={self.source}, "
            f"app_key={redact(self.application_key)}, "
            f"auth_token={redact(self.auth_token)}, "
            f"sideros={self.world_sideros or '<unset>'}, "
            f"astrolan={self.world_astrolan or '<unset>'}, "
            f"dry_run={self.dry_run})"
        )

    # Guard against accidental logging of the whole object
    __repr__ = __str__


def redact(secret: str | None) -> str:
    """Render a secret safely for logs: first 4 chars, length, nothing else."""
    if not secret:
        return "<missing>"
    if len(secret) <= 8:
        return f"<set, {len(secret)} chars>"
    return f"{secret[:4]}…<{len(secret)} chars>"


class ConfigError(RuntimeError):
    pass


def load_config(env_path: str | None = None, require_worlds: bool = False) -> WAConfig:
    """
    Load credentials. Process environment wins over .env, so you can override
    a single value at invocation time without editing the file.
    """
    found = find_env_file(env_path)
    file_vals = parse_env_file(found) if found else {}

    def get(key: str, default: str = "") -> str:
        return os.environ.get(key) or file_vals.get(key, default)

    app_key = get("WA_APPLICATION_KEY")
    auth = get("WA_AUTH_TOKEN")

    missing = [k for k, v in
               (("WA_APPLICATION_KEY", app_key), ("WA_AUTH_TOKEN", auth))
               if not v]
    if missing:
        where = str(found) if found else \
            f"no {ENV_FILENAME} found in: " + ", ".join(str(p) for p in SEARCH_PATHS)
        raise ConfigError(
            f"Missing required credential(s): {', '.join(missing)}\n"
            f"  Looked in: {where}\n"
            f"  Fix: copy env.example to .env and fill in both values."
        )

    cfg = WAConfig(
        application_key=app_key,
        auth_token=auth,
        app_name=get("WA_APP_NAME", "sideros-canon-sync"),
        app_url=get("WA_APP_URL", "https://github.com/mckamw99/sideros"),
        app_version=get("WA_APP_VERSION", "0.1.0"),
        world_sideros=get("WA_WORLD_SIDEROS"),
        world_astrolan=get("WA_WORLD_ASTROLAN"),
        dry_run=_truthy(get("WA_DRY_RUN"), default=True),
        require_clean_scan=_truthy(get("WA_REQUIRE_CLEAN_SCAN"), default=True),
        source=str(found) if found else "process environment",
    )

    if require_worlds and not cfg.world_sideros:
        raise ConfigError(
            "WA_WORLD_SIDEROS is not set.\n"
            "  Fix: run `python3 wa_preflight.py --list-worlds` and paste the UUID."
        )

    return cfg


# ---------------------------------------------------------------------------
# Client factory
# ---------------------------------------------------------------------------

def build_client(cfg: WAConfig):
    """
    Construct a BoromirApiClient. Signature verified against pywaclient:
        BoromirApiClient(name, url, version, application_key, authentication_token)
    """
    try:
        from pywaclient.api import BoromirApiClient
    except ImportError as exc:
        raise ConfigError(
            "pywaclient is not installed.\n"
            "  Fix: pip install pywaclient"
        ) from exc

    return BoromirApiClient(
        cfg.app_name,
        cfg.app_url,
        cfg.app_version,
        cfg.application_key,
        cfg.auth_token,
    )


# ---------------------------------------------------------------------------
# Guard used by write scripts
# ---------------------------------------------------------------------------

def assert_not_astrolan(cfg: WAConfig, world_id: str) -> None:
    """
    Hard stop: refuse to treat the private GM world as a push target for
    player-facing content. Cheap insurance against a copy-paste mistake.
    """
    if cfg.world_astrolan and world_id == cfg.world_astrolan:
        raise ConfigError(
            "Refusing to push player-facing content to the Astrolan (GM) world.\n"
            "  This is the two-world safety rail. Check your --world argument."
        )


if __name__ == "__main__":
    # Safe to run: prints redacted values only.
    try:
        cfg = load_config()
    except ConfigError as exc:
        print(f"CONFIG ERROR\n{exc}", file=sys.stderr)
        sys.exit(2)
    print("Config loaded OK")
    print(f"  {cfg}")
    print(f"  dry_run={cfg.dry_run}  require_clean_scan={cfg.require_clean_scan}")
