# Phase 3 R1 Second Wave — Bamidbar batch (session notes)

**Date:** 2026-06-02
**Script:** `scripts/apply_phase3_r1_bamidbar.py`
**Goal:** Activate + clear the verifier's per-book quality gate for Bamidbar
(Numbers) by bringing it to ≥5 first-verse twist entries.

## Snapshot

| metric | before | after |
|---|---|---|
| total entries | 135 | 139 |
| twist / note / gloss | 47 / 38 / 50 | 52 / 37 / 50 |
| **Bamidbar first-verse twists** | **0** | **5** |
| verifier | PASS, 0 warnings | PASS, 0 warnings |
| `npm run build` | — | clean |

Bamidbar twist mix after: **total=5 · direct=4 · adjacent=0 · no-citation=1**
→ direct 80% (≥45% ✓) · backed 80% (≥70% ✓) · no-cite 20% (≤30% ✓).

Delta = +4 net-new twists + 1 promotion (note→twist). Net tier movement:
twist +5, note −1 (the ראם promotion), gloss 0.

## Per-entry rundown

### Promotion (note → twist), Blau backing inherited

- **ראם** (روم, ر-و-م) — Num 13:21, 13:32, 15:39 · **direct**
  Heb תור 'to scout/explore' (physical traverse) → Ar روم 'to seek-after,
  pursue (volitionally)'. Reframes biblical exploration from the physical plane
  to the plane of will; sharpest at Num 15:39, where "do not go-roving after
  your heart and eyes" becomes "do not PURSUE after your heart and eyes" —
  internalizing the commandment from outward motion to inner intention.
  Mechanism deepened to twist depth; verses/variants/sources/blau_dict intact.

### Net-new twists — Blau-direct (3)

- **אלת'רא** (الثرى, ث-ر-ي) — Num 16:30, 16:33 · **direct**
  Heb שאול 'Sheol/underworld' → الثرى 'the (damp) earth'. Demythologizes
  biblical cosmology: Korah's company sink into ordinary ground, not a chthonic
  realm. Blau (s.v. ثرى, #14403): post-classical 'underworld/שאול', Saadia
  renders שאול with it **regularly (בקביעות)** — Dozy, al-Fāsī, Ibn Janāḥ.

- **דראדר** (درادر, د-ر-د-ر) — Num 21:14 · **direct**
  Obscure archaic toponym את והב בסופה → 'the breakers of al-Qulzum (the Red
  Sea)'. Dissolves a fossilized war-poetry place-name into maritime realia.
  Blau (s.v. دردور 'breaker', pl. درادر, #15439) cites the **exact verse**.

- **מחצ'ר** (محضر, ح-ض-ر) — Num 6:18, 16:2 · **direct**
  Cultic מוֹעֵד / אֹהֶל מוֹעֵד (divine-appointment / Tent of Meeting) → محضر
  'assembly'. De-sacralizes the sacred-rendezvous term into a civic gathering
  (محضر also = tribunal/court). Blau (s.v. محضر, #17364) cites **Num 16:2**
  (דעאת מחצ'ר 'מזמני העדה') + the خباء المحضر = "tent of meeting = really tent
  of assembly" rendering.

### Net-new twist — no-citation (1)

- **קצד** (قصد, ق-ص-د) — Num 6:26 · **no-citation**
  Anthropomorphic יִשָּׂא יְהוָה פָּנָיו אֵלֶיךָ 'lift His face' → ויקבל בקצדה
  אליך 'receive (you) with His intent'. Anti-anthropomorphic EXEGETICAL
  substitution, not an Arabic-internal lexical shift (قصد = 'intent' is
  classical), so shipped `[lane, saadia-direct]`, no blau_dict. Selectivity is
  the proof of design: Num 6:25 retains a face-word (ויצ'י וגהה), so 6:26 is a
  deliberate local anti-anthropomorphism. Logged in
  `no_cite_audit/phase3_r1_no_blau`. Consistent with the corpus's other no-cite
  identification-twists (אשראף, קרדא, שיאטין).

## Deferred buckets touched

- `_blau_saadia_deferred.json#/phase3_r1_consumed` += 3 (blau_ids 14403, 15439,
  17364; `consumed_on: 2026-06-02`).
- `_blau_saadia_deferred.json#/no_cite_audit/phase3_r1_no_blau` += 1 (קצד).

## Deliberately NOT promoted (honesty over count)

The other three Bamidbar direct-NOTEs were judged semantic, not paradigm-shifting:
- **מגרד** (חלוץ→مجرد) — frame inversion (equipped↔stripped) but the *referent*
  is identical (the vanguard fighter); kept as note.
- **גבן** (תניאון→جبن) — semantic narrowing (dissuade→make-cowardly); kept as note.
- **מחפצה** (משמרת→محفظة) — coinage-matching of an institutional noun; kept as note.

## Yield observations

- Numbers' richest twist vein is **demythologizing**: Saadia systematically
  flattens loaded cosmic/geographic vocabulary (Sheol→earth, opaque toponym→Red
  Sea, sacred-appointment→assembly). Three of four net-new twists came from this
  seam, all Blau-direct.
- The Balaam-oracle anti-anthropomorphic divine-name epithets (אלטאיק 'the
  Powerful' / אלכאפי 'the Sufficient' for אֵל / שַׁדַּי, Num 23-24) and אלנור
  'light' for הרוח (Num 11:25) and תאיבא 'repentant' inserted at the bronze
  serpent (Num 21:8-9) are all corpus-verified but **have no Blau lemma** — a
  rich no-cite reserve for a future pass (would need the ≤30% budget). Logged
  here, not shipped, to keep Bamidbar's no-cite at 1/5.

## Next

→ Batch B (Devarim): `scripts/apply_phase3_r1_devarim.py`. After Devarim clears,
the R1 second wave is complete — all five Torah books with active+passing gates.
