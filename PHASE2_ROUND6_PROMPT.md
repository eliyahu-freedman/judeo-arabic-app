# Phase 2 Round 6 — head-of-queue hand cleanup + scripted Sonnet long-tail sweep

Paste-ready prompt for a fresh Claude Code session. Picks up where Round 5
landed on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

- Round-4 origin prompt: `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`.
- Round-4 B+C resume prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`.
- Round-5 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND5_PROMPT.md`.
- Plan: `~/.claude/plans/i-want-to-continue-quirky-taco.md`.
- Memory: section "Phase 2 Round 5 — Batches D + E SHIPPED 2026-05-28"
  inside `judeo-arabic-app-project.md`.

**Round 5 final state (uncommitted in working tree):**
- Hand-coverage **67.95%** (Round-5 delta +1.31 pts, well below the +5–6 pt
  projection — head counts have flattened since Round 3, so each
  hand entry now buys ~0.02% of 81,225 tokens).
- Covered total **72.08%**. Lane entries **364** (was 349 at Round-4 end,
  250 at Round-3 end).
- Per-book: bereshit 67.06 · shemot 67.66 · vayikra 68.65 · bamidbar
  **71.38** (best) · devarim **65.16** (still laggard; +1.69 in Round 5,
  the biggest single-book gain of the round).
- `npm run build` clean (213 pages). `verify_divergence.py` exit 0 (the
  pre-existing Bereshit-mix warning hasn't budged — it's a Phase-3 item).
  `scope_saadia_notes.py` 0 residual hits.

**Top misses going into Round 6** (the queue this round attacks):

```
 17  תצנעה   [standard]   — 2ms impf + 3ms obj (you-make-it) — verb, hand
 15  בכ'ורא   [has-apos]   — "his firstborn" — בכר + 3ms suffix
 15  תאכלוה   [standard]   — "you shall eat it" — אכל 2mp + 3ms obj
 15  יג'סל    [has-apos]   — "he shall wash" — ghasala 3ms impf
 15  ושריפהם  [w-prefixed] — "and their burning" — שריפה pl + suffix
 15  אלת'ור   [has-apos]   — "the bull" — high-value lemma, scripted-pass
 15  עדא      [standard]   — "except, besides" — function word
 15  חג       [standard]   — "festival" — high-value lemma
 15  פטירא    [standard]   — "matzah, unleavened" — high-value lemma
 15  גרש      [standard]   — "drive out" — verb stem
 15  אלמקרב   [standard]   — "the offering" — high-value lemma
 15  אלאצג'ר  [has-apos]   — "the smaller, the younger" — comparative
 15  וחש      [w-prefixed] — needs context check
 15  כילא     [standard]   — "lest, in order that not"
 15  עבדא     [standard]   — "a slave" (acc/indef) — existing ʿabd-servant variant
```

**Diagnosis.** The head-of-queue count has flattened from Round 3's 30+ to
a long plateau at 15–17 occurrences. The remaining gain to ≥80% hand has
to come from the long tail (12,142 unique misses, ~22,000 occurrences),
not from continued head curation. Round 6 splits into:

