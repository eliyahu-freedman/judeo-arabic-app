# Next session — Phase 4 Bamidbar Batch 1 (or Vayikra Batch 2)

Ready-to-paste prompt for the next session. Choose **Track A** (recommended) or **Track B** based on whether you want fresh-book exploration with strong cross-book opportunity, or to mop up the four NOTE-grade borderlines + cluster heads still on the Vayikra board.

---

## TRACK A — Bamidbar Phase 4 Batch 1 (recommended)

> walk the Bamidbar-flagged subset of `data/_blau_saadia_candidates.json` for Phase 4 Batch 1. Target 10-12 entries shipped (3-5 NOTE + 6-7 GLOSS), same methodology as Vayikra Batch 1.
>
> Context:
> - Read `PHASE4_VAYIKRA_BATCH1_SESSION_NOTES.md` for the just-shipped baseline (106 entries, 36 twist + 29 note + 41 gloss; gates green; 2 promote-in-place precedents `נקל`+`שחמה'`).
> - Read `PHASE4_SHEMOT_BATCH2_SESSION_NOTES.md` for the Shemot-Mishkan-cluster precedent (the Shemot-Vayikra-Bamidbar vocabulary triangle is the high-leverage cross-book territory).
> - Read `PHASE4_BLAU_MINING_PROMPT.md` for the full tier definitions + verification gate methodology.
> - **Cross-book promote-in-place expected:** Bamidbar shares heavy vocabulary with both Shemot (Mishkan/Tabernacle setup carries over to Camp/Tent of Meeting in Num 1-10) and Vayikra (sacrificial system extends to Num 6-8 nazirite + Num 15:24-29 + Num 28-29 festival cycle). Specifically scan for cross-book extensions of: `סלאמה` (peace-offering — Num 6:14-18 nazirite), `ד'כוה` (sin-offering — Num 6:11, 15:24-29, 28-29), `יסתג'פר` (atonement — Num 5:8, 6:11, 15:25-28, 16:46-47, 25:13, 28:22, 28:30, 29:5, 29:11), `מסוחייה` (anointing oil — Num 4 cluster from the deferred Vayikra B1 borderline; this is a strong dual-promotion opportunity), `שחמה'` (already promoted Shemot+Vayikra; check Num for any further extensions), `מוגה` (showbread — Num 4:7 שולחן הפנים cross-attests with the existing entry).
>
> Walk parameters:
> - **Source window:** `data/_blau_saadia_candidates.json#/candidates`, filter on `saadia_citation_lines` containing `במדבר` / `במ׳` / `במ"`. Expected pool size: ~80 candidates per the original mining prompt projection, but expect Vayikra-style cluster-duplication to compress the underlying-article count to ~30-40.
> - **Walk in `blau_id` order** from lowest. No pre-existing cursor; fresh start for the book.
> - **Stop condition:** 10-12 surviving entries; or pool exhaustion.
>
> Verification gate (per candidate):
> 1. Filter candidate set with the Bamidbar citation pattern.
> 2. For each survivor, load `data/tafsir-bamidbar-{ch}.json` for the cited verse.
> 3. Confirm JA surface form (or variant) in the verse's `ja` column AND Hebrew anchor in the `hebrew` column. **Normalize:** strip nikud (U+0591-U+05C7), strip final-form variants (ך→כ, ם→מ, ן→נ, ף→פ, ץ→צ), strip apostrophe (' and ׳ and `). Critical: the tafsir uses **dotted Hebrew letters** (ד', כ', צ', ת') for the corresponding Arabic ذ/خ/ض/ث consonants — Blau's body OCR sometimes omits the dot, so cross-check the actual Cairo-2019 surface before fixing the lemma form.
> 4. If either check fails → log to `borderline` bucket with the open question.
>
> **Cross-book scan (do this BEFORE shipping new entries):** for each surviving candidate whose lemma already exists in `data/tafsir-divergence.json` (Bereshit + Shemot + Vayikra), prefer **promote-in-place** over `cross_book_dupes` deferral — extend `verses[]`, upgrade `tier` if the Bamidbar attestations strengthen the mechanism, rewrite `mechanism` + `blau_dict.sense` to cover the broader pericope. Follow the `שחמה'` precedent from Vayikra B1 (which extended Shemot Ex 29:20 → 6 verses across two ritual systems) and the `נקל` precedent from Shemot B2 (gloss → note tier upgrade with full Exodus-slavery cluster).
>
> Apply pattern:
> - Mirror `scripts/apply_phase4_vayikra_batch1.py` exactly: copy as `scripts/apply_phase4_bamidbar_batch1.py`, update window range in header docstring, replace `NEW_ENTRIES`, replace `BATCH1_DEFERRED`, retarget `_update_deferred()` to write to a new `bamidbar` namespace, retarget `_patch_promote_in_place()` PROMOTE_IN_PLACE dict for any cross-book extensions (or leave empty if none surface — the helper handles `None` gracefully).
>
> Verification gates (run after the apply script lands):
> ```bash
> cd ~/Code/judeo-arabic-app
> python3 scripts/verify_divergence.py    # must show 0 failures
> npm run build                            # must stay clean
> python3 -c "import json; e=json.load(open('data/tafsir-divergence.json'))['entries']; assert len(set(x['lemma_ja'] for x in e))==len(e)"
> ```
>
> Ship a `PHASE4_BAMIDBAR_BATCH1_SESSION_NOTES.md` in the Batch-1/2 format (snapshot, per-entry rundown, deferred buckets, cluster dupes, yield observations, recommended next-session strategy). Leave the working tree uncommitted per project convention.

