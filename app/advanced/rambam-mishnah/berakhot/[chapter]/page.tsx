import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { berakhot_ChapterBySlug, buildMishnahNav, BERAKHOT_CHAPTERS } from "../../chapters";

export function generateStaticParams() {
  return BERAKHOT_CHAPTERS.map((c) => ({ chapter: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  const ch = berakhot_ChapterBySlug[chapter];
  if (!ch) return {};
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Rambam's Commentary on Berakhot in Judeo-Arabic`,
      description: `Rambam's commentary on Tractate Berakhot in the original 12th-century Judeo-Arabic with English translation.`,
      alternates: { canonical: `/advanced/rambam-mishnah/berakhot/${chapter}` },
    };
  } catch {
    return {};
  }
}

export default async function BerakhotoChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const ch = berakhot_ChapterBySlug[chapter];
  if (!ch) notFound();

  let data: WorkData;
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    data = mod.default as unknown as WorkData;
  } catch {
    notFound();
  }

  return (
    <AdvancedReader
      data={data!}
      nav={buildMishnahNav("berakhot", chapter)}
    />
  );
}
