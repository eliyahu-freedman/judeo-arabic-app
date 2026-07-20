import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { zeraim_introChapterBySlug, buildMishnahNav, ZERAIM_INTRO_CHAPTERS } from "../../chapters";

export function generateStaticParams() {
  return ZERAIM_INTRO_CHAPTERS.map((c) => ({ chapter: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ chapter: string }>;
}): Promise<Metadata> {
  const { chapter } = await params;
  const ch = zeraim_introChapterBySlug[chapter];
  if (!ch) return {};
  try {
    const mod = await import(`@/data/${ch.dataKey}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Rambam's Introduction to the Mishnah in Judeo-Arabic`,
      description: `Rambam's Introduction to the Mishnah Commentary in the original 12th-century Judeo-Arabic with English translation.`,
      alternates: { canonical: `/advanced/rambam-mishnah/zeraim-intro/${chapter}` },
    };
  } catch {
    return {};
  }
}

export default async function ZeraimIntroChapterPage({
  params,
}: {
  params: Promise<{ chapter: string }>;
}) {
  const { chapter } = await params;
  const ch = zeraim_introChapterBySlug[chapter];
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
      nav={buildMishnahNav("zeraim-intro", chapter)}
    />
  );
}
