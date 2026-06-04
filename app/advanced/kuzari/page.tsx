import type { Metadata } from "next";
import data from "@/data/kuzari-maqala1.json";
import { AdvancedReader, type WorkData } from "../reader";

export const metadata: Metadata = {
  title: "The Kuzari — Treatise I opening in Judeo-Arabic",
  description:
    "The opening of Judah Halevi's Kuzari (Kitāb al-radd wa-l-dalīl fī l-dīn al-dhalīl) in its original Judeo-Arabic: the Khazar king's dream and the Aristotelian philosopher's answer, with a working English translation, phrase-by-phrase hover highlighting, tap-to-define glosses, and notes on key philosophical terms.",
  alternates: { canonical: "/advanced/kuzari" },
};

export default function KuzariPage() {
  return <AdvancedReader data={data as unknown as WorkData} />;
}
