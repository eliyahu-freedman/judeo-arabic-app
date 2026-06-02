# Phase 4 Devarim Batch 1 — Session Notes

**Date shipped:** 2026-05-29
**Apply script:** `scripts/apply_phase4_devarim_batch1.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 115 | 124 | +9 net-new |
| Tier distribution | 36 twist / 33 note / 46 gloss | 36 / 38 / 50 | +5 NOTE, +4 GLOSS |
| Promote-in-place verse extensions | — | 4 verses across 4 entries | סלאמה +Deut 27:7, יסתג'פר +Deut 9:20, בחפז +Deut 16:3, אצר +Deut 28:48 |
| Cross-book lemmas | 8 | 10 | +2 (בחפז, אצר); two existing lemmas (סלאמה, יסתג'פר) graduate to 3-book |
| Devarim verse attestations | 5 (unverified standing) | 24 | +19 |
| Devarim candidate pool | 78 raw / ~22 article-flattened | — | mined |
| Effective survival rate (article-flattened) | — | **13 ships / 22 articles = 59%** | Phase 4 5-book sweep COMPLETE |
| Gates | — | verify_divergence.py PASS · npm run build clean · 124/124 lemma-unique | all green |

---

## Per-entry rundown

### NEW ENTRIES — 5 NOTE

#### `אקרץ'` — Deut 2:21, 7:17, 9:3, 11:23, 12:2 (conquest-vocabulary system)
Semantic reframe of the entire Devarim conquest-discourse: Heb הוֹרִישׁ (Hiphil of ירש, framing the conquest as DISPOSSESSING/DRIVING OUT) → Ar Form I قَرَضَ ("to cut off, exterminate"), foregrounding ELIMINATION over DISPLACEMENT. Across 5 verses spanning the Anakim-displacement, Moses's hesitation, the divine-fire promise, the conquest-promise reiteration, and the cultic-site destruction injunction, Saadia consistently routes the Heb ירש-Hiphil through extermination-vocabulary. At Deut 9:3 he even uses קרץ' for both verbs in 'הוא ישמידם...והאבדתם' (= ינפד'הם...ותבידהם...פתקרצ'הם), collapsing the Heb's vocabulary-of-degree into a single extermination-frame. The choice is paradigm-defining: where the Heb preserves room for the displaced peoples to survive elsewhere, the Ar names total elimination. **Highest-leverage NOTE entry of the batch** — 5-verse system coverage with a coherent theological-translational signature.

