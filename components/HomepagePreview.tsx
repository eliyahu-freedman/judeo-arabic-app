"use client";

import Link from "next/link";
import { useState, useEffect } from "react";

type Tab = "foundations" | "tafsir" | "library";

const TABS: { id: Tab; label: string }[] = [
  { id: "foundations", label: "I · Foundations" },
  { id: "tafsir", label: "II · Tafsir" },
  { id: "library", label: "III · Library" },
];

export function HomepagePreview() {
  const [active, setActive] = useState<Tab>("tafsir");
  const [paused, setPaused] = useState(false);

  useEffect(() => {
    if (paused) return;
    const id = setInterval(() => {
      setActive((prev) => {
        const i = TABS.findIndex((t) => t.id === prev);
        return TABS[(i + 1) % TABS.length].id;
      });
    }, 5000);
    return () => clearInterval(id);
  }, [paused]);

  function choose(tab: Tab) {
    setPaused(true);
    setActive(tab);
  }

  return (
    <section className="mx-auto max-w-5xl border-y border-ink/10 px-6 py-16 sm:py-20">
      {/* Tab bar */}
      <div className="mb-10 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div className="flex gap-0 border-b border-ink/10">
          {TABS.map((tab) => (
            <button
              key={tab.id}
              onClick={() => choose(tab.id)}
              className={`-mb-px border-b-2 px-4 py-2.5 text-sm font-medium transition-colors ${
                active === tab.id
                  ? "border-wine text-wine"
                  : "border-transparent text-ink/50 hover:text-ink"
              }`}
            >
              {tab.label}
            </button>
          ))}
        </div>
        <p className="text-sm italic text-muted">
          {active === "tafsir"
            ? "↓ tap the highlighted word for a gloss example"
            : active === "foundations"
              ? "The script unlocks in a single session"
              : "Every word carries a tap-to-define gloss"}
        </p>
      </div>

      {active === "foundations" && <FoundationsPanel />}
      {active === "tafsir" && <TafsirPanel />}
      {active === "library" && <LibraryPanel />}
    </section>
  );
}

function FoundationsPanel() {
  return (
    <div className="grid gap-10 md:grid-cols-2">
      <div>
        <div className="rounded-sm border border-ink/10 bg-page p-6 sm:p-8 shadow-sm shadow-wine/5">
          <p className="mb-5 text-xs uppercase tracking-[0.25em] text-muted">
            The first thing you learn
          </p>
          <div className="flex items-center gap-6">
            <span className="font-hebrew text-7xl text-ink leading-none">כ</span>
            <span className="text-2xl text-ink/25">→</span>
            <div>
              <span className="font-arabic text-5xl text-ink leading-none" dir="rtl">
                خ
              </span>
              <p className="mt-1 text-xs text-muted">kh · خاء</p>
            </div>
          </div>
          <div className="mt-6 border-t border-ink/10 pt-5">
            <p className="mb-3 text-xs text-muted">With the diacritic mark:</p>
            <div className="flex items-baseline gap-4">
              <span className="font-hebrew text-3xl text-wine">כ׳לק</span>
              <span className="text-ink/40">→</span>
              <span className="font-arabic text-2xl text-ink/80" dir="rtl">
                خَلَقَ
              </span>
              <span className="text-sm italic text-ink/60">he created</span>
            </div>
          </div>
          <div className="mt-6 border-t border-ink/10 pt-5 text-sm text-ink/60 leading-relaxed">
            The diacritic{" "}
            <span className="font-hebrew not-italic">׳</span> after{" "}
            <span className="font-hebrew not-italic">כ</span> marks the Arabic
            sound{" "}
            <span className="font-arabic" dir="rtl">
              خ
            </span>{" "}
            (kh). A handful of diacritics covers the whole Arabic alphabet.
          </div>
        </div>
      </div>

      <div className="flex flex-col justify-between">
        <div>
          <p className="mb-3 label label-accent">Stage I · Foundations</p>
          <p className="text-xl sm:text-2xl italic leading-relaxed">
            &ldquo;Every Hebrew reader already half-knows this script.&rdquo;
          </p>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-ink/70">
            The same letters you read in Torah cover most of the Arabic
            alphabet — Saadia writes in Hebrew script. A handful of diacritics
            mark the new sounds, one article (אל) stands in for &ldquo;the,&rdquo; and
            the top-fifty vocabulary words unlock the narrative. No prior Arabic
            required.
          </p>
        </div>
        <Link
          href="/foundations"
          className="label label-accent group mt-8 inline-flex items-center gap-2 self-start border-b border-wine/30 pb-1 hover:border-wine"
        >
          Begin Foundations
          <span aria-hidden className="transition-transform group-hover:translate-x-1">
            →
          </span>
        </Link>
      </div>
    </div>
  );
}

