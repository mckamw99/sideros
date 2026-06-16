# SIDEROS — COMPREHENSIVE SESSION HANDOFF
*Paste this at the start of a new Claude conversation to restore full project context.*
*Supersedes all previous handoff documents. Current as of June 12, 2026.*

---

## YOUR ROLE

You are collaborating with Matt on **Sideros** — a complete original TTRPG system set in the world of **Sideros** (common name) / **Astrolan** (formal archaic name). Matt makes all creative decisions. Your role is to develop, organise, stress-test for internal consistency, and flag contradictions. Sessions are wide-ranging — mechanics, narrative, NPC development, infrastructure, and rules clarifications often happen simultaneously.

The system is complete and print-ready. The campaign infrastructure is actively being built. First campaigns are imminent.

---

## CANONICAL TERMINOLOGY — ALWAYS ENFORCE

| Never Say | Always Say |
|---|---|
| Channeling magic | **Weaving** |
| Channels a spell | **Weaves a Working** |
| Channeling Attribute | **Weaving Attribute** |
| Channel Recovery | **Weave Recovery** |
| Proficiency Bonus | **Mastery Bonus** |
| Death Saves | **Loom Tests** |
| Dungeon Master / DM | **Game Master** |
| Concordance | **Game Master** (fully replaced across all documents) |
| Zargon | **NEVER — WotC copyright** |
| Morcar | **NEVER — HeroQuest/Hasbro copyright** |
| Astrolan (in common speech) | **Sideros** (Astrolan = formal/archaic only) |
| SWF | **SWI** (Swiftness abbreviation) |
| Hit Points | **Vitality** |
| Armour Class | **Guard Rating** |
| Spell Slot | **Aetheric Channel** |
| Advantage / Disadvantage | **Resonant Fortune / Resonant Discord** |
| Long Rest / Short Rest | **Deep Attunement / Brief Attunement** |

Magic resource: Aetheric Channels (opened, not channelled). Practitioners Weave a Working.
*The Loom weaves fate; practitioners weave the Aether — same act at different scales.*

Primary villain: AETHAR (personal name) / THE SERPENT BEARER (title).
Gold: Gold Marks (not GP). Attribute abbreviations: FOR / SWI / END / ACU / ATT / RES.

---

## WORLD NAMING — CRITICAL DISTINCTION

- **Sideros** — the common name for the world. What everyone calls it day-to-day: maps in taverns, ship logs, everyday speech, the name players know. Also the name of the TTRPG system itself.
- **Astrolan** — the formal, archaic name. Used in ancient texts, Comet-Magi documentation, Kallos-Sworn records, pre-Pantheonic Fall scholarship, and formal ritual contexts. Aethar thinks of it as Astrolan.

---

## CAMPAIGN INFRASTRUCTURE — CURRENT STATE

### Print Document
**sideros_comprehensive_guide.docx** — v14, 176 pages, fully print-ready.
Structure: ToC (p1) > Binder Guide (p2) > Introduction (p3) > Rules Primer (p5) > Part I Character Creation (p11, Steps I-IX) > Session Zero Guide (p51) > Part II Path Depth Progression (p54) > Rules Reference (p106) > World Reference (p115) > Appendix (p120) > Character Folio (p138).
Margins: L=1.25" binder, R=0.75", T=0.75", B=0.83". All terminology correct. Bond proximities correct. FOR REQ on armour table. XP table Sideros-native (no D&D brand references).

### Roll20 Character Sheet
**sideros_roll20_sheet.html + sideros_roll20_sheet.css** — complete, ready to install.
Requires Roll20 Pro (GM only; players join free).
Install: Game Settings > Character Sheet Template > Custom > paste HTML then CSS.
5 tabs: Core / Combat / Disciplines / Character / Workings.
Auto-calculates: attribute modifiers, Mastery Bonus from Depth, Guard Rating, Weaving Threshold, all 21 discipline bonuses.
43 roll buttons covering all attributes (Mastered/Unmastered/Warding), all disciplines, Strike Resonances, Loom Tests, Weave Working.
Custom Sideros roll template with nat-20 (Resonant Strike) and nat-1 (Critical Miss) highlighting.
Repeating sections: weapons, armour, Aetheric Channels, Fated Bonds, working log, custom disciplines.

