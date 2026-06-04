# Next-step prompt — Phase 3 R1 Second Wave: Bamidbar + Devarim

Paste-ready for a fresh Claude Code session in `~/Code/judeo-arabic-app`. Picks up the
tafsir-divergence R1 second wave where the 2026-05-30 session left off (Shemot + Vayikra
batches shipped). Goal: finish the wave by activating the verifier's per-book quality
gate for the last two books, **Bamidbar** then **Devarim**.

---

## The prompt

Continue the **Phase 3 R1 second wave** of tafsir-divergence mining in
`~/Code/judeo-arabic-app`. The wave adds ≥5 net-new **TWIST-tier** entries per book so the
verifier's per-book quality gate activates uniformly. Shemot and Vayikra are done; do
**Bamidbar** first, then **Devarim**, as two separate batches.

### Re-confirm state first (don't trust blindly)

Last session's tool-output buffering has scrambled before. Run:
```
git -C . status --short
python3 -c "import json,collections;d=json.load(open('data/tafsir-divergence.json'));print(len(d['entries']),collections.Counter(e['tier'] for e in d['entries']))"
python3 scripts/verify_divergence.py | tail -12
```
Expected baseline: **135 entries (47 twist / 38 note / 50 gloss)**, verifier **PASS, 0
warnings**, branch `advanced-library-kuzari`, working tree uncommitted (project
convention). The per-book mix should read Bereshit 35 · Shemot 6 · Vayikra 5 · Devarim 1
(Bamidbar shows only if it has twists — currently 2).

### How the gate works (critical)

The verifier assigns each twist to ONE book = **`verses[0].book`** (the FIRST cited
verse). A book's quality bar activates only at **≥5 twists** and then enforces:
**≥70% backed (direct+adjacent) · ≥45% direct · ≤30% no-citation**. Cross-book entries
anchored in another book do NOT count toward the target book. So to clear a 5-entry
batch: aim for **≥4 direct/adjacent, ≤1 no-cite**.

### Done last session (2026-05-30) — your templates

- `scripts/apply_phase3_r1_shemot.py` — Shemot +5 TWIST (gate active+clear). See
  `PHASE3_R1_SECONDWAVE_SHEMOT_SESSION_NOTES.md`.
- `scripts/apply_phase3_r1_vayikra.py` — Vayikra +5 TWIST (gate active+clear). See
  `PHASE3_R1_SECONDWAVE_VAYIKRA_SESSION_NOTES.md`. **Use this as the per-book apply
  template** — swap `NEW_ENTRIES` and the book; it already has the `_log_deferred`
  helper (phase3_r1_consumed + no_cite_audit).

### The two highest-yield TWIST archetypes (Blau-direct)

1. **Hebrew-driven calque** — an Arabic root loaded with its Hebrew cognate's extra
   sense (e.g. אגתחד: جحد "deny" → "destroy", tracking Heb כחד; פיצ'הא: فيض "overflow" →
   "genital flux", tracking Heb זוב). Blau flags these and is `direct`.
2. **Aramaic-driven calque** — an Arabic root chosen for its *Aramaic* sense, which Blau
   labels "ארמית/בבלית" (e.g. תרפק: رفق "be gentle" → "prune" via Aramaic רפק "dig").
   Invisible from Arabic alone; Blau is `direct`.

