# Blau × Saadia: tier calibration for Tafsir Twist feature

Calibration study of how many Blau dictionary entries citing Saadia's Tafsir clear different editorial bars for inclusion in the Tafsir Twist surface. Sits alongside `PHASE3_ROUND1_PROMPT.md`.

## Corpus baseline

- **Blau total entries:** 6,736
- **Citing Saadia's Tafsir:** **1,596** (23.7% of Blau)
- **Source:** `~/Tools/arabic-lexicon/lex.sqlite`, table `blau`, filter `body LIKE '%רס״ג%' OR body LIKE '%סעדיה%'`
- **Currently shipped Tafsir Twists:** 32 (31 Bereshit + 1 Devarim) at `data/tafsir-divergence.json`

## Tier definitions

| Tier | Bar |
|---|---|
| **STRICT** | Paradigm twist. Saadia's Arabic carries a sense classical Arabic does not: anti-anthropomorphic, philosophical/Mu'tazilite, midrashic identification, theological insertion, semantic loanshift / coinage. |
| **MEDIUM** | Semantic surprise. Calque, register shift, technical-term extension, grammatical-form methodology — "why THIS Arabic word." Diverges from straightforward equivalence but doesn't reframe theology. |
| **EXPANSIVE** | Non-obvious lexical pairing. Heb→Ar mapping a Hebrew reader couldn't predict (non-cognate, false friend, divergent semantic field). Standard Arabic sense but pedagogically useful for JA acquisition. |
| **BORDERLINE** | Saadia cited but body context doesn't clarify the semantic point. Leans EXPANSIVE but unconfirmed. |
| **SKIP** | Trivial cognate (אב→أب), bare textual-variant note, non-Tafsir Saadia citation, redundant attestation. |

## Calibration walks

### n=50 random sample
- STRICT: 0 (0%)
- MEDIUM: 10 (20%)
- EXPANSIVE: 18 (36%)
- SKIP: 22 (44%)

The 44% SKIP rate later proved to be a methodology artifact — the agent worked from ~80–180 char body snippets and defaulted uncertain cases to SKIP.

### n=200 random sample (full-body context)
- STRICT: 2 (1.0%) → ~16 / 1,596
- MEDIUM: 6 (3.0%) → ~48
- EXPANSIVE: 101 (50.5%) → ~807
- BORDERLINE: 87 (43.5%) → ~694
- SKIP: 4 (2.0%) → ~32

**Combined STRICT + MEDIUM + EXPANSIVE: 54.5% → ~870 entries**

**Upper bound including BORDERLINE: 98% → ~1,564 entries**

## Calibrated answers

| Bar | Best estimate | Range | % of 1,596 |
|---|---|---|---|
| Strict only | **~16–80** | 16 (random hit rate) to 80 (current 32 shipped + R1 ~30 + ceiling) | 1–5% |
| Strict + Medium | **~65** | 50–100 | 3–6% |
| Strict + Medium + Expansive | **~870** | 800–950 | 50–60% |
| All non-SKIP (incl. BORDERLINE) | **~1,560** | 1,400–1,564 | 88–98% |

The **expansive bar** the project picked yields **~870 confident inclusions, up to ~1,560 if BORDERLINE entries are upgraded after review.**

### Reconciling STRICT count

Random sample suggests STRICT prevalence is ~1% → ~16 entries in the full 1,596. But the project has already shipped 32 STRICT entries, and PHASE3_ROUND1_PROMPT.md targets ~30 more (~60 total expected by end of R1).

