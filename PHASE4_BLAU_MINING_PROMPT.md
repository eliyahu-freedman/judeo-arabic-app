# Phase 4 — Mine MEDIUM + EXPANSIVE Blau-Saadia entries into the tiered surface

**Context (read first):**
- `BLAU_SAADIA_CALIBRATION.md` — corpus baseline + tier definitions (STRICT / MEDIUM / EXPANSIVE / SKIP / BORDERLINE) and the expected ~870 entries that clear the expansive bar (up to ~1,560 with BORDERLINE upgrades).
- `~/.claude/plans/lets-continue-phase-4-partitioned-wombat.md` — the just-approved Phase 4 plan (this session shipped the infrastructure described there).
- Prior plan reference: `~/.claude/plans/lets-continue-code-judeo-arabic-app-phas-vivid-pony.md`.

## What's already shipped (uncommitted in the working tree)

The full tiering pipeline is live in the codebase. Confirm `git diff` matches before adding mined entries:

| Piece | File | Effect |
|---|---|---|
| Schema | `lib/divergence.ts` | `DivergenceTier = "twist" \| "note" \| "gloss"` + optional `tier?` on `DivergenceEntry` + `divergenceTier()` helper |
| Display | `app/tafsir/reader.tsx` | `DivergenceBanner` switches on `d.tier`: `TwistBanner` (wine, current style) / `SaadiaNoteBanner` (muted ink, one-line contrast) / `GlossCard` (compact one-liner, no eyebrow). Underline gate suppresses `gloss`-tier (hover-only). |
| Mining | `scripts/mine_blau_saadia_candidates.py` (NEW) | Queries `~/Tools/arabic-lexicon/lex.sqlite`, emits `data/_blau_saadia_candidates.json` — 1596 entries, citation lines on 1596/1596. Re-runnable. |
| Verifier | `scripts/verify_divergence.py` | Per-book Blau-backed threshold now applies to `twist`-tier entries only (note + gloss are Blau-backed by construction). Tier distribution reported. |
| Migration | `data/tafsir-divergence.json` | All 32 baseline entries stamped `"tier": "twist"` via `scripts/stamp_tier_twist.py` (idempotent). |

**Verified this session:** `npm run build` clean in 3.2s, no TS errors; `verify_divergence.py` exit 0 with the Bereshit 65% twist-tier warning preserved; mining script produced 1596/1596 citation extractions; spot-checked entries (نعام, ذكوة, بسيط) returned clean Saadia-citing snippets.

## The Phase 4 mining task

Classify `data/_blau_saadia_candidates.json` (1596 candidates) into:
- **`tier: "note"`** — MEDIUM bar. Semantic surprise (calque, register shift, technical extension, grammatical-form methodology). ~300 expected.
- **`tier: "gloss"`** — EXPANSIVE bar. Non-obvious Heb→Ar pairing pedagogically useful for JA acquisition (non-cognate, false friend, divergent semantic field). ~575 expected.
- **SKIP** — trivial cognate, bare textual-variant note, non-Tafsir Saadia citation, redundant attestation. ~30 expected (real rate after methodology corrections).
- **BORDERLINE** — Saadia cited but body context doesn't clearly justify the divergence. ~600 expected; **defer to a re-review backlog, do not promote on first pass.**

STRICT-tier (paradigm twist) candidates surfaced during this walk should be flagged for separate Phase 3 R1 review (`PHASE3_ROUND1_PROMPT.md`) — do NOT add them to the divergence file under `tier: "note"`.

## Recommended approach

**Don't classify all 1596 in one shot.** Tier judgment needs careful per-entry reading of Blau's body; the calibration's n=200 walk took multiple agent runs and still left ~43% BORDERLINE. Work in batches:

### Batch 1 — Bereshit-anchored pilot (~50 entries)

1. Filter `data/_blau_saadia_candidates.json` to candidates whose `saadia_citation_lines` mention a Bereshit verse (look for `ברא׳` / `בראשית` / `ב׳` patterns + chapter:verse refs in the citation lines).
2. Hand- or agent-classify each into note / gloss / skip / borderline / strict-defer. Use the calibration doc's tier exemplars as anchors:
   - `note`: جبروة → גבורה (divine-attribute extension); جسس → גישש (Form-I methodology)
   - `gloss`: وجدان → מציאות (non-cognate ontology); فريدة → singular-word (technical metalanguage); ضرغام → אריה (high-register synonym)
   - `skip`: trivial cognate, bare textual variant, non-Tafsir Saadia cite
