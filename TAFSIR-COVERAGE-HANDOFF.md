# Handoff — Tafsir dictionary coverage to ~100%

Run from `~/Code/judeo-arabic-app`. The Saadia-Tafsir reader shares `dictionary-starter.json` +
`dictionary-lane.json` with the Advanced reader, so every entry authored here also lifts the
Advanced library (and vice versa).

## State (2026-06-05)
- Overall Tafsir hand-coverage **97.21%** (92.72% → Bereshit pass → 95.66% → Bamidbar pass → 97.21%).
- **Bereshit = 100.0% and Bamidbar = 100.0% (0 misses) — done.** Per-book remaining:
  shemot 92.67% (~1,225 miss), vayikra 93.38% (~810), devarim 98.47% (~231).
- lane = **7,900 entries** (Bamidbar pass: 7,059 → 7,453 → 7,900, +841 over two ~500-group bursts).
- **Bamidbar took 2 workflow bursts** (961 residual groups → +394, then 501 tail groups → +447;
  the 2nd burst used `total=510, CHUNK=51` = 10 agents covering the whole frequency-1 tail at once).
  Commit this pass: see git log on `feat/advanced-reader-coverage`.
- **Bug fixed this pass — `apply_dict_advanced.py` now dedups by CONTENT, not id.** The workflow
  mints author ids as `taf-h-{start}-{i}`, which are NOT unique across runs, so the old id-equality
  skip silently dropped ~345/400 genuinely-new entries every re-run (a 450-group batch was moving
  coverage only +0.09%). The rewrite (a) mints a unique id on collision instead of skipping, and
  (b) folds suffixed/prefixed misses (חמיר → חמירהם) into the existing stem's `variants[]`. Same
  450-group batch then moved Bereshit +3.97% / overall +1.07%. Any future run benefits automatically.
- **Caveat — the Workflow runner does NOT inject `args` into the script.** `args:{total,chunk}` is
  ignored; the script's `let total = ... || 450` / `CHUNK || 45` defaults are what actually run.
  To change batch size, edit `scripts/tafsir_pilot_workflow.js`. Reliable burst ≈ 10 author agents
  (total≈450); a 19-agent burst hit the account session/usage limit mid-run and 15 agents authored
  nothing — keep bursts small or watch for the limit.
- **Remaining to ~100% (Shemot/Vayikra/Devarim): ~1,778 lemma groups** (re-run steps 1–3 per book
  to regenerate the worklist; the autopatch sweep keeps catching suffixed forms for free each pass).

## The pipeline (all built, reused from the Bahya/advanced pass)
1. `python3 scripts/stage_tafsir_misses.py all` (or a single book) → writes `data/_advanced_misses_grouped.json`
   (frequency-sorted lemma worklist; one book or whole corpus).
2. `echo "[]" > data/_dict_advanced.json && echo "{}" > data/_dict_advanced_patch.json` (reset staging).
3. `python3 scripts/autopatch_advanced_misses.py` → free suffix→existing-stem patches + `_advanced_misses_residual.json`.
4. Author the residual via the workflow (use the ABSOLUTE scriptPath; the Workflow runner resolves
   relative to the session cwd, which may not be this repo):
   `Workflow({scriptPath:"/Users/eliyahufreedman/Code/judeo-arabic-app/scripts/tafsir_pilot_workflow.js"})`
   — fan-out authoring agents (id prefix `taf-h-`), then a merge agent that concats → `apply_dict_advanced.py`
   → re-measures via `coverage_report.py` + `stage_tafsir_misses.py all`.
   `total`/`chunk` are EDITED IN THE SCRIPT (args are not injected — see caveat above); `total` = how
   many top-frequency residual groups to author this run. Clear `data/_bahya_authored/` + reset
   `_dict_advanced*.json` before each run, then re-stage that book and re-autopatch so the residual
   only holds still-uncovered groups (the workflow always authors residual[0:total]).
5. Repeat step 4 in chunks until `coverage_report.py` overall hand ≈ 100%; close the last ~2% tail
   (double-prefix / dup-lemma forms) with explicit patches like the Bahya tail did.

## Authoring rules (baked into the workflow prompt)
- `variants[]` MUST contain every observed surface verbatim (that's what makes a word covered).
- Biblical **proper names** → pos "proper noun", root "—", gloss_en = English name, gloss_he = Hebrew name;
  use Saadia's documented place-IDs (Nile=Pishon, Zawila=Havilah, Tigris=Hiddekel, Mosul=Ashur, …).
- Verify ordinary words against Lane/Blau (`~/Tools/arabic-lexicon/cli.py lookup`); never fabricate a root —
  use a trailing " (?)" for genuine guesses.

## Cheapest path (recommended for the bulk)
A lean **API batch script** (cached system block, ~40 lemmas/call, like `scripts/translate_tafsir_english.py`)
does the ~4,960 remaining entries for **~$8–12 on Sonnet** in ~2 hours — ~6× cheaper than the agentic
workflow (measured ~1,360 tokens/entry agentic vs ~225/entry API). Use the workflow for in-session chunks;
use the API script to finish the long tail.

## Verify
`python3 scripts/coverage_report.py` (overall + per-book) · `npx tsc --noEmit` · `npm run build`.
