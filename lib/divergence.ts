import data from "@/data/tafsir-divergence.json";
import { normalizeToken } from "@/lib/lookup";

/**
 * Display register for a Saadia / Blau pairing in the Tafsir reader.
 *
 * - **twist**: paradigm-shifting move (anti-anthropomorphic, philosophical,
 *   midrashic identification, semantic loanshift). Wine underline + full
 *   classical-vs-Saadia banner. Rare by design (~30–80 Torah-wide).
 * - **note**: semantic surprise without theological reframe — calque,
 *   register shift, technical extension, grammatical methodology. Muted
 *   underline + lighter banner. ~300 Torah-wide.
 * - **gloss**: non-obvious Heb→Ar pairing pedagogically useful for JA
 *   acquisition (non-cognate, false friend, divergent field). No underline;
 *   surfaces only on tap as a compact one-line card. ~575 Torah-wide.
 *
 * Omitted `tier` defaults to `twist` for back-compat with the original 32
 * entries shipped before tiering existed.
 */
export type DivergenceTier = "twist" | "note" | "gloss";

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
  /** Display register. Defaults to `twist` when omitted. */
  tier?: DivergenceTier;
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

/**
 * Return the display tier for a token, or null if no entry exists.
 * Lets the reader cheaply gate the underline (twist + note get it; gloss
 * is hover-only) without re-walking the prefix-stripping chain twice.
 */
export function divergenceTier(rawToken: string): DivergenceTier | null {
  const d = lookupDivergence(rawToken);
  if (!d) return null;
  return d.tier ?? "twist";
}
