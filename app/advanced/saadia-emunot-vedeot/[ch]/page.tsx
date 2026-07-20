import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../reader";
import { buildEmunotNav, EMUNOT_CHAPTERS } from "../chapters";

export function generateStaticParams() {
  return EMUNOT_CHAPTERS.map((c) => ({ ch: c.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ ch: string }>;
}): Promise<Metadata> {
  const { ch } = await params;
  try {
    const mod = await import(`@/data/saadia-emunot-${ch}.json`);
    const data = mod.default as unknown as WorkData;
    return {
      title: `${data.section} — Emunot v'Deot in Judeo-Arabic`,
      description: `${data.section} from Saadia Gaon's Emunot v'Deot (Kitāb al-Amānāt wal-Iʿtiqādāt) in the original Judeo-Arabic, with a working English translation.`,
      alternates: { canonical: `/advanced/saadia-emunot-vedeot/${ch}` },
    };
  } catch {
    return {};
  }
}

export default async function EmunotChapterPage({
  params,
}: {
  params: Promise<{ ch: string }>;
}) {
  const { ch } = await params;
  let data: WorkData;
  try {
    const mod = await import(`@/data/saadia-emunot-${ch}.json`);
    data = mod.default as unknown as WorkData;
  } catch {
    notFound();
  }
  return <AdvancedReader data={data!} nav={buildEmunotNav(ch)} />;
}
