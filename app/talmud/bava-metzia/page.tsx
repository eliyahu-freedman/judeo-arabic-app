import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Bava Metzia — Talmud Bavli",
  description: "Talmud Bavli, Tractate Bava Metzia — Shnayim Ohazim. Hebrew text with English translation.",
  alternates: { canonical: "/talmud/bava-metzia" },
};

const DAPIM = ["2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b"];

export default function BavaMetzeiaIndex() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16">
      <header className="mb-10">
        <p className="label mb-3">Talmud Bavli · Seder Nezikin</p>
        <div className="flex items-baseline gap-4">
          <h1 className="display text-4xl text-ink">Bava Metzia</h1>
          <span dir="rtl" className="font-hebrew text-2xl text-ink/60">
            בבא מציעא
          </span>
        </div>
        <p className="mt-4 text-ink/70 leading-relaxed max-w-lg">
          Chapter 1 — <em>Shnayim Ohazim</em>. Two hold a garment…
        </p>
      </header>

      <ul className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        {DAPIM.map((daf) => (
          <li key={daf}>
            <Link
              href={`/talmud/bava-metzia/${daf}`}
              className="flex items-center justify-center rounded border border-ink/10 bg-page py-4 hover:border-wine/40 hover:shadow-sm transition-all"
            >
              <span dir="rtl" className="font-hebrew text-lg text-ink">
                {daf}
              </span>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
