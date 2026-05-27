import type { Metadata } from "next";
import jaData from "@/data/bahya-bab1.json";
import enData from "@/data/bahya-bab1-english.json";
import alignedData from "@/data/bahya-bab1-aligned.json";
import {
  AdvancedReader,
  type AlignedSegment,
  type WorkData,
  type WorkPage,
} from "../reader";

export const metadata: Metadata = {
  title: "Bahya ibn Paquda's Chovot HaLevavot — The First Gate in Judeo-Arabic",
  description:
    "Read the opening gate of Bahya ibn Paquda's Chovot HaLevavot (Duties of the Heart) in its original 11th-century Judeo-Arabic, alongside a working English translation. Hover a phrase to see its English light up; tap any word for a gloss.",
  alternates: { canonical: "/advanced/bahya" },
};

export default function BahyaPage() {
  const enPar = enData.paragraphs;
  const nJa = jaData.pages.length;
  const nEn = enPar.length;

  const alignedByPage = alignedData.pages as Record<string, AlignedSegment[]>;
  const pages: WorkPage[] = jaData.pages.map((p, i) => {
    const enStart = Math.floor((nEn * i) / nJa);
    const enEnd = Math.floor((nEn * (i + 1)) / nJa);
    return {
      page_he: p.page_he,
      paragraphs: p.paragraphs,
      english_paragraphs: enPar.slice(enStart, enEnd),
      aligned: alignedByPage[p.page_he],
    };
  });

  const data: WorkData = {
    work: jaData.work,
    section: jaData.section,
    subtitle: jaData.subtitle,
    author: jaData.author,
    english_translator: enData.translator,
    pages,
  };
  return <AdvancedReader data={data} />;
}
