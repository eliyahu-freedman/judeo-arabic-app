import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { MishnaReader, type MishnaChapterData } from "@/components/MishnaReader";

const CHAPTERS = [1];

export function generateStaticParams() {
  return CHAPTERS.map((ch) => ({ chapter: String(ch) }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  return {
    title: `Mishnah Yoma, Chapter ${chapter}`,
    description: `Mishnah Tractate Yoma, chapter ${chapter} — Hebrew text with English translation.`,
    alternates: { canonical: `/mishna/yoma/${chapter}` },
  };
}

export default async function MishnaYomaChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const chNum = Number(chapter);
  if (!CHAPTERS.includes(chNum)) notFound();

  const mod = await import(`@/data/mishna-yoma-${chNum}.json`);
  const data = mod.default as unknown as MishnaChapterData;

  const idx = CHAPTERS.indexOf(chNum);
  const prevChapter = idx > 0 ? CHAPTERS[idx - 1] : null;
  const nextChapter = idx < CHAPTERS.length - 1 ? CHAPTERS[idx + 1] : null;

  return (
    <MishnaReader
      data={data}
      prevChapter={prevChapter}
      nextChapter={nextChapter}
      tractateSlug="yoma"
    />
  );
}
