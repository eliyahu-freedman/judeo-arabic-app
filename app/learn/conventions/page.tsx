import type { Metadata } from "next";
import { GrammarLesson, type GrammarData } from "../grammar/lesson";
import { TrackVisit } from "@/components/TrackVisit";
import conventions from "@/data/conventions.json";

const data = conventions as GrammarData;

export const metadata: Metadata = {
  title: "Ambiguities & Saadianic Conventions — reading real Judeo-Arabic",
  description:
    "Why one Hebrew letter can stand for two Arabic sounds in Judeo-Arabic: dropped diacritics, the competing ways of writing خ and غ, and Saadia's classical spelling habits (alif maqṣūra, tāʾ marbūṭa, plene ā) — with a reading strategy for resolving the ambiguity.",
  alternates: { canonical: "/learn/conventions" },
};

export default function ConventionsPage() {
  return (
    <>
      <TrackVisit label={data.title} href="/learn/conventions" />
      <GrammarLesson
        data={data}
        backHref="/foundations"
        backLabel="Foundations"
        eyebrowSuffix="lesson 4"
      />
    </>
  );
}
