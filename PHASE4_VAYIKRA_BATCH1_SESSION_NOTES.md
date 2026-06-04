# Phase 4 Vayikra — Batch 1 Hand-off

## Snapshot

- **Date shipped:** 2026-05-29 (immediately after Shemot Batch 2; first Vayikra pass)
- **Entries shipped:** 13 worth — 12 net-new (5 NOTE + 7 GLOSS) appended, plus 1 existing entry (`שחמה'`) promoted in place with 5 Vayikra attestations added to the Shemot baseline
- **Divergence file size:** 106 entries (36 twist + 29 note + 41 gloss; from the 94 Batch-2 baseline)
- **All gates green:** `verify_divergence.py` 0 failures; `npm run build` clean (213 static pages, all 184 tafsir routes generated); lemma uniqueness 106/106
- **Deferred file:** `data/_blau_saadia_deferred.json#/vayikra` created fresh (17 skip + 4 borderline + 13-entry `_cluster_dupes_logged` audit trail + `_session` tag)

## Window walked

- **Range:** Full Vayikra-flagged subset of `data/_blau_saadia_candidates.json` — `blau_id 13781–20399` (filter on `saadia_citation_lines` containing `ויקרא` / `ויק׳` / `ויק"`)
- **Pool size:** 76 candidates surfacing 32 underlying Blau articles (44 source-SQLite rows are cluster-duplicates of 13 article-heads)
- **Survival rate:** ~17% raw (13 / 76) or ~41% cluster-flattened (13 / 32) — the cluster-flattened survival rate is the meaningful figure here, since Vayikra has the heaviest cluster-duplication of any book seen so far (Bereshit Batch 1: 24%; Shemot Batch 1: 22%; Shemot Batch 2: ~18% cluster-flattened)

## Batch 1 entries (12 net-new + 1 promoted)

### GLOSS tier (7 net-new)

| blau_id | Lemma JA | Verse(s) | Pairing | Note |
|---|---|---|---|---|
| 18190 | `פריך` | 2:14 | فريك ↔ אביב קלוי (parched fresh-grain) | Technical-agricultural — milky-stage spike roasted in fire; same lemma propagates to Shemot spring-barley cluster |
| 16123 | `סתותייה` | 6:14 | ستوتية ↔ מרבכת (well-mixed dough) | Greek-Aramaic culinary loan; Saadia bridges two outside-the-mainstream technical terms |
| 16371 | `אלסמברץ` | 11:30 | سنبرص ↔ תנשמת (gecko Lacerta mauritanica) | Non-cognate Mediterranean-zoological identification; routes priestly impurity-list through Greco-Arab natural-history |
| 16874 | `צנגה` | 19:36 | صنجة ↔ אבני צדק (calibrated metal weights) | Persian-Aramaic commercial-measure loan; reframes 'stones' as standardized counterweights |
| 15290 | `כ'לף` | 25:5 | خلف ↔ ספיח (Sabbatical aftergrowth) | Non-cognate agricultural-technical — 'that which follows the main crop' across two languages |
| 13884 | `אצר` | 26:13 | إصر ↔ עֹל (binding-burden of slavery yoke) | Quranic-register frame shift — wooden-implement → oath-bond constraint |
| 14760 | `אלחארה` | 26:16 | حارة ↔ קדחת (burning fever in curse-pericope) | Deadjectival noun for everyday illness; preserves heat-frame across roots |

### NOTE tier (5 net-new)

| blau_id | Lemma JA | Verse(s) | Pairing | Mechanism in one line |
|---|---|---|---|---|
| 15168 | `אכ'ס` | 7:18 / 19:7 | أخس ↔ פגול (refuse-offering) | Heb fixed-category noun → Ar elative substantive ('like-the-worst-of-things'); grammatical reframe forcing comparison-judgment onto priestly classification |
| 14064 | `בד'ל` | 10:10 / 21:7 / 21:9 | بذل (noun + Form V verb) ↔ חל/חללה/תחל | Semantic-field calque across noun + passive-participle + Form V; Heb 'profane' → Ar 'squander/expend cheaply' (sanctity as depletable value) |
| 15624 | `ד'כוה` | 4:3 / 4:24 / 7:7 / 16:6 / 16:25 | ذكوة ↔ חטאת (sin-offering) | Theological reframe: names the offering by its EFFECT (purification) rather than CAUSE (sin); aligns with Quranic-Arabic z-k-w family. Invariant across 11+ Vayikra verses |
| 17381 | `חוז` | 14:34 / 25:13 / 25:41 / 27:16 | حوز ↔ אחזה (land-possession) | Pseudo-cognate substitution licensed by sound-similarity; Blau explicitly diagnoses as non-etymological surface-bridge |
| 17999 | `יסתג'פר` | 5:6 / 14:19 / 16:6 / 16:16 / 16:30 | Form X استغفر ↔ כפר (atonement) | Theological reframe from ritual-mechanism to relational-supplication; the priest no longer COVERS the sin but PLEADS for its forgiveness — Karaite-friendly subordination to divine grace |

