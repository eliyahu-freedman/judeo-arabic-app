// Build-time corpus + lexicon statistics.
//
// Server-only module: it imports the full corpus index (~1.6 MB) and the Lane
// dictionary (~3.5 MB) so the figures can be computed once at build and
// rendered into static HTML. Do NOT import this from a "use client" component —
// that would drag both JSON blobs into the browser bundle. The reader's
// client-side concordance already streams `public/corpus-index.json` at
// runtime via `lib/corpus.ts`; this module is the static-render counterpart.

import lane from "@/data/dictionary-lane.json";
import starter from "@/data/dictionary-starter.json";
import index from "@/public/corpus-index.json";
import type { Entry } from "./lookup";

type RawIndex = {
  corpora: string[];
  total_tokens: number;
  unique_keys: number;
};

const LANE = lane.entries as Entry[];
const STARTER = starter.entries as Entry[];
const INDEX = index as RawIndex;

const PENTATEUCH_ORDER = ["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"];

function countUniqueRoots(): number {
  const roots = new Set<string>();
  for (const e of [...LANE, ...STARTER]) {
    if (e.root) roots.add(e.root.trim());
  }
  return roots.size;
}

function countBooksAndChapters(): { books: number; chapters: number } {
  const books = new Set<string>();
  for (const c of INDEX.corpora) books.add(c.split(" ")[0]);
  return { books: books.size, chapters: INDEX.corpora.length };
}

const { books, chapters } = countBooksAndChapters();

/**
 * Canonical headline figures for the project, computed from the same data the
 * app already ships. Used by the home-page credentials strip and the
 * methodology page so the numbers can never drift from the underlying corpus.
 */
export const corpusStats = {
  /** Dictionary headwords (hand-curated starter + Lane-cited). */
  dictionaryEntries: LANE.length + STARTER.length,
  /** Distinct triliteral (and other) roots represented across the lexicon. */
  uniqueRoots: countUniqueRoots(),
  /** Total token instances indexed across the Tafsir. */
  totalTokens: INDEX.total_tokens,
  /** Distinct normalised word-keys in the concordance index. */
  uniqueKeys: INDEX.unique_keys,
  /** Tafsir chapters indexed (one corpus entry per chapter). */
  chapters,
  /** Books of the Pentateuch covered. */
  books,
  /** Whether the full Five Books are present. */
  fullPentateuch: PENTATEUCH_ORDER.every((b) =>
    INDEX.corpora.some((c) => c.startsWith(b + " ")),
  ),
} as const;

/** Format an integer with thousands separators (e.g. 81225 → "81,225"). */
export function fmt(n: number): string {
  return n.toLocaleString("en-US");
}
