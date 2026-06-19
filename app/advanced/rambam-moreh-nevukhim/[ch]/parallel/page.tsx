import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getMorehChapterText } from "@/lib/morehTerms";
import { MOREH_BASE, MOREH_CHAPTERS, morehHref } from "../../chapters";
import tibbon from "@/data/moreh-tibbon.json";

const TIBBON = (tibbon as { chapters: Record<string, string[]> }).chapters;

export function generateStaticParams() {
  return MOREH_CHAPTERS.map((c) => ({ ch: String(c.n) }));
}

type Props = { params: Promise<{ ch: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { ch } = await params;
  const n = Number(ch);
  const meta = MOREH_CHAPTERS.find((c) => c.n === n);
  const title = meta ? meta.title : `Guide I:${ch}`;
  return {
    title: `${title} — Arabic & Ibn Tibbon side by side`,
    description:
      "Maimonides' Judeo-Arabic original of this chapter of the Guide beside Ibn Tibbon's classical Hebrew translation — the source next to the translation that shaped its entire Hebrew reception.",
    alternates: { canonical: `${MOREH_BASE}/${ch}/parallel` },
  };
}

export default async function ParallelPage({ params }: Props) {
  const { ch } = await params;
  const n = Number(ch);
  const meta = MOREH_CHAPTERS.find((c) => c.n === n);
  const chapter = getMorehChapterText(n);
  const tibbonSegs = TIBBON[String(n)] ?? [];
  if (!meta || !chapter) notFound();

  return (
    <div className="max-w-5xl mx-auto px-6 py-12 sm:py-16">
      <header className="mb-8">
        <p className="label mb-2">{meta.title} · parallel</p>
        <h1 className="display text-3xl text-ink">
          The original <span className="text-wine italic">beside</span> the translation.
        </h1>
        <p className="mt-4 max-w-2xl text-sm text-ink/70 leading-relaxed">
          Maimonides wrote the Guide in Judeo-Arabic; it entered the Jewish
          canon through Samuel Ibn Tibbon&apos;s Hebrew. Here the source sits
          beside that translation. Alignment is by chapter, not yet phrase by
          phrase. (Al-Ḥarizi&apos;s rival Hebrew will join when its text is in hand.)
        </p>
        <p className="mt-4 flex flex-wrap gap-x-4 gap-y-1 text-sm">
          <Link href={morehHref(meta.slug)} className="text-wine hover:underline underline-offset-2">
            ← Read with translation & glosses
          </Link>
          <a
            href={`https://moreh.alhatorah.org/1/${n}`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-wine hover:underline underline-offset-2"
          >
            Commentators on AlHaTorah ↗
          </a>
        </p>
      </header>

      <div className="grid gap-8 md:grid-cols-2">
        <section>
          <h2 className="text-[10px] uppercase tracking-[0.3em] text-muted mb-3 pb-1 border-b border-ink/10">
            Judeo-Arabic original
          </h2>
          <div dir="rtl" className="font-hebrew text-lg leading-loose text-ink/90 space-y-3">
            {chapter.segments.map((s, i) => (
              <p key={i}>{s.ja}</p>
            ))}
          </div>
        </section>

        <section>
          <h2 className="text-[10px] uppercase tracking-[0.3em] text-muted mb-3 pb-1 border-b border-ink/10">
            Ibn Tibbon · Hebrew{" "}
            <span className="normal-case tracking-normal text-ink/40">(public domain, via Sefaria)</span>
          </h2>
          {tibbonSegs.length > 0 ? (
            <div dir="rtl" className="font-hebrew text-lg leading-loose text-ink/90 space-y-3">
              {tibbonSegs.map((s, i) => (
                <p key={i}>{s}</p>
              ))}
            </div>
          ) : (
            <p className="text-sm text-muted italic">Ibn Tibbon text not available for this chapter.</p>
          )}
        </section>
      </div>

      <section className="mt-10">
        <h2 className="text-[10px] uppercase tracking-[0.3em] text-muted mb-3 pb-1 border-b border-ink/10">
          Working English
        </h2>
        <div className="text-[15px] leading-relaxed text-ink/80 space-y-2 max-w-2xl">
          {chapter.segments.map((s, i) => (
            <p key={i}>{s.en}</p>
          ))}
        </div>
      </section>
    </div>
  );
}
