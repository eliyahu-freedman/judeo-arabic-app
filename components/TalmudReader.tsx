"use client";

import Link from "next/link";

export type TalmudSection = {
  type: "mishna" | "gemara";
  he: string;
  en: string;
};

export type DafData = {
  tractate: string;
  tractate_he: string;
  daf: string;
  sections: TalmudSection[];
};

const DAPIM = ["2a", "2b", "3a", "3b", "4a", "4b", "5a", "5b"];

export function TalmudReader({
  data,
}: {
  data: DafData;
}) {
  const idx = DAPIM.indexOf(data.daf);
  const prevDaf = idx > 0 ? DAPIM[idx - 1] : null;
  const nextDaf = idx < DAPIM.length - 1 ? DAPIM[idx + 1] : null;

  let lastType: "mishna" | "gemara" | null = null;

  return (
    <div className="max-w-3xl mx-auto px-6 py-12">
      {/* Header */}
      <div className="mb-10">
        <p className="label mb-3">Talmud Bavli · {data.tractate}</p>
        <div className="flex items-baseline gap-4">
          <h1 className="display text-3xl text-ink">
            Daf {data.daf}
          </h1>
          <span dir="rtl" className="font-hebrew text-xl text-ink/60">
            {data.tractate_he} דף {data.daf}
          </span>
        </div>
      </div>

      {/* Sections */}
      <div className="space-y-1">
        {data.sections.map((s, i) => {
          const showTypeLabel = s.type !== lastType;
          lastType = s.type;
          return (
            <div key={i}>
              {showTypeLabel && (
                <div
                  className={`mt-6 mb-3 flex items-center gap-3 ${
                    s.type === "mishna"
                      ? "text-wine"
                      : "text-muted"
                  }`}
                >
                  <span
                    className="text-[10px] font-bold uppercase tracking-[0.22em] leading-none"
                  >
                    {s.type === "mishna" ? "Mishnah" : "Gemara"}
                  </span>
                  <span className="flex-1 h-px bg-current opacity-20" />
                </div>
              )}
              <div
                className={`rounded p-4 ${
                  s.type === "mishna"
                    ? "bg-wine-50 border border-wine/10"
                    : "bg-page border border-ink/6"
                }`}
              >
                <p
                  dir="rtl"
                  lang="he"
                  className="font-hebrew text-[1.1rem] text-ink leading-[2.1]"
                >
                  {s.he}
                </p>
                {s.en && (
                  <p className="mt-3 text-[0.92rem] text-ink/70 leading-relaxed border-t border-ink/8 pt-3">
                    {s.en}
                  </p>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Prev / Next daf */}
      <nav className="mt-12 flex items-center justify-between gap-4 text-sm">
        {prevDaf ? (
          <Link
            href={`/talmud/bava-metzia/${prevDaf}`}
            className="text-wine hover:underline"
          >
            ← {data.tractate} {prevDaf}
          </Link>
        ) : (
          <span />
        )}
        <Link href="/talmud/bava-metzia" className="text-muted hover:text-ink">
          All dapim
        </Link>
        {nextDaf ? (
          <Link
            href={`/talmud/bava-metzia/${nextDaf}`}
            className="text-wine hover:underline"
          >
            {data.tractate} {nextDaf} →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </div>
  );
}
