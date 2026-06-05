# Handoff — Tafsir dictionary coverage to ~100%

Run from `~/Code/judeo-arabic-app`. The Saadia-Tafsir reader shares `dictionary-starter.json` +
`dictionary-lane.json` with the Advanced reader, so every entry authored here also lifts the
Advanced library (and vice versa).

## State (2026-06-04)
- Overall Tafsir hand-coverage **92.72%** (84.28% → 89.07% Devarim pass → 92.72% top-400 head).
- Devarim ≈ 98.3% (done). The four remaining books carry the bulk of the misses.
- lane = 5,768 entries. Commits: Devarim `1e5163d`, top-400 head `3ee6299`.
- **Remaining to ~100% (whole Pentateuch): ~4,539 lemma groups** (re-run steps 1–3 below to
  regenerate the worklist; the autopatch sweep keeps catching suffixed forms for free each pass).

## The pipeline (all built, reused from the Bahya/advanced pass)
1. `python3 scripts/stage_tafsir_misses.py all` (or a single book) → writes `data/_advanced_misses_grouped.json`
   (frequency-sorted lemma worklist; one book or whole corpus).
2. `echo "[]" > data/_dict_advanced.json && echo "{}" > data/_dict_advanced_patch.json` (reset staging).
3. `python3 scripts/autopatch_advanced_misses.py` → free suffix→existing-stem patches + `_advanced_misses_residual.json`.
4. Author the residual via the workflow:
   `Workflow({scriptPath:"scripts/tafsir_pilot_workflow.js", args:{total:<N>, chunk:45}})`
   — fan-out authoring agents (id prefix `taf-h-`), then a merge agent that concats → `apply_dict_advanced.py`
   → re-measures via `coverage_report.py` + `stage_tafsir_misses.py all`.
   `total` = how many top-frequency residual groups to author this run (size it to your token budget).
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
