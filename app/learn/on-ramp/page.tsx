import type { Metadata } from "next";
import data from "@/data/on-ramp.json";
import { OnRamp, type OnRampData } from "./onramp";
import { TrackVisit } from "@/components/TrackVisit";

export const metadata: Metadata = {
  title: "Read Your First Verses — a Judeo-Arabic reading on-ramp",
  description:
    "Read the opening of Genesis in Saadia's own Judeo-Arabic, one clause at a time, word by word — the bridge from the alphabet and first words into the full Tafsir reader.",
  alternates: { canonical: "/learn/on-ramp" },
};

export default function OnRampPage() {
  return (
    <>
      <TrackVisit label="Read Your First Verses" href="/learn/on-ramp" />
      <OnRamp data={data as OnRampData} />
    </>
  );
}
