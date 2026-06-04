# Phase 3 R1 Second Wave — Vayikra Batch — Session Notes

**Date shipped:** 2026-05-30
**Apply script:** `scripts/apply_phase3_r1_vayikra.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

Task **#2** of the Phase 3 R3 continuation — the R1 second wave (≥5 net-new TWIST
per book to activate the per-book gate uniformly). **This batch does Vayikra**
(the 2nd of 4 books, after Shemot). Bamidbar and Devarim remain.

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 130 | 135 | +5 net-new |
| Tier distribution | 42 twist / 38 note / 50 gloss | **47** / 38 / 50 | +5 TWIST |
| Vayikra first-verse twists | 0 (the 1 twist touching Vayikra — חאכמא — is Bereshit-anchored) | **5** | +5 — gate now ACTIVE |
| Vayikra gate | inactive (<5) | **ACTIVE + PASS** | direct 3/5=60% · backed 4/5=80% · no-cite 1/5=20% |
| Gates | — | verify_divergence.py PASS · 0 warnings · npm run build clean | all green |

---

## Per-entry rundown — 5 TWIST

All surfaces VERIFIED in `data/tafsir-vayikra-{ch}.json`; classical senses via Lane;
Blau senses via the arabic-lexicon skill.

### 1. תרפק (رفق, root ر-ف-ق) — Aramaic-driven prune calque · **direct** · 2 verses
Heb תִּזְמֹר "prune" → Ar رفق, Lev 25:3 + 25:4 (the Sabbatical-year vineyard law).
Classical رفق = "to be gentle" ONLY — no agricultural sense. Saadia loads it with the
**Aramaic** רְפַק "to dig/hoe" (the Babylonian-academy register). A trilingual bridge:
Hebrew verb → Arabic root selected for its Aramaic sense. Blau glosses Form I "to hoe,
to prune", flagging the Aramaic substrate and citing Lev 25:3.

### 2. פיצ'הא (فيضة, root ف-ي-ض) — Hebrew-driven flux specialization · **direct** · 1 verse
Heb זוֹב (impurity-law genital discharge) → Ar فيضة, Lev 15:28. Classical فيض = positive
"overflow, abundance"; Saadia narrows it to the clinical-pathological purity-law sense,
tracking the Hebrew root's specialized meaning. Blau lemmatizes فيضة = "genital flux,
gonorrhea / זוב", citing this verse. A register-collapse from "bounty" to "discharge".

### 3. אלכ'אמע (خامع, root خ-م-ع) — vernacular blemish identification · **direct** · 1 verse
Heb שָׂרוּעַ (obscure priestly disqualifying blemish) → Ar خامع "dislocated-hipped", Lev
21:18. Classical خمع = "to limp" (a gait, of the hyena); Saadia uses the **vernacular**
sense "hip dislocated / נשמטה ירכו" (Blau cites Muḥīṭ al-Muḥīṭ, distinguishes from
classical خمع and from خلع). Tafsir reaching past the classical lexicon to living
dialectal medical vocabulary to pin down a Torah blemish-term.

### 4. אלקצבה (قصبة, root ق-ص-ب) — suet read as the interior/pluck · **adjacent** · 3 verses
Heb הַפָּדֶר ("the suet/fat-portion" of the burnt offering) → Ar قصبة "the interior
organ-bloc (liver-lungs-heart)", Lev 1:8, 1:12, 8:20. An exegetical-anatomical fork:
Saadia reads פדר not as fat but as the inner-organ section laid on the altar. Blau
attests قصبة = "interior of the body" (post-classical extension from "interior of a
town") but does not cite the פדר rendering directly → relation=adjacent.

### 5. שיאטין (الشياطين, root ش-ط-ن) — sheirim demythologized as demons · **no-cite** · 1 verse
Heb שְׂעִירִם ("hairy ones / goat-demons / satyrs") → Ar الشياطين "the demons", Lev 17:7.
Saadia identifies the forbidden cult's recipients outright as demons — the same
demythologizing-by-identification method as אשראף (בני-האלהים→nobles), קרדא (Ararat→Qardū),
and אתון (Ur→furnace). The divergence is EXEGETICAL (deciding what the שעירים *are*), not
lexical-within-Arabic (شيطان = demon is classical), so Blau does not lemmatize it.
**Shipped sources=[lane, saadia-direct], no blau_dict** — consistent with the existing
no-cite identification-entries. Logged in `_blau_saadia_deferred.json#/no_cite_audit/phase3_r1_no_blau`.

---

## Deferred buckets

- 4 Blau ids logged to `phase3_r1_consumed` (idempotent): 15824 תרפק, 18378 פיצ'הא,
  17407 אלכ'אמע, 18594 אלקצבה.
- 1 no-blau decision logged to `no_cite_audit/phase3_r1_no_blau`: שיאטין (Lev 17:7).

