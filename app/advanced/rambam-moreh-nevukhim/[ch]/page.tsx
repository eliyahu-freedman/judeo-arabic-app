import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../reader";
import { buildMorehNav } from "../chapters";
import bab2 from "@/data/moreh-bab2.json";
import bab3 from "@/data/moreh-bab3.json";
import bab4 from "@/data/moreh-bab4.json";
import bab5 from "@/data/moreh-bab5.json";
import bab6 from "@/data/moreh-bab6.json";
import bab7 from "@/data/moreh-bab7.json";
import bab8 from "@/data/moreh-bab8.json";
import bab9 from "@/data/moreh-bab9.json";
import bab10 from "@/data/moreh-bab10.json";
import bab11 from "@/data/moreh-bab11.json";
import bab12 from "@/data/moreh-bab12.json";
import bab13 from "@/data/moreh-bab13.json";
import bab14 from "@/data/moreh-bab14.json";

// Chapter I:1 keeps the bare canonical route (../page.tsx); chapters I:2–I:14
// are served here by the dynamic [ch] segment, keyed by chapter number.
const DATA: Record<string, WorkData> = {
  "2": bab2 as unknown as WorkData,
  "3": bab3 as unknown as WorkData,
  "4": bab4 as unknown as WorkData,
  "5": bab5 as unknown as WorkData,
  "6": bab6 as unknown as WorkData,
  "7": bab7 as unknown as WorkData,
  "8": bab8 as unknown as WorkData,
  "9": bab9 as unknown as WorkData,
  "10": bab10 as unknown as WorkData,
  "11": bab11 as unknown as WorkData,
  "12": bab12 as unknown as WorkData,
  "13": bab13 as unknown as WorkData,
  "14": bab14 as unknown as WorkData,
};

export function generateStaticParams() {
  return Object.keys(DATA).map((ch) => ({ ch }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ ch: string }>;
}): Promise<Metadata> {
  const { ch } = await params;
  const data = DATA[ch];
  if (!data) return {};
  return {
    title: `${data.section} — Moreh Nevukhim in Judeo-Arabic`,
    description: data.intro,
    alternates: { canonical: `/advanced/rambam-moreh-nevukhim/${ch}` },
  };
}

export default async function RambamMorehChapterPage({
  params,
}: {
  params: Promise<{ ch: string }>;
}) {
  const { ch } = await params;
  const data = DATA[ch];
  if (!data) notFound();
  // workId loads the per-work Blau overlay (data/blau-notes-moreh.json).
  const workData = { ...data, workId: "moreh" };
  return <AdvancedReader data={workData} nav={buildMorehNav(Number(ch))} />;
}
