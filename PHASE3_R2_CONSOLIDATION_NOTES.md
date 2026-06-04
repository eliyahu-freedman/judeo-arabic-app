# Phase 3 R2 — אלממתעה ↔ ממתעה Consolidation Session Notes

**Shipped:** 2026-05-30
**Apply script:** `scripts/consolidate_mamtuah.py` (one-shot, idempotent)
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Branch:** `advanced-library-kuzari` · working tree uncommitted per project convention

This is the deferred follow-on flagged as top-priority in both R2 Batch 1 and Batch 2 session notes. R2's promote-in-place-only scope forbade entry removal, so the duplicate could be surfaced but not fixed there. This pass removes the corpus's only known data-quality regression.

## Snapshot

| Metric | Before | After |
|---|---|---|
| Total entries | 124 | **123** |
| Tier distribution | 36 twist / 38 note / 50 gloss | **36 twist / 37 note / 50 gloss** |
| Duplicate lemmas | 1 (אלממתעה/ממתעה pair) | **none** |
| Entries covering Deut 23:18 | 2 (TWIST + NOTE) | **1 (`אלממתעה` only)** |
| TWIST cross-book breakdown | 3 three-book · 3 two-book · 29 single-book | **3 three-book · 4 two-book · 29 single-book** |

The 29 single-book TWISTs = 26 Bereshit-only + 3 within-book-strengthened (multi-verse, one book). `אלממתעה` becomes the **4th two-book TWIST**, joining מסלט · גוהר · חגב.

## What shipped

A duplicate-collision cleanup: the TWIST `אלממתעה` (Tamar pericope, Bereshit 38) and the NOTE `ממתעה` (Deut 23:18 prohibition) documented the **same** Saadia lexical move — rendering Heb קְדֵשָׁה/קָדֵשׁ through Ar مُمَتَّعَة (pleasure-object) rather than a consecration- or neutral-prostitute word. They are now a single 2-book TWIST.

## Per-entry rundown

#### DELETE — `ממתעה` (NOTE, ممتعة "cult-prostitute")
**Was:** note tier · 1 verse (Devarim 23:18) · sources `blau-dict, saadia-direct` · variants `ממתע, אלממתעה, אלממתע`.
**Action:** removed. Its distinctive theological analysis (the consecration-stripping / category-delegitimization argument) was **folded into the TWIST mechanism**, so nothing scholarly is lost. Its one new variant (`אלממתע`, masc. w/ article) was merged into the TWIST.

#### PROMOTE — `אלממתעה` (TWIST, الممتعة "temple-prostitute") — +1 verse, +1 book
**Was:** 3 verses, Bereshit-only (38:15, 38:21, 38:22).
**Added:** Devarim 23:18 (the legislative prohibition); variant `אלממתע`.
**After:** 4 verses across **2 books** (Bereshit + Devarim); variants `ממתעה, ממתעת, ממתע, אלממתע`; sources unchanged (`lane, saadia-direct, blau-dict`).
- **Mechanism rewritten** into a cross-Pentateuchal arc: NARRATIVE (Gen 38, three Tamar verses where Saadia routes זוֹנָה / הַקְּדֵשָׁה / קְדֵשָׁה through one Arabic terminus) → LEGISLATIVE (Deut 23:18, where the move carries extra theological charge — Saadia REFUSES the קדש consecration-frame and renames the figure by function not status, working the prohibition through category-DELEGITIMIZATION rather than category-EXCLUSION). Stale "see the separate NOTE entry" pointer removed.
- **`blau_dict.sense` rewritten**: states plainly that Blau cites both Gen 38:21 and Deut 23:18, both now held in this entry's `verses[]`; deferral caveat dropped.
- **No fabrication:** `blau-dict` was already a source and Blau genuinely cites Deut 23:18, so the no-cite-audit rule is honored. Citation resolvability for the new verse is already satisfied — the TWIST's existing variants (`ממתעה`, `ממתע`) match the Deut 23:18 tafsir tokens.

## Deferred buckets

`data/_blau_saadia_deferred.json` → `phase3_r2/batch1/skip`: the `אלממתעה` duplicate-collision record is **marked RESOLVED 2026-05-30** with a `resolution` pointer to this file. The record is **kept, not deleted** — it remains the audit trail. The other three skip records (אלמקדס no-op, תקלידא + מקדש homograph collisions) are unchanged.

## Gates

```
python3 scripts/verify_divergence.py   →  PASS, 0 warnings (123 entries; twist 36 / note 37 / gloss 50; quality bar PASS)
npm run build                          →  ✓ Compiled successfully; 35/35 static pages generated
Total: 123 · tiers 36/37/50 · Dupes: none · Deut 23:18 → ['אלממתעה']
2-book twists: מסלט, גוהר, חגב, אלממתעה   (4) · 3-book twists: אדלג, חאכמא, גמר (3)
```

## Yield observations

1. **First entry-removal in the corpus's history.** All prior phases were additive (promote-in-place or new-entries). The one-shot `consolidate_mamtuah.py` establishes the pattern for future merges: pop the absorbed entry, fold its analysis into the survivor, merge variants, rewrite prose, re-parse.
2. **Folding > deleting.** The NOTE's consecration-stripping argument was the richer half of the pair; preserving it inside the TWIST mechanism turned a lossy delete into a net upgrade of the surviving entry.
3. **Resolvability came for free.** Because the TWIST already listed `ממתעה`/`ממתע` as variants (added in R2's cross-pericope scan), adding the Deut 23:18 verse needed no new variant work for the verifier to pass — the duplicate had already pre-staged the merge.

## Reduce risk / pattern reminders

- For future consolidations, prefer a dedicated one-shot script over editing JSON by hand — idempotent guards (verse-dup check, variant set-union, lemma-vs-variant skip) make re-runs safe.
- Always re-parse after `write_text` (the script does) and run `verify_divergence.py` + `npm run build` before considering a merge landed.
- When deleting, audit whether the deleted entry holds analysis the survivor lacks; fold it in rather than dropping it.

## Next-session pointer

Next queue item (now in progress this session): **new TWIST for the Sinai/Tent تجلَّى manifestation-cluster** (Phase 3 R3) — Ex 19:11/18/20, 34:5; Num 11:25, 12:5 — the candidate the R2 B2 `אורד` mechanism-correction isolated (theophany verses use Form V تجلَّى manifestation vs Babel/Sodom Form IV ورد dispatch). Then queue #2 (חאכם judicial NOTE) and #3 (Phase 3 R1 second wave) per `PHASE3_R2_BATCH2_SESSION_NOTES.md`.
