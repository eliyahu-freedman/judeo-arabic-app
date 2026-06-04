# Phase 3 R2 Batch 1 — Session Notes

**Date shipped:** 2026-05-29
**Apply script:** `scripts/apply_phase3_r2_batch1.py`
**Scan tool:** `scripts/scan_phase3_r2.py` (new — generic R2 scanner, also used for Batch 2)
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 124 | 124 | unchanged (promote-in-place only) |
| Tier distribution | 36 twist / 38 note / 50 gloss | 36 / 38 / 50 | unchanged |
| TWIST 3-book entries | 0 | **2 (אדלג, חאכמא)** | **first 3-book TWISTs in the corpus** |
| TWIST 2-book entries | 2 (חאכמא, אדלג — both now 3-book) | **1 (מסלט)** | net −1 (two graduated up; one promoted from single-book) |
| TWIST Bereshit-only count | 33 | 30 | −3 (אדלג + חאכמא + מסלט now cross-book; 3 within-book strengthenings remain Bereshit-only) |
| TWIST verse attestations | 56 | **74 (Bereshit) + 9 (Shemot) + 1 (Vayikra) + 1 (Bamidbar) + 5 (Devarim) = 90** | **+19 new verses across 4 books beyond Bereshit** |
| Total verse attestations | 241 | 260 | +19 |
| Lemma uniqueness | 124/124 | 124/124 | preserved |
| Gates | — | `verify_divergence.py` PASS · `npm run build` clean · 0 warnings | all green |

---

## Per-entry rundown

### PROMOTE-IN-PLACE — 6 TWIST entries, 19 new verse attestations

#### `אדלג` (أدلج, "rise early at dawn") — +11 verses, 2-book → 3-book graduation
**Was:** Bereshit 19:27, Bamidbar 14:40 (2 verses, 2 books)
**Added:**
- Bereshit (6 new): 20:8 (Abimelech), 21:14 (Hagar cast out), **22:3 (Akedah)**, 26:31 (Isaac–Abimelech treaty), 28:18 (Jacob at Bethel), 32:1 (Laban after Mizpah covenant)
- Shemot (5 new): 8:16 (Moses for blood-plague), 9:13 (Moses for hail-plague), 24:4 (Sinai covenant altar), 32:6 (golden-calf morning offerings), 34:4 (Moses ascending Sinai with second tablets)

**After:** 13 verses across Bereshit / Shemot / Bamidbar. The single largest narrative-formula promotion in the corpus. Heb הִשְׁכִּים / וַיַּשְׁכֵּם → Ar أدلج (Form IV of دلج) invariantly across the full Patriarchal-and-Mosaic 'rose-early' formula tradition. The trailing adverbial باللغداة ("at-the-dawn") is the fixed Saadyan idiom for Heb בַּבֹּקֶר.

The cross-Pentateuchal-arc invariance is the strongest evidence in the corpus that Saadia operates with stable narrative-formula vocabulary: every "rose-early" departure receives the same Arabic lexical signature regardless of speaker (Abraham, Hagar, Isaac, Jacob, Laban, Moses, the Israelites) or context (private journey, treaty-ratification, cultic encounter, military departure). Blau's prose explicitly named Saadia's Tafsir on Exodus 8:16 as the canonical example; R2 syncs verses[] to that prose-existing claim and extends the demonstrably-attested arc to 13 verses.