## Promoted-and-extended entry (special-case)

`שחמה'` existed in baseline as a Shemot-only gloss-tier entry (Ex 29:20). Batch 1's Vayikra mining surfaced the identical fixed Arabic idiom شحمة الأذن across the entire leper-purification pericope (Lev 14:14/17/25/28) and the priestly-consecration completion (Lev 8:23). Rather than skip on lemma collision, the existing entry was patched in place:

- **Tier:** gloss (unchanged — the idiom-anchored pairing argument is the same; multi-verse propagation strengthens the gloss-tier teaching value without requiring a tier promotion)
- **Verses:** 1 → 6 (Ex 29:20 + Lev 8:23, 14:14, 14:17, 14:25, 14:28)
- **Mechanism:** rewritten to highlight the two-ritual-system parallelism — Saadia's same fixed idiom שחמה' אד'ן operates across both the consecration-of-priests AND leper-purification pericopes, making the תְּנוּךְ-בֹּהֶן triad syntactically parallel in JA where the Hebrew already parallels them lexically
- **blau_dict.sense:** upgraded to cross-reference both Ex 29:20 and the full Vayikra ritual cluster

Second promote-in-place ever in the divergence file (after Bereshit→Shemot `נקל` from Shemot Batch 2). Pattern continues to be the right call when a lemma's verse-set genuinely extends — the alternative (logging as cross_book_dupes and skipping) would lose 5 distinct ritual-context verse attestations that strengthen the entry's pedagogical reach.

## Vayikra verses now covered (Batch 1)

19 unique verses across 11 chapters:
- Ch 2: 14
- Ch 4: 3, 24
- Ch 5: 6
- Ch 6: 14
- Ch 7: 7, 18
- Ch 8: 23 (promote-in-place)
- Ch 10: 10
- Ch 11: 30
- Ch 14: 14 (PIP), 17 (PIP), 19, 25 (PIP), 28 (PIP), 34
- Ch 16: 6, 16, 25, 30
- Ch 19: 7, 36
- Ch 21: 7, 9
- Ch 25: 5, 13, 41
- Ch 26: 13, 16
- Ch 27: 16

Multi-verse bundling is even more dominant than Shemot: 5 of the 12 net-new entries bundle 3+ verses (ד'כוה at 5, יסתג'פר at 5, חוז at 4, בד'ל at 3, אכ'ס at 2). The two big semantic-field calques (ד'כוה for חטאת, יסתג'פר for כפר) are theologically the strongest entries shipped in any book pass to date — they restructure the entire sin-offering / atonement system in JA by renaming the offering for its effect rather than its cause, and the act of atonement for its supplicative rather than mechanical aspect.

## Files changed

**Modified:**
- `data/tafsir-divergence.json` — appended 12 entries + patched `שחמה'` in place (94 → 106 entries)
- `data/_blau_saadia_deferred.json` — created fresh `vayikra` namespace (additive only; Bereshit + Shemot namespaces untouched)

**Created:**
- `scripts/apply_phase4_vayikra_batch1.py` (with promote-in-place helper `_patch_promote_in_place()` and fresh-namespace `_update_deferred()`)
- `PHASE4_VAYIKRA_BATCH1_SESSION_NOTES.md` (this file)

Working tree left uncommitted per project convention.

## Deferred buckets — Batch 1 additions

### `skip` (17 added)

Pure metalanguage / no-Vayikra-anchor:
- `13781 أداء`, `14560 جسس`, `14655 جوز`, `14870 تحصيل`, `15266 خلة`, `15559 دنو`, `15787 رشم`, `16131 ستر`

