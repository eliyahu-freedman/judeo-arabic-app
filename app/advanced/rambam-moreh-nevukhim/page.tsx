import type { Metadata } from "next";
import data from "@/data/moreh-bab1.json";
import { AdvancedReader, type WorkData } from "../reader";

export const metadata: Metadata = {
  title: "Moreh Nevukhim — Guide of the Perplexed I:1 in Judeo-Arabic",
  description:
    "The opening chapter of Maimonides' Guide of the Perplexed (Dalālat al-Ḥā'irīn) in its original 12th-century Judeo-Arabic: why 'image and likeness' (tzelem u-demut) do not mean God has a body. With a working English translation, phrase-by-phrase hover highlighting, tap-to-define glosses, and notes on key terms.",
  alternates: { canonical: "/advanced/rambam-moreh-nevukhim" },
};

export default function RambamMorehPage() {
  return <AdvancedReader data={data as unknown as WorkData} />;
}
