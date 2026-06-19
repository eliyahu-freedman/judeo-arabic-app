// Server-only lexicon engine for the standalone search + lemma pages.
//
// This is the request-time, book-aware counterpart to the client reader's
// concordance (lib/corpus.ts). It reads the Tafsir JSON directly via
// lib/tafsirIndex (node:fs) and tokenises each verse with the SAME canonical
// rules the reader uses (tokenizeJa + normalizeToken), so a word's key here is
// identical to its key in public/corpus-index.json. The crucial difference:
// every attestation here keeps its BOOK, which the shipped index drops — that
// is what lets a lemma page link each occurrence to the right chapter.
//
// Do NOT import from a client component: it depends on node:fs. The whole
// concordance is built once per server instance (lazy, memoised).

import { listChapters, readChapter } from "./tafsirIndex";
import { lookup, normalizeToken, normalizeFinals, type Entry } from "./lookup";
import { tokenizeJa } from "./tokenize";
import lane from "@/data/dictionary-lane.json";
import starter from "@/data/dictionary-starter.json";
import advancedIndexRaw from "@/data/advanced-index.json";

type AdvancedUse = { work: string; href: string; n: number };
type AdvancedKeyEntry = {
  count: number;
  att: AdvancedUse[];
  truncated?: boolean;
  sample?: { surface: string; snippet: string } | null;
};
// Judeo-Arabic concordance over the Advanced library (Moreh, Bahya, Saadia
// Emunot, Qirqisani, Kuzari), keyed by normalizeToken — built by
// scripts/build_advanced_index.py. Lets a lemma page show one word's uses
// across the whole library, not just Saadia's Tafsir.
const ADVANCED_INDEX = (advancedIndexRaw as { tokens: Record<string, AdvancedKeyEntry> }).tokens;

const DICT: Entry[] = [
  ...(starter.entries as Entry[]),
  ...(lane.entries as Entry[]),
];

export type Attestation = {
  bookSlug: string;
  book: string;
  ch: number;
  v: number;
  surface: string;
};

export type ConcordanceEntry = {
  /** Total token instances under this key, across all books. */
  count: number;
  /** Every occurrence, in canonical (book, chapter, verse) order. */
  attestations: Attestation[];
};

type VerseText = {
  bookSlug: string;
  book: string;
  ch: number;
  v: number;
  ja: string;
};

type Concordance = {
  byKey: Map<string, ConcordanceEntry>;
  /** Keyed "bookSlug:ch:v" → the full JA verse, for KWIC context. */
  verses: Map<string, VerseText>;
};

/** Light punctuation trim for display surfaces (mirrors lookup.ts stripPunct).
 *  tokenizeJa already excludes most punctuation from word tokens; this catches
 *  a stray leading/trailing apostrophe or quote. */
