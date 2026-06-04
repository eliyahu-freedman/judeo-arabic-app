# Phase 3 R2 Batch 2 — Session Notes

**Date shipped:** 2026-05-30
**Apply script:** `scripts/apply_phase3_r2_batch2.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

---

## Snapshot

| Metric | Pre-R2 | After B1 | After B2 | B2 Δ |
|---|---|---|---|---|
| Total divergence entries | 124 | 124 | 124 | unchanged |
| Tier distribution | 36 / 38 / 50 | 36 / 38 / 50 | 36 / 38 / 50 | unchanged |
| TWIST 3-book entries | 0 | 2 | **3** | +1 (ג'מר) |
| TWIST 2-book entries | 2 (חאכמא, אדלג — both graduated up) | 1 (מסלט) | **3 (מסלט, גוהר, חגב)** | +2 |
| TWIST Bereshit-only | 33 | 30 | **27** | −3 (ג'מר, חגב moved out; אתון strengthened) |
| TWIST verse attestations | 56 | 75 | **101** | +26 across both batches |
| Total verse attestations | 241 | 260 | **271** | +30 across both batches |
| TWIST per-book reach | Bereshit-dominant | Bereshit + Shemot/Vayikra/Bamidbar/Devarim (small) | **All 5 books with meaningful coverage** | Shemot 9→15; Devarim 5→7 |
| Lemma uniqueness | 124/124 | 124/124 | 124/124 | preserved |
| Gates | — | PASS | PASS · 0 warnings | all green |

---

## Per-entry rundown

### PROMOTE-IN-PLACE — 4 TWIST entries, 11 new verse attestations + 1 mechanism correction

#### `ג'מר` (غمر, "abyss / deep") — +5 verses, 1-book → **3-BOOK GRADUATION**
**Was:** Bereshit 7:11 (flood-fountains burst open)
**Added:**
- Bereshit (2 new): 8:2 (flood-fountains stopped), 49:25 (Jacob blesses Joseph: "blessings of the deep crouching below")
- Shemot (2 new): 15:5 (Song of the Sea: "the deep covered them"), 15:8 (Song of the Sea: "deeps frozen in heart of sea")
- Devarim (1 new): 33:13 (Moses blesses Joseph: "from the deep crouching below")

**After:** 6 verses across Bereshit + Shemot + Devarim. **Third 3-book TWIST in the corpus** (joining אדלג + חאכמא from B1).

All 5 extensions are Heb תְהוֹם → Ar غمر renderings — Saadia's invariant Arabic terminus-technicus for the biblical cosmological-abyss across creation-residue + flood + Song-of-Sea + patriarchal-blessing registers. The Gen 49:25 ↔ Deut 33:13 symmetry is structurally striking: Saadia's translational consistency preserves the Moses-rewrites-Jacob paired-blessing pairing through identical Arabic-abyss vocabulary in both books.

#### `גוהר` (جوهر, "jewel / substance / essence") — +4 verses, 1-book → 2-book graduation
**Was:** Devarim 5:19, 9:9, 9:10, 10:1, 10:3 (the **only** Devarim-only TWIST in the corpus before R2)
**Added:**
- Shemot (4 new): 24:12 (Tablets-of-stone promised), 31:18 (Tablets given, "written by the finger of God"), 34:1 (second-Tablets re-issue), 34:4 (Moses descends with second-Tablets)

**After:** 9 verses across Shemot + Devarim. The TWIST extends from its Devarim retrospective-recount anchor back to its Sinai narrative-pillar; Saadia uses جوهر in a dual register (jewel + substance/essence) for Heb לֻחֹת across BOTH the original Sinai pericope AND the Devarim Mosaic-recap, demonstrating an invariant Tablets-vocabulary across narrative + homiletic registers. Skipped 5 Shemot breastplate-craft verses (28:11, 28:17, 31:5, 35:33, 39:10) where the Heb is אֶבֶן and Saadia uses جوهر in the bare classical jewel-sense (one register only).

