export const meta = {
  name: 'fix-inflected-lemmas',
  description: 'Re-key dictionary entries whose headword is an inflected form back to the base citation form',
  phases: [
    { title: 'Rekey', detail: 'one agent per chunk: decide keep-vs-rekey per entry, return corrected entries' },
  ],
}

// total = number of fix_candidates in data/_inflected_worklist.json (A+B tiers).
const TOTAL = (args && args.total) || 998
const CHUNK = (args && args.chunk) || 30

const SCHEMA = {
  type: 'object',
  additionalProperties: false,
  required: ['fixes'],
  properties: {
    fixes: {
      type: 'array',
      items: {
        type: 'object',
        additionalProperties: false,
        required: ['id', 'action'],
        properties: {
          id: { type: 'string', description: 'the entry id, copied verbatim from the input' },
          action: { type: 'string', enum: ['rekey', 'keep'], description: 'rekey if the headword is an inflected/bound form; keep if it is already a valid base citation form' },
          lemma_ja: { type: 'string', description: 'base citation form, Hebrew-script Judaeo-Arabic (rekey only)' },
          lemma_ar: { type: 'string', description: 'voweled classical Arabic base form (rekey only)' },
          root: { type: 'string', description: 'hyphenated radicals e.g. ʾ-m-n (rekey only)' },
          pos: { type: 'string' },
          gloss_en: { type: 'string', description: 'BASE-sense English gloss, NOT the possessed/bound sense (rekey only)' },
          gloss_he: { type: 'string', description: 'BASE-sense Hebrew gloss (rekey only)' },
          variants: { type: 'array', items: { type: 'string' }, description: 'MUST contain every original surface (old lemma_ja + every original variant) verbatim, PLUS the new base form. This is what keeps coverage at 100%.' },
          reason: { type: 'string', description: 'one short phrase' },
        },
      },
    },
  },
}

function prompt(start, end) {
  return `You are correcting Judaeo-Arabic dictionary entries whose HEADWORD (lemma_ja) was authored as an INFLECTED form instead of the base citation form. Run all commands from \`/Users/eliyahufreedman/Code/judeo-arabic-app\`.

THE INVARIANT we are restoring:
  lemma_ja = the BASE CITATION form. variants[] = equal-or-MORE-inflected surface forms only.
A user taps a word in the reader; the lookup matches lemma_ja OR any variant and shows lemma_ja + gloss_en. So if lemma_ja is "אימנאך" glossed "your faith (+suffix)", tapping the base "אלאימאן" shows that wrong suffixed card. The base form must be the headword with a base gloss.

STEP 1 — load your slice (each item has id, lemma_ja, lemma_ar, root, pos, gloss_en, gloss_he, variants, _signals, _shorter_variants, _tier):
  python3 -c "import json;c=json.load(open('data/_inflected_worklist.json'))['lane']['fix_candidates'][${start}:${end}];print(json.dumps(c,ensure_ascii=False))"

STEP 2 — for EACH entry decide action:

  KEEP (action:"keep") if lemma_ja is ALREADY a valid base citation form:
   • A feminine noun ending in tā-marbūṭa (ة → Hebrew ה): פצ'ה "silver", קריה "town", סבעה "seven", כ'צומה "quarrel" are CITATION forms — the final ה is root, NOT a possessive suffix. KEEP.
   • An Arabic VERB cited in the bare 3ms perfect: קאל "qāla = said", כתב "wrote". The 3ms perfect IS the citation form. KEEP. (The _signals may say "conjugation" — ignore that for a bare 3ms perfect.)
   • A bare imperfect stem used as the entry's citation with a base infinitival gloss (e.g. יערף "to know") — KEEP unless the gloss is genuinely possessed/bound.
   • A demonstrative/pronoun/particle that is its own citation form (הד'ה "this f."). KEEP.

  REKEY (action:"rekey") if lemma_ja carries any of: a pronominal/object suffix (-ה/-הא/-הם/-הן/-ך/-כם/-נא/-י/-ני: וג'ודה "His existence", מד'הבה "his doctrine", ידי "my hand", שריעתהא "its law", חג'ג'הם "their arguments"), a definite article אל-, a proclitic ו/ב/ל/כ/פ (פקאל fa-qāla → קאל), or a bound subject affix that is not the citation form (ימכנא "it is possible for us" → ימכן; וג'דנאה "we found it" → base verb).

STEP 3 — for a REKEY, produce:
   lemma_ja  the base form (singular, no article, no possessive, no proclitic; keep tā-marbūṭa if the base is feminine).
   lemma_ar  voweled classical Arabic base.
   root      hyphenated radicals (verify — see STEP 4).
   pos       part of speech.
   gloss_en  the BASE meaning. Strip the possessive/"+suffix" framing: "His existence (wujūd + 3ms suffix)" → "existence, being"; "your faith (+ suffix)" → "faith, belief"; "its law (sharīʿa + suffix)" → "law, legal way".
   gloss_he  base Hebrew gloss.
   variants  EVERY string from the input's lemma_ja + every input variant, VERBATIM (do not drop or alter any — this preserves coverage), PLUS the new base form if not already present.

STEP 4 — VERIFY, don't fabricate. When unsure of root/base/sense:
   python3 ~/Tools/arabic-lexicon/cli.py lookup <root-or-form> --dict lane
   python3 ~/Tools/arabic-lexicon/cli.py lookup <form> --dict blau
   Never invent a root; if genuinely uncertain, KEEP and note why in "reason".

Return via the StructuredOutput tool: { "fixes": [ {id, action, ...} for EVERY entry in your slice ] }. Include id for all; for "keep" you may omit the other fields.`
}

phase('Rekey')
const ranges = []
for (let s = 0; s < TOTAL; s += CHUNK) ranges.push([s, Math.min(s + CHUNK, TOTAL)])
log(`${TOTAL} fix candidates → ${ranges.length} agents (chunk ${CHUNK})`)

const results = await parallel(ranges.map(([s, e]) => () =>
  agent(prompt(s, e), { label: `rekey:${s}-${e}`, phase: 'Rekey', schema: SCHEMA })
))

const fixes = results.filter(Boolean).flatMap(r => r.fixes || [])
const rekey = fixes.filter(f => f.action === 'rekey').length
const keep = fixes.filter(f => f.action === 'keep').length
log(`Collected ${fixes.length} decisions: ${rekey} rekey, ${keep} keep.`)
return { fixes, rekey, keep, agents: ranges.length }
