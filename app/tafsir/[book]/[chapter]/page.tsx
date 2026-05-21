import { notFound } from "next/navigation";
import {
  findChapter,
  listChapters,
  readChapter,
  readChapterEnglish,
} from "@/lib/tafsirIndex";
import { TafsirReader, type TafsirData, type Verse } from "../../reader";

export async function generateStaticParams() {
  const all = await listChapters();
  return all.map((r) => ({
    book: r.bookSlug,
    chapter: String(r.chapter),
  }));
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

  return (
    <TafsirReader
      data={merged}
      prev={found.prev}
      next={found.next}
    />
  );
}
