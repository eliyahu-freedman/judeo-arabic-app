# Dictionary Coverage — Batch 1 (session notes)

**Date:** 2026-06-02
**Scripts:** `scripts/apply_dict_batch1.py` (append) · data:
`data/_dict_batch1.json` (shipped) · `data/_dict_batch1_deferred.json` (parked)
**Goal:** raise hand-curated tap-to-define coverage of the Saadia Tafsir toward
the documented **≥80% hand → retire the unverified Camel auto-dict** milestone.

## Snapshot (via `scripts/coverage_report.py`, 81,225 tokens)

| metric | before | after | Δ |
|---|---|---|---|
| hand-starter | 18,195 (22.40%) | 18,195 | — |
| hand-lane | 44,092 (54.28%) | **45,250 (55.71%)** | +1,158 |
| **hand TOTAL** | **62,287 (76.68%)** | **63,445 (78.11%)** | **+1.43 pts** |
| auto (Camel) | 2,686 (3.31%) | 2,686 | — |
| COVERED | 64,973 (79.99%) | **66,131 (81.42%)** | +1.43 pts |
| misses (occ.) | 16,252 (20.01%) | **15,094 (18.58%)** | −1,158 |
| distinct miss types | 10,571 | **10,265** | −306 |

Per-book hand-coverage after: bereshit 76.02 · shemot 78.67 · vayikra 79.61 ·
bamidbar 82.43 · devarim 74.38. `npm run build` clean (node_modules was absent —
`npm install` first).

`dictionary-lane.json` entries: **657 → 790** (+133).

## What shipped

**133 verified entries** appended to the lane tier (95 content words + 38 proper
nouns), drawn from the **top ~250 ranked misses** in `coverage-misses.json`.
Method: two subagents grouped miss surfaces by stem and read each word's meaning
straight from the **aligned `hebrew` / `hebrew_translation`** of an actual corpus
occurrence (every gloss traces to a real verse — not guessed); a serializer then
deduped against starter/lane/auto **and** `tafsir-divergence.json`, shipped only
confidence-high content + all proper nouns, and parked the rest.

- Content: common vocabulary the reader hits constantly — e.g. עד "count/census",
  עמיק "deep", אלעצפור "bird", אלקלעה→(fortress, see deferred), ממלכה, אלאחכאם
  "the laws", כ'בז "bread", כ'מר "wine", ד'הב "gold", חמאר "donkey", נהר "river",
  כרוב "cherub", עמאמה "mitre", זרפין "hooks", רקאק/גרדק "wafers/loaves".
- Proper nouns: the census-chief genealogies (נחשון, עמינדב, אליסף, אליצור,
  שלומיאל, נתנאל, גמליאל, אבידן, אחיעזר, פגעיאל, אחירע …) + patriarchs/places
  (תרח, עמרם, צלפחד, גלעד, ברנע, חמאת, עמון). These recur across the censuses, so
  they punch above their per-surface frequency.

Spot-check (post-apply): שipped surfaces resolve (אלעצפור, נחשון, עמדהא, ועלק,
יתפש, אלחבס, כ'זף, אלמסתקים, ככואכב, צלפחד …). ✓

## Deferred (`data/_dict_batch1_deferred.json`, 81 entries)

- **55 "already covered"** — the stem lemma already exists in a dict (or in the
  divergence corpus), so the serializer skipped it. **BUT** many of these are the
  highest-value Batch-2 targets: the existing entry lacks the *suffixed* miss
  surface, which the lookup's candidate-chain can't reduce (it strips prefixes
  ו/אל/ב·ל·כ·פ + final-letters + trailing-', but **not pronominal suffixes**).
  Confirmed live: ויד'בחה (stem ד'בח), אלאיימה (אמאם), אזואגא (זוג) are still
  misses because their stems shipped elsewhere without these variants. Examples
  to absorb in Batch 2: אעטי←אעטיהא/אעטיה · יאכל←יאכלונה · עין←עינאה · קאל←וקאלא ·
  מות←מותה · קריה←קראהם · עדו←אעדאיה · מעדוד←מעדודי · קצבה, ג'שא, קדם, סמא …
- **4 divergence collisions** (logged): חמאה (vs תחמיה variant), זוג (vs זוג'),
  קצבה (vs פדר→qaṣaba twist), יפאע — left to the divergence panel.
- **~22 med/low/uncertain** parked for a verified pass: קלעה, גנאח, נעמא
  (asseverative), דארום (Saadia "Negeb"→fortress), חרג ("curse"), אמהאג ("bars"?),
  בדרה (measure), שפאהא (idiom), פיח↔אזכרה, תוניה, צידא, ברד=Bered (homograph of
  "hail"), plus the divergence-owned ראם/ת'רא/צריח.
- **2 drops**: אלה (ambiguous fragment of أهل / demonstrative), וא (orphaned waw).

## Yield observations

- The miss curve is extremely flat (top 100 surfaces = 3.8% of miss occurrences;
  max single-surface freq = 9), because the tokenizer counts inflected *surface*
  forms. Stem-grouping with `variants[]` is the multiplier; 133 stem entries
  closed 306 distinct miss-types / 1,158 occurrences.
- **Biggest remaining lever = pronominal-suffix resolution.** A large share of
  misses are `<stem>+ה/הא/הם/ך/כם/י`. Two ways to harvest:
  (1) **Batch 2 — variant augmentation**: add the suffixed surfaces to the ~55
  already-existing stems (this batch's deferred list) + keep descending the
  ranked misses. Low-risk, data-only.
  (2) **Structural (higher value, higher risk)**: teach the candidate-chain in
  `lib/lookup.ts` (and its mirror in `scripts/verify_divergence.py`) to strip
  pronominal suffixes — would auto-resolve thousands of inflected misses at once,
  but must be tested carefully against over-matching and the divergence verifier.

## Next

1. **Batch 2 (recommended):** variant-augmentation of the 55 already-covered
   stems + misses ~250–500. Re-run `coverage_report.py`; target hand ≥ 80%.
2. At hand ≥ 80%: retire the auto-dict (`source:"camel"`) — one-line UI change in
   `app/tafsir/reader.tsx` + disable the `auto` tier in `lib/lookup.ts` (per
   `PHASE2_ROUND6_PROMPT.md`).
3. Stretch: the structural suffix-stripping change (above), as its own tested PR.

Working tree left uncommitted per project convention.
