import { normalizeToken } from "@/lib/lookup";

/**
 * Key-term footnotes for the advanced prose reader. A lighter cousin of
 * `lib/divergence.ts`: instead of a global singleton loaded from one file,
 * term cards travel inside each work's own JSON (passed in as data), so the
 * reader stays content-agnostic and two works can gloss the same surface
 * form differently.
 */

export type TermCard = {
  /** Stable id, referenced by AlignedSegment.terms[].termId. */
  id: string;
  /** Canonical Judeo-Arabic surface form (the headword to mark/match). */
  ja: string;
  /** Arabic-script form, for reference. */
  ar?: string;
  /** Latin transliteration, e.g. "tawḥīd". */
  translit?: string;
  /** Short English gloss. */
  gloss: string;
  /** Longer note: why the term matters, how it's used here. */
  note?: string;
  /** Optional free-text references (editions, secondary lit). */
  refs?: string[];
  /**
   * Extra surface forms to index, so single tokens of a multi-word headword
   * (or inflected forms) still resolve. Matched like `ja` after prefix-strip.
   */
  variants?: string[];
};

/** A segment-level pointer from a JA surface form to a shared TermCard. */
export type TermRef = { ja: string; termId: string };

export type TermIndex = Map<string, TermCard>;

/** Index a work's term cards by their canonical JA surface form. */
export function buildTermIndex(terms: TermCard[] | undefined): TermIndex {
  const m = new Map<string, TermCard>();
  for (const t of terms ?? []) {
    m.set(t.ja, t);
    for (const v of t.variants ?? []) m.set(v, t);
  }
  return m;
}

/**
 * Resolve a tapped/highlighted token to a term card. Mirrors the
 * prefix-stripping chain in `lib/lookup.ts#lookup` and `lookupDivergence`:
 * exact → no-vav → no-vav-no-al → no-al → single-letter-prefix → normalized.
 */
export function lookupTerm(index: TermIndex, rawToken: string): TermCard | null {
  if (index.size === 0) return null;
  const tok = rawToken.replace(/^[.,:;؛،"'\s]+|[.,:;؛،"'\s]+$/g, "");
  if (!tok) return null;

  const tries: string[] = [tok];
  if (tok.startsWith("ו") && tok.length > 1) {
    const noVav = tok.slice(1);
    tries.push(noVav);
    if (noVav.startsWith("אל") && noVav.length > 2) tries.push(noVav.slice(2));
  }
  if (tok.startsWith("אל") && tok.length > 2) tries.push(tok.slice(2));
  for (const p of ["ב", "ל", "כ", "פ"]) {
    if (tok.startsWith(p) && tok.length > 1) tries.push(tok.slice(1));
  }
  tries.push(normalizeToken(rawToken));

  for (const t of tries) {
    const hit = index.get(t);
    if (hit) return hit;
  }
  return null;
}

export function hasTerm(index: TermIndex, rawToken: string): boolean {
  return lookupTerm(index, rawToken) !== null;
}
