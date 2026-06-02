# Devarim word-level alignment — paste-ready session prompt

Continue the Devarim word-level trilingual (HE↔JA↔EN) alignment of the Saadia Tafsir in
`~/Code/judeo-arabic-app`. Do a SMALL batch this session — do NOT attempt the whole book; that
burned huge tokens and hit the daily session limit last time.

## WHAT THIS IS

Hover-alignment where each JA (Saadia) word is its own triple linked to the Hebrew word it renders +
its English. The resolver `lib/alignment.ts` is already global and backward-compatible — this is
PURELY data authoring, NO code changes.

## BRANCH

Work on `devarim-alignment`. It diverged before the Bamidbar merge, so FIRST (one-time):

```
git checkout devarim-alignment && git rebase main
```

The changesets touch disjoint files (`devarim_*` vs `bamidbar_*`), so the rebase is conflict-free.
Skip if already rebased (i.e. `git merge-base --is-ancestor main devarim-alignment` is true).

## DONE SO FAR

Chs 1, 3, 5 (committed). Confirm remaining by checking which
`data/tafsir-devarim-N-alignment.json` files are missing.

## THIS BATCH

Pick up to 3 chapters, in priority order:

1. WIP drafts that exist but aren't validated/committed: `scripts/align_data/devarim_{6,7,8,9}.py`
   (drafted, have unresolved problems — FIX, don't rewrite from scratch).
2. Then the lowest-numbered chapter with no `.py` yet: 2, 4, 10, 11, … 34.

## AGENTS

One Sonnet agent per chapter, MAX 3 concurrent.

- NEVER use Haiku — last time it fabricated success (reported word-level counts while the `.py`
  was byte-identical to clause-level). NEVER run 9+ at once — that hit the session limit.

Each agent, for its chapter N, must:

- Read the gold standard `scripts/align_data/bamidbar_18.py` BEFORE authoring.
- Read sources `data/tafsir-devarim-N.json` (he+ja) and `data/tafsir-devarim-N-english.json`.
- Author/fix `scripts/align_data/devarim_N.py` exporting
  `ALIGNMENTS: dict[int, list[tuple[he|None, ja, en]]]`.
  One JA word per triple; split across word-order crossings; `he=None` for words Saadia added
  with no Hebrew counterpart; he/ja/en must EACH be a verbatim, non-overlapping substring of
  its source side, in left-to-right order. Maqaf = ASCII `-`, JA geresh = ASCII `'`. Copy OCR
  artifacts verbatim. Respect source verse gaps — don't invent verses.
- Validate: `python3 scripts/handalign_chapter.py --book devarim --chapter N` → iterate to 0 problems.
- `python3 scripts/check_alignment_semantics.py --book devarim --chapter N` → no `!!MISS`; eyeball
  for wrong-occurrence mappings.
- GRANULARITY SELF-CHECK: report avg triples/verse; must be ~>4 (clause-level is ~2). This is
  what catches the Haiku no-op failure mode.
- `python3 scripts/handalign_chapter.py --book devarim --chapter N --write` to emit
  `data/tafsir-devarim-N-alignment.json`.
- Report: chapter, avg triples/verse, "0 problems" confirmed, "no MISS" confirmed.

## DO NOT TRUST `validate_alignment.py`

It's the old monotonic-cursor checker and flags legitimate word-order crossings as false problems on
word-level data. Use `handalign` + `check_alignment_semantics` ONLY.

## AFTER agents return

Independently verify each (don't trust the report): re-run `handalign` and a granularity check on
each chapter's written json. Then commit each chapter SEPARATELY:

```
git add scripts/align_data/devarim_N.py data/tafsir-devarim-N-alignment.json
git commit -m "Devarim N: word-level alignment"
```

Add ONLY those two paths per chapter — the working tree has unrelated untracked WIP
(`app/advanced/*`, `data/_lane_frag_*`, `data/_misses_block_*`) that MUST stay uncommitted.

## FINISH

Run `npm run build` (must pass — prerenders all chapters). Report which Devarim chapters are now
done and how many of {2,4,6–34} remain. Stop after this batch; don't roll into more.

---

The detailed authoring lore lives in memory `judeo-arabic-tafsir-alignment.md` — this prompt is the
condensed, paste-ready version. Cadence: ≤3 chapters/session ⇒ ~10–11 sessions to finish the
remaining 31 chapters.
