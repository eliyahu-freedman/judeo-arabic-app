import type { Metadata } from "next";
import data from "@/data/aramaic-cognates.json";
import { AramaicCognateCards, type AramaicCognateEntry } from "./cards";
import { TrackVisit } from "@/components/TrackVisit";

type AramaicCognateData = {
  _total: number;
  entries: AramaicCognateEntry[];
};

export const metadata: Metadata = {
  title: "Aramaic–Arabic Cognates — If You Know Onkelos…",
  description:
    "Forty Aramaic words from Targum Onkelos that bridge straight into Arabic — including the interdental words (תלת, דהב, דכר) where Hebrew shifted its consonants but Aramaic and Arabic still agree. Most appear in this week's parashah.",
  alternates: { canonical: "/learn/aramaic-cognates" },
};

export default function AramaicCognatesPage() {
  const payload = data as AramaicCognateData;
  return (
    <>
      <TrackVisit
        label="If You Know Onkelos…"
        href="/learn/aramaic-cognates"
        completeId="aramaic-cognates"
      />
      <AramaicCognateCards entries={payload.entries} />
    </>
  );
}
