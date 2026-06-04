# Phase 2 Round 7 — continue inline long-tail sweep (target ~76–80% hand)

Paste-ready prompt for a fresh Claude Code session. Picks up where Round 6
landed on 2026-05-28 in `~/Code/judeo-arabic-app/`.

---

## Context (read first)

- Round-4 origin prompt: `~/Code/judeo-arabic-app/PHASE2_ROUND4_PROMPT.md`.
- Round-4 B+C resume prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND4_BC_PROMPT.md`.
- Round-5 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND5_PROMPT.md`.
- Round-6 prompt (done): `~/Code/judeo-arabic-app/PHASE2_ROUND6_PROMPT.md`.
- Round-6 plan: `~/.claude/plans/lets-do-code-judeo-arabic-app-phase2-rou-hidden-lampson.md`.
- Memory: "Phase 2 Round 6 — F + 6× inline G chunks SHIPPED 2026-05-28"
  inside `judeo-arabic-app-project.md`.

**Round 6 final state (uncommitted in working tree):**
- Hand-coverage **72.28%** (Round-6 delta +4.33 pts on inline-Opus sweep).
- Covered total **76.00%**. Lane entries **487** (was 364 at Round-5 end).
- Per-book: bereshit 70.59 · shemot 72.42 · vayikra 73.37 · bamidbar
  **76.34 (best — covered total 79.24%, one round from 80% per-book)** ·
  devarim **69.09 (still laggard, +3.93 pts in Round 6)**.
- `npm run build` clean (213 pages). `verify_divergence.py` exit 0
  (pre-existing Bereshit-mix soft warning unchanged). `scope_saadia_notes.py`
  0 residual hits.

**Top 25 misses going into Round 7** (the queue this round attacks):

```
 14  רת                    [standard]    — STUCK: no context hits anywhere
 10  פרג                   [standard]    — no context hits
  9  אליס                  [standard]    — ʔa-laysa "is it not?" interrogative
  9  כלב                   [standard]    — kalb "dog" (homograph w/ Caleb)
  9  ואלעסל                [w-prefixed]  — wa-l-ʿasal "and the honey"
  9  כם                    [standard]    — kam "how much/many"
  9  אולאיך                [standard]    — ʾūlāʾika "those" (distal dem.pl.)
  9  מרצ'ייא               [has-apos]    — marḍiyyan "acceptable" — Saadia for נִיחֹחַ
  9  אלצ'אן                [has-apos]    — al-ḍa'n "the flock" (sheep+goats)
  9  סהוא                  [standard]    — sahwan "inadvertently"
  9  ויג'פר                [w-prefixed]  — wa-yaghfir "and he forgives"
  9  פתקדם                 [standard]    — fa-taqaddam "and he advanced"
  9  כ'לה                  [has-apos]    — khalāhu / khallāhu "(he) left him"
  9  אלובא                 [standard]    — al-wabā' "the plague"
  9  באצבעה                [standard]    — bi-iṣbaʿihi "with his finger"
  9  מיית                  [standard]    — mayyit "dead, deceased"
  9  חד'א                  [has-apos]    — ḥidhā'a "facing, parallel to"
  9  ירחלון                [standard]    — variant of rahala-depart (PATCH)
  9  ער                    [standard]    — proper noun Er, son of Judah
  9  אלסיף                 [standard]    — al-sayf "the sword"
  9  כמסה                  [standard]    — likely khamsa "five" or related
  9  ואביהוא               [w-prefixed]  — Abihu — variant on existing entry?
  9  כ'צומה                [has-apos]    — khuṣūma "quarrel, dispute"
  9  ת'מאניה               [has-apos]    — thamāniya "eight"
  9  וסתר                  [w-prefixed]  — wa-stara "and he covered"
```