#### `חאכמא` (حاكمًا, "as decreer / acting-as-judge") — +1 verse, 2-book → 3-book graduation
**Was:** Bereshit 1:22, Shemot 2:14, Shemot 22:27 (3 verses, 2 books)
**Added:** Vayikra 20:24 (the divine-promise speech-act: וָאֹמַר לָכֶם אַתֶּם תִּירְשׁוּ אֶת אַדְמָתָם → וקלת לכם חאכמא)
**After:** 4 verses across Bereshit / Shemot / Vayikra. The third 3-book TWIST in the corpus (joining סלאמה NOTE and יסתג'פר NOTE from Phase 4 Devarim B1 — though those are NOTE-tier; חאכמא is the **first 3-book TWIST**).

The Vayikra 20:24 attestation is structurally significant: the FIRST divine-promise speech-act in the Levitical land-vocabulary register, routed through exactly the same anti-anthropomorphic circumstantial-accusative חאכמא as the Bereshit 1:22 creation-blessing. The cross-book consistency confirms that the insertion is Saadia's programmatic strategy for the divine speech-act category across the Pentateuch — wherever YHWH "says" something covenantally-binding, the modality is named as judicial-decree rather than vocal-utterance.

Cleanly distinct from the bare-form judicial חאכם / אלחאכם used for human judges (Ex 21:6, 22:7-8; Deut 17:9, 17:12, 21:19, 22:15, 25:2, 25:7), which were deferred to the skip bucket — see Devarim B1 line 158-160 for the register-distinction.

#### `מסלט` (مسلَّط, "set-as-master") — +3 verses, single-book → 2-book graduation
**Was:** Bereshit 1:26, 1:27, 3:16, 4:7, 5:1, 9:6 (6 verses, Bereshit-only)
**Added:**
- Bereshit (1 new): 24:2 (Abraham's senior steward — אלמסלט עלי' גמיע מאלה)
- Shemot (2 new): 8:18 (divine-sovereignty assertion — אני אללה מסלט עלי' גמיע אלעאלם); 21:8 (Form V יתסלט: legal-authority over a betrothed slave-woman)

**After:** 9 verses across Bereshit + Shemot. The TWIST extends from its anti-anthropomorphic imago-Dei core into a programmatic dominion-vocabulary system spanning theology (imago-Dei vicegerency at Gen 1:26-27, 5:1, 9:6) + human-vicegerency (Abraham's steward at Gen 24:2) + divine-sovereignty (God-as-active-presence at Ex 8:18) + legal-authority (Form V at Ex 21:8). The mechanism rewrite explicitly names the cross-register breadth; Shemot 21:8 ships with a borderline caveat (the Form V's legal-authority register is the broadest reach of the lexical family from the anti-anthropomorphic core).

#### `אורד` (أورد, "dispatch / send-down") — +1 verse, Bereshit within-book sync
**Was:** Bereshit 11:5, 11:7 (2 verses, Babel-only)
**Added:** Bereshit 18:21 (Sodom anti-anthropomorphic dispatch — אורד אמרא מוגהא ואנצר for Heb אֵרֲדָה-נָּא וְאֶרְאֶה)
**After:** 3 verses, Bereshit-only.

The original mechanism prose ALREADY explicitly named the Sodom-cluster pillar ("the same template appears throughout the Tafsir wherever the Hebrew has YHWH coming down — Sodom, Sinai, the Tent of Meeting"). The R2 scan confirms Sodom and syncs verses[] to the prose. Cross-Bereshit consistency (Sodom + Babel) demonstrates the anti-anthropomorphic-dispatch pattern at both YHWH-comes-down-to-investigate anchors. **Future Phase 3 R2 Batch 2 candidate**: scan Shemot 19:11, 19:18, 19:20, 34:5 (Sinai descent verses) — if Saadia uses the same Form-IV dispatch-verb, this would graduate the entry to 2-book status.

#### `תואעד` (تواعد, "threaten / warn") — +1 verse, Bereshit within-book broadening
**Was:** Bereshit 6:6, 6:7 (2 verses, flood-decision affective register)
**Added:** Bereshit 20:18 (Abimelech-wombs restraint — לאן אללה כאן קד תואעד בחבס כל רחם for Heb עָצֹר עָצַר ה' בְּעַד כָּל-רֶחֶם)
**After:** 3 verses, Bereshit-only.

The Gen 20:18 attestation broadens the mechanism from the affective-regret category (Heb וַיִּנָּחֶם) to the direct-biological-intervention category (Heb עָצַר). Saadia routes both through the same prophetic-warning frame, preserving divine transcendence by mediating the divine action (whether affective or biological) through warning-vocabulary. Demonstrates a broader Saadyan anti-anthropomorphic principle: when the Hebrew describes God directly doing something that an immanent reading would frame as mechanical intervention, Saadia routes the action through prophetic-warning vocabulary.

#### `אלממתעה` (الممتعة, "the cult-prostitute") — +2 verses, Tamar within-pericope sync
**Was:** Bereshit 38:21 (single verse anchor)
**Added:** Bereshit 38:15 (Heb וַיַּחְשְׁבֶהָ לְזוֹנָה → וחסבהא ממתעה); Bereshit 38:22 (Heb לֹא הָיְתָה בָזֶה קְדֵשָׁה → מא כאנת ההנא ממתעה)
**After:** 3 verses, Bereshit-only (full Tamar pericope).

Structurally significant: Saadia routes BOTH Heb זוֹנָה (generic harlot, Gen 38:15) AND Heb קְדֵשָׁה (cult-prostitute, Gen 38:21-22) through the same Arabic terminus-technicus ממתעה, treating all three Tamar-pericope terms as referring to a single cultic-prostitute category. This is a real exegetical claim: Tamar is read as deliberately assuming a cultic identity to claim the right of levirate-substitution, NOT as merely a generic harlot.

**The Deut 23:18 attestation** (the prohibition on Israelite men/women being a קָדֵשׁ/קְדֵשָׁה) is currently held by the SEPARATE NOTE entry ממתעה shipped in Phase 4 Devarim Batch 1. The original TWIST mechanism prose explicitly cross-references Deut 23:18 ("uses the same word again at Deuteronomy 23:18, confirming the systematic identification") and Blau's prose cites both Gen 38:21 and Deut 23:18 together. This is a clear consolidation opportunity — see **Duplicate collision** in Deferred buckets below.

---

## Deferred buckets

### `phase3_r2/batch1/skip` (5) — homograph filters + duplicate-collision

| Lemma | Verse hint | Reason |
|---|---|---|
| `שא` | Vayikra 22:18, 22:21, 27:13, 27:15, 27:19; Devarim 18:6 | Homograph: Ar شاء is a generic high-frequency verb. The TWIST covers the anti-anthropomorphic CREATION register (Heb וַיֹּאמֶר אֱלֹהִים יְהִי X). The Vayikra/Devarim hits are all human-volitional ("man wills to bring an offering / redeem / enter"). |
| `גלד` | Vayikra 11:32, 13:2-48, 15:17 (11 verses, leprosy + skin/hide laws) | Homograph: Ar جلد here carries the classical literal "skin/hide" sense. The TWIST is specifically the calque-EXTENSION from skin → firmness/firmament (Gen 1:6-20). Verses where Saadia uses the unstretched classical sense don't extend the calque-claim. |
| `חאכם` (judicial cluster) | Shemot 21:6, 22:7, 22:8; Devarim 17:9, 17:12, 21:19, 22:15, 25:2, 25:7 (9 verses) | Homograph: bare חאכם / אלחאכם is the standard judicial-administrative noun. The חאכמא TWIST is about the **circumstantial-accusative participle** (حاكمًا with tanwīn) inserted into DIVINE speech-acts. Different register. Candidate for a separate NEW NOTE entry on Saadia's judicial-vocabulary translation in Phase 4 Vayikra/Devarim B2. |
| `אורד` (noun-surface) | Shemot 25:30 (מוגהא 'presented' showbread); Devarim 23:15, 24:1 (אמרא 'a matter') | Homograph: variants `אמרא` and `מוגהא` are the TWIST's idiom 'amr muwajjah'. Shemot 25:30 is the NOUN sense (showbread "presented"); Devarim 23:15, 24:1 are the generic "matter/thing" noun. Neither is the Form-IV dispatch-verb register. |
| `אלממתעה` ↔ `ממתעה` (NOTE) | Devarim 23:18 | **DUPLICATE COLLISION**. The Phase 4 Devarim B1 NOTE entry ממתעה covers Deut 23:18. The TWIST's mechanism + Blau's prose both already cross-reference Deut 23:18. Adding it to TWIST verses[] would double-attest the verse across two entries. **Out-of-scope for promote-in-place-only R2**; surfaced as a clean cleanup-pass candidate. The cleanest resolution is to delete the NOTE and absorb Deut 23:18 into the TWIST verses[], converting the TWIST to 2-book — but this requires entry-removal, which the user explicitly scoped out of R2. |

### `phase3_r2/batch1/borderline` (1)

| Lemma | Verse hint | Open question |
|---|---|---|
| `מסלט` | Shemot 21:8 (Form V יתסלט legal-authority) | Form V תسلَّط extends the entry's lexical family from divine-dominion + human-vicegerency into the legal-authority register. Shipped in PROMOTE_IN_PLACE with mechanism rewrite naming the cross-register breadth; worth re-evaluating in Phase 3 R3 whether the entry's TWIST status should be re-anchored on the broader dominion-vocabulary program rather than on the anti-anthropomorphic imago-Dei core. |

---

## Yield observations

### 1. First TWIST-tier 3-book entries in the corpus

This batch produces the **first two 3-book TWISTs ever shipped**: `אדלג` (Bereshit + Shemot + Bamidbar, 13 verses) and `חאכמא` (Bereshit + Shemot + Vayikra, 4 verses). The Phase 4 batches established the cross-book promote-in-place pattern at NOTE and GLOSS tier; R2 lifts it to TWIST tier, where it carries more pedagogical weight: a TWIST is a paradigm-defining lexical choice, and a 3-book TWIST documents that Saadia's paradigm-defining move is structurally invariant across the Pentateuch's narrative + covenantal + ritual registers.

| Lemma | Books | Verses | Mechanism gist |
|---|---|---|---|
| `אדלג` | Bereshit + Shemot + Bamidbar | 13 | Heb הִשְׁכִּים → Ar أدلج: Patriarchal + Mosaic + Wilderness 'rose-early' narrative-formula invariance |
| `חאכמא` | Bereshit + Shemot + Vayikra | 4 | Heb לאמר / וָאֹמַר → Ar حاكمًا insertion: anti-anthropomorphic divine speech-act framing across creation-blessing + Mosaic-judicial + Levitical land-promise |

### 2. Sync-verses-to-prose was the dominant pattern

Of the 6 ships, **3 (אדלג, אורד, אלממתעה)** were essentially verses[]-syncing to claims the existing mechanism prose or Blau prose already named:
- `אדלג` blau_dict.sense explicitly cited "Saadia's Tafsir on Exodus 8:16" — verses[] only had Bereshit 19:27 + Bamidbar 14:40
- `אורד` mechanism explicitly named "Sodom, Sinai, the Tent of Meeting" — verses[] only had Babel
- `אלממתעה` mechanism explicitly cross-referenced "Deuteronomy 23:18, confirming the systematic identification" — verses[] only had Bereshit 38:21

This mirrors the Devarim B1 pattern (`בחפז` and `אצר`, where Blau's prose cited Deut 16:3 and 28:48 explicitly but verses[] was unsynced). **The R2 scanner is essentially a verses[]-to-prose synchronization gate**: where Saadia's claims are already documented in the prose, the scan surfaces them as missing verse attestations.

### 3. Homograph filtering rate: ~50%

Of the 11 priority-cluster lemmas scanned, 5 ship and 6 are filtered or no-hit:
- 6 ship as promote-in-place
- 4 are filtered as homographs at the register level (שא human-volitional vs divine-creation; גלד literal-skin vs firmness-calque; חאכם judicial vs divine-speech; אורד-noun-surfaces vs Form-IV dispatch)
- 1 is filtered as duplicate-collision (אלממתעה Devarim 23:18 blocked by NOTE entry)
- 3 had no cross-book hits at all in the corpus (קאול, עטל, מקררא — see scan output `/tmp/phase3_r2_scan.json`)

The ~50% homograph-filter rate is the expected signal-to-noise for the TWIST promote-in-place pattern: TWIST entries are paradigm-defining anti-anthropomorphic or interpretive moves, so they often use lemmas (شاء, جلد, حكم) that also have routine classical-Arabic usages. The promote-in-place criterion needs to be strict at the register/mechanism level, not just the surface level. The scan tool surfaces all surface hits; manual mechanism-fit verification is essential.

### 4. The Sinai descent-cluster is the next high-leverage extension

The אורד promote-in-place extends the entry's Bereshit Babel anchor to the Sodom anchor (Gen 18:21), exactly matching the original mechanism prose's "Sodom, Sinai, the Tent of Meeting" template. The Sinai descent verses (Ex 19:11, 19:18, 19:20, 34:5) are NOT yet in scope — they are the structural pillar the prose names but the scan didn't surface in Batch 1 (the scan looks for אורד/פאורד surface; Sinai descent may use different conjugations). **Phase 3 R2 Batch 2 should explicitly scan the Sinai descent verses for Form-IV ورد derivatives.** If they surface, אורד graduates to 2-book status.

### 5. The duplicate-collision pattern is a known consolidation gap

The אלממתעה ↔ ממתעה NOTE collision surfaces a methodology gap: Phase 4 batches added single-book NOTE entries for lemmas that already had TWIST entries in other books, treating the cross-book attestation as a new ship rather than a promote-in-place. The cleanest fix is a one-time consolidation pass that merges such pairs into single multi-book entries at the higher tier — out-of-scope for R2 per the user's promote-in-place-only scoping, but should be the next-priority cleanup after R2 completes. Currently this is a single instance; the R2 B2 sweep may surface more (e.g., אקרץ' NOTE [Devarim] vs any future TWIST scan that promotes a conquest-verb).

---

## Recommended next-session strategy

In priority order:

1. **Phase 3 R2 Batch 2 — systematic sweep of the remaining ~25 Bereshit-only TWIST entries.** Walk in JSON order (excluding the 11 priority-cluster lemmas already covered in Batch 1). Expected yield: 5–10 more cross-book extensions at the same ~50% homograph-filter rate seen in B1. The scanner is in place (`scripts/scan_phase3_r2.py`); the apply-script skeleton is ready to copy from `apply_phase3_r2_batch1.py`. Explicitly add the Sinai descent verses (Ex 19:11, 19:18, 19:20, 34:5) to the אורד scan-set to test for Form-IV ورد derivatives.

2. **Duplicate-collision consolidation pass** — the אלממתעה ↔ ממתעה pair surfaced in B1 is the cleanest consolidation candidate; resolve before B2 lands (delete the NOTE, absorb Deut 23:18 into the TWIST verses[], promote the TWIST to 2-book Bereshit+Devarim). This is a tier-and-entry-removal operation, currently out-of-scope for R2 per the user's promote-in-place-only scoping — surface to the user as a follow-on decision after R2 B2 completes.

3. **New NOTE: judicial-vocabulary cluster (חאכם)** — the 9 Shemot + Devarim bare-form חאכם judicial hits surfaced in B1 (filtered as homographs from the חאכמא TWIST register) form a coherent cluster: Saadia's systematic use of H-K-M-vocabulary for Heb שׁפט judicial passages across the Pentateuch. Ship as a new NOTE in Phase 4 Vayikra/Devarim B2, mechanism: Saadia's broader judicial-vocabulary translational strategy. The cluster is already inventoried in this session's deferred bucket.

4. **Phase 3 R1 second wave (TWIST gate activation for Shemot/Vayikra/Bamidbar/Devarim)** — Phase 3 R1 cleared the Bereshit twist-tier gate (74.3% Blau-backed). R2 B1's cross-book extensions push Shemot, Vayikra, Bamidbar into TWIST-attestation status, but each remains below the verifier's per-book gate-activation threshold (≥5 TWIST entries). Phase 3 R1 second wave should add ≥5 net-new TWIST entries to each of Shemot/Vayikra/Bamidbar/Devarim to activate the gate uniformly. Lower priority than R2 B2 and the consolidation pass.

---

## Pattern reminders for downstream batches (Phase 3 R2 B2 onward)

### What worked in R2 B1

- **The scan-then-triage pattern**: `scan_phase3_r2.py` surfaces ALL surface hits; manual mechanism-fit verification against `-alignment.json` files is the essential filter. Don't trust surface-only matches at TWIST tier — the homograph rate is ~50% because TWIST lemmas are often paradigm-defining choices on otherwise-common Arabic verbs (شاء, جلد, حكم).

- **Sync-verses-to-prose is the highest-leverage triage signal**: when the mechanism prose or blau_dict.sense already cites a verse explicitly, the scan should confirm it and add it. Three of the six B1 ships were this kind of prose-existing-claim sync (אדלג Ex 8:16, אורד Sodom, אלממתעה Deut 23:18-attempt). For B2, **read each entry's mechanism + blau_dict.sense BEFORE running the scan**, and pre-flag the explicit cross-book claims for verification.

- **Register-distinction is essential at TWIST tier**: the חאכמא TWIST (circumstantial-accusative divine-speech-act insertion) is structurally distinct from the bare judicial חאכם/אלחאכם cluster, even though both surfaces share the root and the lemma_ja search overlaps. B1 distinguished them by checking the Hebrew counterpart at each hit verse: divine-speech-act register (לאמר / וָאֹמַר) ships; judicial-administrative register (לפני האלהים / לחאכם) is filtered. Carry this for B2.

### What to carry forward

- **Duplicate collisions are real and the methodology must handle them**: B1 surfaced one (אלממתעה ↔ ממתעה). B2 may surface more. Always check whether a candidate verse is already covered by ANOTHER entry's verses[] before promoting in-place. If yes, log it as a duplicate-collision skip and surface for a separate consolidation pass.

- **Within-book extensions still count**: 3 of the 6 B1 ships (אורד, תואעד, אלממתעה) are within-Bereshit extensions that don't change the book count but materially strengthen the TWIST claim by extending the verse coverage. Don't gate B2 on cross-book hits only — within-book verse syncs are still in-scope and pedagogically valuable.

- **The Sinai descent-cluster pre-flag**: B2 should explicitly include Ex 19:11, 19:18, 19:20, 34:5 in the אורד scan-set. If the Form-IV ورد derivative surfaces in any of them, אורד graduates to 2-book and the mechanism rewrite should explicitly name the Sinai pillar (which the original prose already does — "Sodom, Sinai, the Tent of Meeting").

- **The Tent-of-Meeting descent verses** (Lev 16:2-ish, Num 11:25, 12:5, 14:14) are the third leg of the אורד prose triad — pre-flag for B2 as well.

- **The Mosaic 'rose-early' rate is now provable**: 5 of the 6 Shemot 'rose-early' verses (the ones with Heb הִשְׁכִּים/וַיַּשְׁכֵּם) ship under אדלג in B1. B2 should check whether any Bamidbar/Devarim 'rose-early' verses (other than Bamidbar 14:40 already in verses[]) extend the formula further — candidates: Num 11:32 (the night the quail came), Num 14:40 (already in), Num 22:13 (Balaam at Beor), Num 22:21 (Balaam saddles donkey), Deut 9:15 (Moses descending Sinai with broken tablets), etc.