This isn't a contradiction:
- The 32 shipped were found via **verse-first** curation (walk Bereshit verse by verse, ask "what's the divergence?"), not Blau-first random sampling.
- PHASE3_ROUND1_PROMPT.md's Blau-first approach starts from the 1,596 candidates and filters — the random sample suggests it'll yield ~16 if applied purely randomly, but in practice the curator filters favorably and recovers ~30–80 (the prompt's stated target).
- The mature ceiling is probably **~60–100 STRICT entries Torah-wide.** Past that, additional curation re-finds known cases.

## Tier exemplars

### STRICT — from existing 32 shipped (random walks rarely surface these)

- **אכ'תיאר** (Ber 4:7) "by free choice" — Mu'tazilite libertarian voluntarism inserted into God's address to Cain. Classical Arabic *ikhtiyār* = "choice"; Saadia smuggles in the technical philosophical sense.
- **מסלט** (Ber 1:26–27) "ruling" — anti-anthropomorphic gloss on בְּצַלְמֵנוּ. The image of God is dominion, not visual likeness.
- **גלד** (Ber 1:6) "hardness" stretched to render רקיע. Semantic loanshift classical Arabic does not have.

### STRICT — from n=200 random walk

- **نوراني** (*nūrānī*, "luminous") — Saadia deliberately avoids this post-classical philosophical adjective, preferring biblical references (sun, moon). The avoidance itself is theologically motivated.
- **نير** (*nīr*, "light-bearer") — Explicit anti-anthropomorphic avoidance noted in Blau ("אין רס״ג משתמש").

### MEDIUM — from n=200

- **نفس** (*nafs*, "soul") — non-classical usage pattern with theological weight in Saadia's Tafsir
- **جماز** (*jimāz*, "contortion") — semantic divergence from classical attestation
- **جامد** (*jāmid*, "solid") — technical extension of classical sense
- **جبروة** (*jabrūwa*) → גבורה (from n=50) — divine-attribute extension into theological vocabulary
- **جسس** (*jassa*) → גישש (from n=50) — Form-I choice mirrors Hebrew rather than picking idiomatic Form-V
- **بشريون** (*bashariyyūn*) (from n=50) — Saadia extends "human" beyond strict human reference

### EXPANSIVE — from n=200

- **عطب** (*ʿaṭb*, "damage") — non-cognate dialectal pairing
- **لحم** (*laḥama*, "to fight") — standard Arabic applied to biblical combat/anatomy contexts
- **حوز** (*ḥāza*, "to seize") — non-obvious semantic field pairing
- **ناهض** (*nāhiḍ*, "wise") — register/dialect variation in character description

### EXPANSIVE — from n=50

- **وجدان** (*wijdān*) → מציאות / קיום "existence, being" — non-cognate ontological vocabulary
- **فريدة** (*farīda*) → "singular/unique word" — Saadia's lexicographic metalanguage
- **سرح** (*saraḥa*) → pasture/graze — pastoral semantic field
- **ضرغام** (*ḍirghām*) → אריה — high-register synonym for "lion"

### SKIP — what the bar should exclude

- Bare textual-variant notes ("Dirinburg reads X, MS Y reads Z") with no semantic point
- Trivial cognates (אב→أب) — Hebrew reader gains nothing
- Non-Tafsir Saadia citations (his *Emunot ve-Deot*, biblical commentaries, etc.)
- Entries where Saadia is cited only to confirm a sense already attested elsewhere

## Semantic-field clusters within EXPANSIVE

The n=200 walk surfaced these recurring sub-domains in the EXPANSIVE tier:

- Spatial / locational (e.g. ناحية, ضلع)
- Bodily / anatomical (e.g. عراياء)
- Celestial / luminous (e.g. نوراني, نير)
- Political / legal (authority, judgment terminology)
- Textual / linguistic (writing, transmission)
- Commercial / legal (trade, debt, contracts)
- Psychological / philosophical (mind, knowledge, soul)
- Sensory / descriptive (taste, color, form)
- Agricultural / pastoral (crops, animals)

Each cluster has natural sub-feature potential: a "Saadia's pastoral vocabulary" mini-glossary, a "commercial JA" reference card, etc.

## Methodology limitations

1. **No row-by-row table.** The n=200 walk agent returned aggregate counts and exemplars only, not the full 200-row classification. To audit individual decisions, a re-run with explicit row-dump instructions would be needed.
2. **Possible double-counting in agent's analysis.** *نوراني* appears as both a STRICT exemplar (avoidance) and in the EXPANSIVE field clusters (celestial/luminous). Indicates the per-entry classifications may have boundary cases the agent handled inconsistently.
3. **BORDERLINE is large (~43.5%).** Many "Saadia cited but unclear why" cases. Whether these are usable depends on a curator's tolerance for thin attestations.
4. **Random sample is bad at STRICT.** STRICT-tier prevalence is ~1%; n=200 gives wide confidence intervals (95% CI for STRICT: roughly 0.1%–3.6%). The verse-first curation approach used by PHASE3_ROUND1_PROMPT.md remains the right strategy for the strict tier.

## Use of this calibration

- **Phase 3 Round 1** stays scoped to STRICT (~30 new entries) via the targeted curation approach already in PHASE3_ROUND1_PROMPT.md.
- **Phase 4 (proposed)** would mine MEDIUM + EXPANSIVE (~870 entries) via a lighter, scripted Blau-first pipeline. No mechanism essay per entry — just lemma, verse, Blau reference, relation type.
- **Tier schema** on `data/tafsir-divergence.json` (proposed): add `tier: 'twist' | 'note' | 'gloss'` field; route to different display registers in `app/tafsir/reader.tsx`.

See plan file: `~/.claude/plans/lets-continue-code-judeo-arabic-app-phas-vivid-pony.md`
