import type { Metadata } from "next";
import Link from "next/link";
import {
  AVOT_CHAPTERS,
  AVODAH_ZARAH_CHAPTERS,
  BERAKHOT_CHAPTERS,
  SANHEDRIN_CHAPTERS,
  ZERAIM_INTRO_CHAPTERS,
  mishnahHref,
  MISHNAH_BASE,
} from "./chapters";

export const metadata: Metadata = {
  title: "Rambam — Commentary on the Mishnah in Judeo-Arabic",
  description:
    "Maimonides' Commentary on the Mishnah in its original 12th-century Judeo-Arabic — the Introduction to the Mishnah, Tractate Avot (including the Eight Chapters), and Tractate Sanhedrin (including the 13 Principles).",
  alternates: { canonical: MISHNAH_BASE },
};

type TractateSection = {
  heading: string;
  tractate: "zeraim-intro" | "avot" | "sanhedrin" | "berakhot" | "avodah-zarah";
  chapters: typeof AVOT_CHAPTERS;
};

const SECTIONS: TractateSection[] = [
  ...(ZERAIM_INTRO_CHAPTERS.length > 0
    ? [
        {
          heading: "Introduction to the Mishnah",
          tractate: "zeraim-intro" as const,
          chapters: ZERAIM_INTRO_CHAPTERS,
        },
      ]
    : []),
  { heading: "Tractate Berakhot", tractate: "berakhot" as const, chapters: BERAKHOT_CHAPTERS },
  { heading: "Tractate Avodah Zarah", tractate: "avodah-zarah" as const, chapters: AVODAH_ZARAH_CHAPTERS },
  { heading: "Tractate Avot", tractate: "avot" as const, chapters: AVOT_CHAPTERS },
  { heading: "Tractate Sanhedrin", tractate: "sanhedrin" as const, chapters: SANHEDRIN_CHAPTERS },
];

export default function MishnahIndex() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Mishnah Commentary</p>
        <h1 className="display text-4xl text-ink">
          Rambam on <span className="text-wine italic">the Mishnah</span>
        </h1>
        <p className="mt-5 text-base text-ink/75 leading-relaxed max-w-xl">
          Maimonides&apos; Commentary on the Mishnah in its original 12th-century
          Judeo-Arabic — including the Eight Chapters on the soul and the virtues,
          and the essay on the Thirteen Principles of Faith.
        </p>
      </header>

      {SECTIONS.map(({ heading, tractate, chapters }) => (
        <section key={tractate} className="mb-10">
          <h2 className="text-xs uppercase tracking-[0.18em] text-ink/50 mb-4">
            {heading}
          </h2>
          <ul className="space-y-3">
            {chapters.map((ch) => (
              <li key={ch.slug}>
                <Link
                  href={mishnahHref(tractate, ch.slug)}
                  className="group flex items-center gap-4 rounded-md bg-page border border-ink/10 px-6 py-4 hover:border-wine/40 hover:shadow-sm transition-all"
                >
                  <span className="text-sm text-ink/40 w-6 text-right shrink-0">
                    {ch.n === 0 ? "—" : ch.n}
                  </span>
                  <span className="text-base text-ink group-hover:text-wine transition-colors">
                    {ch.title}
                  </span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
