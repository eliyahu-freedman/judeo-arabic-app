import data from "@/data/tafsir-divergence.json";
import { normalizeToken } from "@/lib/lookup";

export type DivergenceEntry = {
  lemma_ja: string;
  lemma_ar: string;
  root: string;
  classical_en: string;
  classical_he: string;
  saadia_en: string;
  saadia_he: string;
  mechanism: string;
  verses: { book: string; ch: number; v: number }[];
  /**
   * Additional surface forms (with pronoun suffixes, accusative -א, etc.)
   * that should resolve to this entry. The lookup chain only strips
   * leading prefixes, so inflected forms must be listed explicitly.
   */
  variants?: string[];
  /**
   * Honest attribution of what informed this entry, drawn from the
   * top-level `_sources` legend. Required so we never overclaim Blau.
   */
  sources: string[];
  /**
   * If Blau's Dictionary of Medieval Judaeo-Arabic Texts (2006) has
   * an entry that bears on the present gloss, record root + sense and
   * how directly it supports the claim. Absent means no Blau Dict
   * backing — say so plainly rather than implying one.
   */
  blau_dict?: {
    root: string;
    sense: string;
    relation: "direct" | "adjacent" | "different-sense";
  };
  /**
   * If Blau's Festschrift article ('עיונים בתרגום רס"ג לבראשית א-יב')
   * treats the same verse — even on a different lexeme — record the
   * page and explain the relationship. Marks the present entry as
   * adjacent-but-independent rather than as Blau-derived.
   */
  blau_festschrift?: {
    page: number;
    lemma_he: string;
    relation:
      | "direct"
      | "same-verse-different-lexeme"
      | "parallel-pattern";
    note: string;
  };
};

const ENTRIES: DivergenceEntry[] = (
  data as unknown as { entries: DivergenceEntry[] }
).entries;

const BY_LEMMA = new Map<string, DivergenceEntry>();
for (const e of ENTRIES) {
  BY_LEMMA.set(e.lemma_ja, e);
  for (const v of e.variants ?? []) BY_LEMMA.set(v, e);
}

/**
 * Look up a divergence entry for a tapped/highlighted token.
 * Mirrors the prefix-stripping chain in `lib/lookup.ts#lookup`:
 * exact → no-vav → no-vav-no-al → no-al → single-letter-prefix → normalized.
 */
export function lookupDivergence(rawToken: string): DivergenceEntry | null {
  const tok = rawToken.replace(/^[.,:;؛،"'\s]+|[.,:;؛،"'\s]+$/g, "");
  if (!tok) return null;

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
  for (const p of ["ב", "ל", "כ", "פ"]) {
    if (tok.startsWith(p) && tok.length > 1) {
      tries.push(tok.slice(1));
    }
  }
  tries.push(normalizeToken(rawToken));

  for (const t of tries) {
    const hit = BY_LEMMA.get(t);
    if (hit) return hit;
  }
  return null;
}

export function hasDivergence(rawToken: string): boolean {
  return lookupDivergence(rawToken) !== null;
}
