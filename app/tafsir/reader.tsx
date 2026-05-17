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
    <div className="max-w-3xl mx-auto px-6 py-10 pb-44">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 2 · Saadia on Bereshit 1
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          Tafsir <span className="text-wine italic">Reader</span>
        </h1>
        <p className="mt-4 text-base text-ink/70 leading-relaxed max-w-xl">
          Tap any Judeo-Arabic word for a starter gloss. Toggle the
          Arabic-script form, the Hebrew translation, and English (coming
          soon).
        </p>
      </header>

      <div className="sticky top-0 z-10 bg-parchment/90 backdrop-blur supports-[backdrop-filter]:bg-parchment/70 -mx-6 px-6 py-3 border-y border-ink/10 flex flex-wrap items-center gap-2 text-sm">
        <span className="text-[10px] uppercase tracking-[0.25em] text-muted mr-1">
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
          hint="soon"
        />
      </div>

      <ol className="mt-10 space-y-6">
        {data.verses.map((verse) => (
          <li
            key={verse.v}
            className="rounded-md bg-page border border-ink/10 p-7"
          >
            <div className="text-[11px] uppercase tracking-[0.25em] text-muted mb-5">
              {data.book} {data.chapter}:{verse.v}
            </div>
            <div dir="rtl" className="space-y-5">
              <p className="font-hebrew text-2xl text-ink leading-loose">
                {verse.hebrew}
              </p>
              <div className="border-r-2 border-wine/60 pr-5">
                <p className="font-hebrew ja-text text-xl text-ink/90 leading-loose">
                  <JaText
                    text={verse.ja}
                    activeToken={activeToken}
                    onTap={setActiveToken}
                  />
                </p>
              </div>
              {showArabic && verse.arabic && (
                <p className="font-arabic text-xl text-ink/75 leading-loose">
                  {verse.arabic}
                </p>
              )}
              {showHebrewTr && verse.hebrew_translation && (
                <p className="font-hebrew text-lg text-muted italic leading-loose">
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
            className={`inline cursor-pointer rounded-sm transition-colors px-0.5 -mx-0.5
              ${
                isActive
                  ? "bg-wine-100 text-wine-700"
                  : "hover:bg-wine-50"
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
    <div className="fixed bottom-0 inset-x-0 z-20 bg-page border-t border-wine/20 shadow-[0_-8px_24px_-12px_rgba(114,47,55,0.2)]">
      <div className="max-w-3xl mx-auto px-6 py-5">
        <div className="flex items-center justify-between mb-3">
          <div className="flex items-baseline gap-4">
            <span className="font-hebrew text-3xl text-ink" dir="rtl">
              {token}
            </span>
            <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
              Tapped word
            </span>
          </div>
          <button
            type="button"
            onClick={onClose}
            className="text-ink/40 hover:text-wine text-2xl leading-none w-8 h-8 flex items-center justify-center rounded-full hover:bg-wine-50 transition-colors"
            aria-label="Close"
          >
            ×
          </button>
        </div>
        {entries.length === 0 ? (
          <p className="text-sm text-muted mt-2 italic">
            No entry yet in the starter dictionary. (The full Blau lexicon
            will be wired in later — this prototype covers high-frequency
            words.)
          </p>
        ) : (
          <ul className="space-y-4 mt-2">
            {entries.map((e) => (
              <li key={e.id} className="border-l-2 border-wine/40 pl-4">
                <div className="flex items-baseline gap-3 flex-wrap">
                  <span className="font-hebrew text-xl text-ink" dir="rtl">
                    {e.lemma_ja}
                  </span>
                  <span className="font-arabic text-lg text-ink/70" dir="rtl">
                    {e.lemma_ar}
                  </span>
                  <span className="text-xs text-muted font-mono">
                    √{e.root}
                  </span>
                  <span className="text-xs text-muted italic">{e.pos}</span>
                </div>
                <p className="text-[15px] text-ink mt-1.5">{e.gloss_en}</p>
                <p
                  className="font-hebrew text-base text-muted mt-0.5"
                  dir="rtl"
                >
                  {e.gloss_he}
                </p>
                {e.notes && (
                  <p className="text-[13px] text-muted mt-2 leading-relaxed italic">
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
      className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all
        ${
          on
            ? "bg-wine text-page border-wine"
            : "bg-page text-ink/70 border-ink/15"
        }
        ${
          disabled
            ? "opacity-40 cursor-not-allowed"
            : "hover:border-wine/50 hover:text-wine"
        }`}
    >
      {label}
      {hint && <span className="ml-1 opacity-70">({hint})</span>}
    </button>
  );
}
