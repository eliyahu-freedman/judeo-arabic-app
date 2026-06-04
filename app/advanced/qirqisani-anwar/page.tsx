import type { Metadata } from "next";
import data from "@/data/qirqisani-anwar-maqala1.json";
import { AdvancedReader, type WorkData } from "../reader";

export const metadata: Metadata = {
  title: "Qirqisani, Kitāb al-Anwār — Discourse I opening",
  description:
    "The opening of Yaʿqūb al-Qirqisānī's 10th-century Karaite summa Kitāb al-Anwār wa'l-Marāqib (ed. Nemoy) in its original Arabic: the baḥth-wa-naẓar manifesto — religious obligations must be reached by inquiry and rational speculation, and the truth accepted from whoever holds it. With a working English translation, phrase-by-phrase hover highlighting, and notes on key terms.",
  alternates: { canonical: "/advanced/qirqisani-anwar" },
};

export default function QirqisaniPage() {
  // workId loads the per-work Blau overlay (data/blau-notes-qirqisani.json) —
  // Qirqisani is the work Blau cites most, so its special JA senses are richest.
  const workData = { ...(data as unknown as WorkData), workId: "qirqisani" };
  return <AdvancedReader data={workData} />;
}
