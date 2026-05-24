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

const stages = [
  {
    numeral: "I",
    eyebrow: "Start here",
    eyebrowEmphasis: true,
    href: "/alphabet",
    title: "Alphabet",
    subtitle: "5 lessons",
    body: "Five short lessons on how Hebrew letters render Arabic phonemes — the diacritic letters, the definite article אל, and the orthographic conventions of medieval Judeo-Arabic.",
    sample: "ג׳ · ד׳ · ח׳ · ט׳ · ת׳",
  },
  {
    numeral: "II",
    eyebrow: "Saadia, Bereshit",
    href: "/tafsir",
    title: "Tafsir Reader",
    subtitle: "Stage 2",
    body: "Read Saadia's Tafsir verse-by-verse alongside the biblical Hebrew. Tap any Judeo-Arabic word for a starter Blau gloss; toggle Arabic-script, Hebrew translation, and English.",
    sample: "אול מא כ׳לק אללה",
  },
  {
    numeral: "III",
    eyebrow: "Bahya, The First Gate",
    href: "/advanced",
    title: "Advanced Reader",
    subtitle: "Stage 3",
    body: "The opening gate of Bahya ibn Paquda's Chovot HaLevavot in its original Judeo-Arabic, with Ibn Tibbon's classical Hebrew translation (Sefaria) and a working English translation alongside.",
    sample: "תוחיד אללה תעאלי",
  },
];

