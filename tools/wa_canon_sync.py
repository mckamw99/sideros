#!/usr/bin/env python3
"""
wa_canon_sync.py -- one-way publish: local files -> World Anvil.

Design rules, in order of importance:

1. ONE WAY. Local files are canon. This script never reads WA content back
   into your sources. World Anvil has no version history (the feature has been
   formally declined), so anything edited only in WA has no undo. Edit locally,
   re-run this.

2. WORLD-AWARE SECRET GATE. GM material is expected in Astrolan and forbidden
   in Sideros. A gate that fires on every GM push gets ignored, so it only
   blocks when the target world is public.

3. IDEMPOTENT. Article ids are recorded in a state file, so a second run
   patches the existing article instead of creating a duplicate.

Usage:
    python wa_canon_sync.py --list
    python wa_canon_sync.py --kindred Human --world sideros --dry-run
    python wa_canon_sync.py --kindred Human --world sideros --push
"""
import re, json, sys, argparse
from pathlib import Path

from wa_config import load_config, ConfigError, assert_not_astrolan

SRC = Path("sideros_kindred_compendium.html")
STATE = Path.home() / ".config" / "sideros" / "wa_sync_state.json"
CATMAP = Path("wa_category_map.json")

PANELS = [
    ("Human", "panel-human"), ("Eldren", "panel-eldren"),
    ("Dunmarim", "panel-dunmarim"), ("Wolf-Shifter", "panel-wolf"),
    ("Gear-Forged", "panel-gear"), ("Ashé-Touched", "panel-ashe"),
]

# The definite article and the specific names are the secret; the bond-tier
# words (Paired/Triad/Quad/Quint) are player-safe mechanics and are NOT here.
HARD_SECRETS = [
    "Quint Bond", "all five members", "fully acknowledged", "cluster members",
    "Five Who Remember", "Fang of the Whisper", "Antarctos", "Serath",
    "Drava Nullsong", "Quint Bond Adjacent", "Four Architects", "Scion Shift",
    "Inti-kora", "Asha-Wing", "Hinerangi", "Matuā-kore", "Ashen Coil",
]

# Clauses excised from PUBLIC articles only. Astrolan keeps them.
# Note: mechanics text leaks secrets too -- the Faction Fluency trait names the
# Ashen Coil inline in a faction list. Lore-only extraction never saw this.
GM_ONLY_CLAUSES = [
    "The Ashen Coil's Triad is human. ",
    "Ashen Coil, ",
]


# ------------------------------------------------------------------ extract
def _strip(x):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", "", x)).strip()


def _field(sec, cls, many=False):
    hits = [_strip(h) for h in
            re.findall(rf'class="{cls}"[^>]*>(.*?)</', sec, re.S)]
    return hits if many else (hits[0] if hits else "")


def extract(name):
    html = SRC.read_text(encoding="utf-8")
    ids = [p for _, p in PANELS]
    i = [n for n, _ in PANELS].index(name)
    start = html.find(f'id="{ids[i]}"')
    end = html.find(f'id="{ids[i+1]}"') if i + 1 < len(ids) else len(html)
    if start == -1:
        raise SystemExit(f"Panel for {name} not found in {SRC}")
    sec = html[start:end]

    lore = [_strip(p) for p in
            re.findall(r'class="lore-para"[^>]*>(.*?)</p>', sec, re.S)]
    traits = list(zip(
        _field(sec, "tc-name", True), _field(sec, "tc-type", True),
        [_strip(x) for x in
         re.findall(r'class="tc-body"[^>]*>(.*?)</div>', sec, re.S)]))
    stats = list(zip(_field(sec, "sc-label", True), _field(sec, "sc-val", True),
                     _field(sec, "sc-note", True)))
    return {
        "name": name, "lore": lore, "traits": traits, "stats": stats,
        "also": _field(sec, "kh-also").replace("Also called:", "").strip(),
        "home": _field(sec, "kh-home"),
        "essence": _field(sec, "kh-essence"),
    }


def _excerpt(text, limit=250):
    """WA's excerpt column is VARCHAR(255). Overrun is rejected by the
    database, not by the API, so the error arrives as a raw SQL trace."""
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(",;:—-") + "…"


# ------------------------------------------------------------------ build
def build(k, world):
    """Assemble the WA payload. world is 'sideros' (public) or 'astrolan'."""
    lore = k["lore"]

    # Mechanics: quick stats in the sidebar, full traits appended to content.
    sidebar = "[h3]At a Glance[/h3]\n" + "\n".join(
        f"[b]{lab}:[/b] {val}\n[i]{note}[/i]\n" for lab, val, note in k["stats"])

    mech = "\n\n[h2]Kindred Traits[/h2]\n" + "\n\n".join(
        f"[h4]{n}[/h4]\n[i]{t}[/i]\n{b}" for n, t, b in k["traits"])

    lifespan = ""
    for _n, _t, body in k["traits"]:
        m = re.search(r"roughly (\d+) years", body)
        if m:
            lifespan = f"Approximately {m.group(1)} years."
            break

    p = {
        "title": k["name"],
        "templateType": "species",
        "isDraft": True,
        "isSentient": True,
        "isIntelligent": True,
        "subheading": k["also"],
        "excerpt": _excerpt(lore[0]) if lore else "",
        # Paragraph 1 IS the overview -- it goes in content only.
        # Paragraphs 2+ are distributed to template fields below, so
        # joining all of them here would render every paragraph twice.
        "content": (lore[0] if lore else "") + mech,
        "sidebarcontent": sidebar,
        "geographicalOrigin": k["home"],
        "ancenstry": k["essence"],
        "lifespan": lifespan,
        "tags": "kindred,playable,sideros",
        "state": "public" if world == "sideros" else "private",
    }
    # Distribute paragraphs 2+ to template fields. Anything that matches no
    # rule is appended to the body -- an earlier version used setdefault here,
    # which silently dropped every unmatched paragraph after the first.
    leftover = []
    for para in lore[1:]:
        if "Solar Chivalry" in para or "founded by" in para:
            p["majorOrganizations"] = para
        elif "cosmic lineage" in para or "Aether" in para:
            p["culture"] = para
        elif "interspeciesRelations" not in p:
            p["interspeciesRelations"] = para
        else:
            leftover.append(para)
    if leftover:
        p["content"] = (lore[0] if lore else "") + "\n\n" + \
                       "\n\n".join(leftover) + p["content"][len(lore[0] if lore else ""):]

    if world == "sideros":
        for clause in GM_ONLY_CLAUSES:
            for key, val in list(p.items()):
                if isinstance(val, str) and clause in val:
                    p[key] = val.replace(clause, "")
    return p