**Diagnosis.** Head count has flattened further (top miss 14 down from 17 at
R6 start; the bulk at count 9). Roughly 1,000 candidates with count ≥ 4
remain in `data/coverage-misses.json`. From Round 6's evidence, each
inline-Opus entry yields ~0.035 pts of hand-coverage. To push 72.28% → 80%
(closing the Camel-badge retirement gate) needs ~215 more entries, roughly
8–9 chunks of the same scale.

Round 7 splits the work into the same two phases that worked in Round 6,
but the head-cleanup phase is much smaller now:

1. **Batch H — head hand cleanup** (~10–15 entries, ~+0.3–0.5 pt).
   The 10 hand-glossable items from the top-25 above that aren't pure
   patches: ʔa-laysa, kalb, ʿasal, kam, ʾūlāʾika, marḍiyyan, ḍa'n, sahwan,
   yaghfir, wabā', mayyit, ḥidhā'a, sayf, khamsa, khuṣūma, thamāniya, satara
   — plus the proper noun `ʿEr-name` and likely a `Abihu-name` patch.

2. **Batch I — continue inline Sonnet-style sweep** (~5–8 chunks of 25,
   ~+5–8 pt target). Same pattern as Round 6 Batch G: pull 25 candidates,
   look up contexts, preflight lemma collisions, write apply script in
   `scripts/apply_round7_I_chunkN.py`, apply, repeat.

**Round-7 target: 72.28% → ~76–80% hand.** Stretch goal hand ≥ 80% would
retire the Camel auto-dict badge globally; Bamidbar would cross 80% covered
first (already at 79.24%).

---

## Batch H — head-of-queue hand cleanup (~15 entries)

### Step 1: Confirm the top-25 still match `data/coverage-misses.json`

```bash
cd ~/Code/judeo-arabic-app
python3 -c "
import json
m = json.load(open('data/coverage-misses.json'))['misses']
for e in m[:25]: print(f\"  {e['count']:3d}  {e['surface']:20s}  [{e['bucket']}]\")"
```

### Step 2: Pre-classify each candidate

For Round-7 the diagnostic block above already does most of this — verify
1-2 context verses per candidate via the helper from Round 6:

```bash
python3 - <<'PY'
import json
ctx = json.load(open('/tmp/ja-context-index.json'))
for tok in ['אליס','כלב','כם','אולאיך','מרצ'ייא','אלצ'אן','סהוא','ויג'פר','כ'לה','אלובא','באצבעה','מיית','חד'א','ער','אלסיף','כמסה','כ'צומה','ת'מאניה','וסתר']:
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

### Step 3: Author `scripts/apply_round7_H.py`

Same shape as `scripts/apply_round6_F.py`. **Always preflight-check the
proposed lemmas against the dict before writing** — Round-6 caught one
near-duplicate (`muqaddas-holy` ≈ existing `muqaddas-sacred`) and several
PATCH-targets that would otherwise have been mis-added:

```bash
python3 - <<'PY'
import json
d = json.load(open('data/dictionary-lane.json'))
d2 = json.load(open('data/dictionary-starter.json'))
proposed = [...]  # your candidate lemmas
for lemma in proposed:
    hits = [e for e in d['entries'] if e.get('lemma_ja') == lemma] + \
           [e for e in d2['entries'] if e.get('lemma_ja') == lemma]
    variants = [e for e in d['entries'] if lemma in (e.get('variants') or [])] + \
               [e for e in d2['entries'] if lemma in (e.get('variants') or [])]
    print(f"  {lemma}  {'⚠ ' + str([e['id'] for e in hits+variants]) if hits or variants else '✓'}")