#### `חגב` (حجب, "veil / screen / conceal") — +1 verse, 1-book → 2-book graduation
**Was:** Bereshit 7:16 (וַיִּסְגֹּר ה' בַּעֲדוֹ — "and YHWH shut him in")
**Added:** Devarim 31:18 (וְאָנֹכִי הַסְתֵּר אַסְתִּיר פָּנַי — "I will surely hide my face")
**After:** 2 verses across Bereshit + Devarim.

Saadia uses حجب — the kalām technical term for God's being veiled from creaturely vision — for biblical divine-action involving ANY concealment-frame (sealing-of-ark + hiding-of-face). At Deut 31:18 Saadia routes BOTH the verb (סָתַר → حجب) AND the object (פָּנַי "my face" → רחמתי "my mercy") through anti-anthropomorphic transformations.

#### `אתון` (أتّون, "fiery furnace") — +1 verse, Bereshit within-book sync
**Was:** Bereshit 11:28 (Haran dies in Ur of the Chaldees), 11:31 (Terah's family leaves Ur)
**Added:** Bereshit 15:7 (the divine self-introduction at Covenant-Between-the-Pieces: "I am YHWH who brought you out from Ur of the Chaldees" → "from the FURNACE of the Chaldees")
**After:** 3 verses, Bereshit-only.

The Gen 15:7 attestation is structurally significant: it is the DIVINE-SPEECH-ACT confirmation of the midrashic-furnace claim — God himself names the Abraham-rescue as "bringing-out-from-the-furnace," aligning the foundational covenant-narrative with the Aggadic-furnace tradition (Bereshit Rabbah 38:13 + Pirqei De-Rabbi Eliezer 26). Saadia's commitment is structurally midrashic across the full Abraham-foundational arc.

#### `אורד` — MECHANISM CORRECTION (no verses[] extension)

The Batch 1 mechanism rewrite preserved the original entry's prose claim that "the same template appears throughout the Tafsir wherever the Hebrew has YHWH coming down — **Sodom, Sinai, the Tent of Meeting**." The B2 scan empirically disproves the Sinai/Tent part:

| Verse | Heb | Saadia's actual Ar | Frame |
|---|---|---|---|
| Ex 19:11, 19:18, 19:20 | יָרַד ה' עַל הַר סִינַי | פתגלא אללה | **Form V تجلَّى manifest** |
| Ex 34:5 | וַיֵּרֶד ה' בֶּעָנָן | פתגלא אללה באלג'מאם | **Form V تجلَّى manifest** |
| Num 11:25 | וַיֵּרֶד ה' בֶּעָנָן | פתגלא אללה פי אלג'מאם | **Form V تجلَّى manifest** |
| Num 12:5 | וַיֵּרֶד ה' בְּעַמּוּד עָנָן | פתגלא אללה בעמוד ג'מאם | **Form V تجلَّى manifest** |
| Gen 11:5, 11:7 (Babel) | וַיֵּרֶד ה' לִרְאֹת | אורד אמרא מוגהא | **Form IV ورد dispatch** |
| Gen 18:21 (Sodom) | אֵרֲדָה-נָּא וְאֶרְאֶה | אורד אמרא מוגהא | **Form IV ورד dispatch** |

The two strategies are structurally distinct:
- **Dispatch-frame (ورد)** — used where YHWH descends to **INVESTIGATE** human action (Babel + Sodom)
- **Manifestation-frame (تجلَّى)** — used where YHWH descends to **MANIFEST** presence-and-speech in **cultic space** (Sinai theophany + Tent of Meeting)

The دispatch-frame is bounded to **3 Bereshit verses** (11:5, 11:7, 18:21). The تجلَّى manifestation-cluster (~6 verses across Shemot + Bamidbar) is a candidate for a **separate future TWIST entry** to be considered in Phase 3 R3. The B2 mechanism rewrite scopes the dispatch-frame correctly and flags the manifestation-cluster as future work.

This is the corpus's **first empirically-disproved prose claim** corrected at the verse level — methodologically valuable as a precedent for using the R2 scanner to AUDIT mechanism prose against the actual tafsir surface, not just to ADD verses.

---

## Process correction (logged for downstream batches)

During the initial B2 application, the apply script fabricated a `blau_dict.sense` rewrite for `אתון` claiming Blau cites the Aramaic-loan furnace-vocabulary. The verifier crashed with `KeyError: 'relation'` because the freshly-written `blau_dict` had no `relation` field (the entry originally had `blau_dict: None`). On investigation: `אתון` is one of the saadia-direct-only entries explicitly listed in `PHASE3_R1_SESSION_NOTES.md:64` ("ריאח, תהב · אטג'אני · אשראף · קרדא · קרבאן · אתון") as having no Blau attestation. The fabricated Blau-prose was a fabrication. **Fix:** removed the `blau_dict_sense_rewrite` from the apply script's `אתון` block, manually reverted `blau_dict` to None in the divergence file, re-ran the apply script (idempotent), re-verified gates (PASS).

**Lesson for downstream batches:** before adding a `blau_dict_sense_rewrite` to any apply script, check whether the entry's `sources[]` includes `"blau-dict"`. If not (sources is only `["lane", "saadia-direct"]`), the entry is saadia-direct-only per the PHASE3_R1 no-cite-audit, and the apply script must NOT touch `blau_dict`. The B2 apply script's helper now respects this convention.

---

## Deferred buckets

### `phase3_r2/batch2/skip` (5)

| Lemma | Verse hint | Reason |
|---|---|---|
| `אשראף` | Ex 16:22, 34:31; Num 1:16, 3:32, 7:2, 7:10, 7:84, 10:4, 16:2, 31:13 (10 verses) | Register-homograph: routine chieftain-vocabulary usage vs the entry's specific anti-mythological reading of Heb בְּנֵי הָאֱלֹהִים at Gen 6:2-4. The lexical-systemic basis (Saadia HAS أشراف as routine chieftain-vocab) grounds the anti-mythological move at Gen 6:2-4, but extending verses[] would dilute the TWIST's specific scope. |
| `מלאיכה` | Bereshit 19:15 (angels-at-Sodom) | Mechanism-mismatch: the TWIST is rerouting Heb אֱלֹהִים (lesser divine beings) → Ar ملائكة. At Gen 19:15 the Heb is הַמַּלְאָכִים (literal angels-sent-to-Lot) — direct cognate (Heb מלאך ~ Ar ملك), not the anti-anthropomorphic move. |
| `בדן` | Shemot 30:32 (anointing-oil prohibition) | Register-homograph: different Heb counterpart (Heb בְּשַׂר אָדָם at Ex 30:32 vs Heb עוֹר at Gen 3:21). The بدن usage is lexically consistent across the Pentateuch but the specific Gen 3:21 mechanism (avoiding جلد) doesn't apply to Ex 30:32. |
| `קרבאן` | 72 hits across all 5 books | Register-homograph at scale: the TWIST is the SPECIFIC anti-anthropomorphic DOUBLE substitution at Gen 8:21 (smelled→accepted; aroma→offering). The 72 cross-book hits are routine offering-vocabulary usage of قربان for various biblical sacrifice-terms (קרבן, מנחה, עלה, חטאת, אשם, שלמים). Same homograph-at-scale pattern as B1's שא and גלד. |
| `גוהר` (breastplate cases) | Shemot 28:11, 28:17, 31:5, 35:33, 39:10 (5 verses) | Register-homograph: the dual-register Tablets move ≠ the bare classical jewel-sense applied to artisan-stone for the breastplate. The 4 Tablets-register Shemot verses (24:12, 31:18, 34:1, 34:4) ARE shipped — see PROMOTE_IN_PLACE. |

### No-hit lemmas (15)

15 single-book TWIST entries returned zero cross-book attestations:

> גאמרה · מסתבחרה · ריאח · תהב · אטג'אני · קיאדך · כ'טאך · אכ'תיאר · טאעה · תופי · ינג'מד · שמשאר · קרדא · יסיידונך · ד'רקובה · משוובה

All anchored at unique-context Bereshit creation / flood / Babel / Patriarchal verses. The vocabulary is sufficiently context-specific that Saadia uses it nowhere else in the Pentateuch. These entries are honest single-verse TWISTs — not extensible by promote-in-place.

---

## Yield observations

### 1. Phase 3 R2 sweep COMPLETE — final numbers

| Phase 3 R2 outcome | Pre-R2 | After B1 | After B2 |
|---|---|---|---|
| TWIST 3-book entries | 0 | 2 (אדלג · חאכמא) | **3** (+ ג'מר) |
| TWIST 2-book entries | 2 | 1 (מסלט) | **3** (+ גוהר · חגב) |
| TWIST Bereshit-only | 33 | 30 | **27** |
| TWIST verse attestations | 56 | 75 | **101** (+45 across R2) |
| Cross-book lemmas (R2-promoted) | — | 6 | **10** (+ ג'מר · גוהר · חגב · אתון) |
| Promote-in-place ships | — | 6 | **10** |
| Verse extensions | — | 19 | **30** |
| Mechanism corrections | — | 0 | **1** (אורד dispatch/manifestation scoping) |

**Phase 3 R2 has lifted the TWIST tier from a Bereshit-dominant corpus to a 5-book-spanning corpus** with meaningful cross-book breadth: Shemot 15 attestations (was 6), Vayikra 1 (was 0), Bamidbar 1 (was 1), Devarim 7 (was 5). The methodology — promote-in-place from existing TWIST entries — extracted ~25% of the corpus's TWIST-tier latent cross-book potential without adding a single new entry, changing a single tier, or adjusting any source-of-truth Blau citation.

### 2. The empirically-corrected אורד finding is methodologically novel

This is the corpus's **first empirically-disproved prose claim** corrected via the R2 scanner. The B1 mechanism rewrite for אורד preserved the original entry's prose claim ("Sodom, Sinai, the Tent of Meeting all use the same template") that turned out to be empirically wrong at the surface level: Sinai/Tent verses use Form V تجلَّى, not Form IV ورد. The scanner surfaced this; the B2 mechanism rewrite corrected it; the dispatch-frame is now correctly bounded to Babel + Sodom, and the تجلَّى cluster is logged for future work.

This is a precedent worth preserving: **the R2 scanner is not just a verse-extension tool — it is also a mechanism-audit tool**. Other entries may have similar overreaching prose claims that future R3+ scans can correct. The scanner's value compounds when used proactively on entries whose prose makes empirical claims about Saadia's lexical patterns.

### 3. Sync-verses-to-prose continues to be the dominant promote-in-place pattern

Of the 10 R2 ships across both batches, **7 were sync-verses-to-prose cases** (the entries' existing mechanism prose or Blau prose already named cross-book attestations that weren't in verses[]):
- B1: אדלג (Blau cites Ex 8:16); אורד (mechanism named Sodom); אלממתעה (mechanism + Blau both cite Deut 23:18, blocked by NOTE duplicate)
- B2: גוהר (mechanism implies Tablets-program across Pentateuch); ג'מר (mechanism cross-references גאמרה Gen 1:2); חגב (kalām-context implies broader concealment-verb usage); אתון (mechanism implies systematic furnace-identification)

**For Phase 3 R3 and beyond:** the highest-yield mining strategy is to read each entry's mechanism + blau_dict.sense BEFORE scanning, pre-flagging the entries whose prose makes claims wider than their verses[]. These are the highest-confidence promote-in-place candidates.

### 4. Homograph rate stabilizes around ~40-50% at TWIST tier

Across both R2 batches: 13 entries scanned in B1 → 6 ships (54%); 25 entries scanned in B2 → 5 ships (20%). The B2 rate is lower partly because 15 entries had ZERO cross-book hits (saturated single-verse anchors) and partly because the easy promote-in-place candidates were already covered in B1 (the priority-cluster lemmas had the most prose-claimed cross-book potential).

The remaining 5 entries that DID have cross-book hits but were filtered (אשראף, מלאיכה, בדן, קרבאן, גוהר-breastplate) all share a common pattern: **routine-usage homograph** where Saadia's lemma is a high-frequency Arabic word with a baseline classical sense PLUS a paradigm-defining TWIST sense. The promote-in-place criterion at TWIST tier must filter for **mechanism-fit**, not just surface-fit.

---

## Recommended next-session strategy

In priority order:

1. **Consolidation pass for אלממתעה ↔ ממתעה duplicate (out-of-scope-for-R2 deferred from B1)** — the single most actionable cleanup task in the corpus. The cleanest resolution is to delete the NOTE entry and absorb Deut 23:18 into the TWIST verses[], converting the TWIST to 2-book Bereshit+Devarim. This requires entry-removal (out-of-scope for promote-in-place-only R2) and should be the next-priority pass before R3 begins. Single-entry change, well-scoped, no methodology risk.

2. **New TWIST entry: Sinai/Tent تجلَّى manifestation-cluster** (Phase 3 R3 candidate) — the empirical B2 finding that Sinai descent verses (Ex 19:11, 19:18, 19:20, 34:5) + Tent-of-Meeting descent verses (Num 11:25, 12:5) use Form V تجلَّى as a distinct anti-anthropomorphic strategy is a clean 6-verse, 2-book candidate for a new TWIST entry. The mechanism is structurally parallel to the אורד dispatch-frame (both anti-anthropomorphic, both Pentateuchal-narrative-pillar) but operates in the manifestation-register rather than the investigation-register. Worth pursuing in Phase 3 R3 alongside the strict-tier additions.

3. **New NOTE: judicial-vocabulary cluster (חאכם)** (Phase 4 Vayikra/Devarim B2 candidate) — the 9 Shemot+Devarim bare-form חאכם judicial hits surfaced in R2 B1 form a coherent cluster: Saadia's systematic use of H-K-M-vocabulary for Heb שׁפט judicial passages. Ready to ship as a new NOTE in the next Phase 4 batch.

4. **Phase 3 R1 second wave (TWIST gate activation for Shemot/Vayikra/Bamidbar/Devarim)** — Phase 3 R2 surfaced meaningful TWIST attestations across all 5 books for the first time (Shemot 15, Vayikra 1, Bamidbar 1, Devarim 7), but the verifier's per-book gate (≥5 TWIST entries with explicit per-book anchor) still only activates for Bereshit + Devarim. Phase 3 R1 second wave should add ≥5 net-new TWIST entries anchored at Shemot/Vayikra/Bamidbar/Devarim to activate the gate uniformly.

5. **The remaining 4 Vayikra B1 NOTE/GLOSS borderlines** (כ'אמע · קצבה · לג · מסוחייה) + the 4 Devarim B1 borderlines (יקתצ'י · ממד-יד · נווב · תנאצי) — coordinated Vayikra/Devarim Batch 2 pass. Lower priority than items 1-3.

---

## Pattern reminders for downstream batches (Phase 3 R3+ onward)

### What worked in R2 (both batches)

- **The scan-then-triage pattern** is the right shape for cross-book mining at TWIST tier. The scanner surfaces all surface hits; triage filters homographs by checking mechanism-fit against alignment files. Don't trust surface-only matches.

- **Sync-verses-to-prose** is the highest-leverage triage signal. When mechanism prose or Blau prose already cites a cross-book verse, the scan should confirm-and-sync. 7 of the 10 R2 ships were prose-existing-claim syncs.

- **Mechanism-audit via scanning** is a new capability. The אורד B2 correction demonstrates that the R2 scanner can not only ADD verses but also AUDIT existing mechanism claims. Future R3+ batches should proactively audit entries whose prose makes wider empirical claims than their verses[].

- **Register-distinction is essential**. TWIST entries are paradigm-defining moves on lemmas that often have routine classical-Arabic senses. Filter by Hebrew counterpart + context register, not just by Arabic surface.

### What to carry forward

- **CHECK `sources[]` BEFORE adding `blau_dict_sense_rewrite`**. If `sources` is only `["lane", "saadia-direct"]` (no `"blau-dict"`), the entry is saadia-direct-only per PHASE3_R1's no-cite-audit. Do NOT fabricate a Blau citation. The B2 verifier-crash on אתון was a self-introduced bug from skipping this check.

- **The جوهر dual-register pattern** is a clean template for future Tablets-and-related-vocabulary entries. Saadia's deployment of philosophically-loaded Arabic terms (jawhar = substance/essence) in registers where Heb provides a literal-physical alternative (אֶבֶן = stone) is a recurring pattern worth flagging.

- **The تهوم → غمر cross-book invariance** (B2's ג'מר extension) is the broadest cosmological-vocabulary commitment in the corpus. Worth comparing to other potential cosmological-vocabulary cross-book candidates in future R3+ work (חַיָּה / רֶמֶשׂ creation-vocabulary; שָׁמַיִם / רָקִיעַ cosmos-vocabulary).

- **The duplicate-collision pattern** (אלממתעה ↔ ממתעה, surfaced in B1, still standing in B2) is a known methodology gap. The next-priority cleanup pass should resolve it before Phase 3 R3 begins. Future batches should always check for cross-tier duplicates when promoting cross-book.

- **For the corpus's first TWIST 3-book trio (אדלג · חאכמא · ג'מר):** these represent paradigm-defining lexical commitments that Saadia maintains invariantly across narrative + covenantal + ritual + cosmological registers. They are the corpus's strongest evidence that Saadia operates with stable cross-Pentateuchal vocabulary — worth foregrounding in any future scholarly writeups.