1. **Batch F — head hand cleanup** (~15 entries, ~+0.5–1 pt).
   The remaining high-value lemmas in the top-50 (חג festival, פטירא
   matzah, אלת'ור bull, אלמקרב offering, גרש drive-out, אלאצג'ר smaller,
   עדא except, כילא lest, יג'סל wash, etc.) + the high-frequency inflected
   forms that decompose to existing stems (תצנעה, בכ'ורא, תאכלוה, ושריפהם,
   עבדא) added as variants on existing entries.

2. **Batch G — scripted Sonnet long-tail sweep** (~+5–10 pts target).
   `scripts/generate_lane_entries.py` driven against a regenerated
   `/tmp/ja-candidates.json` (built from the post-Round-5
   `data/coverage-misses.json`). Filter min-freq ≥ 5, batch 25/call, target
   ~300–500 entries, cost-cap $10–15.

**Round-6 target: 67.95% → ~75–80% hand-coverage.** Stretch goal is
hand ≥ 80%, which would let us retire the auto-dict (Camel MSA) badge —
at that point Camel's noisy MSA glosses on Saadianic stems do more harm
than good.

---

## Batch F — head-of-queue hand cleanup (~15 entries, ~+0.5–1 pt)

### Step 1: Audit which top-50 misses are still hand-curatable

```bash
python3 - <<'PY'
import json
m = json.load(open('data/coverage-misses.json'))['misses']
# Show top 50 with their bucket — sorted descending
for entry in m[:50]:
    print(f"  {entry['count']:3d}  {entry['surface']:18s}  [{entry['bucket']}]")
PY
```

### Step 2: For each candidate, classify as (a) inflected variant on existing stem or (b) new lemma

Inflected-variant candidates (likely):
- **תצנעה** — 2ms imperfect of צנע "to make" + 3ms object pronoun.
  Stem `tasnaʿ-make` likely exists in lane; add `תצנעה` as variant.
- **בכ'ורא** — בכר "firstborn" + 3ms suffix. Existing `bakr-firstborn`?
- **תאכלוה** — 2mp imperfect of אכל "eat" + 3ms object. Existing `akala-eat`
  was extended in Batch B; add `תאכלוה`.
- **ושריפהם** — שריפה "burning" pl + 3mp suffix. Check if `sharifa-burning`
  exists; if so, add variant; if not, new entry.
- **עבדא** — accusative indefinite of עבד. Already in `ʿabd-servant` variants? 
  My Round-5 audit showed it's still missing. Add as variant.
- **יג'סל** — 3ms imperfect of ghasala "to wash". The verb stem may be
  missing entirely from lane; if so it's a new entry.

New-lemma candidates:
- **חג** — festival (Hebrew חַג, Arabic ḥajj). Saadia's regular gloss for
  Hebrew חַג. Likely already in starter under a different surface form —
  audit first.
- **פטירא** — "matzah, unleavened bread" (Hebrew מַצָּה, Arabic faṭīr).
  Saadia's regular gloss; appears in Pesach + sacrificial passages.
- **אלת'ור** — "the bull" (الثور, al-thawr). Saadia's gloss for פַּר.
- **אלמקרב** — "the offering" (al-muqarrab, "what is brought near").
  Saadia's gloss for קָרְבָּן in many contexts.
- **גרש** — "to drive out, expel" (Arabic gharasa? or Saadia's calque on
  Hebrew גָּרַשׁ? Context-check needed). Likely a calque.
- **אלאצג'ר** — "the smaller, the younger" (al-aṣghar). Saadia's gloss
  for הַקָּטֹן in Esau/Jacob and similar passages.
- **עדא** — "except, besides" (ʿadā). Function word. Saadia for זוּלָתִי /
  מִלְּבַד (overlaps `sawa-besides` from Round 5; verify they're not
  duplicates).
- **כילא** — "lest, in order that not" (kay-lā). Function word, Saadia
  for פֶּן.
- **וחש** — needs verse context-check before guessing sense.

### Step 3: Author `/tmp/apply_round6_F.py`

Same `NEW_ENTRIES` / `VARIANTS_PATCH` / `STARTER_VARIANTS_PATCH` shape as
the Round-5 scripts. The Round-5 D/E scripts are reference templates —
unfortunately `/tmp/` gets wiped between sessions, so reconstruct from
`scripts/apply_round4_A.py` plus the apply-with-patch logic from the
Round-5 plan file.

### Step 4: Validate JSON round-trip, re-run coverage

```bash
python3 -c "import json; json.load(open('data/dictionary-lane.json')); json.load(open('data/dictionary-starter.json'))"
python3 scripts/coverage_report.py  # ~3-4 min — skip pre-batch refresh if dict unchanged
```

Report delta against +0.5–1 pt target.

---

## Batch G — scripted Sonnet long-tail sweep (~+5–10 pts target)

### Step 1: Regenerate `/tmp/ja-candidates.json` from post-Round-5 misses

The script reads `{token, count}` objects from `/tmp/ja-candidates.json`.
The post-Round-5 `data/coverage-misses.json` is the source — convert
surface → token:

```bash
python3 - <<'PY'
import json
m = json.load(open('data/coverage-misses.json'))['misses']
# coverage-misses.json caps at 1000; for Round 6 we want the full miss
# queue. Re-run coverage_report.py with the long-tail capture if needed.
# As of Round 5 the top 1000 captures every form with count ≥ 5.
out = [{"token": e["surface"], "count": e["count"], "bucket": e["bucket"]}
       for e in m]
with open('/tmp/ja-candidates.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(out)} candidates to /tmp/ja-candidates.json")
PY
```

If you want the FULL tail (down to count=1), tweak
`scripts/coverage_report.py`'s top-N cap and re-run (3–4 min) before
generating candidates. The Round-5 cap of 1000 covers ~52% of total miss
occurrences (head-loaded); going to 5000 covers ~85%.

### Step 2: Dry-run preview (no API spend)

```bash
.venv-camel/bin/python3 scripts/generate_lane_entries.py \
    --dry-run --limit 5 --min-freq 5
```

This prints the first 5 candidates with their context blocks, exactly as
they'd be sent to Sonnet 4.6. Verify the prompt shape looks reasonable
(token + count + 1–2 example verses each).

### Step 3: Small validation run (~$1)

```bash
ANTHROPIC_API_KEY=... \
.venv-camel/bin/python3 scripts/generate_lane_entries.py \
    --limit 50 --batch 25 --min-freq 5 --cost-cap 2.0
```

Audit the 50 new entries: read 5–10 of them and confirm:
- Saadia-specific senses are NOT being asserted in `gloss_en` (system
  prompt says no, but verify).
- Function words got the right pos tag.
- Hebrew-letter biblical proper names got the right Hebrew gloss.
- No entry duplicates an existing lane lemma with the same gloss.

Re-run `coverage_report.py` to measure the delta. If +0.5–1 pt for 50
entries, the larger run will land ~+5–10 pts for 300–500 entries.

### Step 4: Full sweep

```bash
ANTHROPIC_API_KEY=... \
.venv-camel/bin/python3 scripts/generate_lane_entries.py \
    --limit 400 --batch 25 --min-freq 5 --cost-cap 15.0
```

Cost-meter persists at `~/.cache/judeo-arabic-app/lane-entries-cost.json`.
Use `--show-cost` (the meter is read-only; just inspect the file directly
if the flag isn't wired). The Round-3 baseline was ~$0.08/chapter × 187
chapters ≈ $15 for translation; lane-entry generation is shorter prompts
+ cached system block, so 400 entries at $0.03–0.05 each = $12–20 max.
Hard-cap is `--cost-cap`.

### Step 5: Post-sweep cleanup

The script's de-dupe pass keeps entries safe, but two scoping issues
need a pass after Batch G:

1. **Re-run `scripts/scope_saadia_notes.py`** — Sonnet may write
   "Saadia's gloss for X" into the `notes` field; the scoper moves those
   to `saadia_note`. Should report ≥0 entries updated; 0 residual hits.

2. **Manual spot-check of 5–10 random Batch-G entries.** Look for:
   - Lane-territory glosses that are actually Saadia coinages (the
     system prompt warns against this but doesn't catch everything).
     If found, move sense to `saadia_note` and rewrite `gloss_en` to
     the classical Arabic baseline.
   - Overly broad glosses ("good", "thing", "do") that need narrowing.
   - Wrong POS tags (especially particle vs. preposition).

3. **Optional: add divergence entries.** If a Batch-G token reveals a
   Saadia-specific sense distinct from classical Arabic, add to
   `data/tafsir-divergence.json` (Phase 3 work, runs in parallel).

---

## Per-batch workflow (unchanged)

1. **Refresh misses if dict changed:** `python3 scripts/coverage_report.py`
   (~3–4 min). Skip if no dict changes since last run.
2. **Build the patch / candidate file** as above.
3. **Validate JSON round-trip:**
   `python3 -c "import json; json.load(open('data/dictionary-lane.json'))"`.
4. **Re-run coverage** and confirm delta against targets.
5. **Build check at end:** `npm run build` — must stay clean (213+ pages).
6. **No commit.** Working tree stays uncommitted per project pattern.

---

## Verification at end of Round 6

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 75%**
  (stretch ≥ 80%). +7–12 pts over the 67.95% baseline.
- `python3 scripts/verify_divergence.py` exits 0.
- `python3 scripts/scope_saadia_notes.py` reports 0 residual hits.
- `npm run build` clean.
- Spot-check 3 random tafsir chapters in dev (`npm run dev`):
  - `/tafsir/bamidbar/29` for ordinals + sacrificial-day vocab
  - `/tafsir/bereshit/41` for אללחם / אלת'ור / אלמקרב
  - `/tafsir/devarim/16` for חג / פטירא / festival vocab
  Confirm previously-missing tokens now open the gloss panel.
- Cost-meter spend tallied; <$15 cumulative for Round 6 Batch G.

## Gotchas (carry-overs from Round 5)

- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts` policy: `אלאה ≠ stem אלא + suffix`).
- **Trailing-apostrophe lemmas** (טאעה' style) — store bare `טאעה`, add
  `'`-suffixed variant if needed. `normalizeFinals` strips trailing `'`
  on BOTH sides, so duplicates are fine.
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note`. The Advanced reader hides `saadia_note` entirely;
  `scope_saadia_notes.py` auto-migrates Saadia-mentioning sentences after
  each batch.
- **Homographs are fine** — keep separate entries for `מר` (pass) vs `מר`
  (bitter), `רגל` (man) vs `רגל` (foot), `לבן` (Laban) vs `לבן` (milk).
  The UI shows both on tap.
- **`coverage_report.py` runs ~3–4 min** (npx tsx warmup × 187 chapters).
  Skip the pre-batch refresh if the dict hasn't changed since the
  snapshot timestamp.
- **Round-5 lesson — prompt projections are optimistic.** The Round-5
  prompt projected +5–6 pts; reality was +1.31. The Sonnet long-tail
  sweep is the actual lever for closing the gap to 80% — head curation
  has reached diminishing returns.
- **Don't ship Camel-tools fallback past 80%.** Once hand ≥ 80%, the
  auto-dict (`source: "camel"`) badge should be retired in
  `app/tafsir/reader.tsx` and `lib/lookup.ts`'s `auto` tier disabled.
  This is a one-line UI change + a 2-line lookup change.

## After Round 6

- **Phase 3 (divergences 32 → ~180).** Run in parallel on
  `data/tafsir-divergence.json`. Doesn't touch dict files. Plan TBD —
  likely a curated-by-book sweep similar to the dictionary expansion.
- **Phase 4 (Word-of-the-Day homepage card).** Year-mixed deterministic
  seed; pulls from lane dict; shows on `app/page.tsx`. Independent files.
- **Retire auto-dict badge** once hand ≥ 80%.

---

**Tell Claude:** "Resume Phase 2 Round 6 per
`~/Code/judeo-arabic-app/PHASE2_ROUND6_PROMPT.md`. Run Batch F first
(hand-curate the ~15 remaining head-of-queue lemmas + add inflected
variants to existing stems), then Batch G (regenerate
`/tmp/ja-candidates.json`, dry-run, $1 validation run on 50 entries,
then full $10–15 sweep on ~400 entries), reporting coverage delta after
each. Final spot-check 3 chapters in dev."
