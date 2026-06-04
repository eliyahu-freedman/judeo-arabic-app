# Phase 3 R3 — Sinai/Tent تَجَلּَى Manifestation-Cluster TWIST · Session Notes

**Shipped:** 2026-05-30
**Apply script:** `scripts/apply_phase3_r3_tajalla.py` (new-entry, idempotent)
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json` (no-cite-audit log)
**Branch:** `advanced-library-kuzari` · working tree uncommitted per project convention

First Phase 3 R3 entry. The candidate was empirically isolated by the R2 Batch 2 `אורד` mechanism correction (which proved Saadia splits the Hebrew "descent" verb ירד into two anti-anthropomorphic frames). This session confirmed the manifestation half against the actual Saadia text and shipped it as a standalone TWIST, immediately after the אלממתעה↔ממתעה consolidation (`PHASE3_R2_CONSOLIDATION_NOTES.md`).

## Snapshot

| Metric | Before (post-consolidation) | After |
|---|---|---|
| Total entries | 123 | **124** |
| Tier distribution | 36 twist / 37 note / 50 gloss | **37 twist / 37 note / 50 gloss** |
| TWIST cross-book breakdown | 3 three-book · 4 two-book · 29 single-book | **3 three-book · 5 two-book · 29 single-book** |
| Verse attestations | — | +6 (Shemot 4 · Bamidbar 2) |
| Duplicate lemmas / double-covered verses | none | **none** |

`תגלא` is the **5th two-book TWIST** (Shemot + Bamidbar), joining מסלט · חגב · גוהר · אלממתעה.

## The new entry

#### `תגלא` (تَجَلَّى, Form V "to manifest oneself") — new TWIST, 6 verses, 2 books

- **Lemma/variants:** `תגלא` + `["יתגלא", "פתגלא"]` (covers the imperfect at Ex 19:11 and the wāw/fa-prefixed perfects; resolvability verified — every cited verse has a token resolving to lemma or variant).
- **Root:** ج-ل-و · **lemma_ar:** تجلّى · **tier:** twist.
- **Verses (read from the repo's Saadia text, not assumed):**
  | Verse | Hebrew trigger | Saadia (Form V) |
  |---|---|---|
  | Ex 19:11 | יֵרֵד יְהוָה | יתגלא אללה ... עלי גבל סיני |
  | Ex 19:18 | יָרַד עָלָיו ... בָּאֵשׁ | תגלא עליה אללה באלנאר |
  | Ex 19:20 | וַיֵּרֶד ... עַל הַר סִינַי | תגלא אללה עלי גבל סיני |
  | Ex 34:5 | וַיֵּרֶד ... בֶּעָנָן | פתגלא אללה באלג'מאם |
  | Num 11:25 | וַיֵּרֶד ... בֶּעָנָן | פתגלא אללה פי אלג'מאם |
  | Num 12:5 | וַיֵּרֶד ... בְּעַמּוּד עָנָן | פתגלא אללה בעמוד ג'מאם |
- **Mechanism:** anti-anthropomorphic substitution — the theophany counterpart to the `אורד` dispatch-frame. Saadia sorts the single Hebrew verb ירד into two theologically-typed Arabic renderings: (1) **dispatch-for-judgment** — Form IV أورد at the punitive Babel/Sodom descents (the `אורד` entry); (2) **manifestation-for-revelation** — Form V تَجَلَّى at the Sinai + Tent theophanies (this entry). The manifestation is always localized in the fire (אלנאר) / cloud (אלג'מאם) / light (אלנור), never a moving divine body. Carries a precise Islamic-register resonance: تَجَلَّى is the Qur'an's own Sinai-theophany verb (Q 7:143, فَلَمَّا تَجَلَّى رَبُّهُ لِلْجَبَلِ).
- **Sources:** `["lane", "saadia-direct"]` — **NO blau-dict** (see decision below).

## Blau no-cite decision (audit trail)

Per the PHASE3_R1 no-cite-audit rule (and the R2 B2 אתון verifier-crash precedent — never fabricate a Blau citation), the entry carries **no `blau_dict` block** and does **not** cite `blau-dict`:

- Blau's *Dictionary of Medieval Judaeo-Arabic Texts* (via `~/Tools/arabic-lexicon`, slug `blau-judeoarabic`) has **no Form V تجلّى entry**. A full-text search returns **0 hits** for every Form V surface — تجلى / تجلّى / تجل / انجلى — **0** for Form II جلّى, and **0** for the Hebrew-script JA surfaces Saadia uses (תג'לי / יתג'לי). The root appears only as **Form I**: جلو / جلا, glossed in Blau as "to reflect (light) / החזיר," "to go into exile / emigrate (גלות, جلاء)," and the classical polish/clear senses — **none** documenting the theophany-manifestation rendering of Heb ירד.
- Grounding is therefore **saadia-direct** (the six attested renderings, read from the repo corpus) + **Lane** (ج-ل-و: polish/cleanse → become clear/unveiled; Q 7:143 Sinai resonance). Logged under `_blau_saadia_deferred.json#/no_cite_audit/phase3_r3_no_blau`.

## Gates

```
python3 scripts/verify_divergence.py   →  PASS, 0 warnings (124 entries; twist 37 / note 37 / gloss 50)
                                          citation-resolvability PASS for all 6 new verses
                                          Shemot twist n=1 (< 5) → per-book quality gate exempt; no new warning
npm run build                          →  ✓ Compiled successfully
Total: 124 · tiers 37/37/50 · Dupes: none · verses covered by >1 entry: none
```

## Yield observations

1. **Two-frame theophany split confirmed from primary text.** The R2 B2 hypothesis (dispatch-أورد vs. manifestation-تَجَلَّى) is now backed by all six theophany verses read directly from the Saadia corpus — not a prose claim but verse-level evidence.
2. **No silent assumptions.** Every JA surface form in the entry was extracted from `tafsir-{book}-{ch}.json` before authoring; the imperfect form (יתגלא, Ex 19:11) differs from the perfect forms and was added as an explicit variant so the verifier resolves it.
3. **Clean saadia-direct + Lane TWIST.** Demonstrates the corpus can carry a strong TWIST without Blau when Blau genuinely lacks the lemma — the no-cite-audit discipline prevents the corpus's integrity from degrading.

## Recommended next-session strategy (remaining R2/R3 follow-ons)

1. **New NOTE for the חאכם judicial-vocabulary cluster** (9 Shemot+Devarim hits in the R2 B1 skip bucket; bare-noun "judge" register, distinct from the חאכמא circumstantial-accusative divine-speech TWIST) — Phase 4 Vayikra/Devarim Batch 2.
2. **Phase 3 R1 second wave** — add ≥5 net-new TWIST entries to each of Shemot/Vayikra/Bamidbar/Devarim to activate the verifier's per-book quality gate uniformly (Shemot now has 1 first-verse TWIST via תגלא — 4 short of the ≥5 threshold).
3. Optional: add a reader-facing back-pointer from the `אורד` entry to the new `תגלא` entry (they are the two halves of the ירד split).
