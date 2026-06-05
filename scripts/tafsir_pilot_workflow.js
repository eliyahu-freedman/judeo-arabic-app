export const meta = {
  name: 'tafsir-devarim-pilot',
  description: 'Pilot: author Tafsir (Devarim) dictionary entries toward ~100% coverage',
  phases: [
    { title: 'Author', detail: 'fan out: each agent authors a slice of the Devarim residual worklist' },
    { title: 'Merge', detail: 'one agent: concat → apply → re-measure coverage (coverage_report.py)' },
  ],
}

const CHUNK = (args && args.chunk) || 45
let total = (args && args.total) || 1871

const MERGE_SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['applied_entries', 'devarim_hand_pct', 'overall_hand_pct', 'remaining_groups', 'note'],
  properties: {
    applied_entries: { type: 'integer', description: 'net +N lane entries from apply_dict_advanced.py' },
    devarim_hand_pct: { type: 'number', description: 'devarim hand-coverage % from coverage_report.py after apply' },
    overall_hand_pct: { type: 'number', description: 'overall hand TOTAL % from coverage_report.py after apply' },
    remaining_groups: { type: 'integer', description: '_lemma_groups in the regenerated Devarim worklist (uncovered groups left)' },
    note: { type: 'string' },
  },
}

function authorPrompt(start, end) {
  return `You are authoring Judaeo-Arabic dictionary entries for the SAADIA TAFSIR reader (Pentateuch), book of Devarim. Work ONLY on residual worklist groups [${start}:${end}]. Run all commands from \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

STEP 1 — load your slice:
  python3 -c "import json;g=json.load(open('data/_advanced_misses_residual.json'))['groups'][${start}:${end}];print(json.dumps(g,ensure_ascii=False))"
Each group = {key, ar, count, texts, surfaces[]}. \`key\` is a prefix-stripped stem guess, \`ar\` its back-converted Arabic, \`surfaces\` the observed forms.

STEP 2 — author ONE entry per group with EXACTLY these fields:
  id        unique "taf-d-${start}-<i>"
  lemma_ja  clean Hebrew-script JA citation form. \`key\` is sometimes BROKEN (a radical ב/ל/כ/פ/ו or אל wrongly stripped) — when so, use the real surface as lemma_ja.
  lemma_ar  voweled classical Arabic (from \`ar\`)
  root      hyphenated radicals, e.g. "ʿ-l-m"; for proper names / particles use "—"
  pos       part of speech
  gloss_en / gloss_he  concise glosses
  source    the literal string "lane"
  variants  MUST contain EVERY string in the group's surfaces[] VERBATIM (this is what makes the word covered) + any inflections you're sure of.

CONTEXT — this is the Pentateuch in Saadia's Arabic translation, so expect heavy:
  • BIBLICAL PROPER NAMES (people, places, tribes). Gloss as pos "proper noun", root "—", gloss_en = the standard English name, gloss_he = the Hebrew name. Saadia uses well-known place-IDs: e.g. אלשאם/al-Sham=Canaan area, identifications like the Jordan (אלארדן), Edom, Moab, Bashan, etc. If unsure which name, grep the source for context (see step 3).
  • NUMBERS, weights/measures, ritual/legal terms.
  • Ordinary Arabic words + their inflections.

STEP 3 — VERIFY, do not fabricate:
  python3 ~/Tools/arabic-lexicon/cli.py lookup <ar-root> --dict lane
  python3 ~/Tools/arabic-lexicon/cli.py lookup <form> --dict blau
For a proper name or ambiguous form, grep the Devarim source for the sentence:
  grep -h "<surface>" data/tafsir-devarim-*.json | head
Then identify the verse/name. For a genuinely uncertain rare form, give your best contextual gloss with a trailing " (?)" — never invent a fake root.

STEP 4 — write your file (mkdir -p data/_bahya_authored first):
  data/_bahya_authored/tafd_${start}.json  containing { "entries": [ ... ], "patches": { } }
Use "patches" (existing_entry_id -> [surface,...]) only when a surface is clearly an inflection of a stem that already has a lane entry.

Return ONE short line: entries authored + anything you guessed. The written file is the deliverable.`
}

function mergePrompt() {
  return `MERGE + MEASURE step for the Tafsir Devarim pilot. Run from \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

1. Concat this round's chunk files into the apply input, and MERGE chunk patches into the EXISTING patch file (which already holds the autopatch sweep — do not clobber it):
   python3 - <<'PY'
import json, glob
entries = []
for f in sorted(glob.glob('data/_bahya_authored/tafd_*.json')):
    try: d = json.load(open(f))
    except Exception as e: print('SKIP', f, e); continue
    entries += d.get('entries', []) or []
    p = d.get('patches', {}) or {}
    if p:
        cur = json.load(open('data/_dict_advanced_patch.json'))
        for k, v in p.items(): cur[k] = list(dict.fromkeys((cur.get(k, []) or []) + v))
        json.dump(cur, open('data/_dict_advanced_patch.json','w'), ensure_ascii=False, indent=2)
json.dump(entries, open('data/_dict_advanced.json','w'), ensure_ascii=False, indent=2)
print('merged entries:', len(entries))
PY

2. Apply (capture the "+N" from the APPEND line):
   python3 scripts/apply_dict_advanced.py

3. Re-measure:
   python3 scripts/coverage_report.py            # overall "Hand TOTAL" % and the devarim per-book hand %
   python3 scripts/stage_tafsir_misses.py devarim # prints "_lemma_groups" = uncovered Devarim groups left

4. RETURN via StructuredOutput: applied_entries (+N from step 2), devarim_hand_pct + overall_hand_pct (from step 3 coverage_report), remaining_groups (the lemma-group count printed by stage_tafsir_misses in step 3), note (flag any tracebacks/skipped files). Do NOT hand-edit dictionary files.`
}

phase('Author')
const ranges = []
for (let s = 0; s < total; s += CHUNK) ranges.push([s, Math.min(s + CHUNK, total)])
log(`Devarim pilot: ${total} residual groups → ${ranges.length} authoring agents (chunk ${CHUNK})`)
await parallel(ranges.map(([s, e]) => () =>
  agent(authorPrompt(s, e), { label: `author:${s}-${e}`, phase: 'Author' })
))

phase('Merge')
const m = await agent(mergePrompt(), { label: 'merge', phase: 'Merge', schema: MERGE_SCHEMA })
if (m) {
  log(`PILOT RESULT: +${m.applied_entries} entries | Devarim hand ${m.devarim_hand_pct}% (was 81.91%) | overall hand ${m.overall_hand_pct}% (was 84.28%) | ${m.remaining_groups} Devarim groups left. ${m.note}`)
}
return m