### World Anvil
**sideros_world_manager.jsx** — Claude-powered React management artifact, operational now.
Full Sideros canon embedded as system context. Quick actions for all major article types.
Application Key: submitted June 12, 2026, pending World Anvil approval.
User Authentication Token: in hand.
Without Application Key: AI drafting works, copy output to WA manually.
With Application Key: push articles directly to WA, browse/update live articles.
GM secrets render visually distinct from player-visible content in every draft.

### World Map
Player-facing (labelled): Siderosv11.jpg (1260x952px JPEG) — GM reference only until unlabelled version arrives.
High-res master: Sideros-v1-(1).png (27.7MB PNG) — on Google Drive.
Unlabelled base: requested from designer June 12, 2026, awaiting response.
Plan: World Anvil interactive map, progressive pin reveal as players discover locations.
GM layers planned: Coil cell locations, Argent Spire approach route, Scion positions, intel operations.

### World Bible
Map_Quote.xlsx — 8-sheet world bible. Contains: civilisation overviews, cultural architectures, legendary beast lairs, trade routes, political geography, resources, environmental systems, physical geography, complete zodiac matrix (13 civilisations x 13 signs = 169 named positions).

---

## PENDING RESOLUTIONS

1. **Ashélands naming:** Document uses "Orun-Ayé"; project conversations use "Orsha-Anu." Which is current canon? (Unresolved.)
2. **Number 56:** Pending character creation. If any player's Fate Number falls 55-58, they are Number 56. Their zodiac sign determines the fifth Resonant Binding component.
3. **Fifth Resonant Binding component:** Determined by Number 56's zodiac sign + corresponding Legendary Beast.
4. **Opening hook:** What draws this specific party into the campaign?
5. **World Anvil Application Key:** Submitted, awaiting approval.
6. **Clean unlabelled map:** Awaiting designer response.

---

## CORE COSMOLOGY

**The Pantheonic Fall:** 4,000 years ago, the twelve zodiac gods dissolved into cosmic force, leaving twelve Legendary Beasts (their undivided truth) and fragmenting their divine signal into thirteen cultural interpretations. The Hollow Serpent (Ophiuchus/thirteenth force) was partially sealed but not contained.

**The Crystalline Core:** The Hollow Serpent's fragment, sealed beneath Argent Spire in Antarctos (the secret southern continent). The Kallos-Sworn Comet-Magi guard it.

**The Loom of Fate:** Tracks every living creature's Fate Number (1-99). Void-Touched Numbers: 13, 66, 99. Fated Bonds form when people with compatible Numbers acknowledge their connection. Bond tiers: Paired (within 5 pts), Triad (within 4), Quad (within 2), Quint (within 1).

**The Resonant Binding:** Five-person ritual to permanently seal the Crystalline Core. Each of the five Quint Bond performers brings a physical component from their zodiac sign's Legendary Beast domain.

**The Weaver's Loom:** A physical location in the world — the lair of the Kelp-Weaver Leviathan (Aquarius Legendary Beast). A vast, magically-tended kelp forest surrounding the Aquarian Archipelago. A living ecosystem, not a structure. Visible on the world map between the main continent and Antarctos.

---

## THE 13 CIVILISATIONS