function TafsirPanel() {
  return (
    <div className="grid gap-10 md:grid-cols-2">
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
              <span className="label">Gloss</span>
              <div className="text-right">
                <div className="font-hebrew text-xl" dir="rtl">
                  כ׳לק
                </div>
                <div className="mt-0.5 font-arabic text-base text-muted" dir="rtl">
                  خلق
                </div>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-y-4 text-sm">
              <div>
                <span className="mb-1 block label">Root</span>
                <span className="font-mono">√ḫ-l-q</span>
              </div>
              <div>
                <span className="mb-1 block label">Part of Speech</span>
                <span className="italic">verb · perf. 3sg.m.</span>
              </div>
              <div>
                <span className="mb-1 block label">English</span>
                <span>he created</span>
              </div>
              <div>
                <span className="mb-1 block label">Hebrew</span>
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

      <div className="flex flex-col justify-between">
        <div>
          <p className="mb-3 label label-accent">Stage II · Tafsir</p>
          <p className="text-xl sm:text-2xl italic leading-relaxed">
            &ldquo;The first thing God created: the heavens and the earth.&rdquo;
          </p>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-ink/70">
            Saadia begins not with a calque of Hebrew{" "}
            <span className="font-hebrew" dir="rtl">
              בראשית
            </span>
            , but with an Arabic construction —{" "}
            <span className="font-hebrew" dir="rtl">
              אול מא כ׳לק
            </span>{" "}
            — that resolves the verse&apos;s syntactic ambiguity in the act of
            translating it. Tap any word to look it up; hover a phrase to see
            all three columns light up together.
          </p>
        </div>
        <Link
          href="/tafsir/bereshit/1#verse-1-1"
          className="label label-accent group mt-8 inline-flex items-center gap-2 self-start border-b border-wine/30 pb-1 hover:border-wine"
        >
          Open in the reader
          <span aria-hidden className="transition-transform group-hover:translate-x-1">
            →
          </span>
        </Link>
      </div>
    </div>
  );
}

function LibraryPanel() {
  return (
    <div className="grid gap-10 md:grid-cols-2">
      <div>
        <div className="rounded-sm border border-ink/10 bg-page p-6 sm:p-8 shadow-sm shadow-wine/5">
          <p
            dir="rtl"
            className="font-hebrew text-right text-2xl sm:text-3xl leading-loose"
          >
            <span className="rounded-sm bg-wine-100 text-wine-700 px-1.5 py-0.5 ring-1 ring-wine/25">
              כתאב
            </span>
            <span> אלהדאיה אלי פראיץ׳ אלקלוב</span>
          </p>

          <div className="mt-8 border-l-2 border-wine bg-parchment/60 p-5">
            <div className="mb-4 flex items-start justify-between gap-4">
              <span className="label">Gloss</span>
              <div className="text-right">
                <div className="font-hebrew text-xl" dir="rtl">
                  כתאב
                </div>
                <div className="mt-0.5 font-arabic text-base text-muted" dir="rtl">
                  كِتَاب
                </div>
              </div>
            </div>
            <div className="grid grid-cols-2 gap-y-4 text-sm">
              <div>
                <span className="mb-1 block label">Root</span>
                <span className="font-mono">√k-t-b</span>
              </div>
              <div>
                <span className="mb-1 block label">Part of Speech</span>
                <span className="italic">noun · masc.</span>
              </div>
              <div className="col-span-2">
                <span className="mb-1 block label">English</span>
                <span>book; a written work; scripture</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="flex flex-col justify-between">
        <div>
          <p className="mb-3 label label-accent">Stage III · The Library</p>
          <p className="text-xl sm:text-2xl italic leading-relaxed">
            &ldquo;The Book of Guidance to the Duties of the Hearts.&rdquo;
          </p>
          <p className="mt-1 text-sm text-muted">
            Baḥya ibn Paquda · Andalusia, 11th century
          </p>
          <p className="mt-6 max-w-md text-sm leading-relaxed text-ink/70">
            Bahya&apos;s complete Chovot HaLevavot in its original Judeo-Arabic
            — the introduction and all ten gates — alongside parallel Hebrew and
            English, with a tap-to-define gloss on every word. Also live:
            Rambam&apos;s Moreh Nevukhim, Halevi&apos;s Kuzari, Saadia&apos;s
            Emunot v&apos;Deot, and Qirqisani&apos;s Anwar.
          </p>
        </div>
        <Link
          href="/advanced"
          className="label label-accent group mt-8 inline-flex items-center gap-2 self-start border-b border-wine/30 pb-1 hover:border-wine"
        >
          Browse the Library
          <span aria-hidden className="transition-transform group-hover:translate-x-1">
            →
          </span>
        </Link>
      </div>
    </div>
  );
}
