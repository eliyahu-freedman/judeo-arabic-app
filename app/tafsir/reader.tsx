"use client";

import { useState } from "react";

export type Verse = {
  ch: number;
  v: number;
  hebrew: string;
  ja: string;
  arabic: string;
  hebrew_translation: string;
};

export type TafsirData = {
  book: string;
  chapter: number;
  verses: Verse[];
};

export function TafsirReader({ data }: { data: TafsirData }) {
  const [showArabic, setShowArabic] = useState(false);
  const [showHebrewTr, setShowHebrewTr] = useState(false);
  const [showEnglish, setShowEnglish] = useState(false);

  return (
    <div className="max-w-3xl mx-auto px-6 py-8">
      <header className="mb-6">
        <div className="text-xs uppercase tracking-widest text-stone-500">
          Stage 2 · Saadia on Bereshit 1
        </div>
        <h1 className="mt-1 font-serif text-3xl tracking-tight">
          Tafsir Reader
        </h1>
        <p className="mt-3 text-sm text-stone-600 leading-relaxed">
          Read Saadia&apos;s Judeo-Arabic Tafsir verse-by-verse alongside the
          biblical Hebrew. Toggle the Arabic-script form, Hebrew translation,
          and English (coming soon).
        </p>
      </header>

      <div className="sticky top-0 z-10 bg-stone-50 -mx-6 px-6 py-3 border-y border-stone-200 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-xs uppercase tracking-widest text-stone-500 mr-1">
          Layers
        </span>
        <ToggleChip on disabled label="Hebrew" />
        <ToggleChip on disabled label="JA Tafsir" />
        <ToggleChip
          on={showArabic}
          onClick={() => setShowArabic((x) => !x)}
          label="Arabic script"
        />
        <ToggleChip
          on={showHebrewTr}
          onClick={() => setShowHebrewTr((x) => !x)}
          label="Hebrew translation"
        />
        <ToggleChip
          on={showEnglish}
          onClick={() => setShowEnglish((x) => !x)}
          label="English"
          disabled
          hint="coming soon"
        />
      </div>

      <ol className="mt-8 space-y-8">
        {data.verses.map((verse) => (
          <li
            key={verse.v}
            className="border-b border-stone-200 pb-6 last:border-0"
          >
            <div className="text-xs text-stone-500 mb-3 font-mono">
              {data.book} {data.chapter}:{verse.v}
            </div>
            <div dir="rtl" className="space-y-3">
              <p className="font-serif text-lg leading-relaxed text-stone-900">
                {verse.hebrew}
              </p>
              <p className="font-serif text-lg leading-relaxed text-amber-900 border-r-2 border-amber-200 pr-3">
                {verse.ja}
              </p>
              {showArabic && verse.arabic && (
                <p className="font-serif text-base leading-relaxed text-stone-700">
                  {verse.arabic}
                </p>
              )}
              {showHebrewTr && verse.hebrew_translation && (
                <p className="font-serif text-base leading-relaxed text-stone-600 italic">
                  {verse.hebrew_translation}
                </p>
              )}
            </div>
          </li>
        ))}
      </ol>
    </div>
  );
}

function ToggleChip({
  on,
  onClick,
  label,
  disabled,
  hint,
}: {
  on: boolean;
  onClick?: () => void;
  label: string;
  disabled?: boolean;
  hint?: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      title={hint}
      className={`px-3 py-1 rounded-full border text-xs transition-colors
        ${
          on
            ? "bg-stone-900 text-stone-50 border-stone-900"
            : "bg-white text-stone-700 border-stone-300"
        }
        ${disabled ? "opacity-50 cursor-not-allowed" : "hover:border-stone-500"}`}
    >
      {label}
      {hint && <span className="ml-1 text-[10px] opacity-70">({hint})</span>}
    </button>
  );
}
