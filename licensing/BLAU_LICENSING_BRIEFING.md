# Blau Dictionary — Internal Licensing Briefing

**Audience:** Eli only (prep for a meeting with the Academy of the Hebrew Language). **Not for distribution.**
**Date drafted:** 2026-06-05
**Subject:** Use of data derived from Joshua Blau ז״ל, *A Dictionary of Medieval Judaeo-Arabic Texts* (Jerusalem, 2006; ISBN 965-208-171-X).

> **Rights holders:** The print dictionary's copyright line names **the Academy of the Hebrew Language (האקדמיה ללשון העברית)** and **the Israel Academy of Sciences and Humanities (האקדמיה הלאומית הישראלית למדעים)**, תשס״ו (2006). Blau himself is deceased, so the institutions hold the rights.

---

## 1. The one-sentence honest summary

The **public app** ships a *small, fully attributed, transformative* set of original scholarly notes that *cite* Blau (strong fair-use posture); a **separate local research tool** holds a *near-complete structured reproduction* of the dictionary (the weaker spot, and the thing to be candid about).

Be forthright about **both** layers. Leading with only the first would be technically true but not the whole truth, and the goal here is honesty + goodwill.

---

## 2. What is used, and exactly where

### Layer 1 — The public web app (`~/Code/judeo-arabic-app`)

What the public actually sees. All of it is original editorial content that *references* Blau, not Blau's article text.

| Item | File | Count | Nature |
|---|---|---|---|
| "Tafsir twist / note / gloss" divergence notes | `data/tafsir-divergence.json` | **140** (56 twist · 34 note · 50 gloss); **129 carry a `blau_dict` backing field** | One-line original note: lemma, root, classical vs. Saadia sense, mechanism. Cites Blau *s.v.* a root. |
| Per-work overlay — Maimonides' *Guide* | `data/blau-notes-moreh.json` | 2 | Original note on a word's special JA sense, attributed to Blau. |
| Per-work overlay — Qirqisani's *al-Anwar* | `data/blau-notes-qirqisani.json` | 5 | Same. |

**Attribution is explicit and granular:**
- Each divergence renders a literal **"Blau s.v. [root]"** label in the reader (`app/tafsir/reader.tsx` ~line 716; advanced reader `app/advanced/reader.tsx` ~line 554).
- The site footer (`app/layout.tsx` lines 206–209) credits *"Joshua Blau ז״ל's Dictionary of Medieval Judaeo-Arabic Texts (Jerusalem, 2006)."*
- The explainer page (`app/what-is-judeo-arabic/page.tsx`) and resources page (`app/resources/page.tsx`, links to Magnes Press) name the dictionary as the reference standard.

**What is *not* in the app:** Blau's definitions verbatim, his article bodies, his citations, or any bulk extract. A user cannot reconstruct the dictionary from the app.

### Layer 2 — The local research tool (`~/Tools/arabic-lexicon`) — NOT published

This is back-end infrastructure on Eli's machine, used to *build* Layer 1. It is **not** in the app repo and **not** served to any user. But it is the substantive reproduction and must be disclosed.

- A **full structured mirror of all 6,736 usable Blau entries** — `blau-cleanup/blau-clean.jsonl` (5.1 MB), queryable in `lex.sqlite` under the dict slug `blau`, with raw-OCR fallback under `blau-judeoarabic`.
- Per-work extractions in `blau-by-work/` (e.g. `qirqisani.json`, 157 entries).
- Searchable Hebrew↔Arabic, sense-tagged, with register notes, idioms, variants, cross-refs.

---

## 3. Provenance chain (so every claim is verifiable)

Print book → **OCR** (`~/Tools/arabic-lexicon/blau-judeoarabic.txt`; copyright line names the two Academies) → **block extraction** (4,475 entry blocks → `blau-entries-raw.jsonl`) → **AI cleanup/structuring** (Claude Haiku, two passes, **total spend $28.68**, completed 2026-05-17 → 6,736 usable entries) → **indexed** into `lex.sqlite` → **mined** for Saadia-citing entries (1,596 candidates) → **hand-curated** into the 140 + 7 original notes that ship.