function cleanSurface(tok: string): string {
  return tok.replace(/^[.,:;؛،"'\s]+|[.,:;؛،"'\s]+$/g, "");
}

let _concordance: Promise<Concordance> | null = null;

async function build(): Promise<Concordance> {
  const byKey = new Map<string, ConcordanceEntry>();
  const verses = new Map<string, VerseText>();

  const chapters = await listChapters();
  for (const c of chapters) {
    let data;
    try {
      data = await readChapter(c.bookSlug, c.chapter);
    } catch {
      continue;
    }
    for (const verse of data.verses) {
      const vKey = `${c.bookSlug}:${verse.ch}:${verse.v}`;
      verses.set(vKey, {
        bookSlug: c.bookSlug,
        book: data.book,
        ch: verse.ch,
        v: verse.v,
        ja: verse.ja,
      });
      for (const tok of tokenizeJa(verse.ja)) {
        if (tok.kind !== "word") continue;
        const key = normalizeToken(tok.text);
        if (!key) continue;
        const surface = cleanSurface(tok.text);
        if (!surface) continue;
        let entry = byKey.get(key);
        if (!entry) {
          entry = { count: 0, attestations: [] };
          byKey.set(key, entry);
        }
        entry.count++;
        entry.attestations.push({
          bookSlug: c.bookSlug,
          book: data.book,
          ch: verse.ch,
          v: verse.v,
          surface,
        });
      }
    }
  }
  return { byKey, verses };
}

function loadConcordance(): Promise<Concordance> {
  return (_concordance ??= build());
}

// ─── Search ────────────────────────────────────────────────────────────────

export type SearchResult = {
  /** Normalised concordance key — the lemma page's URL segment. */
  key: string;
  lemma_ja: string;
  lemma_ar: string;
  root: string;
  pos: string;
  gloss_en: string;
  gloss_he: string;
  /** Corpus frequency under `key`, 0 if unattested in the indexed Tafsir. */
  count: number;
  matchKind: "lemma" | "variant" | "gloss" | "root";
};

/** The concordance key a dictionary entry maps to (its citation form). */
function entryKey(e: Entry): string {
  return normalizeToken(e.lemma_ja);
}

/** Drop the JA gershayim apostrophe (and its Unicode variants) so a learner
 *  who omits the diacritic — searching כלק for כ׳לק — still matches. */
function stripApos(s: string): string {
  return s.replace(/['׳״ʼʹ’‘]/g, "");
}

/**
 * Search the lexicon by Judeo-Arabic word, Arabic word, root, or English/
 * Hebrew gloss. Exact-lemma matches rank first, then variant, root, gloss;
 * within a tier, more-frequent words come first. Returns up to `limit`.
 */
export async function searchLexicon(
  rawQuery: string,
  limit = 60,
): Promise<SearchResult[]> {
  const q = rawQuery.trim();
  if (!q) return [];

  const conc = await loadConcordance();
  const qNorm = normalizeFinals(normalizeToken(q));
  const qLoose = stripApos(qNorm);
  const qLower = q.toLowerCase();

  const scored = new Map<string, { e: Entry; rank: number; kind: SearchResult["matchKind"] }>();

  const consider = (e: Entry, rank: number, kind: SearchResult["matchKind"]) => {
    const id = e.id;
    const prev = scored.get(id);
    if (!prev || rank < prev.rank) scored.set(id, { e, rank, kind });
  };

  for (const e of DICT) {
    const lemmaNorm = normalizeFinals(normalizeToken(e.lemma_ja));
    // Tier 0/1 — exact then prefix on the Judeo-Arabic lemma. Apostrophe-loose
    // exact match (qLoose) sits just below exact so omitting the gershayim
    // diacritic still finds the word.
    if (lemmaNorm === qNorm) consider(e, 0, "lemma");
    else if (qLoose && stripApos(lemmaNorm) === qLoose) consider(e, 1, "lemma");
    else if (qNorm && lemmaNorm.startsWith(qNorm)) consider(e, 1, "lemma");
    else if (
      e.variants?.some((v) => {
        const vn = normalizeFinals(normalizeToken(v));
        return vn === qNorm || (qLoose && stripApos(vn) === qLoose);
      })
    )
      consider(e, 2, "variant");
    // Arabic-script lemma (exact / contains).
    if (e.lemma_ar && (e.lemma_ar === q || e.lemma_ar.includes(q)))
      consider(e, 2, "lemma");
    // Root.
    if (e.root && e.root.toLowerCase() === qLower) consider(e, 3, "root");
    // Gloss (English or Hebrew), substring.
    if (
      (e.gloss_en && e.gloss_en.toLowerCase().includes(qLower)) ||
      (e.gloss_he && e.gloss_he.includes(q))
    )
      consider(e, 4, "gloss");
  }

  const results: SearchResult[] = [...scored.values()].map(({ e, kind }) => {
    const key = entryKey(e);
    return {
      key,
      lemma_ja: e.lemma_ja,
      lemma_ar: e.lemma_ar,
      root: e.root,
      pos: e.pos,
      gloss_en: e.gloss_en,
      gloss_he: e.gloss_he,
      count: conc.byKey.get(key)?.count ?? 0,
      matchKind: kind,
    };
  });

  // Sort by rank tier, then descending corpus frequency, then shorter lemma.
  const rankOf = (r: SearchResult) =>
    r.matchKind === "lemma" ? 0 : r.matchKind === "variant" ? 1 : r.matchKind === "root" ? 2 : 3;
  results.sort((a, b) => {
    const ra = rankOf(a);
    const rb = rankOf(b);
    if (ra !== rb) return ra - rb;
    if (b.count !== a.count) return b.count - a.count;
    return a.lemma_ja.length - b.lemma_ja.length;
  });

  return results.slice(0, limit);
}

// ─── Lemma page ──────────────────────────────────────────────────────────────

export type SurfaceVariant = { surface: string; count: number };

export type BookAttestations = {
  bookSlug: string;
  book: string;
  /** One row per occurrence, in chapter/verse order, with KWIC verse text. */
  rows: { ch: number; v: number; surface: string; ja: string }[];
};

export type LemmaData = {
  key: string;
  /** Dictionary entries sharing this key (homographs possible). */
  entries: Entry[];
  /** Total corpus frequency under this key. */
  count: number;
  /** Distinct surface forms that collapse into this key, most frequent first. */
  variants: SurfaceVariant[];
  /** Attestations grouped by book, in canonical order. */
  byBook: BookAttestations[];
  /** Uses of this key across the Advanced library (Moreh, Bahya, …). */
  library?: {
    count: number;
    uses: AdvancedUse[];
    truncated: boolean;
    sample?: { surface: string; snippet: string } | null;
  };
};

const BOOK_SLUG_ORDER = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"];

/**
 * Everything a lemma page needs for one normalised word-key: its dictionary
 * entry/entries, its corpus frequency, the surface forms that fall under it,
 * and every attestation grouped by book with KWIC context. Returns null only
 * when the key is neither in the dictionary nor the corpus.
 */
export async function getLemma(rawKey: string): Promise<LemmaData | null> {
  const key = normalizeToken(rawKey.trim());
  if (!key) return null;

  const conc = await loadConcordance();
  const entries = lookup(key);
  const concEntry = conc.byKey.get(key);
  const adv = ADVANCED_INDEX[key];

  if (!entries.length && !concEntry && !adv) return null;

  // Surface-form breakdown.
  const surfaceCounts = new Map<string, number>();
  for (const a of concEntry?.attestations ?? []) {
    surfaceCounts.set(a.surface, (surfaceCounts.get(a.surface) ?? 0) + 1);
  }
  const variants: SurfaceVariant[] = [...surfaceCounts.entries()]
    .map(([surface, count]) => ({ surface, count }))
    .sort((a, b) => b.count - a.count);

  // Group attestations by book, deduping repeated verses but keeping each
  // surface occurrence as its own row (KWIC convention).
  const byBookMap = new Map<string, BookAttestations>();
  for (const a of concEntry?.attestations ?? []) {
    let group = byBookMap.get(a.bookSlug);
    if (!group) {
      group = { bookSlug: a.bookSlug, book: a.book, rows: [] };
      byBookMap.set(a.bookSlug, group);
    }
    const ja = conc.verses.get(`${a.bookSlug}:${a.ch}:${a.v}`)?.ja ?? "";
    group.rows.push({ ch: a.ch, v: a.v, surface: a.surface, ja });
  }
  const byBook = [...byBookMap.values()].sort(
    (a, b) => BOOK_SLUG_ORDER.indexOf(a.bookSlug) - BOOK_SLUG_ORDER.indexOf(b.bookSlug),
  );
  for (const g of byBook) {
    g.rows.sort((a, b) => (a.ch - b.ch) || (a.v - b.v));
  }

  return {
    key,
    entries,
    count: concEntry?.count ?? 0,
    variants,
    byBook,
    library: adv
      ? {
          count: adv.count,
          uses: adv.att,
          truncated: !!adv.truncated,
          sample: adv.sample ?? null,
        }
      : undefined,
  };
}
