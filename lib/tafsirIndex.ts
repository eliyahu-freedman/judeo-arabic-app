// Server-only: relies on node:fs. Don't import from client components.
import { promises as fs } from "node:fs";
import path from "node:path";

const DATA_DIR = path.join(process.cwd(), "data");

const FILE_RE = /^tafsir-([a-z]+)-(\d+)\.json$/;

// Canonical book order (slug → display name). Add as new books are ingested.
const BOOK_ORDER = ["bereshit", "shemot", "vayikra", "bamidbar", "devarim"] as const;
const BOOK_DISPLAY: Record<string, string> = {
  bereshit: "Bereshit",
  shemot: "Shemot",
  vayikra: "Vayikra",
  bamidbar: "Bamidbar",
  devarim: "Devarim",
};

export type ChapterMeta = {
  /** URL slug, lowercase: "bereshit" */
  bookSlug: string;
  /** Display label: "Bereshit" */
  book: string;
  chapter: number;
  /** Order index used for prev/next across books */
  ord: number;
};

export type ChapterRecord = ChapterMeta & {
  hasEnglish: boolean;
};

let _cache: ChapterRecord[] | null = null;

export async function listChapters(): Promise<ChapterRecord[]> {
  if (_cache) return _cache;
  let names: string[] = [];
  try {
    names = await fs.readdir(DATA_DIR);
  } catch {
    return (_cache = []);
  }
  const records: ChapterRecord[] = [];
  for (const name of names) {
    const m = FILE_RE.exec(name);
    if (!m) continue;
    const bookSlug = m[1];
    const chapter = Number(m[2]);
    const englishName = `tafsir-${bookSlug}-${chapter}-english.json`;
    const hasEnglish = names.includes(englishName);
    records.push({
      bookSlug,
      book: BOOK_DISPLAY[bookSlug] ?? bookSlug,
      chapter,
      hasEnglish,
      ord: 0, // assigned below
    });
  }
  records.sort((a, b) => {
    const ai = BOOK_ORDER.indexOf(a.bookSlug as (typeof BOOK_ORDER)[number]);
    const bi = BOOK_ORDER.indexOf(b.bookSlug as (typeof BOOK_ORDER)[number]);
    if (ai !== bi) return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
    return a.chapter - b.chapter;
  });
  records.forEach((r, i) => (r.ord = i));
  return (_cache = records);
}

export async function findChapter(
  bookSlug: string,
  chapter: number,
): Promise<{
  record: ChapterRecord;
  prev: ChapterMeta | null;
  next: ChapterMeta | null;
} | null> {
  const all = await listChapters();
  const idx = all.findIndex(
    (r) => r.bookSlug === bookSlug && r.chapter === chapter,
  );
  if (idx === -1) return null;
  return {
    record: all[idx],
    prev: idx > 0 ? all[idx - 1] : null,
    next: idx < all.length - 1 ? all[idx + 1] : null,
  };
}

/** Read the JA chapter JSON. */
export async function readChapter(
  bookSlug: string,
  chapter: number,
): Promise<{
  book: string;
  chapter: number;
  verses: {
    ch: number;
    v: number;
    hebrew: string;
    ja: string;
    arabic: string;
    hebrew_translation: string;
  }[];
}> {
  const file = path.join(DATA_DIR, `tafsir-${bookSlug}-${chapter}.json`);
  const raw = await fs.readFile(file, "utf-8");
  return JSON.parse(raw);
}

/** Read the optional English sidecar; returns {} if missing. */
export async function readChapterEnglish(
  bookSlug: string,
  chapter: number,
): Promise<Record<string, string>> {
  const file = path.join(DATA_DIR, `tafsir-${bookSlug}-${chapter}-english.json`);
  try {
    const raw = await fs.readFile(file, "utf-8");
    const data = JSON.parse(raw) as { translations?: Record<string, string> };
    return data.translations ?? {};
  } catch {
    return {};
  }
}

/**
 * Read the optional JA↔EN phrase-pair alignment sidecar; returns {} if
 * missing. Shape: { [verseNumber]: [{ja, en}, ...] }.
 */
export async function readChapterAlignment(
  bookSlug: string,
  chapter: number,
): Promise<Record<string, { ja: string; en: string }[]>> {
  const file = path.join(
    DATA_DIR,
    `tafsir-${bookSlug}-${chapter}-alignment.json`,
  );
  try {
    const raw = await fs.readFile(file, "utf-8");
    const data = JSON.parse(raw) as {
      alignments?: Record<string, { ja: string; en: string }[]>;
    };
    return data.alignments ?? {};
  } catch {
    return {};
  }
}
