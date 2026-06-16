export const meta = {
  name: 'bahya-coverage',
  description: 'Author Bahya Advanced-reader dictionary entries to 100% tap-to-define coverage (all 11 gates)',
  phases: [
    { title: 'Prime', detail: 'one agent: run the coverage→stage→autopatch→apply pipeline, report the real residual count' },
    { title: 'Author', detail: 'fan out: each agent authors a slice of the residual worklist + writes its chunk file' },
    { title: 'Merge', detail: 'one agent: concat chunks → apply → suffix-sweep → re-gate, report residual' },
  ],
}

// ---- knobs -----------------------------------------------------------------
const CHUNK = (args && args.chunk) || 45      // residual groups per authoring agent
const MAX_ROUNDS = (args && args.maxRounds) || 8
let total = (args && args.total) || 0         // 0 → the Prime step measures it

// The merge step reports the regenerated residual and the WORST per-gate
// coverage across all in-scope Bahya gates (the gate is "all gates at 100%",
// i.e. residual == 0). min_bahya_pct is for human-readable progress only.
const MERGE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['min_bahya_pct', 'gates_at_100', 'residual_groups', 'residual_surfaces', 'applied_entries', 'note'],
  properties: {
    min_bahya_pct: { type: 'number', description: 'the LOWEST covered_pct among all bahya-* texts in coverage-advanced.json' },
    gates_at_100: { type: 'integer', description: 'how many bahya-* texts are at 100.0% coverage' },
    residual_groups: { type: 'integer', description: 'group count in the regenerated _advanced_misses_residual.json' },
    residual_surfaces: { type: 'integer' },
    applied_entries: { type: 'integer', description: 'net new lane entries added this round' },
    note: { type: 'string', description: 'one-line status, e.g. any apply/coverage errors' },
  },
}

const PRIME_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['residual_groups', 'residual_surfaces', 'min_bahya_pct', 'note'],
  properties: {
    residual_groups: { type: 'integer' },
    residual_surfaces: { type: 'integer' },
    min_bahya_pct: { type: 'number' },
    note: { type: 'string' },
  },
}

function primePrompt() {
  return `You are the PRIME step for the Bahya coverage workflow. Run everything from \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

Run the coverage → stage → autopatch → apply pipeline once to establish the current residual worklist across ALL Bahya gates (hakdamah + bab1…bab10):
  python3 scripts/coverage_advanced.py ; python3 scripts/stage_advanced_misses.py ; python3 scripts/autopatch_advanced_misses.py
  python3 scripts/apply_dict_advanced.py
  python3 scripts/coverage_advanced.py
  (coverage_advanced.py exits non-zero while any in-scope text is < 100% — that is EXPECTED; keep going.)

Then RETURN via StructuredOutput:
  - residual_groups, residual_surfaces: from data/_advanced_misses_residual.json (_residual_groups / _residual_surfaces)
  - min_bahya_pct: the LOWEST by_text["bahya-*"].covered_pct in data/coverage-advanced.json
  - note: one line — flag any python tracebacks or anomalies.`
}

function authorPrompt(round, start, end) {
  return `You are authoring Judaeo-Arabic dictionary entries for the Bahya (Ḥovot ha-Levavot) Advanced-reader coverage pass. Work ONLY on residual worklist groups [${start}:${end}].

Run all commands from the repo root: \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

STEP 1 — load your slice:
  python3 -c "import json;g=json.load(open('data/_advanced_misses_residual.json'))['groups'][${start}:${end}];print(json.dumps(g,ensure_ascii=False))"
Each group = {key, ar, count, texts, surfaces[]}. \`key\` is a prefix-stripped stem guess, \`ar\` is its back-converted Arabic (your Lane lookup key), \`surfaces\` are the actual observed word forms.

STEP 2 — author ONE entry per group, an object with EXACTLY these fields:
  id        unique string "adv-b-r${round}-${start}-<i>" (i = index within your slice)
  lemma_ja  the BASE CITATION form in Hebrew-script Judaeo-Arabic — singular, no article אל-, no pronominal suffix, no proclitic; an Arabic verb's citation form is the bare 3ms perfect; a feminine noun keeps its tā-marbūṭa (final ה). NEVER put an inflected/suffixed surface in lemma_ja (that creates the "tap base word → see possessed gloss" bug; lint: scripts/find_inflected_lemmas.py). The inflected surfaces all go in variants[] (STEP 2 below). NOTE: \`key\` is sometimes a BROKEN stem because a radical ב/ל/כ/פ/ו or אל was wrongly stripped (e.g. surface פתיחה reduced to key תיחה); when \`key\` looks broken, derive the base from the real surface form (e.g. lemma_ja=פתיחה), not the broken key.
  lemma_ar  voweled classical Arabic (start from \`ar\`, add ḥarakāt when confident)
  root      hyphenated radicals with ʿ/ʾ, e.g. "ʕ-l-m", "w-ḥ-d", "ʾ-m-n"
  pos       part of speech ("noun","verb","adjective","particle","proper noun", etc.)
  gloss_en  concise English gloss
  gloss_he  concise Hebrew gloss (vocalized is fine, plain is fine)
  source    the literal string "lane"
  variants  ARRAY THAT MUST CONTAIN EVERY STRING IN THE GROUP'S surfaces[] VERBATIM. This is what makes the word covered — do not omit, alter, or normalize any surface. Add other inflections you're confident about too.

STEP 3 — VERIFY, do not fabricate. For ordinary Arabic words check Lane:
  python3 ~/Tools/arabic-lexicon/cli.py lookup <ar-root> --dict lane
  python3 ~/Tools/arabic-lexicon/cli.py lookup <form> --dict blau   (for Judaeo-Arabic senses)
If a form is clearly EMBEDDED BIBLICAL/LITURGICAL HEBREW (not Arabic — Bahya quotes Scripture and piyyut heavily), grep the source for context and identify the verse:
  grep -o "...<surface>..." data/bahya-*.json   (all gates; or python json load + search)
Then gloss it in Hebrew, put the citation (e.g. "תהלים נח:ה") in gloss_he, set pos "proper noun" or "Hebrew quote", root "—". For a genuinely uncertain rare form, give your best contextual gloss and say so in a trailing " (?)" — never invent a fake root/Arabic.

STEP 4 — write your output file (create the dir first if needed):
  mkdir -p data/_bahya_authored
Write data/_bahya_authored/r${round}_${start}.json containing:
  { "entries": [ ...your entry objects... ], "patches": { } }
Use "patches" (map of existing_entry_id -> [surface,...]) ONLY if you're sure a surface is just an inflection of a stem that already has a lane entry; otherwise author a normal entry. Most go in "entries".

Return ONE short line: how many entries you authored and any groups you had to guess on. Your written file is the real deliverable.`
}

