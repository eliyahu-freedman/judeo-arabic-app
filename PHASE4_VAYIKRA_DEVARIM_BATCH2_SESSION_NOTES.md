# Phase 4 Vayikra/Devarim Batch 2 — Session Notes

**Date shipped:** 2026-05-30
**Apply script:** `scripts/apply_phase4_vayikra_devarim_batch2.py`
**Files modified:** `data/tafsir-divergence.json`, `data/_blau_saadia_deferred.json`
**Git status:** working tree uncommitted (per project convention)

This is **task #1** of the Phase 3 R3 continuation (the חאכם judicial-vocabulary
NOTE flagged in Devarim B1 Yield Observation #5 and logged to the R2 B1 skip
record). Scope was deliberately **#1 only** — no #2 R1 second wave, no #3 reader
cross-link.

---

## Snapshot

| Metric | Before | After | Δ |
|---|---|---|---|
| Total divergence entries | 124 | 125 | +1 net-new |
| Tier distribution | 37 twist / 37 note / 50 gloss | 37 / 38 / 50 | +1 NOTE |
| New cross-book NOTE | — | אלחאכם (Shemot + Devarim, 9 verses) | first 2-book judicial NOTE |
| Deferred records resolved | — | `phase3_r2/batch1/skip` lemma חאכם → RESOLVED | audit trail kept |
| Gates | — | verify_divergence.py PASS · 0 warnings · npm run build clean | all green |

---

## Per-entry rundown

### NEW ENTRY — 1 NOTE

**`אלחאכם`** (الحاكم, root ح-ك-م) — `note` tier, 9 verses across 2 books.

Saadia collapses **three distinct Hebrew judicial terms** onto the single bare
noun אלחאכם "(the) judge":

| Heb term | verses | Saadia surface |
|---|---|---|
| הָאֱלֹהִים ("God"/the elohim-judges) | Ex 21:6, 22:7, 22:8 | אלי' אלחאכם |
| הַשֹּׁפֵט ("the judge") | Deut 17:9, 17:12, 25:2 | (מן) אלחאכם / פליבסטה אלחאכם |
| הַשַּׁעַר / הַשָּׁעְרָה ("the gate") | Deut 21:19, 22:15, 25:7 | באב (אל)חאכם "the gate of the judge" |

Two interpretively notable moves captured in the mechanism prose: (1) the
**elohim-as-judges** rendering of הָאֱלֹהִים, which is both the rabbinic-juridical
reading and anti-anthropomorphic-adjacent (the litigation venue is the human judge,
not the deity); (2) the **gate→judge** identification — the city gate (biblical
judicial venue) rendered באב אלחאכם, making the gate's juridical function lexically
explicit.

**Register distinction (the whole point of the NOTE):** structurally distinct from
the existing **חאכמא** TWIST. The TWIST is the circumstantial-accusative participle
حاكمًا that Saadia *inserts* into divine speech-acts (Gen 1:22, Ex 2:14/22:27,
Lev 20:24) to avoid anthropomorphism — a syntactic deployment in divine-speech.
This NOTE is the ordinary substantive for human judicial officials in
legal-procedural narrative. Same root ح-ك-م, opposite move (the TWIST *adds* a
participle; the NOTE *flattens* varied Hebrew nouns onto one substantive).

**Blau sourcing:** `sources = [lane, saadia-direct, blau-dict]`, `relation: "adjacent"`.
Blau's חכם entry attests the judicial **verb** (Form III "שפט, דן / to judge"
[Pirqei Avot] + the legal "to sue / summon to lawsuit") but gives the bare-noun
substantive حاكم "(the) judge" **no separate headword** — that noun is the classical
agent-noun of the verb Blau glosses (Lane, s.v. حكم). `blau_dict.sense` states this
verb-vs-noun distinction honestly. This mirrors the sibling חאכמא TWIST exactly
(also `relation: "adjacent"` for the same root). Confirmed in planning via the
arabic-lexicon skill (slug `blau-judeoarabic`): a grep for the bare-noun حاكم
returned no headword; only the verb senses are present.

