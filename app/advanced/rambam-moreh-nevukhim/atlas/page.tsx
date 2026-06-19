import type { Metadata } from "next";
import Link from "next/link";
import { getAtlasTerms, type AtlasTerm } from "@/lib/morehTerms";
import { MOREH_BASE } from "../chapters";

export const metadata: Metadata = {
  title: "The Atlas of God-Language — Maimonides' lexicon of equivocal terms",
  description:
    "Every equivocal term Maimonides unfolds in Part I of the Guide of the Perplexed — image, likeness, place, throne, ascending, sitting, standing, rock, drawing near, passing, dwelling, foot — mapped to the chapter that treats it, with its senses. A navigable index of the Guide's lexicon of God-language.",
  alternates: { canonical: `${MOREH_BASE}/atlas` },
};

export default function AtlasPage() {
  const terms = getAtlasTerms();

  // Group consecutively by chapter (getAtlasTerms returns chapter order).
  const groups: { n: number; title: string; href: string; terms: AtlasTerm[] }[] = [];
  for (const t of terms) {
    const last = groups[groups.length - 1];
    if (last && last.n === t.chapterN) last.terms.push(t);
    else groups.push({ n: t.chapterN, title: t.chapterTitle, href: t.href, terms: [t] });
  }

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Guide of the Perplexed · Part I</p>
        <h1 className="display text-4xl text-ink">
          The Atlas of <span className="text-wine italic">God-language</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Part I of the Guide is, at heart, a dictionary: Maimonides takes the
          words by which Scripture seems to speak of God as a body — image and
          likeness, place and throne, ascending and sitting, standing, rock,
          drawing near, passing, dwelling, foot — and shows that each is{" "}
          <span className="italic">equivocal</span>, never bodily. Here are all{" "}
          {terms.length} key terms he unfolds, in the order he takes them up.
          Tap any chapter to read it in the Judeo-Arabic.
        </p>
        <p className="mt-5 text-sm">
          <Link href={MOREH_BASE} className="text-wine hover:underline underline-offset-2">
            ← Read the Guide
          </Link>
        </p>
      </header>

      <div className="space-y-10">
        {groups.map((g) => (
          <section key={g.n}>
            <Link
              href={g.href}
              className="inline-block text-sm font-medium text-wine hover:underline underline-offset-2 mb-3"
            >
              {g.title} →
            </Link>
            <ul className="space-y-3">
              {g.terms.map((t) => (
                <li
                  key={`${g.n}-${t.id}`}
                  className="rounded-md bg-page border border-ink/10 p-5"
                >
                  <div className="flex items-baseline justify-between gap-3 flex-wrap">
                    <span dir="rtl" className="font-hebrew text-2xl text-ink leading-snug">
                      {t.ja}
                    </span>
                    {t.translit && (
                      <span className="text-sm italic text-ink/60">{t.translit}</span>
                    )}
                  </div>
                  <p className="mt-2 text-[15px] text-ink/80">{t.gloss}</p>
                  {t.note && (
                    <p className="mt-2 text-sm text-ink/65 leading-relaxed">{t.note}</p>
                  )}
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
