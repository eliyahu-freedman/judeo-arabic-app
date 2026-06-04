# Phase 4 Shemot — Batch 1 Hand-off

## Snapshot

- **Date shipped:** 2026-05-29
- **Entries added:** 11 (4 NOTE + 7 GLOSS), all Shemot-anchored
- **Divergence file size:** 83 entries (36 twist + 19 note + 28 gloss; from 72 baseline)
- **All gates green:** `verify_divergence.py` 0 failures, no new warnings; `npm run build` clean
- **Deferred file extended:** `data/_blau_saadia_deferred.json` now has a `shemot` namespace with 5 entries across 4 buckets (skip, borderline, phase3_r2_candidates, cross_book_dupes)
- **No dedup collisions on insert** — all 11 lemmas were unique against the existing 72 entries

## Batch 1 (the only batch this session)

| Apply script | Entries | NOTE | GLOSS | Deferred this round |
|---|---|---|---|---|
| `scripts/apply_phase4_shemot_batch1.py` | 11 | 4 | 7 | 5 (2 skip + 1 borderline + 1 phase3_r2 + 1 cross-book dupe) |

## Shemot verses now covered (Batch 1)

12 unique verses across 9 chapters: 8:15, 9:8, 9:32, 12:11, 12:49, 22:15, 25:4, 25:5, 26:14, 28:6, 28:15, 28:22, 28:30, 30:12, 35:25, 37:24.

(Multi-verse bundling: `אסמאנגון` covers 25:4 / 28:6 / 35:25 in one entry; `בדנה` covers 28:15 / 28:22 / 28:30; `דארש` covers 25:5 / 26:14. Per the Bereshit `ת'ואלת'` precedent.)

## Files changed

**Modified:**
- `data/tafsir-divergence.json` — appended 11 entries (existing 72 untouched).
- `data/_blau_saadia_deferred.json` — added top-level `shemot` namespace; existing Bereshit-era keys untouched.

**Created:**
- `scripts/apply_phase4_shemot_batch1.py`
- `PHASE4_SHEMOT_SESSION_NOTES.md` (this file)

Working tree left uncommitted per project convention (also matches the Bereshit Phase 4 hand-off).

## Per-entry rundown (for future audit)

### GLOSS tier (7)

| blau_id | Lemma JA | Verse(s) | Pairing | Note |
|---|---|---|---|---|
| 14048 | `בדרה'` | 37:24 | بذرة ↔ כִּכָּר (talent weight) | Non-cognate weight-measure |
| 13872 | `אסמאנגון` | 25:4 / 28:6 / 35:25 | أسمانجون ↔ תְּכֵלֶת | Persian loan via Arabic; Saadia's standard JA rendering for biblical blue |
| 14868 | `אחציתהם` | 30:12 | أحصى ↔ פָּקַד (census) | Form IV; root ح-ص-ي in the surface, ح-ص-ر in Blau's head entry (related cluster) |
| 14907 | `בחפז` | 12:11 | حفز ↔ חִפָּזוֹן | Consonantal calque ḥ-p-z; Saadia strips Heb -on suffix |
| 14935 | `חפניכמא` | 9:8 | حفن ↔ חָפְנֵיכֶם | Bare-stem حفن over standard حَفْنَة; Blau explicitly tags "Heb-influenced" |
| 15118 | `כ'דע` | 22:15 | خدع ↔ יְפַתֶּה | Non-cognate semantic field; Heb "persuade" ~ Ar "deceive/seduce" |
| 15410 | `אלדכ'יל` | 12:49 | دخيل ↔ גֵּר (doublet w/ ج‍ـريب) | Religious-legal "convert"; Qirqisāni parallel |

### NOTE tier (4)

| blau_id | Lemma JA | Verse(s) | Pairing | Mechanism in one line |
|---|---|---|---|---|
| 14058 | `בדנה` | 28:15 / 28:22 / 28:30 | بدنة ↔ חֹשֶׁן | Hebraizing technical coinage; Blau explicitly tags `(hebraizing)` |
| 13902 | `אפלתאן` | 9:32 | آفل ↔ אֲפִילֹת | Semantic-field extension of أ-ف-ل ("to set, be hidden, be unripe"); Blau hedges *why* but surface confirmed |
| 14507 | `גריחה` | 8:15 | جريحة ↔ אֶצְבַּע אֱלֹהִים | Saadia recasts "finger of God" as substantive "miracle"; **TWIST-watch** (see phase3_r2_candidates) |
| 15441 | `דארש` | 25:5 / 26:14 | دارش ↔ תַּחַשׁ | Parshanic identification: the disputed תחש = a known black-dyed leather |

## Deferred buckets (extended `data/_blau_saadia_deferred.json#/shemot`)

### `skip` (2)
- **`14097 برص` / Ex 2:23** — Dirinburg-variant-only reading. Blau quotes "ולקה בצרעת ומת מלך מצרים" but this is Dirinburg's interpolated text; our Cairo 2019 baseline tafsir-shemot-2.json doesn't reflect it.
- **`13864 إنطرك` / Ex ?:?** — Tanḥum-routed citation ("תרגם רס״ג לשמות … לפי תנחום, בערכו"). ch:v also OCR-corrupted as `٦7:9`. No direct verse anchor in baseline.

### `borderline` (1)
- **`15549 دفق` / Ex 26:14** — Blau cites Saadia on 26:14 for "bar for carrying", but tafsir-shemot-26.json at v.14 uses different lexemes (no bar-language in the *covering* verse). Either a recension difference or a mis-cite; cross-check needed against bar-pericopes at 25:13-14, 27:6.

