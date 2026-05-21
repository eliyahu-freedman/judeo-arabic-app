import type { Metadata } from "next";
import data from "@/data/cognates.json";
import { CognateCards, type CognateEntry } from "./cards";

type CognateData = {
  _total: number;
  entries: CognateEntry[];
};

export const metadata: Metadata = {
  title: "Hebrew–Arabic Cognates You Already Know",
  description:
    "Modern Hebrew words you already use that come straight from Arabic — and how Saadia used them a thousand years ago. From yallah and sababa to ראש, אם, and כלב, the lexical bridge between Hebrew and Arabic in Saadia's Tafsir.",
  alternates: { canonical: "/learn/cognates" },
};

export default function CognatesPage() {
  const payload = data as CognateData;
  return <CognateCards entries={payload.entries} />;
}
