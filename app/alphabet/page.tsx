import type { Metadata } from "next";
import Link from "next/link";
import data from "@/data/alphabet.json";
import { AlphabetUI, type AlphabetData } from "./alphabet";

export const metadata: Metadata = {
  title: "The Judeo-Arabic Alphabet for Hebrew Readers",
  description:
    "Five short lessons on how the Hebrew alphabet renders Arabic phonemes in medieval Judeo-Arabic — the diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, and the orthographic conventions used by Saadia, Bahya, and the Cairo Genizah scribes.",
  alternates: { canonical: "/alphabet" },
};

const stageOneNext = [
  {
    href: "/learn/cognates",
    title: "You Already Know This",
    blurb:
      "Modern Hebrew words that come straight from Arabic — from yallah and sababa to ראש, אם, and כלב.",
    sample: "יאללה · ראש · שמע · אחלה",
  },
  {
    href: "/learn/aramaic-cognates",
    title: "If You Know Onkelos…",
    blurb:
      "Forty Aramaic words that bridge straight to Arabic — including the interdentals (תלת, דהב, דכר) only Aramaic can teach.",
    sample: "תלת · דהב · ארעא · בית · חמרא",
  },
  {
    href: "/learn/first-50",
    title: "First 50 Words",
    blurb:
      "The fifty Judeo-Arabic words that show up most across Saadia's Tafsir — function words, common verbs, the cast of characters.",
    sample: "אללה · ארץ׳ · קאל · כ׳לק · מוסי",
  },
  {
    href: "/learn/saadia-story",
    title: "Who Was Saadia?",
    blurb:
      "A short walk through the 10th century and the choice one rabbi made that shaped how Arabic-speaking Jews would read Torah.",
    sample: "ca. 882 – 942 CE · Egypt → Baghdad",
  },
  {
    href: "/learn/saadia-preface",
    title: "Saadia's Own Preface",
    blurb:
      "Saadia's preface to the Tafsir — in Judeo-Arabic alongside English. Most of it being published in English for the first time.",
    sample: "תפסיר תורה · ca. 930 CE",
  },
];

export default function AlphabetPage() {
  return (
    <>
      <AlphabetUI data={data as AlphabetData} />

      {/* Stage 1 follow-on rail */}
      <section className="max-w-3xl mx-auto px-6 pb-20">
        <div className="border-t border-ink/10 pt-12">
          <p className="text-[10px] font-bold uppercase tracking-[0.3em] text-wine mb-3">
            Next in Stage 1
          </p>
          <h2 className="text-2xl tracking-tight text-ink">
            You&apos;ve got the script.{" "}
            <span className="text-wine italic">Now get the words.</span>
          </h2>
          <p className="mt-4 text-sm text-ink/70 leading-relaxed max-w-xl">
            Foundations isn&apos;t just letters. Before opening Saadia, browse
            the cognates you already know and the first fifty words you&apos;ll
            see most.
          </p>

          <ul className="mt-8 space-y-4">
            {stageOneNext.map((l) => (
              <li key={l.href}>
                <Link href={l.href} className="group block">
                  <div className="block rounded-md bg-page border border-ink/10 p-6 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5">
                    <div className="text-xl text-ink group-hover:text-wine transition-colors">
                      {l.title}
                    </div>
                    <p className="mt-2 text-sm text-ink/70 leading-relaxed">
                      {l.blurb}
                    </p>
                    <div
                      dir="rtl"
                      className="font-hebrew text-lg text-ink/80 mt-4 leading-loose"
                    >
                      {l.sample}
                    </div>
                  </div>
                </Link>
              </li>
            ))}
          </ul>

          <div className="mt-10 pt-6 border-t border-ink/10 text-sm text-ink/70 flex items-center justify-between flex-wrap gap-3">
            <span>Ready for Stage 2?</span>
            <Link
              href="/tafsir"
              className="text-wine hover:underline tracking-wide"
            >
              Open Saadia&apos;s Tafsir →
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