# ------------------------------------------------------------------ gate
def gate(payload, world):
    """Block hard secrets, but ONLY when publishing to the public world."""
    if world != "sideros":
        return []
    hits = []
    for key, val in payload.items():
        if not isinstance(val, str):
            continue
        for s in HARD_SECRETS:
            if s.lower() in val.lower():
                i = val.lower().find(s.lower())
                hits.append((key, s, val[max(0, i - 60): i + 70]))
    return hits


# ------------------------------------------------------------------ push
def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(st):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, indent=2))


def _explain(exc):
    """Pull the one useful sentence out of WA's SQL error dump."""
    txt = str(exc)
    m = re.search(r"SQLSTATE\[\w+\]: ([^']+?)(?: at row|\\n)", txt)
    if m:
        return m.group(1).strip()
    m = re.search(r"'summary': '([^']{0,180})", txt)
    return m.group(1) if m else txt[:300]


def sync_one(name, world, world_id, cat_id, client, st, push):
    """Build, gate and (optionally) push one Kindred. Returns True on success."""
    payload = build(extract(name), world)
    payload["world"] = {"id": world_id}
    if cat_id:
        payload["category"] = {"id": cat_id}

    hits = gate(payload, world)
    filled = len([x for x, v in payload.items() if v not in ("", None)])
    if hits:
        print(f"  {name:16} BLOCKED -- {[h[1] for h in hits]}")
        for key, sec, ctx in hits:
            print(f"      [{sec}] in '{key}'\n        …{ctx}…")
        return False

    if not push:
        print(f"  {name:16} clean, {filled} fields  (dry run)")
        return True

    key = f"{world}:{name}"
    # WA rejects a PATCH that includes fields fixed at creation time.
    # templateType is the one it names; world is dropped for the same reason
    # (an article cannot be moved between worlds by update).
    IMMUTABLE = ("templateType", "world")
    try:
        if key in st:
            update = {k: v for k, v in payload.items() if k not in IMMUTABLE}
            client.article.patch(st[key], update)
            print(f"  {name:16} UPDATED  {st[key]}")
        else:
            res = client.article.put(payload)
            aid = res.get("id") or res.get("entity", {}).get("id")
            st[key] = aid
            save_state(st)
            print(f"  {name:16} CREATED  {aid}")
        return True
    except Exception as exc:                              # noqa: BLE001
        print(f"  {name:16} FAILED -- {_explain(exc)}", file=sys.stderr)
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kindred")
    ap.add_argument("--all", action="store_true",
                    help="every Kindred in the compendium")
    ap.add_argument("--world", choices=["sideros", "astrolan"], default="sideros")
    ap.add_argument("--push", action="store_true", help="actually write")
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args()

    if args.list:
        for n, _ in PANELS:
            print(f"  {n}")
        return
    if not args.kindred and not args.all:
        ap.error("--kindred or --all is required (or use --list)")

    try:
        cfg = load_config()
    except ConfigError as exc:
        sys.exit(f"CONFIG ERROR\n{exc}")

    world_id = cfg.world_sideros if args.world == "sideros" else cfg.world_astrolan
    if not world_id:
        sys.exit(f"WA_WORLD_{args.world.upper()} is not set in .env")
    if args.world == "sideros":
        assert_not_astrolan(cfg, world_id)

    cat_id = None
    if CATMAP.exists():
        cat_id = json.loads(CATMAP.read_text()).get(args.world, {}).get("kindred")
        print(f"Category: {'Kindreds ' + cat_id[:8] + '…' if cat_id else 'UNMAPPED -- will land at root'}")
    else:
        print(f"WARNING: {CATMAP} missing -- run wa_categories.py --write")

    client = None
    if args.push:
        from pywaclient.api import BoromirApiClient
        client = BoromirApiClient(
            "sideros-canon-sync", "https://github.com/mckamw99/sideros",
            "0.1.0", cfg.application_key, cfg.auth_token)

    st = load_state()
    names = [n for n, _ in PANELS] if args.all else [args.kindred]
    print(f"\n{'PUSH' if args.push else 'DRY RUN'} -> {args.world}  ({len(names)} article(s))")

    ok = sum(sync_one(n, args.world, world_id, cat_id, client, st, args.push)
             for n in names)
    print(f"\n{ok}/{len(names)} succeeded")
    if not args.push:
        print("Re-run with --push to write.")
    sys.exit(0 if ok == len(names) else 1)


if __name__ == "__main__":
    main()
