"use client";

import Link from "next/link";

export type Mishnah = {
  mishnah: number;
  he: string;
  en: string;
};

export type MishnaChapterData = {
  tractate: string;
  tractate_he: string;
  chapter: number;
  mishnayot: Mishnah[];
};

const ALEPH_BET = "אבגדהוזחטיכלמנסעפצקרשת";
function toHebNum(n: number): string {
  return ALEPH_BET[n - 1] ?? String(n);
}

export function MishnaReader({
  data,
  prevChapter,
  nextChapter,
  tractateSlug,
}: {
  data: MishnaChapterData;
  prevChapter?: number | null;
  nextChapter?: number | null;
  tractateSlug: string;
}) {
  return (
    <div className="max-w-3xl mx-auto px-6 py-12">
      {/* Header */}
      <div className="mb-10">
        <p className="label mb-3">Mishnah · {data.tractate}</p>
        <div className="flex items-baseline gap-4">
          <h1 className="display text-3xl text-ink">
            Chapter {data.chapter}
          </h1>
          <span
            dir="rtl"
            className="font-hebrew text-2xl text-ink/60"
          >
            פרק {toHebNum(data.chapter)}
          </span>
        </div>
        <p dir="rtl" className="font-hebrew text-xl text-ink/70 mt-1">
          מסכת {data.tractate_he}
        </p>
      </div>

      {/* Mishnayot */}
      <ol className="space-y-8">
        {data.mishnayot.map((m) => (
          <li
            key={m.mishnah}
            className="border border-ink/8 rounded-md bg-page p-6 shadow-sm"
          >
            {/* Mishnah number marker */}
            <div className="flex items-start gap-5">
              <div className="shrink-0 w-8 text-center mt-1">
                <span
                  dir="rtl"
                  className="font-hebrew text-base font-semibold text-wine/80"
                  title={`Mishnah ${m.mishnah}`}
                >
                  {toHebNum(m.mishnah)}
                </span>
              </div>

              <div className="flex-1 space-y-4">
                {/* Hebrew text */}
                <p
                  dir="rtl"
                  lang="he"
                  className="font-hebrew text-[1.15rem] text-ink leading-[2.1]"
                >
                  {m.he}
                </p>

                {/* English translation */}
                {m.en && (
                  <p className="text-[0.94rem] text-ink/75 leading-relaxed border-t border-ink/8 pt-4">
                    {m.en}
                  </p>
                )}
              </div>
            </div>
          </li>
        ))}
      </ol>

      {/* Prev / Next */}
      <nav className="mt-12 flex items-center justify-between gap-4 text-sm">
        {prevChapter != null ? (
          <Link
            href={`/mishna/${tractateSlug}/${prevChapter}`}
            className="text-wine hover:underline"
          >
            ← Chapter {prevChapter}
          </Link>
        ) : (
          <span />
        )}
        <Link href={`/mishna/${tractateSlug}`} className="text-muted hover:text-ink">
          All chapters
        </Link>
        {nextChapter != null ? (
          <Link
            href={`/mishna/${tractateSlug}/${nextChapter}`}
            className="text-wine hover:underline"
          >
            Chapter {nextChapter} →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </div>
  );
}
