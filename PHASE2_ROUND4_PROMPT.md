# Phase 2 Round 4 — Tafsir dictionary coverage 67% → ~76%

Paste-ready prompt for a fresh Claude Code session. Picks up where Phase 1
left off on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

Plan: `~/.claude/plans/lets-come-up-with-dazzling-lark.md`.
Memory: section "Phase 1 coverage tooling — SHIPPED 2026-05-28" inside
`judeo-arabic-app-project.md`.

**Phase 1 deliverables** (uncommitted in working tree, do not re-author):
- `lib/tokenize.ts` — zero-dep `tokenizeJa`
- `lib/lookup.ts` — re-exports tokenizer from `./tokenize`
- `scripts/_tokenize_ja_cli.ts` — stdin→JSONL CLI for Python callers
- `scripts/coverage_report.py` — measures hand/auto/miss coverage
- `scripts/verify_divergence.py` — citation + sources legend integrity
- `data/coverage-snapshot.json`, `data/coverage-misses.json` (regenerated)

**Baseline confirmed 2026-05-28:**
- 81,225 word-tokens
- hand 61.52% (starter 21.92% + lane 39.60%)
- auto 5.33% (Camel Tools, badge: "auto · Unverified")
- miss 33.15% — 12,947 unique surface forms
- Per-book miss rate: bereshit 33.5 / shemot 33.7 / vayikra 32.9 / **bamidbar 30.6 (best) / devarim 35.0 (worst)**

## Goal of Round 4

Drive **hand-coverage 61.5% → ~70%** (+8 pts) by curating the top miss
surface forms into `data/dictionary-lane.json` — either as new lemma
entries, or as `variants[]` on existing stems.

**Three sub-batches in order:**

### Batch A — Proper names (~25 entries → ~+2 pts)

Pure-add. Mine `data/coverage-misses.json` for hits matching Saadia's
place-name and patriarchal-name conventions:

- Moab (מואב), Abram (אברם), Judah (יהודה), Rachel (רחל), Leah (לאה),
  Sodom (סדם), Eleazar (אלעאזר), tribal names (גאד, אשר, נפתלי, …)
- Place-name identifications from Saadia's gazetteer (already documented in
  `data-source/saadia-gloss-table.json` and the project memory):
  Nile=פישון, Zawila=חוילה, Tigris=חידקל, Mosul=אשור, Abyssinia=כוש,
  Banyas=דן, Nablus=שכם, al-Khalus=גרר, al-Sharah=שעיר, al-Sadir=גשן,
  Ein Shams=רעמסס, Qardu=אררט, al-Ardan=ירדן

Author each as a new lane entry with `gloss_en`/`gloss_he` carrying the
biblical identification; do NOT add `saadia_note` — these are general
geographic identifications, not Saadia twists. Variants include any
prefixed forms in misses (אלארדן etc.).

### Batch B — w-prefixed verbal perfects (~20 stem additions → ~+2 pts)

The composable prefix chain handles ו-strip only if the **underlying stem
exists in lane**. Many don't. From the miss queue: ולדת (27), פולדת (21,
פ+ולדת — fa-perfect), ונזלו, ורחלו, וקאלו, וקל, ואצנע, וצבג'.

Strategy: identify the verbal root (ילד "give birth", נזל "descend",
רחל "depart" — already in lane but לדת is the תפעלה masdar form, distinct
from ולד "child"). Add stem entries with paradigm variants:
- perfect 3ms/3fs/3pl: -, ת, ו
- imperfect: י-, ת-, נ-
- masdar (ולדת, וקאל, …)
- f/w-prefixed perfects (this is the new bucket — פ+ולדת etc.)

**Decision:** the existing prefix chain strips ו but NOT פ-when-followed-by-vav-then-stem. If `פולדת` keeps coming up despite ולדת being in lane,
either (i) add `פולדת` as an explicit variant, or (ii) audit whether the
chain's [ב ל כ פ]-strip walks past the ו. **Check `lib/lookup.ts:lookup`
first** — `for base in [tok, after_vav]` may already cover this; if it
does, the miss is just because the underlying ולד-paradigm stem isn't yet
in lane.

### Batch C — Saadianic stems missing from lane (~30 entries → ~+4 pts)

