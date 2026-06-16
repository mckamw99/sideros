#!/usr/bin/env python3
"""
convert_kindreds.py
-------------------
Extracts each Kindred from the canon HTML compendium files and emits a
World Anvil-ready article (YAML front-matter + BBCode body) per Kindred.

Handles BOTH source schemas:
  - Vol I & II : .lore-para / .trait-card > .tc-name/.tc-type/.tc-body / .sc-* stats
  - Vol III    : .lore / .trait > .tn/.tt/.tb / .stat-* stats

Source pages live in /mnt/project (read-only). Output goes to
worldanvil/articles/kindreds/. Re-runnable and idempotent.

NOTE: source text is preserved verbatim. The pending "Concordance" -> "Game Master"
canon decision is NOT applied here; sweep later once Matt confirms.
"""
import os, re, json
from bs4 import BeautifulSoup, NavigableString, Tag

SRC = [
    "/mnt/project/sideros_kindred_compendium.html",  # Vol I  (6)
    "/mnt/project/sideros_kindred_vol2.html",        # Vol II (8)
    "/mnt/project/sideros_kindred_vol3.html",        # Vol III(6)
]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "articles", "kindreds")
os.makedirs(OUT, exist_ok=True)

def inline_to_bbcode(node):
    """Convert an element's children to BBCode, mapping <strong>/<b>->[b], <em>/<i>->[i]."""
    out = []
    for c in node.children:
        if isinstance(c, NavigableString):
            out.append(str(c))
        elif isinstance(c, Tag):
            inner = inline_to_bbcode(c)
            if c.name in ("strong", "b"):
                out.append(f"[b]{inner}[/b]")
            elif c.name in ("em", "i"):
                out.append(f"[i]{inner}[/i]")
            elif c.name == "br":
                out.append(" ")
            else:
                out.append(inner)
    return re.sub(r"[ \t]+", " ", "".join(out)).strip()

def slug(name):
    s = re.sub(r"^the\s+", "", name.strip(), flags=re.I)
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def get_text(panel, sel):
    el = panel.select_one(sel)
    return el.get_text(" ", strip=True) if el else None

def extract_panel(panel):
    name_el = panel.select_one(".kh-name")
    if not name_el:
        return None
    name = re.sub(r"^The\s+", "", name_el.get_text(strip=True))
    also = get_text(panel, ".kh-also")
    if also:
        also = re.sub(r"^Also called:\s*", "", also, flags=re.I).strip()
    home = get_text(panel, ".kh-home")
    essence = get_text(panel, ".kh-essence")
    tags = [t.get_text(strip=True) for t in panel.select(".kh-tag")]

    # lore paragraphs (both schemas)
    lore = [inline_to_bbcode(p) for p in panel.select(".lore-para, p.lore")]

    # traits (both schemas)
    traits = []
    for card in panel.select(".trait-card, .trait"):
        tn = card.select_one(".tc-name, .tn")
        tt = card.select_one(".tc-type, .tt")
        tb = card.select_one(".tc-body, .tb")
        if tn and tb:
            traits.append((
                tn.get_text(strip=True),
                tt.get_text(strip=True) if tt else "",
                inline_to_bbcode(tb),
            ))

    # stat cells (both schemas)
    stats = []
    for cell in panel.select(".stat-cell, .stat"):
        lbl = cell.select_one(".sc-label, .stat-label")
        val = cell.select_one(".sc-val, .stat-val")
        note = cell.select_one(".sc-note, .stat-note")
        if lbl and val:
            stats.append((
                lbl.get_text(" ", strip=True),
                val.get_text(" ", strip=True),
                note.get_text(" ", strip=True) if note else "",
            ))

    # zodiac resonance table (Vol I/II only)
    zrows = []
    tbl = panel.select_one("table.kz-table")
    if tbl:
        for tr in tbl.select("tr"):
            cells = tr.find_all(["td", "th"])
            if len(cells) >= 3 and cells[0].name == "td":
                zrows.append(tuple(c.get_text(" ", strip=True) for c in cells[:3]))

    play = get_text(panel, ".pb-text")

    return dict(name=name, also=also, home=home, essence=essence, tags=tags,
                lore=lore, traits=traits, stats=stats, zrows=zrows, play=play)

def to_article(k):
    b = []
    # Intro / overview line
    facts = []
    if k["home"]:    facts.append(f"[b]Homeland:[/b] {k['home']}")
    if k["essence"]: facts.append(f"[b]Primal Essence:[/b] {k['essence']}")
    if k["also"]:    facts.append(f"[b]Also called:[/b] {k['also']}")
    if k["tags"]:    facts.append(f"[b]Aspects:[/b] {', '.join(k['tags'])}")
    if facts:
        b.append("\n".join(facts))
    # Lore
    if k["lore"]:
        b.append("[h2]Lore[/h2]\n" + "\n\n".join(k["lore"]))
    # Traits
    if k["traits"]:
        tlines = []
        for tn, tt, tb in k["traits"]:
            head = f"[b]{tn}[/b]" + (f" — [i]{tt}[/i]" if tt else "")
            tlines.append(head + "\n" + tb)
        b.append("[h2]Kindred Traits[/h2]\n" + "\n\n".join(tlines))
    # Stats
    if k["stats"]:
        slines = [f"[li][b]{l}:[/b] {v}" + (f" — {n}" if n else "") + "[/li]"
                  for l, v, n in k["stats"]]
        b.append("[h2]Resonance Attributes[/h2]\n[ul]\n" + "\n".join(slines) + "\n[/ul]")
    # Zodiac resonance
    if k["zrows"]:
        zlines = [f"[li][b]{sign} — {rn}:[/b] {eff}[/li]" for sign, rn, eff in k["zrows"]]
        b.append("[h2]Kindred–Zodiac Resonance (Selected Signs)[/h2]\n[ul]\n"
                 + "\n".join(zlines) + "\n[/ul]")
    # Play guidance
    if k["play"]:
        b.append("[h2]Playing this Kindred[/h2]\n" + k["play"])
    return "\n\n".join(b)

def front_matter(k, wave=1):
    title = k["name"]
    return (
        "---\n"
        f"title: {title}\n"
        "template: species\n"
        "category: Kindreds\n"
        "privacy: public\n"
        f"wave: {wave}\n"
        f"slug: {slug(k['name'])}\n"
        "tags: [kindred, species, player-facing]\n"
        "status: drafted\n"
        "source: sideros_kindred_compendium (vols I-III)\n"
        "---\n\n"
    )

def main():
    manifest = []
    order = 0
    for path in SRC:
        soup = BeautifulSoup(open(path).read(), "html.parser")
        for panel in soup.select("div.panel"):
            k = extract_panel(panel)
            if not k or not k["lore"] and not k["traits"]:
                continue  # skip intro/non-kindred panels
            order += 1
            fname = f"{order:02d}-{slug(k['name'])}.md"
            with open(os.path.join(OUT, fname), "w") as f:
                f.write(front_matter(k) + to_article(k) + "\n")
            manifest.append(dict(
                file=f"articles/kindreds/{fname}",
                title=k["name"], template="species", category="Kindreds",
                privacy="public", wave=1, status="drafted",
            ))
            print(f"  wrote {fname:32s} traits={len(k['traits'])} lore={len(k['lore'])}")
    print(f"\nTotal Kindred articles: {len(manifest)}")
    return manifest

if __name__ == "__main__":
    main()
