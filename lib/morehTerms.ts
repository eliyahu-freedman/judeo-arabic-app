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

/** A key-term card as authored inside each chapter's `terms[]`. */
export type RawTermCard = {
  id: string;
  ja: string;
  ar?: string;
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
