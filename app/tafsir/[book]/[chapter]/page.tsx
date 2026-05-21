import type { Metadata } from "next";
import { notFound } from "next/navigation";
import {
  findChapter,
  listChapters,
  readChapter,
  readChapterEnglish,
} from "@/lib/tafsirIndex";
import {
  BOOK_ORDER,
  PARSHA_SCHEDULE,
  parseRange,
  parshaSlug,
  type ParshaEntry,
} from "@/lib/parsha";
import {
  TafsirReader,
  type ChapterIndexEntry,
  type ParshaNavEntry,
  type TafsirData,
  type Verse,
} from "../../reader";

export async function generateStaticParams() {
  const all = await listChapters();
  return all.map((r) => ({
    book: r.bookSlug,
    chapter: String(r.chapter),
  }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ book: string; chapter: string }>;
}): Promise<Metadata> {
  const { book, chapter: chapterStr } = await params;
  const chapter = Number(chapterStr);
  const found = await findChapter(book, chapter);
  if (!found) return {};

  const display = found.record.book;
  const parsha = findParshaForChapter(book, chapter);
  const parshaSuffix = parsha ? ` (Parashat ${parsha.title})` : "";

  const title = `Saadia's Tafsir on ${display} ${chapter}${parshaSuffix}`;
  const description = `Saadia Gaon's medieval Judeo-Arabic translation of ${display} ${chapter}, verse by verse alongside the biblical Hebrew, with classical Hebrew (Ibn Tibbon-style) and English translations and a tap-to-define dictionary.`;
  const path = `/tafsir/${book}/${chapter}`;

  return {
    title,
    description,
    alternates: { canonical: path },
    openGraph: { title, description, url: path, type: "article" },
    twitter: { card: "summary_large_image", title, description },
  };
}

function findParshaForChapter(
  bookSlug: string,
  chapter: number,
): ParshaEntry | null {
  for (const p of PARSHA_SCHEDULE) {
    for (const a of p.aliyot) {
      const r = parseRange(a);
      if (!r) continue;
      if (r.start.book !== bookSlug) continue;
      if (chapter >= r.start.ch && chapter <= r.end.ch) return p;
    }
  }
  return null;
}

export default async function TafsirChapterPage({
  params,
}: {
  params: Promise<{ book: string; chapter: string }>;
}) {
  const { book, chapter: chapterStr } = await params;
  const chapter = Number(chapterStr);
  if (!Number.isInteger(chapter)) notFound();

  const found = await findChapter(book, chapter);
  if (!found) notFound();

  const [data, enMap] = await Promise.all([
    readChapter(book, chapter),
    readChapterEnglish(book, chapter),
  ]);

  const merged: TafsirData = {
    book: data.book,
    chapter: data.chapter,
    verses: data.verses.map<Verse>((v) => ({
      ch: v.ch,
      v: v.v,
      hebrew: v.hebrew,
      ja: v.ja,
      arabic: v.arabic,
      hebrew_translation: v.hebrew_translation,
      english: enMap[String(v.v)] ?? "",
    })),
  };

  const allChapters = await listChapters();
  const chapterIndex: ChapterIndexEntry[] = allChapters.map((r) => ({
    bookSlug: r.bookSlug,
    chapter: r.chapter,
  }));

  const seen = new Set<string>();
  const parshaList: ParshaNavEntry[] = [];
  for (const p of PARSHA_SCHEDULE as ParshaEntry[]) {
    const slug = parshaSlug(p.title);
    if (seen.has(slug)) continue;
    seen.add(slug);
    parshaList.push({
      slug,
      title: p.title,
      hebrew: p.hebrew,
      aliyot: p.aliyot,
    });
  }
  parshaList.sort((a, b) => {
    const ra = parseRange(a.aliyot[0]);
    const rb = parseRange(b.aliyot[0]);
    if (!ra || !rb) return 0;
    const ai = BOOK_ORDER.indexOf(ra.start.book);
    const bi = BOOK_ORDER.indexOf(rb.start.book);
    if (ai !== bi) return ai - bi;
    if (ra.start.ch !== rb.start.ch) return ra.start.ch - rb.start.ch;
    return ra.start.v - rb.start.v;
  });

  return (
    <TafsirReader
      data={merged}
      prev={found.prev}
      next={found.next}
      bookSlug={found.record.bookSlug}
      chapterIndex={chapterIndex}
      parshaList={parshaList}
    />
  );
}
