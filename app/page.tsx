import type { Metadata } from "next";
import Link from "next/link";
import {
  ALIYAH_DAY_LABELS,
  ALIYAH_LABELS,
  BOOK_DISPLAY,
  currentReading,
  rangeHref,
} from "@/lib/parsha";

export const metadata: Metadata = {
  alternates: {
    canonical: "/",
    languages: {
      "en-US": "/",
      he: "/",
      "x-default": "/",
    },
  },
};

const primary = {
  href: "/alphabet",
  title: "Alphabet",
  subtitle: "Start here · Stage 1",
  body: "Five short lessons on how Hebrew letters render Arabic phonemes — the diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, and the orthographic conventions of medieval Judeo-Arabic.",
  sample: "ג׳ · ד׳ · ח׳ · ט׳ · ת׳",
};

const modules = [
  {
    href: "/tafsir",
    title: "Tafsir Reader",
    subtitle: "Stage 2 · Saadia on Bereshit",
    body: "Read Saadia's Tafsir verse-by-verse alongside the biblical Hebrew. Tap any Judeo-Arabic word for a starter Blau gloss; toggle Arabic-script, Hebrew translation, and English.",
    sample: "אול מא כ׳לק אללה",
  },
  {
    href: "/advanced",
    title: "Advanced Reader",
    subtitle: "Stage 3 · Bahya, The First Gate",
    body: "The opening gate of Bahya ibn Paquda's Chovot HaLevavot in its original Judeo-Arabic, with Ibn Tibbon's classical Hebrew translation (Sefaria) and a working English translation alongside.",
    sample: "אכ'לאץ תוחיד אלכ'אלק",
  },
  {
    href: "/learn",
    title: "Learn",
    subtitle: "Bite-sized formats",
    body: "Your first 50 Judeo-Arabic words ranked by how often they show up in Saadia, Hebrew–Arabic and Aramaic–Arabic cognates, the story of Saadia, and his own preface.",
    sample: "אללה · ארץ' · קאל · כ'לק · מוסי",
  },
];

