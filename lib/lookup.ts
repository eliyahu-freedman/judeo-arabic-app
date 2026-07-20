import starter from "@/data/dictionary-starter.json";
// dictionary-lane.json (~6.5 MB) is NOT statically imported — bundling it
// synchronously creates a ~5 MB client JS chunk that crashes low-memory tabs.
// It is loaded lazily on the client the first time this module is evaluated;
// lookup() falls back to an empty Lane result set during the brief window
// before the async fetch completes.
// The auto-extracted Camel-tools dictionary (dictionary-auto.json) has been
// retired: hand coverage (starter + lane) now exceeds 80%, so the unverified
// MSA fallback is no longer consulted. The JSON file is kept on disk for the
// coverage report only; it is no longer imported into the app.

// Re-export the tokeniser from its zero-dependency home so existing callers
// keep importing `tokenizeJa` from `lib/lookup`. The canonical implementation
// lives in `lib/tokenize.ts` so external tools (e.g. the Python coverage
// script via `scripts/_tokenize_ja_cli.ts`) can import it without dragging
// in the dictionary JSON path aliases.
export { tokenizeJa } from "./tokenize";

export type Entry = {
  id: string;
  lemma_ja: string;
  lemma_ar: string;
  root: string;
  pos: string;
  gloss_en: string;
  gloss_he: string;
  /**
   * Generic / classical-Arabic commentary. Rendered in BOTH readers (Tafsir
   * and Advanced library). Should not mention Saadia or the Tafsir corpus —
   * that material belongs in `saadia_note` so it doesn't leak into readers
   * for Rambam, Kuzari, Qirqisani, Bahya, etc.
   */
  notes?: string;
  /**
   * Saadia-specific commentary: how Saadia uses this word in the Tafsir,
   * Hebrew calques, anti-anthropomorphic substitutions, etc. Rendered ONLY
   * in the Tafsir reader (`app/tafsir/reader.tsx`) under an explicit
   * "In Saadia's Tafsir:" prefix. Suppressed in the Advanced library reader.
   */
  saadia_note?: string;
  /**
   * Scope tag. `"saadia"` means the entry's primary gloss is itself a
   * Saadia-specific semantic shift (e.g. גלד glossed as "firmament" — the
   * classical Arabic sense is "skin/hide"). Such entries are filtered OUT
   * of the gloss panel in the Advanced library reader so users reading
   * Rambam / Kuzari / etc. don't see Saadia-coinage glosses presented as
   * neutral classical Arabic.
   */
  scope?: "saadia";
  source?: "lane" | "blau" | "camel";
  /**
   * Explicit surface-form variants (inflected forms, common pronominal-suffix
   * forms, orthographic alternates). Matched after the exact lemma but before
   * the auto-dict fallback. Kept explicit rather than algorithmic so we never
   * silently strip a suffix off a word that doesn't take one
   * (e.g. אלאה ≠ stem אלא + suffix; מלאיכה ≠ stem מלאיכ + suffix).
   */
  variants?: string[];
};

const STARTER: Entry[] = starter.entries as Entry[];

// Lazy Lane singleton — loaded once, reused thereafter.
type LaneShape = { entries: Entry[] };
let _lane: LaneShape | null = null;
if (typeof window !== "undefined") {
  import("@/data/dictionary-lane.json").then((m) => {
    _lane = m.default as unknown as LaneShape;
  });
}
function getLane(): Entry[] {
  return _lane ? (_lane.entries as Entry[]) : [];
}

