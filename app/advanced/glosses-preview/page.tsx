import type { Metadata } from "next";
import alignedData from "@/data/bahya-bab1-aligned.json";
import glossesData from "@/data/bahya-bab1-glosses.json";

export const metadata: Metadata = {
  title: "Bahya glosses — preview (page מד)",
  description: "Interlinear preview of contextual per-token glosses for Bahya, Shaʿar ha-Yiḥud, page מד.",
  robots: { index: false, follow: false },
};

type AlignedSegment = {
  ja: string;
  he?: string;
  en: string;
  isHeader?: boolean;
};

type Token = {
  token: string;
  norm: string;
  ar: string;
  root: string;
  pos: string;
  gloss_en: string;
  gloss_he: string;
  note: string;
};

type SegmentGlosses = {
  segment: number;
  tokens: Token[];
};

const PAGE = "מד";

export default function GlossesPreviewPage() {
  const segments = (alignedData.pages as Record<string, AlignedSegment[]>)[PAGE] ?? [];
  const pageGlosses = (glossesData.pages as Record<string, SegmentGlosses[]>)[PAGE] ?? [];
  const glossesBySeg = new Map(pageGlosses.map((s) => [s.segment, s.tokens]));

  const totalTokens = pageGlosses.reduce((n, s) => n + s.tokens.length, 0);

  return (
    <div className="max-w-5xl mx-auto px-6 py-10 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Preview · not indexed
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          Bahya glosses — page <span className="font-hebrew text-wine">{PAGE}</span>
        </h1>
        <p className="mt-3 text-base text-ink/70 leading-relaxed max-w-3xl">
          Sanity-check view for the contextual per-token glosses generated from
          JA + Ibn Tibbon Hebrew + English. Each JA word is shown above its
          English and Hebrew gloss in interlinear form. Below each segment:
          Ibn Tibbon&apos;s full Hebrew (the gold standard) and the English.
        </p>
        <p className="mt-2 text-sm text-muted">
          {segments.length} segments · {totalTokens} tokens glossed · source:
          {" "}<code className="text-xs">data/bahya-bab1-glosses.json</code>
        </p>
        <p className="mt-1 text-sm">
          <a href="/advanced" className="text-wine underline hover:no-underline">
            ← back to /advanced
          </a>
        </p>
      </header>

      <article className="space-y-12">
        {segments.map((seg, segIdx) => {
          const tokens = glossesBySeg.get(segIdx) ?? [];
          return (
            <section
              key={segIdx}
              className="rounded-md bg-page border border-ink/10 p-7"
            >
              <div className="flex items-baseline justify-between mb-5">
                <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
                  Segment {segIdx}
                  {seg.isHeader && (
                    <span className="ml-2 text-wine">· header</span>
                  )}
                </span>
                <span className="text-[10px] uppercase tracking-[0.3em] text-muted">
                  {tokens.length} tokens
                </span>
              </div>

              {/* Interlinear JA / EN / HE */}
              <div dir="rtl" className="mb-6">
                <div className="flex flex-wrap items-start gap-x-5 gap-y-6">
                  {tokens.map((t, i) => (
                    <TokenStack key={i} t={t} />
                  ))}
                </div>
              </div>

              {/* Ibn Tibbon Hebrew translation */}
              <div className="pt-5 border-t border-ink/10">
                <p className="text-[10px] uppercase tracking-[0.25em] text-muted mb-2">
                  Ibn Tibbon (gold standard for context)
                </p>
                <p
                  dir="rtl"
                  className="font-hebrew text-lg text-ink/80 italic leading-loose"
                >
                  {seg.he}
                </p>
              </div>

              {/* English translation */}
              <div className="pt-4 mt-3">
                <p className="text-[10px] uppercase tracking-[0.25em] text-muted mb-2">
                  English
                </p>
                <p
                  dir="ltr"
                  className="text-[15px] text-ink/80 leading-relaxed"
                >
                  {seg.en}
                </p>
              </div>

              {/* Notes table: tokens with non-empty notes */}
              {tokens.some((t) => t.note) && (
                <div className="pt-5 mt-5 border-t border-ink/10">
                  <p className="text-[10px] uppercase tracking-[0.25em] text-muted mb-3">
                    Notes
                  </p>
                  <ul className="space-y-2 text-sm text-ink/75">
                    {tokens
                      .map((t, i) => ({ t, i }))
                      .filter(({ t }) => t.note)
                      .map(({ t, i }) => (
                        <li key={i} className="flex gap-3 items-baseline">
                          <span
                            dir="rtl"
                            className="font-hebrew text-base text-ink min-w-[5rem]"
                          >
                            {t.token}
                          </span>
                          <span className="text-muted">{t.note}</span>
                        </li>
                      ))}
                  </ul>
                </div>
              )}
            </section>
          );
        })}
      </article>
    </div>
  );
}

function TokenStack({ t }: { t: Token }) {
  const isFormula = t.pos === "formula" || t.pos === "proper";
  return (
    <div className="flex flex-col items-center text-center min-w-[5rem]">
      <span
        dir="rtl"
        className={`font-hebrew text-2xl leading-tight ${
          isFormula ? "text-wine/80" : "text-ink"
        }`}
      >
        {t.token}
      </span>
      <span
        dir="ltr"
        className="mt-1 text-[12px] text-ink/85 leading-snug max-w-[10rem]"
      >
        {t.gloss_en}
      </span>
      <span
        dir="rtl"
        className="mt-0.5 font-hebrew text-[13px] text-muted leading-snug max-w-[10rem]"
      >
        {t.gloss_he}
      </span>
      {t.ar && !isFormula && (
        <span
          dir="rtl"
          className="mt-1 font-arabic text-[12px] text-ink/40 leading-tight"
        >
          {t.ar}
        </span>
      )}
    </div>
  );
}
