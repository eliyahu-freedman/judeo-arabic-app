# Moreh Nevukhim reader — continuation guide

Hand-off note for resuming the Guide (Dalālat al-Ḥāʾirīn / Moreh Nevukhim) Advanced-library
reader in a fresh session. Last updated 2026-06-19.

## Features built on Part I (2026-06-19, second session) — NOT yet committed/deployed
Four "never-been-done" companion features on the 28 chapters, each shipping-clean (`npm run build`
→ 290 static pages; coverage gate still `GATE PASSED`):
1. **Atlas of God-language** — `/advanced/rambam-moreh-nevukhim/atlas`; aggregates all 123 term
   cards via `lib/morehTerms.ts` (`getAtlasTerms`).
2. **"Maimonides on this verse" reverse verse-index** — `/verses`; built by
   `scripts/build_moreh_verse_index.py` → `data/moreh-verse-index.json` (26 books, 239 verses, 272
   citations). Per-chapter "Scripture cited" footer = `VersesCited.tsx`; outbound links to Sefaria
   (per verse) + AlHaTorah commentators (per chapter).
3. **Library-wide lemma search** — extended the Tafsir-only engine: `scripts/build_advanced_index.py`
   → `data/advanced-index.json` (7.3 MB, keyed by normalizeToken; Moreh + Bahya + Saadia + Qirqisani
   + Kuzari). `lib/lexicon.ts` `getLemma` now returns a `library` field; `/lexicon/[key]` shows an
   "Across the library" cross-author panel.
4. **Arabic ⇄ Ibn Tibbon parallel view** — `/[ch]/parallel`; Ibn Tibbon Hebrew fetched by
   `scripts/fetch_moreh_tibbon.py` → `data/moreh-tibbon.json` (public domain, via Sefaria).
   Al-Ḥarizi deferred (no clean source yet). Chapter-level alignment, not phrase-by-phrase.
- Companion links live in the reader's `ChapterNav` aux row (`ReaderNav.aux`, set in `buildMorehNav`).
- **Regenerate** any data: rerun the three scripts above. **Parts II–III remain parked** (no JA source).

## Dictionary quality — proper-noun homographs (2026-06-19)
`אלמדן` in I:2 was glossing as "Medan" (proper noun) when it means *city* — the lexicon was harvested
from the Tafsir, where `מדן`/`מדין` are the names Medan/Midian, and `lookup()` is context-free. Fixed:
added the *city* sense for the `מדן` skeleton and pruned over-broad variants off proper-noun entries,
**moving** homeless verb forms to their correct common entries first so word-tap coverage never drops
(`scripts/fix_propernoun_homographs.py`, one-shot). Reusable check: `scripts/audit_dict_homographs.py`
lists proper-noun↔common collisions and flags over-reach (7 remaining are legit homographs left alone —
Hittite/until, and-Gad/he-found, book/journey). Coverage gate still `GATE PASSED`.

## Where things stand

