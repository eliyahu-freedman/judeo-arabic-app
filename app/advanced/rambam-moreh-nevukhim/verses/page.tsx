import type { Metadata } from "next";
import Link from "next/link";
import index from "@/data/moreh-verse-index.json";
import { MOREH_BASE, MOREH_CHAPTERS, morehHref } from "../chapters";

export const metadata: Metadata = {
  title: "Maimonides on this verse — Scripture cited in the Guide, Part I",
  description:
    "Every biblical verse Maimonides interprets in Part I of the Guide of the Perplexed, indexed by verse: which chapter treats it, his own words, and a link to the verse on Sefaria. The Guide made navigable by the Scripture it expounds.",
  alternates: { canonical: `${MOREH_BASE}/verses` },
};

type Occ = { n: number; snippet: string };
type Verse = { v: string; ref: string; occ: Occ[] };
type Book = { book: string; order: number; verses: Verse[] };

const DATA = index as { totals: { books: number; verses: number; citations: number }; books: Book[] };

const CH = new Map(MOREH_CHAPTERS.map((c) => [c.n, { title: c.title, href: morehHref(c.slug) }]));

export default function VersesPage() {
  const { totals, books } = DATA;
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Guide of the Perplexed · Part I</p>
        <h1 className="display text-4xl text-ink">
          Maimonides on <span className="text-wine italic">this verse</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Part I of the Guide moves through the verses by which Scripture seems
          to speak of God in bodily terms. Here those{" "}
          {totals.verses} verses are turned around: pick a verse and see which
          chapter takes it up, in Maimonides' own words — then open the verse on
          Sefaria. {totals.citations} citations in all.
        </p>
        <p className="mt-5 text-sm">
          <Link href={MOREH_BASE} className="text-wine hover:underline underline-offset-2">
            ← Read the Guide
          </Link>
          <span className="mx-2 text-ink/30">·</span>
          <Link href={`${MOREH_BASE}/atlas`} className="text-wine hover:underline underline-offset-2">
            Atlas of God-language
          </Link>
        </p>
      </header>

      <div className="space-y-9">
        {books.map((b) => (
          <section key={b.book}>
            <h2 className="text-xs uppercase tracking-[0.25em] text-muted mb-3 border-b border-ink/10 pb-1">
              {b.book}
            </h2>
            <ul className="space-y-4">
              {b.verses.map((vs) => (
                <li key={vs.ref}>
                  <a
                    href={`https://www.sefaria.org/${vs.ref}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="font-medium text-ink hover:text-wine transition-colors"
                  >
                    {b.book === "Mishnah & Talmud" ? vs.v : `${b.book} ${vs.v}`} ↗
                  </a>
                  <ul className="mt-1 ml-4 space-y-1">
                    {vs.occ.map((o, i) => {
                      const ch = CH.get(o.n);
                      return (
                        <li key={`${vs.ref}-${o.n}-${i}`} className="text-sm text-ink/70">
                          {ch && (
                            <Link
                              href={ch.href}
                              className="text-wine hover:underline underline-offset-2 mr-2 whitespace-nowrap"
                            >
                              {ch.title}
                            </Link>
                          )}
                          <span className="text-ink/60">{o.snippet}</span>
                        </li>
                      );
                    })}
                  </ul>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </div>
  );
}
