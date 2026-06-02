# Phase 4 Bamidbar Batch 1 — Session Notes

**Date shipped:** 2026-05-29
**Apply script:** `scripts/apply_phase4_bamidbar_batch1.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 106 | 115 | +9 net-new |
| Tier distribution | 36 twist / 29 note / 41 gloss | 36 / 33 / 46 | +4 NOTE, +5 GLOSS |
| Promote-in-place verse extensions | — | 14 verses across 4 entries | מוגה +1, סלאמה +4, ד'כוה +4, יסתג'פר +5 (was 5; -1 corrected during gate) |
| Bamidbar candidate pool | 32 raw / 18 article-flattened | — | mined |
| Effective survival rate (article-flattened) | — | **13 ships / 18 articles = 72%** | highest cross-book overlap pass yet |
| Gates | — | verify_divergence.py PASS · npm run build clean · 115/115 lemma-unique | all green |

---

## Per-entry rundown

### NEW ENTRIES — 5 GLOSS

#### `רמד` — Num 4:13 (altar ash-removal)
Essive-ablative semantic flip on the noun-derived verb. Heb `דִּשֵּׁן` (D-stem ablative: "remove ashes") → Ar Form I `رمد` (essive: "be reduced to ash"). Both verbs derive from each language's word for "ash" (Heb `דֶּשֶׁן` ~ Ar `رماد`), but Saadia preserves the root-link while inverting the action-direction. Surface morphology rhymes; ergative orientation reverses. Pedagogically distinctive.

#### `פרצן` — Num 6:4 (nazirite grape-pip)
Non-cognate lexical substitution for a nazirite-prohibition noun. Heb `חַרְצָן` ("grape-stone") → Ar `فرصن` — a rare/marginal noun, probably a Hebraizing technical coinage. The pairing exposes Saadia working at the fringes of standard Arabic. Pairs cleanly with the parallel `אלזג` (Heb `זג` "outer-skin" preserved as transliteration at the same verse), showing Saadia's mixed strategy across the same prohibition list.

#### `וכאיה` — Num 21:18 (well-digging song staves)
Concrete-to-abstract register shift. Heb `מִשְׁעֲנֹתָם` (concrete staves the well-diggers carried) → Ar `وكاية` (abstract verbal-noun "their supports / leanings"). The choice generalizes the mythic well-digging song to a more abstract poetic register, fitting Saadia's tendency to smooth concrete-archaic Hebrew into philosophical-poetic Arabic at exactly the moments where the Heb is most archaic (Num 21:14's quotation from the "Book of the Wars of YHWH").

#### `בידאא` — Num 22:1 + 26:3 + 31:12 + 33:48 + 35:1 + 36:13 (Trans-Jordanian wilderness)
Landscape-semantic shift AWAY from the available cognate. Heb `עַרְבוֹת מוֹאָב` ("steppe-pasturelands of Moab", agricultural-fringe). Saadia could have used the cognate `عربة` — but chose `بيداء` ("wilderness, trackless waste") instead. Flattens the Bible's careful distinction between `מדבר` (wilderness) and `ערבה` (steppe-arabah). Six-verse invariance across the entire Bamidbar travel narrative confirms the lexical-fixed choice.

#### `תחמיה` — Num 35:12 (asylum-cities)
Specific-asylum to general-protection. Heb `מִקְלָט` (precise priestly-legal institutional noun) → Ar `تحمية` (Form II abstract verbal noun, "the act of protecting"). The cities don't get a name; they get a description. The Form V `تَحَمَّى` ("to take refuge") was available; Saadia chose Form II for the GIVING-protection sense rather than the SEEKING-protection sense, foregrounding the cities' institutional role over the fugitive's act.

### NEW ENTRIES — 4 NOTE

#### `גבן` — Num 32:7, 32:9 (Reubenite-Gadite confrontation)
Semantic narrowing from generic-dissuasion to specifically-emotional-cowardice. Heb `תְּנִיאוּן` / `וַיָּנִיאוּ` (Hiphil of נוא, "to discourage, draw back") → Ar Form II `جبن` ("to make cowardly"). Heb names the behavioral OUTCOME; Ar names the EMOTIONAL state induced. Reframes the Reubenite sin from "discouraging Israel" (neutral) to "making Israel cowardly" (morally pejorative), aligning with the rabbinic tradition that reads this exchange as slander-by-fear-mongering.

#### `מגרד` — Num 31:5, 32:21, 32:27, 32:29, 32:30 (Midianite war + Transjordan conquest)
Frame-shift from equipped-vanguard to stripped-for-action. Heb `חָלוּץ` ("girded for war", foregrounds the EQUIPPING) → Ar `مجرد` (Form II passive participle, "stripped of impediments", foregrounds the STRIPPING). The two participles are nearly opposite in their frame, yet name the same soldier-type. Saadia routes Heb military-cultic vocabulary through classical-Arabic mounted-light-cavalry vocabulary. Cross-pericope consistency across the Midianite war + Transjordan conquest cluster confirms it's lexical-fixed, not context-driven.

#### `מחפצה` — Num 3:7, 3:8, 3:28, 3:32, 3:38, 8:26, 18:3, 31:30 (Levitical guard-duty)
Institutional-technical coinage by Form II nominal. Heb `מִשְׁמֶרֶת` is itself a coined-technical mishkal-mafʿélet of שמר for the priestly guard-duty institution. Saadia coins the parallel — `محفظة`, Form II nominal مفعلة of حفظ — matching the Heb coining-strategy at the morphological level. **Pedagogically distinctive because the morphological-parallelism is legible to a bilingual reader at the morphological level itself**, beyond the lexical pairing. 8-verse Bamidbar coverage across both Num 3 Levitical census + the Num 8/18/31 watch-rotations confirms it's the invariant administrative-technical choice.

#### `ראם` — Num 13:21, 13:32, 15:39 (12-spies + tzitzit)
Volitional reframe of a physical-exploration verb. Heb `תור` (physical exploration, foot-traversal) → Ar `روم` (intentional pursuit, volitional aim). Saadia consistently renders both the 12-spies physical-scouting AND the metaphorical "do not go-after your heart and eyes" prohibition with the same volitional verb. The cross-pericope consistency across two semantically-distinct contexts confirms the lexical-fixed choice. Particularly striking at Num 15:39 — the prohibition becomes about pursuit-with-intent, foregrounding the volitional-moral dimension the rabbinic-philosophical tradition emphasizes.

### PROMOTE-IN-PLACE — 4 cross-book extensions

| Lemma | Before | Added | After total |
|---|---|---|---|
| `מוגה` (showbread) | Shemot 25:30, 35:13 | Bamidbar 4:7 (table-of-presence) | 3 verses |
| `סלאמה` (peace-offering) | Shemot 24:5, 32:6 | Bamidbar 6:14, 6:17, 7:17, 10:10 (nazirite + chieftains + festivals) | 6 verses |
| `ד'כוה` (sin-offering) | Vayikra 4:3, 4:24, 7:7, 16:6, 16:25 | Bamidbar 6:11, 7:16, 15:24, 28:15 (nazirite + chieftains + inadvertent + festivals) | 9 verses |
| `יסתג'פר` (atonement) | Vayikra 5:6, 14:19, 16:6, 16:16, 16:30 | Bamidbar 5:8, 8:12, 15:25, 17:11 (restitution + Levite-consecration + communal + Korach) | 9 verses |