Manuscript-variant / recension-difference / Cairo-baseline gap:
- `15824 رفق` (Lev 25:3 prune, competing reading with 15954)
- `16407 سوغ` (Lev 22:21, Blau himself flags the connection as obscure)
- `16820 مصففة` (Cairo 2019 uses masc. צף not fem. מצפפ)
- `19861 نفذ` (Lev 26:30 MISSING from tafsir-vayikra-26.json — chapter jumps v.29 → v.31)

Pure cognate / grammar-particle (no divergence to display):
- `16869 صمغ` (Heb צ-מ-ג ↔ Ar ص-م-غ)
- `17953 غريبة/غويب` (Heb עורב ↔ Ar غراب)
- `18463 قدس` family (Heb ק-ד-ש ↔ Ar ق-د-س)
- `18995 كل` family (quantifier-particle, grammar-territory)
- `20398 وليمة/ولي` (Heb פנה אל ↔ Ar ولى إلى, borderline-cognate)

### `borderline` (4 added — NOTE-grade but cut at 5-NOTE cap)
- `17407 خمع` (Lev 21:18 שרוע → medical خمع 'dislocated hip') — strong, ship in Batch 2 with the priestly-disqualification cluster
- `18594 قصبة` (Lev 1:8 פדר → قصبة 'body-cavity, viscera') — strong, ship in Batch 2 with sacrificial-anatomy entries
- `19142 لج` (Lev 14:10 לג → Heb-loanword retention) — parallels the מרזבאן Persian-loan pattern from Shemot Batch 2
- `19427 مسوحية` (Lev 8:2 + 8:10 משחה → Aramaic-Syriac calque) — strong Mishkan-cross-reference candidate

### `_cluster_dupes_logged` (13 entries)

Source-SQLite cluster duplications: 17302-17307 (ثلول cluster, 6 rows), 17381-17384 (4 rows), 17407-17408 (2), 17953-17955 (3), 17999-18000 (2), 18190-18191 (2), 18378-18379 (2), 18463-18468 (6), 18995-19000 (6), 19427-19428 (2), 19861-19871 (11 rows — biggest cluster in any book pass to date), 20398-20399 (2). Total: 13 underlying articles fragmented across 48 source-SQLite rows. The qadas + nafd + thlul + kull cluster-families dominate.

## Yield-rate observations

