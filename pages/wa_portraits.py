#!/usr/bin/env python3
"""
wa_portraits.py -- link images already uploaded to World Anvil to their
Kindred articles.

Upload happens in the WA UI (the Boromir client wraps a JSON PUT, not a
multipart upload, so binaries can't go through it). This script does the
matching afterwards: list the world's images, pair each with a Kindred by
filename, and patch the article's portrait.

    python wa_portraits.py                 # show matches, write nothing
    python wa_portraits.py --push          # set portraits

Refuses to touch the labelled world map, which is GM-only.
"""
import sys, json, re, argparse
from pathlib import Path

from wa_config import load_config, ConfigError

STATE = Path.home() / ".config" / "sideros" / "wa_sync_state.json"

# Image filename stem -> Kindred article title.
# Deprecated names are mapped deliberately so a stale upload still lands on the
# right article rather than silently missing.
FILENAME_TO_KINDRED = {
    "human": "Human", "eldren": "Eldren", "dunmarim": "Dunmarim",
    "wolfshifter": "Wolf-Shifter", "gearforged": "Gear-Forged",
    "ashetouched": "Ashé-Touched", "serpentkin": "Serpent-Kin",
    "avian": "Avian", "faeblooded": "Fae-Blooded", "wakakin": "Waka-kin",
    "te_kapo": "Te Kapo", "tekapo": "Te Kapo", "lizardfolk": "Lizard-Folk",
    "beastdescended": "Beast-Descended", "geodekin": "Geode-Kin",
    "beastkin": "Beast-Kin", "orckin": "Orc-Kin", "giantkin": "Giant-Kin",
    "elementalkin": "Elemental-Kin",
}

# Never link these into a player-facing world. The v11 map carries printed
# labels; text scans cannot see words baked into an image.
FORBIDDEN_PUBLIC = {"siderosv11", "sideros_v11", "siderosv11map"}


def norm(name):
    """Reduce a filename to comparable letters: 'Wolf Shifter (1).jpg',
    'WolfShifter.jpg' and 'wolf-shifter' all collapse to 'wolfshifter'."""
    return re.sub(r"[^a-z0-9]", "", Path(str(name)).stem.lower())


def match_kindred(title):
    """Filenames survive downloads badly -- browsers add ' (1)', strip
    extensions, swap underscores for spaces. Match on normalised substrings
    in both directions rather than requiring an exact key."""
    n = norm(title)
    if not n:
        return None
    if n in FILENAME_TO_KINDRED:
        return FILENAME_TO_KINDRED[n]
    # longest key first so 'beastkin' cannot shadow 'beastdescended'
    for key in sorted(FILENAME_TO_KINDRED, key=len, reverse=True):
        if key in n or n in key:
            return FILENAME_TO_KINDRED[key]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--push", action="store_true")
    ap.add_argument("--world", choices=["sideros", "astrolan"], default="sideros")
    args = ap.parse_args()

    try:
        cfg = load_config()
    except ConfigError as exc:
        sys.exit(f"CONFIG ERROR\n{exc}")

    world_id = cfg.world_sideros if args.world == "sideros" else cfg.world_astrolan
    if not world_id:
        sys.exit(f"WA_WORLD_{args.world.upper()} is not set")

    if not STATE.exists():
        sys.exit("No sync state found -- push the Kindred articles first.")
    state = json.loads(STATE.read_text())

    from pywaclient.api import BoromirApiClient
    client = BoromirApiClient(
        "sideros-canon-sync", "https://github.com/mckamw99/sideros", "0.1.0",
        cfg.application_key, cfg.auth_token)

    images = list(client.world.images(world_id))
    print(f"{len(images)} image(s) in {args.world}\n")

    matched, unmatched, blocked = [], [], []
    for img in images:
        title = img.get("title") or img.get("filename") or ""
        s = norm(title)
        if any(f in s for f in FORBIDDEN_PUBLIC) and args.world == "sideros":
            blocked.append(title)
            continue
        kindred = match_kindred(title)
        key = f"{args.world}:{kindred}" if kindred else None
        if kindred and key in state:
            matched.append((kindred, img["id"], state[key], title))
        else:
            unmatched.append((title, kindred or "-"))

    if blocked:
        print("REFUSED -- GM-only asset, not linked to a public world:")
        for b in blocked:
            print(f"    {b}")
        print()

    print(f"MATCHED ({len(matched)}):")
    for k, iid, aid, title in matched:
        print(f"    {k:16} {title[:28]:28} img {iid[:8]}… -> art {aid[:8]}…")

    if unmatched:
        print(f"\nNO ARTICLE ({len(unmatched)}):")
        for title, guess in unmatched:
            print(f"    {title[:34]:34} kindred={guess}")

    if not args.push:
        print("\nDry run -- nothing written. Re-run with --push.")
        return

    ok = 0
    for k, iid, aid, _t in matched:
        try:
            client.article.patch(aid, {"portrait": {"id": iid}})
            print(f"  {k:16} portrait set")
            ok += 1
        except Exception as exc:                          # noqa: BLE001
            print(f"  {k:16} FAILED -- {str(exc)[:140]}", file=sys.stderr)
    print(f"\n{ok}/{len(matched)} portraits set")


if __name__ == "__main__":
    main()
