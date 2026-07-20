// Aggregates the per-chapter key-term cards from every Moreh Nevukhim chapter
// (data/moreh-bab{1..28}.json) into one flat, chapter-tagged list — the data
// behind the "Atlas of God-Language" index. Pure aggregation of the `terms[]`
// already authored in each chapter file; no new content. Server/build only.

import { MOREH_CHAPTERS, morehHref } from "@/app/advanced/rambam-moreh-nevukhim/chapters";

import bab1 from "@/data/moreh-bab1.json";
import bab2 from "@/data/moreh-bab2.json";
import bab3 from "@/data/moreh-bab3.json";
import bab4 from "@/data/moreh-bab4.json";
import bab5 from "@/data/moreh-bab5.json";
import bab6 from "@/data/moreh-bab6.json";
import bab7 from "@/data/moreh-bab7.json";
import bab8 from "@/data/moreh-bab8.json";
import bab9 from "@/data/moreh-bab9.json";
import bab10 from "@/data/moreh-bab10.json";
import bab11 from "@/data/moreh-bab11.json";
import bab12 from "@/data/moreh-bab12.json";
import bab13 from "@/data/moreh-bab13.json";
import bab14 from "@/data/moreh-bab14.json";
import bab15 from "@/data/moreh-bab15.json";
import bab16 from "@/data/moreh-bab16.json";
import bab17 from "@/data/moreh-bab17.json";
import bab18 from "@/data/moreh-bab18.json";
import bab19 from "@/data/moreh-bab19.json";
import bab20 from "@/data/moreh-bab20.json";
import bab21 from "@/data/moreh-bab21.json";
import bab22 from "@/data/moreh-bab22.json";
import bab23 from "@/data/moreh-bab23.json";
import bab24 from "@/data/moreh-bab24.json";
import bab25 from "@/data/moreh-bab25.json";
import bab26 from "@/data/moreh-bab26.json";
import bab27 from "@/data/moreh-bab27.json";
import bab28 from "@/data/moreh-bab28.json";
import bab29 from "@/data/moreh-bab29.json";
import bab30 from "@/data/moreh-bab30.json";
import bab31 from "@/data/moreh-bab31.json";
import bab32 from "@/data/moreh-bab32.json";
import bab33 from "@/data/moreh-bab33.json";
import bab34 from "@/data/moreh-bab34.json";
import bab35 from "@/data/moreh-bab35.json";
import bab36 from "@/data/moreh-bab36.json";
import bab37 from "@/data/moreh-bab37.json";
import bab38 from "@/data/moreh-bab38.json";
import bab39 from "@/data/moreh-bab39.json";
import bab40 from "@/data/moreh-bab40.json";
import bab41 from "@/data/moreh-bab41.json";
import bab42 from "@/data/moreh-bab42.json";
import bab43 from "@/data/moreh-bab43.json";
import bab44 from "@/data/moreh-bab44.json";
import bab45 from "@/data/moreh-bab45.json";
import bab46 from "@/data/moreh-bab46.json";
import bab47 from "@/data/moreh-bab47.json";
import bab48 from "@/data/moreh-bab48.json";
import bab49 from "@/data/moreh-bab49.json";
import bab50 from "@/data/moreh-bab50.json";
import bab51 from "@/data/moreh-bab51.json";
import bab52 from "@/data/moreh-bab52.json";
import bab53 from "@/data/moreh-bab53.json";
import bab54 from "@/data/moreh-bab54.json";
import bab55 from "@/data/moreh-bab55.json";
import bab56 from "@/data/moreh-bab56.json";
import bab57 from "@/data/moreh-bab57.json";
import bab58 from "@/data/moreh-bab58.json";
import bab59 from "@/data/moreh-bab59.json";
import bab60 from "@/data/moreh-bab60.json";
import bab61 from "@/data/moreh-bab61.json";
import bab62 from "@/data/moreh-bab62.json";
import bab63 from "@/data/moreh-bab63.json";
import bab64 from "@/data/moreh-bab64.json";
import bab65 from "@/data/moreh-bab65.json";
import bab66 from "@/data/moreh-bab66.json";
import bab67 from "@/data/moreh-bab67.json";
import bab68 from "@/data/moreh-bab68.json";
import bab69 from "@/data/moreh-bab69.json";
import bab70 from "@/data/moreh-bab70.json";
import bab71 from "@/data/moreh-bab71.json";
import bab72 from "@/data/moreh-bab72.json";
import bab73 from "@/data/moreh-bab73.json";
import bab74 from "@/data/moreh-bab74.json";
import bab75 from "@/data/moreh-bab75.json";
import bab76 from "@/data/moreh-bab76.json";