### `phase3_r2_candidates` (1)
- **`14507 جريحة` / Ex 8:15** — Shipped here as NOTE but **flagged for TWIST promotion**. Saadia recasts אצבע אלהים = 'miracle' (גריחה מן ענד אללה); theological reframe with a Qirqisāni parallel (Qirqisāni 2:303 uses cognate جرائح for biblical 'signs and wonders'). The "finger of God" → abstract event-noun is the kind of move that lifts a NOTE to TWIST.

### `cross_book_dupes` (1)
- **`14897 حظاء`** — already shipped as `חצ'אא` (Gen 39:21) in Bereshit Batch 1. Shemot filter caught on incidental mention of "ספר אברהם לבראשית ושמות"; all verse-anchored citations in this Blau entry are Bereshit.

## Cluster duplicates seen in the window (logged, not auto-deduped)

- **`14907 ≈ 14928`** (both حفز / Ex 12:11) — same Blau article duplicated in source SQLite. Shipped one (14907) as the canonical entry.
- **`14909 ≈ 14930`** (both محفظ) — co-article with حفز; did not surface a Shemot anchor, so no entry shipped.
- **`14717 ≈ 14719`** (both حجر) — verified no Shemot anchor; skipped silently.

These match the Bereshit Phase 4 finding: Blau's source SQLite has cluster duplication where one article gets subdivided across 4-8 rows (morphological variants, byforms). Useful to log so future passes don't re-classify the same article twice.

## Yield-rate observations

- **Window walked:** ~50 candidates in the `blau_ids 13769–15700` range (out of 168 Shemot-flagged total)
- **Survivor count:** 11 entries → roughly **22% survival rate**, in line with Bereshit Batch 1's 24%
- **Failure modes encountered (matches Bereshit + Plan-agent prediction):**
  - Dirinburg-variant-only readings (1 hit: برص)
  - Tanḥum-routed citations (1 hit: إنطرك)
  - Recension/cite mismatches (1 hit: دفق)
  - Cross-book false positives (1 hit: حظاء)
  - Cluster duplicates (3 hits: 14907≈14928, 14909≈14930, 14717≈14719)
- **Bonus finding:** The Mishkan-cluster (Ex 25-40) gave us 3 multi-verse-bundled entries (`אסמאנגון`, `בדנה`, `דארש`) — efficient coverage compared to Bereshit's narrative chapters where most entries anchor to single verses.

## Banner-variant smoke test (status)

All three banner variants now have real Shemot verses to render on. Dev-server eyeball test not executed this session (the npm-build gate is the meaningful programmatic check), but the URLs to walk are:

| Banner | Verse | Pairing |
|---|---|---|
| NOTE — SaadiaNoteBanner | `/tafsir/shemot/28` v.15 | בדנה (חושן) |
| NOTE — SaadiaNoteBanner | `/tafsir/shemot/9`  v.32 | אפלתאן (אפילת) |
| NOTE — SaadiaNoteBanner | `/tafsir/shemot/8`  v.15 | גריחה (אצבע אלהים) |
| GLOSS — GlossCard | `/tafsir/shemot/22` v.15 | כ'דע (יפתה) |
| GLOSS — GlossCard | `/tafsir/shemot/25` v.4  | אסמאנגון (תכלת) |
| GLOSS — GlossCard | `/tafsir/shemot/12` v.49 | אלדכ'יל (גר) |

If anything looks wrong (color contrast, spacing, GlossCard layout, banner copy in a multi-verse-bundled entry), tighten the CSS in `app/tafsir/reader.tsx` before mining Batch 2.

## Recommended next-session strategy

In priority order:

1. **Continue with Shemot Batch 2** — walk the next candidate window (`blau_ids 15700–19000`, ~50-60 candidates of the remaining ~118 Shemot-flagged subset). Target another 10-12 entries. Same pattern, same gates. Realistic ceiling per Bereshit precedent: ~25-35 total entries for Shemot first-pass; we're ~30% there.

2. **Or pivot to Vayikra Phase 4 Batch 1** — Vayikra has only 71 candidates in the pool (vs Shemot's 168), but the Leviticus pool is rich in ritual/cultic vocabulary that maps well to NOTE-tier "technical extension" entries. Lower ceiling but also lower noise.

3. **Defer the Shemot metalanguage / no-cite pool** until either UI design clarifies where Saadia's translation-theory terms surface, or the verse-anchored pool exhausts.

4. **Phase 3 R2 for Shemot** is premature until Shemot has more twist-tier entries — the verifier per-book gate skips books with <5 twist entries, and Shemot currently has 1 (the existing `חאכמא` Ex 1:22 / 2:14 / 22:27). Worth picking up only after another 3-4 TWIST-grade discoveries land in the `phase3_r2_candidates` bucket.

## How to resume

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py    # baseline now: 83 entries, 0 failures, 0 warnings
cat data/_blau_saadia_deferred.json | python3 -m json.tool | head -100   # review deferral state
ls scripts/apply_phase4_*.py            # pattern for Batch 2 (copy shemot_batch1.py, advance window)
```

**Window pointer for Batch 2:** start at `blau_id ≥ 15700` in `data/_blau_saadia_candidates.json`. The next candidate immediately after the Batch 1 cutoff is `15740 دلا` (already known from the n=200 calibration walk as a metalanguage-cluster Form V — defer to Saadia's-translation-theory pool, not Phase 4).
