# Moreh Nevukhim — plan for the next chunk of Part I (I:29 onward)

Hand-off plan for a fresh session. Pairs with `MOREH-CONTINUATION.md` (the per-chapter build
pattern + gotchas) — read that first; this file is the *what next* and the *new, easier source*.

## Where we are
- **Live: Part I, chapters 1–36** (1–28 the "lexicon of equivocal terms"; **I:29–36 added 2026-06-19**
  from Sefaria's jrb JA — etzev/akhol, then the first essay arc: limits of intellect, restraint,
  teaching-order, the five causes [I:34], incorporeality-is-not-a-secret, anger/idolatry). Plus four
  companion features (Atlas, verse reverse-index, library-wide search, Arabic⇄Ibn-Tibbon). See
  MOREH-CONTINUATION.md. Build clean: 306 static pages, `GATE PASSED`, substring `PROBLEMS: 0`.
- **Part I has 76 chapters** (confirmed via Sefaria: Part 1.76 exists, 1.77 does not). So **40 chapters
  of Part I remain (I:37–76)** — continuous philosophical essays (the divine attributes, negative
  theology, the kalām critique), **denser and longer** than the short lexical chapters 1–28.
- **Next chunk: I:37–40** (panim/achor/lev/ruach — a short lexical cluster, a quick session) or push
  into the attributes essays (I:50 onward). `scripts/fetch_moreh_ja.py` already exists — just widen
  its `range()`. Repeat the exact pipeline below.

## The source problem is solved — use Sefaria's Judeo-Arabic
The on-disk FJMS source (`data-source/rambam-moreh/rambam-moreh.txt`, resourceId 6) only has I:1–28.
**But Sefaria hosts the full Guide in Judeo-Arabic**: version **"Judeo Arabic, Paris, 1856 [jrb]"**
— verified to cover I:29, II:1, III:1, … (the 1856 Paris/Munk Arabic base; **public-domain by age**,
though Sefaria tags the licence "unknown" — sanity-check before a large pull). Fetch it exactly like
the Ibn Tibbon layer was fetched:
```
# mirror scripts/fetch_moreh_tibbon.py, swapping the version title:
vhe = "Judeo Arabic, Paris, 1856 [jrb]"     # the JA original
ref = f"Guide_for_the_Perplexed, Part 1.{N}"  # old API: ...?context=0&vhe=<title>
```
Caveat: this is a **different edition** than the FJMS text used for 1–28 — expect minor orthographic
differences (and Sefaria's own segmentation). That's fine; it's the same work. The fetch only gives
**raw JA segments** — the English translation, phrase-by-phrase pairs, key-term cards, and 100%
dictionary coverage are still **hand-authored per chapter** (that's the real work; see the pattern).

## Recommended next chunk
**I:29–40** (12 chapters) — but these are essays, not lexical entries, so **do fewer if dense**
(6–8 is a reasonable session). Author each into `data/moreh-bab{N}.json` with the `WorkData` shape,
following the I:2–28 pattern in MOREH-CONTINUATION.md verbatim (header segment, terms[], pages[] of
aligned {ja,en,pairs}, gershayim `״` for `י״י`/`ע״אס`, etc.).

## Per-chapter steps (build pattern — see MOREH-CONTINUATION.md for detail)
1. Fetch JA for the chapter from Sefaria jrb (new `scripts/fetch_moreh_ja.py`); use it as the source
   to author `data/moreh-bab{N}.json`.
2. Author EN + JA↔EN `pairs` (verbatim substrings) + 4–8 `terms` cards.
3. **Substring check** → `PROBLEMS: 0` (the python snippet in MOREH-CONTINUATION.md; widen the range).

## After authoring the chunk — re-sync everything (so all features cover the new chapters)
- **Routes/nav:** add entries to `MOREH_CHAPTERS` in `app/advanced/rambam-moreh-nevukhim/chapters.ts`;
  add `import bab{N}` + `DATA["{N}"]` in `[ch]/page.tsx`.
- **Atlas:** add `import bab{N}` + `BY_CHAPTER` entries in `lib/morehTerms.ts` (auto-flows to `/atlas`).
- **Coverage gate:** add `("moreh-bab{N}", …, True, "hebrew")` rows to `TEXTS` in
  `scripts/coverage_advanced.py`; run it; drive `data/dictionary-lane.json` to **`GATE PASSED`**.
  Watch for proper-noun homograph mistakes (run `scripts/audit_dict_homographs.py`; see the m-d-n fix).
- **Regenerate derived data (just rerun — they pick up new chapters):**
  - `python3 scripts/build_moreh_verse_index.py`  (globs `moreh-bab*.json` → `/verses`)
  - `python3 scripts/build_advanced_index.py`      (reads `TEXTS` → library search)
  - extend the chapter range in `scripts/fetch_moreh_tibbon.py` and rerun (Ibn Tibbon layer + `/parallel`)
- **Nav scaling:** the chip row wraps, but past ~40 chapters consider grouping chips or a dropdown
  in `ChapterNav` (`app/advanced/reader.tsx`). Not yet needed at 28.

## Verify → deploy
`PROBLEMS: 0` → `GATE PASSED` → `npm run build` clean → smoke the new chapters (hover, gloss, atlas,
verses footer, Ibn Tibbon toggle). Deploy: `vercel --prod` (uploads working tree) on the user's go-ahead.

## Bonus: this also un-parks Parts II & III
The same Sefaria jrb version covers **all of Parts II and III** in Judeo-Arabic. The earlier blocker
("no JA source on disk") is gone — Parts II/III are now a *fetch + author* program, same pattern,
just denser philosophy. Sequence after Part I, or interleave a "greatest hits" set (II:13 creation,
III:51 the palace parable) if desired.
