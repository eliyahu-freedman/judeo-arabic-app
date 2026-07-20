import type { Metadata } from "next";
import Link from "next/link";
import { GuidedPath } from "@/components/GuidedPath";

export const metadata: Metadata = {
  title: "Learn Judeo-Arabic — Short lessons and vocabulary",
  description:
    "Bite-sized ways into Judeo-Arabic: the first 50 words from Saadia's Tafsir ranked by frequency, Hebrew–Arabic cognates you already know, Aramaic bridges from Onkelos, the story of Saadia Gaon, and Saadia's own preface in Judeo-Arabic and English.",
  alternates: { canonical: "/learn" },
};

const lessons = [
  {
    href: "/learn/first-50",
    status: "Live",
    title: "First 50 Words",
    body: "The fifty Judeo-Arabic words that show up most across Saadia's Tafsir — function words, common verbs, the cast of characters. Each card links straight into the Tafsir for a real example.",
    sample: "אללה · ארץ' · קאל · כ'לק · מוסי",
  },
  {
    href: "/learn/cognates",
    status: "Live",
    title: "You Already Know This",
    body: "Modern Hebrew words you already use that come straight from Arabic — and how Saadia used them a thousand years ago. From yallah and sababa to ראש, אם, and כלב.",
    sample: "יאללה · ראש · שמע · אחלה",
  },
  {
    href: "/learn/aramaic-cognates",
    status: "Live",
    title: "If You Know Onkelos…",
    body: "Forty Aramaic words that bridge straight to Arabic — and most of them are sitting in your weekly parashah. The interdental words (תלת, דהב, דכר) are the ones only Aramaic can teach: where Hebrew shifted its consonants, Aramaic and Arabic agree.",
    sample: "תלת · דהב · ארעא · בית · חמרא",
  },
  {
    href: "/learn/grammar/article",
    status: "Grammar",
    title: "The Definite Article",
    body: "Arabic has one word for \"the\" — אל, glued to the front of the noun. Learn it, plus why אלשמס is said ash-shams, and a huge share of every page turns into \"the X.\"",
    sample: "אלסמא · אלשמס · אלקמר · אלארץ׳",
  },
  {
    href: "/learn/grammar/suffixes",
    status: "Grammar",
    title: "Pronominal Suffixes",
    body: "\"His book\" is one word: כתאב + ה. These little endings are the #1 reason a word you know looks unfamiliar — peel them off and the stem jumps back out.",
    sample: "רבה · להם · מנה · אסמה",
  },
  {
    href: "/learn/grammar/verbs",
    status: "Grammar",
    title: "The Verb Spine",
    body: "Two verbs hold the Tafsir together: קאל \"he said\" and כאן \"he was.\" Learn how they flex — past-tense endings, present-tense prefixes — and the narrative opens up.",
    sample: "קאל · קאלוא · יקול · כאן",
  },
  {
    href: "/learn/on-ramp",
    status: "Read",
    title: "Read Your First Verses",
    body: "Put it together. Read the first day of creation in Saadia's own Arabic — one clause at a time, word by word — then step straight into the full chapter.",
    sample: "אול מא כ׳לק אללה · פכאן נור",
  },
  {
    href: "/learn/saadia-story",
    status: "Live",
    title: "Who Was Saadia?",
    body: "A short walk through the 10th century — and the choice one rabbi made that shaped how Arabic-speaking Jews would read Torah for the next thousand years. Ends with Saadia's own words.",
    sample: "ca. 882 – 942 CE · Egypt → Baghdad",
  },
  {
    href: "/learn/saadia-preface",
    status: "Live",
    title: "Saadia's Own Preface",
    body: "Saadia's preface to the Tafsir — in Judeo-Arabic alongside English. The opening, his theory of why the Torah teaches by story, and his plain statement of why he wrote this book. Most of it being published in English for the first time.",
    sample: "תפסיר תורה · ca. 930 CE",
  },
];

export default function LearnHub() {
  return (
    <div className="max-w-5xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12 max-w-2xl">
        <p className="label mb-3">
          Learn · short formats
        </p>
        <h1 className="display text-4xl text-ink">
          A way <span className="text-wine italic">in</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Bite-sized, browseable ways into Judeo-Arabic. No prior background
          required — start with the words you&apos;ll see most.
        </p>
      </header>

      <GuidedPath />

      <ul className="grid gap-5 lg:grid-cols-2">
        {lessons.map((l) => {
          const card = (
            <div
              className={`block rounded-md bg-page border p-7 transition-all ${
                l.href
                  ? "border-ink/10 hover:border-wine/40 hover:shadow-md hover:shadow-wine/5 cursor-pointer"
                  : "border-ink/10 opacity-60"
              }`}
            >
              <div className="flex items-baseline justify-between">
                <span className={`badge ${l.status === "Live" ? "badge-live" : "badge-muted"}`}>
                  {l.status}
                </span>
              </div>
              <div
                className={`mt-1 text-2xl text-ink transition-colors ${
                  l.href ? "group-hover:text-wine" : ""
                }`}
              >
                {l.title}
              </div>
              <p className="mt-3 text-[15px] text-ink/70 leading-relaxed">
                {l.body}
              </p>
              <div
                dir="rtl"
                className="font-hebrew text-xl text-ink/80 mt-5 leading-loose"
              >
                {l.sample}
              </div>
            </div>
          );
          return (
            <li key={l.title}>
              {l.href ? (
                <Link href={l.href} className="group block">
                  {card}
                </Link>
              ) : (
                card
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
