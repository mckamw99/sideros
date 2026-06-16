# SIDEROS PROJECT HANDOFF — v17 Continuity Prompt

*Use this prompt at the start of a new chat session to bring Claude fully up to speed on the Sideros TTRPG project. Paste this in as the first message, then provide any new tasks.*

---

## PROJECT IDENTITY

I'm **Matt**, building **Sideros**, an original TTRPG system set in the world of **Astrolan**.

- **System name:** Sideros
- **World name:** Sideros (common, day-to-day use) / Astrolan (formal, archaic — used in ancient texts and Comet-Magi contexts)
- **Compatibility:** 5e SRD–compatible; mechanical scaffolding from D&D 5e, with all canonical Sideros terminology replacing 5e terms throughout
- **Scope:** Player-facing character creation guide (printable binder format), bestiary, worldbuilding canon, AI art assets, Midjourney/Gemini production pipeline
- **Your role:** Collaborative worldbuilding partner, document builder, consistency auditor. I make definitive creative decisions; you develop, organize, stress-test, and flag contradictions.

---

## CURRENT DOCUMENT STATE

The primary deliverable is the **Sideros Player's Comprehensive Guide** (v16 colophon, ongoing).

- **Current length:** ~341 pages, ~4.32 MB docx
- **Format:** US Letter, 1.25" binder margin (left), single-sided print
- **Output file:** `/mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx`
- **Source file:** `/home/claude/sideros_comprehensive_guide.docx` (text/markdown source, ~5800 lines)
- **Build script:** `/home/claude/build_binder.js` (Node.js docx library; titlePage: true; first-page empty Header; US Letter 12240×15840 DXA)
- **Preview PDF:** `/home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf`
- **Kindred portraits:** `/home/claude/images/*.png` (20 kindred portraits)

**Build process:**
```bash
cd /home/claude && node build_binder.js
soffice --headless --convert-to pdf /mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx --outdir /home/claude/preview
pdfinfo /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf | grep Pages
```

**Verified TOC anchors (must be re-verified after every addition):**
- RULES REFERENCE: p170
- WORLD REFERENCE: p206
- APPENDIX: p261

After any insertion that shifts pages, update the TOC line at the top of the source file. Use `pdftotext -layout` and Python to find actual section pages.

---

## CRITICAL CANONICAL TERMINOLOGY (always enforce)

### Magic system
- Magic use = **Weaving** (NEVER "channeling" — WoT/Jordan IP risk)
- Practitioners **Weave** a **Working** (NEVER "cast a spell" in mechanical context)
- Resource = **Aetheric Channels** (opened, not channeled)
- **Weaving Attribute** (NEVER "Channeling Attribute")
- **Weave Recovery** (NEVER "Channel Recovery")
- **Weaving Risks** (Kallos-Sworn vulnerabilities)
- **Weave-capable** = can use magic

### Core mechanics
- **Mastery Bonus** (NEVER "Proficiency Bonus")
- **Loom Tests** (NEVER "Death Saves")
- **Threshold** preferred over **DC** (DC still used in back-matter quick-reference)
- **Game Master** (NEVER "Concordance" in player-facing — Concordance was a deprecated term)
- **Active Resonance** (NEVER "ability check" / "skill check")
- **Warding Resonance** (NEVER "saving throw")
- **Strike Resonance** (NEVER "attack roll")
- **Resonant Fortune / Resonant Discord** (NEVER "advantage / disadvantage")
- **Vitality** (NEVER "HP")
- **Guard Rating** (NEVER "AC")
- **Vita Dice** (NEVER "Hit Dice")
- **Pulse Order** (NEVER "Initiative")
- **Deep Attunement** (NEVER "Long Rest")
- **Brief Attunement** (NEVER "Short Rest")
- **Kindred** (NEVER "race")
- **Path** (NEVER "class")
- **Origin** (NEVER "background")
- **Depth** (NEVER "level" for character progression — except Aetheric Depletion levels which is canonical)
- **Discipline** (NEVER "skill")

### Currency
- Standardized to **all Marks**: cm / sm / gm / pm
- Ratio: **10 cm = 1 sm; 10 sm = 1 gm; 10 gm = 1 pm**
- **50 Marks of any denomination = 1 lb** (carrying weight)
- Old "Copper Coin (cp)" and "Platinum Crown (pc)" terms are DEPRECATED
- No electrum in Sideros canon

