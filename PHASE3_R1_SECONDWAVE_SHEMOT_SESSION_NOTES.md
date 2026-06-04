# Phase 3 R1 Second Wave — Shemot Batch — Session Notes

**Date shipped:** 2026-05-30
**Apply script:** `scripts/apply_phase3_r1_shemot.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

This is **task #2** of the Phase 3 R3 continuation — the R1 second wave, which
adds ≥5 net-new TWIST entries per book to activate the verifier's per-book
quality gate uniformly. **This batch does Shemot** (the first of 4 books). Vayikra,
Bamidbar, and Devarim remain for subsequent batches.

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 125 | 130 | +5 net-new |
| Tier distribution | 37 twist / 38 note / 50 gloss | **42** / 38 / 50 | +5 TWIST |
| Shemot first-verse twists | 1 (תגלא, no-cite) | **6** | +5 — gate now ACTIVE |
| Shemot gate | inactive (<5 entries) | **ACTIVE + PASS** | direct 4/6=67% · backed 5/6=83% · no-cite 1/6=17% |
| Gates | — | verify_divergence.py PASS · 0 warnings · npm run build clean | all green |

The Shemot quality bar now activates (≥5 twists) and clears all three thresholds
(≥45% direct, ≥70% backed, ≤30% no-cite). תגלא's pre-existing no-citation entry is
absorbed at 17% — well under the 30% ceiling.

---

## Per-entry rundown — 5 TWIST

All surfaces VERIFIED in `data/tafsir-shemot-{ch}.json` (fields ch/v/ja/hebrew);
classical senses confirmed via Lane; Blau senses via the arabic-lexicon skill.

### 1. שריעה (شريعة, root ش-ر-ع) — Torah-as-*sharīʿa* calque · **direct** · 6 verses
Heb תּוֹרָה / תּוֹרַת ה' / תּוֹרֹת → Ar شريعة / شرائع. The biblical "instruction/teaching"
re-coded into the Islamic-theological **revealed-law** category. Systematic across
12:49 (תּוֹרָה אַחַת = שריעה ואחדה), 13:9 (תּוֹרַת יְהוָה = שריעה' אללה), 16:4 (בְּתוֹרָתִי
= שראיעי), 16:29 (even הַשַּׁבָּת = שריעה' אלסבת), 18:20 (הַתּוֹרֹת = אלשראיע), 24:12
(וְהַתּוֹרָה, tablets verse = ואלשראיע). Lane: شريعة primarily "watering-place"; the
legal sense (سَنَّ → شريعة) is the loaded religious register. Blau: الشرائع = the
Pentateuch. The single lexical choice carries a theology of revelation.

### 2. אלמהל (مهل, root م-ه-ل) — anti-anthropomorphic אֶרֶךְ אַפַּיִם · **adjacent** · 1 verse
Heb אֶרֶךְ אַפַּיִם ("long of nostrils/anger") → Ar طويל אלמהל ("long of forbearance/
respite"), Shemot 34:6 — the Thirteen-Attributes verse. Strips the somatic
nostrils→anger idiom and substitutes the impassible attribute of patient respite.
Same anti-anthropomorphic strategy Saadia uses for the divine face/hand/descent.
Relation=adjacent: Blau attests مهل="respite/delay"; the divine-attribute deployment
is Saadia's own.

### 3. אגתחד (اجتحد, root ج-ح-د) — Hebrew-driven "destroy" calque · **direct** · 1 verse
Heb וַתִּכָּחֵד ("you would have been effaced") → Ar اجتحد "be destroyed", Shemot 9:15.
Classical جحد = "to deny" ONLY (Lane); no destroy-sense. Saadia keeps the Hebrew
ROOT via its Arabic cognate and rides the Hebrew's extra "destroy" range (Heb כחד =
deny + be-destroyed). Blau flags it as a Hebrew-influenced sense, citing Derenbourg
on this verse. Exposes the bilingual cognate-substrate of the Tafsir.

### 4. צריח (صريح, root ص-ر-ح) — אֶזְרָח → pure-lineage legal category · **direct** · 3 verses
Heb אֶזְרָח ("native-born") → Ar صريح "of pure unmixed descent", paired antithetically
with دخيل (= גֵּר). Shemot 12:19, 12:48, 12:49 (the Passover inclusion-law). Converts
the biblical native/sojourner distinction (birthplace) into a native/incomer
distinction framed by **purity of descent**. Blau (headword صريحي) = "of pure race,
native", cites Saadia at Shemot 12. (Corpus surface is base صريح; Blau lemmatizes the
nisba صريحي of the same root/sense.)

### 5. מתרבץ (متربّص, root ر-ب-ص) — מִסְתּוֹלֵל hapax reframe · **direct** · 1 verse
Heb מִסְתּוֹלֵל (hapax, traditionally "you exalt yourself") → Ar متربّص "detaining (my
people)", Shemot 9:17. Classical تربّص = intransitive "to wait / lie in wait"; Saadia
bends it to transitive "detain, hold back", the purpose-clause (ללא תטלקהום "so as
not to release them") carrying the reading that Pharaoh's offense is obstruction, not
arrogance. Blau records the post-classical transitive ربص+ب "to hold back", citing
this verse. Hapax-strategy: opaque Hebrew → stretchable Arabic word + syntax-driven
sense.
(Note: lemma stored as `מתרבץ` without the trailing apostrophe — the verifier/runtime
`stripPunct` strips trailing `'`, so the corpus surface `מתרבץ'` resolves to `מתרבץ`.)

---

## Deferred buckets

No new skip/borderline records. 5 Blau ids logged to `phase3_r1_consumed` (audit
trail, idempotent on blau_id): 16530 שריעה, 19552 אלמהל, 14480 אגתחד, 16947 צריח,
15668 מתרבץ.

---

## Gates

- `python3 scripts/apply_phase3_r1_shemot.py` → "Added 5 entries", "Total entries now:
  130", tiers `{twist:42, note:38, gloss:50}`, `phase3_r1_consumed_added: 5`.
- `python3 scripts/verify_divergence.py` → **130 entries · All citation + sources
  checks PASS · 0 warnings · Quality bar PASS**. Shemot now total=6, direct=4,
  adjacent=1, no-cite=1.
- `npm run build` → **clean** (187 SSG tafsir paths).

---

## Yield observations

1. **Blau-first mining is high-yield for the rich-content books.** Of 135 Shemot-citing
   Blau candidates, the verified TWIST-grade survivors clustered in exactly the
   theologically-charged passages: the Decalogue/attributes (34:6), the Plagues
   narrative (9:15, 9:17), the Passover inclusion-law (12:19-49), and the
   torah-vocabulary (12:49–24:12). Mine the dense legal/theological chapters first.

2. **The gate is comfortably cleared with 5 new direct/adjacent twists per book.**
   With one legacy no-cite entry (תגלא), 4 direct + 1 adjacent yields 67%/83%/17% —
   clear margins. Target ratio for the remaining books: aim for ≥4 of any 5-batch to
   be `direct`, with at most 1 `adjacent` and 0 new `no-cite`. Avoid shipping
   no-citation twists in the R1 second wave.

3. **Two distinct TWIST archetypes recurred and are worth seeking in the other books:**
   (a) **anti-anthropomorphic attribute substitution** (אלמהל ← erekh apayim) — look
   in Bamidbar's divine-attribute repeats (Num 14:18 repeats erekh apayim — a likely
   cross-book extension of אלמהל rather than a new entry) and theophany passages;
   (b) **Hebrew-driven cognate calque** (אגתחד ← כחד) — look for Arabic verbs Saadia
   loads with a Hebrew cognate's extra sense; Blau flags these explicitly as
   "השפעת העברית".

4. **Lemma-form / apostrophe hygiene matters for the gate.** `מתרבץ` (drop trailing `'`)
   and plural-stem variants (שראיע, שראיעי) had to be set deliberately so the
   verifier's `candidate_chain` (strips ו / אל / one of ב·ל·כ·פ + final-letter and
   trailing-`'` normalization) resolves every cited verse. Always re-pull all corpus
   occurrences and check each cited verse has a resolving token BEFORE applying.

