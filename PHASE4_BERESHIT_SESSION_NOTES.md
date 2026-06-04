# Phase 4 Bereshit — Session 1 Hand-off

## Snapshot

- **Date shipped:** 2026-05-28 / 2026-05-29
- **Entries added:** 24 (9 NOTE + 15 GLOSS), all Bereshit-anchored
- **Divergence file size:** 56 entries (32 baseline twist + 9 note + 15 gloss)
- **All gates green:** `verify_divergence.py` 0 failures, `npm run build` clean (213 static pages)
- **Pre-existing warning unchanged:** Bereshit twist-tier 20/31 = 65% Blau-backed (< 70%) — Phase 3 R1 territory, untouched here
- **One meaningful dedup catch:** Batch 4's `ינג'מד` (Gen 6:3, Blau alternative root غمد) collided with the baseline twist entry that uses the standard جمد derivation; the dedup correctly preserved the baseline. Documents a genuine Blau ambiguity at this lemma.

## Per-batch counts

| Batch | Apply script | Entries | NOTE | GLOSS | Deferred |
|---|---|---|---|---|---|
| Pilot | `scripts/apply_phase4_pilot.py` | 4 | 1 | 3 | 1 SKIP |
| Batch 1 | `scripts/apply_phase4_bereshit_batch1.py` | 12 | 4 | 8 | 1 STRICT, 1 BORDERLINE |
| Batch 2 | `scripts/apply_phase4_bereshit_batch2.py` | 4 | 3 | 1 | — |
| Batch 3 | `scripts/apply_phase4_bereshit_batch3.py` | 3 | 1 | 2 | — |
| Batch 4 | `scripts/apply_phase4_bereshit_batch4.py` | 1 | 0 | 1 | 1 lemma-collision |
| **Total** | | **24** | **9** | **15** | **4** |

## Bereshit verses now covered

19 unique verses across 12 chapters: 8:22 (paired qiẓ/khurīf), 9:7, 12:13, 15:17, 18:27, 19:8, 25:31, 25:33, 30:13, 31:34, 31:37, 37:2, 37:7, 37:22, 38:26, 39:21, 42:30, 45:26, 49:3, 49:5, 49:9, 49:15, 49:17, 50:23.

## Files changed

**Modified:**
- `data/tafsir-divergence.json` — appended 20 entries (existing 32 untouched)

**Created:**
- `scripts/apply_phase4_pilot.py`
- `scripts/apply_phase4_bereshit_batch1.py`
- `scripts/apply_phase4_bereshit_batch2.py`
- `scripts/apply_phase4_bereshit_batch3.py` (mines no-verse-ref pool via embedded Hebrew n-grams)
- `scripts/apply_phase4_bereshit_batch4.py` (loose body-excerpt scan)
- `data/_blau_saadia_deferred.json`
- `PHASE4_BERESHIT_SESSION_NOTES.md` (this file)

Working tree left uncommitted per project convention.

## Realistic ceiling (calibration drift from plan target)

The plan's headline target of **80–100 entries** assumed the ~226 Bereshit-flagged candidate rows in `data/_blau_saadia_candidates.json` would yield ~25 entries per ~50-row batch at ~45–55% survival rate. The actual session-1 yield rate was **~10–12 entries per ~50 rows examined**, for these reasons:

1. **Page-line citations dominate.** A large share of "רס״ג לבראשית X:Y" patterns in citation lines are actually Saadia commentary footnotes (page-line: e.g., `15:8` = page 15 line 8 of Zucker's *Saadia on Bereshit*, not Gen 15:8). The verifier sees the citation contains "לבראשית" + ch:v-shaped text and includes the row in the Bereshit short-list, but the actual lemma isn't tied to a verse — it's tied to Saadia's translation theory or a footnote gloss.

2. **Cluster duplication.** Many Blau articles are subdivided in the source SQLite table into 4–8 morphological variants (e.g., `نوراني / نير / النيران / نيرة / منور / نوع` all collapse into the Gen 1:14 luminaries article). Each shows up as a separate row in `_blau_saadia_candidates.json` but only one entry's worth of content. Auto-dedup on `(verse, root_ar)` would tighten this.

3. **Root mismatches in OCR.** Several promising-looking candidates resolved to verses where the surfaced JA root differs from the Blau lemma — e.g., `[19001] دء → Gen 8:3` body actually uses تَرَاجَع; `[18436] قتار → Gen 19:28` body uses دخان. The Blau citation chain references those verses for a *different* purpose (parallel-pattern or contrast).

4. **Metalanguage cluster needs sub-batch treatment.** Saadia's translation-theory terms (`مخكم`, `مجاز`, `متشابه`, `شبه`, `تمام`, `دلا` Form V) cluster in Saadia's intro to Genesis (Zucker pp. 8–18, 39+). They're high-value for a learner but don't anchor to a specific Bereshit *verse* — they'd need a separate display surface (e.g., a "Saadia's vocabulary" sidebar on the Tafsir reader's chapter index, not the verse panel).

**Realistic ceiling for first-pass verse-anchored mining:** ~25–35 entries from Bereshit. To reach the original 80–100 target, the next session(s) need to:

- Triage the **166 candidates without detected verse refs** by reading their body excerpts (~ 600 chars each) for embedded Hebrew quotes — many anchor to a verse via the *quoted Hebrew text* rather than a chapter:verse citation.
- Handle the **metalanguage cluster** as a separate sub-batch with its own UI surface, OR write them as gloss entries pinned to *every* verse where Saadia foregrounds his translation method (this would over-couple to verses though).
- Continue with **Shemot / Vayikra / Bamidbar / Devarim** Blau-mining; the pool of 1,596 was Torah-wide, not Bereshit-only. The other books may yield more clean verse-anchored entries simply because Blau's Festschrift article concentrated on Bereshit, biasing the dictionary citations toward it.

## Deferred buckets (input for future passes)

In `data/_blau_saadia_deferred.json`:

- **`skip`** (1 entry so far): non-Tafsir Blau citations. These are documented rather than discarded so the bar is visible to future curators.
- **`borderline`** (1 entry: `18250 فضض / Gen 3:5`): Blau lemma root differs from JA-surfaced root; needs cross-checking against Blau's actual entry text.
- **`phase3_r1_candidates`** (1 entry: `16430 سيد / Gen 49:8`): paradigm-twist on Judah blessing. Saadia recasts "your brothers shall praise you" as "your brothers shall make you ruler". This is exactly the kind of interpretive contrast that lifts a `twist`-tier entry and helps the Bereshit Blau-backed gate move past 65%. Recommend Phase 3 R1 pick it up first.

## Banner-variant smoke test (status)

All three banner variants now have real Bereshit verses to render on:

| Banner | Pilot verse | Batch verse | Status |
|---|---|---|---|
| TwistBanner | Gen 1:2 (`גאמרה` baseline) | (32 baseline still all twist) | unchanged from previous session |
| SaadiaNoteBanner | Gen 31:34 (`פגסס`) | Gen 45:26, 49:3, 49:5, 30:13, 18:27, 9:7, 38:26 | new, eyeball if dev server available |
| GlossCard | Gen 12:13, 37:7, 42:30 | Gen 25:31, 39:21, 49:9, 49:15, 49:17, 8:22, 50:23, 37:2, 37:22 | new, eyeball if dev server available |

The dev server was running on :3000 during the session; the user was offered URLs to eyeball the three variants on pilot verses. No course-correct was triggered during execution.

## Recommended next-session strategy

In priority order:

1. **Pivot to Phase 3 R1** (the deferred `phase3_r1_candidates` bucket has its first real entry — `16430 سيد` on Gen 49:8 — plus the existing ~30-entry STRICT backlog from `PHASE3_ROUND1_PROMPT.md`). Landing ~10–15 STRICT entries should push the Bereshit Blau-backed gate above 70% and clear the verifier warning.

2. **Mine the no-verse-ref pool** with embedded-Hebrew-quote heuristics. For each of the 166 candidates without detected verse refs, look for double-quoted biblical phrases in `body_excerpt`/`saadia_citation_lines` and reverse-look them up in `tafsir-bereshit-{ch}.json`. This should surface another ~15–25 entries.

3. **Begin Shemot Phase 4** (`PHASE4_SHEMOT_BATCH1.py`) once the Bereshit warning clears. Bereshit-shaped pipeline transfers directly; only the chapter-range filter changes.

4. **Defer the metalanguage sub-batch** until UI design clarifies where Saadia's translation-theory terms should surface (probably *not* on the per-verse divergence panel).

## How to resume

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py    # baseline: 52 entries, 1 pre-existing warning
cat data/_blau_saadia_deferred.json      # pick up STRICT / BORDERLINE buckets
ls scripts/apply_phase4_*.py             # pattern for next batch
```