#### `יסיב` — Deut 15:1, 15:2, 15:3 (shemittah-release system)
System-vocabulary calque covering the entire Sabbatical-year lexical field. Heb's שמט-root produces the institutional pair (the noun שְׁמִטָּה for the year + the Qal/Hiphil verbs for the release-acts); Saadia mirrors this morphological strategy through Ar Form II سَيَّبَ + verbal-noun تَسْيِيب, preserving the institutional-technical two-pole structure (act-of-releasing + period-of-release). The pastoral-Bedouin semantic field (animals set loose, debts released) matches the Heb sevenfold-cycle's release-of-claim structure. Cross-pericope consistency across Deut 15:1-3 plus 15:9 confirms the choice is lexical-fixed for the institution, not context-driven. Pedagogically distinctive at the morphological-parallelism level (Form II + verbal-noun mirrors Heb's coined-term strategy), in the same vein as the `מחפצה` precedent from Bamidbar B1.

#### `תכ'רסתם` — Deut 1:27 (spy-report rebellion)
Striking semantic flip on a paradigm-emotional verb: Heb רָגַן (rare verb, always pejorative — "to murmur, complain") frames the spies-report rebellion as the people's ACTIVE PRODUCTION OF complaint-speech. Saadia routes this through Ar Form V تَخَرَّسَ — the OPPOSITE-direction reflexive: "you reduced yourselves to silence, you became dumbfounded". The active-complaint frame inverts to a passive-silenced frame; the people aren't producing speech but ceasing it. The choice fits Saadia's broader tendency to read the wilderness-rebellions as failures of FAITH (silent doubt) rather than failures of OBEDIENCE (vocal complaint). Pairs cleanly with the Bamidbar B1 `ראם` entry (volitional reframe of physical-exploration verb תור) — both moves redirect spies-narrative agency from external action to internal volitional/emotional state.

#### `זאיל` — Deut 21:18 (rebellious-son rationalist reframe)
Rationalist-philosophical reframe of the wayward-son institution: Heb סוֹרֵר ("rebellious", a verb-of-political-opposition) → Ar زائل (active participle of زَالَ "to deviate from"), foregrounding the EPISTEMIC-MORAL dimension over the POLITICAL-AUTHORITY dimension. The Quranic-register idiom زائل عن الصواب ("deviating from the right") routes the Torah's institutional discipline through the philosophical school's discourse of soul-trajectories. The same verse's two participles get split across two semantic fields — זאיל (epistemic-philosophical "one who deviates") + מכ'אלף (logical-rhetorical "one who contradicts") — giving the legal-institutional son two simultaneous philosophical frames, neither of which is the Heb's political-rebellion frame.

#### `ממתעה` — Deut 23:18 (cultic-prostitute sexualized reframe)
Theologically-significant lexical refusal: Heb קְדֵשָׁה / קָדֵשׁ name the cultic-prostitute through the consecration-vocabulary (the SAME root that names Israelite priests' consecration). Saadia routes this through Ar مُمَتَّعَة / مُمَتَّع ("pleasure-object", passive participle of متع) — entirely abandoning the consecration-frame and renaming the figure by FUNCTION (sexual-utility) rather than STATUS (cultic-set-apartness). Where Heb concedes that the foreign cult-prostitute is "consecrated" (even if to the wrong god), Saadia REFUSES the consecration label. The prohibition becomes a CATEGORY-DELEGITIMIZATION rather than a CATEGORY-EXCLUSION. Pedagogically distinctive because the Heb-Ar pairing surfaces a real theological-rhetorical choice — Saadia's lexicon won't grant rival cults a consecration-vocabulary, even in the act of forbidding them.

### NEW ENTRIES — 4 GLOSS

#### `תנהזמו` — Deut 1:42 (battle-rout)
Non-cognate semantic-field substitution for the military-defeat passive: Heb נִגַּף (Niphal of נגף "to strike, defeat") → Ar Form VII إنهزم ("to be routed in battle"). The substitution replaces the Hebrew's strike-vocabulary frame (the divine STRIKE that causes the rout) with the Arabic's rout-vocabulary frame (the army-being-broken result). Cross-pericope consistency across Lev 26:17 / Num 14:42 / Deut 1:42 confirms it's Saadia's lexical-fixed choice for the military-defeat passive.

#### `צנגתאן` — Deut 25:13 (false weights)
Concrete-to-technical lexical specification: Heb אֶבֶן וָאֶבֶן ("stone and stone in your pouch") — a literal-objective description of the merchant-fraud — gets rendered with Ar صَنْجَتَان ("two weights", the dual of the Persian-loan technical commercial-weight substantive). The Heb names the deceptive object by its PHYSICAL SUBSTANCE; the Ar names it by its FUNCTIONAL CATEGORY. The Persian-loan صنجة marks the entry as drawn from the East-Arabic commercial-administrative register, fitting Saadia's preference for institutional-technical Arabic in weights-and-measures pericopes.

#### `אתקצאהם` — Deut 32:26 (Ha'azinu hapax)
Non-cognate lexical substitute for an obscure Hebrew hapax: Heb אַפְאֵיהֶם (a Ha'azinu hapax with disputed etymology — "scatter to corners" / "bring to nothing") → Ar Form VIII اقتصى ("pursue to the end, investigate exhaustively"). The choice elegantly covers BOTH possible Heb readings: a corner-extension (pursue them to the farthest reach) AND an annihilation (pursue until none remain). Showcases Saadia's method for hapax-handling: not literal-glossing but semantic-coverage selection.

#### `אלג'ראביב` — Deut 14:14 (jet-black ravens)
Register-elevation in the unclean-birds list: Heb עֹרֵב (standard biblical raven-substantive) → Ar broken-plural غُرَابِيب — a specifically poetic-elevated register form (Q35:27 "غَرَابِيبُ سُودٌ" "jet-black ravens"). The choice routes the dietary-prohibition through the Quranic-poetic register, elevating the prosaic list to the literary-register. Showcases Saadia's poetics-of-translation: even the dietary list gets elevated register.

### PROMOTE-IN-PLACE — 4 cross-book extensions

| Lemma | Before | Added | After total |
|---|---|---|---|
| `סלאמה` (peace-offering) | Shemot 24:5, 32:6; Bamidbar 6:14, 6:17, 7:17, 10:10 | Deut 27:7 (Mt. Ebal covenant ceremony) | 7 verses / 3 books |
| `יסתג'פר` (atonement-supplication) | Vayikra 5:6, 14:19, 16:6, 16:16, 16:30; Bamidbar 5:8, 8:12, 15:25, 17:11 | Deut 9:20 (Moses intercedes for Aaron) | 10 verses / 3 books |
| `בחפז` (in-haste) | Shemot 12:11 | Deut 16:3 (Pesach-reminder) | 2 verses / 2 books |
| `אצר` (yoke-burden) | Vayikra 26:13 | Deut 28:48 (Curses yoke-of-iron) | 2 verses / 2 books |

Key mechanism updates:
- **סלאמה** (now FIVE ritual systems): Sinai covenant ceremony + nazirite-completion + chieftains'-dedication + festival cycle + **Mt. Ebal covenant-renewal**. The cross-attestation arc now spans the entire covenant-renewal trajectory from Sinai through land-entry. סלאמה is the first lemma to graduate to **3-book attestation** in the entire divergence corpus.
- **יסתג'פר** (now spanning priestly AND prophetic atonement): the existing Vayikra+Bamidbar priestly-cultic context now extends to **Moses-as-intercessor** at Deut 9:20 (the golden-calf aftermath). The Heb's lexical distinction between priestly-atonement (כפר) and prophetic-intercession (התפלל) collapses into a single Arabic Form-X supplication-vocabulary, confirming the cross-pericope unification. New 1cs-perfect variant פאסתג'פרת surfaces for the first time. Second lemma to graduate to **3-book attestation**.
- **בחפז**: confirms the canonical Pesach-haste pair — Ex 12:11 original prescription + Deut 16:3 commemorative reminder. The Blau prose already cited Deut 16:3 explicitly; verses[] is now synced.
- **אצר**: confirms the Blessings-Curses chiastic pair — Lev 26:13 (yoke-broken at exodus) + Deut 28:48 (yoke-restored as curse). New variant אצרא (indefinite-accusative) surfaces at Deut 28:48. The Blau prose already cited Deut 28:48 explicitly; verses[] is now synced.

---

## Deferred buckets

### Devarim.skip (26)

| blau_id | root_ar | Reason |
|---|---|---|
| 13983 | أول | Direct adverbial cognate (בראשונה ~ أول) |
| 14868 | حصر | Ex 30:12 citation, not Devarim-anchored |
| 15084 | خبر | Methodology (Sefer ha-Shetarot), no Devarim |
| 15118 | خدع | Ex 22:15 + Proverbs, no clean Devarim anchor |
| 15403 | دجن | Blau headword misattributed — Saadia uses **ברّ** (~ Ar بَرّ) for the 7 Devarim דגן-attestations, not دجن. Defer for a separate ברّ-entry once the manuscript-tradition split is clarified. |
| 16765 | صحراء | Direct sense-pairing (שדה ~ صحراء) |
| 17158 | طول | Methodology, no clean Deut 32:39 substitution |
| 17212 | عتق | "דברים" = "matters" not the Book |
| 17256 | عدا | No Devarim citation |
| 18454-18456 | قدح cluster | Direct cognate at Deut 32:22 |
| 18694 | مقلب | Already covered by Bereshit-19 Sodom-narrative |
| 18778-18780 | مقام/قوم cluster | Direct cognate (Deut 5:15) |
| 18889-18890 | تكرير/كرب | No Devarim anchor |
| 19325 | ما | Routine particle-mapping |
| 19636 | نتج (14-row cluster) | Deut 3:5 ונגור = نجور 'bolt' — GLOSS-borderline cut for cluster-revisit in Phase 3 R2 |
| 19861 | تنغيم / nfd family (11 rows) | Already deferred from Vayikra B1 + Bamidbar B1; Deut 7:10 لانفاذه IS the canonical انفذ destruction-frame; consolidate at cluster-head in Phase 3 R2 |
| 19950-19953 | نهاية/ناهيك/نوء/ناب | Cluster artifact around 19954 نوبة (see borderline) |
| 20003 | يده / نال | Standard idiomatic-substitution for Deut 16:10 |

### Devarim.borderline (4)

NOTE/GLOSS-grade candidates cut at the 5-NOTE / 4-GLOSS cap for Batch 1, all promotable in Batch 2:

- **18619 قضى → יקתצ'י** (Deut 15:2 לא יגש = פלא יקתצ'י) — Form VIII اقتضى ("demand-payment") for Heb נגש (creditor's pressure-verb). Strong NOTE candidate; pairs with the יסיב shemittah-release entry as the creditor's complementary action. **Pair-up with יסיב in Batch 2.**
- **19379 ممد اليد → ממד ידך** (Deut 23:21 משלח-ידך = ממד ידך) — calque idiom for the Heb "outstretching of hand" undertaking-vocabulary. GLOSS-borderline.
- **19954 نوبة → אלנווב** (Deut 18:8 ממכריו = אלנווב) — striking exegetical reframe: Heb obscure "his sale-proceeds" → Ar "priestly duty-rotations (مَشَامِر הכהונה)". NOTE-borderline; adopts the rabbinic-Sifrei interpretation.
- **19775 تناصى → תנאציאן** (Deut 25:11 וינצו = תנאציאן) — Form VI mutual-reciprocity calque morphologically mirroring the Heb Niphal. GLOSS-borderline; fits the מחפצה morphological-parallelism criterion.

### Devarim._cluster_dupes_logged (13)

13 cluster groups logged for potential re-mining; the largest (19636-19649 نٰtج/nٰtr/nٰjr 14-row + 19861-19871 nfd family 11-row) are pre-flagged as Phase 3 R2 candidates for cross-book destruction-vocabulary consolidation. Full list in `data/_blau_saadia_deferred.json#/devarim/_cluster_dupes_logged`.

---

## Yield observations

### 1. Phase 4 5-book sweep is COMPLETE

Devarim B1 closes the Phase 4 cross-book mining series. Cumulative running totals across all 5 books:

| Book | Net-new entries | Promote-in-place verse extensions | Total verse attestations |
|---|---|---|---|
| Bereshit (B1-4 + Phase 3 R1) | 72 | — (anchor book) | 100 |
| Shemot (B1+B2) | 15 | 1 (נקל) | 44 |
| Vayikra (B1) | 13 | 1 (שחמה') | 31 |
| Bamidbar (B1) | 9 | 4 (מוגה, סלאמה, ד'כוה, יסתג'פר) | 42 |
| **Devarim (B1)** | **9** | **4 (סלאמה, יסתג'פר, בחפז, אצר)** | **24** |
| **Total** | **124** | **10** | **241** |

The corpus is now ready for **Phase 3 R2 cross-book TWIST scan**. All 5 books have ≥1 cross-book lemma; 2 lemmas (**סלאמה**, **יסתג'פר**) span 3 books each; the methodology has 10 promote-in-place precedents to draw on.

### 2. Effective survival rate continued the pattern

| Pass | Raw | Article-flattened | Ships | Article-survival |
|---|---|---|---|---|
| Bereshit | 165 | ~80 | 19 | ~24% |
| Shemot B1 | ~180 | ~90 | 20 | ~22% |
| Shemot B2 | ~165 | ~85 | 15 | ~18% |
| Vayikra B1 | 76 | 32 | 13 | 41% |
| Bamidbar B1 | 32 | 18 | 13 | 72% |
| **Devarim B1** | **78** | **22** | **13** | **59%** |

Devarim's 59% sits between Vayikra's 41% and Bamidbar's 72%, fitting the pattern: as the pool shrinks AND as cross-book promote-in-place precedents accumulate, the article-survival rate climbs. Devarim's pool was somewhat larger than Bamidbar's (78 vs 32 raw, 22 vs 18 articles) because it pulls in 5-book noisier-cluster citations (the 14-row 19636 cluster, the 11-row nfd family), but the surviving ships per article matches the high-cross-book-reuse profile of late-Pentateuchal mining.

### 3. The first 3-book lemmas surfaced

This batch produces the **first two 3-book lemmas in the entire divergence corpus**: סלאמה (Shemot + Bamidbar + Devarim) and יסתג'פר (Vayikra + Bamidbar + Devarim). The cross-Pentateuchal arc is structurally significant:

- **סלאמה** spans the full covenant-renewal trajectory: Sinai (Ex 24/32) → Mishkan-dedication (Num 7) → festival-cycle (Num 10) → land-entry covenant (Deut 27). One Arabic word holds the entire covenant-ceremony semantic field.
- **יסתג'פר** spans the priestly-AND-prophetic atonement field: Vayikra priestly-ritual core → Bamidbar communal-cultic extensions → Deut 9:20 Moses-as-intercessor. The Heb's lexical distinction between priestly-atonement (כפר) and prophetic-intercession (התפלל) collapses into a single Arabic Form-X supplication-vocabulary, confirming the cross-pericope unification at the level of mediated-atonement broadly.

These two lemmas are the strongest evidence that Saadia operates with stable cross-Pentateuchal technical vocabulary for ritual-theological systems, and they set the template for Phase 3 R2's retroactive scan of the existing 36 TWIST entries for similar multi-book consolidation.

### 4. Devarim-specific signature: rationalist-philosophical reframe

The two Devarim NOTE entries `זאיל` (סורר → "deviant from right") and `תכ'רסתם` (רגן → "be silenced") show a coherent Saadyan-Devarim signature: routing the Heb's institutional-political vocabulary (rebellion, complaint, dispossession) through the rationalist-philosophical vocabulary (deviation, dumbfoundedness, extermination). The four NEW NOTE entries combine to map a single Saadyan-translational program for the Mosaic-discourse Book — Devarim's homiletic-rhetorical register gets re-clothed in classical-Arabic philosophical-theological garb. Worth noting in future writeups about Saadia's translation-philosophy.

### 5. The שופט / חאכם judicial-vocabulary cluster did NOT ship

The Phase A cross-book pre-scan surfaced 6 Devarim hits for **חאכם / אלחאכם** (the bare/definite "judge" form), all in legal-administrative passages (Deut 17:9, 17:12, 21:19, 22:15, 25:2, 25:7) where Saadia consistently renders Heb שופט with Ar حاكم. This is distinct from the existing **חאכמא** TWIST entry (which is specifically about Saadia's accusative-of-state insertion of חאכמא = "as one who decrees" into divine-speech verses). The judicial-vocabulary cluster is a CANDIDATE for a new Devarim-specific NOTE entry about Saadia's systematic H-K-M-for-שפט substitution across Devarim's judicial pericopes — but it overlaps lexically with the existing חאכמא TWIST, and the substitution is largely cognate-direct (Heb חכם ~ Ar حكم). Logged for Phase 3 R2 cross-book scan: if the H-K-M cluster surfaces parallel attestations in Shemot's judicial passages (Ex 18:13-26 Jethro / Ex 22:8-9 elohim-as-judges / Ex 23:1-3 court-of-witnesses), it can ship as a new NOTE about Saadia's broader judicial-vocabulary translational strategy.

---

## Recommended next-session strategy

In priority order:

1. **Phase 3 R2 cross-book TWIST scan** — the headline next-session. Phase 4's 5-book sweep is now complete; methodology is mature with 10 promote-in-place precedents (including the two 3-book lemmas סלאמה + יסתג'פר). Retroactively scan the existing 36 TWIST entries for multi-book attestations using the same promote-in-place pattern. Highest-leverage move available — should ship 8-15 verse extensions across the 5-book corpus. Specifically scan:
   - The 5-book Sodom-cluster (Bereshit 19 → Lev 18 prohibitions → Deut 29:22 → Isa 13 prophetic → Jer 49 prophetic).
   - The 5-book covenant-vocabulary cluster (ברית = عهد across all 5 books — verify whether Saadia uses different Arabic-genres in different contexts).
   - The cross-book divine-attributes cluster (חאכמא TWIST entry: scan whether Bamidbar/Devarim divine-speech passages get the same circumstantial-accusative).
   - The judicial-vocabulary cluster (חאכם judge — see Yield Observation #5 above; if the Shemot Jethro/elohim passages parallel the Devarim pattern, ship as a new NOTE).
   - The conquest-vocabulary cluster (the new אקרץ' entry: scan whether Bamidbar's כאלון Anakim-vocabulary surfaces the same Form I قرض).

2. **Vayikra Batch 2 (Track B)** — the 4 NOTE/GLOSS borderlines (כ'אמע, קצבה, לג, מסוחייה) still standing from Vayikra B1, with the Devarim Batch 1 borderlines (יקתצ'י, ממד-יד, נווב, תנאצי) now available for a coordinated Vayikra-Devarim B2 pass. Strategically sound to run after Phase 3 R2 lands its first wave, since R2 may surface additional Vayikra-Devarim cross-attestations.

3. **Phase 3 R1 second wave (Shemot/Vayikra/Bamidbar/Devarim STRICT-tier additions)** — the verifier's per-book gate is currently active only for Bereshit (35 twist entries); the other 4 books are at 1-2 twists and skip the gate. To activate the gate uniformly, Phase 3 R1 needs to add ≥5 TWIST entries to each of Shemot/Vayikra/Bamidbar/Devarim. Devarim's new NOTE entries (אקרץ', יסיב, ממתע) are TWIST-adjacent and could promote to TWIST in R1 if Blau-verification confirms paradigm-shifting status. Lower priority than R2.

4. **Devarim Batch 2 (cluster-head re-mining)** — the 13 cluster groups logged in Devarim B1's `_cluster_dupes_logged` flagged article-heads we skipped. The largest (19636-49 nٰtج/nٰjr 14-row cluster at Deut 3:5 ונגור; 19861-71 nfd family 11-row at Deut 7:10 אנפד'הם) may have tier-grade GLOSS readings hidden inside OCR-mangled body excerpts. Lower priority than R2; can wait until R2 surfaces consolidated cross-book destruction-vocabulary that pulls these clusters into a coherent multi-book entry.

---

## Pattern reminders for future batches (Phase 3 R2 onward)

### What worked in Devarim B1

- **Direct-tafsir scanning for promote-in-place candidates** continued to be high-yield: Phase A's 9-lemma pre-scan surfaced 4 ships (סלאמה, יסתג'פר, בחפז, אצר), of which 2 were NOT in my initial 9-lemma list (בחפז + אצר surfaced via a secondary-pass grep of the divergence file for any lemma whose blau_dict-prose explicitly cited Deut). **Phase A should run BOTH passes from the start**: (1) the explicit cross-book-lemma list, AND (2) a grep of the entire divergence file for entries whose blau_dict.sense mentions the target book.

- **The 3-book graduation event** for סלאמה and יסתג'פר is the strongest pedagogical-cleanup signal in the corpus. Future cross-book extensions should foreground 3+ book lemmas in the entry's mechanism, because the cross-Pentateuchal arc tells a structural story that single-book or 2-book entries can't.

- **The "first-person perfect" variant graduation** for יסתג'פר (פאסתג'פרת at Deut 9:20) demonstrates that promote-in-place can also extend variants[] beyond the originally-shipped morphological inventory. When a new book introduces a new conjugation/tense, the variant capture matters for the verifier's normalized-token match.

### What to carry forward

- **Blau-attribution caution**: the 15403 dجn / ברّ misattribution (Blau cites dجn but Saadia surface uniformly uses ברّ for דגן) is the second OCR-induced misattribution after Bamidbar B1's تخوية ~ تحمية case. Always cross-check the Blau body-OCR against the actual Cairo 2019 surface; the candidate's `root_ar` is suggestive, not authoritative. **Re-mine 15403 ברّ in a future batch as a separate entry** if the ברّ Hebraizing-loan choice for דגן proves systematic.

- **The hapax-handling pattern** (אתקצא for Deut 32:26 אפאיהם) is now a clear Saadyan strategy: when the Heb is obscure, Saadia selects an Arabic verb whose semantic range covers the relevant interpretive options, rather than guessing a single literal meaning. Worth flagging in future entries that handle Heb hapaxes.

- **The morphological-mirroring criterion** (Form II + verbal-noun pairing for institutional terminology) continues to be a strong NOTE-tier signal. יסיב + תסייב mirrors מחפצה + משמרת (Bamidbar B1); both ship specifically because the COINING-STRATEGY at the morphological level parallels the Heb's coining-strategy. Phase 3 R2 should explicitly look for parallel-coining as a multi-book extension criterion.

- **Devarim-specific Saadyan signature**: routing institutional-political vocabulary (rebellion, complaint, dispossession) through rationalist-philosophical vocabulary (deviation, dumbfoundedness, extermination). The combined Devarim-B1 NOTE entries map this program; future Devarim Batch 2 + Phase 3 R2 mining should look for additional Devarim-specific philosophical-register lexical choices, especially in the Ha'azinu (Deut 32) + Vezot HaBerakhah (Deut 33) poetic-blessing sections.

- **Cross-book promote-in-place is now the DOMINANT pattern, not just the standard pattern**. Out of 13 Devarim B1 ships, 4 are promote-in-place (31%) and 9 are net-new. Bamidbar B1 had 4/13 = 31% same ratio. The cross-Pentateuchal-arc-extension methodology is the high-leverage move going forward; Phase 3 R2 should expand it from 2-book to 3-book to 5-book lemmas systematically.