Key mechanism updates:
- **מוגה**: variants extended with `מווגה` / `אלמווגה` (double-waw spelling from Cairo 2019 manuscript-tradition); the entry's blau_dict.sense already documented Num 4:7 in prose — verses[] now matches the prose.
- **סלאמה**: variants extended with `סלאמת` / `סלאמתכם` (ta-marbuta opens to -ת before pronominal suffixes; surfaces at Num 10:10 "סלאמתכם" = "your peace-offerings"). Mechanism rewrite documents the 4-system invariance (covenant ceremony + nazirite + chieftain-dedication + festival cycle).
- **ד'כוה**: mechanism rewrite documents the full 5-system priestly-cultic coverage (Vayikra offerings + nazirite-impurity + chieftain-dedication + inadvertent-community-sin + festival sin-offerings).
- **יסתג'פר**: mechanism rewrite documents 5 Bamidbar contexts AND surfaces the marked counter-case at Num 25:13 (Phinehas's covenant of peace, where Saadia retains the bare cognate Form I `כפר` rather than Form X `יסתג'פר`, framing the Phinehas episode as covenant-zeal rather than routine atonement-supplication).

---

## Deferred buckets

### Bamidbar.skip (13)

| blau_id | root_ar | Reason |
|---|---|---|
| 14196 | بكر | Direct cognate (firstborn) |
| 14286 | بيذر | No surface attestation in Num 15:20 tafsir |
| 14347 | ترك | Generic cognate-direct (to leave/abandon) |
| 15295 | خلاف | Methodology citation (Ibn Janāḥ, not Bamidbar-anchored) |
| 17395 | خدم | Standard semantic-split (Heb עבד narrowed to attendant-service) — not paradigm-shifting |
| 17430 | رأس | Direct cognate (head/start-of-time idiom) |
| 17639 | عشر | Direct cognate (count-of-ten) |
| 17640 | عشريني | No Bamidbar attestation of the bare substantive |
| 19633 | نحص | No surface attestation; manuscript-variant cross-reference |
| 19634 | نحل | Direct cognate (inherit Form I) |
| 19635 | نحلة | Direct cognate (inheritance substantive) |
| 19861 | تنغيم / nfd family (11 rows) | Already deferred from Vayikra B1 (Lev 26:30 missing); no Bamidbar surface for the destruction-frame at Num 33:52 |
| 20392 | وكاية | Promoted to NEW_ENTRIES as וכאיה |