---

## Recommended next-session strategy

Continue the R1 second wave on the **remaining 3 books**, one batch each (same
mine→curate→verify→apply→gate pipeline used here):

1. **Vayikra** — currently 1 first-verse twist. Mine the Vayikra-citing Blau
   candidates; the sacrificial/purity/holiness vocabulary is a rich TWIST seam
   (consecration, atonement-mechanism, impurity reframes).
2. **Bamidbar** — currently 2 first-verse twists. Includes the likely **cross-book
   extension** of אלמהל to Num 14:18 (erekh apayim repeat) — promote-in-place rather
   than a new entry — plus net-new twists from the wilderness-narrative + nazirite +
   census vocabulary.
3. **Devarim** — currently 1 first-verse twist, but it already has TWIST-adjacent
   NOTEs (אקרץ', יסיב, ממתעה) that could promote to TWIST in R1 if Blau-verification
   confirms paradigm-shifting status (per Devarim B1 next-strategy #3); net-new
   candidates from the Mosaic-discourse register (the rationalist-philosophical
   reframes already noted as Devarim's signature).

Reusable assets from this batch: the verified-surface workflow (grep all corpus
occurrences → check token resolution → set variants), the Lane+Blau confirmation
step, and `apply_phase3_r1_shemot.py` as the per-book script template (just swap
NEW_ENTRIES and the book filter).