All 9 surface forms were read directly from `data/tafsir-{book}-{ch}.json` — no JA
was hand-authored.

---

## Deferred buckets

No new deferred records this batch. One existing record **RESOLVED**:

- `phase3_r2/batch1/skip` lemma **חאכם** → `status: "RESOLVED 2026-05-30"` +
  `resolution` pointing at this NOTE. Kept as audit trail (not deleted), per
  convention.

This closes the prediction made in Devarim B1 Yield Observation #5 (line 158-160)
and next-strategy item #1 (line 172): "if the Shemot Jethro/elohim passages parallel
the Devarim pattern, ship as a new NOTE." The R2 B1 scan surfaced exactly those
Shemot elohim-as-judges hits (Ex 21:6, 22:7, 22:8), upgrading the cluster from the
6-verse Devarim-only candidate to a 9-verse 2-book NOTE.

---

## Gates

- `python3 scripts/apply_phase4_vayikra_devarim_batch2.py` → "Added 1 entries",
  "Total entries now: 125", tiers `{twist:37, note:38, gloss:50}`,
  `{"חאכם_skip_resolved": true}`.
- `python3 scripts/verify_divergence.py` → **125 entries · All citation + sources
  checks PASS · 0 warnings · Quality bar PASS**. (NOTE-tier entry does not count
  against the twist-tier per-book relation mix.)
- `npm run build` → **clean** (187 SSG tafsir paths emitted).
- Re-confirm one-liner → `125 Counter({'gloss': 50, 'note': 38, 'twist': 37})`.

---

## Yield observations

1. **First 2-book NOTE in the judicial register.** The chains for the cross-book
   NOTEs to date have been ritual/conquest/atonement vocabulary (סלאמה, יסתג'פר,
   אקרץ'). אלחאכם is the first multi-book NOTE built on a *register-distinction
   against a sibling TWIST* rather than on a single Heb→Ar substitution. The
   pedagogical payload is the contrast with חאכמא, not the substitution alone.

2. **The skip record was a high-quality candidate, as predicted.** The R2 B1 triage
   correctly identified the bare-noun cluster as a deferred NOTE rather than forcing
   it into promote-in-place on the חאכמא TWIST. Deferring (vs. mis-merging) preserved
   the register-distinction that is the entry's reason to exist. Validates the
   "skip-with-a-reason, ship-later" discipline.

3. **`relation: "adjacent"` is the honest verdict when Blau has the verb but not the
   substantive.** This is the same call as the sibling חאכמא, and a cleaner precedent
   than the תגלא case (where Blau had *zero* hits → no blau_dict, logged in
   no_cite_audit). The decision tree is now: bare-noun-not-in-Blau-but-verb-is →
   cite blau-dict at `adjacent` with an explicit verb-vs-noun note; sense-entirely-
   absent-from-Blau → drop blau-dict, log in no_cite_audit.

---

## Recommended next-session strategy

Pick up at the continuation prompt's **task #2 — Phase 3 R1 second wave** (now the
headline). The per-book quality gate is still active only for Bereshit (35 twists);
Shemot/Vayikra/Bamidbar/Devarim sit at 1 twist each and skip the gate. Add **≥5
net-new TWIST entries per book** to activate it uniformly. Source candidates from
`data/_blau_saadia_candidates.json` and the per-book scans. This is the larger,
multi-batch piece — split per book.

Note the Devarim NOTEs `אקרץ'`, `יסיב`, `ממתעה` are TWIST-adjacent and could promote
to TWIST in R1 if Blau-verification confirms paradigm-shifting status (per Devarim
B1 next-strategy #3).

Deferred-but-not-forgotten: the Vayikra/Devarim B2 *borderlines* (יקתצ'י, ממד-יד,
נווב, תנאצי) remain available, and the R2 cluster-head re-mining (19636-49 nٰtج,
19861-71 nfd) is still open.

Optional, anytime: task **#3** — a reader-UX back-pointer cross-linking אורד
(dispatch) ↔ תגלא (manifestation), the two halves of the ירד split. Not started.
