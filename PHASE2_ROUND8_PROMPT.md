# Phase 2 Round 8 — continue inline long-tail sweep (target ~80–82% hand; unlock Camel-badge retirement)

Paste-ready prompt for a fresh Claude Code session. Picks up where Round 7
landed on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

- Round-4 origin prompt: `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`.
- Round-4 B+C resume prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`.
- Round-5 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND5_PROMPT.md`.
- Round-6 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND6_PROMPT.md`.
- Round-7 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND7_PROMPT.md`.
- Round-6 plan: `~/.claude/plans/lets-do-code-judeo-arabic-app-phase2-rou-hidden-lampson.md`.
- Memory: "Phase 2 Round 7 — H + 8× inline I chunks SHIPPED 2026-05-28"
  inside `judeo-arabic-app-project.md`.

**Round 7 final state (uncommitted in working tree):**
- Hand-coverage **76.68%** (Round-7 delta +4.40 pts on inline-Opus sweep).
- Covered total **79.99%** (within 0.01 of 80% global covered).
- Lane entries **657** (was 487 at Round-6 end; +170 across H + 8 chunks).
- Per-book: bereshit 74.76 · shemot 77.16 · vayikra 78.11 · bamidbar
  **80.67 (HAND CROSSED 80% — first per-book to do so; covered 83.07%)** ·
  devarim **73.27 (still laggard, +4.18 pts in Round 7)**.
- `npm run build` clean (213 pages). `verify_divergence.py` exit 0
  (pre-existing Bereshit-mix soft warning unchanged). `scope_saadia_notes.py`
  0 residual hits. Lookup spot-check passed 29/29 (including the resolved
  tokenizer-artifact pair `רת'` / `פרג'`).

**Top 25 misses going into Round 8** (the queue this round attacks):

```
  9  אלה                   [standard]    — household-of (ahl-hu); PATCH on ahl-family
  8  וא                    [w-prefixed]  — ortho-artifact in `אכת'ר וא עצ'ם` — investigate
  7  עד                    [standard]    — ʿudd "count!" imperative; PATCH ʿadad-number
  7  איה                   [standard]    — Aiah (Gen 36:24); proper noun
  7  טרקה                  [standard]    — ṭuruqahu (his ways); PATCH (already partial)
  7  ועלק                  [w-prefixed]  — wa-ʿallaq "and hang up" (Tabernacle veil); Form II
  7  עמדהא                 [standard]    — ʿumudahā "its pillars"; new noun ʿamūd
  7  אלאימן                [standard]    — al-ayman "the right (side)"; new yamin
  7  אלאיימה               [standard]    — al-aʾimma alt-spell; PATCH aimma-priests
  7  ויד'בחה               [w-prefixed]  — wa-yadhbaḥuhu; PATCH dhabaḥa
  7  עמיק                  [standard]    — ʿamīq "deep" (of skin-lesion); new adj
  7  יתפש                  [standard]    — yatfish "spreads" (lesion); new verb tafasha
  7  אלעצפור               [standard]    — al-ʿuṣfūr "the bird" (leper-rite); new noun
  6  נחשון                 [standard]    — Nahshon ben Amminadab; proper noun
  6  עמינדב                [standard]    — Amminadab (Judah's chief); proper noun
  6  אליסף                 [standard]    — Eliasaph (Gad/Levi chief); proper noun
  6  יכונאן                [standard]    — yakūnāni dual; PATCH kana-be
  6  מראחלהם               [standard]    — marāḥiluhum "their journey-stages"; new
  6  קסמת                  [standard]    — qasamtu "I apportioned/divided"; new verb
  6  עקובה                 [standard]    — ʿuqūba "punishment"; new noun
  6  יאכלונה               [standard]    — yaʾkulūnahu; PATCH akala-eat
  6  ואכ'בר                [w-prefixed]  — wa-akhbara "and he informed"; new Form IV
  6  אלענב                 [standard]    — al-ʿinab "the grapes"; new noun
  6  חמאה                  [standard]    — Hamath (Num 13:21, 34:8); proper noun
  6  ת'מרה                 [has-apos]    — thamarahu "its fruit"; new noun
```

