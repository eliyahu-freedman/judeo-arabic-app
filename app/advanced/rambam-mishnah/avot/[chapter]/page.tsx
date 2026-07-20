import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { avotChapterBySlug, buildMishnahNav, AVOT_CHAPTERS } from "../../chapters";

export function generateStaticParams() {
  return AVOT_CHAPTERS.map((c) => ({ chapter: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  const ch = avotChapterBySlug[chapter];
  if (!ch) return {};
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Rambam Mishnah Commentary in Judeo-Arabic`,
      description: `Rambam's commentary on ${data.section} of Pirke Avot, in the original 12th-century Judeo-Arabic with English translation.`,
      alternates: { canonical: `/advanced/rambam-mishnah/avot/${chapter}` },
    };
  } catch {
    return {};
  }
}

export default async function AvotChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const ch = avotChapterBySlug[chapter];
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
      nav={buildMishnahNav("avot", chapter)}
    />
  );
}