| Civilisation | Cultural Tradition | Key Detail |
|---|---|---|
| Duchy Compact / Terra Firma | Western (Lord/Lady titles) | Primary campaign setting |
| Boreal Expanse | Norse Runic (12 Hearths) | Jarl Skadi = Aquarius |
| Tuathan Archipelago | Celtic Tree Calendar | Fade-Guardians, Noctilith Moon-Stone |
| Shen-li / Jade Empire | Chinese 12 Animals | Azure Dragon Emperor = Leo; Gear-Forged cold war |
| Khem-Ma'at | Egyptian Solar | 13 Dragon Lords; Sun-Kissed Adamas |
| Abyssal Sea Civilisation | Babylonian Maritime | The Great One = Leo supreme; Tiamat = 13th |
| K'uh-la'an | Mayan Day-Lords | Serpent-Kin homeland; Weep-Stone currency |
| Ashélands of [Orun-Ayé/Orsha-Anu] | Yoruba Orisha | Active contact with Great Roc fragment |
| Mori-Okami | Japanese Kami-Binding | Wolf-Shifter homeland; Grove of Fallen Stars |
| Great Kurgan Bog | Mongolian Sky-Earth | Bog-Keeper Oshen Varr = Scorpio |
| Chinvat | Persian Asha Tradition | Avian homeland; built Equilibrium's truth field |
| Scattered Temples | Hindu Rasi-Siddha | 12 temples worldwide; only cure for Void illness |
| Antarctos | Comet-Magi Celestial | SECRET southern continent; Argent Spire; Core |

The 13 Coil leaders ARE the 13th zodiac (Ophiuchus) manifesting in each civilisation through their specific cultural gateway. Aethar did not recruit them — he recognised them.

---

## THE ASHEN COIL TRIAD

**Aethar the Serpent Bearer** — Alpha, Fate 13 (Void-Touched). Pale, silver-white hair, void-black inverted-constellation Comet-Magi robes. Former 12th Circle Comet-Mage, Shifting Horizons Conclave. Does NOT know he killed the Fourth Architect. Planning Stage 3 approach to Argent Spire. Has the approach route memorised from when he was stationed there.

**Serath of the Closed Circle** — Omega, Fate 16. Medium-dark complexion, neat dark hair, operational gear and Cartographer tools. Has identified 3 of 5 Quint Bond members and WITHHELD from Aethar for 6+ weeks — first successful resistance in 4,000 years. Most significant redemption path. Carries Aethar's child (GM only). Does not know the Arrow is the Fourth Architect.

**Drava Nullsong** — Beta, Fate 19. Pale, silver-short hair, dark operational clothing. Runs the Fang of the Whisper network. Found Mael Cassiveth's location in Loom records — NOT told Aethar. Loyalty is personal (to Aethar and Serath as people), not ideological. Path to Serath runs through Drava.

**The Triad's bond:** An inverted Fated Bond — the first in history — formed when catastrophic Bond severance at the Night of Kallos corrupted Aethar's remaining connections. Holds through Void energy rather than the Loom's design. All three are surviving members of the original Four Architects.

**Aethar's Five Stages:**
1. Disrupt zodiac positions (blight-rot, political chaos, succession crises) — 60% complete
2. Prevent the Quint Bond from forming — active; Serath withholding 3/5 identities
3. Seize the Crystalline Core (remove the Three Conclaves) — not yet begun
4. Sever the Quint Bond catastrophically — requires Bond to be fully formed first
5. Force the Maw open using released energy — final goal

---

## KEY NPCs

**Mael Cassiveth (Fate 72, Omega):** The Lunar Queen — doesn't know it. Early 50s human, Port Damaris Harbormaster's Intelligence Ledger analyst. Identity hidden by altered records. Three intelligence operations watching him simultaneously: Fang, Loom, Order of Pure Reason — none fully aware of the others. Lord Leo (Fate 71) and Mael (72) are within 1 point — when they meet, Lord Leo will go silent; Mael will understand immediately.

**Arch-Oracle Lyra (Omega, Aquarius, Shifting Horizons):** Permanently blindfolded, sees probability futures. Has been waiting 40 years for the party. Her Resonant Binding plan is incomplete — misses cross-cultural synthesis the heroes provide.

