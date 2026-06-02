# Phase 2 Round 5 — pronominal-suffix variants + ordinal/lemma gaps

Paste-ready prompt for a fresh Claude Code session. Picks up where Round
4 landed on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

- Round-4 origin prompt: `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`.
- Round-4 B+C resume prompt (now done): `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`.
- Plan: `~/.claude/plans/lets-come-up-with-dazzling-lark.md`.
- Memory: section "Phase 2 Round 4 — Batches B + C + cleanup SHIPPED
  2026-05-28" inside `judeo-arabic-app-project.md`.

**Round 4 final state (uncommitted in working tree):**
- Hand-coverage **66.64%** (was 61.52% at Round-4 start; +5.12 pts net).
- Covered total **71.16%**. Lane entries 349 (was 250 at Round-3 end).
- Per-book: bereshit 66.10 · shemot 66.28 · vayikra 67.28 · bamidbar
  **70.10** (best) · devarim **63.47** (laggard, but moved +3.77).
- `npm run build` clean (213 pages). `verify_divergence.py` exit 0.
  `scope_saadia_notes.py` 0 residual hits.

**Top misses going into Round 5** (the queue this round attacks):

```
 30  בך      [standard]   — ב + 2ms suffix (with you)
 22  עליכם   [standard]   — עלי + 2mp suffix (upon you-mp)
 21  בי      [standard]   — ב + 1s suffix (with me)
 17  תצנעה   [standard]   — 2ms impf + 3ms obj (you-make-it)
 17  עבידך   [standard]   — עביד (servants pl) + 2ms suffix (your servants)
 17  אלשר    [standard]   — "the evil" — MISSING LEMMA (shar)
 17  אבאיך   [standard]   — אבא (fathers pl) + 2ms suffix
 17  אללחם   [standard]   — "the meat/bread" — MISSING LEMMA (laḥm)
 16  אניתה   [standard]   — אנייה (vessel) + 3ms suffix
 16  חפץ     [standard]   — "desire/will" — MISSING LEMMA (or homograph)
 16  ימנה    [standard]   — ימין + 3ms suffix (his right)
 16  בכם     [standard]   — ב + 2mp suffix
 16  סוא     [standard]   — "equal/same" — MISSING LEMMA (sawāʾ)
 16  אלת'אלת  [has-apos]  — "the third" — MISSING ordinal lemma
 16  אלבת'נייה [has-apos] — "the second/Deuteronomy" — MISSING ordinal lemma
```

Round 5 splits cleanly into **two parallel sub-batches**:

1. **Batch D — pronominal-suffix variants on existing stems** (~40
   variant additions across ~12 existing entries; ~+2–3 pts).
2. **Batch E — missing standalone lemmas** (~12 new entries for shar,
   laḥm, ḥafẓ, sawāʾ, ordinals 1st–10th, plus a few mid-tier misses;
   ~+2–3 pts).

**Total Round-5 target: 66.64% → ~72% hand-coverage (+5–6 pts).**

---

## Batch D — pronominal-suffix variants on existing stems

The single-letter prepositions and 1st-person/2nd-person inflections of
core nouns/preps don't get caught by the prefix-strip chain
(`lib/lookup.ts:117`) because variants are explicit-only by policy
(`אלאה ≠ stem אלא + suffix`). Round 5 enumerates them per stem.

**Target stems** (verify each lives in lane or starter before patching;
check both for homographs):

