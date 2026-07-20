import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { sanhedrinChapterBySlug, buildMishnahNav, SANHEDRIN_CHAPTERS } from "../../chapters";

export function generateStaticParams() {
  return SANHEDRIN_CHAPTERS.map((c) => ({ chapter: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  const ch = sanhedrinChapterBySlug[chapter];
  if (!ch) return {};
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Rambam on Sanhedrin in Judeo-Arabic`,
      description: `Rambam's commentary on ${data.section} of tractate Sanhedrin, in the original 12th-century Judeo-Arabic with English translation.`,
      alternates: { canonical: `/advanced/rambam-mishnah/sanhedrin/${chapter}` },
    };
  } catch {
    return {};
  }
}

export default async function SanhedrinChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const ch = sanhedrinChapterBySlug[chapter];
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
      nav={buildMishnahNav("sanhedrin", chapter)}
    />
  );
}
