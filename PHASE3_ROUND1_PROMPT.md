# Phase 3 Round 1 — Blau-first divergence mining (target 32 → ~60 entries; clear Bereshit warning)

Paste-ready prompt for a fresh Claude Code session. Pivots the divergence
workstream from *verse-first* hand-picking to *Blau-first* dictionary
mining. Runs on `~/Code/judeo-arabic-app/`.

---

## Context (read first)

This is the **divergence-set** thread (`data/tafsir-divergence.json`),
distinct from the Lane-dictionary thread (Rounds 4–7 + the queued R8).
Both can run independently — they share helper scripts but write to
different data files.

- Phase 2 round prompts (Lane dict — done R4–R7, R8 queued):
  - `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`
  - `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`
  - `~/Code/judeo-arabic-app/PHASE2_ROUND5_PROMPT.md`
  - `~/Code/judeo-arabic-app/PHASE2_ROUND6_PROMPT.md`
  - `~/Code/judeo-arabic-app/PHASE2_ROUND7_PROMPT.md`
  - `~/Code/judeo-arabic-app/PHASE2_ROUND8_PROMPT.md`
- Memory: `judeo-arabic-app-project.md` — search for "divergence" and
  "Phase 2 Round 7" sections.
- Plan that produced this prompt:
  `~/.claude/plans/write-a-prompt-for-sprightly-nebula.md`.

## Why we're shifting strategy

**Today's approach is verse-first.** Read a verse, notice that Saadia
chose an unusual Arabic word, back-check whether Blau's Dictionary
attests the same sense. This is how the existing 32 divergence entries
were authored — slowly, one verse at a time, with the curator deciding
what to flag.

**The new approach is Blau-first.** Yehoshua Blau spent his career
documenting exactly the kind of Saadia-specific semantic moves that this
divergence file is trying to capture. Of Blau's 6,736 dictionary entries,
**1,596 explicitly cite Saadia's Tafsir** (24% of his whole dictionary)
— and we've turned 15 of those into divergence entries. That's <1% of
the Blau-Saadia evidence the dictionary already gathers.

Mining Blau directly for Saadia-citing entries flips the workflow:
**Blau already did the hard work of identifying which Saadia choices are
lexicographically interesting.** Our job becomes (a) extract those
candidates, (b) verify the lemma actually surfaces in the tafsir we
display, (c) write the entry. The Blau backing is automatic; the
quality-bar warnings should clear by construction.

This round is **Phase 3 Round 1** — the first round of the mining
pipeline. Subsequent rounds repeat the loop on the remaining Blau
remainder.

## Current divergence state (verified 2026-05-28)

- **32 entries total** — 31 Bereshit + 1 Devarim (`גוהר`, the tablets-of-substance entry).
- Backing distribution: **15 direct / 6 adjacent / 2 different-sense / 9 no-citation.**
- `verify_divergence.py` emits one warning: **Bereshit Blau-backed = 20/31 = 65% < 70% threshold.** The script enforces ≥70% backed + ≥45% direct + ≤30% no-cite per book with ≥5 entries.
- The `/about/blau` public-tally page was deleted in commit `a214f70`. The verifier is the only quality signal now.

**The 9 no-cite Bereshit entries** (deserve a re-audit pass — see Bereshit-warning sidetask below):

| lemma_ja | verse | mechanism |
|---|---|---|
| מסתבחרה | Ber 1:2 | Saadianic coinage for בֹהוּ — "vast like a sea" |
| ריאח | Ber 1:2 | "winds" (pl.) for רוּחַ אֱלֹהִים — anti-anthropomorphic |
| תהב | Ber 1:2 | pair with ריאח — "blows" |
| אטג'אני | Ber 3:13 | deception recast as moral transgression |
| אשראף | Ber 6:2 | "nobility" for בְּנֵי הָאֱלֹהִים — anti-mythological |
| שמשאר | Ber 6:14 | boxwood for גֹּפֶר |
| קרדא | Ber 8:4 | Qardū identification for אֲרָרָט |
| קרבאן | Ber 8:21 | "offering" for רֵיחַ הַנִּיחֹחַ — double anti-anthropomorphism |
| אתון | Ber 11:28 | Babylonian "furnace" identification for אוּר כַּשְׂדִּים |

These are not bad entries — they're entries written when "no Blau citation
found yet" was the honest answer. Some of these probably ARE in Blau and
just weren't searched at authoring time. The Phase 3a mining will likely
surface several of them with proper backing.

## Pipeline architecture: Mine → Curate → Apply

Three stages, each with its own script. Mirrors the R7 chunk pattern but
prefixed with a one-time mining step.