export default function Home() {
  const reading = currentReading();
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      {reading && (
        <Link
          href={rangeHref(reading.range)}
          className="group block mb-12 rounded-md bg-wine/[0.04] border border-wine/25 px-6 py-5 transition-all hover:bg-wine/[0.07] hover:border-wine/50"
        >
          <div className="flex items-baseline justify-between gap-4 flex-wrap">
            <div className="text-[10px] uppercase tracking-[0.3em] text-wine/80">
              This week · {ALIYAH_DAY_LABELS[reading.aliyahNumber - 1]} ·{" "}
              {ALIYAH_LABELS[reading.aliyahNumber - 1]}
            </div>
            <div dir="rtl" className="font-hebrew text-base text-wine/90">
              {reading.parsha.hebrew}
            </div>
          </div>
          <div className="mt-2 flex items-baseline justify-between gap-4 flex-wrap">
            <div className="text-xl text-ink group-hover:text-wine transition-colors">
              Today&apos;s aliyah in the Tafsir →{" "}
              <span className="italic text-wine">{reading.parsha.title}</span>
            </div>
            <div className="text-sm text-ink/70 font-mono">
              {BOOK_DISPLAY[reading.range.start.book]} {reading.range.start.ch}:
              {reading.range.start.v}
              {"–"}
              {reading.range.end.ch === reading.range.start.ch
                ? reading.range.end.v
                : `${reading.range.end.ch}:${reading.range.end.v}`}
            </div>
          </div>
        </Link>
      )}

      <section className="mb-16 sm:mb-20">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-4">
          A reader-first introduction
        </p>
        <h1 className="text-4xl sm:text-5xl tracking-tight text-ink leading-tight">
          Learn to read{" "}
          <span className="text-wine italic">Judeo-Arabic</span>.
        </h1>
        <p
          dir="rtl"
          lang="he"
          className="mt-3 font-hebrew text-2xl sm:text-3xl text-wine/90 leading-snug"
        >
          ערבית־יהודית לקוראי עברית
        </p>
        <p className="mt-6 text-lg text-ink/75 leading-relaxed max-w-2xl">
          For Hebrew readers: start with the script, read Saadia&apos;s Tafsir
          on Bereshit alongside the biblical text, then move on to Bahya&apos;s
          philosophical prose. Each text appears with parallel translations
          and a tap-to-define dictionary.
        </p>
        <Link
          href="/tafsir/bereshit/1#verse-1-1"
          className="group block mt-10 -mx-3 px-3 py-5 rounded-md transition-colors hover:bg-wine/[0.04]"
          aria-label="Open Saadia's Tafsir on Bereshit 1:1 in the reader"
        >
          <div className="flex items-baseline justify-between gap-3 mb-3 flex-wrap">
            <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
              Preview · Saadia, Bereshit 1:1
            </span>
            <span className="text-[10px] uppercase tracking-[0.3em] text-ink/70 italic normal-case">
              ↓ tap any word for a Blau gloss
            </span>
          </div>
          <div
            dir="rtl"
            className="font-hebrew text-2xl sm:text-3xl leading-loose"
          >
            <span className="text-wine/90">אול מא </span>
            <span className="bg-wine-100 text-wine-700 rounded-sm px-1.5">
              כ׳לק
            </span>
            <span className="text-wine/90"> אללה. אלסמאואת ואלארץ׳</span>
          </div>

          <div className="mt-4 sm:max-w-md sm:ml-auto bg-page border border-wine/30 rounded-md p-4 shadow-sm shadow-wine/10">
            <div className="flex items-baseline gap-3 flex-wrap">
              <span className="font-hebrew text-xl text-ink" dir="rtl">
                כ׳לק
              </span>
              <span className="font-arabic text-lg text-ink/70" dir="rtl">
                خلق
              </span>
              <span className="text-xs text-muted font-mono">√ḫ-l-q</span>
              <span className="text-xs text-muted italic">
                verb · perf. 3sg.m.
              </span>
            </div>
            <p className="mt-2 text-[15px] text-ink">he created</p>
            <p
              dir="rtl"
              className="font-hebrew text-base text-muted mt-0.5"
            >
              ברא
            </p>
            <p className="text-[12px] text-muted italic mt-2 leading-relaxed">
              Saadia&apos;s rendering of biblical ברא. The diacritic ׳ on כ
              marks خ (kh).
            </p>
          </div>

          <p className="mt-4 text-xs uppercase tracking-widest text-muted group-hover:text-wine/70 transition-colors">
            &ldquo;The first thing God created: the heavens and the earth.&rdquo;{" "}
            <span aria-hidden className="text-wine">→ open in the reader</span>
          </p>
        </Link>
      </section>

      {/* Primary CTA — Alphabet */}
      <Link
        href={primary.href}
        className="group block rounded-md bg-wine/[0.06] border-2 border-wine/40 p-7 sm:p-9 transition-all hover:bg-wine/[0.09] hover:border-wine/60 hover:shadow-lg hover:shadow-wine/10"
      >
        <div className="text-xs uppercase tracking-[0.3em] text-wine">
          {primary.subtitle}
        </div>
        <h2 className="mt-2 text-3xl sm:text-4xl text-ink group-hover:text-wine transition-colors font-normal">
          {primary.title}{" "}
          <span aria-hidden className="text-wine">→</span>
        </h2>
        <p className="mt-3 text-[16px] text-ink/75 leading-relaxed">
          {primary.body}
        </p>
        <div
          dir="rtl"
          className="text-2xl text-ink/85 mt-5 leading-loose font-hebrew"
        >
          {primary.sample}
        </div>
      </Link>

      {/* Then: Tafsir, Advanced, Learn */}
      <ul className="space-y-5 mt-5">
        {modules.map((m) => (
          <li key={m.href}>
            <Link
              href={m.href}
              className="group block rounded-md bg-page border border-ink/10 p-7 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
            >
              <div className="text-xs uppercase tracking-[0.25em] text-muted">
                {m.subtitle}
              </div>
              <h2 className="mt-1 text-2xl text-ink group-hover:text-wine transition-colors font-normal">
                {m.title}
              </h2>
              <p className="mt-3 text-[15px] text-ink/70 leading-relaxed">
                {m.body}
              </p>
              <div
                dir="rtl"
                className="text-xl text-ink/80 mt-5 leading-loose font-hebrew"
              >
                {m.sample}
              </div>
            </Link>
          </li>
        ))}
      </ul>

      {/* Quiet bottom rail for returning users */}
      <div className="mt-10 pt-6 border-t border-ink/10 text-sm text-ink/70 flex items-center justify-between flex-wrap gap-3">
        <span>Already practicing?</span>
        <Link
          href="/review"
          className="text-wine hover:underline tracking-wide"
        >
          Continue your daily review →
        </Link>
      </div>
    </div>
  );
}
