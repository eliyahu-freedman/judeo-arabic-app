"use client";

import Link from "next/link";
import { useState } from "react";

export type AramaicCognateEntry = {
  rank: number;
  aramaic: string;
  aramaic_translit: string;
  aramaic_en: string;
  hebrew: string;
  hebrew_translit: string;
  arabic: string;
  arabic_translit: string;
  group: string;
  story: string;
  onkelos_ref: string | null;
  onkelos_phrase: string | null;
  onkelos_phrase_en: string | null;
  tafsir_count?: number;
  tafsir_n_verses?: number;
  tafsir_key?: string;
  tafsir_first?: {
    book_slug: string;
    book: string;
    ch: number;
    v: number;
    surface: string;
    ja_phrase?: string;
    hebrew_phrase?: string;
  };
};

const GROUP_ORDER = ["interdentals", "religious", "daily", "talmudic"] as const;
type Group = (typeof GROUP_ORDER)[number];

const GROUP_LABEL: Record<Group, string> = {
  interdentals: "The consonants Hebrew dropped",
  religious: "Onkelos' religious vocabulary",
  daily: "Onkelos' everyday vocabulary",
  talmudic: "Beyond Onkelos · Talmudic Aramaic",
};

const GROUP_HINT: Record<Group, string> = {
  interdentals:
    "Eight words where Aramaic and Arabic preserve a consonant Hebrew lost. *ṯ → Hebrew ש, Aramaic ת, Arabic ث. *ḏ → Hebrew ז, Aramaic d, Arabic ذ. Same root, three different paths — and Hebrew is the outlier. These are the cognates only Aramaic can teach you.",
  religious:
    "The vocabulary of prayer, scripture, judgment, and the sages. Most are three-way cognates — same root in Hebrew, Aramaic, and Arabic. Every one of these appears in Onkelos.",
  daily:
    "House, hand, head, eye, river, wine — the words you'd hear in a Galilean kitchen and a Damascene one. Onkelos uses every one of them.",
  talmudic:
    "Words that come into Aramaic after Onkelos — the legal and commercial vocabulary of the Talmud and the Geonic responsa. Onkelos doesn't have these, but the medieval Judeo-Arabic reader meets them everywhere.",
};

export function AramaicCognateCards({
  entries,
}: {
  entries: AramaicCognateEntry[];
}) {
  const [filter, setFilter] = useState<Group | "all">("all");
  const groups = GROUP_ORDER.filter((g) => entries.some((e) => e.group === g));

  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · Aramaic cognates
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          If you know <span className="text-wine italic">Onkelos</span>…
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          …you already know most of these. The Aramaic of the Targum is the
          bridge to Arabic. Where Hebrew shifted its consonants — שלש, זהב,
          זכר — Aramaic and Arabic agreed: תלת/ثلاث, דהב/ذهب, דכר/ذكر. Every
          card shows all three languages, the Onkelos verse where the Aramaic
          word appears, and (where Saadia uses it) a link straight to the
          Tafsir.
        </p>
      </header>

      <div className="flex flex-wrap gap-2 mb-8 text-sm">
        <FilterPill
          on={filter === "all"}
          label={`All ${entries.length}`}
          onClick={() => setFilter("all")}
        />
        {groups.map((g) => (
          <FilterPill
            key={g}
            on={filter === g}
            label={GROUP_LABEL[g]}
            onClick={() => setFilter(g)}
          />
        ))}
      </div>

      {groups.map((g) => {
        if (filter !== "all" && filter !== g) return null;
        const groupEntries = entries.filter((e) => e.group === g);
        return (
          <section key={g} className="mb-12 last:mb-0">
            <h2 className="text-xs uppercase tracking-[0.25em] text-muted mb-2">
              {GROUP_LABEL[g]}
            </h2>
            <p className="text-[13px] text-ink/65 leading-relaxed max-w-xl mb-5 italic">
              {GROUP_HINT[g]}
            </p>
            <ol className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {groupEntries.map((e) => (
                <AramaicCard key={e.rank} entry={e} />
              ))}
            </ol>
          </section>
        );
      })}
    </div>
  );
}