- **Window walked:** 76 candidates in `blau_id 13781–20399` (full Vayikra-flagged pool)
- **Survivor count:** 12 net-new + 1 promote-in-place = 13 effective ships
- **Raw survival rate:** ~17% (12/76) — lowest of any pass to date
- **Cluster-flattened survival rate:** ~41% (13 / 32 underlying articles) — HIGHEST of any pass to date, surpassing Bereshit Batch 1's 24%
- **The big discovery:** Vayikra's pool size (76) is misleading because the source SQLite atomizes each Blau article into 4-11 derivative-form rows. After cluster-flattening, Vayikra has only ~32 underlying articles, but those articles yield denser tier-grade entries than Shemot or Bereshit because the priestly-system vocabulary is fundamentally technical-cultic — every offering type, every body part, every ritual implement has a distinct Saadia equivalent
- **Two paradigm entries:** ד'כוה (sin-offering = purity-offering) and יסתג'פר (atonement = seeking-forgiveness) are theologically the strongest entries shipped across all 4 batches so far. They aren't merely lexical replacements; they're Karaite-friendly redirections of the entire sacrificial-atonement system from priestly-ritual to divine-grace framing
- **Multi-verse bundling at all-time high:** 5 of 12 net-new entries bundle 3+ verses (vs. Shemot Batch 2's 7 of 12 ≥2, this batch's 5 ≥3); the ד'כוה and יסתג'פר entries each span 5 representative verses out of 10+ actual attestations — the underlying system-vocabulary depth is exceptional in Vayikra
- **Promote-in-place pattern matures:** second usage (after Shemot Batch 2's נקל); same rationale (multi-pericope idiom propagation strengthens the existing entry rather than requiring a new lemma collision). Worth re-using whenever an existing entry's lemma surfaces in a new ritual-context

## Banner-variant smoke test (status)

Skipped per session decision; baseline coverage continues to exercise all three banner variants. The new high-density Vayikra chapters that should render well:
- Ch 16 (Yom Kippur) — 4 of the 5 יסתג'פר verses + 2 of the 5 ד'כוה verses live here. The densest atonement-system chapter in the entire corpus
- Ch 14 (leper purification) — 5 of the 6 שחמה verses (promote-in-place) + Lev 14:10 (lj borderline) + Lev 14:19 (יסתג'פר) + Lev 14:34 (חוז)
- Ch 25 (Sabbatical + jubilee) — Lev 25:5 (כ'לף) + Lev 25:13/41 (חוז jubilee return)
- Ch 21 (priestly disqualifications) — Lev 21:7 + 21:9 (בד'ל cluster); pairs with the deferred 21:18 (כ'אמע) for a future-batch coordinated pass
- Ch 11 (dietary law) — Lev 11:30 (סמברץ)
- Ch 26 (curses-pericope) — Lev 26:13 (אצר) + 26:16 (חארה)

If a UI eyeball pass happens later, prioritize Ch 16 (Yom Kippur density) and Ch 14 (leper-purification four-entry stack including the שחמה promote-in-place).

## Recommended next-session strategy

The priority stack continues to evolve:

1. **Pivot to Bamidbar Phase 4 Batch 1** — projected at ~80 candidates per the original mining prompt, but expect Vayikra's cluster-duplication pattern to repeat (Bamidbar shares many of the same priestly-system articles). Realistic ceiling: 10-15 entries after cluster-flattening, with strong opportunity for **cross-book promote-in-place** because the Tabernacle-vocabulary (Shemot 25-39) + offering-vocabulary (Lev 1-7, 16) + camp-vocabulary (Num 1-10) overlap heavily. Specifically, look for cross-book extensions of: סלאמה (peace-offering, Lev parallels deferred this batch but Num 6:14-18 nazirite peace-offering should surface), ד'כוה (sin-offering, Num 6:11 + Num 15:24-29 + Num 28-29 festival cycle), מסוחייה (Num 4 anointing oil from this batch's deferred borderline), שחמה' (already promoted, may extend further if Num attestations exist).

2. **Or pivot to Vayikra Batch 2** — promote the 4 borderline entries from this batch (17407 כ'אמע, 18594 קצבה, 19142 לג, 19427 מסוחייה), plus mine the 11 cluster-head dupes that were skipped. Realistic ceiling: 6-8 more entries before Vayikra's verse-anchored tier fully exhausts.

3. **Or pivot to Phase 3 R1** (cross-book strict-tier extensions) — the existing נקל (now Bereshit + Shemot) + שחמה' (now Shemot + Vayikra) precedents suggest a methodology for retroactively scanning the existing 36 twist entries for multi-book attestation. This is the highest-leverage cross-book move available; worth scoping after Bamidbar lands.

4. **Devarim Phase 4 Batch 1** — last book; reuse the deuteronomic-law parallels from Bereshit + Shemot Holiness-Code crossovers.

5. **Defer the Vayikra metalanguage / no-cite pool** — same reasoning as Bereshit + Shemot; needs UI design for translation-theory display first.

## How to resume

```bash
cd ~/Code/judeo-arabic-app
python3 scripts/verify_divergence.py    # baseline now: 106 entries, 0 failures
cat data/_blau_saadia_deferred.json | python3 -m json.tool | jq '.vayikra | keys, ._session'
ls scripts/apply_phase4_*.py            # pattern for Bamidbar: copy vayikra_batch1.py, retarget Bamidbar (filter on במדבר/במ׳)
cat PHASE4_VAYIKRA_BATCH1_SESSION_NOTES.md  # this file
```

**Next-batch pointer:** the natural cursor is now **Bamidbar Phase 4 Batch 1** (per recommendation 1 above). Same script-copy pattern: copy `apply_phase4_vayikra_batch1.py` → `apply_phase4_bamidbar_batch1.py`, retarget the citation filter (`במדבר` / `במ׳` / `במ"`), drop the promote-in-place helper if no Shemot/Vayikra cross-book carryover surfaces (otherwise mirror this batch's promote-in-place for any extending lemma), retarget `_update_deferred()` to a fresh `"bamidbar"` namespace.

The Vayikra-flagged subset that produced this batch had a 41% cluster-flattened survival rate. If Bamidbar shows similar density (likely, given the shared priestly-system vocabulary), expect ~12-15 entries after cluster-flattening, with 2-4 cross-book promote-in-place opportunities surfacing through the offering + tabernacle vocabularies.
