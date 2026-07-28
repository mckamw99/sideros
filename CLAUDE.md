# CLAUDE.md — Start Here

*If you are a future Claude (or any AI) picking up this repository: read this file first, then read [`context/sideros_handoff_master.md`](context/sideros_handoff_master.md) for the full canon. This file orients you; the handoff master is the authoritative source of truth.*

**Last updated: 27 July 2026.**

---

## ⚠ Repository visibility

**This repository is currently PUBLIC.** Earlier versions of this file instructed
that it be kept private because it contains GM material. That instruction is no
longer accurate and should not be acted on as written.

Matt has made an informed decision to keep it public for now. What that means in
practice:

- `context/sideros_handoff_master.md` is publicly readable and contains the full
  GM layer — the Ashen Coil Triad, named Quint Bond members, the Fang of the
  Whisper network, Antarctos.
- Do not treat "it's in the repo" as evidence that something is player-safe.
  The player/GM boundary below still applies to every artifact you produce.
- If the repo is later set to private, remove the auto-fetch instruction from
  the Project settings — it will otherwise fail on every new chat.

---

## What Sideros is

**Sideros** is an original tabletop RPG (5e-SRD-compatible) set in the world of **Astrolan**.
- **Sideros** = the common, everyday name everyone uses.
- **Astrolan** = the formal/archaic name, used only in ancient texts, scholarly contexts, and Comet-Magi documentation.

The cosmology is built on the zodiac: 13 signs (12 + **Ophiuchus**), 13 Legendary Beasts, 13 civilizations, 20 Kindreds, 18 Paths, **27 player-selectable Origins** (plus GM-assigned).

**Creator:** Matt (Dr. Matthew McKay) is the sole creator and makes every definitive creative decision. Your role is collaborative worldbuilding partner, document builder, and **consistency auditor**. You propose and execute; Matt decides.

## How Matt works (operating manual)

- Pattern: Matt shares a concept or direction → you propose an integration approach → he confirms ("yes, do it") → you execute → you summarize what changed.
- For substantial additions, **propose first and wait for "yes"** before building.
- Matt reads on **mobile** — keep output structured and concise; use tables when they add clarity; don't over-format.
- Approvals are often incremental (frequently just "Yes").
- Your value is as organizer, stress-tester, and consistency auditor. **Flag contradictions; offer options when he's torn; don't silently pick a side on canon conflicts.**
- Matt works on **Windows / PowerShell**, no Git installed as of July 2026. Deliver
  files for download rather than assuming a commit is possible.

## Repository map

| Path | What it is |
|---|---|
| `index.html` | Styled hub linking every page + both guide editions |
| `pages/` | 31 player- and GM-facing reference pages (the modular canon) |
| `guide/` | The Player's Comprehensive Guide — printable binder `.docx` (current + v16 binder) |
| **`context/sideros_handoff_master.md`** | **The authoritative continuity file. Read this for full canon.** |
| `context/sideros_handoff_supplement.md` | Deep GM / per-civilization / Coil detail |
| `context/sideros_aetheric_artifacts_catalogue.md` | Magic-item / artifact catalogue |
| `context/archive/` | Superseded handoffs kept for lineage |
| `tools/` | World Anvil sync tooling (see below) |
| `assets/maps/Siderosv11.jpg` | **Labelled world map — GM reference. Never player-facing.** |
| `assets/portraits/` | Canonical Kindred portraits (visual canon reference) |

## Canonical terminology — ALWAYS enforce

Magic use is **Weaving**. A practitioner **weaves** a **Working** (never "casts a spell"). The resource is **Aetheric Threads** — casually "Threads", tiered 1st–9th, drawn from the Aether on Deep Attunement.

