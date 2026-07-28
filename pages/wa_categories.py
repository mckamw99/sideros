#!/usr/bin/env python3
"""
wa_categories.py -- list the categories in each world and write the id map
that wa_canon_sync.py uses to file articles automatically.

    python wa_categories.py            # list both worlds
    python wa_categories.py --write    # also write wa_category_map.json
"""
import sys, json, argparse
from pathlib import Path

from wa_config import load_config, ConfigError

OUT = Path("wa_category_map.json")

# content type -> category NAME (matched case-insensitively against WA)
TYPE_TO_CATEGORY = {
    "kindred":      "Kindreds",
    "civilization": "Civilizations",
    "path":         "Paths & Callings",
    "origin":       "Origins",
    "working":      "The Weaving",
    "cosmology":    "Cosmology",
    "beast":        "Bestiary",
    "location":     "World and Geography",
    "item":         "Equipment & Items",
    "rules":        "Rules & References",
    "history":      "History and Lore",
    "npc":          "Characters",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    try:
        cfg = load_config()
    except ConfigError as exc:
        sys.exit(f"CONFIG ERROR\n{exc}")

    from pywaclient.api import BoromirApiClient
    client = BoromirApiClient(
        "sideros-canon-sync", "https://github.com/mckamw99/sideros", "0.1.0",
        cfg.application_key, cfg.auth_token)

    worlds = {"sideros": cfg.world_sideros, "astrolan": cfg.world_astrolan}
    found = {}

    for label, wid in worlds.items():
        if not wid:
            print(f"\n{label}: not configured, skipping")
            continue
        print(f"\n=== {label} ({wid[:8]}…) ===")
        cats = list(client.world.categories(wid))
        if not cats:
            print("  (no categories)")
        found[label] = {}
        for c in sorted(cats, key=lambda x: x.get("title", "")):
            title, cid = c.get("title", "?"), c.get("id", "?")
            print(f"  {title:26} {cid}")
            found[label][title.lower()] = cid

    if not args.write:
        print("\n(dry run -- re-run with --write to save the mapping)")
        return

    # resolve content type -> category id, per world
    mapping, missing = {}, []
    for label in found:
        mapping[label] = {}
        for ctype, cname in TYPE_TO_CATEGORY.items():
            cid = found[label].get(cname.lower())
            if cid:
                mapping[label][ctype] = cid
            elif label == "sideros":
                missing.append(cname)

    OUT.write_text(json.dumps(mapping, indent=2))
    print(f"\nWrote {OUT}")
    if missing:
        print("\nNo Sideros category matched these names -- check spelling,"
              "\nor edit TYPE_TO_CATEGORY in this file:")
        for m in sorted(set(missing)):
            print(f"    {m}")


if __name__ == "__main__":
    main()