| Existing stem (id / lemma) | Suffix forms to add | Approx miss-coverage |
|---|---|---|
| `bi-with` (lemma `ב`, starter) | בי, בך, בכם, בה, בהא, בהם, בנא — most likely already present; patch any gaps | בך 30, בי 21, בכם 16 = ~67 |
| `ala` (lemma `עלי'`, starter — already patched in cleanup) | עליכם, עליה (without apostrophe), עליהא, עליהם, עלינא | עליכם 22 + tail = ~30+ |
| `ab-father` (lemma `אב`, lane) | אבך, אביך, אבאיך, אבאיכם, אבאינא, אבאיהם, אבוה, אבוהם | אבאיך 17 = ~25 |
| `yamin-right-side` (lemma `ימני`, Round-4 entry) | ימנה, ימנהא, ימנך, ימני (1s), ימינך, ימינהם — pp some already present | ימנה 16 = ~20 |
| `abad-slave` / `ʿabd` (verify which exists) | עבידך (collective pl. ʿabīd + 2ms), עבידהם, עבידהא, עבידי, עבידנא | עבידך 17 = ~25 |
| `aniya-vessel` (verify lemma) | אניתה, אניתהא, אניתהם, אניתי, אנייתכם | אניתה 16 = ~20 |
| `quds-sanctuary` (already patched Round 4) | additional קדסך, קדסה, קדסהם variants if any miss-form not covered | tail ~10 |
| `nafs-soul` (Round-4 entry) | already patched; spot-check אנפסכם, אנפסהא tail | tail ~5 |
| `kalima-word` (verify) | כלמתך, כלמתה, כלמתהם — if stem present | ~10 |
| `qalb-heart` (Round-4 entry) | already has קלבה/הא/הם/י/ך/כם/נא; check for קלובכם, קלובהם plural+suffix | tail |

**Strategy:** before writing the patch script, dump the variants of
each target entry and audit the gap against the actual miss queue.

```bash
python3 -c "
import json
d = json.load(open('data/dictionary-lane.json'))
ids = ['ab-father', 'yamin-right-side', 'nafs-soul', 'qalb-heart']  # etc
for e in d['entries']:
    if e['id'] in ids:
        print(e['id'], e['lemma_ja'], sorted(e.get('variants', [])))
"
```

Then audit which `[standard]`-bucket misses (top 200) decompose to one
of these stems + a known pronominal-suffix pattern. The pronominal
suffixes that recur in JA:

```
1s   :  ני (with verb)   |  י (with noun/prep)
2ms  :  ך
2fs  :  כי
2mp  :  כם
2fp  :  כן
3ms  :  ה / הו / ה' (with apostrophe in some scribes)
3fs  :  הא
3mp  :  הם
3fp  :  הן
1mp  :  נא
```

So for each existing stem `X`, enumerate `X+suffix` for the 8–10 forms
and add as variants. Write `/tmp/apply_round5_D.py`.

---

## Batch E — missing standalone lemmas

These aren't suffix variants — they're stems missing entirely. ~12
entries, each ~16–17 occurrences = ~+2–3 pts.

| Miss | Count | Likely meaning |
|---|---|---|
| אלשר | 17 | "the evil" (الشر, shar). Saadia's gloss for Hebrew רָע / רָעָה in moral contexts. |
| אללחם | 17 | "the meat/flesh" (اللحم, laḥm). Saadia's gloss for Hebrew בָּשָׂר / לֶחֶם (context-dependent). |
| חפץ | 16 | "desire, will, intention" (حِفظ vs. حَفِظ — verify root). Or Hebraism. Spot-check verses. |
| סוא | 16 | "equal, same; together" (سَواء, sawāʾ). Saadia uses for Hebrew יַחְדָּו. |
| אלת'אלת | 16 | "the third" (الثالث). Ordinal — likely from "the third day/year/time". |
| אלבת'נייה | 16 | "the deuteronomy / repetition" (الثانية mishna-style) OR "Bashan" (אלבת'נייה). Verify in context — this is **probably אלבת'נייה = Bashan** (Deut/Num passages); the Bashan land. |
| **add ordinals 1st–10th as a single entry-family** (if not already in lane): ת'אני, ת'אלת', ראבע, כ'אמס, סאדס, סאבע, ת'אמן, תאסע, עאשר — each w/ אל-prefixed variants | ~50 cumulative | ordinals appear in many sacrifice / day-N / year-N passages |
| Inspect next 30 misses (17-15 range) for further isolated lemmas worth adding | varies | aim for ~5 more |

**Workflow for Batch E:**
1. For each candidate, run the context-check Python block (see
   `scripts/coverage_report.py` patterns or the inline script in the
   Round-4 conversation log) to confirm sense before writing the entry.
2. Author entries with `notes` (cross-text-safe) and `saadia_note`
   (Tafsir-only). `scope:"saadia"` reserved for Saadia-coinage glosses.