- **Live: all of Part I, chapters 1–28 — Part I is now COMPLETE.** I:1 pre-existing; I:2–I:14
  added 2026-06-19; **I:15–I:28 added 2026-06-19** with the full treatment (working-draft English,
  phrase-by-phrase JA↔EN hover, per-chapter key terms, 100% hand-dictionary coverage). No QC pass
  on I:15–I:28 (drafted from the JA, citations by hand — the user's standing choice).
- **I:15–I:28 are NOT yet committed** (the `moreh-guide-i2-i14` branch @ `1088f93` only holds
  I:2–I:14; repo has no GitHub remote). New files: `data/moreh-bab15.json … moreh-bab28.json`,
  ~274 new `data/dictionary-lane.json` entries, wired in `[ch]/page.tsx` + `chapters.ts` +
  `scripts/coverage_advanced.py`. Verified: substring check `PROBLEMS: 0`, coverage `GATE PASSED`,
  `npm run build` clean (all 27 dynamic chapters prerender). **Not merged, not pushed, not
  deployed** — awaiting the user's go-ahead (deploy = `vercel --prod`).
- **Note — I:28 is truncated in the source.** `rambam-moreh.txt` breaks off mid-sentence inside
  I:28 (the closing remark on Onkelos only negating corporeality); the chapter is built through the
  last complete clause, flagged in its `intro`. A fuller I:28 needs a fresh scrape.
- `qc/` is **intentionally untracked** — it holds `gl-reference-i2-4.txt`, an extract of the
  copyrighted Goodman/Lieberman (2024) translation, plus `moreh-i2-4-qc.md` (an accuracy QC of
  I:2–4 against it; it found only 2 minor biblical-citation slips, which the user chose to leave).

## Source on disk

`data-source/rambam-moreh/rambam-moreh.txt` — FJMS resourceId 6, **Part I only** (intro +
chapters 1–28, 40 pages, I:28 truncated mid-chapter). Page breaks marked `[עמוד: N]`; chapters
marked `פצל`/`פרק. <heb-num>.`. **All of Part I (I:1–28) is now built.** Everything past I:28
(the tail of I:28 included), and all of Parts II–III, would need a fresh scrape (see "Going further").

## The build pattern (repeat per chapter)

Author directly from the JA (these chapters were NOT made with the Bahya align-workflow — they're
hand-authored to match `data/moreh-bab1.json`'s register and schema). For each chapter:

1. **Create `data/moreh-bab<N>.json`** with the `WorkData` shape (see `app/advanced/reader.tsx`):
   top-level `work / section / section_ja / subtitle / author / english_translator / intro /
   source`, a `terms[]` array (4–8 key-term cards: `id, ja, translit, gloss, note, variants`),
   and `pages[]`, each `{ page_he, aligned[] }`. Each aligned segment is
   `{ ja, en, isHeader?, pairs[] }`. The first segment of page 1 is the `isHeader: true` title.
   - Assign each segment to the page where it **begins** (`page_he` from the `[עמוד: N]` markers).
   - `pairs` are JA↔EN phrase pairs in **JA order**; they drive the hover highlighter
     (`lib/alignment.ts:resolveVerseAlignment`). **Every `pairs[].ja` and `pairs[].en` must be a
     verbatim substring of that segment's `ja`/`en`.**
2. **GOTCHA — abbreviations**: render `י"י`, `ז"ל`, `ע"אס` with the **Hebrew gershayim U+05F4 `״`**
   (i.e. `י״י`), never ASCII `"`. The tokenizer (`lib/tokenize.ts`) treats `"` as a separator and
   would shatter the abbreviation into single letters (breaking coverage); `״` is a word char.
   Keep ASCII apostrophe `'` for letter-geresh (`ג'`, `ט'`) and for `וכו'`.
3. **GOTCHA — substring breakage**: the recurring failure is a pair whose `en` ends in a closing
   quote where the segment has `.'` or `,'` (drop the trailing quote from the pair), or a biblical
   citation `(Gen 3:6)` interrupting an English run (trim the pair to the contiguous part, or keep
   the citations inside the pair so it stays contiguous). Validate before doing anything else:

   ```bash
   cd ~/Code/judeo-arabic-app && python3 - <<'PY'
   import json
   probs=0
   for n in range(15,29):            # adjust range to the chapters you authored
       ch=f"moreh-bab{n}"
       d=json.load(open(f"data/{ch}.json"))
       for pg in d["pages"]:
           for s in pg["aligned"]:
               if s.get("isHeader"): continue
               for p in s.get("pairs",[]):
                   if p["ja"] not in s["ja"]: print(ch,"JA",p["ja"]); probs+=1
                   if p["en"] not in s["en"]: print(ch,"EN",p["en"]); probs+=1
   print("PROBLEMS:",probs)
   PY
   ```

4. **Coverage to 100%**: add `("moreh-bab<N>","moreh-bab<N>.json",True,"hebrew")` to the `TEXTS`
   list in `scripts/coverage_advanced.py`, then `python3 scripts/coverage_advanced.py`. For each
   miss, add a dictionary entry to `data/dictionary-lane.json`. **The foolproof rule**: list the
   exact missing surface form as a `lemma_ja` or in `variants` — the lookup candidate chain always
   includes the token itself (final-normalized), so that guarantees a match. The chain strips
   prefixes only **one level** (`ו`, `אל`, single-letter `ב/ל/כ/פ`), so e.g. `פבאלעקל` won't reduce
   to `עקל` — include such forms explicitly. Entry shape: `{id, lemma_ja, lemma_ar?, gloss_en,
   gloss_he, variants?, source:"lane", notes}`. Hebrew/Aramaic quote-words get no `lemma_ar`.
   - A throwaway batch script (define `[(id, ja, ar|None, en, he, [variants])]`, validate all misses
     are covered against `candidate_chain`, then `--write` to append) is the efficient way; the two
     used on 2026-06-19 were deleted after running. Re-run the gate → expect `GATE PASSED`.

5. **Routes**: nothing to add per chapter — the dynamic route already covers any chapter present in
   its `DATA` map. To expose new chapters: in `app/advanced/rambam-moreh-nevukhim/[ch]/page.tsx`
   add the `import bab<N>` + a `DATA["<N>"]` entry, and add the chapter to `MOREH_CHAPTERS` in
   `app/advanced/rambam-moreh-nevukhim/chapters.ts` (with a concise chip title `I:<N> · <topic>`).
   I:1 stays at the bare `page.tsx`. `buildMorehNav` and `ChapterNav` need no changes.
   - **Nav scaling**: the chip row already wraps; past ~20 chapters consider grouping the chips or a
     dropdown. Not yet needed.

6. **Verify**: substring check (step 3) → coverage gate (`GATE PASSED`, all 100%) → `npm run build`
   (chapters prerender; bare I:1 still resolves; out-of-range `/<n>` 404s) → optional dev smoke
   (`npm run dev`, load a couple chapters, confirm hover + tap-gloss + active nav chip).

## Optional QC against Goodman/Lieberman

The 2024 Stanford translation PDF is at
`~/Downloads/Academic/Jewish-Studies/General/The Guide to the Perplexed- A New Translation.pdf`
(selectable text; Part I chapters sit ~lines 3456–3840 of `pdftotext -layout` output, anchored by
"Chapter N" body headings — numbering matches ours). The user has so far chosen **no QC pass** on
new chapters (draft from JA, keep citations accurate by hand). If asked: extract the relevant
chapters, compare segment `en` vs G/L for genuine accuracy errors only (mistranslation, missed
negation, wrong/misattributed citation), and write a REVISION_SHEET-style review to `qc/` — report
first, edit only on approval. Keep `qc/` untracked (copyright).

## Going further (I:29–76, and Parts II–III) → see MOREH-NEXT-CHUNK-PLAN.md

**Next session: build the next chunk of Part I (I:29 onward).** Part I has **76 chapters**; we have
1–28. **The source is no longer a blocker:** Sefaria hosts the full Guide in Judeo-Arabic — version
**"Judeo Arabic, Paris, 1856 [jrb]"** (public-domain by age) — covering I:29–76 **and all of Parts
II–III**. Fetch it via the Sefaria API exactly like the Ibn Tibbon layer (`scripts/fetch_moreh_tibbon.py`),
swapping the version title. The full step-by-step (recommended chunk I:29–40, per-chapter pattern,
and the feature re-sync checklist) is in **`MOREH-NEXT-CHUNK-PLAN.md`**. The old FJMS-scrape route is
superseded for this purpose.

## Quick commands

```bash
source ~/.nvm/nvm.sh && cd ~/Code/judeo-arabic-app
npm run dev                                   # http://localhost:3000
python3 scripts/coverage_advanced.py          # 100% gate for all Advanced texts
npm run build                                 # typecheck + prerender
git log --oneline -3                          # branch moreh-guide-i2-i14 @ 1088f93
```

## Open decisions for the user
- **Commit I:15–I:28** (currently uncommitted working-tree changes), merge to `main`, set up a
  GitHub remote + push (none exists yet), and **deploy** (`vercel --prod`).
- **Next scope (all needs scraping more of FJMS resourceId 6):** the full text of I:28 (truncated
  on disk), then **Part II / Part III**, or a curated cross-Guide selection. Ask before a large batch.
- Optional: a QC pass on I:15–I:28 against Goodman/Lieberman (the user declined for this batch).
