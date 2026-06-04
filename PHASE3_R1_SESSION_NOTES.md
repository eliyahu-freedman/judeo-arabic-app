# Phase 3 Round 1 — Session 1 Hand-off

## Snapshot

- **Date shipped:** 2026-05-29
- **Entries added:** 16 (4 twist + 6 note + 6 gloss), all direct-Blau-backed
- **Existing entries patched:** 2 (saadia-direct-only twists got `blau_dict` blocks from the no-cite re-audit)
- **Divergence file size:** 56 → 72 entries
- **Gate cleared:** Bereshit twist-tier Blau-backed 20/31 = **65%** → 26/35 = **74.3%** (well past the 70% threshold). Zero verifier warnings.
- **All gates green:** `verify_divergence.py` 0 failures + 0 warnings, `npm run build` clean (213 static pages).

## Gate math, verified

```
Bereshit twist-tier (verify_divergence.py output):

  Before:  total=31  direct=14  adjacent=6  different-sense=2  no-citation=9
  After:   total=35  direct=20  adjacent=6  different-sense=2  no-citation=7

  Backed ratio:  26/35 = 74.3%  (was 20/31 = 65%)
  Direct ratio:  20/35 = 57.1%  (was 14/31 = 45%)
  No-cite ratio:  7/35 = 20.0%  (was  9/31 = 29%)
```

Movement:
- +4 new direct twists (سيد · درق · ممتعة · شوب)
- +2 re-audit patches converted no-cite to direct (مستبحرة · شمشار)
- All three quality-bar dimensions improved simultaneously.

## Per-tier breakdown

| Tier | Lemma | Verse | Mechanism summary |
|---|---|---|---|
| TWIST | יסיידונך | Gen 49:8 | Judah blessing "praise" → "make ruler" (denominative Form II of سيد). Consumes deferred `phase3_r1_candidates` seed. |
| TWIST | ד'רקובה | Gen 12:20 | Pharaoh "escorts" (not "expels") Abram. Saadia overrules the harsh reading; Dirinbourg's emendation rejected. |
| TWIST | אלממתעה | Gen 38:21 | qedeshah → "temple-prostitute" (vs generic زانية). Lexical-cultic specification. |
| TWIST | משוובה | Gen 41:23 | Pharaoh's lean ears "scorched/contaminated by east wind" via شوب (classical "to mix/adulterate"). Post-classical semantic extension. |
| NOTE | אלמקלב | Gen 19:29 | Hebrew-shaped noun-form مقلَب for הַהֲפֵכָה (instead of verbal-noun انقلاب). Pattern-mirror calque. |
| NOTE | כרבת | Gen 41:8 | Pharaoh's spirit "troubled" via كرب (genuine grief register) vs the surface ضاق that would render the Hebrew הִפָּעֵם flatly. |
| NOTE | דהקתני | Gen 31:36 | Laban's "hot pursuit" via دهق (classical "to thrust/push hard"). Marked over the neutral اتبع / لحق. |
| NOTE | תמאות | Gen 33:13 | Jacob's flock argument: serial-aspect "die one after another" via Form I + plural accusative + softened to כת'יר ("many") not גמיע ("all"). |
| NOTE | תראגע | Gen 8:3 | Hebrew הָלוֹךְ וְ-X infinitive-absolute paradigm → Arabic كلما مر رجع serial-comparative. Blau says this is Saadia's stock equivalent. |
| NOTE | וחאם | Gen 30:41 | Sheep "in heat" — وحم post-classical migration from human-pregnancy register to animal-estrus register, exactly matching Hebrew יָחֵם. |
| GLOSS | יפאע | Gen 49:26 | high-register hill (vs prosaic تل) for גבעה in poetic-blessing context. |
| GLOSS | אלואנא | Gen 27:4 | culinary plural "kinds of dishes" for מטעמים. |
| GLOSS | תוניה | Gen 37:3 | Aramaic-flavored loan تونية (vs قميص) for כתונת. Phonological resonance preserved. |
| GLOSS | באלקפאר | Gen 6:14 | consonantal-calque k-p-r → q-f-r for biblical כפר (pitch). Verb pair וקפרהא ~ וְכָפַרְתָּ. |
| GLOSS | קטוע | Gen 29:2 | Marked plural قطوع (vs قطعان) for עדרי צאן. |
| GLOSS | אליבאס | Gen 1:9 | biblical-translation-register noun يَباس for יבשה. |