3. Ordinals form a paradigm — consider a single entry `ordinals-1-10`
   with all 10 lemma surface forms as variants (compact pattern).
4. Write `/tmp/apply_round5_E.py`. Same NEW_ENTRIES / VARIANTS_PATCH /
   STARTER_VARIANTS_PATCH structure as `/tmp/apply_round4_*.py`.

---

## Per-batch workflow (unchanged)

1. **Refresh misses if dict changed:** `python3 scripts/coverage_report.py`
   (~3–4 min runtime). Skip if no dict changes since last run.
2. **Build `/tmp/apply_round5_X.py`** with `NEW_ENTRIES` and
   `VARIANTS_PATCH` (and `STARTER_VARIANTS_PATCH` if touching starter).
3. **Validate JSON round-trip:**
   `python3 -c "import json; json.load(open('data/dictionary-lane.json')); json.load(open('data/dictionary-starter.json'))"`.
4. **Re-run coverage** and confirm delta against targets.
5. **Build check at end:** `npm run build` — must stay clean (213+ pages).
6. **No commit.** Working tree stays uncommitted per project pattern.

---

## Verification at end of Round 5

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 72%**
  (stretch ≥ 74%). +5–8 pts over the 66.64% baseline.
- `python3 scripts/verify_divergence.py` exits 0 — divergence untouched
  but reverify to confirm no regression.
- `python3 scripts/scope_saadia_notes.py` clean (0 residual Saadia
  mentions in cross-text fields).
- `npm run build` clean.
- Spot-check 3 random tafsir chapters in dev (`npm run dev`, visit
  `/tafsir/devarim/3` for Bashan, `/tafsir/bamidbar/7` for ordinals,
  `/tafsir/vayikra/22` for עבידך) — confirm previously-missing tokens
  now open the gloss panel.

## Gotchas (carry-overs from Round 4)

- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts:38-44` policy: `אלאה ≠ stem אלא + suffix`).
- **Trailing-apostrophe lemmas** (טאעה' style) will never match — store
  bare `טאעה` and add `'`-suffixed variant if needed.
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note`. The Advanced reader hides `saadia_note` entirely.
- **Homographs are fine** — keep separate entries for `מר` (pass) vs `מר`
  (bitter), `רגל` (man) vs `רגל` (foot). The UI shows both on tap.
- **`coverage_report.py` runs ~3–4 min.** Skip the pre-batch refresh
  if the dict hasn't changed since the snapshot timestamp.
- **The fa-perfect chain works** — verified during Round 4 (`פולדת`
  strips פ → matches `ולדת` variant). No chain change needed for
  pronominal suffixes either; just enumerate variants.
- **Mid-word apostrophe scribal variants** — Devarim manuscripts
  sometimes write `עלי'ה` (mid-word `'` between letters) for `עליה`.
  These are different surface tokens from the tokenizer's perspective.
  Patch both forms if both appear in the miss queue.

## After Round 5

- **Round 6** (~72 → ~80% via the scripted Sonnet pass on the long
  tail of unique miss surface forms — there are 12,271 unique misses
  but the head is now flattened, so each scripted entry will only buy
  fractional points; the value is in the cumulative ~5,000-token sweep
  across infrequent forms). Use
  `scripts/generate_lane_entries.py` with the `/tmp/ja-candidates.json`
  freq-sorted list. Cost-cap at $10–15.
- Retire the auto-dict (Camel) badge once hand ≥ 80% — at that point
  the Camel-tools fallback is doing more harm than good (noisy MSA
  glosses on Saadianic stems).
- **Phase 3** (divergences 32 → ~180) and **Phase 4** (Word-of-the-Day
  homepage card on year-mixed deterministic seed) run in parallel on
  independent files — won't touch dict.

---

**Tell Claude:** "Resume Phase 2 Round 5 per
`~/Code/judeo-arabic-app/PHASE2_ROUND5_PROMPT.md`. Run Batch D first
(audit the suffix-variant gaps on existing stems before patching),
then Batch E (standalone-lemma gaps including ordinals), reporting
coverage delta after each."
