# Handoff: continue Devarim word-level alignment

Paste the **prompt** below into a new Claude Code session (run from
`/Users/eliyahufreedman/Code/judeo-arabic-app`) to continue the work. Everything
needed is self-contained.

---

## PROMPT (copy from here)

Continue the Devarim tri-lingual word-level alignment for the highlighter in this
repo (`/Users/eliyahufreedman/Code/judeo-arabic-app`). Work on branch
**`devarim-alignment`** (`git checkout devarim-alignment` first).

### What this is
The reader at `/tafsir/<book>/<chapter>` shows Hebrew ↔ Saadia's Judeo-Arabic
Tafsir ↔ English with hover-highlighting. Each chapter has a hand-authored
alignment in `scripts/align_data/devarim_<N>.py` (a plain literal
`ALIGNMENTS: dict[int, list[tuple[str|None, str, str]]]` mapping verse → list of
`(hebrew_or_None, ja, english)` triples), compiled to
`data/tafsir-devarim-<N>-alignment.json` by `scripts/handalign_chapter.py`.

### State (already done — do NOT redo)
Chapters **1–12** are complete and committed on `devarim-alignment`:
A=1,3,5  B=2,4,6  C=7,8,9  D=10,11,12.
**Remaining: chapters 13–34 (22 chapters).**

Verse counts for the remaining chapters:
13:19  14:29  15:23  16:22  17:20  18:22  19:21  20:20  21:23  22:29  23:26
24:22  25:19  26:19  27:26  28:69  29:28  30:19  31:30  32:52  33:28  34:12.
(28 and 32 are the large ones.)

### Workflow (proven this session)
Go in batches of ~3 chapters. For each batch, spawn **one subagent per chapter in
parallel** (model `sonnet`, `general-purpose`), each authoring its
`devarim_<N>.py` and self-validating. Then **you** independently verify and commit
the batch. Suggested next batch: **13, 14, 15**.

Give each subagent this recipe (parameterized by chapter N):

> Create `scripts/align_data/devarim_<N>.py` — a plain literal `ALIGNMENTS` dict
> (no data-file loading), short docstring. Cover ALL verses of chapter N.
> First READ `scripts/align_data/devarim_9.py` and `devarim_6.py` as references,
> plus `data/tafsir-devarim-9.json` + `-english.json` to see input→output.
> Inputs for ch N: `data/tafsir-devarim-<N>.json` (verses[].v/.hebrew/.ja) and
> `data/tafsir-devarim-<N>-english.json` (translations[str(v)]).
> Each triple `(he, ja, en)` in verse V:
>  1. `ja` = verbatim contiguous substring of that verse's `.ja` (group 1–3 JA
>     words that render one unit; ~1 word where natural).
>  2. `he` = verbatim contiguous substring of that verse's `.hebrew` (EXACT
>     niqqud/cantillation + maqaf `־`), or `None` for a Saadia gloss/connective
>     with no Hebrew source.
>  3. `en` = verbatim contiguous substring of that verse's English.
>  4. Walk the JA left-to-right, one triple per unit. The resolver matches each
>     side independently and tolerates word-order crossings — HE/EN need not be
>     in JA order, but each piece must be an exact substring.
>  5. Each source occurrence is claimed once; one Hebrew word → two JA words means
>     group the JA into ONE triple. A Hebrew word that genuinely appears twice in
>     the verse MAY be mapped at each occurrence.
> Quality: map each JA word to the Hebrew it ACTUALLY translates + the English
> that renders it, by meaning not position (scholarly Saadia Tafsir work).
> Gotchas: JA geresh `'` is part of words (verbatim); COPY Hebrew from source
> (don't retype); JA may contain bracketed editorial readings `]word]` (align to
> the clean words, copy any used substring verbatim); use EXACT English wording.
> Validate to the gate, iterating:
> `python3 scripts/handalign_chapter.py --book devarim --chapter <N>` must report
> `... 0 problem(s)`. Then `python3 scripts/validate_alignment.py --book devarim
> --chapter <N>` — its "issues" are EXPECTED word-order-crossing false-positives;
> do NOT chase them. Finally write:
> `python3 scripts/handalign_chapter.py --book devarim --chapter <N> --write`.
> Report verse count, total triples, the final handalign line, and any non-obvious
> judgment calls. Do NOT commit.

### Your verification per batch (don't skip)
1. Re-run the gate yourself: `for c in <chapters>; do python3
   scripts/handalign_chapter.py --book devarim --chapter $c | tail -1; done`
   — every line must say `0 problem(s)`.
2. `npm run build` — must compile clean and prerender all pages.
3. Smoke-test: start `npm run dev`, curl `/tafsir/devarim/<N>` → 200, then stop dev.
4. Spot-check 1–2 verses per chapter (especially any flagged judgment call, the
   liturgical passages, and any verse with bracket `]` artifacts) by dumping the
   triples and reading the HE/JA/EN correspondence for sense.
5. Commit the batch (HE/JA/EN files): message like
   `Align Devarim 13, 14, 15 (word-level, batch E)` with stats, ending with the
   `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` trailer.

### Key facts / gotchas
- **Authoritative gate = handalign's `0 problem(s)`.** `validate_alignment.py`
  crossing "issues" are false-positives (it's stale-monotonic); the runtime
  resolver handles crossings via backward-fallback claim. Trust build + resolver.
- The alignment JSON omits the `he` key when `he` is None (so read with
  `t.get("he")`).
- Bracket `]…]` sequences in some JA verses are pre-existing source/OCR artifacts;
  they already display in the verse text — just align around them.
- Don't touch `scripts/align_data/bamidbar_7.py` here — its phrase-level fix lives
  on a separate branch `fix/bamidbar-7-phrase-alignment` (off `main`), unrelated.

### When Devarim is finished (all 34)
Consider pushing `devarim-alignment` and opening a PR. Optionally merge to `main`
(Vayikra + Bamidbar word-level are already on main per project memory).

## END PROMPT