### Phase 3a — Mine Blau for Saadia citations (script-driven)

Author `scripts/mine_blau_saadia_candidates.py`. Queries the local Blau
dictionary at `~/Tools/arabic-lexicon/lex.sqlite` for every entry that
cites Saadia's Tafsir, then dumps a candidate list.

**SQL shape:**

```python
import sqlite3
conn = sqlite3.connect(str(pathlib.Path.home() / "Tools/arabic-lexicon/lex.sqlite"))
cur = conn.cursor()
# Hebrew abbreviation patterns Blau uses for Saadia:
#   סעדיה, רס״ג (with gershayim), רס"ג (with straight quotes), רסאג, סעדיה גאון
rows = cur.execute("""
    SELECT id, root_ar, root_norm, body
    FROM entries
    WHERE dict='blau' AND (
        body LIKE '%סעדיה%' OR
        body LIKE '%רס״ג%' OR
        body LIKE '%רס"ג%' OR
        body LIKE '%רסאג%'
    )
""").fetchall()
```

Expected scale: ~1,596 raw matches (verified). Some are general "Saadia
uses this word here" notes; the curator pass (3b) filters to the
~30–80 that represent genuine semantic divergences.

**Output schema** — write to `data/_blau_saadia_candidates.json`
(underscore prefix marks it as a build-time scratch file, like the
`_lane_frag_*.json` and `_misses_block_*.json` already in `data/`):

```json
{
  "_generated": "2026-05-XX",
  "_source": "Blau Dictionary 2006 via ~/Tools/arabic-lexicon/lex.sqlite",
  "_total": <count>,
  "candidates": [
    {
      "blau_id": <int>,
      "root_ar": "<root from blau, e.g. غمر>",
      "lemma_ar": "<headword, e.g. غامرة>",
      "lemma_he": "<JA equivalent if Blau lists it, e.g. גאמרה>",
      "blau_body_excerpt": "<first 400 chars of the Blau entry body>",
      "saadia_citation_text": "<the actual ...סעדיה... sentence(s) extracted>",
      "hebrew_lemma_referenced": "<Hebrew biblical word Saadia is glossing, if Blau names it>",
      "possible_verses": ["<book ch:v references Blau cites, parsed if present>"]
    }
  ]
}
```

The script should be **re-runnable** (overwrites the output file). Spot-check
3–5 candidates by hand after first run to confirm the extraction is sensible.

### Phase 3b — Curator pass (inline-Opus, R7-style)

Walk the candidate file. For each candidate, decide:

1. **Does the JA token surface in the tafsir corpus?**
   Use `/tmp/ja-context-index.json` (rebuild via
   `python3 scripts/build_ja_context_index.py` if missing). If the lemma
   doesn't appear in any Pentateuch verse — skip; we can't gloss what we
   don't display.

2. **Is the Saadia sense genuinely distinct from classical Lane?**
   Many Blau citations are just "Saadia uses standard Arabic word X for
   Hebrew Y" — that's vocabulary, not divergence. A divergence requires
   that Saadia's choice carries a sense classical Arabic doesn't (calque,
   philosophical gloss, anti-anthropomorphism, coinage, midrashic
   identification). Lane check: search `~/Tools/arabic-lexicon/cli.py
   lookup <root>` or `search <lemma> --dict lane`.

3. **Author the entry.** Use the canonical schema (see "Schema cheat
   sheet" below). Set `blau_dict.relation` to:
   - `"direct"` — Blau's Dictionary's own gloss IS the Saadia sense
     being claimed. (E.g. existing `אדלג`: Blau cites Saadia at She 8:16
     for the شَهَر/أَدْلَج semantic shift.)
   - `"adjacent"` — Blau attests the root and a related sense; not
     identical, but in the same semantic neighborhood. (E.g. existing
     `חאכמא`: Blau has حكم Form III "to judge," our claim is the
     circumstantial-accusative usage.)
   - `"different-sense"` — Blau attests the root but a clearly different
     lexeme or sense. Rare; usually means we should reconsider whether
     the entry is well-founded.

4. **Decide what to skip.** A "not actually a divergence" candidate is
   not a failure — it's the filter doing its job. Aim for 30–80 curated
   entries from the ~1,596 raw mining hits.

### Phase 3c — Apply (R7-style script)

Author `scripts/apply_phase3_round1.py` mirroring
`scripts/apply_round7_I_chunk3.py` but pointing at
`data/tafsir-divergence.json` instead of the Lane dict. Single bucket:

```python
NEW_ENTRIES = [
    {
        "lemma_ja": "...",
        "lemma_ar": "...",
        "root": "...",
        "classical_en": "...",
        "classical_he": "...",
        "saadia_en": "...",
        "saadia_he": "...",
        "mechanism": "...",
        "verses": [{"book": "Bereshit", "ch": <int>, "v": <int>}],
        "sources": ["lane", "saadia-direct", "blau-dict"],
        "blau_dict": {
            "root": "<arabic root, e.g. غمر>",
            "sense": "<verbatim or near-verbatim Blau gloss with citation>",
            "relation": "direct"  # or "adjacent" / "different-sense"
        },
        # optional:
        "variants": ["..."],
        "blau_festschrift": { ... }  # only if Blau's 1992 Festschrift article also covers it
    },
    # ... 20-40 more
]
```

Apply pattern from R7 chunk 3 (lane bucket only — no STARTER twin):
append entries that aren't already present (by `lemma_ja` + first verse
ref), JSON round-trip validate, report deltas.

