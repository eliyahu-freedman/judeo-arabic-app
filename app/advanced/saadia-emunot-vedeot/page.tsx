import type { Metadata } from "next";
import data from "@/data/saadia-emunot-intro.json";
import { AdvancedReader, type WorkData } from "../reader";
import { buildEmunotNavIntro } from "./chapters";

export const metadata: Metadata = {
  title: "Emunot v'Deot — Saadia Gaon's Book of Beliefs and Opinions in Judeo-Arabic",
  description:
    "The opening of Saadia Gaon's Emunot v'Deot (Kitāb al-Amānāt wa'l-Iʿtiqādāt) — the first systematic Jewish theology (933 CE) — in its original Judeo-Arabic: why doubt befalls people in their inquiries and how knowledge dispels it. With a working English translation, phrase-by-phrase hover highlighting, tap-to-define glosses, and notes on key terms.",
  alternates: { canonical: "/advanced/saadia-emunot-vedeot" },
};

export default function SaadiaEmunotPage() {
  return <AdvancedReader data={data as unknown as WorkData} nav={buildEmunotNavIntro()} />;
}
