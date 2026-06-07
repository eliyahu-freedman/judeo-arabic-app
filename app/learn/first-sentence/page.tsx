import type { Metadata } from "next";
import {
  FirstSentenceDecoder,
  type FirstSentenceData,
} from "./decoder";
import { TrackVisit } from "@/components/TrackVisit";
import firstSentence from "@/data/first-sentence.json";

const data = firstSentence as FirstSentenceData;

export const metadata: Metadata = {
  title: "Read Your First Sentence — Saadia's Genesis 1:1, letter by letter",
  description:
    "The capstone of the Judeo-Arabic foundations: decode the opening line of Saadia's Tafsir (Genesis 1:1) one word and one letter at a time, putting the alphabet, the diacritics, the article, and the Saadianic conventions together — then step into the reader.",
  alternates: { canonical: "/learn/first-sentence" },
};

export default function FirstSentencePage() {
  return (
    <>
      <TrackVisit label={data.title} href="/learn/first-sentence" />
      <FirstSentenceDecoder data={data} />
    </>
  );
}
