# Phase 4 Shemot — Batch 2 Hand-off

## Snapshot

- **Date shipped:** 2026-05-29 (same day as Batch 1; Batch 2 directly continues the window)
- **Entries shipped:** 12 worth — 11 net-new (4 NOTE + 7 GLOSS) appended, plus 1 existing entry (`נקל`) promoted from gloss → note with the full Exodus-slavery cluster merged in
- **Divergence file size:** 94 entries (36 twist + 24 note + 34 gloss; from the 83 Batch-1 baseline)
- **All gates green:** `verify_divergence.py` 0 failures (after one mid-run fix to add `מוגהא` accusative-indefinite variant); `npm run build` clean; lemma uniqueness 94/94
- **Deferred file extended:** `data/_blau_saadia_deferred.json#/shemot` grew from 5 → 11 entries via idempotent merge — buckets now 6 skip / 3 borderline / 1 phase3_r2_candidates / 1 cross_book_dupes, plus an 11-line `_cluster_dupes_logged` audit trail
- **`_session` tag** preserved Batch 1's marker and appended Batch 2's

## Window walked

- **Range:** `blau_id 15700–20473` of `data/_blau_saadia_candidates.json` (the second half of the Shemot-flagged subset after Batch 1's 13769–15700 cutoff)
- **Candidates inspected:** 104 (after filtering by `blau_id >= 15700` + Shemot citation pattern)
- **Survival rate:** ~12% (12 / 104) — lower than Batch 1's 22%, driven mostly by heavier source-SQLite cluster duplication and a higher cognate-rejection rate in the upper window

## Batch 2 entries (12)

### GLOSS tier (7 net-new)

| blau_id | Lemma JA | Verse(s) | Pairing | Note |
|---|---|---|---|---|
| 16332 | `סלאמה` | 24:5 / 32:6 | سلامة ↔ שלמים (peace-offering) | Cognate semantic-field; the idiom ذبائح السلامة becomes the JA technical name for biblical שלמים |
| 16478 | `שחמה'` | 29:20 | شحمة ↔ תנוך אזן (earlobe) | Idiom-anchored: Saadia uses the fixed Arabic anatomical idiom شحمة الأذن |
| 16596 | `שפשג` | 28:8 / 28:27 / 28:28 | شفشج ↔ חשב (ephod's belt) | Rare quadriliteral; non-cognate technical pairing, transmitted by Ibn Janāḥ |
| 16871 | `צנאן` | 27:3 / 38:3 | صنان ↔ סירת לדשנו (ash-pans) | Mishkan technical narrowing; spelling spread between أصنان/أضنان (Saadia hypercorrect) |
| 17101 | `מטל` | 12:7 / 12:22 / 12:23 | مطل ↔ משקוף (lintel) | Architectural specialization — both Heb + Ar route through "overlook from above" |
| 17350 | `ג'יב` | 28:7 / 28:25 / 28:27 | جيب ↔ כתף האפוד (shoulder-piece) | Specialized narrowing; Saadia's Aggron 5:258 fixes the equivalence |
| 17941 | `אלג'רובין` | 12:6 | بين الغروبين ↔ בין הערבים (twilight) | Dual-idiom calque preserved across languages |

### NOTE tier (4 net-new + 1 promoted = 5)

| blau_id | Lemma JA | Verse(s) | Pairing | Mechanism in one line |
|---|---|---|---|---|
| 17509 | `יצפח` | 23:21 | صفح ↔ נשא לפשעכם (forgive) | Theological reframe: Heb "lift/bear sin" → Ar "turn-the-page on" |
| 18778 | `יקימו` | 31:16 | يقيم ↔ ושמרו השבת (uphold) | Active-legal calque: Heb "guard" → Ar Form-IV "establish/uphold" |
| 19402 | `מרזבאן` | 16:16 | مرزبان ↔ עמר לגלגלת (omer/head) | Persian-loan measure equivalence (administrative term repurposed) |
| 19895 | `נקל` (promoted) | Gen 49:15 + Ex 1:11 / 2:11 / 5:4 / 5:5 / 6:6 / 6:7 | نقل ↔ סבל (burden) | Semantic-field calque: Heb "forced labor" → Ar "transport/logistics" across full Exodus-slavery cluster |
| 20182 | `מוגה` | 25:30 / 35:13 | موجه ↔ לחם הפנים (showbread) | Calque-by-passive-participle preserving the "facing/two-faced bread" semantics |

## Promoted-and-extended entry (special-case)

`נקל` existed in baseline as a gloss-tier Bereshit-only entry (Gen 49:15). Batch 2's Shemot mining surfaced the same lemma across the full Exodus-slavery cluster (Ex 1:11, 2:11, 5:4, 5:5, 6:6, 6:7). Rather than skip on lemma collision, I patched the existing entry in place:

- **Tier:** gloss → **note** (the multi-verse semantic-field calque is mechanism-grade, not just pedagogical pairing)
- **Verses:** 1 → 7 (Bereshit + full Exodus-slavery cluster)
- **Variants:** 3 → 5 (added `נקלהם`, `לנקלכם`, `נקל אלמצריון`)
- **Mechanism:** rewritten to capture the logistics-frame-not-labor-pain-frame insight that motivates Saadia's invariant rendering across both books
- **blau_dict.sense:** upgraded to cross-reference both Gen 49:15 and the full Exodus cluster with Rashbam 11

This is the first promoted/cross-book entry in the divergence file. Pattern worth re-using when future batches surface a lemma that's already shipped at a lower tier or sparser verse-set.

## Shemot verses now covered (Batch 1 + 2 combined)

26 unique verses across 14 chapters:
- Batch 1: 8:15, 9:8, 9:32, 12:11, 12:49, 22:15, 25:4, 25:5, 26:14, 28:6, 28:15, 28:22, 28:30, 30:12, 35:25, 37:24
- Batch 2: 1:11, 2:11, 5:4, 5:5, 6:6, 6:7, 12:6, 12:7, 12:22, 12:23, 16:16, 23:21, 24:5, 27:3, 28:7, 28:8, 28:25, 28:27, 28:28, 29:20, 31:16, 32:6, 35:13, 38:3
- Plus the Bereshit promotion (Gen 49:15) gets a Shemot-attestation upgrade

Multi-verse bundling continues to be the high-yield pattern: 7 of the 12 entries bundle 2+ verses (e.g. נקל at 7 verses, מטל at 3, ג'יב at 3, שפשג at 3).

## Files changed

**Modified:**
- `data/tafsir-divergence.json` — appended 11 entries + patched `נקל` in place (existing 83 → 94)
- `data/_blau_saadia_deferred.json` — merged into existing `shemot` namespace (additive only; Batch 1's entries untouched)

**Created:**
- `scripts/apply_phase4_shemot_batch2.py` (with merging `_update_deferred()` helper)
- `PHASE4_SHEMOT_BATCH2_SESSION_NOTES.md` (this file)
- `PROMPT_NEXT_PHASE4_BATCH.md` (next-session prompt; see below)

Working tree left uncommitted per project convention.

## Deferred buckets — Batch 2 additions

### `skip` (4 added → 6 total)
- `15740 دلا` — metalanguage-only marker; defer to translation-theory pool
- `17144 طوف` (Ex 14/15 wave-cover) — Cairo 2019 uses غ-ط-و, not ط-و-ف; Blau cite mismatches the baseline
- `18436 قتر` (Ex 29:13 הקטרת) — pure consonantal cognate ق-ت-ر ↔ ק-ט-ר; no tier-promoting divergence
- `20277 وشمة` cluster (Ex 21:6 ורצע) — culturally-equivalent tool-substitution (Heb awl ↔ Ar branding-iron); borderline-cognate; defer pending Mishpatim re-walk

### `borderline` (2 added → 3 total)
- `17513 ضعيف` (Ex 22:24 העני) — close register-shift cousin; both root-clusters orbit "weakness"
- `19132 لبن` (Ex 1:14 / 5:7-14) — Blau explicitly tags Heb-influenced; NOTE-tier in principle but hard to surface without inverting the bilingual frame

### `_cluster_dupes_logged` (11 new entries)
Source-SQLite cluster duplications captured for future-batch hygiene: 17350≈17351, 17513-17516 (4 rows), 17597≈17598, 17999≈18000, 18778-18780 (3 rows), 19132-19134 (3 rows), 19545-19548 (4 rows), 20065-20068 (4 rows), 20114-20118 (5 rows), 20277-20280 (4 rows), 20402-20408 (7 rows).

## Yield-rate observations

- **Window walked:** 104 candidates in `blau_id 15700–20473`
- **Survivor count:** 12 entries → ~12% survival rate (Batch 1: 22%; Bereshit Batch 1: 24%)
- **Failure-mode shift:** Batch 2's upper window had ~7 large cluster-duplications (vs Batch 1's 3) inflating the candidate count. Once cluster-flattened, the effective survival rate is closer to 18%. Heavier hit on cognate-misses (Heb-Ar cousins like سلامة/شحمة required careful tier judgment — kept as glosses because they teach JA-acquisition value despite cognacy).
- **New pattern this batch:** the **promote-existing-entry** path — `נקל` was the first lemma to get upgraded in place rather than dropped on collision. Yields better cross-book coverage at no schema cost.

## Banner-variant smoke test (status)

Skipped per session decision (per the plan; Batch 1 already exercises all three banner variants on real Shemot verses). The new high-density chapters that should render banner content:
- Ex 28 (4 entries: שפשג, ג'יב, plus Batch-1 בדנה + אסמאנגון) → walk this for any banner-stacking-edge-case
- Ex 12 (5 entries: 12:6 גרובין, 12:7/22/23 מטל, plus Batch-1 12:11 בחפז + 12:49 אלדכ'יל) — densest Passover verse coverage
- Ex 5 + Ex 6 — first appearance of multi-verse-NOTE on consecutive chapters (נקל at Ex 5:4/5, 6:6/7)

If a UI eyeball pass happens later, prioritize Ex 12 and Ex 28.

## Recommended next-session strategy

Same Bereshit-precedent priority stack as Batch 1's hand-off, now updated:

1. **Continue with Shemot Batch 3** — but the next window is structurally different. After 20473 the candidate pool exhausts on Shemot anchors (the source SQLite top-IDs out at ~20480), so Batch 3 would need to **re-walk the metalanguage / no-verse-ref pool** with embedded-Hebrew-quote heuristics OR **revisit the BORDERLINE bucket** for tier-promotion candidates (currently 3: דפק Ex 26:14 from Batch 1, ضعيف Ex 22:24 + لبن Ex 1:14 from Batch 2). Realistic ceiling: 3-6 more entries before Shemot Phase 4 plateaus.

2. **Pivot to Vayikra Phase 4 Batch 1** *(recommended next)* — Vayikra has only ~71 candidates in the candidates pool (vs. Shemot's 168), but the Leviticus pool is rich in ritual/cultic vocabulary that maps well to NOTE-tier "technical extension" entries. Lower ceiling but also lower noise, and the JA Mishkan-vocabulary cross-references from Batches 1 + 2 (סלאמה, בדנה, אסמאנגון, שפשג, etc.) will pre-validate Vayikra readings.

3. **Or pivot to Phase 3 R2 for Shemot** — Shemot now has 1 twist entry (the existing `חאכמא` Ex 1:22 / 2:14 / 22:27) plus 1 `phase3_r2_candidates` flag (גריחה Ex 8:15 from Batch 1). The verifier's per-book twist-bar gate skips books with <5 twist entries, so this is still premature. Worth picking up only after 3-4 more TWIST-grade reframes land in the candidates bucket.

4. **Defer the Shemot metalanguage / no-cite pool** — same reasoning as Batch 1; needs UI design for translation-theory display first.

## How to resume

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py    # baseline now: 94 entries, 0 failures
cat data/_blau_saadia_deferred.json | python3 -m json.tool | head -120
ls scripts/apply_phase4_*.py            # pattern for next: copy shemot_batch2.py, retarget Vayikra (filter on ויקרא/ויק׳)
cat PROMPT_NEXT_PHASE4_BATCH.md         # ready-to-use prompt for next session
```

**Next-batch pointer:** the natural cursor is now **Vayikra Phase 4 Batch 1** (per recommendation 2 above). The Shemot pool has effectively exhausted in the verse-anchored verse-citation tier; the remaining 79 Shemot-anchored candidates (104 − 12 shipped − 7 deferred − ~6 cluster-flatten dupes) are mostly borderline-cognate, Dirinburg-variant, or no-verse-anchor entries that would need a different walking heuristic.
