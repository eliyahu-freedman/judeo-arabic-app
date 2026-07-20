import type { Metadata } from "next";
import Link from "next/link";

export const metadata: Metadata = {
  title: "Mishnah",
  description: "Mishnah with Hebrew text and English translation.",
  alternates: { canonical: "/mishna" },
};

const tractates = [
  {
    slug: "yoma",
    name: "Yoma",
    he: "יומא",
    seder: "Moed",
    chapters: [{ n: 1, label: "Chapter 1" }],
  },
];

export default function MishnaIndex() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16">
      <header className="mb-10">
        <p className="label mb-3">Mishnah</p>
        <h1 className="display text-4xl text-ink">
          משנה
        </h1>
        <p className="mt-4 text-ink/70 leading-relaxed max-w-lg">
          Mishnah with vocalized Hebrew text and English translation.
        </p>
      </header>

      {tractates.map((t) => (
        <section key={t.slug} className="mb-10">
          <div className="flex items-baseline gap-3 mb-4">
            <h2 className="text-lg font-semibold text-ink">
              Tractate {t.name}
            </h2>
            <span dir="rtl" className="font-hebrew text-lg text-ink/60">
              מסכת {t.he}
            </span>
            <span className="label ml-2">{t.seder}</span>
          </div>
          <ul className="space-y-2">
            {t.chapters.map((ch) => (
              <li key={ch.n}>
                <Link
                  href={`/mishna/${t.slug}/${ch.n}`}
                  className="flex items-center gap-4 rounded border border-ink/10 bg-page px-5 py-3 hover:border-wine/40 hover:shadow-sm transition-all"
                >
                  <span className="text-sm text-ink">{ch.label}</span>
                  <span className="text-xs text-muted ml-auto">→</span>
                </Link>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
