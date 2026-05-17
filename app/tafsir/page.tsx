import data from "@/data/tafsir-bereshit-1.json";
import english from "@/data/tafsir-bereshit-1-english.json";
import { TafsirReader, type TafsirData, type Verse } from "./reader";

export default function TafsirPage() {
  const enMap = english.translations as Record<string, string>;
  const merged: TafsirData = {
    book: data.book,
    chapter: data.chapter,
    verses: data.verses.map<Verse>((v) => ({
      ch: v.ch,
      v: v.v,
      hebrew: v.hebrew,
      ja: v.ja,
      arabic: v.arabic,
      hebrew_translation: v.hebrew_translation,
      english: enMap[String(v.v)] ?? "",
    })),
  };
  return <TafsirReader data={merged} />;
}