PY
```

If a proposed lemma collides, route via `VARIANTS_PATCH` (lane) or
`STARTER_VARIANTS_PATCH` (starter) instead of creating a duplicate entry.
Apply pattern from Round-6 chunk 4 supports all three: `NEW_ENTRIES`,
`VARIANTS_PATCH`, `STARTER_VARIANTS_PATCH`.

### Step 4: Validate JSON + re-scope notes

```bash
python3 -c "import json; json.load(open('data/dictionary-lane.json')); json.load(open('data/dictionary-starter.json'))"
python3 scripts/scope_saadia_notes.py
# Optionally re-run coverage_report.py to measure Batch H delta on its own,
# but it's slow (~3-4 min) — easier to bundle the measurement with Batch I.
```

---

## Batch I — continue inline long-tail sweep (5–8 chunks of 25)

### Step 1: Regenerate candidates from the post-H miss queue

```bash
python3 scripts/coverage_report.py    # ~3-4 min; refresh after H
python3 - <<'PY'
import json
m = json.load(open('data/coverage-misses.json'))['misses']
out = [{"token": e["surface"], "count": e["count"], "bucket": e["bucket"]} for e in m]
json.dump(out, open('/tmp/ja-candidates.json','w'), ensure_ascii=False, indent=2)
print(f"Wrote {len(out)} candidates")
PY
python3 scripts/build_ja_context_index.py   # refreshes /tmp/ja-context-index.json
```

### Step 2: Per-chunk loop (target 5–8 iterations)

For each chunk N (1..8):

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
1. Walk the 25 candidates inline; gloss each per Round-6 rules:
   - `gloss_en` carries the **classical Arabic** sense only — no Saadia
     calques (the audit pass at end-of-round will catch slips into the
     gloss text, but only via `scope_saadia_notes.py` — embedded "(Saadia:
     X)" parentheticals require a manual rewrite).
   - Saadia-specific commentary → `saadia_note` (Advanced reader hides it).
   - Function words → `root: "—"`, pos = `particle`/`conjunction`/`preposition`.
   - Proper nouns → `pos: "proper noun"`, `root: "—"`.
   - Inflected forms covered as variants on the base lemma, not separate
     entries (lemma_ja = base form).
   - `source: "lane"` for everything.
2. **Preflight lemma collisions** — use the snippet from Batch H Step 3.
3. Write `scripts/apply_round7_I_chunk<N>.py` with `NEW_ENTRIES` +
   `VARIANTS_PATCH` + optional `STARTER_VARIANTS_PATCH`. Run it.
4. Validate JSON round-trip. Move to next chunk.

After all chunks:

```bash
python3 scripts/scope_saadia_notes.py    # auto-migrate Saadia sentences from notes
# If it flags residuals in gloss_en/gloss_he, do the same manual gloss-rewrite
# pass Round 6 did — strip the parentheticals; saadia_note carries the same info.
python3 scripts/verify_divergence.py     # exit 0 expected (Bereshit-mix warning OK)
python3 scripts/coverage_report.py       # final hand_pct
npm run build                            # 213+ pages clean
```

---

## Per-batch workflow (unchanged)

1. **Refresh misses if dict changed:** `python3 scripts/coverage_report.py`
   (~3–4 min). Skip if no dict changes since last run.
2. **Build candidate file + context index** with the snippets above.
3. **Preflight lemma collisions** before authoring each chunk.
4. **Validate JSON round-trip** after each apply.
5. **Build check at end of round:** `npm run build` must stay clean.
6. **No commit.** Working tree carries Round 4 + 5 + 6 + 7 (uncommitted).

---

## Verification at end of Round 7

- `python3 scripts/coverage_report.py` reports hand-coverage **≥ 76%**
  (stretch ≥ 80%, which unlocks Camel-badge retirement).
- `python3 scripts/verify_divergence.py` exits 0.
- `python3 scripts/scope_saadia_notes.py` reports 0 residual hits.
- `npm run build` clean.
- Spot-check 3 random tafsir chapters in dev (`npm run dev`):
  - `/tafsir/bamidbar/14` for אלובא (plague) + אלשעב
  - `/tafsir/bereshit/24` for כ'צומה / אליס
  - `/tafsir/devarim/2` for ער (proper noun) + שעב
  Confirm previously-missing tokens now open the gloss panel.

## Gotchas (carry-overs from Round 6)

- **Always preflight-check proposed lemmas** before adding new entries.
  The muqaddas-holy mistake (chunk 1) cost a round-trip; subsequent chunks
  caught 5+ collisions cleanly with the preflight snippet.
- **Variants must be explicit per stem**, not algorithmic suffix-strip
  (`lib/lookup.ts` policy).
- **Trailing-apostrophe lemmas** — store bare form, add `'`-suffixed
  variant if needed. `normalizeFinals` strips trailing `'` on both sides.
