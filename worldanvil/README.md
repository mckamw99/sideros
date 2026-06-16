# worldanvil/ — Staged World Anvil Import

Import-ready content for the Sideros World Anvil world, staged here so it can be
**retrieved and pushed once the World Anvil connector / Application Key is live**.
The build container that generated these files cannot reach `worldanvil.com`
(egress-blocked), so the actual push runs on Matt's machine.

## What's here

| File / dir | Purpose |
|---|---|
| `manifest.json` | Machine-readable index of every staged article (file, template, category, privacy, wave) + the wave plan and account-config to-dos |
| `articles/world/` | World primer (public-safe overview / campaign description) |
| `articles/kindreds/` | All 20 Kindreds as **Species** articles (World Anvil BBCode) |
| `articles/civilizations/` | Overview hub + 12 civilizations as **Ethnicity** articles (Antarctos excluded — secret) |
| `build_civilizations.py` | Generator for the Wave 2 civilization articles (hand-authored, secrets-stripped) |
| `convert_kindreds.py` | The converter that generated the Kindred articles from the canon HTML (handles both source schemas; re-runnable) |
| `import_to_worldanvil.py` | Local push script — Boromir v2 API, dry-run by default |

Each article is a `.md` file: a small YAML front-matter block (title, template,
category, privacy, wave, tags) followed by the **BBCode body** World Anvil expects.

## How to import (once the key is approved)

```bash
pip install pywaclient requests
export WA_APPLICATION_KEY="..."      # approved app key
export WA_AUTH_TOKEN="..."           # User -> API Tokens page
export WA_WORLD_ID="..."             # target world id

python import_to_worldanvil.py            # DRY RUN — inspect the payloads first
python import_to_worldanvil.py --live --wave 1   # push wave 1 for real
```

Verify the first created article in World Anvil before pushing the rest. Auth
(headers `x-application-key` / `x-auth-token`) and the `/api/external/boromir`
base are confirmed against the WA docs; the exact article CREATE field names
(template id, category id, draft state) should be confirmed on the first live call
— which is why dry-run is the default.

## Wave plan

1. **Wave 1 (staged ✓):** world primer + 20 Kindred species articles — player-facing, no secrets.
2. **Wave 2 (staged ✓):** civilizations overview + 12 civilizations. Antarctos is held back as a secret location for the Wave 5 private layer.
3. Wave 3: Paths & Weaving, Origins, core mechanics.
4. Wave 4: Legendary Beasts / bestiary / locations (incl. Port Damaris).
5. Wave 5: **GM-only** layer as separate private articles (NPCs, Ashen Coil, secrets matrix).

## Resolve before importing (account config)

- The **TTRPG system tag** (prior flag: incorrect / IP-problematic) — confirm or replace.
- **Public-safe primers** — this primer is secrets-stripped; keep any future overview articles the same.
- **World public title** — confirm.
- The **`Concordance` -> `Game Master`** canon decision is still open; some Kindred trait text
  preserves "Concordance" verbatim from source. Sweep these articles once Matt confirms the term.

## Privacy

Wave 1 is entirely player-facing. The GM-only layer (Wave 5) must be staged as **private**
World Anvil articles and is intentionally not included in this batch.
