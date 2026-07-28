# SIDEROS — WORLD ANVIL SESSION HANDOFF (v19)

**Session date:** 27 July 2026
**Scope:** World Anvil app-key approval → platform capability research → publication architecture decision → credential tooling
**Read this alongside:** `sideros_handoff_master.md` (canon), `CLAUDE.md` (repo orientation)

> **Why this doc exists:** the sandbox egress allowlist is fixed at conversation start, so
> a network-settings change requires a fresh chat. This carries the session forward.

---

## 0. FIRST ACTION IN THE NEW CHAT

Run this and report the result:

```bash
curl -sI https://www.worldanvil.com/ | head -1
```

| Result | Meaning | Next |
|---|---|---|
| `200` / `301` | Whitelist propagated | Claude can do WA read ops + dry-runs |
| `403` + `x-deny-reason: host_not_allowed` | Still blocked | Stay local-only; do not burn time on it |

**Nothing on the critical path depends on this.** The whitelist saves two local commands.
If it fails, proceed exactly as planned with local execution.

---

## 1. HOW WE WORK (unchanged)

- Matt makes all creative decisions. Claude proposes → Matt approves briefly → Claude executes → concise summary.
- Deliverables to `/mnt/user-data/outputs/`; working copies in `/home/claude/`.
- Structured output, tables preferred.
- Canon sweep before every player-facing push.
- Two-file discipline for anything with GM secrets.

---

## 2. WHAT THIS SESSION ESTABLISHED

### 2a. Account tier confirmed

The Boromir **API application key is a Grandmaster-tier-and-above feature**. Since the key
was approved, the account holds at minimum:

| Capability | Sideros application |
|---|---|
| Custom article templates | Native Kindred / Path / Working templates (deferred — see §4) |
| Custom statblock templates | **Use these.** Vitality / Guard Rating / Mastery Bonus, not HP/AC/Prof |
| Subscriber containers | Private blocks inside public articles |
| Polygonal / circular / custom / HTML / draggable map markers | Civilization territories; live party position |
| Content trees (organograms) | Kindred → civilization hierarchy |
| Random generators, rollable tables | Encounter tables, per-civilization name gen |
| 100 subscribers · 20 campaigns · 9 co-authors · 5 GB | Table + playtesters + beta readers |
| Selective visibility toggles, custom access-denied page | Article-level control |

### 2b. The platform constraint that drove the architecture

**World Anvil permissions are additive only.** Secrets and subscriber groups *grant*
visibility to named groups. There is no mechanism to hide something from one group while
showing it publicly — WA staff have confirmed this is a logged feature request with no
current workaround beyond spoiler tags and trust.

**Consequence:** anything that must never reach players cannot live in the public world at all.
Secrets are for *staged reveals*, not *inviolable separation*.

### 2c. RATIFIED — Two-world architecture

| World | Visibility | Contents |
|---|---|---|
| **Sideros** | Public (with private articles + secrets) | Kindreds, civilizations, geography, Paths/Callings/Origins, Workings, public bestiary, lexicon, known-history timeline |
| **Astrolan** | Private — subscribers: Matt + co-GM only | Coil Triad dossiers, Quint Bond tracking, Antarctos, Resonant Binding, Fang of the Whisper ops, labeled map, metaplot Chronicle |

*Astrolan* is deliberate: the formal archaic name, and the name Aethar uses.

**The graduation model.** Content moves *up* as the campaign reveals it:

```
Astrolan (never-player)  →  Sideros secret (staged reveal)  →  Sideros public
```

Placement test is **not** "will players eventually learn this." It is
**"what does a premature leak cost."** If the answer is *an arc*, it starts in Astrolan.

**Accepted cost:** the autolinker, "referenced in" backlinks, and search are per-world.
Cross-world references are manual. Judged worth paying — a papercut versus an
unrecoverable leak.

**Why this over procedural discipline:** see §3. The rule was already in force and still
produced ~163 leaks. This makes separation a property of the system rather than of
sustained human attention.

---

## 3. CRITICAL FINDING — CANON SCAN RESULTS

Scanner built this session: `canon_scan.py` (two independent scan sets, exits nonzero on
any hard-secret hit). Run against `/mnt/project` HTML+MD canon set.

### Wave 2 is BLOCKED

`sideros_three_new_cultures.html` — direct source for ≥3 Ethnicity articles — carries
**32 hard-secret hits**, structurally woven into the cultural writeups:

| Leak | Count |
|---|---:|
| Three of the four Quint Bond member names, **each with Fate number attached** | 12 |
| "the Quint Bond" (incl. a section header) | 4 |
| Fang of the Whisper | 6 |
| Serath (incl. "has identified all three new-culture members") | 3 |
| Four Architects | 2 |
| Resonant Binding | 2 |
| Drava Nullsong | 1 |