Also reliable: **anti-anthropomorphic** attribute substitutions (אלמהל: ארך אפים →
طويل المهل); **vernacular-sense realia** identifications where Blau cites Muḥīṭ al-Muḥīṭ
(אלכ'אמע: שרוע → "dislocated-hip"). And **one demythologizing/midrashic identification
per book may ship no-cite** (שיאטין: שעירים → demons; matches existing אשראף/קרדא/אתון
precedent — Blau won't lemmatize an exegetical identification).

### Batch A — Bamidbar (do first)

Bamidbar currently has 2 first-verse twists → needs **≥3 net-new** (ship 3–5 to clear
comfortably; with 2 legacy entries, check their relations first via the verifier output
and top up so the combined mix clears ≥45% direct / ≥70% backed / ≤30% no-cite).

- **Free win — cross-book promote-in-place, NOT a new entry:** the Shemot `אלמהל` entry
  (אֶרֶךְ אַפַּיִם → طويل المهل) recurs at **Num 14:18** (וַיהוָה אֶרֶךְ אַפַּיִם). Extend
  that entry's `verses[]` (+ mechanism note) rather than authoring a new one — use the
  `PROMOTE_IN_PLACE` pattern from `scripts/apply_phase4_devarim_batch1.py` /
  `apply_phase3_r2_batch1.py`. (This does NOT add a Bamidbar first-verse twist, since
  אלמהל is Shemot-anchored — it's a corpus-quality win, separate from the gate count.)
- **Net-new Bamidbar twists:** mine the wilderness-narrative, nazirite (Num 6), census,
  and Balaam-oracle (Num 22–24) vocabulary. The Balaam oracles are an especially rich
  TWIST seam (poetic/prophetic register, divine-name handling).

### Batch B — Devarim (do second)

Devarim currently has 1 first-verse twist → needs **≥4 net-new**.

- **Faster path — promote existing NOTEs to TWIST:** three TWIST-adjacent Devarim NOTEs
  already shipped (`אקרץ'` conquest-extermination, `יסיב` shemittah-release, `ממתעה`).
  Re-verify each against Blau; if the divergence is genuinely paradigm-shifting (per
  Devarim B1 next-strategy #3), promote tier `note`→`twist` in place. Promotions count
  toward the Devarim first-verse gate IF the entry's `verses[0].book` is Devarim — check
  each. **A tier flip is an entry mutation, not a new entry** — write a small in-place
  patch (find by lemma_ja, set `tier`), don't append.
- **Net-new Devarim twists:** mine the Mosaic-discourse rationalist-philosophical
  register (Devarim's documented signature — political/institutional vocabulary recast
  as moral-epistemological deviation, etc.).

### Per-book workflow (same as Shemot/Vayikra)

1. **Mine** — launch a general-purpose subagent over `data/_blau_saadia_candidates.json`
   (1596 OCR'd Blau Saadia-citing candidates: fields `blau_id, root_ar, root_he,
   body_excerpt, saadia_citation_lines`). Filter on the book's Saadia-citation pattern
   ("רס״ג לבמדבר" / "במדבר" ; "רס״ג לדברים" / "דברים"). Have it VERIFY each surface in the
   corpus and return ~10–12 ranked, with blau_id / lemma / Heb word / verse / ja+hebrew
   snippet / Blau gloss / Lane sense / tier rationale / VERIFIED flag.
2. **Curate + verify yourself (no fabrication)** — re-pull every surface from
   `data/tafsir-{book}-{ch}.json` (fields ch/v/ja/hebrew); confirm each cited verse has a
   token that resolves via the verifier's `candidate_chain` (it strips leading ו / אל /
   one of ב·ל·כ·פ, + final-letter & trailing-`'` normalization — see
   `scripts/verify_divergence.py:40-100`). Set `variants[]` to cover every cited verse's
   surface token. **Trailing-`'` gotcha:** a lemma ending in `'` never matches — drop it
   (e.g. `מתרבץ`, not `מתרבץ'`). **Diff proposed lemma_ja against the consumed set FIRST**
   (`{e['lemma_ja'] for e in entries}`) — a colliding lemma_ja is silently skipped on
   append (cost Vayikra its כ'לף candidate). AVOID roots already used in entries touching
   the book.
3. **Author + apply** — copy `apply_phase3_r1_vayikra.py` → `apply_phase3_r1_bamidbar.py`
   (then `_devarim.py`). Each entry: `lemma_ja, variants, lemma_ar, root` (Arabic-script
   hyphenated, e.g. `ج-ح-د`), `tier:"twist"`, `classical_en/he`, `saadia_en/he`,
   `mechanism` (~200–280 words, honest about the divergence), `verses[]` (capitalized
   book names), `sources` (legend keys only: lane / saadia-direct / blau-dict /
   blau-festschrift), and `blau_dict:{root,sense,relation}` with relation ∈
   {direct,adjacent,different-sense}. No-cite entries omit `blau_dict` and use
   `sources:[lane,saadia-direct]`; log the decision in
   `_blau_saadia_deferred.json#/no_cite_audit/phase3_r1_no_blau`. Log consumed blau_ids
   in `#/phase3_r1_consumed`. Write-back idiom: `json.dumps(payload,
   ensure_ascii=False, indent=2) + "\n"`, then re-parse.
4. **Gates** — `python3 scripts/verify_divergence.py` must report **PASS, 0 warnings**
   and show the target book's mix clearing the thresholds; `npm run build` clean.
5. **Session notes** — `PHASE3_R1_SECONDWAVE_{BAMIDBAR,DEVARIM}_SESSION_NOTES.md`
   following the Shemot/Vayikra template (snapshot table · per-entry rundown · deferred
   buckets · gates · yield observations · next-session pointer).

### Hard constraints / conventions

- **Verify Blau before citing.** Before any `blau-dict` source / `blau_dict` block,
  confirm Blau actually has the sense via the `arabic-lexicon` skill (slug
  `blau-judeoarabic`). If absent → `sources=[lane, saadia-direct]`, no `blau_dict`, log
  in `no_cite_audit`. Never fabricate (precedents: אתון verifier-crash, תגלא, שיאטין).
- **Read actual Saadia surface forms from the corpus** — never hand-author the JA.
- **Working tree stays uncommitted.** One session-notes file per batch.

### After this — the wave is complete

Once Bamidbar and Devarim both clear, all 5 books have active+passing per-book gates.
Remaining deferred items for future passes (logged in the Vayikra session notes):
re-mine Vayikra `כ'לף` via promote-in-place; the deferred Vayikra identification-TWISTs
(Azazel→Mount Azaz Lev 16:8/10; אני יהוה→"God the Punisher"; נפש בדם→"blood is the
soul's dwelling" 17:11); optional reader back-pointer אורד↔תגלא.

Pick up at **Batch A — Bamidbar**.
