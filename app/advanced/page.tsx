import jaData from "@/data/bahya-hakdamah.json";
import heData from "@/data/bahya-hakdamah-hebrew.json";
import { BahyaReader, type BahyaData, type BahyaPage } from "./reader";

export default function AdvancedPage() {
  const hebrewParas = heData.paragraphs;
  const nJa = jaData.pages.length;
  const nHe = hebrewParas.length;

  // Linear-interpolation alignment. Paragraph boundaries don't match
  // 1:1 between editions; this gets learners "approximately the right"
  // Hebrew beside each JA page, and the UI labels it as approximate.
  const pages: BahyaPage[] = jaData.pages.map((p, i) => {
    const start = Math.floor((nHe * i) / nJa);
    const end = Math.floor((nHe * (i + 1)) / nJa);
    return {
      page_he: p.page_he,
      paragraphs: p.paragraphs,
      hebrew_paragraphs: hebrewParas.slice(start, end),
    };
  });

  const data: BahyaData = {
    work: jaData.work,
    section: jaData.section,
    author: jaData.author,
    hebrew_translator: heData.translator,
    pages,
  };
  return <BahyaReader data={data} />;
}