`sideros_zodiac_cultures.html` adds 4 more. Antarctos appears only as a Comet-Magi
reference — consistent with its exclusion.

**Requires sentence-level rewriting, not find-and-replace.**

### Wave 1 is nearly clean

One hard-secret hit: the Star-Metal Stag antler entry in `sideros_kindred_compendium.html`
calls the fragments "a component of the Resonant Binding ritual." Cut that clause.

Vocabulary sweep needed: Concordance ×27, Moana-kin ×16, channel/channeling ×11,
Aetheric Channels ×8, Comet-Mage ×1.

### Broader: 19 player-facing files, ~163 hard-secret hits

| File | Hits | Notable |
|---|---:|---|
| `sideros_three_new_cultures.html` | 32 | member names + Fate numbers |
| `sideros_kallos_sworn.html` | 29 | member name in Path text |
| `sideros_legendary_depth.html` | 23 | "all five members" |
| `sideros_fated_bond.html` | 14 | "all five members", "fully acknowledged" |
| `sideros_zodiac_attunement.html` | 13 | Fate 55–58 range |
| `sideros_origins.html` | 10 | Quint Bond Adjacent |
| `sideros_paths_unique.html` | 9 | **Stellar Cartographer leak still present** |
| `sideros_character_creation.html` | 8 | see warning below |
| `sideros_mechanics_codex.html` | 1 | **member name in a rules line (L164)** |
| 10 others | 1–4 each | mostly Resonant Binding / Fang of the Whisper |

**Two highest-severity — member names in mechanics text:**
- `sideros_mechanics_codex.html` L164 — Kore-kore overload rule ends by naming a member as immune
- `sideros_kallos_sworn.html` — names a member in connection with the sixth Binding component

**Live-site warning:** `sideros_character_creation.html` is the source for the public
GitHub Pages page. The published copy was sanitized; **the source was not.** Any rebuild
from source re-leaks. Diff live vs source before touching it.

**Scanner caveat:** strips tags and reads prose. Cannot distinguish a GM-only callout box
from body text — some hits may already sit inside marked GM sections. Needs eyeballing.
Also cannot see text baked into images.

---

## 4. RATIFIED DECISIONS

| Decision | Call | Reasoning |
|---|---|---|
| Two-world split | **Yes** | §2c |
| Custom **statblock** templates | **Yes, before any statblock exists** | Stock blocks are 5e-shaped; adopting them re-imports HP/AC/Proficiency into a corpus deliberately purged of them. No sunk cost — no statblocks yet. |
| Custom **article** templates | **Defer ~3 months** | Waves 1–2 already drafted against stock Species/Ethnicity. Stock Species `Related Ethnicities` field auto-generates the Kindred→civilization organization tree for free. Design custom templates against real friction, not predicted friction. Templates are swappable; content is the expensive part. |
| Credential handling | **Local-first** | §6 |

---

## 5. TEMPLATE MAPPING

| Sideros concept | WA template | Note |
|---|---|---|
| 20 Kindreds | Species | `Related Ethnicities` auto-builds the org tree |
| 13 civilizations | Ethnicity | Wave 2 |
| Cities | Settlement | Port Damaris first |
| Comet-Magi, Kallos-Sworn, nations | Organization | has diplomacy webs |
| Legendary Beasts | Species (or Character if named/personified) | |
| Workings | Spell | |
| Weaving, the Loom, Fate | Physical/Metaphysical Law | |
| Attunement rites | Tradition/Ritual | |
| Paths, Callings, Origins, mechanics | Generic Article | WA explicitly recommends Generic for RPG mechanics |
| Aetheric artifacts | Item / Material | |

**Features worth exploiting, not yet planned for:**
- **Chronicles** — interactive map + horizontal timeline, 4 parallel lanes, per-event privacy. Near-purpose-built for the Serpent Bearer metaplot. Put it in Astrolan.
- **Storyteller Notes** — private field on every timeline event; a second GM layer needing no secret object.
- **Variables** — define canon terms once, reference everywhere, change globally.
- **Discord webhooks** — new article → campaign Discord.

---

## 6. CREDENTIAL KIT (built this session)

Files delivered to outputs — **Matt should have downloaded these; if not, rebuild**:

| File | Purpose |
|---|---|
| `SETUP_CREDENTIALS.md` | Five-minute setup, exit codes, safety notes |
| `env.example` | Template with placeholders (safe to commit) |
| `wa_config.py` | Loader, redaction, client factory, `assert_not_astrolan()` rail |
| `wa_preflight.py` | Read-only credential check; active reachability probe |
| `gitignore.snippet` | Lines to append before creating `.env` |
| `canon_scan.py` | Two-set scanner; gate the sync on it |

`BoromirApiClient` signature **verified against installed pywaclient**:
```python
BoromirApiClient(name, url, version, application_key, authentication_token)  # 5 positional
```

pywaclient endpoints include `/secret` and `/subscribergroup` — **the whole GM/player
layering can be scripted**, not just article pushes.

**Exit codes:** `0` OK · `2` config · `3` auth rejected · `4` network/proxy/Cloudflare.
Exit 4 means credentials were never tested — do not regenerate keys.

### Credential handling policy

**There is no private storage in Claude's sandbox.** Uploads and project-knowledge files
are readable text in the transcript. A credential file Claude can read is a credential file
in conversation history.

| Operation | Where |
|---|---|
| Drafting, script-writing, canon scans | Claude |
| Read ops, dry-runs | Either (if whitelist works) |
| **Live writes, bulk pushes, anything destructive** | **Matt's machine** |

Never paste the app key or auth token into chat. `.env`, chmod 600, gitignored.
Verify with `git check-ignore -v .env` **before** creating the file.

---

## 7. PLATFORM GOTCHAS

- **Map canvas size is permanent in practice.** Replacing the base image with a different
  size does not delete pins but requires repositioning every one. WA's own advice: build on
  a canvas larger than currently needed and reveal progressively. **Fix dimensions before
  placing a single pin** — relevant to the incoming unlabelled cartographer map.
- **Map deletion is irreversible** and takes all pins, layers and settings.
- **"Open Secrets" world setting** exposes all secrets to co-owners/editors regardless of
  subscriber group. Must stay OFF if any player gets edit rights on their character article.
- **Cloudflare** intermittently returns a bot-challenge page instead of JSON on Boromir
  calls. Known issue, not a credential problem.
- **Boromir is beta** and not backward-compatible with Aragorn. Pin the pywaclient version.
- Subscribers count once regardless of group membership — 100 seats is ample.

---

## 8. BUILD ORDER

1. Create **Astrolan** (private) first. Move every GM secret there before anything goes live.
2. Create **Sideros** (public).
3. `wa_preflight.py --list-worlds` → paste UUIDs into `.env`.
4. Set world RPG system; **build the Sideros statblock template**.
5. **Wave 1 scrub** (vocabulary sweep + Stag antler clause) → push.
6. **Map**: fix canvas size → base layer → marker groups → pins.
7. **Wave 2 rewrite** (sentence-level) → push.
8. **Chronicle** for the metaplot, in Astrolan.
9. Subscriber groups — one per player + one party group — once players exist.

---

## 9. IMMEDIATE NEXT TASK

**Wave 2 rewrite.** Needs no API access, no whitelist, no credentials — can start immediately.

Rewrite the Te Kapo, Waka-tōhora, and Ceque-Keeper sections of
`sideros_three_new_cultures.html`:

- **Keep:** cultural material, navigational and perceptual practice, cosmology, the
  Ceque grid, Kore-kore reading, dark-zodiac perception
- **Cut:** all Fate numbers, all Quint Bond member names, all Coil surveillance and
  Serath/Drava intelligence, Four Architects lineage detail, Resonant Binding references
- **Replace:** the "The Quint Bond and All Three New Cultures" section with a player-safe
  cultural-significance section
- **Relocate:** everything cut goes to Astrolan as GM dossiers

Also queued: the Wave 1 vocabulary sweep (mechanical, 63 hits + one clause).

---

## 10. OPEN ITEMS CARRIED FORWARD

- Whitelist verification (§0)
- Player's Guide: export font-correct PDF; verify Index/Credits page numbers vs static TOC
- Repo canon sweeps still unpropagated (Concordance→GM, Comet-Mage→Comet-Magus, Threads rename, Waka-kin, Orun-Ayé, Nebula Thread)
- Stellar Cartographer Quint Recognition leak — fixed in Player's Guide, **still live in repo HTML**
- Diff live GitHub Pages Character Creation vs source
- Update repo `CLAUDE.md` with: two-world convention, graduation rule, scanner as pre-push gate
- Trilogy: ratify Nebula Thread immunity; name F (proposed Vaiora); name M2's people; name the simurgh
- Map commission: unlabelled base still pending

---

*Canon terminology, cosmology, Kindred/Path/civilization lists, and GM secret inventory:
see `sideros_handoff_master.md`. This document does not duplicate them.*