### Bamidbar.borderline (0)

None. The pre-scan dual-promotion candidate `מסוחייה` (Vayikra borderline blau_id=19427) does **NOT** attest in Bamidbar — Saadia renders שמן המשחה at Num 4:16 with `دهن المسح`, not `مسوحية`. The Vayikra borderline stays put for Track B (Vayikra B2) and is **not** consumed here. Track A's hybrid `_promote_from_vayikra_borderline()` helper was planned but not needed.

### Bamidbar._cluster_dupes_logged (6)

- 17639≈17640 (عشر/عشريني, 2 rows — both SKIP)
- 18162≈18163 (فرص/فرصم, 2 rows — 18162 SHIPPED as פרצן; 18163 is the headword-variant)
- 19633-19635 (نحص/نحل/نحلة, 3 rows — all SKIP)
- 19861-19871 (nfd family, 11 rows — Vayikra-B1 deferred)
- סלאמה chieftain-dedication cluster (Num 7:17-83 = 12 verses) — collapsed to 1 representative anchor (7:17)
- ד'כוה chieftain-dedication cluster (Num 7:16-82 = 12 verses) — collapsed to 1 representative anchor (7:16)

---

## Yield observations

### 1. Cross-book promote-in-place dominated, as projected

The plan called this out: with five of six pre-scan lemmas (סלאמה, ד'כוה, יסתג'פר, שחמה', מוגה) already in divergence, the dominant Bamidbar mechanism was always going to be cross-book extension over net-new entry. The actual count confirms it: **14 verse-additions via promote-in-place across 4 entries**, vs. 9 net-new entries with 25 total verses. By a weighted "coverage-extension" count (verses added), promote-in-place is on par with net-new (14 vs 25), but the strategic significance is much higher — promote-in-place restructures pre-existing entries to span multiple books, which is the long-term goal of the Phase 4 mining series.

### 2. Effective survival rate is the highest yet — 72%

| Pass | Raw | Article-flattened | Ships | Article-survival |
|---|---|---|---|---|
| Bereshit | 165 | ~80 | 19 | ~24% |
| Shemot B1 | ~180 | ~90 | 20 | ~22% |
| Shemot B2 | ~165 | ~85 | 15 | ~18% |
| Vayikra B1 | 76 | 32 | 13 | 41% |
| **Bamidbar B1** | **32** | **18** | **13** | **72%** |

The pattern is now legible: as the pool shrinks, the article-survival rate climbs. This isn't a quality regression — it's a consequence of the cross-book promote-in-place pattern compounding. Bamidbar's vocabulary is heavily reused from Shemot (Mishkan furniture → Camp/Tent-of-Meeting cycles) and Vayikra (sacrificial system → nazirite + chieftain-dedication + festival cycles), so what looks like a "thin" candidate pool is really a "highly-reusable" pool. The right way to read 72% isn't "we shipped almost everything" but "the entries we DIDN'T ship were correctly-identified cognate-direct skips, and the entries we DID ship multi-system promotions overlap their value across pericopes".

### 3. The Phinehas Form I — a useful marked-exception

The verification gate caught a real prompt-projection error: Num 25:13's `וְכִפֵּר` is rendered by Saadia with the bare cognate Form I `כפר`, not Form X `יסתג'פר`. This is a publishable counter-example to the otherwise-invariant Form-X rule, and now lives in the יסתג'פר mechanism rewrite as a marked exception. Worth noting: Saadia preserves the Hebrew's emphasis on Phinehas's ZEAL-ACT (Heb covenant-of-peace is granted because of the act, not because of any supplicatory mechanism), and the bare-cognate choice respects that frame. Future Devarim work may surface similar marked exceptions; expect them and don't auto-extend.

### 4. تخوية was an OCR misread; the actual lemma is تحمية

Blau-OCR reads `פתכוית` for Num 35:12 cities-of-refuge; the actual Cairo 2019 surface is `תחמיה` (Form II of حمى, not the orphan root خو-ي). Shipped as a correctly-OCR'd new GLOSS. Worth watching: the Blau body-OCR has occasional OCR-induced ghosts like this; the verification gate (loading the actual tafsir surface for each candidate) is essential. The candidate's reported `root_ar` was `تخوية`; the shipped lemma's `root` is `ح-م-ي` (different family).

### 5. مسوحية did NOT extend to Bamidbar — Track B B.1 stays intact

The plan flagged מסוחייה as a strong dual-promotion opportunity for the Track A + Track B coordination point. Direct check on Num 4:16 (شَمَن הַמִּשְׁחָה in the Mishkan-furniture pericope) showed Saadia uses `دهن المسح` — the bare Form I verbal-noun, not the Aramaic-Syriac calque form `مسوحية`. So the Vayikra-borderline 19427 stays put as a 4-borderline target for Track B (Vayikra B2), and Track A's planned hybrid `_promote_from_vayikra_borderline()` helper was correctly identified as unnecessary.

---

## Recommended next-session strategy

In priority order:

1. **Devarim Phase 4 Batch 1** — last book. Reuse the Holiness-Code (Lev 17-26) → deuteronomic-law parallels and the now-cross-book-attested Mishkan vocabulary (سلامة, ذكوة, يستغفر, موجه — all now spanning 2-3 books). Devarim recapitulates much of the priestly vocabulary in homiletic register; expect a similar cross-book promote-in-place pattern to Bamidbar's. Tentative pool projection: ~40-60 candidates.

2. **Vayikra Batch 2 (Track B)** — the three remaining borderlines (17407 כ'אמע, 18594 קצבה, 19142 לג) plus 19427 מסוחייה (with the Bamidbar-non-attestation now documented as a stable point) can ship as a coordinated 4-borderline promotion. Now that Bamidbar is on the board, the Vayikra B2 mechanism notes for מסוחייה can explicitly state "Vayikra-only; does NOT extend to Bamidbar despite same Mishkan-furniture context".

3. **Phase 3 R2 cross-book scan** — with three promote-in-place precedents now shipped (`נקל` Bereshit+Shemot, `שחמה'` Shemot+Vayikra, `סלאמה` Shemot+Bamidbar, `מוגה` Shemot+Bamidbar, `ד'כוה` Vayikra+Bamidbar, `יסתג'פר` Vayikra+Bamidbar), the methodology is mature enough to retroactively scan the 36 existing TWIST-tier entries for multi-book attestation. Highest-leverage cross-book move available.

4. **Phase 3 R1** — the ~30 deferred STRICT-tier additions never shipped. Re-evaluate once all 5 books are at ≥5 twist entries each so the verifier's per-book gate activates uniformly. Bamidbar B1 added zero twist entries (intentional — twist-tier requires paradigm-divergence verification at a deeper level than the cluster-flattened pool surfaced); Devarim B1 may similarly skew NOTE/GLOSS-only.

---

## Pattern reminders for future batches

### What worked

- **Direct-tafsir scanning for promote-in-place candidates** turned out to be more productive than Blau-citation-only mining. The pre-scan list (סלאמה, ד'כוה, יסתג'פר, מוגה) yielded 14 verse-additions; the candidate-pool walk yielded 9 net-new. Future batches should run BOTH passes in parallel from the start — don't depend on Blau-OCR to surface all promote-in-place opportunities.

- **The morphological-parallelism criterion** (mishkal-mafʿélet matching مفعلة, etc.) is a strong NOTE-tier signal worth flagging explicitly. מחפצה ships specifically because its coining-by-template parallels Heb משמרת's coining-by-template; the entry's mechanism narrative foregrounds the morphological parallel because it's the pedagogically distinctive feature.

- **The verification gate's hard requirement** that lemma OR a variant surfaces in the cited verse's normalized JA caught two real errors (the Num 25:13 Phinehas Form-I miss + the Num 10:10 suffixed-form variant gap). Trust the gate; investigate when it fails rather than soft-failing the entry.

### What to carry forward

- **OCR-induced root-misattributions in Blau** (تخوية misread of تحمية) are persistent. Always verify the surface in the actual tafsir before fixing the lemma root in the entry. The candidate's `root_ar` field is suggestive only.

- **The "marked exception" pattern** (Num 25:13 Phinehas Form-I vs the otherwise-invariant Form-X) deserves explicit narrative space in promote-in-place mechanism rewrites. A claim of "invariant across the system" is stronger, not weaker, when it can call out the principled exceptions.

- **Cross-book promote-in-place compounds**: the three precedents now in the divergence file (נקל, שחמה', and Bamidbar's four new ones) form a methodological cluster. Devarim B1 should explicitly pre-scan all 7 cross-book lemmas for further extensions before mining the Devarim candidate pool.

- **Suffixed-form variants matter for the verifier**: ta-marbuta-opening (סלאמה → סלאמת), pronominal suffix harmonization (סלאמתכם), and definite-article prefixing (אלסלאמה) are all distinct surface forms. When extending verses[] across a system, include the suffixed/definite forms that surface in the cited verses, not just the bare lemma.
