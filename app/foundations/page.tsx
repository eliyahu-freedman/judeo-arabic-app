import type { Metadata } from "next";
import Link from "next/link";
import { CURRICULUM } from "@/lib/curriculum";

export const metadata: Metadata = {
  title: "Foundations — the Judeo-Arabic reading path for Hebrew readers",
  description:
    "Stage I of the curriculum: the Hebrew alphabet as Arabic sounds, the diacritics and the article אל, the Saadianic spelling conventions, the cognates and first fifty words you already half-know, the grammar that holds the Tafsir together, and your first decoded sentence — everything you need before opening Saadia.",
  alternates: { canonical: "/foundations" },
};

// The foundations path is the curriculum minus the final "Open the Tafsir"
// step, which is the handoff into Stage II.
const steps = CURRICULUM.filter((s) => s.id !== "tafsir");

export default function FoundationsHub() {
  return (
    <div className="max-w-5xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12 max-w-2xl">
        <p className="label mb-3">
          Stage I · Foundations
        </p>
        <h1 className="display text-4xl text-ink">
          Everything before <span className="text-wine italic">Saadia</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed">
          A short, ordered path from zero to reading. Learn the Hebrew letters
          as Arabic sounds, the conventions of a real manuscript page, the
          words and grammar you already half-know — and finish by decoding your
          first sentence of the Tafsir. No prior Arabic required.
        </p>
      </header>

      <ol className="grid gap-4 lg:grid-cols-2">
        {steps.map((step, i) => (
          <li key={step.id}>
            <Link href={step.href} className="group block">
              <div className="block rounded-md bg-page border border-ink/10 p-6 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5">
                <div className="flex items-baseline gap-3">
                  <span className="text-[11px] font-mono text-muted shrink-0">
                    {String(i + 1).padStart(2, "0")}
                  </span>
                  <div className="text-xl text-ink group-hover:text-wine transition-colors">
                    {step.title}
                  </div>
                </div>
                <p className="mt-2 pl-7 text-sm text-ink/70 leading-relaxed">
                  {step.blurb}
                </p>
              </div>
            </Link>
          </li>
        ))}
      </ol>

      <div className="mt-12 pt-6 border-t border-ink/10 text-sm text-ink/70 flex items-center justify-between flex-wrap gap-3">
        <span>Done with the foundations?</span>
        <Link href="/tafsir" className="text-wine hover:underline tracking-wide">
          Open Saadia&apos;s Tafsir — Stage II →
        </Link>
      </div>
    </div>
  );
}
