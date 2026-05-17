import jaData from "@/data/bahya-bab1.json";
import heData from "@/data/bahya-bab1-hebrew.json";
import enData from "@/data/bahya-bab1-english.json";
import { BahyaReader, type BahyaData, type BahyaPage } from "./reader";

export default function AdvancedPage() {
  const hePar = heData.paragraphs;
  const enPar = enData.paragraphs;
  const nJa = jaData.pages.length;
  const nHe = hePar.length;
  const nEn = enPar.length;

  // Linear-interpolation alignment for both Hebrew and English. Source
  // editions divide paragraphs differently so granularity differs from
  // the JA page structure; the UI labels the alignment as approximate.
  const pages: BahyaPage[] = jaData.pages.map((p, i) => {
    const heStart = Math.floor((nHe * i) / nJa);
    const heEnd = Math.floor((nHe * (i + 1)) / nJa);
    const enStart = Math.floor((nEn * i) / nJa);
    const enEnd = Math.floor((nEn * (i + 1)) / nJa);
    return {
      page_he: p.page_he,
      paragraphs: p.paragraphs,
      hebrew_paragraphs: hePar.slice(heStart, heEnd),
      english_paragraphs: enPar.slice(enStart, enEnd),
    };
  });

  const data: BahyaData = {
    work: jaData.work,
    section: jaData.section,
    subtitle: jaData.subtitle,
    author: jaData.author,
    hebrew_translator: heData.translator,
    english_translator: enData.translator,
    pages,
  };
  return <BahyaReader data={data} />;
}
