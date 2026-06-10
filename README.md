# Judeo-Arabic: A Digital Reader & Lexicon

A reader-first digital edition of medieval Hebrew-script Arabic for Hebrew
readers. It presents Saadia Gaon's Tafsir on the whole Pentateuch and a growing
library of classical prose (Bahya, Maimonides, Halevi, Qirqisani, and more) in
the Judeo-Arabic original, with parallel Hebrew and English and a word-by-word,
tap-to-define lexicon.

Edited by Eli Freedman (Hebrew University, Dept. of Arabic).
Live: https://judeo-arabic-app.vercel.app

## What it does

- **Tafsir reader** (`/tafsir`) — Saadia's Tafsir verse-by-verse against the
  biblical Hebrew. Tap any word for a root / part-of-speech / gloss panel.
- **Foundations** (`/foundations`) — a three-stage path for Hebrew readers:
  the script and diacritics, the Hebrew–/Aramaic–Arabic cognates, and the 50
  highest-frequency words.
- **Advanced library** (`/advanced`) — classical Judeo-Arabic prose with
  parallel translations.
- **Lexicon** (`/lexicon`) — search scaffold over the dictionary + concordance
  (search UI in progress; the same lookup already powers tap-to-define).
- **Methodology & sources** (`/about`) — editorial principles, bibliography,
  and citation/license.

## Data & sources

Everything is static JSON shipped with the app; there is no database.

- `data/dictionary-lane.json` + `data/dictionary-starter.json` — the lexicon
  (~8,700 hand-curated entries: `lemma_ja`, `lemma_ar`, `root`, `pos`,
  English + Hebrew glosses, inflected `variants[]`, Saadia-specific notes).
  Classical glosses paraphrase E. W. Lane, *An Arabic-English Lexicon* (Perseus
  TEI); divergence notes cite Joshua Blau, *A Dictionary of Mediaeval
  Judaeo-Arabic Texts* (Jerusalem, 2006).
- `public/corpus-index.json` — the concordance: every token in the Tafsir
  (~81k instances over all 187 chapters), keyed by normalised form with its
  occurrences `(chapter, verse, surface)`.
- `data/tafsir-{book}-{chapter}.json` (+ `-english`, `-alignment`) — the Tafsir
  text, translation, and line-to-line alignment.
- Library texts (`data/bahya-*`, etc.) from the editions listed on `/about`;
  Judeo-Arabic page images via the Friedberg Jewish Manuscript Society.

## Architecture

- **Next.js 16 / React 19 / Tailwind 4**, deployed on Vercel (serverless;
  `next.config.ts` traces the per-chapter Tafsir JSON into the function).
- **Lexicon engine** — `lib/lookup.ts` resolves any surface form back to its
  lemma through a prefix/suffix candidate chain (handles the `אל`/`ו`/`ב ל כ פ`
  proclitics and final↔medial letter forms). `lib/corpus.ts` is the
  client-side concordance (occurrences, inflected-form breakdown, unique
  verses). `lib/corpusStats.ts` computes build-time headline figures.
- **Design system** — `app/globals.css` defines the scholarly type primitives
  (`.label`, `.display`, `.apparatus`, `.scholarly-table`) and per-script RTL
  metrics; the palette is warm parchment + ink + wine. Fonts: Lora (body),
  Noto Serif Hebrew, Amiri (Arabic).

## Develop

```bash
npm install
npm run dev      # http://localhost:3000
npm run build    # production build
npm run lint
```

## License

Editorial text, translations, glosses, and notes: **CC BY-NC 4.0**. Source
texts and manuscript images remain under the rights of their respective
editions and holding institutions (see `/about`). Corrections welcome —
freedmaneli@gmail.com.
