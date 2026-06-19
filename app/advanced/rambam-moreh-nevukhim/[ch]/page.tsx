import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { AdvancedReader, type WorkData } from "../../reader";
import { buildMorehNav } from "../chapters";
import { VersesCited } from "../VersesCited";
import tibbon from "@/data/moreh-tibbon.json";

const TIBBON = (tibbon as { chapters: Record<string, string[]> }).chapters;
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
import bab15 from "@/data/moreh-bab15.json";
import bab16 from "@/data/moreh-bab16.json";
import bab17 from "@/data/moreh-bab17.json";
import bab18 from "@/data/moreh-bab18.json";
import bab19 from "@/data/moreh-bab19.json";
import bab20 from "@/data/moreh-bab20.json";
import bab21 from "@/data/moreh-bab21.json";
import bab22 from "@/data/moreh-bab22.json";
import bab23 from "@/data/moreh-bab23.json";
import bab24 from "@/data/moreh-bab24.json";
import bab25 from "@/data/moreh-bab25.json";
import bab26 from "@/data/moreh-bab26.json";
import bab27 from "@/data/moreh-bab27.json";
import bab28 from "@/data/moreh-bab28.json";
import bab29 from "@/data/moreh-bab29.json";
import bab30 from "@/data/moreh-bab30.json";
import bab31 from "@/data/moreh-bab31.json";
import bab32 from "@/data/moreh-bab32.json";
import bab33 from "@/data/moreh-bab33.json";
import bab34 from "@/data/moreh-bab34.json";
import bab35 from "@/data/moreh-bab35.json";
import bab36 from "@/data/moreh-bab36.json";

// Chapter I:1 keeps the bare canonical route (../page.tsx); chapters I:2–I:36
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
  "15": bab15 as unknown as WorkData,
  "16": bab16 as unknown as WorkData,
  "17": bab17 as unknown as WorkData,
  "18": bab18 as unknown as WorkData,
  "19": bab19 as unknown as WorkData,
  "20": bab20 as unknown as WorkData,
  "21": bab21 as unknown as WorkData,
  "22": bab22 as unknown as WorkData,
  "23": bab23 as unknown as WorkData,
  "24": bab24 as unknown as WorkData,
  "25": bab25 as unknown as WorkData,
  "26": bab26 as unknown as WorkData,
  "27": bab27 as unknown as WorkData,
  "28": bab28 as unknown as WorkData,
  "29": bab29 as unknown as WorkData,
  "30": bab30 as unknown as WorkData,
  "31": bab31 as unknown as WorkData,
  "32": bab32 as unknown as WorkData,
  "33": bab33 as unknown as WorkData,
  "34": bab34 as unknown as WorkData,
  "35": bab35 as unknown as WorkData,
  "36": bab36 as unknown as WorkData,
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
  return (
    <>
      <AdvancedReader
        data={workData}
        nav={buildMorehNav(Number(ch))}
        tibbon={TIBBON[ch]}
      />
      <VersesCited n={Number(ch)} />
    </>
  );
}