### Primary villain
- **AETHAR** (personal name) / **THE SERPENT BEARER** (title)
- NEVER "Zargon" (WotC copyright) or "Morcar" (HeroQuest/Hasbro copyright)
- Aethar is a former **12th Circle Comet-Magus** of the Shifting Horizons Conclave
- Named for the Aether he betrayed

### Comet-Magi terminology (v16 canonical)
- **Comet-Magus** = singular practitioner / the Path
- **Comet-Magi** = plural / the order / institutional body
- "Comet-Mage" is DEPRECATED (v16+); 0 instances should exist in current guide

---

## FOUNDATIONAL VISION (RECENTLY ESTABLISHED — pages 3-5 of binder)

The opening of the guide now leads with four foundational vision sections before the mechanical introduction:

### 1. THE WARRING ZODIACS (cosmological foundation)
> Sideros is not a world with one pantheon of gods or a single truth about the stars. The laws of the cosmos are not universal; they are regional in nature. Each culture is a living testament to its zodiac, and their truths are fundamentally incompatible.

The Ashen Coil is the only faction that has stepped outside the warring zodiacs entirely. They are a force of cosmic heresy, not just political opposition.

### 2. THE FOUR SENSES (experiential foundation)
- **A Sense of Wonder** — diversity, every horizon a new truth
- **A Sense of Agency** — world on a knife's edge, individuals tip the scales
- **A Sense of Aspiration** — freedom to be anything, love anyone, find heroism in unexpected places
- **A Sense of Hope** — defiance against darkness; even in a sundered world, connection and courage forge a better future

### 3. GENRE
- Primary: **Epic High Fantasy**
- Sub-genres: **Mythic Fantasy** (mythologies are tangibly true), **Dark Fantasy / Cosmic Horror** (Soul Harvesting, void worship), **Political Intrigue** (Loom-of-Fate shadow wars, Grand Concord of Merchants)

### 4. TECHNOLOGY AND MAGIC
Iron Age / High Medieval baseline. *Why invent a crane when a mage can lift the stone?* Spectrum:
- **High End — Magi-Tech**: Jade Empire of Shen-lì (steam, clockwork, Gear-Forged, paper currency)
- **Master Craftsmanship**: Dunmarim (metallurgy, Aether-Dampening Ore work)
- **Arcane Science**: Comet-Magi of Argent Spire (magic as fundamental science, borders on super-science)
- **Low-Tech / High-Magic**: Tuathan, Ashélands, Mori-Ōkami Wolf-Shifters (enchanted wood, sacred herbs, spirit-blessed warriors)

---

## MAJOR CANON FACTS

### Cosmology
- **13 zodiac signs** (12 traditional + Ophiuchus). Ophiuchus has no month — its sacred days are reckoned only by Comet-Magi and Kallos-Sworn (Six Days of Witness between Sagittarius and Capricorn months)
- **20 Kindreds**, **18 Paths**, **24 Origins**
- **16 Conditions**, ~14 damage types
- **Fate Numbers 1-100** (1d100)
- **Void-Touched Fate Numbers: 13, 66, 99**
- **13 Beasts** with **Three Aspects** each (Peripheral / Resonant / Apex Emanations)
- **Aquarius → Kelp-Weaver**; **Ophiuchus → Abyssal Leviathan** (also called Hollow Serpent)

### The 13 Apex Emanations (T4 Apex Fragments)
| Sign | Beast | Apex Fragment |
|---|---|---|
| ♈ Aries | Ashen Ram | First-Ember Ram horn-shaving |
| ♉ Taurus | Khalkotauros | Plain-Tread hoof-pressed stone |
| ♊ Gemini | Twin-Serpents | Twinned-scale pair (gold + void-black) |
| ♋ Cancer | Adamant Crab | Walking Island carapace flake |
| ♌ Leo | Nemean Lion | Solar Maned mane-hair |
| ♍ Virgo | Queen Bee | Celestial Honey (Bee-Priestess produced) |
| ♎ Libra | Great Roc | The Shed (primary feather) |
| ♏ Scorpio | Stygian Scorpion | Crystal-Stinger shard |
| ♐ Sagittarius | Star-Metal Stag | Waymarker antler tine |
| ♑ Capricorn | Sea-Goat | Both-Natured cave-pearl |
| ♒ Aquarius | Kelp-Weaver | Loom-Voice bioluminescent strand |
| ♓ Pisces | Twin Dream-Fish | Twin-Dream cenote-glass |
| ⛎ Ophiuchus | Abyssal Leviathan / Hollow Serpent | **Not harvestable** ("The Wound does not give. To take is to be taken.") |

