import type { Metadata } from "next";
import data from "@/data/moreh-bab1.json";
import { AdvancedReader, type WorkData } from "../reader";
import { buildMorehNav } from "./chapters";
import { VersesCited } from "./VersesCited";
import { loadPortuguese, mergePortuguese } from "@/lib/morehPortuguese";
import tibbon from "@/data/moreh-tibbon.json";

const TIBBON = (tibbon as { chapters: Record<string, string[]> }).chapters;

export const metadata: Metadata = {
  title: "Moreh Nevukhim — Guide of the Perplexed I:1 in Judeo-Arabic",
  description:
    "The opening chapter of Maimonides' Guide of the Perplexed (Dalālat al-Ḥā'irīn) in its original 12th-century Judeo-Arabic: why 'image and likeness' (tzelem u-demut) do not mean God has a body. With a working English translation, phrase-by-phrase hover highlighting, tap-to-define glosses, and notes on key terms.",
  alternates: { canonical: "/advanced/rambam-moreh-nevukhim" },
};

export default async function RambamMorehPage() {
  // workId loads the per-work Blau overlay (data/blau-notes-moreh.json) — a
  // special JA sense shown here never leaks into the other Advanced readers.
  const pt = await loadPortuguese("moreh-bab1");
  const workData = mergePortuguese(
    { ...(data as unknown as WorkData), workId: "moreh" },
    pt,
  );
  return (
    <>
      <AdvancedReader data={workData} nav={buildMorehNav(1)} tibbon={TIBBON["1"]} />
      <VersesCited n={1} />
    </>
  );
}