3. Produce a fresh-format entry per accepted candidate matching the existing `DivergenceEntry` shape (see `data/tafsir-divergence.json` for examples). REQUIRED fields per tier:
   - `note`: full schema — `lemma_ja`, `lemma_ar`, `root`, `classical_en/he`, `saadia_en/he`, `mechanism` (short), `verses[]`, `sources[]`, `tier: "note"`, plus `blau_dict { root, sense, relation }` (mandatory for note tier).
   - `gloss`: trimmed — `lemma_ja`, `lemma_ar`, `root`, `classical_en/he` (the Hebrew word the gloss explains), `saadia_en/he` (the Arabic rendering), `verses[]`, `sources[]`, `tier: "gloss"`, `blau_dict { root, sense, relation }`. `mechanism` may be empty string or one short clause. Skip the classical-vs-Saadia contrast logic — `GlossCard` only renders `classical_he → lemma_ja / lemma_ar · saadia_en`.

### Apply pattern

Mirror the Round 4–7 `scripts/apply_round*_*.py` shape. For Phase 4:

```python
# scripts/apply_phase4_bereshit_batch1.py
import json, pathlib
DATA = pathlib.Path(__file__).resolve().parent.parent / "data" / "tafsir-divergence.json"

NEW_ENTRIES = [
    { "lemma_ja": "...", "tier": "gloss", "blau_dict": {...}, ... },
    ...
]

payload = json.loads(DATA.read_text())
payload["entries"].extend(NEW_ENTRIES)
DATA.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
```

### Verification gates (run after every batch)

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py   # tier distribution should show new note/gloss entries; Bereshit twist-tier warning unchanged
npm run build                          # must stay clean; tier='gloss' rendering goes through GlossCard
```

Then dev-server smoke: `npm run dev`, open `/tafsir/bereshit/1` (or whichever chapter your batch targets). Walk the verse with the new entries — note-tier words should get a muted dotted underline + "SAADIA NOTE" banner; gloss-tier words should have NO underline but pop the compact card on tap.

## Open question to confirm before mining

The plan's step-5 visual smoke test (inject one fake `note` + one fake `gloss` entry into Bereshit 1, confirm the three display variants, revert) was NOT executed this session — programmatic gates all passed but the UI variants haven't been eyeball-verified. Do that test once before mining starts; if anything looks wrong (color contrast, spacing, GlossCard layout), tighten the banner CSS before adding hundreds of entries.

## Don't forget: Phase 3 R1 is also waiting

`PHASE3_ROUND1_PROMPT.md`'s ~30 STRICT-tier additions never shipped (the data file is still at the 32 baseline). Phase 4 infra was prioritized over R1 so both tracks share the same pipeline. After Phase 4's Batch 1 lands cleanly, either:
- continue Phase 4 batches (Shemot, Vayikra, Bamidbar, Devarim each ~150 entries), or
- pivot to R1 (verse-first curation against `data/_blau_saadia_candidates.json` + the Bereshit text, target ~30 new `tier: "twist"` entries to lift Bereshit's 65% Blau-backed twist-tier warning above 70%).

The pipeline doesn't care which tier the next batch carries — both are drop-in.

## Files to read first when resuming

- `BLAU_SAADIA_CALIBRATION.md` (tier definitions + exemplars)
- `PHASE3_ROUND1_PROMPT.md` (Blau SQL pattern, strict-tier curation method)
- `data/tafsir-divergence.json` (existing entry shape — first 3 entries are a useful template)
- `app/tafsir/reader.tsx` lines ~640–760 (current `DivergenceBanner` / `TwistBanner` / `SaadiaNoteBanner` / `GlossCard`)
- `lib/divergence.ts` (the full type with the new `tier` field)
- `data/_blau_saadia_candidates.json` (1.4 MB; load via `json.load`, not Read tool)
