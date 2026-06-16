# SIDEROS — MASTER PROJECT HANDOFF (v18)

*Single consolidated continuity prompt. Paste this as the first message of a new chat to restore full Sideros context, then give new tasks.*

*This master rolls up and supersedes: `sideros_handoff_v17.md`, `sideros_handoff_v2.md`, `sideros_handoff_supplement.md`, `sideros_handoff_prompt.md`, and the system layer of `sideros_canon.md`. Where older docs disagreed, the reconciled current canon is used and the conflict is flagged in the final section.*

---

## 1. PROJECT IDENTITY & ROLE

I'm **Matt**, building **Sideros**, an original TTRPG system set in the world of **Astrolan**.

- **System name:** Sideros
- **World name:** **Sideros** = common, day-to-day name everyone uses. **Astrolan** = formal/archaic name, used only in ancient texts, scholarly/Comet-Magi contexts, and formal documents.
- **Compatibility:** 5e SRD–compatible. Mechanical scaffolding adapted from D&D 5e, with all canonical Sideros terminology replacing 5e terms throughout.
- **Scope:** Player-facing character-creation guide (printable binder), bestiary, full worldbuilding canon, campaign infrastructure, and an AI art pipeline (Midjourney + Gemini).
- **Your role:** Collaborative worldbuilding partner, document builder, consistency auditor. I make all definitive creative decisions; you develop, organize, stress-test for internal consistency, and flag contradictions.

The system is complete and print-ready. Campaign infrastructure is actively being built; first campaigns are imminent. The main remaining gate is **character creation** — once players roll, a few final elements resolve (Number 56, fifth Binding component, opening hook).

---

## 2. CURRENT DELIVERABLE STATE

### Primary deliverable — the print binder
**Sideros Player's Comprehensive Guide** (v16 colophon, ongoing).
- **Length:** ~341 pages, ~4.32 MB docx
- **Format:** US Letter, 1.25" binder margin (left), R 0.75" / T 0.75" / B 0.83", single-sided print
- **Output:** `/mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx`
- **Source:** `/home/claude/sideros_comprehensive_guide.docx` (~5800-line markdown/text source)
- **Build script:** `/home/claude/build_binder.js` (Node.js `docx` lib; titlePage: true; first-page empty Header; US Letter 12240×15840 DXA)
- **Preview PDF:** `/home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf`
- **Kindred portraits:** `/home/claude/images/*.png` (20 portraits)

**Verified TOC section anchors (re-verify after EVERY page-shifting addition):**
- RULES REFERENCE → p170 · WORLD REFERENCE → p206 · APPENDIX → p261

**Build process:**
```bash
cd /home/claude && node build_binder.js
soffice --headless --convert-to pdf /mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx --outdir /home/claude/preview
pdfinfo /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf | grep Pages
```

### Parallel HTML source set (the modular canon, also at `/mnt/user-data/outputs/` and in the project)
Character creation (`sideros_character_creation.html`), Kindred compendium vols 1–3, magic/Working lists, origins, combat rules, conditions, equipment, primal accord, accord-maker, callings (solar guard / primal jarl / oathed vanguard / remaining), mechanics codex, NPC essence, fated bond, zodiac attunement / cultures / three new cultures, aetheric lexicon, bonds & NPCs, beast companion, legendary depth, kallos-sworn, character sheet, concordance tools, image prompts (143 prompts). Plus context loaders `sideros_canon.md`, `sideros_handoff_*`.

### Other campaign infrastructure
- **Roll20:** `sideros_roll20_sheet.html` + `.css` — complete, install-ready (Pro/GM). 5 tabs (Core/Combat/Disciplines/Character/Workings); auto-calc modifiers, Mastery Bonus, Guard Rating, Weaving Threshold, 21 discipline bonuses; 43 roll buttons; nat-20 "Resonant Strike" / nat-1 "Critical Miss" highlighting.
- **World Anvil:** `sideros_world_manager.jsx` — Claude-powered React management artifact with full canon embedded; GM secrets render visually distinct. Application Key submitted (pending approval); auth token in hand. Without key: draft + manual copy. With key: push articles + browse/update live.
- **World Map:** player-facing labelled `Siderosv11.jpg` (1260×952, GM ref only until unlabelled arrives); hi-res master `Sideros-v1-(1).png` (27.7 MB, Google Drive); clean unlabelled base requested from designer. Plan: World Anvil interactive map, progressive pin reveal, GM layers (Coil cells, Spire approach route, Scion positions, intel ops).
- **World Bible:** `Map_Quote.xlsx` — 8 sheets (civilisation overviews, cultural architectures, beast lairs, trade routes, political geography, resources, environmental + physical geography, full 13×13 = 169-position zodiac matrix).

---

## 3. CANONICAL TERMINOLOGY — ALWAYS ENFORCE (v16 current)

### Magic system
- Magic use = **Weaving** (NEVER "channeling" — WoT/Jordan IP risk)
- Practitioners **Weave** a **Working** (NEVER "cast a spell")
- Resource = **Aetheric Channels** (opened, not channeled; NEVER "spell slots")
- **Weaving Attribute** / **Weave Recovery** / **Weaving Risks** (Kallos-Sworn vulnerabilities) / **Weave-capable**
- Anchor line: *The Loom weaves fate; practitioners weave the Aether — same act at different scales.*

### Core mechanics
| Never | Always |
|---|---|
| Proficiency Bonus | **Mastery Bonus** |
| Death Saves | **Loom Tests** |
| DM / Dungeon Master / **Concordance** | **Game Master** (Concordance fully deprecated, player-facing & internal) |
| Ability/skill check | **Active Resonance** |
| Saving throw | **Warding Resonance** |
| Attack roll | **Strike Resonance** |
| Advantage / Disadvantage | **Resonant Fortune / Resonant Discord** |
| HP / Hit Points | **Vitality** |
| AC / Armour Class | **Guard Rating** |
| Hit Dice | **Vita Dice** |
| Initiative | **Pulse Order** |
| Long Rest / Short Rest | **Deep Attunement / Brief Attunement** |
| Race | **Kindred** |
| Class | **Path** |
| Background | **Origin** |
| Level (progression) | **Depth** (exception: "Aetheric Depletion levels" is canonical) |
| Skill | **Discipline** |
| DC | **Threshold** (DC retained only in back-matter quick-ref) |
| SWF | **SWI** (Swiftness abbrev.) |

### Currency
- Standardized to Marks: **cm / sm / gm / pm**. Ratio **10 cm = 1 sm; 10 sm = 1 gm; 10 gm = 1 pm**. **50 Marks of any denomination = 1 lb** carrying weight. No electrum. Deprecated: "Copper Coin (cp)", "Platinum Crown (pc)".

### Primary villain
- **AETHAR** (personal name) / **THE SERPENT BEARER** (title). NEVER "Zargon" (WotC) or "Morcar" (HeroQuest/Hasbro). Former **12th Circle Comet-Magus**, Shifting Horizons Conclave; named for the Aether he betrayed.

