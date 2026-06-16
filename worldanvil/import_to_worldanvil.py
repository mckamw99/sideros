#!/usr/bin/env python3
"""
import_to_worldanvil.py
-----------------------
Pushes the staged Sideros articles in this folder to World Anvil via the
Boromir (v2) API. RUN THIS ON MATT'S MACHINE — the build container that
generated these files cannot reach worldanvil.com (egress-blocked).

Prerequisites
-------------
1. World Anvil Application Key APPROVED (still pending as of staging).
2. A User Authentication token (User -> API Tokens page).
3. The target World's id.
4. pip install pywaclient   (Boromir client; v1.6.8+ confirmed available)

Set environment variables (do NOT hardcode secrets):
    export WA_APPLICATION_KEY="..."
    export WA_AUTH_TOKEN="..."
    export WA_WORLD_ID="..."

Usage
-----
    python import_to_worldanvil.py             # DRY RUN — prints what it would send
    python import_to_worldanvil.py --live      # actually creates articles
    python import_to_worldanvil.py --wave 1    # only wave 1 (default: all)
    python import_to_worldanvil.py --only kindreds   # filter by category substring

Auth + endpoint are verified against the Boromir docs (headers x-application-key /
x-auth-token; base /api/external/boromir). The exact CREATE payload field names
(template / category id / draft state) should be confirmed against the live
article schema on first run — that is exactly why DRY RUN is the default.
"""
import os, sys, json, argparse, re
from pathlib import Path

import requests  # for the article PUT; pywaclient used for discovery

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "manifest.json"
BASE = "https://www.worldanvil.com/api/external/boromir"
APP = "Sideros-Importer/1.0 (private)"

def load_front_matter(path: Path):
    """Parse the leading --- YAML-ish block and return (meta_dict, body_str)."""
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="actually create articles")
    ap.add_argument("--wave", type=int, default=None)
    ap.add_argument("--only", type=str, default=None, help="category substring filter")
    args = ap.parse_args()

    app_key = os.environ.get("WA_APPLICATION_KEY")
    auth = os.environ.get("WA_AUTH_TOKEN")
    world_id = os.environ.get("WA_WORLD_ID")

    if args.live and not all([app_key, auth, world_id]):
        sys.exit("LIVE run needs WA_APPLICATION_KEY, WA_AUTH_TOKEN, WA_WORLD_ID set.")

    manifest = json.loads(MANIFEST.read_text())
    items = manifest["articles"]
    if args.wave is not None:
        items = [a for a in items if a.get("wave") == args.wave]
    if args.only:
        items = [a for a in items if args.only.lower() in a.get("category", "").lower()]

    headers = {
        "x-application-key": app_key or "<APP_KEY>",
        "x-auth-token": auth or "<AUTH_TOKEN>",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": APP,
    }

    print(f"{'LIVE' if args.live else 'DRY RUN'} — {len(items)} article(s) "
          f"-> world {world_id or '<WA_WORLD_ID>'}\n")

    for a in items:
        meta, body = load_front_matter(HERE / a["file"])
        title = meta.get("title", a.get("title", "Untitled"))
        # Best-known Boromir article create payload. Confirm field names live.
        payload = {
            "title": title,
            "content": body,                 # BBCode
            "state": meta.get("privacy", "public"),   # public | private
            "world": {"id": world_id},
            "templateType": meta.get("template", "article"),
            "tags": meta.get("tags", ""),
        }
        if not args.live:
            print(f"[DRY] {a['category']:10s} | {title:18s} "
                  f"| tmpl={payload['templateType']:8s} | {len(body)} chars BBCode")
            continue
        r = requests.put(f"{BASE}/article", headers=headers, json=payload, timeout=30)
        ok = r.status_code in (200, 201)
        print(f"[{'OK ' if ok else 'ERR'}] {title:18s} -> {r.status_code}")
        if not ok:
            print("   ", r.text[:300])

    if not args.live:
        print("\nDry run only. Re-run with --live once the Application Key is approved "
              "and WA_* env vars are set. Verify the first article in World Anvil, then "
              "continue the batch.")

if __name__ == "__main__":
    main()
