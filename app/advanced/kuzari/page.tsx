import type { Metadata } from "next";
import Link from "next/link";
import { KUZARI_GATES } from "./volume";

export const metadata: Metadata = {
  title: "Yehuda HaLevi's Kuzari — complete, in Judeo-Arabic",
  description:
    "The complete Kuzari (Kitāb al-Khazarī) of Yehuda HaLevi — all five maqalat — in its original 12th-century Judeo-Arabic, with a tap-to-define dictionary on every word.",
  alternates: { canonical: "/advanced/kuzari" },
};

export default function KuzariContents() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Stage III · The Library</p>
        <h1 className="display text-4xl text-ink">
          Halevi,{" "}
          <span className="text-wine italic">Kitāb al-Khazarī</span>.
        </h1>
        <p className="mt-3 text-lg font-hebrew text-ink/70" dir="rtl">
          כתאב אלרד ואלדליל פי אלדין אלד׳ליל
        </p>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          The complete <span className="italic">Kuzari</span> — all five
          maqalat — in its original 12th-century Judeo-Arabic, with a working
          English translation and phrase-by-phrase hover highlighting
          throughout. Every word taps to a dictionary gloss. Maqala I also
          carries notes on nine key philosophical terms.
        </p>
      </header>

      <ol className="space-y-3">
        {KUZARI_GATES.map((g) => {
          const { section, section_ja, subtitle } = g.json;
          const isTranslated = Boolean(g.english && g.aligned);
          return (
            <li key={g.slug}>
              <Link
                href={`/advanced/kuzari/${g.slug}`}
                className="group block rounded-md bg-page border border-ink/10 p-5 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
              >
                <div className="flex items-baseline justify-between gap-3">
                  <span className="text-2xl text-ink group-hover:text-wine transition-colors">
                    {section}
                  </span>
                  {section_ja && (
                    <span dir="rtl" className="font-hebrew text-lg text-ink/70">
                      {section_ja}
                    </span>
                  )}
                </div>
                {subtitle && (
                  <p className="mt-1 text-[15px] text-ink/65 italic leading-relaxed">
                    {subtitle}
                  </p>
                )}
                {isTranslated && (
                  <span className="badge badge-live mt-3 inline-block">
                    + English &amp; hover highlighting
                  </span>
                )}
              </Link>
            </li>
          );
        })}
      </ol>

      <p className="mt-10">
        <Link href="/advanced" className="text-sm text-muted hover:text-ink">
          ← Back to the Library
        </Link>
      </p>
    </div>
  );
}