## Re-audit hits (patched into existing twist entries)

| lemma | verse | patch |
|---|---|---|
| מסתבחרה | Gen 1:2 | + `blau_dict.relation = "direct"`: Form X استبحر "to be covered by water, to overflow" cites Saadia on Bereshit directly. |
| שמשאר | Gen 6:14 | + `blau_dict.relation = "direct"`: شمشار "ash-tree / boxwood" cites Saadia on Gen 6:14 directly, with Ibn Janāḥ corroborating. |

Both patches add `"blau-dict"` to `sources[]` of the target entry.

## Re-audit misses (documented in `_blau_saadia_deferred.json:no_cite_audit`)

7 of the 9 audited entries had no Blau attestation against the lemma or root:
ריאח, תהב (Ber 1:2) · אטג'אני (3:13) · אשראף (6:2) · קרדא (8:4) · קרבאן (8:21) · אתון (11:28).

These remain `"saadia-direct"`-only readings. They are honest entries — Blau just doesn't reach the specific divergence claim being made. The deferred file records the search outcome so the bar stays visible.

## Files changed

**Modified:**
- `data/tafsir-divergence.json` — appended 16 new entries (56 → 72 total); patched `blau_dict` + `sources` on 2 existing twist entries.
- `data/_blau_saadia_deferred.json` — removed consumed `16430 سيد` from `phase3_r1_candidates`; logged into new `phase3_r1_consumed` array; added new `no_cite_audit` section with hits + misses; updated `borderline` note with Phase 3 R1 lemma-surface confirmation.

**Created:**
- `scripts/apply_phase3_round1.py` — apply script following the `apply_phase4_bereshit_batch*.py` template, with an inline RE_AUDIT_PATCHES pass that mutates existing entries by lemma_ja.
- `PHASE3_R1_SESSION_NOTES.md` — this file.

Working tree left uncommitted per project convention (matches `PHASE4_BERESHIT_SESSION_NOTES.md:41`).

## Recommended next-session strategy

In priority order:

1. **Begin Shemot Phase 4** — the Bereshit warning is fully cleared with margin (74.3% > 70%). The mining pipeline transfers directly to `data/_blau_saadia_candidates.json` filtered for Shemot citations. Write `scripts/apply_phase4_shemot_batch1.py` mirroring the Bereshit batches; the per-chapter filter is the only change.

2. **Phase 3 R2** — walk deeper into the 1,596-row Blau pool for additional twist-grade Bereshit divergences. The Phase 3 R1 yield was ~12 keepers per ~50 inspected rows; another R2 pass should clear ~10-15 more entries before hitting diminishing returns (most clean verse-anchored cases now consumed).

3. **Defer the metalanguage sub-batch** (مخكم, متشابه, مجاز, شبه, تمام, دلا Form V) — still waiting on UI design clarity about where Saadia's translation-theory vocabulary should surface (per-verse divergence panel? dedicated "Saadia's vocabulary" sidebar?).

4. **Re-attempt the BORDERLINE deferred entry** (`18250 فضض / Gen 3:5`) only as a sidetask in a future نفض-targeted scan. The Phase 3 R1 confirmation that the tafsir lemma is `תנפצ'` (Form V of نفض) means the candidate's root attribution to فضض was a Blau-side error.

## How to resume

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py    # baseline: 72 entries, 0 warnings
cat data/_blau_saadia_deferred.json     # phase3_r1_candidates is now empty; phase3_r1_consumed logs what landed
ls scripts/apply_phase*.py              # pattern for next batch
```
