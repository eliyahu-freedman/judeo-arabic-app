# Dictionary Coverage — NEXT (self-contained prompt for the next session)

## Where we are (2026-06-02, after Batch 1)

The Saadia-Tafsir reader's tap-to-define dictionary resolves in three tiers
(`lib/lookup.ts`): hand **starter** (53) → hand **lane** (790) → unverified
**auto** Camel (2,322). Measured by `scripts/coverage_report.py` over 81,225
tokens:

- **hand 78.11% · +auto = 81.42% covered · 18.58% miss** (15,094 occurrences /
  10,265 distinct surface types).
- Per-book hand: bamidbar 82.4 · vayikra 79.6 · shemot 78.7 · bereshit 76.0 ·
  **devarim 74.4 (weakest)**.
- Batch 1 shipped +133 verified lane entries (`scripts/apply_dict_batch1.py`,
  data in `data/_dict_batch1.json`); see `DICT_COVERAGE_BATCH1_SESSION_NOTES.md`.

**North star (`PHASE2_ROUND6_PROMPT.md`):** once **hand ≥ 80%**, retire the noisy
Camel auto-dict — a one-line UI change in `app/tafsir/reader.tsx` + disable the
`auto` tier in `lib/lookup.ts`. We are **1.89 points away**.

## Mechanics you must respect (read the code first)

- Dict files are `{... , "entries":[]}`. Entry schema: `{id, lemma_ja, lemma_ar,
  root, pos, gloss_en, gloss_he, source, variants[], notes?, saadia_note?}`.
- `lib/lookup.ts` candidate-chain strips leading ו / אל / one of ב·ל·כ·פ +
  final-letter normalization (ך→כ ם→מ ן→נ ף→פ ץ→צ) + trailing-`'`, and matches
  `lemma_ja` OR any `variants[]` entry. **It does NOT strip pronominal suffixes**
  (־ה ־הא ־הם ־ך ־כם ־י ־נא ־הא …) — so an inflected/suffixed surface only
  resolves if it is listed as a `variant`.
- Corpus verses (`data/tafsir-{book}-{ch}.json`) carry aligned `hebrew` +
  `hebrew_translation` next to `ja` — use them to ground every gloss in real
  usage (no guessing). Reserve arabic-lexicon (Lane / `blau-judeoarabic`) for
  Saadia-specific or non-obvious senses. Never fabricate.
- Always run `coverage_report.py` before and after; it rewrites
  `data/coverage-snapshot.json` + `data/coverage-misses.json` (top-1000 ranked).
- node_modules is absent in this checkout → `npm install` before `npm run build`.

## Batch 2 — variant augmentation (recommended; low-risk, data-only)

The single biggest remaining lever is **pronominal-suffix misses**: a large share
of the 10,265 uncovered types are `<stem>+suffix` of a stem that already has an
entry. Closing them is purely additive to existing `variants[]`.

1. **Harvest the targets.** Two sources:
   - The 55 "already covered" rows in `data/_dict_batch1_deferred.json` — each is
     a stem that EXISTS but lacks the miss surface. Confirmed live still-misses:
     `ויד'בחה`→stem `ד'בח`, `אלאיימה`→`אמאם`, `אזואגא`→`זוג`; plus from the Batch-1
     worklist: `אעטי←אעטיהא/אעטיה`, `יאכל←יאכלונה`, `עין←עינאה`, `קאל←וקאלא`,
     `מות←מותה`, `קריה←קראהם`, `עדו←אעדאיה`, `מעדוד←מעדודי`, `קצבה`, `ג'שא`,
     `קדם`, `סמא`, `כ'דם`, `כ'דמה`, `למא`, `כבר`, `מת'ל`, `מרכב`, `בהימה`, …
   - Fresh `data/coverage-misses.json` ranks ~250–600: group surfaces by stem.
2. **For each target stem, find the existing entry** across starter/lane/auto
   (search `lemma_ja` + `variants`). Confirm its sense matches the miss surface's
   meaning (read an aligned corpus occurrence). Then **append the miss surface(s)
   to that entry's `variants[]`** (dedup). If the stem lives only in the *auto*
   tier, instead author a proper hand **lane** entry (lane outranks auto) carrying
   the variants, rather than editing unverified Camel data.
3. **Also append net-new stems** for misses whose stem has no entry yet (same
   stem-grouping + corpus-grounded gloss method as Batch 1).
4. **Apply** via a new `scripts/apply_dict_batch2.py`. Mirror
   `scripts/apply_dict_batch1.py`, but it needs a **PATCH mode** for variant
   augmentation: find entry by `lemma_ja` in the right file, extend `variants[]`
   (dedup), write back `json.dumps(..., ensure_ascii=False, indent=2)+"\n"` +
   re-parse. Keep the append path for net-new entries with the same dedup guard
   (skip if lemma_ja/variant already resolves, incl. vs `tafsir-divergence.json`).
5. **Measure + build + notes.** `coverage_report.py` before/after (target hand
   ≥ 80%); `npm run build` clean; write `DICT_COVERAGE_BATCH2_SESSION_NOTES.md`.

## After Batch 2 clears ≥ 80% hand

**Retire the auto-dict** (separate small change): per `PHASE2_ROUND6_PROMPT.md`,
remove the `source:"camel"` badge in `app/tafsir/reader.tsx` and disable the
`auto` tier in `lib/lookup.ts`. Re-run `coverage_report.py` (covered will drop by
the ~3.3% auto contribution — expected; the point is hand-only quality). Verify
the reader still renders cleanly.

## Stretch (higher value, higher risk — its own tested PR)

Teach the candidate-chain to **strip pronominal suffixes** in BOTH `lib/lookup.ts`
and its mirror `scripts/verify_divergence.py:candidate_chain`. This would
auto-resolve thousands of inflected misses at once. Risks: over-matching
(spurious hits) and breaking the divergence verifier's per-verse resolution.
Gate it behind tests: run `verify_divergence.py` (must stay PASS, 0 warnings) and
`coverage_report.py` (misses must drop without false hits — spot-check a sample).

## Verified pass over the ~22 med/low deferrals

In `data/_dict_batch1_deferred.json`: Saadia-specific senses worth proper
arabic-lexicon verification — `דארום` (Negeb→fortress near Gaza), `חרג` (curse),
`נעמא` (asseverative "indeed"), and uncertain Arabic forms `אמהאג` (bars?),
`בדרה` (measure), `תוניה` (tunic), `צידא`, `שפאהא`. Verify or drop; don't ship
unverified Saadia-specific glosses.

## Files of record

- `data/dictionary-lane.json` (790; appended), `data/dictionary-starter.json`,
  `data/dictionary-auto.json`
- `data/coverage-snapshot.json` + `data/coverage-misses.json` (regenerate)
- `scripts/coverage_report.py`, `scripts/apply_dict_batch1.py`,
  `scripts/build_auto_dict_camel.py`
- `lib/lookup.ts`, `app/tafsir/reader.tsx`
- `DICT_COVERAGE_BATCH1_SESSION_NOTES.md`, `data/_dict_batch1_deferred.json`
- Memory: `judeo-arabic-dictionary-coverage` (in the daily-rashi project memory)