### The Coil Triad
- **Aethar (α)** — Fate 13, Void-Touched. Pale, silver-white hair, void-black inverted-constellation Comet-Magi robes. Killed the Fourth Architect under the Hollow Serpent's influence; his memory of the act was altered — he does not know he did it.
- **Serath (Ω)** — Fate 16. Medium-dark, neat dark hair, operational gear + Cartographer tools. Has identified 3 of 5 Quint Bond members, withheld from Aethar for ~6 weeks.
- **Drava Nullsong (β)** — Fate 19. Pale, silver-short hair, dark operational clothing. Runs the Fang of the Whisper network.

The Triad are surviving members of the original **Four Architects** who attempted the first Resonant Binding 4,000 years ago. Their leadership bond is an **inverted Fated Bond** — the first ever created, formed when catastrophic Bond severance corrupted Aethar's remaining connections.

### The Fourth Architect mystery (GM-only)
- The Arrow (Sagittarius Scion, embedded in Riven Soll's Quad Bond) IS the Fourth Architect, converted by the interrupted Resonant Binding's energy rather than truly dying.
- Neither the Arrow nor Aethar knows this.
- At campaign climax, when the Arrow's zodiac drive completes, the Fourth Architect returns with full memory of both lives.

### Aethar's Five Stages
1. Accelerate Void-Husk production across Kindred populations
2. Destabilise zodiac political blocs (Leonine succession crisis is Stage 2 in motion)
3. Seize the Crystalline Core beneath Argent Spire
4. Void the Loom itself
5. **(UNWRITTEN)** Prevent the Quint Bond from forming. Serath knows. Serath has identified 3 of 5 members and has not reported this to Aethar.

### The Quint Bond Prophecy — The Verse of Five
> *Five voices when the Wound speaks,*
> *Five threads drawn from the Twelve,*
> *Five bonds sealed by the Loom,*
> *Five gifts returning what was scattered.*
> *And in their gathering, the Serpent sleeps.*

Discovered in Pre-Fall fragments in the Resonant Archive substructure. Every Comet-Magi initiate learns it. Kallos-Sworn study it as operational scripture.

---

## CRITICAL PLAYER vs GM BOUNDARIES

These items appear in the GM-only sections but **must NEVER be named in player-facing material**:

### Quint Bond members (4 named, 1 unknown)
- **Inti-kora** (Sagittarius, Fate 55) — Star-Metal Antler Fragment carrier
- **Asha-Wing** (Libra, Fate 57) — Great Roc Feather carrier
- **Hinerangi** (Pisces, Fate 58) — Cenote Water carrier
- **Matuā-kore** (Scorpio, Fate 66 Void-Touched) — Stygian Crystal carrier
- **Quint Bond member #56** — IDENTITY PENDING (Game Master determines at campaign setup)

**These names must remain in 0 instances in the player-facing comprehensive guide.** Always reference them anonymously (e.g., "a confirmed Resonant Binding component holder") in player-visible content.

### Scion shift mechanic
- Scions shift when their zodiac drive completes
- Specific conditions for all 13 Scions are GM-only
- Players are never told the system exists

### Other GM-only canon
- The Hollow Serpent's specific influence pattern on Aethar
- The exact composition of Riven Soll's Quad Bond and the Arrow's identity
- Serath's withholding of intelligence from Aethar
- Stage 5 of Aethar's plan (the unwritten one)

---

## DOCUMENT STRUCTURE (CURRENT BINDER ORGANIZATION)

| Tab | Section | Pages | Contents |
|---|---|---|---|
| (front matter) | Foundational opening | 3-5 | Warring Zodiacs, Four Senses, Genre, Tech & Magic, Introduction |
| **Tab 1** | Character Creation | 6-58 | Rules Primer, Character Creation Steps I-IX, 20 Kindreds, 18 Paths, 24 Origins, Session Zero Guide |
| **Tab 2** | Path Depth Progression | 64-169 | All 18 Paths, Depths 1-20 with Callings |
| **Tab 3** | Rules Reference | 170-205 | Combat, Conditions, Zodiac Feats, Weaving, Fighting Styles, Cultural Combat Traditions, Aether-Dampening Ore, Working Mechanics |
| **Tab 3** | World Reference | 206-260 | Equipment (Simple/Martial/Cultural Weapons, Armor, Accessories, Anointed Weapons, Material Upgrades, Maintenance, Adventuring Gear, Equipment Packs, Aetheric Artifact Rarity), Mounts, Trinkets, Currency, Economy (Magical Materials, Trade Goods, Cultural Currency Customs, Banking, Black Market, Aetheric Obligation), Cost of Living, Food/Drink/Lodging, Services, Sideros Calendar, Primal Essence, Downtime, Campaign Tracking (with Verse of Five, Pacing 4 Acts, Fated Bond Acknowledgment Ritual) |
| **Tab 4** | Appendix | 261-290 | Disciplines Reference, General Feats, Adventuring Rules, Languages, Tool Proficiencies (with detail), 8 Sideros-Specific Tools |
| **Tab 4** | GM Toolkit | ~314+ | Cultural Name Tables (240 names), Faction NPC Templates (18 stat blocks), Random Encounter Tables (96 prompts), Failure-as-Progress Prompts (30), Player Handout Templates (15), Regional Soundscape Reference |
| **Tab 5** | Character Folio | ~292+ | 3-page character sheet mirroring D&D 5e structure with Sideros terminology |

---

## KEY ADDITIONS RECENTLY COMPLETED

### Mechanical infrastructure (most recent first)
- **Foundational vision opening** (Warring Zodiacs / Four Senses / Genre / Technology and Magic)
- **Economy overhaul** — fixed currency (cm/sm/gm/pm at 10:1), added Trade Goods (35 items), Cultural Currency Customs (13 cultures), Banking & Letters of Credit (6 institutions), Black Market & Coil Trade pricing, Aetheric Obligation as soft currency, 50 Marks = 1 lb carrying weight
- **Character Folio restructured** to 3-page format mirroring D&D 5e (Page 1 Play Sheet / Page 2 Identity & World / Page 3 Weaving) with full Sideros terminology
- **GM Toolkit** — 240 cultural names, 18 NPC stat block templates, 96 regional encounter prompts, 30 failure-as-progress prompts, 15 player handout templates, regional soundscape reference
- **Verse of Five (Quint Bond Prophecy)** formalized with 4 competing faction interpretations
- **Campaign Pacing — Four Acts** (Witnessing 1-12, Gathering 13-30, Binding 31-50, Sealing 51-80)
- **Fated Bond Acknowledgment Ritual** (4-step table-side ceremony)
- **Sideros Calendar** — 12 months + Days of Ophiuchus + 12 Major Festivals + 5 extra-day cultural observances
- **8 Sideros-Specific Tools** (Apex Fragment Containment Kit, Lead-Scale Detector Kit, Void-Sight Lens, Beast Resonance Tuner, Resonant Geode Calibrator, Bond Witness Seal Set, Pre-Fall Star Chart Kit, Aetheric Distillation Apparatus)
- **Fighting Styles unified** (8 total) + **8 Cultural Combat Traditions** (Solar Chivalry, Mori-Ōkami Bushidō, Sagittarian Mounted Archery, Te Kapo Cave-Fighting, Moana-kin Wave-Stance, Shen-lì Twin-Hook Mastery, Dunmar Underground Defense, Tuathan Cold-Iron Veil-Fighting)
- **Beast Emanation Materials** — 39 named materials (13 Beasts × 3 aspects)
- **Apex Fragment Reagents** (5 tiers T1-T5)
- **Three Aspects of the Beasts** framework
- **Anointed Weapons** (8 cultural smith upgrades)
- **Cultural Weapons** (12 cultures, 40+ weapons including ranged: Tao Whana, Khepri Throw-Stick, Eagle-Bow, Cave-Blowgun, Composite Bow, plus universal Javelin/Net/Bola)
- **Cultural Armor** (Yoroi, Ichcahuipilli, Linen-and-Scale, Woven Flax, Lamellar, Reinforced Leather, Hide-and-Iron, Tuathan Bronze)
- **Cultural Accessories** (8 functional items including Asha-Crystal Pendant, Beaded Ifá Cord, Star-Reading Bracer)
- **Material Upgrade Pricing** (Black Iron, Star-Metal, Sun-Kissed Adamas, Hearthwood Haft, Stygian-Edged, Tuathan Bronze, Obsidian-Edged)
- **Maintenance and Repair** (Pristine/Damaged/Broken states + environmental risks)
- **Adventuring Gear** (~70 itemized) + Cultural Gear Variants (22) + 10 Equipment Packs (7 standard + 3 Sideros + 4 cultural-specialty)
- **Aetheric Artifact Rarity** (6 tiers with Sideros examples per tier — Common to Apex-grade)
- **Food/Drink/Lodging** itemized + Regional Specialty Foods (24 items × 12 regions) + Regional Lodging Specialties (8 cultural)
- **Services & Hireling Rates** + Working Casting Services (cultural cheapest/most expensive per service)

---

## PENDING / OPEN ITEMS

These items were introduced (often in the foundational vision sections) but have not been mechanically formalized:

1. **Soul Harvesting** — named as the Coil's signature cosmic-horror practice. Not yet detailed mechanically. Worth a dedicated entry on what it does to victim and to world.
2. **Grand Concord of Merchants** — named as a faction conducting economic machinations. Not yet detailed. Could fit as a banking/trade institution alongside Silk Road Guild and Solar Treasury.
3. **Loom of Fate as institutional body** — the phrase "shadow wars conducted around the Loom of Fate" suggests institutions (Stellar Cartographer secret tradition, Kallos-Sworn) operating clandestinely around fate-readings. Could be formalized.
4. **Quint Bond member #56** — identity pending; will be determined at character creation by dice roll.
5. **Fifth Resonant Binding component** — corresponds to member #56's zodiac sign; pending.
6. **TOC sub-entry alignment** — major section markers (Rules Ref / World Ref / Appendix) are verified. Some sub-entries (INTRODUCTION p2, RULES PRIMER p6, etc.) are 2 pages off due to foundational vision insertion. Low priority navigation polish.

---

## WORKING STYLE / WORKFLOW PREFERENCES

### How Matt operates
- Iterative, wide-ranging conversations spanning mechanics, narrative, NPC development, rules clarifications
- Often shares vision/canon text and expects integration into the guide
- Pattern: shares concept → Claude proposes integration → "yes, do it" → Claude executes → Claude summarizes
- Will share fragmentary canon and trust Claude to integrate consistently
- Definitive on creative decisions; uses Claude as organizer, stress-tester, consistency auditor

### How Claude should respond
- **Mobile-friendly responses** (Matt reads on mobile frequently)
- Structured but not over-formatted; tables when they add clarity
- Brief acknowledgment → clear proposal → confirmation prompt → execute → summarize what changed
- For substantial additions: propose first, wait for "yes", then execute
- For canon questions / audits: present findings clearly, identify gaps, propose what to add
- **Always re-verify TOC after additions** (Rules Reference / World Reference / Appendix page numbers)
- **Always rebuild and PDF-preview after major changes** to catch rendering issues
- **Always verify in canon check after changes:** 0 deprecated terms (Comet-Mage, Concordance, Zargon, Morcar, old currency abbreviations), 0 named Quint Bond members in player-facing material

### Technical patterns
- str_replace for precise edits; create_file for new artifacts
- view file ranges to locate exact insertion points
- After str_replace, re-view if multiple edits needed (view output goes stale)
- Use python3 with pdftotext for canon verification
- pdftoppm for visual rendering check on critical pages

### Known gotchas
- **Python-docx splicing**: restrict element search to `el.tag == qn('w:p')` paragraph elements only; searching all body children matches table cell text
- **Node.js docx library source files**: ASCII-only strings; em-dashes, curly quotes, arrows, accented characters in literals cause silent parser errors
- **HeightRule.EXACT on TableRow** (value 13680 twips): produces full-page divider tables without trailing page-break; adding page break after EXACT-height table creates a blank page
- **Forward insertion** (iterating elements in order, inserting at `ref_pos + i`): preserves content sequence in docx splicing

---

## IMAGE PRODUCTION (separate workflow, less active currently)

- **Midjourney** (encounter/threat tone) with sref `https://s.mj.run/ZCWUP9V0TPo --style raw --stylize 200`
- **Gemini** (lore/peacetime tone)
- Midjourney Chrome tab: tabId 1910478369
- Batches of exactly 3 prompts via Chrome extension
- Persistent drift issues require explicit `--no` parameters:
  - Eldren: add "NOT elderly, ageless" + `--no old man, elderly, wrinkles, tattered, worn`
  - Wolf-Shifter: add "HUMAN FACE, human nose, human mouth" + `--no wolf face, muzzle, snout, werewolf`
  - Serpent-Kin: add "HUMAN FACE" + `--no scales on face, reptilian face, lizard`
  - Avian: persistent issue; use "HUMAN FACE" but MJ defaults to bird heads — use `--cref` human portrait for production
  - Gear-Forged: add `--no organic skin, human flesh`

### Canonical Beast visuals (Gemini, lore/peacetime tone)
- Twin-Serpents: gold rune-dragon + void-black serpent in ruined library
- Abyssal Leviathan: black stone-scaled sea serpent, purple glowing cracks, multiple eyes, stormy sea
- Ashen Ram: dark grey wool with lava-crack fleece, ember eyes, volcanic terrain
- Sea-Goat: goat + iridescent fish tail, deep underwater bioluminescent cave
- Kelp-Weaver: blue/green/orange scaled sea dragon with kelp tendrils and glowing nodes
- Nemean Lion: golden, glowing eyes, coliseum backdrop
- Adamant Crab: iridescent shell as tropical island with palm trees
- Star-Metal Stag: navy star-map coat, silver antlers, moonlit forest
- Queen Bee: amber translucent body with crown in honeycomb throne room
- Twin Dream-Fish: silver + golden koi around galaxy spiral in jungle cenote
- Khalkotauros: stone-armored dark bull, green ember eyes, standing stones
- Stygian Scorpion: dark bark-textured carapace with green bioluminescent nodes, green crystal stinger, blue bioluminescent mushroom cave (NOT void-black/light-absorbing)
- Great Roc: white/pale grey eagle with glowing heart-shaped chest pattern, perched on mountain peak above clouds at sunrise (serene, not threatening in scale)

---

## CANON-CHECK COMMANDS (run after major changes)

```bash
# Verify file builds and renders
cd /home/claude && node build_binder.js 2>&1 | tail -1
soffice --headless --convert-to pdf /mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx --outdir /home/claude/preview 2>&1 | tail -1
pdfinfo /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf | grep Pages
pdftotext -layout /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf /home/claude/preview/final.txt

# Verify deprecated terms are absent
python3 << 'EOF'
with open('/home/claude/preview/final.txt') as f:
    text = f.read()
print("DEPRECATED TERM CHECK (all should be 0):")
for term in ['Comet-Mage', 'Concordance', 'Zargon', 'Morcar', 'v14', 'v15', 'Copper Coin (cp)', 'Platinum Crown (pc)', '100 cp = 1', 'em (electrum)']:
    print(f"  '{term}': {text.count(term)}")

print("\nQUINT BOND PRIVACY CHECK (all should be 0 in player-facing):")
for name in ['Inti-kora', 'Asha-Wing', 'Hinerangi', 'Matuā-kore']:
    print(f"  '{name}': {text.count(name)}")

print("\nCANONICAL TERMS PRESENT:")
for term in ['Comet-Magus', 'Comet-Magi', 'AETHAR', 'Verse of Five', 'Warring Zodiacs']:
    print(f"  '{term}': {text.count(term)}")
EOF

# Verify TOC alignment
python3 << 'EOF'
with open('/home/claude/preview/final.txt') as f:
    text = f.read()
pages = text.split('\f')
targets = {'RULES REFERENCE': 170, 'WORLD REFERENCE': 206, 'APPENDIX': 261}
for i, p in enumerate(pages, 1):
    lines = [l.strip() for l in p.split('\n') if l.strip() and 'SIDEROS · Player' not in l]
    for l in lines[:4]:
        if l in targets:
            expected = targets[l]
            status = "OK" if i == expected else f"SHIFTED: TOC p{expected} vs actual p{i}"
            print(f"  {l}: p{i} {status}")
            break
EOF
```

---

## HOW TO START THE NEXT SESSION

When this prompt is loaded into a new chat:

1. Acknowledge the context briefly — confirm you understand the project state, terminology rules, and current document
2. Wait for Matt's next task or vision text
3. If he shares new canon/vision text: propose integration before executing
4. If he asks for an addition: confirm approach, then execute, then verify (rebuild + canon check + TOC alignment)
5. If he asks for a review or audit: be specific about what's currently there, what's missing, and recommend what to add

The output file at `/mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx` should be presented at the end of any session with substantial changes via `present_files`.

---

*Sideros v16 · The Loom weaves all. Your thread is your own.*

*Handoff document version: v17 (created at conclusion of v16 binder session that established foundational vision, character folio restructure, GM toolkit, economy overhaul, and 3-aspect material framework)*
