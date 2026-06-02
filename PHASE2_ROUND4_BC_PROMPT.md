# Phase 2 Round 4 — Batches B + C (resume after Batch A)

Paste-ready prompt for a fresh Claude Code session. Picks up where Batch A
landed on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

Round-4 origin prompt: `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`.
Plan: `~/.claude/plans/lets-come-up-with-dazzling-lark.md`.
Memory: section "Phase 2 Round 4 — Batch A SHIPPED 2026-05-28" inside
`judeo-arabic-app-project.md`.

**Batch A landed 2026-05-28.** 34 new lane entries (proper names +
Saadia's gazetteer). Coverage moved 61.52% → 62.04% hand (+0.52 pts).
Below the planned +2 because the top miss frequencies were only
19/17/16/15… not the 25-40 the plan assumed. **Round-4 total is now
realistically +3–5 pts (landing 65–67% hand), not +8.**

**Current state (uncommitted in working tree):**
- `data/dictionary-lane.json`: 284 entries (was 250)
- `data/coverage-snapshot.json` + `data/coverage-misses.json`: regenerated 2026-05-28 after Batch A
- Apply script archived: `/tmp/apply_round4_A.py`

**Top 15 misses going into Batch B:**

```
  32  דנא  [standard]      — homograph/demonstrative? check context
  30  בך  [standard]       — "in/with you" 2ms — should be variant of ב prep or stand-alone pronominal
  29  ברייה  [standard]    — creature/creation (Saadianic stem)
  27  ד'א  [has-apostrophe] — demonstrative "this" — check ד'ה/הד'א in lane
  27  ולדת  [w-prefixed]   — Batch B target (perfect of ולד "give birth")
  26  חצ'אא  [has-apostrophe] — ?
  22  עליכם  [standard]    — "upon you 2mp" — pronominal suffix variant of עלי
  22  גהה  [standard]      — direction (Saadianic stem)
  21  גמלה  [standard]     — totality/sum (Saadianic stem)
  21  חתא  [standard]      — until/even (particle)
  21  בי  [standard]       — "in/with me" — pronominal of ב
  21  תעמלו  [standard]    — 2mp imperfect of עמל "do/act"
  21  אמץ  [standard]      — find? exert?
  21  פצאר  [standard]     — pa-perfect of צאר "become" (Batch B)
  21  פולדת  [standard]    — pa-perfect of ולדת (Batch B)
```

Several "top miss" tokens are not Saadianic stems but **pronominal-suffix
variants** of preps/pronouns already in lane (בך, בי, עליכם). Round 5 was
designed for the suffix-variant pass — but the highest-frequency cases
might be worth pulling forward into Round 4 if they're easy single-line
additions. Use judgment.

## Goal

Drive **hand-coverage 62.04% → ~66%** (+4 pts realistic) by completing
Batches B (w-prefixed perfects) and C (Saadianic stems missing from lane).

---

## Batch B — w-prefixed verbal perfects (~20 stem additions → ~+1 pt)

**Audit `lib/lookup.ts:lookup` FIRST.** The composable prefix chain
(optional ו → optional one of [ב ל כ פ] → optional אל) strips ו but NOT
פ-when-followed-by-vav-then-stem. So `פולדת` (21) is the fa-perfect of
ולדת. The chain strips פ → "ולדת" → strips ו → "לדת". If neither ולדת
nor לדת is in lane, the token misses.

**Check first:** `python3 -c "import json; d=json.load(open('data/dictionary-lane.json')); print([e['id'] for e in d['entries'] if 'walad' in e['id'] or 'ולד' in (e['lemma_ja'],*e.get('variants',[]))])"`.

**Strategy: identify the verbal root → add stem entry with paradigm
variants** (perfect 3ms/3fs/3pl: -, ת, ו; imperfect: י-, ת-, נ-; masdar;
fa/wa-prefixed perfects).

**Candidate verbs from miss queue** (verify each in context first):

| Miss | Count | Root | Likely meaning |
|---|---|---|---|
| ולדת | 27 | ולד | "she gave birth" (3fs perfect, w-prefixed) |
| פולדת | 21 | ולד | "and-then she gave birth" (fa-perfect) |
| תעמלו | 21 | עמל | "you-2mp will do" |
| פצאר | 21 | צאר | "fa-perfect: and it became" |
| תאכלו | 19 | אכל | "you-2mp will eat" — אכל already in lane; check for missing 2mp variant |
| וקרבו | 16 | קרב | "they drew near" w-perfect 3mp |
| ועאש | 16 | עאש | "and he lived" — עאש (#117) already in lane? |
| פאשתד | 16 | שדד | "and it intensified" (Form VIII pa-perfect) |
| פסמע | 16 | סמע | "and he heard" |
| פבעת | 16 | בעת' | "and he sent" |
| סמעת | 16 | סמע | "I heard" 1s perfect |
| יעמל | 16 | עמל | "he will do" 3ms imperfect |
| גאו | 14 | גי(א) | "they came" 3mp perfect |
| תיאלידהם | 14 | ילד | "their genealogies" — broken plural |
| ואקף | 14 | וקף | "and standing" / "and-he-stood" |
| אקבל | 14 | קבל | "I accept" / "he came/approached" |
| ועאש | 16 | עאש | (already noted) |
| אטלק | 15 | טלק | "he released / declared" Form IV |
| ועאש | 16 | (above) | |
| פליאת | 15 | אתי | "let him bring" (pa-jussive) |
| גרש | 15 | גרש | "he drove out" |
| יפיץ | 14 | פיץ | "he overflows" |

**Workflow:**
1. Refresh misses (already current from Batch A — skip unless dict changed).
2. For each candidate, check the prefix chain trace by hand: does the
   bare stem (after stripping w/f) exist in lane? If yes, add the
   pa-perfect/wa-perfect as an explicit variant on the existing entry.
   If no, add a new stem entry with the full paradigm.
3. Write `/tmp/apply_round4_B.py` using the same pattern as
   `/tmp/apply_round4_A.py` (NEW_ENTRIES + VARIANTS_PATCH dict keyed by
   existing-stem-id).
4. Run, validate JSON, re-run `python3 scripts/coverage_report.py`.
5. Expected: **+0.5–1.0 pts** (the long tail of verbal stems is
   diluted across many low-frequency forms).

**Special check before starting Batch B:** look at whether the lookup
chain actually strips פ when followed by ו+stem. From `lib/lookup.ts`
walk: `for (const stripVav of [false, true]) { for (const prefix of [..., ב, ל, כ, פ]) { for (const stripAl of [false, true]) ... } }`. The
chain SHOULD compose to handle פ+ולדת → strip פ → ולדת → (no ו strip
needed since the chain already considered ו) → לדת. **If `פולדת` keeps
missing despite `ולדת` being in lane, the chain isn't double-stripping.**
Either add `פולדת` as an explicit variant, or audit the chain order.

---

## Batch C — Saadianic stems missing from lane (~30 entries → ~+2–3 pts)

**Highest-value bucket.** From the miss queue:

| Miss | Count | Likely meaning |
|---|---|---|
| אלמחצ'ר | 132 | tent of the assembly (Saadia's אהל מועד) — **saadia_note material** |
| תכלימא | 81 | speech masdar (Sinai dialogue gloss) — **saadia_note** |
| אלמצריון | 68 | Egyptians |
| מר | 67 | to pass (homograph w/ "bitter" — keep separate entries) |
| ועשירה | 54 | clan (Saadia's משפחה) — **saadia_note** |
| הוד'א | 53 | behold this |
| לעשאירהם | 49 | "to their clans" — variant of עשירה |
| אלגמאעה | 49 | assembly |
| ברייה | 29 | creature, creation |
| גהה | 22 | direction |
| גמלה | 21 | totality, sum |
| חתא | 21 | until, even |
| תעמלו | 21 | (verbal — Batch B) |
| אמץ | 21 | seek/exert? — verify |
| פצאר | 21 | (verbal — Batch B) |
| אלגוף | 15 | **inwards/entrails** (Saadia's גוף for קֶרֶב, root j-w-f) — Batch C **not** a place name |
| משזור | 21 | twisted (re: linen) |
| חצ'אא | 26 | ? — verify |
| כ'ארג | 50 | outside (might already be in lane?) |
| טול | 50 | length/throughout (might already be in lane?) |
| אלזי | 44 | relative pronoun variant |
| לוט | 19 | (covered in Batch A) |

**Rules** (per [[scope_saadia_notes]] convention):
- `notes` MUST be cross-text safe — no Saadia/Tafsir mention.
- Saadia-specific commentary → `saadia_note` (rendered only in Tafsir reader, hidden in Advanced reader).
- `scope:"saadia"` ONLY when the primary `gloss_en` IS a Saadia coinage
  (rare — only גלד and מסתבחרה qualify today).
- אלמחצ'ר: `gloss_en` = "tent of the assembly, tabernacle"; `saadia_note`
  = "Saadia's standard rendering of אֹהֶל מוֹעֵד (tent of meeting); compare
  the older רחבת אלאגתמאע — this is his settled later term."
- ועשירה: lemma `עשירה`; `gloss_en` = "clan, extended family";
  `saadia_note` = "Saadia's rendering of Hebrew מִשְׁפָּחָה (family, clan)."
- אלגמאעה: lemma `גמאעה`; gloss_en "assembly, congregation"; no
  saadia_note (this IS standard Arabic, even if Saadia uses it for עֵדָה).

**Workflow:**
1. Refresh misses if dict changed.
2. Write `/tmp/apply_round4_C.py` with NEW_ENTRIES + VARIANTS_PATCH.
3. Run, validate, re-run `coverage_report.py`.
4. **Run `python3 scripts/scope_saadia_notes.py` after Batch C** — catches
   any Saadia-mention that slipped into `notes`. Idempotent.

---

## Per-batch workflow (boilerplate, same as Round 4 origin)

1. **Refresh misses if dict changed:** `python3 scripts/coverage_report.py` (~4 min runtime).
2. **Build `/tmp/apply_round4_X.py`** — declare `NEW_ENTRIES` list (lemma
   + ar + gloss_en + gloss_he + variants + optional saadia_note +
   optional notes) and `VARIANTS_PATCH` dict keyed by stem id (for
   additions to existing entries). Read `data/dictionary-lane.json`,
   merge, write back.
3. **Validate JSON:** `python3 -c "import json; json.load(open('data/dictionary-lane.json'))"`.
4. **Re-run coverage:** `python3 scripts/coverage_report.py`. Confirm
   delta against targets.
5. **Build check at end:** `npm run build` — must stay clean (215+ pages).
6. **No commit.** Working tree stays uncommitted per project pattern.

---

## Verification at end of Round 4

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 65%**
  (stretch ≥ 67%). +3–5 pts over the 61.52% baseline.
- `python3 scripts/verify_divergence.py` exits 0 — divergence untouched
  but reverify to confirm no regression.
- `python3 scripts/scope_saadia_notes.py` clean (no Saadia mentions
  leaked into `notes`).
- `npm run build` clean.
- Spot-check 3 random tafsir chapters in dev (`npm run dev`, visit
  `/tafsir/bamidbar/14`, `/tafsir/devarim/30`, etc., tap on previously-
  missing tokens like `אלמחצ'ר`, `אלגוף`, `הוד'א` and confirm the gloss
  panel now opens — including the "In Saadia's Tafsir: …" italic block
  on `אלמחצ'ר` and `ועשירה`).
- Spot-check 1 Advanced reader page (e.g. `/advanced/rambam-moreh-nevukhim`)
  to confirm `saadia_note` is NOT rendered there.

## Gotchas

- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts:38-44` policy: `אלאה ≠ stem אלא + suffix`).
- **Trailing-apostrophe lemmas** (טאעה' style) will never match — store
  bare `טאעה` and add `'`-suffixed variant if needed.
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note`. The Advanced reader hides `saadia_note` entirely.
- **Homographs are fine** — keep separate entries for `מר` (pass) vs `מר`
  (bitter). The UI shows both on tap.
- **`coverage_report.py` runs ~4 min.** Skip the pre-batch refresh if
  the dict hasn't changed since the snapshot timestamp.
- **The fa-perfect strip** (פ-then-ו-then-stem) — verify chain behavior
  before fighting it; explicit variants are always a safe fallback.

## After Round 4

Round 5 (~66 → ~74% via pronoun-suffix variants — בך, בי, עליכם, מנך,
מנהם, etc., extend `scripts/generate_lane_entries.py` with
`--variants-only` mode). Round 6 (~74 → ~82% via the scripted Sonnet
pass on the long tail). Retire the auto-dict badge once hand ≥ 80%.
Phase 3 (divergences 32 → ~180) and Phase 4 (Word of the Day) run in
parallel on independent files.

---

**Tell Claude:** "Resume Phase 2 Round 4 per `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`. Run Batch B first (audit the pa-perfect chain behavior before adding entries), then Batch C, reporting coverage delta after each."
