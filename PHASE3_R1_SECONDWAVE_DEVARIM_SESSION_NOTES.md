# Phase 3 R1 Second Wave — Devarim batch (session notes)

**Date:** 2026-06-02
**Script:** `scripts/apply_phase3_r1_devarim.py`
**Goal:** Bring Devarim to ≥5 first-verse twists so its per-book gate activates
and clears. This is the **final** book of the R1 second wave.

## Snapshot

| metric | before (post-Bamidbar) | after |
|---|---|---|
| total entries | 139 | 140 |
| twist / note / gloss | 52 / 37 / 50 | 56 / 34 / 50 |
| **Devarim first-verse twists** | **1** | **5** |
| verifier | PASS, 0 warnings | PASS, 0 warnings |
| `npm run build` | clean | clean |

Devarim twist mix after: **total=5 · direct=4 · adjacent=0 · no-citation=1**
→ direct 80% (≥45% ✓) · backed 80% (≥70% ✓) · no-cite 20% (≤30% ✓).

Delta = +1 net-new twist + 3 promotions (note→twist). Net tier movement:
twist +4, note −3, gloss 0.

## Per-entry rundown

### Existing twist (unchanged)

- **גוהר** (جوهر) — Deut 5:19 (+ Shemot) · **direct**
  Tablets of the Covenant as לוחי אלגוהר 'Tablets of substance/jewel' —
  midrashic + falsafa dual-register. Already present; no change.

### Promotions (note → twist, Blau backing inherited, all first=Devarim, all direct)

- **אקרץ'** (قرض, ق-ر-ض) — Deut 2:21, 7:17, 9:3, 11:23, 12:2 · **direct**
  Heb הוֹרִישׁ 'to dispossess/drive out' → Ar قرض 'to exterminate, cut off'.
  Conquest reframed from DISPLACEMENT (nations driven out, may survive elsewhere)
  to EXTERMINATION (cut off entirely) — a re-theologizing of the whole conquest
  ethic. Blau (s.v. قرض) documents the systematic rendering.

- **תכ'רסתם** (تخرّس, خ-ر-س) — Deut 1:27 · **direct**
  Heb רגן 'to murmur/complain' (active complaint-speech) → Ar Form V تخرّس
  'to be struck dumb / silenced'. A semantic-polarity **inversion**: vocal
  rebellion → faithless speechlessness. Blau (s.v. خرس) + al-Fāsī Jāmiʿ 1:103
  (both Form II 'silence' / Form V 'be silenced').

- **זאיל** (زائل, ز-ي-ل) — Deut 21:18 · **direct**
  Heb סוֹרֵר '(stubborn-)rebellious son' (political insubordination) → Ar زائל
  'one who DEVIATES from the right' (زائل عن الصواب/الطاعة). The wayward-son
  institution rationalized: rebellion-against-authority → moral-epistemological
  deviation. Blau (s.v. زيل) cites Deut 21:18 (סורר → זאיל).

### Net-new twist — no-citation (1)

- **אעלם** (اعلم, ع-ل-م) — Deut 6:4 · **no-citation**
  The Shema: Heb שְׁמַע 'Hear, O Israel' → Ar אעלם 'Know, O Israel'. Judaism's
  central confession recast from audition to **cognition** — divine unity as an
  object of rational knowledge (tawḥīd per Emunot ve-Deot), reinforced by the
  inserted אן 'that' (propositional content-clause). Not an Arabic-internal
  lexical shift (اعلم = 'know' is classical; the natural calque of שמע is اسمع),
  so shipped `[lane, saadia-direct]`, no blau_dict. Logged in
  `no_cite_audit/phase3_r1_no_blau`.

## Deferred buckets touched

- `_blau_saadia_deferred.json#/no_cite_audit/phase3_r1_no_blau` += 1 (אעלם).
- No `phase3_r1_consumed` additions: the 3 promotions reuse already-consumed
  Blau ids from the Phase 4 Devarim Batch 1 NOTE work; only the tier + mechanism
  changed.

## Deliberately NOT promoted / left alone (honesty over count)

- **יסיב** (שמט→سيب) — kept as **note**. The Sabbatical/shemittah field is
  rendered via the pastoral-release Arabic root, but the *meaning* (release) is
  preserved — an institutional-vocabulary calque, not a paradigm reframe.
- **אלממתעה** (Deut 23:18) — already a twist, but Bereshit-anchored
  (verses[0] = Bereshit 38:21), so it counts for Bereshit, not Devarim. Untouched.

## Yield observations

- Deuteronomy's richest twist vein is the **rationalist-philosophical / anti-
  anthropomorphic** register of the Mosaic oration — exactly as predicted. The
  high-value seam, however, sits almost entirely **outside Blau**: the candidates
  file has no entries for the theological roots (علم, جهل, كفر, شطن, خالق,
  عمد/معتمد), so the strongest net-new candidates are all no-cite. The ≤30%
  no-cite budget allowed exactly one (אעלם), which is why the batch leaned on
  3 promotions of already-Blau-backed NOTEs rather than net-new authoring.
- **Rich no-cite reserve for a future pass** (all corpus-verified, no Blau lemma):
  בליעל→גהל 'ignorance' (Deut 15:9, sin as cognitive defect); אֵשׁ אֹכְלָה /
  אֵל קַנָּא → עקאב...אלטאיק אלמעאקב (4:24, God's *punishment* is fire; "the
  Powerful Punisher" for "jealous God"); צוּר → מעתמד 'the Reliance' (the Rock
  de-reified, 32:31/37); פָּנִים בְּפָנִים → שפאהא 'orally' (5:4, 34:10, face
  removed); עֹצֶם יָדִי → עצם קדרתי 'magnitude of my power' (8:17); circumcise-
  the-heart → אזילו ג'ש / ישרח צדרך (10:16, 30:6); שֵׁדִים → אלשיאטין (32:17);
  חָלַק...אֹתָם → בת' נורהא 'dispersed their light' (4:19, astral cult
  demythologized). These would need Blau-backed companions to stay under the
  no-cite bar if shipped as twists.

## Wave status — COMPLETE

All five Torah books now have **active + passing** per-book gates:

| book | twists | direct | adjacent | no-cite | direct% | backed% | no-cite% |
|---|---|---|---|---|---|---|---|
| Bereshit | 35 | 20 | 6 | 7 (+2 diff-sense) | 57% | 74% | 20% |
| Shemot | 6 | 4 | 1 | 1 | 67% | 83% | 17% |
| Vayikra | 5 | 3 | 1 | 1 | 60% | 80% | 20% |
| Bamidbar | 5 | 4 | 0 | 1 | 80% | 80% | 20% |
| Devarim | 5 | 4 | 0 | 1 | 80% | 80% | 20% |

Corpus: **140 entries — 56 twist / 34 note / 50 gloss.** Verifier PASS, 0 warnings.

## Next (deferred for future passes)

- Devarim no-cite reserve above (pair with Blau-backed twists to stay ≤30%).
- Carried from Vayikra notes: re-mine Vayikra כ'לף via promote-in-place; deferred
  Vayikra identification-twists (Azazel→Mount Azaz; אני יהוה→"God the Punisher";
  נפש בדם); optional reader back-pointer אורד↔תגלא.
- Bamidbar no-cite reserve (see Bamidbar notes): Balaam divine-name epithets
  (אלטאיק/אלכאפי, Num 23-24), אלנור for הרוח (11:25), תאיבא at the bronze
  serpent (21:8-9).