- **`notes` is cross-text-safe.** Saadia-specific text belongs in
  `saadia_note` (auto-migrated by `scope_saadia_notes.py`). For entries
  whose gloss IS a Saadia coinage, write the **classical** sense in
  `gloss_en` and put the Saadianic application in `saadia_note` — don't
  inline "Saadia: ..." into the gloss text. If you do, the audit pass
  flags it but won't auto-fix; manual rewrite required.
- **Homographs are fine** — keep separate entries when senses are genuinely
  distinct (e.g. בקי "remain" vs Bukki name; כלב "dog" vs Caleb).
- **`coverage_report.py` runs ~3–4 min** (npx tsx warmup × 187 chapters).
  Skip the pre-batch refresh if the dict hasn't changed since the snapshot.
- **`/tmp/ja-candidates.json` and `/tmp/ja-context-index.json` get wiped
  between sessions.** Rebuild via the snippets above + 
  `scripts/build_ja_context_index.py` (durable). Apply scripts go in
  `scripts/`, not `/tmp/`.
- **Tail oddity worth investigating in this round:** `רת` (count 14) has
  no context hits — likely a tokenizer artifact in `coverage_report.py`,
  not a real miss. Worth peeking at `lib/tokenize.ts` + the chapter-loop in
  `coverage_report.py` to see what surface the report is constructing.
- **Round-6 lesson — inline-Opus is ~0.035 pts/entry.** Realistic gain
  for 5–8 chunks (~125–200 entries) is +4–7 pts. Project Round-7 final at
  76–79% hand, with 80% as the upper edge.

## ID cleanups worth bundling in (low priority)

Round 6 surfaced two existing entries with wrong IDs (semantically intact,
just the kebab-case slug is misleading):
- `naqis-defective` → should be `najis-unclean` (root n-j-s, not n-q-ṣ).
- `ʿaqd-covenant` → should be `ʿahd-covenant` (the lemma + gloss are
  already correct; only the id mismatches).

Rename via a small fix-up script — these are not blockers but they'll
mislead future grepping.

## After Round 7

- **If hand ≥ 80% at end of round 7:** retire the Camel auto-dict badge.
  Per-Round-6 prompt notes: one-line UI change in
  `app/tafsir/reader.tsx:613-644` (SourceBadge "camel" branch) + 2-line
  change in `lib/lookup.ts:177-183` (skip Priority-3 auto lookup).
- **Phase 3 (divergences 32 → ~180).** Runs on `data/tafsir-divergence.json`.
  Doesn't touch dict files; can run in parallel with dict expansion.
- **Phase 4 (Word-of-the-Day homepage card).** Year-mixed deterministic
  seed; pulls from lane dict; shows on `app/page.tsx`. Independent files.
- **One-off pickup:** `רת` tokenizer artifact investigation.

---

**Tell Claude:** "Resume Phase 2 Round 7 per
`~/Code/judeo-arabic-app/PHASE2_ROUND7_PROMPT.md`. Run Batch H first
(hand-curate ~15 head-of-queue lemmas + variant patches), then Batch I
(5–8 inline chunks of ~25 candidates each, no API spend), reporting
coverage delta after each. Final spot-check 3 chapters in dev. If hand
≥ 80% at end of round, do the Camel-badge retirement diff."
