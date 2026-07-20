# A Judeo-Arabic Reading Platform — Technical Overview & Collaboration Note

**For:** the Sefaria engineering & scholarship teams
**From:** Eli Freedman — freedmaneli@gmail.com
**Date:** 2026-06-05

This is a short, candid tour of a working web app for learning to *read* medieval
Judeo-Arabic — Saadia Gaon's Tafsir, Bahya's *Duties of the Heart*, Maimonides' *Guide*,
Halevi's *Kuzari*, Qirqisani's *al-Anwār* — and of the few pieces of it that I think are
genuinely novel and might be useful to Sefaria. It ends with a concrete collaboration ask.

Stack: **Next.js 16 / React 19 / Tailwind 4**, deployed on Vercel. Text data ships as bundled
JSON; readers are server-rendered. No database — the "intelligence" is in hand-curated data
plus a small, deterministic lookup/alignment layer.

---

## 1. Layered tap-to-define — Lane for the language, Blau for the *text*

The headline idea. Tap any word in a Judeo-Arabic text and get its sense in context. What
makes it more than a glossary is that the lookup is **layered by source and scope**:

- **General classical Arabic — Lane.** A hand-curated two-tier dictionary keyed on
  Hebrew-script Judeo-Arabic: `data/dictionary-starter.json` (**53** foundational entries)
  + `data/dictionary-lane.json` (**9,154** entries paraphrased from E. W. Lane's *Lexicon*).
  This answers "what does this Arabic word mean."
- **Special medieval-JA senses — Blau, scoped per work.** Many words mean something
  *different* in medieval Judeo-Arabic than in classical Arabic, and often differently again
  in a *specific* author. Those senses live in per-work overlays
  (`lib/workNotes.ts` + `data/blau-notes-{work}.json`) drawn from Joshua Blau's *Dictionary
  of Medieval Judaeo-Arabic Texts* (2006) — currently `blau-notes-moreh.json` (2 notes) and
  `blau-notes-qirqisani.json` (5). They surface **only** in the reader for the work they
  belong to, so Maimonides' technical sense of a word never leaks into the Bahya reader.

The same isolation principle runs through the data via a `scope: "saadia"` flag on entries,
so Saadia's coinages don't pollute the general library. The pedagogical pay-off: a learner
sees the *ordinary* meaning and the *this-author-means-something-special* meaning as
distinct, attributed layers — which is exactly the distinction a critical reader needs.

> Provenance note for Sefaria: the Lane layer derives from public-domain Lane; the small Blau
> overlay is **licensing-pending** — I'm in touch with the Academy of the Hebrew Language
> (Blau's rights holder) about it, and I'd keep any Sefaria integration clean of unlicensed
> Blau data until that's settled.

---

## 2. A deterministic prefix-stripping lookup, parity-locked to a coverage gate

Judeo-Arabic agglutinates the article and prepositions onto the word (ובאלכלאם = ו+ב+אל+כלאם).
Rather than a morphology engine, the lookup is a small, auditable **candidate chain**
(`candidateForms()` in `lib/lookup.ts`): try the exact form, then strip leading *vav*, then a
single-letter preposition (ב/ל/כ/פ), then the article (אל), normalize final↔medial letters,
strip the orthographic apostrophe — first hit wins. The same chain is reused by the Blau
overlay and the divergence layer, so all three resolve a tapped word identically.

What makes this trustworthy at scale: the identical algorithm is **re-implemented in Python**
(`scripts/coverage_report.py`, `scripts/coverage_advanced.py`) and run as a **CI gate that
fails the build if any in-scope text is below 100% tap-to-define coverage**. Every token in
every in-scope chapter is guaranteed to resolve to a real dictionary entry — no silent dead
taps. The five Torah books of the Tafsir and six advanced excerpts are at 100% under this gate.

---

## 3. Tri-lingual hover-highlight alignment (Hebrew ↔ Judeo-Arabic ↔ English)

Hover a word/phrase in any of the three columns and the corresponding spans light up in the
other two. Implementation is deliberately **data-driven, not inferred**:

- Alignment is stored as ordered hand-authored phrase-pairs per verse
  (`data/tafsir-{book}-{chapter}-alignment.json`; **187** files so far), each pair a
  `{he?, ja, en}` substring triple.
- A resolver (`lib/alignment.ts`) maps each substring back to a character span using a
  **forward cursor with fallback** — it prefers the next unclaimed occurrence in reading
  order but can fall back anywhere, which gracefully handles word-order crossing (negation
  fronting, verb–subject inversion) that purely positional aligners miss. Spans get a shared
  group id; the UI highlights by group across all columns, with a debounced hover to avoid
  flicker.

Honest status: alignment is **actively authored** — word-level on some books (Vayikra,
Bamidbar, much of Devarim), clause-level elsewhere (Bereshit, Shemot). The *data model*,
though, is simple and portable, which is the relevant bit for Sefaria.

---

## 4. Supporting pieces

- **Hebrew↔Arabic script bridge** (`lib/arabicToJa.ts`): advanced texts like Qirqisani exist
  in Arabic script; this converts a tapped Arabic token to the Hebrew-keyed dictionary form
  (a port of the convention in my `arabic-lexicon` toolkit: غ→ע׳, ج→ג׳, ث→ת׳, …).
- **"Tafsir twist" divergence overlay** (`lib/divergence.ts`, `data/tafsir-divergence.json`,
  ~**140** entries in three tiers — twist / note / gloss): a pedagogical layer that surfaces
  *where and why* Saadia's Arabic departs from classical expectation (anti-anthropomorphism,
  Muʿtazilite vocabulary, calque, coinage), each attributed and tier-rendered.
- **Spaced repetition** (`lib/wordState.ts`, `ts-fsrs`): tapped words move new → learning →
  known with FSRS scheduling in localStorage; a `/review` page drills what's due. Plus
  curated learn modes (first-50, Hebrew/Aramaic cognates).

---

## 5. Why I'm writing to Sefaria — a collaboration ask

Sefaria already hosts much of the *source* this app reads — Derenbourg's Tafsir, ibn Tibbon's
Bahya, and more — and Judeo-Arabic is a corpus that deserves first-class reading tools. A few
concrete places this could meet Sefaria:

1. **The alignment data model.** A lightweight, hand-authorable phrase-pair format for
   multi-version word-correspondence highlighting, with a forgiving resolver. Could generalize
   to any Sefaria text-with-translation pairing, not just Judeo-Arabic.
2. **Tap-to-define with scoped lexicons.** The Lane-general / per-work-special layering is a
   pattern that fits Sefaria's many-commentary world; the lookup is small and dependency-free.
3. **The Judeo-Arabic corpus + coverage discipline.** A growing, 100%-glossed JA reading set
   with a CI gate that guarantees no dead taps — a quality bar that could seed JA on Sefaria.

I'd love a short conversation about whether any of this is useful to you — whether as an
upstream contribution, a data donation, or just comparing notes. Everything here is mine to
share except the small Blau overlay, which I'd hold back pending the Academy discussion.

Thank you for Sefaria — it's the reason a project like this can stand on real texts.

— Eli Freedman · freedmaneli@gmail.com

---

*File/count references reflect the repo as of 2026-06-05 and can be verified directly:
`data/dictionary-lane.json` (9,154), `data/dictionary-starter.json` (53),
`data/tafsir-divergence.json` (140), `data/blau-notes-{moreh,qirqisani}.json` (2 + 5),
`lib/lookup.ts`, `lib/alignment.ts`, `lib/workNotes.ts`, `lib/arabicToJa.ts`,
`scripts/coverage_*.py`.*