/** Strip trailing punctuation that gets glued onto a word (".,:;؛،"). */
function stripPunct(tok: string): string {
  return tok.replace(/^[.,:;؛،"'\s]+|[.,:;؛،"'\s]+$/g, "");
}

/**
 * Lookup-key normalizer applied on BOTH the candidate side and the dict
 * (lemma + variants) side so the two converge to a common comparison form.
 *
 * Two rules:
 *  1. Hebrew final ↔ medial letter forms (ן/נ ם/מ ץ/צ ף/פ ך/כ). JA uses
 *     finals word-final, medials elsewhere — e.g. the lemma אבן (final נ)
 *     inflects to אבנה "his son" (medial נ).
 *  2. Strip a trailing apostrophe. In JA orthography ' marks a consonant
 *     diacritic (ת' = ث, ד' = ذ, כ' = خ, ع'ʿ = غ, etc.); when it sits at
 *     word-end after stripPunct, both token-side and dict-side may or may
 *     not retain it depending on scribal convention. Collapsing the
 *     trailing ' on both sides makes the comparison apostrophe-tolerant.
 */
export function normalizeFinals(s: string): string {
  let r = s
    // Drop Hebrew points/cantillation (U+0591–U+05C7) on BOTH the token and the
    // dictionary side, so a vocalized embedded quote (נִפְלָאוֹת) and a
    // tā-marbūṭa construct variant authored with a tsere (צורהֵ) both converge
    // with their plain forms. No-op on the unvocalized JA/Tafsir corpus.
    .replace(/[֑-ׇ]/g, "")
    .replace(/ך/g, "כ")
    .replace(/ם/g, "מ")
    .replace(/ן/g, "נ")
    .replace(/ף/g, "פ")
    .replace(/ץ/g, "צ");
  if (r.endsWith("'")) r = r.slice(0, -1);
  return r;
}

/**
 * Canonical form used as the key for per-word state (known/learning/etc.)
 * and for collapsing variants. Strips punctuation, leading vav (and) and
 * leading אל (al-) — the two prefixes that are unambiguously prefixes when
 * they lead a JA token. Single-letter ambiguous prefixes (ב ל כ פ) are
 * left in place so that e.g. בית doesn't collide with ית.
 */
export function normalizeToken(rawToken: string): string {
  let t = stripPunct(rawToken);
  if (t.startsWith("ו") && t.length > 1) t = t.slice(1);
  if (t.startsWith("אל") && t.length > 2) t = t.slice(2);
  return t;
}

/**
 * Find dictionary entries for a token. Returns an array because of
 * homographs (e.g. מא = both ما "what" and ماء "water").
 *
 * Candidate-generation chain (composable; first hit wins):
 *   - exact token
 *   - optionally strip leading ו (and-)
 *   - optionally strip one of [ב ל כ פ] (with/to/like/and-then), in either
 *     order with the vav above
 *   - optionally strip leading אל (the-), applied after any of the above
 *
 * So a token like ובאלמחצ'ר produces candidates {ובאלמחצ'ר, באלמחצ'ר,
 * אלמחצ'ר, מחצ'ר} — letting us resolve compound-prefixed surface forms
 * without enumerating every combination as an explicit variant.
 */
/**
 * Generate the normalized candidate-form chain for a raw token, shared by
 * `lookup` and by the per-work Blau overlay (`lib/workNotes.ts`) so the two
 * match a tapped word identically. See the chain description on `lookup`.
 *
 * Returns final↔medial-normalized forms (apply `normalizeFinals` to a
 * dictionary lemma/variant before comparing — `lookup` and `workNotes` do).
 */
export function candidateForms(rawToken: string): string[] {
  // Drop Hebrew points/cantillation (niqqud, teʿamim: U+0591–U+05C7) so a
  // vocalized embedded quote — e.g. the Hebrew verses Qirqisani cites,
  // נִפְלָאוֹת — matches its unvocalized dictionary lemma נפלאות. JA/Tafsir text
  // is unvocalized, so this is a no-op there.
  const tok = stripPunct(rawToken).replace(/[֑-ׇ]/g, "");
  if (!tok) return [];

  const tries = new Set<string>();
  // Apply optional אל-strip on the input, and add both forms.
  function withAlStripped(s: string) {
    if (!s) return;
    tries.add(s);
    if (s.startsWith("אל") && s.length > 2) {
      tries.add(s.slice(2));
    }
  }

  // Layer 1: the token itself
  withAlStripped(tok);

  // Layer 2: strip leading ו (and-)
  let afterVav: string | null = null;
  if (tok.startsWith("ו") && tok.length > 1) {
    afterVav = tok.slice(1);
    withAlStripped(afterVav);
  }

  // Layer 3: strip a single-letter prep [ב ל כ פ] from the original token
  // and (if present) from the post-vav form too.
  const PREFIXES = ["ב", "ל", "כ", "פ"];
  for (const base of [tok, afterVav].filter(Boolean) as string[]) {
    for (const p of PREFIXES) {
      if (base.startsWith(p) && base.length > 1) {
        withAlStripped(base.slice(1));
      }
    }
  }

  const triesArr = Array.from(tries);
  // Expand the candidate chain with final↔medial-normalized forms so e.g.
  // אבנה (medial nun) can match the lemma אבן (final nun).
  return Array.from(new Set([...triesArr, ...triesArr.map(normalizeFinals)]));
}

/**
 * Order a candidate's hits so the most precise entry renders first (the reader
 * shows hits[0] as the headword). An entry whose lemma_ja IS the tapped form
 * (exact citation-form match) beats one that only matched via an inflected
 * `variants[]` entry; ties break to the shorter lemma. This means a proper base
 * entry always wins over a residual conflated/inflected entry that merely lists
 * the base form as a variant — the same defect the data cleanup removes.
 */
function rankHits(hits: Entry[], t: string): Entry[] {
  return [...hits].sort((a, b) => {
    const ax = normalizeFinals(a.lemma_ja) === t ? 0 : 1;
    const bx = normalizeFinals(b.lemma_ja) === t ? 0 : 1;
    if (ax !== bx) return ax - bx;
    return normalizeFinals(a.lemma_ja).length - normalizeFinals(b.lemma_ja).length;
  });
}

export function lookup(rawToken: string): Entry[] {
  const tok = stripPunct(rawToken);
  if (!tok) return [];

  const triesNorm = candidateForms(rawToken);

  // Priority 1: hand-curated starter dictionary (Bereshit-1 exemplars).
  // Match by exact lemma OR by an explicit variant.
  for (const t of triesNorm) {
    const hits = STARTER.filter(
      (e) =>
        normalizeFinals(e.lemma_ja) === t ||
        (e.variants && e.variants.some((v) => normalizeFinals(v) === t)),
    );
    if (hits.length) return rankHits(hits, t);
  }
  // Priority 2: hand-curated Lane-cited dictionary (top-frequency tokens).
  // Walks the same candidate chain so prefixed variants resolve correctly.
  for (const t of triesNorm) {
    const hits = getLane().filter(
      (e) =>
        normalizeFinals(e.lemma_ja) === t ||
        (e.variants && e.variants.some((v) => normalizeFinals(v) === t)),
    );
    if (hits.length) return rankHits(hits, t);
  }
  // (Priority 3, the auto-extracted Camel-tools fallback, has been retired —
  // hand coverage now exceeds 80%; see the import note at the top of this file.)
  return [];
}

// tokenizeJa is re-exported from `lib/tokenize` at the top of this file.