**Riven Soll (Fate 53, Omega):** Former Stellar Cartographer, effective director of the Loom of Fate. Hiding 8 years (Fang targeting Cartographers in the 55-58 cluster). His Quad Bond includes the Arrow in disguise as "Cael." Has partial profiles on Inti-kora (55), Asha-Wing (57), Hinerangi (58). Cannot identify Matuā-kore (66) or Number 56.

**Harbormaster Issa Velm:** Port Damaris. 60s. Knows her analyst (Mael) is being surveilled and is furious.

**Mireth Coss:** Fang cell leader, Port Damaris. Watching Mael 6 weeks with no instructions from Drava. Growing restless.

**Sable Fen:** Loom operative, Port Damaris. Translation business cover. Filing urgent reports to Riven with no reply.

---

## PORT DAMARIS

Most important city in Campaign 1. A chaotic, anarchic city run by a council of pirate captains — the largest free port in the world. Built on a ridge with stratified tiers on Precursor-era pier foundations.

Districts: The Ledger (upper, administrative), The Anchorage (harbour), The Silk Quarter (merchant), The Whisper Walk (information brokers), The Deep (underground Shadow-Council).

Three simultaneous intelligence operations all watching Mael Cassiveth, none fully aware of each other: Fang of the Whisper (Mireth Coss, growing restless), Loom of Fate (Sable Fen, urgent reports going unanswered), Order of Pure Reason (still searching, observer in Silk Quarter).

---

## THE QUINT BOND

Five souls within 3 points of each other. Bond membership exclusive — anyone already in a bond is disqualified.

| Member | Number | Identity | Zodiac | Component |
|---|---|---|---|---|
| Inti-kora | 55 | Ceque-Keeper, Elethorn | Sagittarius | Star-Metal Antler Fragment |
| Number 56 | 56 | PENDING character creation | TBD | TBD |
| Regent Asha-Wing | 57 | Tidal Regent, Calm Harbour | Libra | Great Roc Feather |
| Hinerangi | 58 | Moana-kin, Te Moana-nui | Pisces | Cenote Water |
| Matua-kore | 66 (Void-Touched) | Te Kapo, Obsidian Deep | Scorpio | Stygian Scorpion component |

Asha-Wing and Lord Libra: Sign Resonance, NOT a Fated Bond. Asha-Wing is free for the Quint Bond.
The Shell (Cancer Scion) has sheltered one Quint Bond member in a secret refuge for 3 years.

---

## GM-ONLY SECRETS — NEVER REVEAL TO PLAYERS

### The Night of Kallos — The Full Truth
The Four Architects were performing the original Resonant Binding in a Quad Bond. At the critical moment, Aethar killed the Fourth Architect. The Hollow Serpent had been influencing him — it acted through him. He did not choose this consciously. The Wound then altered his memory. Aethar believes the Fourth Architect died in the ritual's collapse. He has spent 4,000 years studying accounts of his own crime without recognising himself in them.

The catastrophic Bond severance: destroyed the city of Kallos; compressed the Hollow Serpent into the Crystalline Core; created the first inverted bond in history (Aethar/Serath/Drava); the Wound filled the frequency-shaped absence left by the Fourth Architect's death.

Serath and Drava ARE the Second and Third Architects. They remember. They know. The inverted bond makes acting on this knowledge feel like tearing something out of themselves. In 4,000 years, neither has acted on it — until Serath began withholding intelligence 6 weeks ago.

The catastrophic irony: The Resonant Binding would free Serath and Drava by dissolving the Ophiuchus frequency feeding the inverted bond. They are on the wrong side of the war that would liberate them.

Aethar's plan is grief operating at civilisational scale. He wants the Wound to close. He doesn't know the Wound closes through the Binding's completion, not its prevention.

### The Arrow IS the Fourth Architect
The Arrow (Sagittarius Scion), embedded in Riven Soll's Quad Bond for 18 years as "Cael," IS the Fourth Architect. When Aethar killed the Fourth Architect, the Binding's energy converted the dying Architect into the Sagittarius Scion rather than simply killing them.