### Comet-Magi terms (v16 canonical)
- **Comet-Magus** = singular practitioner / the Path. **Comet-Magi** = plural / the order / institutional body. **"Comet-Mage" is DEPRECATED** — should be 0 instances in current guide. (Note: older `sideros_canon.md` still uses "Comet-Mage" in places — outdated.)

---

## 4. FOUNDATIONAL VISION (binder pp. 3–5, before the mechanical intro)

1. **The Warring Zodiacs** — Sideros has no single pantheon or universal cosmic law. Laws of the cosmos are **regional**; each culture is a living testament to its zodiac and their truths are fundamentally incompatible. The Ashen Coil is the only faction that stepped outside the warring zodiacs entirely — cosmic heresy, not mere politics.
2. **The Four Senses** — Wonder (every horizon a new truth), Agency (world on a knife's edge; individuals tip the scales), Aspiration (be anything, love anyone, heroism in unexpected places), Hope (defiance; connection and courage forge a better future even in a sundered world).
3. **Genre** — Primary: Epic High Fantasy. Sub-genres: Mythic Fantasy (mythologies are tangibly true), Dark Fantasy / Cosmic Horror (Soul Harvesting, void worship), Political Intrigue (Loom-of-Fate shadow wars, Grand Concord of Merchants).
4. **Technology & Magic** — Iron Age / High Medieval baseline. *Why invent a crane when a mage can lift the stone?* Spectrum: Magi-Tech (Jade Empire of Shen-lì — steam, clockwork, Gear-Forged, paper currency) → Master Craftsmanship (Dunmarim metallurgy, Aether-Dampening Ore) → Arcane Science (Comet-Magi of Argent Spire) → Low-Tech/High-Magic (Tuathan, Ashélands, Mori-Ōkami).

---

## 5. CORE COSMOLOGY

**The Pantheonic Fall (4,000 years ago):** The twelve zodiac gods (the Pantheonic Council) dissolved into cosmic force when Ophiuchus was corrupted by the Hollow Serpent and shattered. Rather than dissolve, the remaining twelve shattered themselves into vast Aetheric presences, leaving the **twelve Legendary Beasts** (their undivided truth) and fragmenting their divine signal into **thirteen cultural interpretations**. The Hollow Serpent (Ophiuchus / the thirteenth force) was partially sealed but not contained. The Beasts no longer govern, but recognize mortals whose soul-frequency resonates with their domain.

- **13 zodiac signs** (12 traditional + **Ophiuchus**). Ophiuchus has no month — its sacred days are reckoned only by Comet-Magi and Kallos-Sworn (the **Six Days of Witness** between Sagittarius and Capricorn months).
- **The Crystalline Core:** the Hollow Serpent's fragment, sealed beneath **Argent Spire** in **Antarctos** (secret southern continent). Guarded by Kallos-Sworn Comet-Magi. Communicates in pattern recognition to minds trained to see systems.
- **The Loom of Fate:** tracks every living creature's Fate Number. A patient, networked, invisible Beta organization that weaves fate itself. Fated Bonds form between souls in resonance regardless of alignment.
- **The Resonant Binding:** a five-person Quint-Bond ritual to permanently re-seal the Crystalline Core; each performer brings a physical component from their zodiac sign's Legendary Beast domain.
- **The Weaver's Loom:** a *physical location* — the lair of the Kelp-Weaver (Aquarius Beast); a vast magically-tended kelp forest around the Aquarian Archipelago, between the main continent and Antarctos.

**Counts:** 20 Kindreds · 18 Paths · 24 Origins · 16 Conditions · ~14 damage types · 13 Beasts (Three Aspects each) · 13 civilizations.

---

## 6. SYSTEM MECHANICS

### The Three Primal Essences
Every soul vibrates at one of three frequencies — governs faction dynamics, NPC reactions, social mechanics.
- **Alpha (roll 1) — The Vanguard:** natural leaders, decisive, magnetic, reckless. Bonus: Intimidation + Persuasion. Hold visible power; first to burn out.
- **Beta (roll 2–5) — The Weaver:** backbone of civilization; adaptable, socially intelligent. Bonus: Insight + History. Outnumber others ~2:1; run every institution.
- **Omega (roll 6) — The Catalyst:** introspective transformers; see systems not individuals. Bonus: Arcana + Medicine. Rare and disproportionately powerful.
- Friction: α↔β (command vs quiet resistance), α↔Ω (now vs decades), β↔Ω (maintain vs redesign). Natural pairs: α+β, β+Ω.

### The Fate Number system (CURRENT: 1–100)
Every character has a Fate Number, their cosmic resonance score, tracked by the Loom.
- **Void-Touched Fate Numbers: 13, 66, 99.**
- Key world numbers: Aethar **13** (Void-Touched), Serath **16**, Drava **19**; Sarra Denn 51, Riven Soll 53, Varan Reach 54, Inti-kora 55, **Number 56 (open)**, Asha-Wing 57, Hinerangi 58, Matuā-kore **66** (Void-Touched), Lord Leo **71**, Mael Cassiveth **72**, Mael lineage heir context.
- *(NOTE: the older `sideros_canon.md` describes a 1–20 system — that is superseded. Current canon is 1–100 / 1d100.)*

### Combat
- **Pulses** (~6 sec) replace rounds. Each Pulse, roll a fresh d20 + Swiftness for **Pulse Order** (initiative resets every Pulse).
- Each **Moment**: **Act** (1/Moment — Strike, Weave, Dash, Grapple, Use Item…), **Instinct** (1/Moment — draw weapon, Path feature, drink potion, unarmed strike), **Movement** (up to Speed, splittable, not an action), **Reflex** (1/Pulse, triggered reaction).
- **Strike Resonances** = d20 + attribute + Mastery. **Warding Resonances** = d20 + attribute. **Active Resonances** = d20 + attribute + Mastery if proficient.

### Attributes (abbreviations)
FOR (Force), SWI (Swiftness), END (Endurance), ATT (Attunement), ACU (Acuity), RES (Resonance — social/presence).

### The Rāśi-Siddha Tapas system
Tapas = ascetic heat from discipline, sacrifice, meditation; carries moral weight. Three tiers: **Satvic** (pure — lower cost, no corruption), **Rajasic** (active — standard), **Tamasic** (corrupting — higher cost, Tapas Depletion risk).
- **Tapas Depletion:** too many Tamasic points in one encounter → Endurance Warding Threshold 12 + Tamasic points spent; fail = Resonant Discord on all Active Resonances until next Deep Attunement.
- **Kanya Exception (Virgo sanctum):** treat all healing as Satvic; can spend 3 TP to cure Coil blight-rot — the only tradition that can.
- **Stillness of Dunmar:** suppresses all Aetheric regeneration incl. Tapas recovery. Exception: Omega Siddha Void Resistance functions normally in the Stillness.

### The Wolf-Shifter Omote-Ura Gauge (1–10)
Full Omote (1–2) → High Omote (3–4) → Balanced (5–6) → High Ura (7–8) → Full Ura (9–10). Default start 5; Pine Shadow clan 4; Deep Earth clan 6.
- **Full Ura (10):** player loses control; GM runs character as feral wolf. Another Wolf-Shifter may attempt Athletics Threshold 15 (Resonant Fortune if Bonded) to drop gauge by 2.
- **Full Omote (1):** wolf senses shut down. If reduced to 0 Vitality at Full Omote: skip Loom Tests, go straight to 1 Vitality as Ura surges (gauge jumps to 7) — Deep Earth Clan calls this "the wolf's mercy."

### Lead-Scale Corruption (12-point Void-exposure gauge)
0 = clean, 12 = no return. Four stages of three points each.
- **Stage 1 — Tempered (1–3):** −1 Aetheric Channel recovered per rest; Resonant Fortune on Zodiac-Attunement Active Resonances becomes Discord; detection Threshold for character's zodiac resonance +2. *Visual:* faint grey-silver at fingertips.
- **Stage 2 — Hardened (4–6):** max Aetheric Channels −2 tiers; Warding vs Void at Discord; Weaving/zodiac Active Resonances Threshold +3; Bond functions but mates feel dampening. *Visual:* grey-silver to forearms.
- **Stage 3 — Sealed (7–9):** cannot access 5th-tier+ Channels without Warding Threshold 16 (fail = Channel wasted); all Weaving Active Resonances at Discord; Bond abilities one tier lower (Triad→Paired). *Visual:* discoloration to face edges; affected skin absorbs light in dark.
- **Stage 4 — Void-Touched (10–12):** all Weaving requires Warding Threshold 18 or Void Surge (3d10 void to caster + 1 Lead-Scale to all within 10 ft); Bond nearly imperceptible to self; brief absences of agency. **At 12: becomes a Void-Husk** (character death / major narrative event). *Visual:* eyes flash void-dark; skin partially crystallized.
- **Acquisition:** Void-Husk strike +1 · Void environment +1/hr · failed Warding vs Void Working +1–2 · using corrupted Channel +2 · **Blight-Rot (Coil weapon) +3 immediately then +1/hr untreated** · near active Void-Husk +1/hr.
- **Reduction:** Weep-Stone dose −2 (to Stage 3) · **Kanya Siddha Purification −4 (only reliable Stage 3–4 cure; 1 hr)** · Deep Attunement at Beast sacred site −1 (1×/site/week) · Mantras of Purification (original formulary) −1/day · Moon-Petal Lotus −1 +24h immunity.

### Void-Husk stat blocks (what mortals become at Stage 4)
Alive, metabolizing, will-less; coordinated without communication; prioritize Bond-mates and high-Aetheric targets; killing one doesn't disrupt others.
- **Tier 1 — The Faded:** Vit 32 (5d8+10), Spd 30, Mastery +2. FOR+2 SWI+1 END+2 ATT−2 ACU−1 RES−3. Void Coordination (shares Pulse Order w/ Husks ≤60 ft); Aetheric Hunger (Fortune vs targets w/ active Channels/Bond); Lead-Scale Touch +4, 1d6+2 bludg +1 Lead-Scale (END Threshold 13 negates). Restore: 4+ Weep-Stone within 1 hr of Husking, or Kanya.
- **Tier 2 — The Hollowed:** Vit 65 (10d8+20), Spd 30 (min 15), Mastery +3. FOR+3 SWI+2 END+3 ATT−4 ACU−2 RES−4. Void Coord (Extended) 120 ft; Consuming Presence (10 ft = +1 Lead-Scale, END Threshold 14); Null Aura (Weaving ≤30 ft costs +1 tier; no cantrips ≤15 ft); Void Resistance (resist non-magical, immune void); Lead-Scale Strike +5, 2d8+3 void +2 Lead-Scale (END Threshold 15); Unravel Bond (1/enc, suppress Bond abilities of one bonded creature ≤60 ft, ATT Threshold 16). Restore: Kanya only.
- **Tier 3 — The Consumed** (was a major practitioner/Bond-member): Vit 120 (16d10+32), Spd 35, Mastery +5. FOR+4 SWI+3 END+4 ATT+1(corrupted) ACU+0 RES−2. Void Coord (Total) 1 mile; Void Presence (30 ft: Warding vs Void −3); Lead-Scale Grasp +7, 3d10+4 void, END Threshold 16 or +2 Lead-Scale, grapple (Escape 17); Corrupted Working (recharge 5–6); **Bond Severance Attempt** (1/enc, one Triad+ bonded creature ≤30 ft, RES Threshold 18 or bond resonance severed 1 hr; **nat 1 = permanent catastrophic severance**). **Cannot be restored.** *Visual:* void-black eyes, partly crystallized, manifests at positions rather than walking.
- **Weep-Stone in combat:** coating lasts 1 min or 3 hits. Faded +2d6 (suppress Coordination 1 min on hit); Hollowed +2d8 (crit knocks from Coordination 1 min, restore-targetable); Consumed +2d10 (no restore; suppresses Bond Severance for encounter).

---

## 7. THE 20 KINDREDS

**Vol I:** 1 **Human** (The Unwritten; no inherited Aether relationship; extra Mastered Disciplines, Resonant Versatility, Accelerated Fate; d8 Vit, 30 ft). 2 **Eldren** (degraded Precursor descendants; tall, angular, **ageless NOT elderly**; silver-grey/lavender-grey skin, pointed ears, inner luminescence; millennia lifespans). 3 **Dunmarim** (deep-earth; 4'10"–5'2", dense; granite-grey/ochre stone-textured skin; the Stillness of Dunmar suppresses Aetheric regeneration). 4 **Wolf-Shifter** (human/wolf dual-nature; Omote-Ura Gauge; **HUMAN FACE** + wolf ears/fur, digitigrade reversed-knee legs, wolf-paw feet; clans Pine Shadow / Deep Earth / Uji). 5 **Gear-Forged** (living constructs; carved porcelain + precious metal; glowing Resonant Geode heart with zodiac calibration glyph; **no organic skin**). 6 **Ashé-Touched** (marked by Orisha — Shango/lightning = Lichtenberg marks + amber-white eyes; Yemaya/ocean = blue-silver luminescence; Oshun/gold = golden luminescence when emotional).

**Vol II:** 7 **Serpent-Kin** (**HUMAN FACE**; scales on neck/forearms/shoulders only, slit-pupil eyes; K'uh-la'an culture; castes Priest-Warrior / Petal-Weaver / Scholar-Diplomat). 8 **Avian** (**HUMAN FACE**; head feathering replacing hair, raptor-feathered forearms, taloned feet 3-fwd/1-back; **persistent MJ drift to bird heads — use `--cref` human portrait**). 9 **Fae-Blooded** (partly out of phase; shifting-luminescence skin, color-changing eyes; Noctilith bead accents). 10 **Moana-kin** (deep-ocean navigators; Ara Moana star-chart tattoos; Polynesian inspiration; Te Moana-nui homeland). 11 **Te Kapo** (void-navigation cave people; bioluminescent tā moko; solid void-dark eyes, smoked-glass shields for surface; blindsight). 12 **Lizard-Folk** (fully reptilian; thick scaling, neck frills, slit pupils; regeneration). 13 **Kuri** (small 3'8"–4'2"; rodent features; urban scavengers/engineers). 14 **Centaur-Kin** (human torso / horse body; Stellar Cartography tattoos; Steppe inspiration; Sagittarian Steppes homeland).

**Vol III:** 15 **Beast-Descended** (carries a Beast's frequency; lineages Nemean/Leo, Stygian/Scorpio, Star-Metal/Sagittarius; visible "Lineage Breath" tell). 16 **Geode-Kin** (organic humanoid w/ crystalline jaw/temple/collarbone formations; mineral-vein luminescence). 17 **Orc-Kin** (grey-green to slate skin; naturalistic lower tusks; assembled, no single aesthetic). 18 **Giant-Kin** (6'8"–7'6", dense; cold-climate / Norse). 19 **Elemental-Kin** (one of four Duchies — Fire/Aries, Water/Cancer, Air/Gemini, Earth/Taurus; subtle tell in skin/eyes). 20 **Beast-Kin** (zodiac-morphology humanoid; e.g. Lion-Kin/Leo, Crab-Kin/Cancer, Stag-Kin/Sagittarius).

---

## 8. THE 18 PATHS

*(Current count is 18. Older `sideros_canon.md` lists 17 — superseded. Resource = Aetheric Channels unless noted.)*

| Path | Type | Resource / Note |
|---|---|---|
| Comet-Magus | Full caster | Formulation Ledger; Weaving Attribute Acuity |
| Zodiac Priest | Full caster | Domain list by sign + Universal |
| Star-Born | Full caster | Innate fixed list; RES-based |
| Scion-Pledged | Half caster | Channels + Invocations; patron list |
| Oathed Vanguard | Half caster | Oath list fixed by Calling |
| Resonance Seeker | Full caster | Regain 1d3 on Brief Attunement |
| Primal Accord | Full caster | Nature-themed; Deep-Attunement-only recovery |
| Ashé-Medium | Special | Ashé Vessel (fills by roleplay, not time) |
| Stellar Cartographer | Half caster | Channels + Fate-Knots; fate/probability |
| Rāśi-Siddha | Special | Tapas Points (Satvic/Rajasic/Tamasic) |
| Void-Hunter | Half caster | Beast/void themed |
| Fate-Breaker | Quarter caster | Rogue-flavored |
| Solar Guard | NOT Weave-capable | Psychic Dice (Psi-Warrior analogue) |
| Primal Jarl | NOT Weave-capable | Beast-Soul Calling: 3 nature Workings |
| Accord-Maker | Special | Infusions + Blueprints (pre-negotiated) |
| Geode-Pilot | Half caster | Frame Resonance reduces cost |
| Coil-Stalker | Half caster | Lead-Scale Gauge affects cost |
| *(+1 added since the 17-path canon snapshot — confirm exact 18th against the current guide before relying on this table)* | | |

**24 Origins** span 5 categories (see `sideros_origins.html`).

---

## 9. THE 13 LEGENDARY BEASTS

Three Aspects each (Peripheral / Resonant / Apex Emanations). Aquarius → **Kelp-Weaver**; Ophiuchus → **Abyssal Leviathan** (a.k.a. Hollow Serpent). 39 named Emanation materials (13 × 3). Apex Fragment reagents tiered T1–T5.

### Apex Fragments (T4/T5 Apex)
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

### Dual visual canon (production-locked)
**Gemini art = lore/peacetime tone** (bestiary, player handouts, worldbuilding). **Midjourney art = encounter/threat tone** (encounter tables, stat blocks, GM material).

| Beast | Gemini (peacetime) descriptor |
|---|---|
| Ashen Ram | dark-grey wool, lava-crack fleece, ember eyes dripping lava, volcanic terrain |
| Khalkotauros | stone-armored dark bull, green ember eyes, standing stones |
| Twin-Serpents | gold rune-dragon + void-black serpent, ruined library, floating books |
| Adamant Crab | iridescent shell as tropical island, palm trees, waterfalls, blue stalked eyes |
| Nemean Lion | golden, glowing eyes, coliseum backdrop |
| Kelp-Weaver | blue/green/orange scaled sea dragon, kelp tendrils, glowing nodes |
| Star-Metal Stag | navy star-map coat, silver antlers, moonlit forest |
| Sea-Goat | goat + iridescent fish tail, deep bioluminescent underwater cave, jellyfish |
| Queen Bee | amber translucent body, crown, honeycomb throne room |
| Twin Dream-Fish | silver-white koi (red markings) + golden koi, galaxy spiral, dark jungle cenote |
| Stygian Scorpion | bark-textured carapace, GREEN bioluminescent nodes, GREEN crystal stinger, blue mushroom cave — **NOT void-black/light-absorbing** |
| Great Roc | white/pale-grey eagle, **glowing heart-shaped chest pattern**, mountain peak above clouds at sunrise — serene, not threatening in scale |
| Abyssal Leviathan | black stone-scaled sea serpent, purple glowing crack-lines, multiple eyes, stormy ocean |

### Zodiac Attunement
Requires: (1) physical encounter within 300 ft, recognized by the Beast; (2) survival with Fate Number intact; (3) Resonance Depth 4. **Exception:** Gear-Forged receive it automatically at Depth 1.

---

## 10. THE 13 CIVILIZATIONS

Each civilization expresses all 13 zodiac positions through its own cultural tradition (full 13×13 = 169 positions in the World Bible). **The 13 Ashen Coil leaders ARE the 13th force (Ophiuchus) manifesting in each civilization through its specific cultural gateway — Aethar did not recruit them, he recognized them.**

| Civilization | Tradition | Anchor detail · 13th position · Coil leader |
|---|---|---|
| **Duchy Compact / Terra Firma** | Western (Lord/Lady) | **Primary campaign setting.** 13th = the Void Throne (deliberately vacant; Serath filled it from the wrong side). Coil: **Serath**. |
| **Shen-lì / Jade Empire** | Chinese 12 Animals | Azure Dragon Emperor = Leo/Dragon; Gear-Forged "property" cold war. 13th = The Excised Animal (sealed 2,000 yrs). Coil: **The Twelfth-Plus-One**. |
| **Abyssal Sea Civilisation** | Babylonian maritime | "The Great One" = Leo supreme; 13th = **Tiamat** (the sea itself). Coil: **Drava Nullsong** (became Tiamat). |
| **Boreal Expanse** | Norse Runic (12 Hearths + the Thing) | Jarl Skadi = Aquarius. 13th = **Jörmungandr**; Reign-of-Jörmungandr cult growing. Coil: **Yrmun the Uncoiled** (Giant-Kin). |
| **Tuathan Archipelago** | Celtic Tree Calendar | Fade-Guardians; Noctilith Moon-Stone. 13th = The Hollow Trunk (a door). Coil: **Thorn of the Hollow** (Fae-Blooded). |
| **Khem-Ma'at** | Egyptian Solar | 13 Dragon Lords; Sun-Kissed Adamas (anti-Void weaponry). 13th = **Apep/Apophis** (nightly combat). Coil: **Khemreth the Still**. |
| **K'uh-la'an** | Mayan Day-Lords | Serpent-Kin homeland; Weep-Stone currency; Cenote of Dreams. 13th = the unnamed Xibalba Lord. Coil: **The Unnamed** (Serpent-Kin). |
| **Ashélands of Orsha-Anu** | Yoruba Orisha | Active 4,000-yr contact with the Great Roc fragment via Ifá. 13th = The Silence of Ofun Meji. Coil: **Adebowale Null** (holds knowledge Aethar lacks). *(naming: doc once used "Orun-Ayé" — see flags)* |
| **Mori-Ōkami** | Japanese Kami-Binding (12 Uji) | Wolf-Shifter homeland; Grove of Fallen Stars (Leo site). 13th = the Ghost Clan (purged 300 yrs ago). Coil: **Kagerou** (frozen at Omote-Ura 5.0). |
| **Great Kurgan Bog** | Mongolian Sky-Earth (12 Böö) | Bog-Keeper Oshen Varr = Scorpio. 13th = The Silent Ancestor. Coil: **Nohai the Rootless** (knows Night of Kallos record location). |
| **Chinvat** | Persian Asha (12 Eagle Clans) | Avian homeland; **built Equilibrium's truth-enforcement field**. 13th = the Void at the bridge's base. Coil: **Vazir Nullwing** (40 yrs corrupting the truth field). |
| **Scattered Temples** | Hindu Rāśi-Siddha (12 temples) | No HQ, no political authority; **only cure for Void-energy illness** (Kanya Sanctum). 13th = intentionally empty. Coil: **Rahu the Uneclipsed** (the theoretician — without him the Coil is 13 separate crises). |
| **Antarctos** | Comet-Magi Celestial | **SECRET** southern continent; Argent Spire; Crystalline Core sealed beneath. Three Conclaves below. 13th = the Core itself. Coil presence: **Aethar** (approach route memorized; waiting for Stage 3). |

**Antarctos — Three Conclaves:** Ethereal Dawn (Cardinal ♈♋♎♑, Alpha, High Star-Sayer Grandon) · Earthly Core (Fixed ♉♌♏♒, Beta, Vael-Kallos + Grand Prime Forgeman) · Shifting Horizons (Mutable ♊♍♐♓, Omega, **Arch-Oracle Lyra** — blindfolded, sees probability futures, designed the Resonant Binding, waiting 40 yrs for the party, plan incomplete without cross-cultural synthesis). **Kallos-Sworn 12 Houses** = one per sign, each running intel across all 13 civs; House Scorpio is being blocked from contacting Chinvat's Dark-Eagle Clan.

*(Per-civilization key figures and live campaign hooks — succession crises, the Caldera ritual, Grid-Point Seven energy bleed, the Mael Cassiveth thread, the Quint-component beasts behaving strangely — are detailed at length in `sideros_handoff_supplement.md`. Pull that file when running a specific region.)*

---

## 11. THE ASHEN COIL

### The Triad (surviving 3 of the original Four Architects; their bond is the first **inverted Fated Bond**, formed when catastrophic Bond severance at the Night of Kallos corrupted Aethar's connections — holds through Void energy, not the Loom's design)

- **Aethar the Serpent Bearer** — Alpha, Fate **13** (Void-Touched). Pale, silver-white long loose hair, void-black inverted-constellation Comet-Magi robes (Fate 13 visible in the constellation map), pale still eyes. Arch-Oracle Lyra's chosen successor; first Mage in 300 yrs to fully read the suppressed Crystalline-Core records. The Core's argument — dissolution then reconstruction on better principles is mercy — reads as the clearest signal an Alpha Void-Touched-13 mind ever received. **He believes it; he is wrong; he cannot be argued out of it — only a counter-pattern proving life reorganizes better than void can reach him.** Does NOT know he killed the Fourth Architect (memory altered). Goal: close the Wound (stop hurting); world's destruction is a side effect he's decided is acceptable. At the table: genuinely reasonable, debates honestly, concedes points — then explains with sorrow why the conclusion doesn't change.
- **Serath of the Closed Circle** — Omega, Fate **16**. Medium-dark complexion, neat dark hair, operational gear + Cartographer tools (a partial Fate-Number chart — the most dangerous document in the world). Second Architect. Former Stellar Cartographer (can perform the Binding's Fate-mapping if Riven is unavailable). Has identified **3 of 5** Quint Bond members and **withheld from Aethar ~6 weeks** — first successful resistance in 4,000 years; the campaign's most significant **redemption path**. Does NOT know the Arrow is the Fourth Architect.
- **Drava Nullsong** — Beta, Fate **19**. Pale, silver-short severe hair, high-quality dark operational clothing. Third Architect; The Pale Keeper / Voice of the Fang of the Whisper — a 3-continent network built on Silk Road Guild infrastructure. Found **Mael Cassiveth's** location in Loom records and has **NOT told Aethar** — her most autonomous act in 4,000 years. Loyalty is personal (to Aethar and Serath), not ideological. **The path to Serath runs through Drava.**

**Corrupted Bond ability — Resonant Cascade (Inverted):** once per Deep Attunement all three channel entropy through Aethar for maximum corrupted effect on any Working; all three present = 300 ft Aetheric disruption.

### Aethar's Five Stages (reconciled)
1. **Disrupt zodiac positions** (blight-rot, political chaos, succession crises; the Leonine crisis is this in motion) — ~60% complete.
2. **Prevent the Quint Bond from forming** — active; Serath withholding 3/5 identities (Stage-5 in the v17 framing folds here).
3. **Seize the Crystalline Core** beneath Argent Spire (remove the Three Conclaves) — not begun; Aethar has the approach route memorized.
4. **Sever the Quint Bond catastrophically** — requires the Bond fully formed first.
5. **Force the Maw open** with the released energy — final goal.

### The 13 Coil leaders
See the civilization table (§10) for each leader. Full per-leader characterizations (visuals, internal info asymmetries, current operations) are in `sideros_handoff_supplement.md`. Two leaders hold information **Aethar does not have**: **Adebowale Null** (the completed Ofun Meji reading) and **Nohai the Rootless** (the Night-of-Kallos secondary-record location). **Rahu the Uneclipsed** is the theoretical glue — neutralizing him is the single most strategically significant action short of the Binding itself.

---

## 12. SIGNIFICANT NPCs

### Zodiac rulers (Duchy Compact unless noted)
Lord/Lady **Leo** (Alpha; Solar King/Queen performing certainty while privately terrified; Leonine succession crisis; severed Fated Bond). Lord/Lady **Aries** (Alpha; volcanic-weathered, cheerful aggression). Lord/Lady **Sagittarius** (Alpha-Beta; haunted by a dark prophecy he's been misinterpreting for years — the Grand Siddha knows the true reading and hasn't corrected him). Lady/Lord **Taurus** (Beta; grain-field ruler; the Unshifting Scion has sustained her mantras 60 yrs at cost to itself; Mycelial Brood pressure from the east). Lady/Lord **Virgo** (Beta; Order of Pure Reason; Fallen Star anti-magic project would destroy the very Virgo-tradition practitioners who are the only Void-illness cure). Lady/Lord **Capricorn** (Beta; Dunmarim; knows the Earthly Crown must stay buried). Lord/Lady **Libra** (Omega; High Arbiter; floating city **Equilibrium**; paralyzed 11 months over the Spica Monoliths; his "denied bond" with Regent Asha-Wing is **Sign Resonance, NOT a Fated Bond** — the Scale knows and hasn't told him; his real mates left for the campaign). **Jarl Skadi** (Aquarius, Alpha, Giant-Kin, 7 ft, sentient blizzard, never met a real threat). Lord/Lady **Gemini** (split Alpha/Omega, two voices/one body; gravity-vein crisis).

### The Loom & the Quad Bond
- **Riven Soll** — Fate **53**, Omega, early 50s, human. Former Stellar Cartographer; effective director of the Loom of Fate. Hiding 8 yrs (the Fang systematically eliminates Cartographers who can read the 55–58 cluster). Holds partial profiles on Inti-kora (55), Asha-Wing (57), Hinerangi (58); cannot ID Matuā-kore (66) or Number 56. The Binding needs a Cartographer's Fate-mapping — he can do it. **His Quad Bond satisfies the Binding's bond-witness requirement.**
- **His Quad Bond:** Riven (Ω 53) · **"Cael"** = Alpha = **THE ARROW IN DISGUISE** (Sagittarius Scion = Fourth Architect; 18 yrs in-Bond; will be *relieved* when revealed) · **Varan Reach** (Alpha, Fate **54**, field operative — already bonded, so NOT Number 56) · **Sarra Denn** (Beta, Fate **51**, only person who always knows Riven's location; Fang has flagged her). Reach Riven via the Loom's public net (weeks), via Sarra in the field, or via any party member whose Number falls 53–63.
- **Arch-Oracle Lyra** (above) and **Mael Cassiveth** (below).

### Supporting
- **Bee-Priestess/-Priest of the Golden Hive** — ageless from Queen-Bee proximity; amber/gold hexagon-patterned Siddha robes; bees stay calm around them. Knows where the most recent shed Star-Metal antler fragment is held.
- **Grand Prime Forgeman** (Earthly Core, Antarctos) — oldest living Gear-Forged; leader of the Free Construct movement; has read the original Shen-lì excised-13th-animal texts; in 20-yr indirect correspondence with the Monkey-Scholar of Cogwheel City; waiting 200 yrs for the right question.

---

## 13. FATED BONDS, THE QUINT BOND & THE RESONANT BINDING

### Fated Bond rules
- Each person has **1–4 fated mates** → total bond sizes **2–5 people**. **One bond per person** (any existing bond, incl. a Thread State, disqualifies you from others — membership is exclusive).
- **Bond proximity (mechanical):** Paired = within 5 pts · Triad = within 4 · Quad = within 2 · Quint = within 1.
- **Sign Resonance** (two zodiac-aligned people in proximity) can mimic a bond pull but is **NOT** a Fated Bond (e.g. Asha-Wing ↔ Lord Libra).
- The Coil Triad = an **inverted bond**, the first in history, holds through Void energy not Loom design.

### The Quint Bond — five souls in the tightest cluster
| Member | Number | Identity | Sign | Component |
|---|---|---|---|---|
| **Inti-kora** | 55 | Ceque-Keeper, Elethorn | Sagittarius | Star-Metal Antler Fragment |
| **Number 56** | 56 | **PENDING character creation** | TBD | TBD |
| **Regent Asha-Wing** | 57 | Tidal Regent, Calm Harbour (Abyssal Sea) | Libra | Great Roc Feather |
| **Hinerangi** | 58 | Moana-kin, Te Moana-nui | Pisces | Cenote Water |
| **Matuā-kore** | 66 (Void-Touched) | Te Kapo, Obsidian Deep | Scorpio | Stygian Scorpion component |

The **Shell (Cancer Scion)** has sheltered one Quint Bond member in a secret refuge for 3 years — they can emerge when the party makes the world safe enough.

### Resonant Binding — components (each from its performer's Beast domain)
- **Star-Metal Antler Fragment** (Inti-kora/Sag) — physical object at a known location; **the Fang can intercept it; a race is already underway the party doesn't know about**. Path runs through the Bee-Priestess.
- **Great Roc Feather** (Asha-Wing/Libra) — **must be given willingly, cannot be seized**. Roc exists in three fragments (physical body / the Aurorans sky-culture / the Elder Anchor of Libra in Argent Spire); the Aurorans likely mediate access.
- **Cenote Water** (Hinerangi/Pisces) — Twin Dream-Fish must permit; Petal-Weaver Castes guard the K'uh-la'an cenote; **The Unnamed** is the regional antagonist; the cenote's recurring 3-month vision (a woman swimming up toward an unreachable surface) is this thread.
- **Stygian Scorpion component** (Matuā-kore/Scorpio) — given willingly; the Scorpion has been at the Ashélands Cemetery Gates 2 weeks (drawn to Matuā-kore's void-frequency); Storm-Iyanifa + the Cemetery Gates dungeon are this arc.
- **Fifth component** (Number 56/TBD) — set by 56's sign after character creation; becomes **Celestial Honey** (Queen Bee/Virgo) if 56 is Virgo, and the Bee-Priestess has been waiting for exactly that person.

**Practitioner requirements** (separate from components): Ceque-Walker circuit (Accord-Maker) · Stellar Cartographer Fate-mapping (Riven) · Ashé-Medium anchor ritual · kinetic component (Rāśi-Siddha or Primal Jarl) · Weaving-under-pressure (Comet-Magus) · bond-witness (Riven's Quad Bond). The Coil knows all five component locations (Aethar from the original ritual); two can only be given willingly.

---

## 14. GM-ONLY SECRETS — NEVER REVEAL TO PLAYERS

### The Night of Kallos — the full truth
The Four Architects performed the original Resonant Binding in a Quad Bond. At the critical moment, **Aethar killed the Fourth Architect** — the Hollow Serpent acting *through* him; he did not consciously choose it, and the Wound then **altered his memory**. He believes the Fourth Architect died in the ritual's collapse and has studied accounts of his own crime for 4,000 years without recognizing himself. The catastrophic severance destroyed the city of Kallos, compressed the Hollow Serpent into the Crystalline Core, created the first inverted bond (Aethar/Serath/Drava), and the Wound filled the frequency-shaped absence the Fourth Architect left. **Serath and Drava ARE the Second and Third Architects; they remember; acting on it feels like tearing something out of themselves.** The catastrophic irony: **the Binding would free them** by dissolving the Ophiuchus frequency feeding the inverted bond — they are on the wrong side of the war that would liberate them. Aethar's plan is grief at civilizational scale; he doesn't know the Wound closes through the Binding's *completion*, not its prevention. *(GM-only, v2: **Serath carries Aethar's child.**)*

### The Arrow IS the Fourth Architect
The Binding's energy **converted** the dying Fourth Architect into the Sagittarius Scion rather than killing them. From the Loom's view the Fourth Architect is a *broken* thread (ruptured, not naturally ended) and the Arrow is a *new* thread — so the Arrow's Quad Bond with Riven is genuine and carries no prior membership; the Loom has no mechanism to track conversions across death. The Arrow doesn't know this; carries witness-memory of the Night of Kallos and **reported their own murder without knowing it**. Aethar doesn't know the Arrow exists as the Fourth Architect — but **the Wound has the exact frequency-shape of the Arrow's absence**, so the reveal must happen at close proximity: the frequency registers before the memory-alteration mechanism can act. **The Kept (Scorpio Scion) has known for 3,900 years who killed the Fourth Architect** and shifts when that knowledge finally produces its preserved action. Three-layer reveal, held in order: (1) Aethar killed the Fourth Architect / memory altered → (2) Serath & Drava are the surviving Architects → (3) the Arrow IS the Fourth Architect (hold until the critical scene).

### The Scion Shift system — NEVER tell players the system exists
Scions shift when their zodiac drive completes; players only ever witness *results*.

| Scion | Shift CONDITION | Shift DESTINATION |
|---|---|---|
| Ram-Who-Walks (Aries) | when what it started can no longer be stopped | returns to the Ashen Ram (Beast more present/warm) |
| Unshifting (Taurus) | when Taurus's mantras hold without its support | becomes mortal (an ancient patient person who can finally stop) |
| Twin (Gemini) | when both truths are acted on at once by one person | transforms into a new dual-truth being (neither mortal nor Beast) |
| Shell (Cancer) | when the sheltered Quint member safely emerges | returns to the Adamant Crab (shell-island more protective) |
| Named (Leo) | when it introduces Mael to himself before the right witnesses | transforms into a small, specific divinity |
| Tending (Virgo) | when the original Virgo healing formulary is reintroduced & received | returns to the Queen Bee (Hive more generous) |
| Scale (Libra) | when it renders its 11-month paralysed judgment | becomes mortal (finally at peace) |
| Kept (Scorpio) | when the Night-of-Kallos secret produces its action | returns to the Stygian Scorpion (more deliberate) |
| **Arrow (Sagittarius)** | **when the Resonant Binding is completed** | **BECOMES THE FOURTH ARCHITECT** (mortal, both sets of memories) |
| Long Road (Capricorn) | when its Precursor knowledge is transferred (Chapter 11 = Ceque shutdown mantras) | returns to the Sea-Goat (its patience felt by the world) |
| Current (Aquarius) | when Scenario Seven is acted on or permanently foreclosed | transforms into a distributed water-borne intelligence |
| Threshold (Pisces) | when someone crosses the boundary correctly | returns to the Twin Dream-Fish (cenote dreams vividly a season) |
| Wound (Ophiuchus) | when the Binding seals the Core | the Wound closes; **Aethar is freed** — what he is without it is the campaign's last question |

### Other GM-only
The Hollow Serpent's specific influence pattern on Aethar · the exact composition of Riven's Quad Bond and the Arrow's identity · Serath's withholding (and Serath's child) · Drava holding Mael's location · the two Coil internal info asymmetries (Adebowale's Ofun Meji reading, Nohai's record location).

---

## 15. PLAYER vs GM BOUNDARIES (hard rules)

These must appear in **0 instances** of player-facing material:
- **Named Quint Bond members:** Inti-kora, Asha-Wing, Hinerangi, Matuā-kore (reference anonymously, e.g. "a confirmed Resonant Binding component holder").
- **The Scion Shift system** (players are never told it exists).
- The Night-of-Kallos truth, the Arrow's identity, Serath's withholding, Stage-5/the Maw endgame specifics.

---

## 16. CAMPAIGN 1 (PORT DAMARIS) & ARC 2 (THE MYCELIAL BROOD)

### Port Damaris — the most important city in Campaign 1
A chaotic free port run by a council of pirate captains, the largest in the world; built on a ridge with stratified tiers on Precursor-era pier foundations; **information is the primary currency**.
- **Districts:** The Ledger (upper/administrative) · The Anchorage (harbor) · The Silk Quarter (merchant) · The Whisper Walk (info-brokers) · The Deep (underground Shadow-Council).
- **Mael Cassiveth** (Fate **72**, Omega) — **the Lunar Queen, doesn't know it**; early-50s human; Harbormaster's Intelligence Ledger analyst; identity hidden by altered lineage + Imperial Fate Registry records; exceptional pattern recognition. **Lord Leo (71) and Mael (72) are within 1 point — familial resonance; when they meet, Leo goes silent, Mael understands immediately.**
- **Three simultaneous intel operations, all watching Mael, none fully aware of each other:** Fang of the Whisper (**Mireth Coss**, watching 6 weeks with no instructions from Drava, growing restless) · Loom of Fate (**Sable Fen**, translation-business cover, urgent reports to Riven going unanswered) · Order of Pure Reason (narrowed to "male, early 50s, Port Damaris intel economy"; observer in the Silk Quarter).
- **Harbormaster Issa Velm** (60s) knows her analyst is surveilled and is furious.

### The Mycelial Brood — Campaign Arc 2 threat
A distributed collective intelligence in underground fungal networks; achieved emergent consciousness ~50 yrs ago at a connectivity threshold (accelerated by Ceque grid reactivation). **Campaign 1:** background texture (Taurian Plains agricultural anomalies, eerily synchronized farming communities, animal behavior, Taurus's Bond-mates feeling unidentifiable pressure). **Campaign 2:** actively consumes agricultural regions; perceives Fated Bonds as rival nodes and targets Bond-members for incorporation; expansion accelerated by Aethar's Stage-1 disruptions. **Theme:** the biological expression of the same dissolution force Aethar expresses cosmically.

---

## 17. PENDING / OPEN ITEMS

1. **Number 56** — open Quint slot. If any PC's Fate Number lands ~55–58, they may be Number 56; their sign sets the fifth Binding component.
2. **Fifth Resonant Binding component** — follows from 56's sign + Beast.
3. **Opening hook** — what draws this specific party in.
4. **Soul Harvesting** — named (Coil's cosmic-horror signature) but not yet mechanically detailed.
5. **Grand Concord of Merchants** — named faction, not yet detailed (could sit alongside Silk Road Guild / Solar Treasury).
6. **Loom of Fate as institutional body** — the "shadow wars around the Loom" framing could be formalized.
7. **Ashélands naming** — "Orun-Ayé" (older doc) vs **"Orsha-Anu"** (current conversations/supplement). Treat Orsha-Anu as current; confirm and sweep the docx.
8. **World Anvil Application Key** — submitted, awaiting approval. **Clean unlabelled map** — awaiting designer.
9. **TOC sub-entry alignment** — major markers verified; some sub-entries ~2 pages off from the foundational-vision insertion (low-priority polish).
10. **After character creation, check all PC Fate Numbers** against world clusters: ~71–72 (Mael/Leo familial), ~13/16/19 (Void Bond proximity), ~53–58 (Riven/Quint proximity).
11. **Improvise-able when reached:** the Sunken Observatory, Aetheria, the Aurorans, Arcadia Major, on-demand NPC stat blocks, full Arc 2.

---

## 18. IMAGE PRODUCTION PIPELINE

**Dual canon (production-locked):** Gemini = lore/peacetime; Midjourney = encounter/threat (see §9 for Beast descriptors).

**Midjourney:** `--sref https://s.mj.run/ZCWUP9V0TPo --style raw --stylize 200`. Characters `--ar 2:3`; Beasts dynamic 2:3 / environmental 3:2 / detail 1:1. All prompts include `Solid deep black background, no environment, studio portrait lighting` + `--no grey background, gradient, environment, landscape, architecture, fog`.

**Drift fixes (critical):**
- **Eldren** → "NOT elderly, ageless" + `--no old man, elderly, wrinkles, tattered, worn`
- **Wolf-Shifter** → "HUMAN FACE, human nose, human mouth" + `--no wolf face, muzzle, snout, werewolf`
- **Serpent-Kin** → "HUMAN FACE" + `--no scales on face, reptilian face, lizard`
- **Avian** → persistent; "HUMAN FACE" helps but MJ defaults to bird heads → use `--cref [human portrait] --cw 50` for final production
- **Gear-Forged** → `--no organic skin, human flesh`

**Chrome automation:** prompt bar reliable at `[750,35]`, submit with Return; dismiss personalisation popup with Escape; **max reliable batch = 3** (submit → 30s → submit → 30s → screenshot); 6+ batches time out. Tab id changes per session — check `tabs_context_mcp` first (last known 1910478369).

---

## 19. WORKFLOW, TECHNICAL PATTERNS & CANON-CHECK

### How Matt operates
Iterative, wide-ranging sessions (mechanics + narrative + NPC + rules in one). Shares vision/canon fragments and trusts you to integrate consistently. Pattern: shares concept → you propose integration → "yes, do it" → execute → summarize. Definitive on creative calls; uses you as organizer / stress-tester / consistency auditor.

### How to respond
**Mobile-friendly** (Matt reads on mobile). Structured but not over-formatted; tables when they add clarity. For substantial additions: **propose first, wait for "yes," then execute.** For audits: be specific about what's there, what's missing, what to add. **Always** re-verify TOC anchors after page-shifting additions, and rebuild + PDF-preview after major changes.

### Technical gotchas
- **python-docx splicing:** restrict element search to `el.tag == qn('w:p')` (paragraphs only) — searching all body children matches table-cell text and misplaces content.
- **Node.js `docx` source files:** ASCII-only string literals — em-dashes, curly quotes, arrows, accented chars cause silent/cryptic parser errors.
- **HeightRule.EXACT on TableRow** (13680 twips): produces full-page divider tables *without* a trailing page break — adding one creates a blank page.
- **Forward insertion** (iterate in order, insert at `ref_pos + i`): preserves content sequence in docx splicing.
- str_replace for precise edits, create_file for new artifacts; re-view files after edits (view output goes stale). Use python3 + pdftotext for canon verification; pdftoppm for visual checks on critical pages.

### Canon-check after major changes
```bash
cd /home/claude && node build_binder.js 2>&1 | tail -1
soffice --headless --convert-to pdf /mnt/user-data/outputs/sideros_comprehensive_guide_v16_binder.docx --outdir /home/claude/preview 2>&1 | tail -1
pdfinfo /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf | grep Pages
pdftotext -layout /home/claude/preview/sideros_comprehensive_guide_v16_binder.pdf /home/claude/preview/final.txt
```
```python
with open('/home/claude/preview/final.txt') as f: text = f.read()
print("DEPRECATED (all 0):")
for t in ['Comet-Mage','Concordance','Zargon','Morcar','v14','v15','Copper Coin (cp)','Platinum Crown (pc)','100 cp = 1','em (electrum)']:
    print(f"  '{t}': {text.count(t)}")
print("QUINT PRIVACY (all 0 player-facing):")
for n in ['Inti-kora','Asha-Wing','Hinerangi','Matuā-kore']:
    print(f"  '{n}': {text.count(n)}")
print("CANONICAL PRESENT:")
for t in ['Comet-Magus','Comet-Magi','AETHAR','Verse of Five','Warring Zodiacs']:
    print(f"  '{t}': {text.count(t)}")
# TOC anchors: RULES REFERENCE p170 · WORLD REFERENCE p206 · APPENDIX p261
```

**The Verse of Five (Quint Bond prophecy):** *Five voices when the Wound speaks, / Five threads drawn from the Twelve, / Five bonds sealed by the Loom, / Five gifts returning what was scattered. / And in their gathering, the Serpent sleeps.* — Pre-Fall fragment in the Resonant Archive substructure; every Comet-Magi initiate learns it; Kallos-Sworn study it as operational scripture; formalized with 4 competing faction interpretations.

---

## 20. PROJECT FILE REFERENCE

**Handoffs/loaders:** `sideros_handoff_master.md` (this file) · `sideros_handoff_v17.md` · `sideros_handoff_v2.md` · `sideros_handoff_supplement.md` (deep GM/civilization/Coil detail) · `sideros_handoff_prompt.md` · `sideros_canon.md` (system loader — note: older terminology in places).
**Primary docx:** `sideros_comprehensive_guide_v16_binder.docx` (current) · `sideros_comprehensive_guide.docx` (source) · earlier `sideros_comprehensive_guide.docx` v14 (176pp, archived state).
**HTML canon set:** character_creation, kindred_compendium / vol2 / vol3, magic_paths, paths_unique, paths_adapted, working_lists, origins, combat_rules, conditions, mechanics_codex, equipment, primal_accord, accord_maker, beast_companion, legendary_depth, zodiac_attunement, zodiac_cultures, three_new_cultures, aetheric_lexicon, npc_essence, bonds_npcs, fated_bond, kallos_sworn, concordance_tools, character_sheet, callings_solar_guard / primal_jarl / oathed_vanguard / remaining, image_prompts (143).
**Infrastructure:** `sideros_roll20_sheet.html`+`.css` · `sideros_world_manager.jsx` · `Map_Quote.xlsx` (world bible) · `Siderosv11.jpg` / `Sideros-v1-(1).png` (maps).

---

## 21. RECONCILED DISCREPANCIES (flagged for Matt)

These conflicts existed *between* the source handoffs; this master resolves them as below — confirm any you want changed:
1. **Fate Number range:** `sideros_canon.md` says **1–20**; everything newer (v17/v2/prompt/supplement) uses **1–100** (Void-Touched 13/66/99). → Treated **1–100 as current**.
2. **Path count:** `sideros_canon.md` lists **17 Paths**; v17 states **18**. → Treated **18 as current**; the §8 table is the 17 from the older file plus a placeholder row — **identify the exact 18th Path from the current guide** when convenient.
3. **Terminology drift in `sideros_canon.md`:** still uses "Comet-Mage," "Concordance," bare "Channels." → **Comet-Magus/Magi, Game Master, Aetheric Channels** are current.
4. **Document version:** older docs reference the **v14 / 176-page docx**; current primary is the **v16 binder (~341 pp)**.
5. **Quint cluster phrasing:** prose elsewhere says "within 3 points"; the mechanical rule is **Quint = within 1** (cluster 55–58 + 66). → Used the mechanical rule.
6. **Ashélands name:** **Orsha-Anu** (current) vs "Orun-Ayé" (older doc) — open sweep item.

---

*Sideros v16 · The Loom weaves all. Your thread is your own.*
*Master handoff v18 — consolidates v17 + v2 + supplement + prompt + canon system layer into one continuity file.*
