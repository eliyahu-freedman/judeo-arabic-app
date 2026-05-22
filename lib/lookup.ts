import starter from "@/data/dictionary-starter.json";
import lane from "@/data/dictionary-lane.json";
import auto from "@/data/dictionary-auto.json";

export type Entry = {
  id: string;
  lemma_ja: string;
  lemma_ar: string;
  root: string;
  pos: string;
  gloss_en: string;
  gloss_he: string;
  notes?: string;
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
const LANE: Entry[] = lane.entries as Entry[];
const AUTO: Entry[] = auto.entries as Entry[];

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
function normalizeFinals(s: string): string {
  let r = s
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
export function lookup(rawToken: string): Entry[] {
  const tok = stripPunct(rawToken);
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
  const triesNorm = Array.from(new Set([...triesArr, ...triesArr.map(normalizeFinals)]));

  // Priority 1: hand-curated starter dictionary (Bereshit-1 exemplars).
  // Match by exact lemma OR by an explicit variant.
  for (const t of triesNorm) {
    const hits = STARTER.filter(
      (e) =>
        normalizeFinals(e.lemma_ja) === t ||
        (e.variants && e.variants.some((v) => normalizeFinals(v) === t)),
    );
    if (hits.length) return hits;
  }
  // Priority 2: hand-curated Lane-cited dictionary (top-frequency tokens).
  // Walks the same candidate chain so prefixed variants resolve correctly.
  for (const t of triesNorm) {
    const hits = LANE.filter(
      (e) =>
        normalizeFinals(e.lemma_ja) === t ||
        (e.variants && e.variants.some((v) => normalizeFinals(v) === t)),
    );
    if (hits.length) return hits;
  }
  // Priority 3: auto-extracted Camel-tools dictionary (unverified, MSA).
  // Keyed by normalizeToken — single lookup, no chain.
  const autoKey = normalizeToken(rawToken);
  if (autoKey) {
    const hits = AUTO.filter((e) => e.lemma_ja === autoKey);
    if (hits.length) return hits;
  }
  return [];
}

/**
 * Split a JA string into tokens for rendering. Words (Hebrew letters,
 * plus the ASCII apostrophe that JA uses for the gershayim diacritic)
 * are returned as {kind: "word"}; whitespace and punctuation are
 * returned as {kind: "sep"} so the renderer can preserve spacing.
 */
export function tokenizeJa(text: string): { kind: "word" | "sep"; text: string }[] {
  const out: { kind: "word" | "sep"; text: string }[] = [];
  let buf = "";
  let bufKind: "word" | "sep" | null = null;
  const isWordChar = (c: string) =>
    /[֐-׿']/.test(c); // Hebrew block + ASCII apostrophe (JA gershayim)

  for (const c of text) {
    const kind: "word" | "sep" = isWordChar(c) ? "word" : "sep";
    if (kind === bufKind) {
      buf += c;
    } else {
      if (buf) out.push({ kind: bufKind!, text: buf });
      buf = c;
      bufKind = kind;
    }
  }
  if (buf) out.push({ kind: bufKind!, text: buf });
  return out;
}
