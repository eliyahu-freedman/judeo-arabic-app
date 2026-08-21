"use client";

import Link from "next/link";

const STAGES = [
  {
    numeral: "I",
    eyebrow: "Start here",
    href: "/foundations",
    title: "Foundations",
    cta: "Begin →",
    tilt: "rotate-[1.2deg]",
    visual: (
      <div className="flex flex-col items-center justify-center flex-1 gap-5">
        <div className="flex items-center gap-5">
          <span className="font-hebrew text-7xl text-ink leading-none">כ</span>
          <span className="text-xl text-ink/25">→</span>
          <div className="flex flex-col items-center gap-1">
            <span className="font-arabic text-6xl text-ink leading-none" dir="rtl">
              خ
            </span>
            <span className="text-[10px] uppercase tracking-[0.2em] text-muted">
              kh
            </span>
          </div>
        </div>
        <div className="w-full border-t border-ink/10 pt-4 text-center">
          <p
            dir="rtl"
            className="font-hebrew text-xl leading-loose text-ink/70"
          >
            כ׳לק · אלשמס · ואלארץ׳
          </p>
          <p className="mt-1 text-[11px] text-muted">Hebrew script · Arabic sounds</p>
        </div>
      </div>
    ),
  },
  {
    numeral: "II",
    eyebrow: "Saadia on the Torah",
    href: "/tafsir",
    title: "Tafsir Reader",
    cta: "Open the reader →",
    tilt: "",
    visual: (
      <div className="flex flex-col justify-center flex-1 gap-4">
        <div
          dir="rtl"
          className="font-hebrew text-2xl leading-loose text-ink text-right"
        >
          אול מא כ׳לק אללה
        </div>
        <div
          dir="rtl"
          className="font-hebrew text-base leading-loose text-ink/55 text-right"
        >
          אלסמאואת ואלארץ׳
        </div>
        <div className="border-t border-ink/10 pt-4">
          <p
            dir="rtl"
            className="font-hebrew text-sm text-muted text-right leading-loose"
          >
            בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
          </p>
          <p className="mt-2 text-[11px] text-muted">
            Tap any word · verse-by-verse gloss
          </p>
        </div>
      </div>
    ),
  },
  {
    numeral: "III",
    eyebrow: "Classical prose",
    href: "/advanced",
    title: "The Library",
    cta: "Browse the library →",
    tilt: "rotate-[-1.2deg]",
    visual: (
      <div className="flex flex-col justify-center flex-1 gap-3">
        <div
          dir="rtl"
          className="font-hebrew text-lg leading-loose text-ink text-right"
        >
          כתאב אלהדאיה אלי פראיץ׳ אלקלוב
        </div>
        <div
          dir="rtl"
          className="font-hebrew text-base leading-loose text-ink/55 text-right"
        >
          דלאלה אלחאירין
        </div>
        <div
          dir="rtl"
          className="font-hebrew text-base leading-loose text-ink/40 text-right"
        >
          כתאב אלאמאנאת ואלאעתקאדאת
        </div>
        <div className="border-t border-ink/10 pt-3">
          <p className="text-[11px] text-muted">
            Bahya · Rambam · Halevi · Saadia
          </p>
        </div>
      </div>
    ),
  },
];

export function StageStrip() {
  return (
    <section
      className="overflow-hidden py-16 sm:py-20"
      aria-label="Three-stage curriculum"
    >
      <div className="flex gap-5 px-6 overflow-x-auto sm:overflow-visible sm:justify-center pb-4 sm:pb-0">
        {STAGES.map((s) => (
          <Link
            key={s.numeral}
            href={s.href}
            className={`
              group shrink-0 w-64 sm:w-72 flex flex-col
              rounded-2xl bg-page border border-ink/10
              p-6 shadow-sm
              transition-all duration-300
              hover:-translate-y-2 hover:shadow-[0_16px_32px_-8px_rgba(114,47,55,0.18)] hover:border-wine/30
              ${s.tilt}
            `}
            style={{ minHeight: 380 }}
          >
            {/* Header */}
            <div className="flex items-baseline justify-between mb-6">
              <span className="text-6xl font-light text-wine/20 leading-none transition-colors group-hover:text-wine/45">
                {s.numeral}
              </span>
              <span className="label">{s.eyebrow}</span>
            </div>

            {/* Visual content */}
            {s.visual}

            {/* Footer */}
            <div className="mt-6 border-t border-ink/10 pt-4 flex items-end justify-between">
              <h3 className="text-base font-semibold text-ink group-hover:text-wine transition-colors">
                {s.title}
              </h3>
              <span className="label label-accent text-[10px] opacity-0 group-hover:opacity-100 transition-opacity">
                {s.cta}
              </span>
            </div>
          </Link>
        ))}
      </div>
    </section>
  );
}
