import type { Metadata } from "next";
import data from "@/data/first-50-ja-words.json";
import { First50Cards, type FirstFiftyEntry } from "./cards";

type FirstFiftyData = {
  _total: number;
  entries: FirstFiftyEntry[];
};

export const metadata: Metadata = {
  title: "First 50 Judeo-Arabic Words — Frequency-ranked vocabulary from Saadia",
  description:
    "The fifty Judeo-Arabic words that show up most across Saadia Gaon's Tafsir on the Torah — function words, common verbs, the cast of characters. Each entry links straight into the verse where the word appears.",
  alternates: { canonical: "/learn/first-50" },
};

export default function First50Page() {
  const payload = data as FirstFiftyData;
  return <First50Cards entries={payload.entries} />;
}
