import type { Metadata } from "next";
import { ComingSoon } from "../_coming-soon";

export const metadata: Metadata = {
  title: "Moreh Nevukhim — coming soon",
  description:
    "Maimonides' Guide of the Perplexed in its 12th-century Judeo-Arabic original, with Hebrew and English alongside. Coming soon to the Judeo-Arabic library.",
  alternates: { canonical: "/advanced/rambam-moreh-nevukhim" },
};

export default function RambamMorehPage() {
  return (
    <ComingSoon
      author="Moses Maimonides (1138–1204)"
      work="Dalālat al-Ḥā'irīn — Moreh Nevukhim"
      oneLiner="Rambam's Guide of the Perplexed in its 12th-century Judeo-Arabic original, with Ibn Tibbon's Hebrew and a modern English alongside."
      sample="דלאלה אלחאירין"
    />
  );
}