**Diagnosis.** Head count is much flatter than R6/R7 start (top miss 9 down
from 14 at R7 start). Roughly half the top-25 are pure new lemmas, half are
patches on existing entries. From Round 7's evidence, each inline-Opus entry
yields ~0.025 pts of hand-coverage (down from R6's 0.035 — diminishing
returns as the queue thins). To push 76.68% → 80% (closing the Camel-badge
retirement gate) needs ~130 more entries, roughly 5–6 chunks of the same
scale.

Round 8 splits the work into the same two phases that worked in R6 + R7,
but the head-cleanup phase keeps shrinking (most R8 head items are patches,
not new entries):

1. **Batch J — head hand cleanup** (~10–12 entries, ~+0.2–0.4 pt).
   ~5 new lemma entries (Aiah, ʿallaqa, ʿamūd, yamīn, ʿamīq, tafasha,
   ʿuṣfūr, Nahshon, Amminadab, Eliasaph, marḥala, qasama, ʿuqūba, akhbara,
   ʿinab, Hamath, thamara) + ~5 variant patches (ahl, ʿadad, ṭarīq, aimma,
   dhabaḥa, kāna, akala-eat).

2. **Batch K — continue inline Opus sweep** (~5–6 chunks of 25, ~+3–5 pt
   target). Same pattern as Round 7 Batch I: pull 25 candidates, look up
   contexts, preflight lemma collisions (against both starter AND lane),
   write apply script in `scripts/apply_round8_K_chunkN.py`, apply.

