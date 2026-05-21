import starter from "@/data/dictionary-starter.json";
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
};

const STARTER: Entry[] = starter.entries as Entry[];
const AUTO: Entry[] = auto.entries as Entry[];

/** Strip trailing punctuation that gets glued onto a word (".,:;؛،"). */
function stripPunct(tok: string): string {
  return tok.replace(/^[.,:;؛،"'\s]+|[.,:;؛،"'\s]+$/g, "");
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
 * Fallback chain (first hit wins):
 *   1. exact match
 *   2. strip leading vav (ו)
 *   3. strip leading vav + leading אל (al-)
 *   4. strip leading אל (al-)
 *   5. strip a single-letter prepositional/conjunction prefix (ב ל כ פ ת ס נ י)
 */
export function lookup(rawToken: string): Entry[] {
  const tok = stripPunct(rawToken);
  if (!tok) return [];

  const tries: string[] = [tok];
  if (tok.startsWith("ו") && tok.length > 1) {
    const noVav = tok.slice(1);
    tries.push(noVav);
    if (noVav.startsWith("אל") && noVav.length > 2) {
      tries.push(noVav.slice(2));
    }
  }
  if (tok.startsWith("אל") && tok.length > 2) {
    tries.push(tok.slice(2));
  }
  // Handful of single-letter prefixes (rough — won't always be right).
  const PREFIXES = ["ב", "ל", "כ", "פ"];
  for (const p of PREFIXES) {
    if (tok.startsWith(p) && tok.length > 1) {
      tries.push(tok.slice(1));
    }
  }

  const seen = new Set<string>();
  for (const t of tries) {
    if (seen.has(t)) continue;
    seen.add(t);
    const hits = STARTER.filter((e) => e.lemma_ja === t);
    if (hits.length) return hits;
  }
  // Fallback: auto-extracted (Lane). Auto dict is keyed by normalizeToken so
  // only that form will hit — no need to walk the candidate chain again.
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