function mergePrompt(round) {
  return `You are the MERGE + GATE step for the Bahya coverage workflow, round ${round}. Run everything from \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

1. Concatenate this round's authored chunk files into the apply inputs:
   python3 - <<'PY'
import json, glob
entries, patches = [], {}
for f in sorted(glob.glob('data/_bahya_authored/r${round}_*.json')):
    try:
        d = json.load(open(f))
    except Exception as e:
        print('SKIP', f, e); continue
    entries += d.get('entries', []) or []
    for k, v in (d.get('patches', {}) or {}).items():
        patches.setdefault(k, [])
        patches[k] += v
json.dump(entries, open('data/_dict_advanced.json','w'), ensure_ascii=False, indent=2)
json.dump(patches, open('data/_dict_advanced_patch.json','w'), ensure_ascii=False, indent=2)
print('merged entries:', len(entries), 'patch keys:', len(patches))
PY

2. Apply, then run the suffix-sweep + regenerate the residual, then apply the sweep, then final coverage:
   python3 scripts/apply_dict_advanced.py
   python3 scripts/coverage_advanced.py ; python3 scripts/stage_advanced_misses.py ; python3 scripts/autopatch_advanced_misses.py
   python3 scripts/apply_dict_advanced.py
   python3 scripts/coverage_advanced.py
   (coverage_advanced.py exits non-zero while bahya < 100% — that's expected, keep going.)

3. Read the final numbers and RETURN them via the StructuredOutput tool:
   - min_bahya_pct: the LOWEST covered_pct among ALL by_text["bahya-*"] entries in data/coverage-advanced.json
   - gates_at_100: how many by_text["bahya-*"] entries have covered_pct == 100.0
   - residual_groups, residual_surfaces: from data/_advanced_misses_residual.json (_residual_groups / _residual_surfaces)
   - applied_entries: the net "+N" from the FIRST apply's "APPEND: lane entries A -> B (+N)" line
   - note: one line — flag any python tracebacks, skipped chunk files, or anomalies.

Do NOT edit lane/starter/dictionary files by hand; only run the scripts.`
}

// Prime: measure the real residual across all 11 gates before fanning out.
phase('Prime')
const primed = await agent(primePrompt(), { label: 'prime', phase: 'Prime', schema: PRIME_SCHEMA })
if (!primed) { log('Prime step returned null — aborting.'); return }
if (!total) total = primed.residual_groups
log(`Primed: ${primed.residual_groups} residual groups (${primed.residual_surfaces} surfaces), worst gate ${primed.min_bahya_pct}%. ${primed.note}`)
if (total <= 0) { log('🎉 Residual already 0 — all gates covered.'); return primed }

for (let round = 1; round <= MAX_ROUNDS; round++) {
  if (total <= 0) { log(`Round ${round}: residual is 0 — done.`); break }

  phase('Author')
  const ranges = []
  for (let s = 0; s < total; s += CHUNK) ranges.push([s, Math.min(s + CHUNK, total)])
  log(`Round ${round}: ${total} residual groups → ${ranges.length} authoring agents (chunk ${CHUNK})`)

  await parallel(ranges.map(([s, e]) => () =>
    agent(authorPrompt(round, s, e), { label: `author:r${round}:${s}-${e}`, phase: 'Author' })
  ))

  phase('Merge')
  const m = await agent(mergePrompt(round), { label: `merge:r${round}`, phase: 'Merge', schema: MERGE_SCHEMA })
  if (!m) { log(`Round ${round}: merge agent returned null — stopping.`); break }
  log(`Round ${round} done: ${m.gates_at_100}/11 gates at 100% (worst ${m.min_bahya_pct}%) | +${m.applied_entries} entries | residual ${m.residual_groups} groups (${m.residual_surfaces} surfaces). ${m.note}`)

  if (m.residual_groups <= 0) { log('🎉 All 11 Bahya gates at 100%.'); return m }
  if (m.residual_groups >= total) { log(`No progress (residual ${m.residual_groups} ≥ round start ${total}) — stopping to avoid a stall loop.`); return m }
  total = m.residual_groups
}
log('Workflow finished (hit MAX_ROUNDS or stall). Re-run to continue if residual remains.')