Dropped in curation:
- **כ'לף** (خلف, ספיח→regrowth, Lev 25:5) — Blau-direct and TWIST-grade, BUT collides
  with the existing gloss lemma `כ'לף` (root خ-ل-ف): the apply script would skip it as a
  duplicate lemma_ja. Resolve later via promote-in-place on the existing entry if the
  regrowth sense is distinct from the existing gloss's sense.
- NOTE-grade (Lane already backs the sense, not paradigm-shifting): תשייט (شوط,
  צרבת→singe), זיברתה (زبر, garment nap), מצ'לפה (ظلف, denominal cloven-hoof).
- Other bonus identification-TWISTs found but not shipped this batch (candidates for a
  future Vayikra batch, all no-cite/saadia-direct): Azazel→Mount Azaz (16:8/16:10),
  אני יהוה→"I am God the Punisher" (18:21, 19:12-28, 22:3), נפש...בדם→"the blood is the
  soul's dwelling" (17:11), חקת עולם→רסם אלדהר (16:29ff, leans NOTE).

---

## Gates

- `python3 scripts/apply_phase3_r1_vayikra.py` → "Added 5 entries", "Total entries now:
  135", tiers `{twist:47, note:38, gloss:50}`, `{phase3_r1_consumed_added:4,
  no_cite_audit_added:1}`.
- `python3 scripts/verify_divergence.py` → **135 entries · All citation + sources checks
  PASS · 0 warnings · Quality bar PASS**. Vayikra total=5, direct=3, adjacent=1, no-cite=1.
- `npm run build` → **clean**.

---

## Yield observations

1. **Revising the Shemot-batch "avoid no-cite" guidance.** Shemot's notes said avoid
   no-citation twists. Vayikra shows the principled exception: **demythologizing /
   midrashic identifications** (שעירים→demons) are inherently EXEGETICAL, not lexical,
   so Blau structurally won't lemmatize them — and the existing corpus already catalogs
   exactly these as no-cite (אשראף, קרדא, אתון). So: avoid no-cite for ordinary lexical
   twists, but a single well-grounded identification-twist per book is legitimate and
   keeps the gate comfortable (here 1/5 = 20%).

2. **Trilingual calques are a distinct, high-value TWIST seam.** תרפק (Hebrew verb →
   Arabic root chosen for its *Aramaic* sense) is invisible from Arabic alone. Blau flags
   these explicitly ("ארמית/בבלית"). Worth a dedicated search pass per book: Blau senses
   that cite Aramaic/Babylonian substrate for a Saadia rendering.

3. **Two calque DIRECTIONS recur and are worth naming as archetypes:** (a) **Hebrew-driven**
   — an Arabic root loaded with its Hebrew cognate's extra sense (Shemot אגתחד כחד→destroy;
   Vayikra פיצ'הא זוב→flux); (b) **Aramaic-driven** — Arabic root chosen for its Aramaic
   sense (Vayikra תרפק זמר→prune via רפק). Both are Blau-direct because Blau documents the
   substrate. Mine for these in Bamidbar/Devarim.

4. **Vernacular-sense identifications** (אלכ'אמע, where Blau cites Muḥīṭ al-Muḥīṭ for a
   colloquial sense outside classical Lane) are a reliable Blau-direct TWIST source for
   the obscure technical-realia terms (blemishes, garments, sacrificial parts).

5. **Lemma-collision check is mandatory before authoring.** כ'לף was a strong TWIST that
   had to be dropped purely because its lemma_ja already exists as a gloss. Always diff
   proposed lemma_ja against the consumed set FIRST.

---

## Recommended next-session strategy

Continue the R1 second wave on the **remaining 2 books**, one batch each:

1. **Bamidbar** — currently 2 first-verse twists; needs ≥3 more (≥5 total). Includes the
   likely **cross-book promote-in-place** of the Shemot אלמהל entry to **Num 14:18**
   (erekh apayim repeat) — extend that entry's verses[] rather than authoring a new one.
   Net-new candidates from the wilderness-narrative, nazirite, census, and Balaam-oracle
   vocabulary. Mine for the Hebrew-driven / Aramaic-driven calque archetypes (#3 above).
2. **Devarim** — currently 1 first-verse twist; needs ≥4 more. The TWIST-adjacent NOTEs
   already shipped (אקרץ' conquest-extermination, יסיב shemittah-release, ממתעה) could
   **promote to TWIST** if Blau-verification confirms paradigm-shifting status (per
   Devarim B1 next-strategy #3) — a faster path than net-new mining. Plus net-new from
   the Mosaic-discourse rationalist-philosophical register (Devarim's signature).

Reusable assets: `apply_phase3_r1_vayikra.py` as the per-book template (swap NEW_ENTRIES
+ book filter); the verified-surface workflow (grep all corpus occurrences → check token
resolution against candidate_chain → set variants); the Lane+Blau confirmation step.
