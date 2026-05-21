import type { Metadata } from "next";
import data from "@/data/alphabet.json";
import { AlphabetUI, type AlphabetData } from "./alphabet";

export const metadata: Metadata = {
  title: "The Judeo-Arabic Alphabet for Hebrew Readers",
  description:
    "Five short lessons on how the Hebrew alphabet renders Arabic phonemes in medieval Judeo-Arabic — the diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, and the orthographic conventions used by Saadia, Bahya, and the Cairo Genizah scribes.",
  alternates: { canonical: "/alphabet" },
};

export default function AlphabetPage() {
  return <AlphabetUI data={data as AlphabetData} />;
}
