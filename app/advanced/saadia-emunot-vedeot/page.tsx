import type { Metadata } from "next";
import { ComingSoon } from "../_coming-soon";

export const metadata: Metadata = {
  title: "Emunot v'Deot — coming soon",
  description:
    "Saadia Gaon's Book of Beliefs and Opinions in its 10th-century Judeo-Arabic original. Coming soon to the Judeo-Arabic library.",
  alternates: { canonical: "/advanced/saadia-emunot-vedeot" },
};

export default function SaadiaEmunotPage() {
  return (
    <ComingSoon
      author="Saadia Gaon (882–942)"
      work="Kitāb al-Amānāt — Emunot v'Deot"
      oneLiner="The Book of Beliefs and Opinions, Saadia's 10th-century systematic theology — the work that gave Geonic Judaism its philosophical vocabulary."
      sample="כתאב אלאמאנאת ואלאעתקאדאת"
    />
  );
}
