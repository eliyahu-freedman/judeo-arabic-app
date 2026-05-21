import schedule from "@/data/parsha-schedule.json";

export type ParshaEntry = {
  /** ISO date (yyyy-mm-dd) of the Shabbat this parsha is read in the diaspora */
  date: string;
  hdate: string;
  /** English title (e.g. "Naso", "Behar-Bechukotai") */
  title: string;
  /** Hebrew title with the "פרשת " prefix */
  hebrew: string;
  /** Seven aliyah ref strings in Hebcal format (e.g. "Numbers 1:1-1:19") */
  aliyot: string[];
  /** Full parsha ref (e.g. "Numbers 1:1-4:20") */
  torah: string;
};

export type BookSlug = "bereshit" | "shemot" | "vayikra" | "bamidbar" | "devarim";

export const BOOK_DISPLAY: Record<BookSlug, string> = {
  bereshit: "Bereshit",
  shemot: "Shemot",
  vayikra: "Vayikra",
  bamidbar: "Bamidbar",
  devarim: "Devarim",
};

export const BOOK_ORDER: BookSlug[] = [
  "bereshit",
  "shemot",
  "vayikra",
  "bamidbar",
  "devarim",
];

const HEBCAL_BOOK_TO_SLUG: Record<string, BookSlug> = {
  Genesis: "bereshit",
  Exodus: "shemot",
  Leviticus: "vayikra",
  Numbers: "bamidbar",
  Deuteronomy: "devarim",
};

export type VerseRef = { book: BookSlug; ch: number; v: number };
export type Range = { start: VerseRef; end: VerseRef };

/** Parse a Hebcal ref like "Numbers 1:1-1:19" or "Exodus 23:23-25:38". */
export function parseRange(ref: string): Range | null {
  const m = /^([A-Za-z]+) (\d+):(\d+)-(?:(\d+):)?(\d+)$/.exec(ref);
  if (!m) return null;
  const book = HEBCAL_BOOK_TO_SLUG[m[1]];
  if (!book) return null;
  const startCh = Number(m[2]);
  const startV = Number(m[3]);
  const endCh = m[4] ? Number(m[4]) : startCh;
  const endV = Number(m[5]);
  return {
    start: { book, ch: startCh, v: startV },
    end: { book, ch: endCh, v: endV },
  };
}

export const PARSHA_SCHEDULE: ParshaEntry[] = (schedule as ParshaEntry[]).slice().sort(
  (a, b) => a.date.localeCompare(b.date),
);

/** Slug a parsha title for URLs: "Behar-Bechukotai" → "behar-bechukotai". */
export function parshaSlug(title: string): string {
  return title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
}

/**
 * Look up the parsha most relevant to a given date in the diaspora-Shnayim-
 * Mikra sense: the upcoming (or today's) Shabbat reading. If the date IS a
 * Shabbat, that Shabbat's parsha. Otherwise, the next Shabbat's parsha.
 */
export function parshaForDate(date: Date): ParshaEntry | null {
  const iso = isoDate(date);
  for (const p of PARSHA_SCHEDULE) {
    if (p.date >= iso) return p;
  }
  return PARSHA_SCHEDULE[PARSHA_SCHEDULE.length - 1] ?? null;
}

/**
 * Daily aliyah index (1..7) by day of week, Sun=1, Mon=2, ..., Sat=7.
 * Follows the common Shnayim-Mikra weekly study pattern.
 */
export function aliyahForDate(date: Date): number {
  const dow = date.getDay(); // 0..6, Sun=0
  return dow === 6 ? 7 : dow + 1;
}

export type CurrentReading = {
  parsha: ParshaEntry;
  aliyahNumber: number; // 1..7
  range: Range;
};

export function currentReading(date: Date = new Date()): CurrentReading | null {
  const p = parshaForDate(date);
  if (!p) return null;
  const n = aliyahForDate(date);
  const ref = p.aliyot[n - 1];
  const range = ref ? parseRange(ref) : null;
  if (!range) return null;
  return { parsha: p, aliyahNumber: n, range };
}

/**
 * Build a URL pointing at the first verse of a range in the Tafsir reader.
 * The reader anchors verses by id `verse-{ch}-{v}` and renders one chapter at
 * a time, so we link to the start chapter.
 */
export function rangeHref(range: Range): string {
  const { book, ch, v } = range.start;
  return `/tafsir/${book}/${ch}#verse-${ch}-${v}`;
}

export const ALIYAH_LABELS = [
  "Rishon",
  "Sheni",
  "Shlishi",
  "Revi'i",
  "Chamishi",
  "Shishi",
  "Shevi'i",
];

export const ALIYAH_DAY_LABELS = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Shabbat",
];

function isoDate(d: Date): string {
  const y = d.getFullYear();
  const m = String(d.getMonth() + 1).padStart(2, "0");
  const day = String(d.getDate()).padStart(2, "0");
  return `${y}-${m}-${day}`;
}
