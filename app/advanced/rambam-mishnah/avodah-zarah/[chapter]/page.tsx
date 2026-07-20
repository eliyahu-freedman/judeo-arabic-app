import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { avodahZarah_ChapterBySlug, buildMishnahNav, AVODAH_ZARAH_CHAPTERS } from "../../chapters";
import type { TractateXrefs } from "@/lib/mishnahXrefs";
import azXrefs from "@/data/xrefs/rambam-mishnah-avodah-zarah.json";

export function generateStaticParams() {
  return AVODAH_ZARAH_CHAPTERS.map((c) => ({ chapter: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  const ch = avodahZarah_ChapterBySlug[chapter];
  if (!ch) return {};
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Rambam's Commentary on Avodah Zarah in Judeo-Arabic`,
      description: `Rambam's commentary on Tractate Avodah Zarah in the original 12th-century Judeo-Arabic with English translation.`,
      alternates: { canonical: `/advanced/rambam-mishnah/avodah-zarah/${chapter}` },
    };
  } catch {
    return {};
  }
}

export default async function AvodahZarahChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const ch = avodahZarah_ChapterBySlug[chapter];
  if (!ch) notFound();

  let data: WorkData;
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    data = mod.default as unknown as WorkData;
  } catch {
    notFound();
  }

  const chapterXrefs = (azXrefs as TractateXrefs).chapters[chapter] ?? {};

  return (
    <AdvancedReader
      data={data!}
      nav={buildMishnahNav("avodah-zarah", chapter)}
      xrefs={chapterXrefs}
    />
  );
}