---

## TRACK B — Vayikra Batch 2 (cleanup pass)

> mop up the four NOTE-grade borderlines from Batch 1 plus mine cluster-head dupes for additional entries. Target 6-8 entries via two sub-tracks (in priority order).
>
> Context:
> - Read `PHASE4_VAYIKRA_BATCH1_SESSION_NOTES.md` for the current Vayikra state (Batch 1 = 12 net-new + 1 promote-in-place across 19 verses in 11 chapters).
> - Read `data/_blau_saadia_deferred.json#/vayikra` for the 21-entry triage bucket (17 skip + 4 borderline + 13 cluster-dupes-logged).
>
> Sub-tracks:
>
> **B.1 — BORDERLINE promotion (target 4 ships):**
> The 4 borderlines were all NOTE-grade candidates CUT AT THE 5-NOTE CAP, not pending-judgment cases. Promote them in one coordinated pass:
> - `17407 כ'אמע` (Lev 21:18 שרוע → خمع 'dislocated hip') — coordinate with the rest of the priestly-disqualification list (Lev 21:18-23: עוֵר, פִּסֵּחַ, חָרֻם, שָׂרוּעַ, שֶׁבֶר רגל, שֶׁבֶר יד, גִּבֵּן, דַּק, תְּבַלֻּל, גָּרָב, יַלֶּפֶת, מְרוֹחַ אָשֶׁךְ — 12 defects, several may be NOTE-grade individually or as a bundle).
> - `18594 קצבה` (Lev 1:8 פדר → قصبة 'body-cavity, viscera') — pair with other sacrificial-anatomy entries in Lev 1-7 if mining surfaces them.
> - `19142 לג` (Lev 14:10 לוג → Heb-loanword retention) — parallels the מרזבאן Persian-loan from Shemot Batch 2; sets up a measure-vocabulary mini-category.
> - `19427 מסוחייה` (Lev 8:2/10 שמן המשחה → Aramaic-Syriac calque) — strong Mishkan-cross-reference candidate; cross-check with Num 4 mining if Track A also runs to coordinate the promote-in-place.
>
> **B.2 — Cluster-head re-mining (target 2-4 ships):**
> The 13 cluster groups logged in Vayikra B1's `_cluster_dupes_logged` flagged article-heads we skipped. A few may have tier-grade NOTE/GLOSS readings hidden inside the OCR-mangled body excerpts:
> - `17302-17307 ثلول/فغلول` (Lev 13:38 יבלת / Lev 21:20 יבלת) — manuscript-variant flagged as skip in B1; re-check Cairo 2019 for actual surface
> - `18378-18379 فيضة/فائض` (Lev 15:28 מזובה) — was cut at-cap; revisit as GLOSS-tier medical-anatomical
> - `17999-18000 غفر/غفارة` — already shipped (יסתג'פר) but check for additional غفارة 'atonement' substantive uses
> - `18190-18191 فركة/فريك` — already shipped (פריך) but check for additional fresh-grain attestations across the spring-harvest pericopes
>
> Apply pattern:
> - Surgical-patch directly into `data/tafsir-divergence.json` for the 4 borderline promotions (move from deferred to shipped + add new entries). Pattern: load the deferred file, pull the 4 borderline blau_ids, remove from `vayikra.borderline[]`, append the corresponding new entries to `tafsir-divergence.json#/entries`. Write both files.
> - For any B.2 cluster-head ships, follow the standard Batch-1 entry shape.
>
> Verification gates (same as Batch 1):
> ```bash
> cd ~/Code/judeo-arabic-app
> python3 scripts/verify_divergence.py
> npm run build
> ```
>
> Ship a `PHASE4_VAYIKRA_BATCH2_SESSION_NOTES.md` with the same structure as Vayikra B1 notes. If only B.1 lands, the doc can be a half-page; if B.2 lands too, full Batch-1/2 format.

---

## After either track lands

The natural follow-ons in priority order:

1. **Bamidbar Batch 2** if A landed, or **Bamidbar Batch 1** if B landed
2. **Devarim Phase 4 Batch 1** — last book; reuse the Holiness-Code (Lev 17-26) → deuteronomic-law parallels and the Mishkan-vocabulary cross-attestations now shipped across Shemot+Vayikra
3. **Phase 3 R2 cross-book scan** — the existing `נקל` (Bereshit+Shemot) + `שחמה'` (Shemot+Vayikra) precedents suggest a methodology for retroactively scanning the existing 36 twist entries for multi-book attestation. Highest-leverage cross-book move available; scope after Bamidbar lands
4. **Phase 3 R1** — the ~30 deferred STRICT-tier additions that never shipped; re-evaluate once all 5 books are at ≥5 twist entries each so the verifier's per-book gate activates uniformly

## Pattern reminders that mattered in Vayikra Batch 1

- **Multi-verse system-vocabulary calques are the highest-leverage entries** — ד'כוה (5 verses across the sin-offering system) and יסתג'פר (5 verses across the atonement system) restructure entire priestly subsystems with a single entry each. When mining, ALWAYS check whether a candidate's lemma surfaces across a coordinated pericope-cluster rather than at just the originally-cited verse — bundle aggressively.
- **Dotted-letter normalization for tafsir orthography** — the Cairo 2019 tafsir uses ד' / כ' / צ' / ת' for Arabic ذ / خ / ض / ث; Blau's body OCR may use bare ד / כ / צ / ת. Always cross-check the lemma form against the actual tafsir surface; ship the dotted form when that's what the verse uses.
- **Cluster-flattened survival rate is the right metric once clusters get heavy** — Vayikra had 76 candidates but only ~32 underlying articles after cluster-flattening. 13 ships / 32 articles = 41% effective survival vs. 13/76 = 17% raw. Bamidbar likely has similar pattern.
- **Promote-in-place pattern is now standard, not exceptional** — two precedents shipped (`נקל`, `שחמה'`); use whenever a cross-book attestation strengthens an existing entry. Don't defer to `cross_book_dupes` unless the new pericope's reading is genuinely orthogonal.
- **Tafsir chapter-files may have gaps** — Lev 26:30 was missing from `data/tafsir-vayikra-26.json` and forced `19861 نفذ` family (11-row cluster) to skip-deferral. If a Bamidbar candidate's cited verse is missing from the chapter file, log to skip with that reason.
- **Deferred file uses fresh namespace per book** — Vayikra B1 created the `vayikra` namespace via `setdefault`; same pattern for Bamidbar (`bamidbar` namespace). Multi-batch namespaces (like Shemot 1+2) use the merge-idempotent `_update_deferred()` pattern.