function AramaicCard({ entry }: { entry: AramaicCognateEntry }) {
  const isInterdental = entry.group === "interdentals";
  const isTalmudic = entry.group === "talmudic";

  return (
    <li className="group rounded-md bg-page border border-ink/10 p-5 hover:border-wine/30 transition-colors flex flex-col">
      <div className="flex items-start justify-between mb-3 gap-3">
        <span className="text-[10px] font-mono text-muted">
          #{String(entry.rank).padStart(2, "0")}
        </span>
        <span
          className={`text-[10px] uppercase tracking-[0.2em] ${
            isTalmudic ? "text-muted" : "text-wine/70"
          }`}
        >
          {isTalmudic ? "post-Onkelos" : "in Onkelos"}
        </span>
      </div>

      <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
        Aramaic
      </div>
      <div dir="rtl" className="font-hebrew text-3xl text-ink leading-tight">
        {entry.aramaic}
      </div>
      <div className="text-[13px] text-ink/55 mt-1 font-mono">
        {entry.aramaic_translit} · {entry.aramaic_en}
      </div>

      <div className="my-4 border-t border-ink/10" />

      <div className="grid grid-cols-2 gap-4">
        <div>
          <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
            Arabic{isInterdental && <span className="text-wine"> ✓</span>}
          </div>
          <div
            dir="rtl"
            className="font-arabic text-2xl text-ink/85 leading-tight"
          >
            {entry.arabic}
          </div>
          <div className="text-[12px] text-ink/55 mt-1 font-mono">
            {entry.arabic_translit}
          </div>
        </div>
        <div>
          <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
            Hebrew
            {isInterdental && (
              <span className="text-ink/40"> · shifted</span>
            )}
          </div>
          <div
            dir="rtl"
            className={`font-hebrew text-2xl leading-tight ${
              isInterdental ? "text-ink/60" : "text-ink/85"
            }`}
          >
            {entry.hebrew}
          </div>
          <div className="text-[12px] text-ink/55 mt-1 font-mono">
            {entry.hebrew_translit}
          </div>
        </div>
      </div>

      {entry.story && (
        <p className="mt-4 text-[13px] text-ink/70 leading-relaxed">
          {entry.story}
        </p>
      )}

      {entry.onkelos_ref && entry.onkelos_phrase && (
        <div className="mt-4 pt-3 border-t border-ink/10">
          <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1">
            Onkelos · {entry.onkelos_ref}
          </div>
          <div
            dir="rtl"
            className="font-hebrew text-lg text-ink/80 leading-snug mt-1"
          >
            {entry.onkelos_phrase}
          </div>
          {entry.onkelos_phrase_en && (
            <div className="text-[12px] text-ink/55 italic mt-1">
              &ldquo;{entry.onkelos_phrase_en}&rdquo;
            </div>
          )}
        </div>
      )}

      {entry.tafsir_first && (
        <div className="mt-3 pt-3 border-t border-ink/10">
          <div className="text-[10px] uppercase tracking-[0.2em] text-muted mb-1 flex items-baseline justify-between gap-2">
            <span>
              Saadia&apos;s Tafsir · {entry.tafsir_first.book}{" "}
              {entry.tafsir_first.ch}:{entry.tafsir_first.v}
            </span>
            {entry.tafsir_count && entry.tafsir_count > 0 && (
              <span
                className="font-mono"
                title={`${entry.tafsir_count} occurrences across ${entry.tafsir_n_verses ?? "?"} verses`}
              >
                {entry.tafsir_count}× · {entry.tafsir_n_verses}v
              </span>
            )}
          </div>
          {entry.tafsir_first.ja_phrase && (
            <div
              dir="rtl"
              className="font-hebrew text-lg text-ink/80 leading-snug mt-1"
            >
              {entry.tafsir_first.ja_phrase}
            </div>
          )}
          {entry.tafsir_first.hebrew_phrase && (
            <div
              dir="rtl"
              className="font-hebrew text-sm text-ink/50 leading-snug mt-1 italic"
              title="The Hebrew Torah verse Saadia is translating"
            >
              {entry.tafsir_first.hebrew_phrase}
            </div>
          )}
          <Link
            href={`/tafsir/${entry.tafsir_first.book_slug}/${entry.tafsir_first.ch}#verse-${entry.tafsir_first.ch}-${entry.tafsir_first.v}`}
            className="mt-2 inline-flex items-baseline gap-1.5 text-[12px] text-wine hover:underline"
          >
            <span>See in the Tafsir</span>
            <span aria-hidden>→</span>
          </Link>
        </div>
      )}
    </li>
  );
}

function FilterPill({
  on,
  label,
  onClick,
}: {
  on: boolean;
  label: string;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={`px-3 py-1 rounded-full border text-xs uppercase tracking-wider transition-all ${
        on
          ? "bg-wine text-page border-wine"
          : "bg-page text-ink/70 border-ink/15 hover:border-wine/50 hover:text-wine"
      }`}
    >
      {label}
    </button>
  );
}