**Retired vocabulary (target: 0 instances).** "Aetheric Channels" / "Channels" as the resource; the verb "channel / channeling"; "Channeler". These were swept to zero across all 31 pages on 27 July 2026. The ordinary English conduit sense ("diplomatic channels", the Elethorn grid's physical fire channels) is *not* banned — only the magic resource and the magic verb.

**Cosmology metaphor.** A Thread is a line of starlight, as on a star chart. The Loom is the cosmic engine drawing constellations. Weaving and Fate are the same drawn starlight at two scales. **No textile imagery** — no cloth, fabric, tapestry, spun, fiber, or strand-as-fiber.

| Never | Always |
|---|---|
| Proficiency Bonus | **Mastery Bonus** |
| Death Saves | **Loom Tests** |
| HP / Hit Points | **Vitality** |
| AC / Armour Class | **Guard Rating** |
| Race / Class / Background | **Kindred / Path / Origin** |
| Level | **Depth** |
| Skill / DC | **Discipline / Threshold** |
| Attack / Save / Check | **Strike / Warding / Active Resonance** |
| Advantage / Disadvantage | **Resonant Fortune / Resonant Discord** |
| Initiative / round | **Pulse Order / Pulse** |
| Long Rest / Short Rest | **Deep / Brief Attunement** |
| Channel Divinity | **Oathlight** |

- Attributes: **FOR, SWI, END, ATT, ACU, RES** (Force, Swiftness, Endurance, Attunement, Acuity, Resonance).
- Currency: Marks — **cm / sm / gm / pm** (10:1 each step; 50 Marks = 1 lb). No electrum.
- **Comet-Magus** = singular / the Path; **Comet-Magi** = plural / the order. "Comet-Mage" is deprecated.
- **Game Master** — never "Concordance" (deprecated v18, swept to zero July 2026).
- **Waka-kin** — never "Moana-kin". Waka Reaches; Ara Waka navigation.
- **Orun-Ayé** — canonical Ashélands name, matches the commissioned map. "Orsha-Anu" is deprecated.
- Primary villain: **AETHAR** (personal name) / **THE SERPENT BEARER** (title). Never "Zargon" (WotC) or "Morcar" (Hasbro). Aethar is a former 12th Circle Comet-Magus of the Shifting Horizons Conclave.
- **Oathlight** — the Oathed Vanguard's Oath resource, replacing the SRD's "Channel Divinity". Oaths in Sideros are sworn *before the Loom*, not before gods; flavour framing is **the Loom's Regard**.

### Fated Bond proximities (canonical)

Paired ≤5 Fate points · Triad ≤4 · Quad ≤2 · Quint ≤1.
The deprecated 10/7/5/3 scale must never be used.

**Nebula Thread** (scholarly) / **red thread** (common): a rare exception allowing a Triad to close across one un-drawn edge when both un-drawn souls are fated to a shared third. Ratified; propagation to the Fated Bond page, lexicon, codex, Player's Guide and World Anvil still outstanding.

## The player ↔ GM secrets boundary (HARD RULES)

The following must appear in **0 instances** of any player-facing output:

- **Named Quint Bond members** (Inti-kora, Asha-Wing, Hinerangi, Matuā-kore) — reference anonymously ("a confirmed Resonant Binding component holder").
- **The Scion Shift system** — players are never told it exists.
- The **Night of Kallos** truth, the **Arrow's identity** as the Fourth Architect, **Serath's withholding**, and the Maw endgame specifics.
- **The Ashen Coil Triad** — Aethar (α), Serath (Ω), Drava Nullsong (β).

Note: the bond-tier words Paired / Triad / Quad / Quint are **player-safe mechanics**. The secret is the definite article "*the* Quint Bond", "all five members", and the specific Fate range.

GM-only material lives mainly in `context/` and in three `pages/` files: `concordance_tools`, `npc_essence`, `bonds_npcs`.

**Images are not covered by text scans.** Words baked into an image are invisible to every keyword sweep in this repo. Review art visually before any player-facing use. Genuine Kindred portraits are 532×784; anything landscape in the portrait set is a map or banner and should be treated as suspect.

## World Anvil (live as of 27 July 2026)

Two worlds, one-way sync — **local files are canon, World Anvil is a render target.** WA has no version history (the feature has been formally declined by their team), so nothing should be authored only in WA.

| World | UUID | Use |
|---|---|---|
| Sideros of the Celestial Concord | `95873c91-67e4-4014-84d2-c283f060acbc` | Public, player-facing |
| Astrolan | `81ead1b9-bf47-4975-8505-137bfb05a9ba` | Private, GM-only |

Tooling in `tools/`: `wa_config.py`, `wa_preflight.py`, `wa_canon_sync.py`, `wa_categories.py`, `wa_portraits.py`, `wa_probe.py`. Credentials live in `~/.config/sideros/.env` and must never enter a chat or this repo.

Notes learned the hard way: WA's `excerpt` column is 255 chars and rejects overruns at the database layer with a raw SQL error; `templateType` and `world` are immutable after creation and must be stripped from PATCH payloads; the Species template has ~61 usable fields with inconsistent casing (`growthrate`, `socialstructure`) and two misspellings in WA's own schema (`ancenstry`, `relationshipsIdeals`).

Live: 6 of 20 Kindreds in Sideros, filed under the Kindreds category. Remaining 14 are in `sideros_kindred_vol2.html` and `vol3.html`, which use different class schemes and need their own parsers.

## Open items

1. **Number 56** — the open fifth Quint Bond slot; resolves at character creation. Their zodiac sign sets the fifth Resonant Binding component.
2. **Opening campaign hook** — undecided.
3. **Kindred portrait filenames are unreliable.** At least one (`BeastKin.jpg`) is a world map, not a portrait; `worldmap.jpg` is a portrait. Matt is regenerating the set. Do not trust filename→Kindred mapping without visual confirmation.
4. **Kuri and Centaur-Kin have no portrait art.**
5. **Lexicon repair:** `pages/sideros_aetheric_lexicon.html` contains a sentence broken by an earlier find-replace — the D&D term and its Sideros replacement are the same word. Intended text is almost certainly *("spell slot" implies a container) … ("Aetheric Thread" implies flow and resonance)*.
6. **Nebula Thread propagation** to Fated Bond page, lexicon, codex, Player's Guide, World Anvil.
7. **Player's Guide TOC** — verify back-matter page numbers after PDF export.
8. **World Anvil category cleanup** — 43 categories exist, several overlapping duplicates from a template set.
9. **Undetailed-but-named:** Soul Harvesting, Grand Concord of Merchants, Loom of Fate as an institutional body, the Mycelial Brood (Arc 2).

## Canon-check (run after major changes)

Deprecated-term sweep — all of these must be 0 in player-facing output:
`Concordance`, `Comet-Mage`, `Moana-kin`, `Orsha-Anu`, `Zargon`, `Morcar`, `Aetheric Channel(s)`, `Channeler`, `Channel Divinity`, `channel`/`channeling` as a magic verb, `Copper Coin (cp)`, `Platinum Crown (pc)`, and the named Quint members.

`tools/canon_scan.py` runs the full set against a directory.

---

*The Loom weaves fate; practitioners weave the Aether — same act at different scales.*
*© 2026 Dr. Matthew McKay. All Rights Reserved.*
