// Unified review-deck resolver.
//
// The FSRS map in lib/wordState.ts is keyed by arbitrary strings. Tafsir/first-50
// words use a bare normalized JA token as the key (so a word tapped in the Tafsir
// reader and the same word added from the First-50 lesson share ONE deck entry).
// Beginner items that aren't dictionary words use a NAMESPACED key:
//   cognate       → `cog:<rank>`
//   alphabet letter → `ltr:<ja>`
// resolveDeckItem() turns any key back into a renderable card for /review.

import { lookup, normalizeToken, type Entry } from "./lookup";
import alphabetData from "@/data/alphabet.json";
import cognatesData from "@/data/cognates.json";

export type Letter = {
  ja: string;
  ar: string;
  phoneme: string;
  name: string;
  example_ja: string;
  example_ar: string;
  example_translit: string;
  example_gloss: string;
};

export type Cognate = {
  rank: number;
  modern_he: string;
  modern_translit: string;
  modern_en: string;
  arabic: string;
  arabic_translit: string;
  ja_form: string | null;
  story: string;
  group: string;
};

export type DeckItem =
  | { kind: "word"; key: string; front: string; entries: Entry[] }
  | { kind: "cognate"; key: string; front: string; cognate: Cognate }
  | { kind: "letter"; key: string; front: string; letter: Letter }
  | { kind: "unknown"; key: string; front: string };

const COG_PREFIX = "cog:";
const LTR_PREFIX = "ltr:";

export function deckKeyForCognate(rank: number): string {
  return `${COG_PREFIX}${rank}`;
}

export function deckKeyForLetter(ja: string): string {
  return `${LTR_PREFIX}${ja}`;
}

// Flatten the lesson-keyed alphabet inventory into a single letter list.
const ALL_LETTERS: Letter[] = Object.values(
  (alphabetData as { lessons: Record<string, { letters: Letter[] }> }).lessons
).flatMap((l) => l.letters);

const COGNATES: Cognate[] = (cognatesData as { entries: Cognate[] }).entries;

export function resolveDeckItem(key: string): DeckItem {
  if (key.startsWith(COG_PREFIX)) {
    const rank = Number(key.slice(COG_PREFIX.length));
    const cognate = COGNATES.find((c) => c.rank === rank);
    if (cognate) {
      return {
        kind: "cognate",
        key,
        front: cognate.ja_form ?? cognate.arabic,
        cognate,
      };
    }
    return { kind: "unknown", key, front: key };
  }

  if (key.startsWith(LTR_PREFIX)) {
    const ja = key.slice(LTR_PREFIX.length);
    const letter = ALL_LETTERS.find((l) => l.ja === ja);
    if (letter) {
      return { kind: "letter", key, front: letter.ja, letter };
    }
    return { kind: "unknown", key, front: ja };
  }

  // Bare key → a dictionary word (Tafsir / First-50).
  return { kind: "word", key, front: key, entries: lookup(key) };
}

// Convenience: the canonical key a First-50 word should use (same normalization
// the Tafsir reader applies, so the two sources dedup into one deck entry).
export function deckKeyForWord(lemmaJa: string): string {
  return normalizeToken(lemmaJa);
}