**Round-8 target: 76.68% → ~80–82% hand.** Stretch goal hand ≥ 80% globally
unlocks the Camel auto-dict badge retirement (which is the cleanup task
that's been deferred since Round 5). Bamidbar HAND is already at 80.67% —
a per-book Camel retirement (Bamidbar-only) is a smaller-scope alternative
if global stalls.

---

## Batch J — head-of-queue hand cleanup (~12 entries)

### Step 1: Confirm the top-25 still match `data/coverage-misses.json`

```bash
cd ~/Code/judeo-arabic-app
python3 -c "
import json
m = json.load(open('data/coverage-misses.json'))['misses']
for e in m[:25]: print(f\"  {e['count']:3d}  {e['surface']:20s}  [{e['bucket']}]\")"
```

### Step 2: Verify 1–2 context verses per candidate via the helper

```bash
python3 - <<'PY'
import json
ctx = json.load(open('/tmp/ja-context-index.json'))
for tok in ['אלה','עד','איה','טרקה','ועלק','עמדהא','אלאימן','אלאיימה',"ויד'בחה",'עמיק','יתפש','אלעצפור','נחשון','עמינדב','אליסף','יכונאן','מראחלהם','קסמת','עקובה','יאכלונה',"ואכ'בר",'אלענב','חמאה',"ת'מרה"]:
    hits = ctx.get(tok, [])[:1]
    if not hits: print(f"  {tok}  — no ctx in index"); continue
    h = hits[0]; print(f"  {tok}  → {h['book'][:3]} {h['ch']}:{h['v']}  {h['text'][:120]}")
PY
```

If `/tmp/ja-context-index.json` is missing (it lives in `/tmp` and gets
wiped between sessions), rebuild it:

```bash
python3 scripts/build_ja_context_index.py
```

### Step 3: Preflight lemma collisions (CRITICAL — preflight starter AND lane)

```bash
python3 - <<'PY'
import json
d = json.load(open('data/dictionary-lane.json'))
d2 = json.load(open('data/dictionary-starter.json'))
proposed = [...]  # your candidate lemmas
for lemma in proposed:
    for src, dd in [('lane',d),('starter',d2)]:
        hits = [e for e in dd['entries'] if e.get('lemma_ja') == lemma]
        variants = [e for e in dd['entries'] if lemma in (e.get('variants') or [])]
        if hits or variants:
            print(f"  {lemma:12s}  ⚠ {src}: {[e['id'] for e in hits+variants]}")
            break
    else:
        print(f"  {lemma:12s}  ✓ free")
PY
```

**LESSON FROM R7:** the chunk-2 wajh patch silently FAILED because `wajh`
lives in `dictionary-starter.json`, not lane — but the apply script only
walked lane. The fix landed as a manual patch script + the chunk-3 apply
template added `STARTER_VARIANTS_PATCH`. Preflight MUST check both dicts
or you'll waste a `scripts/apply_round8_*.py` round-trip.

### Step 4: Author `scripts/apply_round8_J.py`

Same three-bucket shape as `scripts/apply_round7_I_chunk3.py` (the
canonical template after R7): `NEW_ENTRIES`, `VARIANTS_PATCH` (lane),
`STARTER_VARIANTS_PATCH`. Always include the homograph-warning path —
multiple R7 chunks added second senses on existing lemmas (umm-mother
alongside am-or-particle, ʿijl-calf alongside ʿagalah-wagon, burr-wheat
alongside barr-wilderness, amah-maidservant alongside umma-nation).

### Step 5: Validate JSON + re-scope notes

```bash
python3 -c "import json; json.load(open('data/dictionary-lane.json')); json.load(open('data/dictionary-starter.json'))"
python3 scripts/scope_saadia_notes.py
# Optionally re-run coverage_report.py to measure Batch J delta on its own,
# but it's slow (~3-4 min) — easier to bundle the measurement with Batch K.
```

The R7 audit auto-migrated 25 entries (11 had Saadia leak in `gloss_en` —
all rewritten cleanly, 0 residual hits). The `scope_saadia_notes.py`
gloss-rewrite path is now reliable; don't sweat parenthetical Saadia
mentions during chunk authoring — they'll get moved automatically.

---

## Batch K — continue inline long-tail sweep (5–6 chunks of 25)

### Step 1: Regenerate candidates from the post-J miss queue

```bash
python3 scripts/coverage_report.py    # ~3-4 min; refresh after J
python3 - <<'PY'
import json
m = json.load(open('data/coverage-misses.json'))['misses']
out = [{"token": e["surface"], "count": e["count"], "bucket": e["bucket"]} for e in m]
json.dump(out, open('/tmp/ja-candidates.json','w'), ensure_ascii=False, indent=2)
print(f"Wrote {len(out)} candidates")
PY
python3 scripts/build_ja_context_index.py   # refreshes /tmp/ja-context-index.json
```

### Step 2: Per-chunk loop (target 5–6 iterations)

For each chunk N (1..6):

```bash
# Pull next 25 not-yet-covered candidates with contexts
python3 - <<'PY'
import json, re
def normalize(t):
    t = re.sub(r'^[.,:;؛،"\'\s]+|[.,:;؛،"\'\s]+$', '', t)
    if t.startswith('ו') and len(t) > 1: t = t[1:]
    if t.startswith('אל') and len(t) > 2: t = t[2:]
    return t
covered = set()
for fn in ['data/dictionary-starter.json', 'data/dictionary-lane.json']:
    d = json.load(open(fn))
    for e in d.get('entries', []):
        for k in (e.get('lemma_ja'), normalize(e.get('lemma_ja',''))):
            if k: covered.add(k)
        for v in (e.get('variants') or []):
            covered.add(v); covered.add(normalize(v))
candidates = json.load(open('/tmp/ja-candidates.json'))
ctx = json.load(open('/tmp/ja-context-index.json'))
batch = []
for c in candidates:
    tok = c['token']
    if tok in covered or normalize(tok) in covered: continue
    batch.append({**c, 'contexts': ctx.get(tok, [])[:2]})
    if len(batch) >= 25: break
print(json.dumps(batch, ensure_ascii=False, indent=1))
PY
```

For each chunk:
1. Walk the 25 candidates inline; gloss each per Round-6/7 rules:
   - `gloss_en` carries the **classical Arabic** sense only — no Saadia
     calques. The audit pass at end-of-round will catch + auto-rewrite
     any slips into the gloss text (reliable as of R7), but cleaner if
     you avoid them at authorship time.
   - Saadia-specific commentary → `saadia_note` (Advanced reader hides it).
   - Function words → `root: "—"`, pos = `particle`/`conjunction`/`preposition`.
   - Proper nouns → `pos: "proper noun"`, `root: "—"`.
   - Inflected forms covered as variants on the base lemma, not separate
     entries (lemma_ja = base form).
   - `source: "lane"` for everything.
2. **Preflight lemma collisions against BOTH dicts** — use the snippet
   from Batch J Step 3.
3. Write `scripts/apply_round8_K_chunk<N>.py` with `NEW_ENTRIES` +
   `VARIANTS_PATCH` + `STARTER_VARIANTS_PATCH`. Run it.
4. Validate JSON round-trip. Move to next chunk.

After all chunks:

```bash
python3 scripts/scope_saadia_notes.py    # auto-migrate + auto-rewrite (reliable)
python3 scripts/verify_divergence.py     # exit 0 expected (Bereshit-mix warning OK)
python3 scripts/coverage_report.py       # final hand_pct
npm run build                            # 213+ pages clean
```

---

## Per-batch workflow (unchanged from R7)

1. **Refresh misses if dict changed:** `python3 scripts/coverage_report.py`
   (~3–4 min). Skip if no dict changes since last run.
2. **Build candidate file + context index** with the snippets above.
3. **Preflight lemma collisions** before authoring each chunk — check
   BOTH dictionary-lane.json AND dictionary-starter.json.
4. **Validate JSON round-trip** after each apply.
5. **Build check at end of round:** `npm run build` must stay clean.
6. **No commit.** Working tree carries Round 4 + 5 + 6 + 7 + 8 (uncommitted).

---

## Verification at end of Round 8

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 80%**
  (stretch ≥ 82%). If global hand crosses 80%, do the Camel-badge
  retirement diff (see "After Round 8" below).
- `python3 scripts/verify_divergence.py` exits 0.
- `python3 scripts/scope_saadia_notes.py` reports 0 residual hits.
- `npm run build` clean.
- Lookup spot-check: same shape as R7 — author a one-off
  `scripts/_spot_check_round8.ts` covering 15–20 previously-missing
  surface forms from this round, run via `npx tsx`, delete after.
- Spot-check 3 random tafsir chapters in dev (`npm run dev`):
  - `/tafsir/vayikra/13` for עמיק (deep) + יתפש (spreads) + אלעצפור
  - `/tafsir/bamidbar/1` for נחשון / עמינדב / אליסף
  - `/tafsir/devarim/10` for טרקה (his ways)
  Confirm previously-missing tokens now open the gloss panel.

## Gotchas (carry-overs from Round 6 + 7)

- **Always preflight-check BOTH dicts.** The R7 wajh-in-starter mistake
  cost a round-trip and a manual patch script. The chunk-3 apply pattern
  with `STARTER_VARIANTS_PATCH` is the durable fix — use it from chunk 1.
- **Trailing-apostrophe-suffix lemmas are real, not artifacts.** R7's
  `רת'` (count 14 at R6 end) and `פרג'` (count 10) appeared in misses
  under their apos-stripped bare forms (`רת`, `פרג`). They ARE legitimate
  lemmas whose surface ends in `'` — `lib/tokenize.ts#stripPunct` trims
  trailing `'` before `coverage_report.py` indexes the miss, but
  `normalizeFinals` collapses trailing `'` on the DICT side too, so adding
  the apostrophed lemma resolves both surface forms. If you see a
  count-≥10 surface with no context hits, before declaring "tokenizer bug,"
  check whether an apos-suffixed form exists in the corpus — `grep -c
  "TOKEN'" data/tafsir-*.json`. R7 also resolved this for `רת'`
  via Blau §1367 (= Heb פר, young bull, Saadia coinage).
- **Homographs are fine** — multiple R7 chunks added second senses on
  existing lemmas: amah-maidservant ≠ umma-nation (both lemma אמה),
  umm-mother ≠ am-or-particle (both אם), ʿijl-calf ≠ ʿagalah-wagon (both
  עגל), burr-wheat ≠ barr-wilderness (both בר). The apply-script's
  `[HOMOGRAPH]` warning is informational, not an error. UI surfaces both
  senses on tap.
- **Form-distinction verbs matter.** R7 added 5 new Form-distinct verbs
  (akhraja F-IV ≠ kharaja F-I, tahhara F-II ≠ tahara F-I, irtafaʿa
  F-VIII ≠ rafaʿa F-I, irtada F-VIII, jaza F-III). When a candidate is
  a clearly-different verb form than the existing Form-I entry, add a
  new entry rather than dumping inflections onto the wrong stem.
- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts` policy).
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note` (auto-migrated by `scope_saadia_notes.py`). R7's audit
  pass auto-rewrote 11 gloss_en cells with parenthetical Saadia mentions
  — the pass is now reliable; you don't need to manually rewrite them.
- **`coverage_report.py` runs ~3–4 min** (npx tsx warmup × 187 chapters).
  Skip the pre-batch refresh if the dict hasn't changed since the
  snapshot.
- **`/tmp/ja-candidates.json` and `/tmp/ja-context-index.json` get wiped
  between sessions.** Rebuild via the snippets above +
  `scripts/build_ja_context_index.py` (durable). Apply scripts go in
  `scripts/`, not `/tmp/`.
- **The `וא` count-8 miss** is likely a tokenizer / OCR artifact
  (appears in `אכת'ר וא עצ'ם` — most likely a junk-split of some
  cliticized form). Investigate via raw-text grep before adding a lemma.
  If it really is just an artifact, leave it for a `lib/tokenize.ts`
  patch instead of polluting the dict.
- **Round-7 lesson — inline-Opus yield is ~0.025 pts/entry** (down from
  R6's 0.035 — diminishing returns). Realistic gain for 5–6 chunks
  (~125–150 entries) is +3–4 pts. Project Round-8 final at 79.5–80.7%
  hand. The 80% global mark may need an extra chunk if luck is bad.

## ID cleanups still worth bundling in (low priority)

Both surfaced in R6, still unfixed:
- `naqis-defective` → should be `najis-unclean` (root n-j-s, not n-q-ṣ).
- `ʿaqd-covenant` → should be `ʿahd-covenant` (the lemma + gloss are
  already correct; only the id mismatches).

Rename via a small fix-up script — these are not blockers but they'll
mislead future grepping.

## After Round 8

- **If global hand ≥ 80% at end of round 8: do the Camel-badge retirement
  diff.** Per Round-6/7 prompt notes:
  - `app/tafsir/reader.tsx:613-644` — `SourceBadge` "camel" branch:
    either drop the branch entirely (preferred — `source: "camel"` no
    longer renders) or repurpose to a "removed" tooltip.
  - `lib/lookup.ts:177-183` — skip Priority-3 auto lookup (the
    `AUTO.filter(...)` block at the end of `lookup()`).
  - Verify with `npm run build` + a dev spot-check on 2–3 chapters that
    previously surfaced auto-dict matches: those tokens should now show
    the empty-state "Not in the dictionary yet" panel.
- **If only Bamidbar hand ≥ 80% (not global):** consider a per-book
  Camel-retirement gate in `lib/lookup.ts`. Add an optional `book?:
  string` argument to `lookup()`, threaded down from the reader, and
  skip the Priority-3 AUTO loop when `book === "bamidbar"`. Trade-off:
  per-book gating is more code than the global one-line skip, but it
  ships the cleanup earlier for the book that earned it.
- **Phase 3 (divergences 32 → ~180).** Runs on
  `data/tafsir-divergence.json`. Doesn't touch dict files; can run in
  parallel with dict expansion.
- **Phase 4 (Word-of-the-Day homepage card).** Year-mixed deterministic
  seed; pulls from lane dict; shows on `app/page.tsx`. Independent
  files.
- **One-off pickup:** the `וא` count-8 surface — confirm artifact via
  raw-text grep, then decide whether to patch `lib/tokenize.ts` or just
  ignore.

---

**Tell Claude:** "Resume Phase 2 Round 8 per
`~/Code/judeo-arabic-app/PHASE2_ROUND8_PROMPT.md`. Run Batch J first
(hand-curate ~12 head-of-queue lemmas + variant patches; preflight
against BOTH starter and lane), then Batch K (5–6 inline chunks of ~25
candidates each, no API spend), reporting coverage delta after each.
Final spot-check 3 chapters in dev. If global hand ≥ 80% at end of
round, do the Camel-badge retirement diff. If only Bamidbar crosses 80%,
hold the retirement diff for Round 9."
