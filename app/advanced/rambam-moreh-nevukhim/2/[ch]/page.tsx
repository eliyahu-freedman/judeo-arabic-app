import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../../reader";
import { buildMorehNavII } from "../../chapters";
import { VersesCited } from "../../VersesCited";

const CHAPTERS = Array.from({ length: 48 }, (_, i) => String(i + 1));

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
    const mod = await import(`@/data/moreh-p2-bab${ch}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Moreh Nevukhim in Judeo-Arabic`,
      description: data.intro,
      alternates: { canonical: `/advanced/rambam-moreh-nevukhim/2/${ch}` },
    };
  } catch {
    return {};
  }
}

export default async function RambamMorehIIChapterPage({
  params,
}: {
  params: Promise<{ ch: string }>;
}) {
  const { ch } = await params;
  if (!CHAPTERS.includes(ch)) notFound();

  let data: WorkData;
  try {
    const mod = await import(`@/data/moreh-p2-bab${ch}.json`);
    data = mod.default as unknown as WorkData;
  } catch {
    notFound();
  }

  const workData = { ...data!, workId: "moreh" };
  return (
    <>
      <AdvancedReader data={workData} nav={buildMorehNavII(Number(ch))} />
      <VersesCited n={Number(ch)} />
    </>
  );
}