/** A key-term card as authored inside each chapter's `terms[]`. */
export type RawTermCard = {
  id: string;
  ja: string;
  ar?: string | null;
  translit?: string;
  gloss: string;
  note?: string;
  variants?: string[];
};

/** A term card tagged with the chapter that introduces it. */
export type AtlasTerm = RawTermCard & {
  chapterN: number;
  /** Short chapter label, e.g. "I:21 · ʿAvar". */
  chapterTitle: string;
  /** Reader href for the chapter. */
  href: string;
};

// chapter number → its `terms[]` (file babN holds chapter N).
const BY_CHAPTER: Record<number, { terms?: RawTermCard[] }> = {
  1: bab1, 2: bab2, 3: bab3, 4: bab4, 5: bab5, 6: bab6, 7: bab7,
  8: bab8, 9: bab9, 10: bab10, 11: bab11, 12: bab12, 13: bab13, 14: bab14,
  15: bab15, 16: bab16, 17: bab17, 18: bab18, 19: bab19, 20: bab20, 21: bab21,
  22: bab22, 23: bab23, 24: bab24, 25: bab25, 26: bab26, 27: bab27, 28: bab28,
  29: bab29, 30: bab30, 31: bab31, 32: bab32, 33: bab33, 34: bab34, 35: bab35,
  36: bab36,
  37: bab37, 38: bab38, 39: bab39, 40: bab40, 41: bab41, 42: bab42, 43: bab43,
  44: bab44, 45: bab45, 46: bab46, 47: bab47, 48: bab48, 49: bab49, 50: bab50,
  51: bab51, 52: bab52, 53: bab53, 54: bab54, 55: bab55, 56: bab56, 57: bab57,
  58: bab58, 59: bab59, 60: bab60, 61: bab61, 62: bab62, 63: bab63, 64: bab64,
  65: bab65, 66: bab66, 67: bab67, 68: bab68, 69: bab69, 70: bab70, 71: bab71,
  72: bab72, 73: bab73, 74: bab74, 75: bab75, 76: bab76,
};

type AlignedSeg = { ja: string; en: string; isHeader?: boolean };
type ChapterFile = { section?: string; section_ja?: string; terms?: RawTermCard[]; pages?: { aligned?: AlignedSeg[] }[] };

/** A chapter's aligned ja/en segments (headers dropped) + its section labels. */
export function getMorehChapterText(n: number): {
  section: string;
  sectionJa: string;
  segments: { ja: string; en: string }[];
} | null {
  const file = BY_CHAPTER[n] as ChapterFile | undefined;
  if (!file) return null;
  const segments: { ja: string; en: string }[] = [];
  for (const pg of file.pages ?? []) {
    for (const s of pg.aligned ?? []) {
      if (s.isHeader) continue;
      segments.push({ ja: s.ja, en: s.en });
    }
  }
  return { section: file.section ?? `Part I, Chapter ${n}`, sectionJa: file.section_ja ?? "", segments };
}

/**
 * Every key-term card across Part I, in chapter order, each tagged with its
 * chapter. The spine of the Guide's lexicon of equivocal God-language.
 */
export function getAtlasTerms(): AtlasTerm[] {
  const out: AtlasTerm[] = [];
  for (const ch of MOREH_CHAPTERS) {
    const file = BY_CHAPTER[ch.n];
    const terms = (file?.terms ?? []) as RawTermCard[];
    for (const t of terms) {
      out.push({
        ...t,
        chapterN: ch.n,
        chapterTitle: ch.title,
        href: morehHref(ch.slug),
      });
    }
  }
  return out;
}