The Arrow does not know this. They carry witness-memory of the Night of Kallos and know who killed the Fourth Architect — not knowing they are reporting their own murder.

Aethar does not know the Arrow exists as the Fourth Architect. The Wound has the exact frequency-shape of the Arrow's absence. When close enough, the Wound will recognise the frequency.

Three-layer reveal:
1. Aethar killed the Fourth Architect; his memory was altered
2. Serath and Drava are the surviving Architects, bound 4,000 years
3. The Arrow IS the Fourth Architect (hold until the critical scene)

### Scion Shift System — NEVER TELL PLAYERS

| Scion | Shift Condition |
|---|---|
| The Ram-Who-Walks (Aries) | When what it started can no longer be stopped |
| The Unshifting (Taurus) | When Lady Taurus's mantras hold without support |
| The Twin (Gemini) | When both truths are acted on simultaneously by one person |
| The Shell (Cancer) | When the sheltered Quint Bond member safely emerges |
| The Named (Leo) | When it introduces Mael Cassiveth to themselves before the right witnesses |
| The Tending (Virgo) | When the original Virgo healing formulary is reintroduced and received |
| The Scale (Libra) | When it renders its 11-month paralysed judgment |
| The Kept (Scorpio) | When the Night of Kallos secret produces the action it was preserved for |
| The Arrow (Sagittarius) | When the Resonant Binding is completed — Arrow shifts into the Fourth Architect |
| The Long Road (Capricorn) | When its Precursor knowledge is successfully transferred |
| The Current (Aquarius) | When Scenario Seven is acted upon or permanently foreclosed |
| The Threshold (Pisces) | When someone crosses the boundary correctly |
| The Wound (Ophiuchus) | When the Binding seals the Core — the Wound closes; Aethar is freed |

The Arrow's shift: the Sagittarius force withdraws, the Fourth Architect returns mortal, carrying 4,000 years of experience and both sets of memories. They are the only person who knew Aethar before the Wound. Whether Aethar can receive that recognition is the campaign's last question.

The Kept (Scorpio Scion): has known for 3,900 years who killed the Fourth Architect. Has known that the Arrow reported their own murder without knowing it. Waiting for the right moment — shifts when the knowledge finally produces the action it was preserved to enable.

---

## FATED BOND RULES — KEY POINTS

- Each person has 1-4 fated mates. Total bond sizes: 2-5 people.
- One bond per person — being in any bond (including Thread State) disqualifies you from others.
- Sign Resonance (two zodiac-sign-aligned people) can mimic a bond pull but is NOT a bond.
- The Ashen Coil Triad = an inverted bond, the first in history, holds through Void energy not Loom design.
- Bond proximity numbers: Paired=within 5 pts, Triad=within 4, Quad=within 2, Quint=within 1.

---

## PROJECT FILES REFERENCE

| File | Contents |
|---|---|
| sideros_handoff_supplement.md | Full Lead-Scale mechanics, Void-Husk stat blocks, all 13 civilisation detail, all 13 Coil leader characterisations, Scion shift destinations, component acquisition detail |
| sideros_comprehensive_guide.docx | v14 print-ready player guide (176pp) |
| sideros_roll20_sheet.html/.css | Roll20 custom character sheet |
| sideros_world_manager.jsx | World Anvil management artifact |
| sideros_character_creation.html | HTML character creation guide |
| sideros_combat_rules.html | Full combat reference |
| sideros_fated_bond.html | Fated Bond system detail |
| Siderosv11.jpg | World map (labelled, GM reference) |
| Map_Quote.xlsx | World bible (8 sheets, sent to map designer) |

For full civilisation detail, all 13 Coil leader characterisations, Scion shift destinations, Void-Husk stat blocks, and Lead-Scale mechanics: read sideros_handoff_supplement.md alongside this document. That supplement remains fully current — it has not been superseded.

---
*The world is ready. Campaigns are imminent. Infrastructure is actively being built.*
*Current as of June 12, 2026.*
