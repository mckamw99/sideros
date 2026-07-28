#!/usr/bin/env python3
"""
Sideros canon + GM-secret scanner.

Usage:
    python3 canon_scan.py <directory> [--ext .html .md .json .txt]

Two independent scan sets:
  DEPRECATED  - banned/retired vocabulary that must be swept before publication
  HARD_SECRET - GM-only content that must NEVER appear in player-facing material

Exit code 1 if any HARD_SECRET hit is found (fail the push).
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------- scan sets

# (label, regex, note)
DEPRECATED = [
    ("Aetheric Channels (resource)",
     r"\bAetheric\s+Channels?\b",
     "-> Aetheric Threads"),
    ("channel/channeling (magic verb)",
     r"\bchannel(?:s|ed|ing|er|ers)?\b",
     "-> weave / Weaving / Weaver  [check for geographic/CSS false positives]"),
    ("Channeler",
     r"\bChanneler(?:s)?\b",
     "-> Weaver"),
    ("Comet-Mage",
     r"\bComet[-\s]Mage(?:s)?\b",
     "-> Comet-Magus (sing.) / Comet-Magi (pl.)"),
    ("Concordance (GM context)",
     r"\bConcordance\b",
     "-> Game Master"),
    ("Moana-kin",
     r"\bMoana[-\s]?kin\b",
     "-> Waka-kin"),
    ("Orsha-Anu",
     r"\bOrsha[-\s]?Anu\b",
     "-> Orun-Ayé"),
    ("Zargon (WotC IP)",
     r"\bZargon\b",
     "-> Aethar / The Serpent Bearer"),
    ("Morcar (Hasbro IP)",
     r"\bMorcar\b",
     "-> Aethar / The Serpent Bearer"),
    ("spell slot",
     r"\bspell\s+slots?\b",
     "-> Aetheric Threads"),
    ("cast a spell",
     r"\bcast(?:s|ing)?\s+(?:a\s+)?spell",
     "-> Weave a Working"),
    ("Proficiency Bonus",
     r"\bProficiency\s+Bonus\b",
     "-> Mastery Bonus"),
    ("Death Save",
     r"\bDeath\s+Saves?\b",
     "-> Loom Tests"),
    # textile imagery - Threads are starlight, never fibre
    ("textile imagery",
     r"\b(?:cloth|fabric|tapestr(?:y|ies)|spun|spinning|fibre|fiber|yarn|loomed\s+cloth|warp\s+and\s+weft)\b",
     "Threads are lines of starlight, NOT fibre - rewrite in celestial terms"),
    # deprecated Fated Bond proximity scale 10/7/5/3
    ("deprecated Bond proximity (10/7/5/3)",
     r"\b(?:within\s+)?10\s+Fate\s+points?\b|\b(?:within\s+)?7\s+Fate\s+points?\b",
     "canonical scale is Paired 5 / Triad 4 / Quad 2 / Quint 1"),
]

HARD_SECRET = [
    ("the Quint Bond", r"\bthe\s+Quint\s+Bond\b"),
    ("all five members", r"\ball\s+five\s+members\b"),
    ("fully acknowledged", r"\bfully\s+acknowledged\b"),
    ("cluster members", r"\bcluster\s+members\b"),
    ("Five Who Remember", r"\bFive\s+Who\s+Remember\b"),
    ("Fang of the Whisper", r"\bFang\s+of\s+the\s+Whisper\b"),
    ("Antarctos", r"\bAntarctos\b"),
    ("Serath", r"\bSerath\b"),
    ("Drava Nullsong", r"\bDrava(?:\s+Nullsong)?\b"),
    ("Resonant Binding", r"\bResonant\s+Binding\b"),
    ("Quint Bond Adjacent", r"\bQuint\s+Bond\s+Adjacent\b"),
    ("Four Architects", r"\bFour\s+Architects\b"),
    ("Scion Shift", r"\bScion\s+Shift\b"),
    ("Fate 55-58 range", r"\bFate\s*(?:#|No\.?|Number)?\s*5[5-8]\b|\b55\s*[-–]\s*58\b"),
    ("Inti-kora", r"\bInti[-\s]?kora\b"),
    ("Asha-Wing", r"\bAsha[-\s]?Wing\b"),
    ("Hinerangi", r"\bHinerangi\b"),
    ("Matuā-kore", r"\bMatu[aā][-\s]?kore\b"),
]

DEFAULT_EXTS = [".html", ".htm", ".md", ".json", ".txt", ".jsx", ".js"]

# ---------------------------------------------------------------- machinery

TAG_RE = re.compile(r"<[^>]+>")
SCRIPT_STYLE_RE = re.compile(
    r"<(script|style)\b.*?</\1>", re.DOTALL | re.IGNORECASE)


def strip_markup(text, path):
    """Remove script/style blocks and tags so we scan prose, not code."""
    if path.suffix.lower() in (".html", ".htm"):
        text = SCRIPT_STYLE_RE.sub(" ", text)
        text = TAG_RE.sub(" ", text)
    return text


def scan_file(path, patterns):
    """Return {label: [(lineno, context, note)]} for one file."""
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        print(f"  !! could not read {path}: {exc}", file=sys.stderr)
        return {}

    cleaned = strip_markup(raw, path)
    hits = defaultdict(list)

    for entry in patterns:
        label, pattern = entry[0], entry[1]
        note = entry[2] if len(entry) > 2 else ""
        rx = re.compile(pattern, re.IGNORECASE)
        for lineno, line in enumerate(cleaned.splitlines(), 1):
            m = rx.search(line)
            if m:
                start = max(0, m.start() - 60)
                end = min(len(line), m.end() + 60)
                context = " ".join(line[start:end].split())
                hits[label].append((lineno, context, note))
    return hits


def report(root, exts):
    files = sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.suffix.lower() in exts
    )
    print(f"Scanning {len(files)} files under {root}\n")

    dep_total = 0
    sec_total = 0
    dep_by_label = defaultdict(int)

    print("=" * 72)
    print("HARD SECRET SCAN  (any hit blocks a player-facing push)")
    print("=" * 72)
    for f in files:
        hits = scan_file(f, HARD_SECRET)
        if hits:
            print(f"\n### {f.relative_to(root)}")
            for label, occurrences in hits.items():
                sec_total += len(occurrences)
                print(f"  [{label}]  x{len(occurrences)}")
                for lineno, ctx, _ in occurrences[:3]:
                    print(f"     L{lineno}: ...{ctx}...")
                if len(occurrences) > 3:
                    print(f"     ... +{len(occurrences) - 3} more")
    if sec_total == 0:
        print("\n  CLEAN - zero hard-secret hits.")

    print("\n" + "=" * 72)
    print("DEPRECATED VOCABULARY SCAN")
    print("=" * 72)
    for f in files:
        hits = scan_file(f, DEPRECATED)
        if hits:
            print(f"\n### {f.relative_to(root)}")
            for label, occurrences in hits.items():
                dep_total += len(occurrences)
                dep_by_label[label] += len(occurrences)
                note = occurrences[0][2]
                print(f"  [{label}]  x{len(occurrences)}   {note}")
                for lineno, ctx, _ in occurrences[:2]:
                    print(f"     L{lineno}: ...{ctx}...")
                if len(occurrences) > 2:
                    print(f"     ... +{len(occurrences) - 2} more")
    if dep_total == 0:
        print("\n  CLEAN - zero deprecated-term hits.")

    print("\n" + "=" * 72)
    print("SUMMARY BY TERM")
    print("=" * 72)
    for label, count in sorted(dep_by_label.items(), key=lambda kv: -kv[1]):
        print(f"  {count:5d}  {label}")
    print(f"\n  Deprecated hits : {dep_total}")
    print(f"  Hard-secret hits: {sec_total}")

    return sec_total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--ext", nargs="*", default=DEFAULT_EXTS)
    args = ap.parse_args()

    root = Path(args.directory).resolve()
    if not root.is_dir():
        sys.exit(f"Not a directory: {root}")

    exts = {e if e.startswith(".") else "." + e for e in args.ext}
    secrets = report(root, exts)
    sys.exit(1 if secrets else 0)


if __name__ == "__main__":
    main()
