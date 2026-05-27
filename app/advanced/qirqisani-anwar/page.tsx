import type { Metadata } from "next";
import { ComingSoon } from "../_coming-soon";

export const metadata: Metadata = {
  title: "Qirqisani, Kitāb al-Anwār — coming soon",
  description:
    "Yaʿqūb al-Qirqisānī's 10th-century Karaite Kitāb al-Anwār wa'l-Marāqib in Judeo-Arabic. Coming soon to the Judeo-Arabic library.",
  alternates: { canonical: "/advanced/qirqisani-anwar" },
};

export default function QirqisaniPage() {
  return (
    <ComingSoon
      author="Yaʿqūb al-Qirqisānī (10th c.)"
      work="Kitāb al-Anwār wa'l-Marāqib"
      oneLiner="The 10th-century Karaite encyclopedia of religious thought, law, and sect-history — a window onto a Judaism that argued in Arabic with Christians, Muslims, and other Jews."
      sample="כתאב אלאנואר ואלמראקב"
    />
  );
}
