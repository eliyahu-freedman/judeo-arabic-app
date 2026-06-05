"use client";

import Link from "next/link";
import { useState } from "react";
import { useProgress } from "@/lib/progress";

type Word = { ja: string; en: string };
type Step = {
  ja: string;
  translit: string;
  en: string;
  words: Word[];
  ref: { book: string; ch: number; v: number };
};
export type OnRampData = {
  id: string;
  title: string;
  intro: string;
  steps: Step[];
  finish: { href: string; label: string };
};

export function OnRamp({ data }: { data: OnRampData }) {
  const { markLessonDone, touchStreak } = useProgress();
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [finished, setFinished] = useState(false);

  const step = data.steps[index];
  const isLast = index === data.steps.length - 1;

  const advance = () => {
    if (isLast) {
      markLessonDone(data.id);
      touchStreak();
      setFinished(true);
      return;
    }
    setIndex((i) => i + 1);
    setRevealed(false);
  };

  return (
    <div className="max-w-2xl mx-auto px-6 py-16 pb-28">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · on-ramp
        </p>
        <h1 className="text-4xl tracking-tight text-ink">{data.title}</h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed">
          {data.intro}
        </p>
      </header>

      {finished ? (
        <div className="rounded-md bg-parchment border border-ink/10 p-10 text-center">
          <p className="text-3xl tracking-tight text-ink">
            You just read the first day.
          </p>
          <p className="mt-3 text-ink/70 leading-relaxed">
            That was Saadia&apos;s own Arabic, not a textbook. The full chapter
            works exactly the same way — tap any word for its meaning.
          </p>
          <div className="mt-8 flex gap-3 justify-center flex-wrap">
            <Link
              href={data.finish.href}
              className="px-5 py-2.5 rounded-full bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine-700 transition-colors"
            >
              {data.finish.label} →
            </Link>
            <Link
              href="/review"
              className="px-5 py-2.5 rounded-full border border-ink/15 text-ink/70 text-sm uppercase tracking-wider hover:border-wine/50 hover:text-wine transition-colors"
            >
              Review your words
            </Link>
          </div>
        </div>
      ) : (
        <>
          <div className="flex justify-between text-[10px] uppercase tracking-[0.25em] text-muted mb-3">
            <span>
              Step {index + 1} of {data.steps.length}
            </span>
            <span>
              {step.ref.book} {step.ref.ch}:{step.ref.v}
            </span>
          </div>
          <div className="h-1 rounded-full bg-ink/10 overflow-hidden mb-8">
            <div
              className="h-full bg-wine transition-all"
              style={{ width: `${((index + 1) / data.steps.length) * 100}%` }}
            />
          </div>

          <div className="rounded-md bg-page border border-ink/10 p-8">
            <p
              dir="rtl"
              className="font-hebrew text-3xl sm:text-4xl text-ink leading-snug text-center"
            >
              {step.ja}
            </p>
            <p className="mt-2 text-center text-[13px] font-mono text-muted">
              {step.translit}
            </p>

            <div className="mt-7 flex flex-wrap gap-2 justify-center" dir="rtl">
              {step.words.map((w, i) => (
                <span
                  key={i}
                  className="inline-flex flex-col items-center rounded-md border border-ink/10 bg-parchment px-3 py-2"
                >
                  <span className="font-hebrew text-xl text-ink">{w.ja}</span>
                  {revealed && (
                    <span dir="ltr" className="mt-1 text-[12px] text-ink/70">
                      {w.en}
                    </span>
                  )}
                </span>
              ))}
            </div>

            {revealed && (
              <p
                dir="ltr"
                className="mt-7 pt-5 border-t border-ink/10 text-center text-lg text-ink"
              >
                {step.en}
              </p>
            )}

            <div className="mt-8 flex gap-3">
              {!revealed ? (
                <button
                  type="button"
                  onClick={() => setRevealed(true)}
                  className="flex-1 px-4 py-3 rounded-md bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine-700 transition-colors"
                >
                  Show meaning
                </button>
              ) : (
                <button
                  type="button"
                  onClick={advance}
                  className="flex-1 px-4 py-3 rounded-md bg-wine text-page text-sm uppercase tracking-wider hover:bg-wine-700 transition-colors"
                >
                  {isLast ? "Finish" : "Next clause →"}
                </button>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}
