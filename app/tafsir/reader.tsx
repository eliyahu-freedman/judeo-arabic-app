"use client";

import { useState } from "react";
import { lookup, tokenizeJa, type Entry } from "./lookup";

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
  const [activeToken, setActiveToken] = useState<string | null>(null);

  const activeEntries: Entry[] = activeToken ? lookup(activeToken) : [];

  return (
    <div className="max-w-3xl mx-auto px-6 py-8 pb-40">
      <header className="mb-6">
        <div className="text-xs uppercase tracking-widest text-stone-500">
          Stage 2 · Saadia on Bereshit 1
        </div>
        <h1 className="mt-1 font-serif text-3xl tracking-tight">
          Tafsir Reader
        </h1>
        <p className="mt-3 text-sm text-stone-600 leading-relaxed">
          Tap any Judeo-Arabic word for a starter gloss. Toggle the
          Arabic-script form, the Hebrew translation, and English (coming
          soon).
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
                <JaText
                  text={verse.ja}
                  activeToken={activeToken}
                  onTap={setActiveToken}
                />
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

      {activeToken && (
        <GlossPanel
          token={activeToken}
          entries={activeEntries}
          onClose={() => setActiveToken(null)}
        />
      )}
    </div>
  );
}

function JaText({
  text,
  activeToken,
  onTap,
}: {
  text: string;
  activeToken: string | null;
  onTap: (t: string) => void;
}) {
  const tokens = tokenizeJa(text);
  return (
    <>
      {tokens.map((t, i) => {
        if (t.kind === "sep") return <span key={i}>{t.text}</span>;
        const isActive = activeToken === t.text;
        return (
          <button
            key={i}
            type="button"
            onClick={() => onTap(t.text)}
            className={`inline cursor-pointer rounded-sm transition-colors px-0.5
              ${
                isActive
                  ? "bg-amber-200 text-amber-950"
                  : "hover:bg-amber-100"
              }`}
          >
            {t.text}
          </button>
        );
      })}
    </>
  );
}

function GlossPanel({
  token,
  entries,
  onClose,
}: {
  token: string;
  entries: Entry[];
  onClose: () => void;
}) {
  return (
    <div className="fixed bottom-0 inset-x-0 z-20 bg-white border-t border-stone-300 shadow-lg">
      <div className="max-w-3xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-baseline gap-3">
            <span className="font-serif text-2xl" dir="rtl">
              {token}
            </span>
            <span className="text-xs uppercase tracking-widest text-stone-500">
              Tapped word
            </span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-stone-500 hover:text-stone-900 text-lg leading-none"
            aria-label="Close"
          >
            ×
          </button>
        </div>
        {entries.length === 0 ? (
          <p className="text-sm text-stone-600 mt-2">
            No entry yet in the starter dictionary. (The full Blau lexicon
            will be wired in later — this prototype only covers high-frequency
            words.)
          </p>
        ) : (
          <ul className="space-y-3 mt-2">
            {entries.map((e) => (
              <li key={e.id} className="border-l-2 border-amber-300 pl-3">
                <div className="flex items-baseline gap-3 flex-wrap">
                  <span className="font-serif text-lg" dir="rtl">
                    {e.lemma_ja}
                  </span>
                  <span className="font-serif text-base text-stone-700" dir="rtl">
                    {e.lemma_ar}
                  </span>
                  <span className="text-xs text-stone-500 font-mono">
                    √{e.root}
                  </span>
                  <span className="text-xs text-stone-500 italic">{e.pos}</span>
                </div>
                <p className="text-sm text-stone-900 mt-1">{e.gloss_en}</p>
                <p className="text-sm text-stone-600 mt-0.5" dir="rtl">
                  {e.gloss_he}
                </p>
                {e.notes && (
                  <p className="text-xs text-stone-500 mt-1 leading-relaxed">
                    {e.notes}
                  </p>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>
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
