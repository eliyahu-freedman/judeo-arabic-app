import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../reader";
import { buildMorehNav } from "../chapters";
import { VersesCited } from "../VersesCited";

// Chapters 2–76 (chapter 1 is served by ../page.tsx)
const CHAPTERS = Array.from({ length: 75 }, (_, i) => String(i + 2));

export function generateStaticParams() {
  return CHAPTERS.map((ch) => ({ ch }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ ch: string }>;
}): Promise<Metadata> {
  const { ch } = await params;
  if (!CHAPTERS.includes(ch)) return {};
  try {
    const mod = await import(`@/data/moreh-bab${ch}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Moreh Nevukhim in Judeo-Arabic`,
      description: data.intro,
      alternates: { canonical: `/advanced/rambam-moreh-nevukhim/${ch}` },
    };
  } catch {
    return {};
  }
}

export default async function RambamMorehChapterPage({
  params,
}: {
  params: Promise<{ ch: string }>;
}) {
  const { ch } = await params;
  if (!CHAPTERS.includes(ch)) notFound();

  let data: WorkData;
  let tibbonChapter: string[] | undefined;
  try {
    const [mod, tibbonMod] = await Promise.all([
      import(`@/data/moreh-bab${ch}.json`),
      import(`@/data/moreh-tibbon.json`),
    ]);
    data = mod.default as unknown as WorkData;
    const tibbon = tibbonMod.default as { chapters: Record<string, string[]> };
    tibbonChapter = tibbon.chapters[ch];
  } catch {
    notFound();
  }

  const workData = { ...data!, workId: "moreh" };
  return (
    <>
      <AdvancedReader
        data={workData}
        nav={buildMorehNav(Number(ch))}
        tibbon={tibbonChapter}
      />
      <VersesCited n={Number(ch)} />
    </>
  );
}
