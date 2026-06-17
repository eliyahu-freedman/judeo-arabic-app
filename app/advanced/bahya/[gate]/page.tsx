import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import {
  AdvancedReader,
  type WorkData,
  type WorkPage,
} from "../../reader";
import {
  BAHYA_GATES,
  gateBySlug,
  gateIndex,
  type AlignedJson,
  type EnglishJson,
  type GateJson,
} from "../volume";

export function generateStaticParams() {
  return BAHYA_GATES.map((g) => ({ gate: g.slug }));
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ gate: string }>;
}): Promise<Metadata> {
  const { gate } = await params;
  const g = gateBySlug[gate];
  if (!g) return {};
  const { section, subtitle } = g.json;
  return {
    title: `Bahya, Chovot HaLevavot — ${section} in Judeo-Arabic`,
    description:
      subtitle
        ? `${section} (${subtitle}) of Bahya ibn Paquda's Chovot HaLevavot in its original 11th-century Judeo-Arabic, with tap-to-define dictionary on every word.`
        : `${section} of Bahya ibn Paquda's Chovot HaLevavot in its original 11th-century Judeo-Arabic, with tap-to-define dictionary on every word.`,
    alternates: { canonical: `/advanced/bahya/${gate}` },
  };
}

/** A translated gate ships an English translation + phrase alignment. Splice
 *  them onto the JA pages: English ratio-sliced across pages (fallback for any
 *  non-aligned region), aligned segments attached by Hebrew page number. */
function buildAligned(
  json: GateJson,
  english: EnglishJson,
  aligned: AlignedJson,
): WorkData {
  const enPar = english.paragraphs;
  const nJa = json.pages.length;
  const nEn = enPar.length;
  const alignedByPage = aligned.pages;
  const pages: WorkPage[] = json.pages.map((p, i) => {
    const enStart = Math.floor((nEn * i) / nJa);
    const enEnd = Math.floor((nEn * (i + 1)) / nJa);
    return {
      page_he: p.page_he,
      paragraphs: p.paragraphs,
      english_paragraphs: enPar.slice(enStart, enEnd),
      aligned: alignedByPage[p.page_he],
    };
  });
  return {
    work: json.work,
    section: json.section,
    subtitle: json.subtitle ?? "",
    author: json.author,
    english_translator: english.translator,
    pages,
  };
}

/** Every other gate is JA-only: full text + tap-to-define, no English layer. */
function buildJaOnly(json: GateJson): WorkData {
  return {
    work: json.work,
    section: json.section,
    subtitle: json.subtitle ?? "",
    author: json.author,
    english_translator: "",
    intro: `${json.work} — ${json.section}${
      json.subtitle ? ` (${json.subtitle})` : ""
    } — in the original 11th-century Judeo-Arabic. Tap any word for a dictionary gloss. (English translation forthcoming.)`,
    pages: json.pages.map((p) => ({
      page_he: p.page_he,
      paragraphs: p.paragraphs,
    })),
  };
}

export default async function BahyaGatePage({
  params,
}: {
  params: Promise<{ gate: string }>;
}) {
  const { gate } = await params;
  const g = gateBySlug[gate];
  if (!g) notFound();

  const data =
    g.english && g.aligned
      ? buildAligned(g.json, g.english, g.aligned)
      : buildJaOnly(g.json);

  const idx = gateIndex(gate);
  const prev = idx > 0 ? BAHYA_GATES[idx - 1] : null;
  const next = idx < BAHYA_GATES.length - 1 ? BAHYA_GATES[idx + 1] : null;

  return (
    <>
      <AdvancedReader data={data} />
      <nav className="max-w-3xl mx-auto px-6 pb-24 -mt-28 flex items-center justify-between gap-4 text-sm">
        {prev ? (
          <Link
            href={`/advanced/bahya/${prev.slug}`}
            className="text-wine hover:underline"
          >
            ← {prev.json.section}
          </Link>
        ) : (
          <span />
        )}
        <Link href="/advanced/bahya" className="text-muted hover:text-ink">
          All gates
        </Link>
        {next ? (
          <Link
            href={`/advanced/bahya/${next.slug}`}
            className="text-wine hover:underline text-right"
          >
            {next.json.section} →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </>
  );
}