export default function Home() {
  const reading = currentReading();
  return (
    <div className="text-ink">
      {/* Sticky parsha banner */}
      {reading && (
        <div className="sticky top-0 z-40 border-b border-ink/10 bg-parchment/85 backdrop-blur supports-[backdrop-filter]:bg-parchment/70">
          <Link
            href={rangeHref(reading.range)}
            className="group block mx-auto max-w-5xl px-6 py-3"
          >
            <div className="flex flex-col items-start justify-between gap-2 sm:flex-row sm:items-center">
              <div className="flex items-baseline gap-4">
                <span className="text-[10px] font-bold uppercase tracking-[0.22em] text-wine">
                  This week · {ALIYAH_DAY_LABELS[reading.aliyahNumber - 1]} ·{" "}
                  {ALIYAH_LABELS[reading.aliyahNumber - 1]}
                </span>
                <span
                  dir="rtl"
                  className="font-hebrew text-lg text-wine/90"
                >
                  {reading.parsha.hebrew}
                </span>
              </div>
              <div className="flex items-baseline gap-3 text-sm italic text-ink/80 transition-colors group-hover:text-wine">
                <span>
                  Today&apos;s aliyah in the Tafsir —{" "}
                  <span className="not-italic">{reading.parsha.title}</span>{" "}
                  <span className="font-mono not-italic text-xs text-ink/60">
                    {BOOK_DISPLAY[reading.range.start.book]}{" "}
                    {reading.range.start.ch}:{reading.range.start.v}
                    {"–"}
                    {reading.range.end.ch === reading.range.start.ch
                      ? reading.range.end.v
                      : `${reading.range.end.ch}:${reading.range.end.v}`}
                  </span>
                </span>
                <span className="text-wine transition-transform group-hover:translate-x-0.5">
                  →
                </span>
              </div>
            </div>
          </Link>
        </div>
      )}

      {/* Editorial hero — left-aligned, focused */}
      <header className="mx-auto max-w-3xl px-6 pt-16 pb-12 sm:pt-24">
        <p className="mb-4 text-[10px] font-bold uppercase tracking-[0.3em] text-wine">
          A Reader-First Introduction
        </p>
        <h1 className="text-4xl sm:text-5xl tracking-tight leading-tight">
          Learn to read{" "}
          <em className="font-normal italic text-wine">Judeo-Arabic.</em>
        </h1>
        <p
          dir="rtl"
          lang="he"
          className="mt-3 font-hebrew text-2xl sm:text-3xl text-wine/90 leading-snug"
        >
          ערבית־יהודית לקוראי עברית
        </p>
        <p className="mt-6 max-w-2xl text-lg leading-relaxed text-ink/75">
          For Hebrew readers: start with the script, read Saadia&apos;s Tafsir
          on Bereshit alongside the biblical text, then move on to Bahya&apos;s
          philosophical prose. Each text appears with parallel translations
          and a tap-to-define dictionary.
        </p>
      </header>

      {/* Parallel-text preview */}
      <section className="mx-auto max-w-5xl border-y border-ink/10 px-6 py-16 sm:py-20">
        <div className="mb-10 flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="mb-2 text-[10px] font-bold uppercase tracking-[0.22em] text-wine">
              Preview · Reader
            </p>
            <h2 className="text-2xl sm:text-3xl">Saadia, Bereshit 1:1</h2>
          </div>
          <p className="text-sm italic text-muted">
            ↓ tap any word for a Blau gloss
          </p>
        </div>

        <div className="grid gap-10 md:grid-cols-2">
          {/* JA source + gloss */}
          <div>
            <div className="rounded-sm border border-ink/10 bg-page p-6 sm:p-8 shadow-sm shadow-wine/5">
              <p
                dir="rtl"
                className="font-hebrew text-right text-2xl sm:text-3xl leading-loose"
              >
                <span>אול מא </span>
                <span className="rounded-sm bg-wine-100 text-wine-700 px-1.5 py-0.5 ring-1 ring-wine/25">
                  כ׳לק
                </span>
                <span> אללה. אלסמאואת ואלארץ׳</span>
              </p>

              <div className="mt-8 border-l-2 border-wine bg-parchment/60 p-5">
                <div className="mb-4 flex items-start justify-between gap-4">
                  <span className="text-[10px] font-bold uppercase tracking-[0.22em] text-muted">
                    Gloss
                  </span>
                  <div className="text-right">
                    <div className="font-hebrew text-xl" dir="rtl">
                      כ׳לק
                    </div>
                    <div
                      className="mt-0.5 font-arabic text-base text-muted"
                      dir="rtl"
                    >
                      خلق
                    </div>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-y-4 text-sm">
                  <div>
                    <span className="mb-1 block text-[10px] uppercase tracking-widest text-muted">
                      Root
                    </span>
                    <span className="font-mono">√ḫ-l-q</span>
                  </div>
                  <div>
                    <span className="mb-1 block text-[10px] uppercase tracking-widest text-muted">
                      Part of Speech
                    </span>
                    <span className="italic">verb · perf. 3sg.m.</span>
                  </div>
                  <div>
                    <span className="mb-1 block text-[10px] uppercase tracking-widest text-muted">
                      English
                    </span>
                    <span>he created</span>
                  </div>
                  <div>
                    <span className="mb-1 block text-[10px] uppercase tracking-widest text-muted">
                      Hebrew
                    </span>
                    <span className="font-hebrew" dir="rtl">
                      ברא
                    </span>
                  </div>
                  <div className="col-span-2 border-t border-ink/10 pt-3 text-xs italic text-ink/70 leading-relaxed">
                    Saadia&apos;s rendering of biblical{" "}
                    <span className="font-hebrew not-italic" dir="rtl">
                      ברא
                    </span>
                    . The diacritic{" "}
                    <span className="font-hebrew not-italic">׳</span> on{" "}
                    <span className="font-hebrew not-italic">כ</span> marks{" "}
                    <span className="font-arabic" dir="rtl">
                      خ
                    </span>{" "}
                    (kh).
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Translation + commentary */}
          <div className="flex flex-col justify-between">
            <div>
              <p className="mb-3 text-[10px] font-bold uppercase tracking-[0.22em] text-wine">
                Translation
              </p>
              <p className="text-xl sm:text-2xl italic leading-relaxed">
                &ldquo;The first thing God created: the heavens and the
                earth.&rdquo;
              </p>
              <p className="mt-6 max-w-md text-sm leading-relaxed text-ink/70">
                Saadia begins his Tafsir not with a calque of Hebrew{" "}
                <span className="font-hebrew" dir="rtl">
                  בראשית
                </span>
                , but with an Arabic construction —{" "}
                <span className="font-hebrew" dir="rtl">
                  אול מא כ׳לק
                </span>{" "}
                — that resolves the verse&apos;s syntactic ambiguity in the
                act of translating it.
              </p>
            </div>
            <Link
              href="/tafsir/bereshit/1#verse-1-1"
              className="group mt-8 inline-flex items-center gap-2 self-start border-b border-wine/30 pb-1 text-[11px] font-bold uppercase tracking-[0.18em] text-wine hover:border-wine"
            >
              Open in the reader
              <span aria-hidden className="transition-transform group-hover:translate-x-1">
                →
              </span>
            </Link>
          </div>
        </div>
      </section>

      {/* Three-stage curriculum */}
      <section className="mx-auto max-w-5xl px-6 py-20 sm:py-24">
        <h2 className="mb-12 text-center text-[10px] font-bold uppercase tracking-[0.3em] text-wine">
          The Curriculum
        </h2>
        <div className="grid gap-px overflow-hidden rounded-sm border border-ink/10 bg-ink/10 md:grid-cols-3">
          {stages.map((s) => (
            <Link
              key={s.href}
              href={s.href}
              className="group flex flex-col bg-parchment p-7 transition-colors hover:bg-page"
            >
              <div className="mb-5 flex items-baseline justify-between gap-2">
                <span className="text-5xl font-light text-wine/25 transition-colors group-hover:text-wine/55">
                  {s.numeral}
                </span>
                <span
                  className={
                    s.eyebrowEmphasis
                      ? "text-[10px] font-bold uppercase tracking-widest text-wine"
                      : "text-[10px] font-bold uppercase tracking-widest text-muted"
                  }
                >
                  {s.eyebrow}
                </span>
              </div>
              <h3 className="mb-2 text-xl font-bold group-hover:text-wine transition-colors">
                {s.title}
              </h3>
              <p className="mb-5 text-sm leading-relaxed text-ink/70">
                {s.body}
              </p>
              <div className="mt-auto border-t border-ink/10 pt-4">
                <p
                  dir="rtl"
                  className="font-hebrew text-xl leading-relaxed text-ink/80"
                >
                  {s.sample}
                </p>
              </div>
            </Link>
          ))}
        </div>

        {/* Learn — bite-sized formats */}
        <Link
          href="/learn"
          className="group mt-8 block rounded-sm border border-ink/10 bg-page p-6 sm:p-7 transition-all hover:border-wine/40 hover:shadow-md hover:shadow-wine/5"
        >
          <div className="flex flex-col gap-3 sm:flex-row sm:items-baseline sm:justify-between">
            <div>
              <p className="text-[10px] font-bold uppercase tracking-widest text-muted">
                Bite-sized formats
              </p>
              <h3 className="mt-1 text-xl group-hover:text-wine transition-colors">
                Learn{" "}
                <span aria-hidden className="text-wine">
                  →
                </span>
              </h3>
            </div>
            <p
              dir="rtl"
              className="font-hebrew text-lg text-ink/80"
            >
              אללה · ארץ׳ · קאל · כ׳לק · מוסי
            </p>
          </div>
          <p className="mt-3 text-sm leading-relaxed text-ink/70">
            Your first 50 Judeo-Arabic words ranked by how often they show up
            in Saadia, Hebrew–Arabic and Aramaic–Arabic cognates, the story
            of Saadia, and his own preface.
          </p>
        </Link>

        {/* Returning-user rail */}
        <div className="mt-10 pt-6 border-t border-ink/10 text-sm text-ink/70 flex items-center justify-between flex-wrap gap-3">
          <span>Already practicing?</span>
          <Link
            href="/review"
            className="text-wine hover:underline tracking-wide"
          >
            Continue your daily review →
          </Link>
        </div>
      </section>
    </div>
  );
}