Source docs (all on disk, can be shown if asked):
- `~/Tools/arabic-lexicon/blau-cleanup/STATE.md` — pipeline + cost log.
- `~/Tools/arabic-lexicon/blau-cleanup/cleanup_prompt.md` — the structuring prompt.
- `BLAU_SAADIA_CALIBRATION.md` (this repo) — the mining/tiering study.
- `PHASE4_BLAU_MINING_PROMPT.md` + the `PHASE3/4_*` session notes — the curation workflow.

---

## 4. Honest IP assessment

### Layer 1 — strong fair-use / fair-dealing posture
- **Amount:** ~147 short original notes vs. ~8,000+ dictionary entries — a tiny fraction, and not the entries themselves.
- **Transformation:** each note is new scholarship (an observation about Saadia's translation choices) that *points to* Blau; it does not reproduce his prose.
- **Attribution:** named, per-entry, plus site-wide credit.
- **Purpose:** educational, non-commercial (confirm — see §6).
- **Market effect:** none plausible — the app drives readers *toward* the dictionary, it cannot substitute for it.

### Layer 2 — candid about the weak spot
- A structured, cleaned, searchable version of **the whole dictionary** is a **substantial reproduction**, even though it lives only on a private machine and is never served.
- The "it's transformed/error-corrected" argument is real but does **not** by itself defeat copyright in a near-complete derivative.
- The OCR carries OCR damage; an uncontrolled copy bearing the Academy's name could be a quality/reputation concern for them.
- **This is the honest crux to put on the table** — and the natural bridge to a partnership or license rather than a fight.

> Caveat: present fair use as a **good-faith position, not settled law.** Don't assert it as a guarantee.

---

## 5. What the Academy might want (anticipate)

- **Credit** — already given; offer to expand/standardize it however they prefer.
- **Control / quality** — they may not want a damaged copy of their dictionary in circulation under their name. Reassure: Layer 2 is private and can be locked down or deleted; or, better, *jointly cleaned* to their standard.
- **A fee** — likely modest if any; the work is educational.
- **The technology** — the structured DB + tap-to-define reader is genuinely useful; they may prefer to *take/co-own it* (a far better outcome than a takedown).
- **Concerns to preempt:** market harm to any print/online edition they sell; an AI-cleaned text mislabeled as authoritative Blau.

---

## 6. Open questions to resolve BEFORE the meeting / before sending the letter

- [ ] **Is the app publicly deployed?** (It is Vercel-linked — confirm the live URL and whether it's indexed/public.)
- [ ] **Is it monetized in any way?** (Donations, ads, paid tiers?) The fair-use story is much cleaner if purely non-commercial.
- [ ] **Who at the Academy handles rights/licensing?** Find the named contact (likely the Academy's scientific secretariat / publications) rather than a generic inbox.
- [ ] Is there an existing *online* Blau (e.g. the Academy's Maagarim / historical-dictionary projects) that this could plug into? That sharpens the partnership pitch.
- [ ] Decide the **walk-away (BATNA):** if they object, you keep only the 147 cited public notes (clearly fair use) and remove/sequester the full Layer-2 mirror. Confirm you're comfortable with that floor.

---

## 7. Negotiation arc (suggested)

1. **Open with disclosure**, not a request — "here is exactly what I built and how I used your dictionary." Goodwill first.
2. **Show the value** — demo the reader + the worked Saadia examples (§ in the letter). Make them want it.
3. **Offer options, let them choose** — blessing for the cited use / a license / a partnership where they host or co-own the tech / a jointly-funded project.
4. **Name the funding path** if money is the friction — a grant or fiscal sponsor could cover a license or a joint build, so it needn't come from the Academy's budget.
5. **BATNA in your back pocket** — never threatened, just your quiet floor: shrink to the indisputably-fair-use public set.

---

*Files referenced in this briefing exist on disk as of 2026-06-05 and can be shown to verify any claim.*