**Caps to enforce in the apply script:**
- Don't add an entry whose `verses[0]` lemma isn't actually findable in
  the corpus via the lookup chain. Reuse the `normalizeFinals` +
  prefix-strip logic from `lib/divergence.ts` (or `lib/lookup.ts` — same
  chain).
- Don't accept `sources[]` keys not listed in `_sources`. The current
  legend has 4 keys: `lane`, `saadia-direct`, `blau-dict`,
  `blau-festschrift`. Add new keys to `_sources` before referencing them.

## Schema cheat sheet (from `lib/divergence.ts:4–51`)

Required fields: `lemma_ja`, `lemma_ar`, `root`, `classical_en`,
`classical_he`, `saadia_en`, `saadia_he`, `mechanism`, `verses[]`,
`sources[]`.

Optional: `variants?: string[]`, `blau_dict?: { root, sense, relation }`,
`blau_festschrift?: { page, lemma_he, relation, note }`.

`verses[].book` uses **capitalized** book names ("Bereshit", "Shemot",
"Vayikra", "Bamidbar", "Devarim") in the JSON — mirrors the existing
entries. (Note this is opposite of the lane-dict convention; don't unify.)

`blau_dict.relation` enum: `"direct" | "adjacent" | "different-sense"`.
`blau_festschrift.relation` enum: `"direct" | "same-verse-different-lexeme" | "parallel-pattern"`.

Sample entry (Ber 1:2 `גאמרה`, direct-Blau):

```json
{
  "lemma_ja": "גאמרה",
  "variants": ["ג'אמרה"],
  "lemma_ar": "غامرة",
  "root": "غ-م-ر",
  "classical_en": "covering, overwhelming (esp. of deep water)",
  "classical_he": "מציף, מכסה (בדרך כלל לתיאור מים עמוקים)",
  "saadia_en": "submerged, flooded — used to render תֹהוּ (\"chaos / formless\")",
  "saadia_he": "מוצף, שטוף מים — מתרגם תֹהוּ",
  "mechanism": "interpretive: Saadia reads primordial chaos as primordial water, not nothingness",
  "verses": [{"book": "Bereshit", "ch": 1, "v": 2}],
  "sources": ["lane", "saadia-direct", "blau-dict"],
  "blau_dict": {
    "root": "غمر",
    "sense": "abyss / תהום (Blau attests غمر as a JA noun meaning \"abyss\", citing Saadia on Tehillim 129:7)",
    "relation": "direct"
  }
}
```

## Bereshit-warning sidetask (re-audit the 9 no-cite entries)

Whether Phase 3a mining clears the warning organically or not, the 9
no-cite Bereshit entries (listed above) deserve a re-audit pass. For
each:

```bash
python3 ~/Tools/arabic-lexicon/cli.py search "<lemma>" --dict blau
# Also search the Arabic root form:
python3 ~/Tools/arabic-lexicon/cli.py search "<root>" --dict blau
```

If Blau backs the claim, add a `blau_dict` object to the existing entry
(via a small variant patch script or by editing the JSON in place).
If Blau doesn't back it, the entry stands as a "saadia-direct"-only
reading — those are legitimate but they count against the 70% bar, so
we may need to either accept the warning or drop a weak entry.

Bundle this into Round 1 if mining time allows; otherwise queue for
Round 2.

## Per-batch workflow

1. **Mine** — `python3 scripts/mine_blau_saadia_candidates.py`
   (one-time per round; re-run if Blau dict updated).
2. **Build context index if missing** — `python3 scripts/build_ja_context_index.py`.
3. **Curate** — author entries inline against the candidate file.
   Preflight: check each proposed `lemma_ja` against existing
   divergence entries to avoid dupes:
   ```python
   d = json.load(open('data/tafsir-divergence.json'))
   existing = {e['lemma_ja'] for e in d['entries']}
   ```
4. **Apply** — `python3 scripts/apply_phase3_round1.py`. JSON round-trip validate.
5. **Verify** — `python3 scripts/verify_divergence.py` must report
   `1 WARNING` or fewer (zero if Bereshit ratio cleared).
6. **Build check** — `npm run build` clean (213+ pages).

## Verification at end of round

- `python3 scripts/verify_divergence.py` reports **zero warnings** (Bereshit
  cleared to ≥70% backed) OR a documented reason the warning persists.
- `python3 scripts/scope_saadia_notes.py` reports 0 residual hits (this
  is the Lane-dict audit but cheap to re-run).
- `npm run build` clean.
- Lookup spot-check via a one-off `scripts/_spot_check_phase3.ts` (write,
  run via `npx tsx`, delete) — confirm 5–10 newly-added divergent tokens
  resolve via `lookupDivergence`.
- Spot-check 2–3 chapters in dev (`npm run dev`):
  - At least one chapter that already had a divergence entry pre-R1
    (regression check)
  - At least one chapter with a new R1 entry (forward check)
  - At least one chapter still WITHOUT any divergence entries (sanity:
    Advanced toggle should render nothing extra)

## Gotchas

- **`_sources` legend gates `sources[]`** — verify_divergence.py rejects
  source keys not in the legend. Add new keys to `_sources` BEFORE the
  first entry that uses them.
- **`verses[]` is the only lookup key.** Every entry must cite real
  biblical verses where the lemma actually appears. Bad cites are caught
  by `verify_divergence.py` (citation checks pass currently).
- **Blau citation ≠ divergence.** Many of Blau's 1,596 Saadia-citing
  entries just record "Saadia uses standard Arabic word X for Heb Y" —
  that's vocabulary, not divergence. The curator must filter for genuine
  semantic shifts (calque, philosophical, anti-anthropomorphic, coinage,
  midrashic identification).
- **`verses[].book` capitalization** — divergence JSON uses
  "Bereshit"/"Shemot"/etc. (capitalized); lane-dict uses lowercase.
  Don't unify; mirror the existing divergence convention.
- **Don't conflate Phase 2 and Phase 3.** They share helpers
  (`build_ja_context_index.py`, `verify_divergence.py`) but target
  different files. Phase 2 writes `data/dictionary-*.json`; Phase 3
  writes `data/tafsir-divergence.json`.
- **`/about/blau` page was deleted.** Don't try to update or restore
  it as part of this round. If the user later wants to restore the
  public tally, that's a separate task.
- **Trailing-apostrophe gotcha** (carried from R7): `stripPunct` in
  `lib/divergence.ts` strips trailing `'`, so a tā'-marbūṭa lemma like
  `טאעה'` will never match — must be `טאעה`. Mid-word apostrophes
  (`כ'טאך`, `אטג'אני`) are unaffected.
- **Existing entries to watch when adding adjacent senses:** `גאמרה`
  (חז'-מ-ר, abyss/cover); `אדלג` (د-ل-ج, dawn-rising); `חאכמא` (ح-ك-م,
  decree/judge). If your new entry shares a root, link the senses via
  `notes` or `mechanism` rather than creating a near-duplicate.

## After Phase 3 Round 1

- **If we land ~30 entries:** divergence count goes 32 → ~60. Bereshit
  warning likely clears (assuming several mining hits land in Ber 1–11
  with direct backing). The "180-entry target" mentioned in Round 7
  memory is then within ~2–3 more rounds.
- **Phase 3 Round 2** repeats Mine→Curate→Apply on the remaining Blau
  candidates not picked up in R1. Mining is incremental: the candidate
  file persists, R2 just walks deeper into it.
- **Phase 2 Round 8** (Lane dict, queued) can run independently — both
  threads share `build_ja_context_index.py` but write to different
  files. They don't conflict.
- **Restoring `/about/blau`** is a possible standalone task once the
  divergence count justifies a public counter again. The deleted page
  had dynamic recomputation from the data file — it would just need to
  be re-added (look at commit `a214f70` for the deleted content).

---

**Tell Claude:** "Resume Phase 3 Round 1 per
`~/Code/judeo-arabic-app/PHASE3_ROUND1_PROMPT.md`. Start with Phase 3a
(write and run `scripts/mine_blau_saadia_candidates.py`), then walk the
candidate file inline (Phase 3b) and author 20–40 new divergence entries
via `scripts/apply_phase3_round1.py` (Phase 3c). Bundle the
Bereshit-warning re-audit on the 9 no-cite entries if time allows.
Verify with `verify_divergence.py` (target: zero warnings) and
`npm run build`."
