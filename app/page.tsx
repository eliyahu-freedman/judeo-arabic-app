import type { Metadata } from "next";
import Link from "next/link";
import {
  ALIYAH_DAY_LABELS,
  ALIYAH_LABELS,
  BOOK_DISPLAY,
  currentReading,
  rangeHref,
} from "@/lib/parsha";
import { ReturningRail } from "@/components/ReturningRail";
import { corpusStats, fmt } from "@/lib/corpusStats";

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

export default function Home() {
  const reading = currentReading();
  return (
    <div className="text-ink">

      {/* ── Sticky parsha banner ─────────────────────────────────────────── */}
      {reading && (
        <div className="sticky top-0 z-40 border-b border-ink/10 bg-parchment/85 backdrop-blur supports-[backdrop-filter]:bg-parchment/70">
          <Link
            href={rangeHref(reading.range)}
            className="group block mx-auto max-w-5xl px-6 py-3"
          >
            <div className="flex flex-col items-start justify-between gap-2 sm:flex-row sm:items-center">
              <div className="flex items-baseline gap-4">
                <span className="label label-accent">
                  This week · {ALIYAH_DAY_LABELS[reading.aliyahNumber - 1]} ·{" "}
                  {ALIYAH_LABELS[reading.aliyahNumber - 1]}
                </span>
                <span dir="rtl" className="font-hebrew text-lg text-wine/90">
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
                <span className="text-wine transition-transform group-hover:translate-x-0.5">→</span>
              </div>
            </div>
          </Link>
        </div>
      )}

      {/* ── Hero ─────────────────────────────────────────────────────────── */}
      <section className="relative overflow-hidden">

        {/* Atmospheric warm wash */}
        <div
          aria-hidden
          className="pointer-events-none absolute inset-0 bg-[radial-gradient(ellipse_55%_50%_at_75%_-5%,rgba(114,47,55,0.09),transparent)]"
        />

        {/* Decorative giant JA text — the subject IS the art */}
        <p
          aria-hidden
          dir="rtl"
          className="pointer-events-none select-none absolute top-0 right-0 font-hebrew text-[9rem] sm:text-[13rem] leading-none text-ink/[0.04] whitespace-nowrap"
        >
          אול מא כ׳לק אללה
        </p>

        <div className="relative mx-auto max-w-2xl px-6 pt-20 pb-16 sm:pt-28 text-center">
          <p className="label label-accent mb-6">A digital reader &amp; lexicon</p>
          <h1 className="display text-5xl sm:text-6xl leading-[1.07]">
            The medieval{" "}
            <em className="font-normal italic text-wine not-italic">Judeo-Arabic</em>{" "}
            library, read in the original.
          </h1>
          <p className="mt-6 text-base sm:text-lg text-ink/65 leading-relaxed max-w-lg mx-auto">
            Saadia, Bahya, Rambam, Halevi, Qirqisani — the classics in
            Judeo-Arabic with parallel Hebrew and English, and a tap-to-define
            lexicon from Lane and Blau.
          </p>
          <p className="mt-7 text-xs text-muted tracking-wide">
            {fmt(corpusStats.totalTokens)} words indexed ·{" "}
            {fmt(corpusStats.dictionaryEntries)} lexicon entries ·{" "}
            {fmt(corpusStats.uniqueRoots)} roots · 6 classical works
          </p>
        </div>
      </section>

      {/* ── Manuscript showcase ──────────────────────────────────────────── */}
      <section className="bg-wine">
        <div className="mx-auto max-w-5xl px-6 py-16 sm:py-20 text-center">
          <p
            dir="rtl"
            className="font-hebrew text-5xl sm:text-6xl md:text-7xl text-parchment/95 leading-loose"
          >
            אול מא כ׳לק אללה
          </p>
          <p
            dir="rtl"
            className="font-hebrew text-2xl sm:text-3xl text-parchment/40 leading-loose -mt-2"
          >
            אלסמאואת ואלארץ׳
          </p>
          <div className="mt-8 border-t border-parchment/15 pt-7">
            <p className="font-serif text-base sm:text-lg italic text-parchment/75 leading-relaxed">
              &ldquo;The first thing God created — the heavens and the earth.&rdquo;
            </p>
            <p className="mt-2 text-[11px] tracking-[0.18em] uppercase text-parchment/40">
              Saadia Gaon · Tafsir al-Torah · Genesis 1:1
            </p>
          </div>
          <Link
            href="/tafsir/bereshit/1#verse-1-1"
            className="inline-flex items-center gap-2 mt-8 text-sm text-parchment/60 hover:text-parchment transition-colors border-b border-parchment/25 hover:border-parchment/60 pb-0.5"
          >
            Open in the Tafsir reader <span aria-hidden>→</span>
          </Link>
        </div>
      </section>

      {/* ── Three stage cards ────────────────────────────────────────────── */}
      <section className="mx-auto max-w-5xl px-6 py-16 sm:py-20">
        <div className="grid gap-6 md:grid-cols-3">

          {/* I · Foundations */}
          <Link
            href="/foundations"
            className="group block rounded-xl bg-page p-8
                       shadow-[0_1px_3px_rgba(28,26,23,0.05),0_6px_24px_-4px_rgba(28,26,23,0.07)]
                       ring-1 ring-inset ring-black/[0.03]
                       transition-all duration-300
                       hover:shadow-[0_10px_44px_-6px_rgba(114,47,55,0.22)]
                       hover:-translate-y-1.5"
          >
            <p className="label mb-5">Stage I</p>
            <h3 className="display text-xl text-ink mb-6 group-hover:text-wine transition-colors">
              Foundations
            </h3>
            <div className="flex items-center gap-5 py-6 border-y border-ink/[0.06]">
              <span className="font-hebrew text-7xl text-ink leading-none">כ</span>
              <span className="text-2xl text-ink/20">→</span>
              <span className="font-arabic text-6xl text-ink leading-none" dir="rtl">خ</span>
            </div>
            <p className="mt-6 text-sm text-muted leading-relaxed">
              Hebrew script covers most of the Arabic alphabet. A handful of
              diacritics mark the new sounds. No prior knowledge required.
            </p>
          </Link>

          {/* II · Tafsir Reader */}
          <Link
            href="/tafsir"
            className="group block rounded-xl bg-page p-8
                       shadow-[0_1px_3px_rgba(28,26,23,0.05),0_6px_24px_-4px_rgba(28,26,23,0.07)]
                       ring-1 ring-inset ring-black/[0.03]
                       transition-all duration-300
                       hover:shadow-[0_10px_44px_-6px_rgba(114,47,55,0.22)]
                       hover:-translate-y-1.5"
          >
            <p className="label mb-5">Stage II</p>
            <h3 className="display text-xl text-ink mb-6 group-hover:text-wine transition-colors">
              Tafsir Reader
            </h3>
            <div dir="rtl" className="py-6 border-y border-ink/[0.06]">
              <p className="font-hebrew text-2xl text-ink leading-loose text-right">
                אול מא כ׳לק אללה
              </p>
              <p className="font-hebrew text-lg text-ink/40 leading-loose text-right">
                אלסמאואת ואלארץ׳
              </p>
            </div>
            <p className="mt-6 text-sm text-muted leading-relaxed">
              Saadia Gaon&apos;s Tafsir on the Torah, verse by verse. Tap any
              word to open the lexicon.
            </p>
          </Link>

          {/* III · The Library */}
          <Link
            href="/advanced"
            className="group block rounded-xl bg-page p-8
                       shadow-[0_1px_3px_rgba(28,26,23,0.05),0_6px_24px_-4px_rgba(28,26,23,0.07)]
                       ring-1 ring-inset ring-black/[0.03]
                       transition-all duration-300
                       hover:shadow-[0_10px_44px_-6px_rgba(114,47,55,0.22)]
                       hover:-translate-y-1.5"
          >
            <p className="label mb-5">Stage III</p>
            <h3 className="display text-xl text-ink mb-6 group-hover:text-wine transition-colors">
              The Library
            </h3>
            <div dir="rtl" className="py-6 border-y border-ink/[0.06] space-y-0.5">
              <p className="font-hebrew text-xl text-ink leading-loose text-right">
                כתאב אלהדאיה אלי פראיץ׳ אלקלוב
              </p>
              <p className="font-hebrew text-base text-ink/45 leading-loose text-right">
                דלאלה אלחאירין
              </p>
              <p className="font-hebrew text-base text-ink/25 leading-loose text-right">
                כתאב אלאמאנאת ואלאעתקאדאת
              </p>
            </div>
            <p className="mt-6 text-sm text-muted leading-relaxed">
              Bahya, Rambam, Halevi, Qirqisani, Saadia — the classical shelf
              in Judeo-Arabic.
            </p>
          </Link>

        </div>
      </section>

      {/* ── Support section ─────────────────────────────────────────────── */}
      <section className="border-t border-ink/8 bg-page/40">
        <div className="mx-auto max-w-5xl px-6 py-16 sm:py-20 md:flex md:items-center md:justify-between md:gap-16">
          <div className="max-w-xl">
            <p className="label label-accent mb-4">Support the project</p>
            <h2 className="display text-3xl sm:text-4xl leading-snug">
              From the script to the shelf —<br className="hidden sm:block" /> stage by stage, free for every reader.
            </h2>
            <p className="mt-5 text-base text-ink/65 leading-relaxed">
              Stage&nbsp;I teaches the Hebrew-script Arabic alphabet. Stage&nbsp;II
              opens Saadia Gaon&apos;s Tafsir, verse by verse. Stage&nbsp;III
              brings the classical shelf — Bahya, Rambam, Halevi, Qirqisani.
              All three stages are free and open. Your support keeps them that way.
            </p>
          </div>
          {process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK && (
            <div className="mt-10 md:mt-0 md:shrink-0 flex flex-col items-start md:items-center gap-3">
              <a
                href={process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 rounded-sm bg-wine px-7 py-3.5 text-sm font-semibold text-parchment transition-colors hover:bg-wine-700"
              >
                Support the project
                <span aria-hidden>→</span>
              </a>
              <p className="text-xs text-muted">One-time or recurring · any amount</p>
            </div>
          )}
        </div>
      </section>

      {/* ── Returning-user rail ──────────────────────────────────────────── */}
      <div className="mx-auto max-w-5xl px-6 pb-16">
        <ReturningRail />
      </div>

    </div>
  );
}