Highest-value bucket — these are common Saadia vocab Saadia uses
heavily but isn't yet curated. From the miss queue:
- אלמחצ'ר (132 — tent of the assembly, Saadia's אהל מועד rendering)
- תכלימא (81 — speech masdar for Sinai dialogue)
- אלמצריון (68 — Egyptians)
- מר (67 — to pass)
- ועשירה (54 — clan / משפחה)
- הוד'א (53 — behold this)
- לעשאירהם (49), אלגמאעה (49 — assembly)
- ברייה (29 — creature, creation), גהה (22), גמלה (21), חתא (21),
  תעמלו (21), אמץ (21), פצאר (21)

For each: lemma + paradigm variants + `gloss_en/he`. **`notes` must be
cross-text safe — no Saadia/Tafsir mention.** Saadia-specific commentary
(e.g. אלמחצ'ר as Saadia's אהל מועד substitution) goes in `saadia_note`
per the [[scope_saadia_notes]] convention. Reserve `scope:"saadia"` ONLY
for entries whose primary `gloss_en` is itself a Saadia coinage (rare —
two such entries exist today, גלד and מסתבחרה).

## Per-batch workflow

1. **Refresh the misses file:**
   ```
   python3 scripts/coverage_report.py
   ```
   Re-reads dicts and rewrites `data/coverage-misses.json`. ~4 min runtime
   (cheap optimization: batch all 187 chapter files into one `npx tsx`
   subprocess call instead of per-chapter; left as TODO).
2. **Build a Python `apply_round4_X.py` script** (mirrors prior pattern in
   `/tmp/apply_variants*.py` per memory):
   - Declare `NEW_ENTRIES` list (lemma + ar + gloss_en + gloss_he + variants
     + optional saadia_note)
   - Declare `VARIANTS_PATCH` dict keyed by stem (for additions to existing
     entries)
   - Read `data/dictionary-lane.json`, merge, write back
   - Re-validate JSON: `python3 -c "import json; json.load(open('data/dictionary-lane.json'))"`
3. **Re-run coverage:** `python3 scripts/coverage_report.py` and confirm
   the delta. Target +2 pts (A) / +2 pts (B) / +4 pts (C) per batch.
4. **Re-run `scripts/scope_saadia_notes.py`** after Batch C to catch any
   Saadia commentary that slipped into `notes` (idempotent — safe to
   re-run).
5. **Build check:** `npm run build` — must remain clean (215+ pages).
6. **No commit yet** — working tree stays uncommitted per project pattern.

## Verification at end of Round 4

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 69%**
  (stretch: ≥ 70%). If you hit 70%, Round 4 is done.
- `python3 scripts/verify_divergence.py` exits 0 — divergence is untouched
  but re-verify to confirm nothing regressed.
- `npm run build` clean.
- Spot-check 5 random tafsir chapters in dev (`npm run dev`, visit a few
  `/tafsir/<book>/<ch>` pages, tap on previously-missing tokens like
  אלמחצ'ר and confirm the gloss panel now opens).

## Gotchas

- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts:38-44` policy: `אלאה ≠ stem אלא + suffix`).
- **Trailing-apostrophe lemmas** (טאעה' style) will never match — store
  bare `טאעה` and add `'`-suffixed variant if needed.
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note`. The Advanced reader hides `saadia_note` entirely.
- **Homographs are fine** — keep separate entries for `מר` (pass) vs `מר`
  (bitter), `רחל` (Rachel) vs `רחל` (depart). The UI shows both on tap.
- **`coverage_report.py` runs ~4 min** — if you're iterating fast,
  optimize first by batching all chapter strings into one `npx tsx`
  invocation (single-line refactor in `tokenise_via_cli`).
- The Phase 1 memory section + the plan file have the full breakdown; this
  prompt is the operational summary.

## After Round 4

Next steps in plan order: Round 5 (~76 → ~84% via pronoun-suffix
variants; extend `scripts/generate_lane_entries.py` with `--variants-only`
mode), then Round 6 (~84 → ~90% via the scripted Sonnet pass), then retire
the auto-dict badge once hand ≥ 85%. Phase 3 (divergences 32 → ~180) and
Phase 4 (Word of the Day) run in parallel on independent files.

---

**Tell Claude:** "Start Phase 2 Round 4 per `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`. Run Batch A first (proper names) and report the coverage delta before moving to B."
