"use client";

import Link from "next/link";
import { useState } from "react";
import { useProgress } from "@/lib/progress";

type LetterPiece = { ja: string; sound: string };
type Word = {
  ja: string;
  translit: string;
  en: string;
  letters: LetterPiece[];
  note?: string;
};
type Sentence = {
  ja: string;
  translit: string;
  en: string;
  ref: { book: string; ch: number; v: number };
};
export type FirstSentenceData = {
  id: string;
  title: string;
  intro: string;
  sentence: Sentence;
  words: Word[];
  finish: { href: string; label: string };
};

export function FirstSentenceDecoder({ data }: { data: FirstSentenceData }) {
  const { markLessonDone, touchStreak } = useProgress();
  const [index, setIndex] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const [finished, setFinished] = useState(false);

  const word = data.words[index];
  const isLast = index === data.words.length - 1;

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
          <Link href="/foundations" className="hover:text-wine">
            Foundations
          </Link>{" "}
          · lesson 5
        </p>
        <h1 className="text-4xl tracking-tight text-ink">{data.title}</h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed">
          {data.intro}
        </p>
      </header>

      {/* The whole sentence, with the current word highlighted */}
      <div className="rounded-md bg-page border border-ink/10 p-6 mb-8">
        <p
          dir="rtl"
          className="font-hebrew text-2xl sm:text-3xl text-ink leading-loose text-center"
        >
          {data.words.map((w, i) => (
            <span
              key={i}
              className={
                !finished && i === index
                  ? "rounded-sm bg-wine-100 text-wine-700 px-1.5 py-0.5 ring-1 ring-wine/25"
                  : finished
                    ? "text-ink"
                    : i < index
                      ? "text-ink/45"
                      : "text-ink/80"
              }
            >
              {w.ja}
              {i < data.words.length - 1 ? " " : ""}
            </span>
          ))}
        </p>
      </div>

      {finished ? (
        <div className="rounded-md bg-parchment border border-ink/10 p-10 text-center">
          <p className="text-3xl tracking-tight text-ink">
            You just read your first sentence.
          </p>
          <p className="mt-4 font-mono text-sm text-muted">
            {data.sentence.translit}
          </p>
          <p className="mt-3 text-lg italic text-ink leading-relaxed">
            &ldquo;{data.sentence.en}&rdquo;
          </p>
          <p className="mt-5 text-ink/70 leading-relaxed">
            That was Saadia&apos;s own Arabic — {data.sentence.ref.book}{" "}
            {data.sentence.ref.ch}:{data.sentence.ref.v}, decoded letter by
            letter. The on-ramp does the same thing across a
            whole passage; then the full Tafsir is just more of what you can
            already do.
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
              Word {index + 1} of {data.words.length}
            </span>
            <span>
              {data.sentence.ref.book} {data.sentence.ref.ch}:
              {data.sentence.ref.v}
            </span>
          </div>
          <div className="h-1 rounded-full bg-ink/10 overflow-hidden mb-8">
            <div
              className="h-full bg-wine transition-all"
              style={{ width: `${((index + 1) / data.words.length) * 100}%` }}
            />
          </div>

          <div className="rounded-md bg-page border border-ink/10 p-8">
            <p
              dir="rtl"
              className="font-hebrew text-5xl sm:text-6xl text-ink leading-none text-center"
            >
              {word.ja}
            </p>

            {/* Letter-by-letter breakdown */}
            <div className="mt-8 flex flex-wrap gap-2 justify-center" dir="rtl">
              {word.letters.map((p, i) => (
                <span
                  key={i}
                  className="inline-flex flex-col items-center rounded-md border border-ink/10 bg-parchment px-3 py-2 min-w-[3rem]"
                >
                  <span className="font-hebrew text-2xl text-ink leading-none">
                    {p.ja}
                  </span>
                  <span dir="ltr" className="mt-1.5 text-[12px] font-mono text-muted">
                    {p.sound}
                  </span>
                </span>
              ))}
            </div>

            {revealed && (
              <div className="mt-7 pt-5 border-t border-ink/10 text-center">
                <p className="font-mono text-sm text-muted">{word.translit}</p>
                <p dir="ltr" className="mt-1 text-xl text-ink">
                  {word.en}
                </p>
                {word.note && (
                  <p className="mt-3 text-[13px] text-ink/70 italic leading-relaxed max-w-md mx-auto">
                    {word.note}
                  </p>
                )}
              </div>
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
                  {isLast ? "Finish" : "Next word →"}
                </button>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
}
