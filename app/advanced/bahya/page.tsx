import type { Metadata } from "next";
import Link from "next/link";
import { BAHYA_GATES } from "./volume";

export const metadata: Metadata = {
  title: "Bahya ibn Paquda's Chovot HaLevavot — complete, in Judeo-Arabic",
  description:
    "The complete Chovot HaLevavot (Duties of the Hearts) of Bahya ibn Paquda — the author's introduction and all ten gates — in its original 11th-century Judeo-Arabic, with a tap-to-define dictionary on every word.",
  alternates: { canonical: "/advanced/bahya" },
};

export default function BahyaContents() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="label mb-3">Stage III · The Library</p>
        <h1 className="display text-4xl text-ink">
          Bahya, <span className="text-wine italic">Chovot HaLevavot</span>.
        </h1>
        <p className="mt-3 text-lg font-hebrew text-ink/70" dir="rtl">
          כתאב אלהדאיה אלי פראיץ' אלקלוב
        </p>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          The complete <span className="italic">Duties of the Hearts</span> — the
          author&apos;s introduction and all ten gates — in its original
          11th-century Judeo-Arabic. Every word taps through to a dictionary
          gloss. The First Gate also carries a working English translation with
          phrase-by-phrase hover highlighting; the remaining gates are being
          translated.
        </p>
      </header>

      <ol className="space-y-3">
        {BAHYA_GATES.map((g, i) => {
          const { section, section_ja, subtitle } = g.json;
          const isFirstGate = g.slug === "bab-1";
          return (
            <li key={g.slug}>
              <Link
                href={`/advanced/bahya/${g.slug}`}
                className="group block rounded-md bg-page border border-ink/10 p-5 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
              >
                <div className="flex items-baseline justify-between gap-3">
                  <span className="text-2xl text-ink group-hover:text-wine transition-colors">
                    {section}
                  </span>
                  {section_ja && (
                    <span
                      dir="rtl"
                      className="font-hebrew text-lg text-ink/70"
                    >
                      {section_ja}
                    </span>
                  )}
                </div>
                {subtitle && (
                  <p className="mt-1 text-[15px] text-ink/65 italic leading-relaxed">
                    {subtitle}
                  </p>
                )}
                {isFirstGate && (
                  <span className="badge badge-live mt-3 inline-block">
                    + English &amp; hover highlighting
                  </span>
                )}
                <span className="sr-only">{`Gate ${i}`}</span>
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
