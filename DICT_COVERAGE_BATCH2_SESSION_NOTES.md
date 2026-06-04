# Dictionary Coverage — Batch 2 session notes (2026-06-02)

Continuation of `DICT_COVERAGE_NEXT_PROMPT.md`. Goal: push tap-to-define **hand
coverage to ≥ 80 %** via variant augmentation + net-new stems, then retire the
unverified Camel auto-dict.

## Result

| metric | before (Batch 1) | after (Batch 2) |
|---|---|---|
| hand_pct | **78.11 %** | **80.39 %** |
| hand-lane hits | 45,250 | 47,103 |
| hand total hits | 63,445 | 65,298 (+1,853) |
| miss occurrences | 15,094 | 13,451 |
| unique miss surfaces | 10,265 | 9,729 |
| lane entries | 790 | 834 (+44) |

Per-book hand %: bereshit 76.02→78.41 · shemot 78.67→80.81 · vayikra 79.61→81.75
· bamidbar 82.43→84.56 · devarim 74.38→76.96 (devarim still the laggard; covered
80.67 %). Target met with ~0.39 pp margin (~315 tokens).

## What shipped

**Variant augmentation (PATCH)** — 157 existing entries gained +304 variants.
The lookup chain (`lib/lookup.ts`) strips leading ו / ב-ל-כ-פ / אל and normalizes
finals + trailing-apostrophe, but does **not** strip pronominal/verbal suffixes,
so every suffixed corpus miss-surface of an already-covered stem was added
verbatim to that entry's `variants[]` (the exact surface always resolves via the
chain's layer-1 candidate — no over-/under-stripping). Sources: the harvest's
auto-grouping of the top-1000 misses by stem, plus hand-routed double-prefixed /
verbal-prefixed forms the single-strip pass missed (e.g. פליקרב→קרב, אלאיאת→איה,
ממלכה→מלך, יעבדוני→עבד, אקדס→קדס, חמיר→חמאר, אצייר→צייר).

**Net-new stems (APPEND)** — 44 corpus-grounded lane entries. Each gloss was
checked against an aligned corpus occurrence (Hebrew anchor) before shipping —
e.g. קץ "recount" (וַיְסַפֵּר), נעמא "rightly so" (כֵּן), חוץ' "basin/laver"
(כִּיּוֹר), חרג "imprecatory oath/curse" (אָלָה), איקין "certainly", רד "return/
give back" (שׁוּב/הֵשִׁיב), מרכב "chariot", בעץ "some / one-another"; proper nouns
סעיר, הרן, בתואל, אהליבמה; common nouns מטר, רמאד, ריח, סמכה, סרג, מג'ארה, גנאח,
חאיט, צנם, רסל, etc.

**Auto-dict retired.** `lib/lookup.ts` no longer imports `dictionary-auto.json`
or consults the Priority-3 Camel tier; `app/tafsir/reader.tsx` no longer renders
the `auto` badge (`SourceBadge` returns null for camel). `dictionary-auto.json`
is kept on disk for the coverage report's informational `auto_pct` only. Coverage
report still prints auto=3.05 % — that is what was given up; effective app
coverage is now hand-only = 80.39 %.

## Pruned (false-friend suffix-strip matches, NOT shipped)

`al-prefix-bare` (אלה — ambiguous), `b1-חד` (וחדהא = waḥd "alone", not ḥadd
"blade" → re-authored as new `wahd-alone`), `ay-namely`/אלאיאת (= "signs" →
routed to `b1-איה`), `li-to`/כליהמא (= "both"), `kull`/אלכלי (= "kidneys"),
`burr-wheat`/ברי, `zala-deviate`/נזולה (= nazala "descend"), `qila-curtain`/
אלקלעה (= "fortress" → new `qalʿa-fortress`), `marra-pass`/אמרני (= "commanded"
→ routed to `amr-matter`), plus אלאתון "furnace" and רגליה "feet".

## Deferred (intentional, not regressions)

- קצבה plural-forms — קצבה is a **divergence twist** (`tafsir-divergence.json`);
  a lane entry would shadow its panel, and divergence forms aren't counted as
  hand coverage. Left to the divergence card.
- מדה (mudda "period") collides with the existing `madda-stretch` entry (same
  consonants, different sense); not forced in, to avoid a wrong gloss for מדתך.
- Saadia-specific deferrals (דארום, ראם, ת'רא, צריח, יפאע, תוניה, תופי …) — the
  divergence-overlap / Saadia-coinage set from `_dict_batch1_deferred.json`;
  still deferred (was item #4 in the brief, out of this session's scope).

## ⚠ Incident: lane file lost & recovered (read before re-running)

`data/dictionary-lane.json` (the 790-entry hand dict) was **uncommitted
working-tree state** built by prior-session apply scripts (HEAD has only 284).
A `git checkout -- data/dictionary-lane.json` during this session destroyed the
790 file (no stash/branch/dangling-blob copy existed). **Recovered in full** from
the Turbopack build sourcemap — `.next/server/chunks/ssr/_0rip7_-._.js.map`
embedded the original JSON in `sourcesContent`; extracted, restored, and
verified bit-for-bit against the 78.11 % baseline (hand-lane 45,250). A backup
of the recovered base sits at `/tmp/dictionary-lane.recovered-790.json`.
**Lesson: commit the dict, or never `git checkout` it without a backup.** The
18 round/batch1 apply scripts only rebuild it to 711 — the remaining ~79 entries
came from `generate_lane_entries.py` (a non-deterministic LLM generator whose
`/tmp/ja-candidates.json` input is gone) and are NOT reproducible from scripts.

## Pipeline / files

- `scripts/batch2_harvest.py` — groups misses by stem → augment vs new;
  writes `data/_batch2_worklist.json`, `data/_batch2_patch_auto.json`.
- `scripts/_build_batch2_inputs.py` — prunes the auto-grouping + adds hand
  routes + authors `NEW_ENTRIES`; writes `data/_dict_batch2_patch.json` and
  `data/_dict_batch2.json`.
- `scripts/apply_dict_batch2.py` — PATCH (extend variants by id) + APPEND
  (new stems; dedup against hand dicts + divergence ONLY, not auto).
- `scripts/coverage_report.py` — before/after measurement (unchanged).

Re-run from repo root: `python3 scripts/_build_batch2_inputs.py && python3
scripts/apply_dict_batch2.py && python3 scripts/coverage_report.py` against a
790-entry `dictionary-lane.json` base.

## Next

1. Continue descending the ranked misses (occ-4 tier still has ~1,400 occ) to
   push devarim/bereshit higher — same augment-then-new method.
2. The deferred Saadia-specific set (item #4 of the original brief).
3. Stretch: teach the candidate chain to strip pronominal suffixes
   (`lib/lookup.ts` + the `verify_divergence.py`/`coverage_report.py` mirrors) —
   would resolve thousands of inflected misses at once, but its own tested PR.
