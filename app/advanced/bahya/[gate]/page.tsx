import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import enData from "@/data/bahya-bab1-english.json";
import alignedData from "@/data/bahya-bab1-aligned.json";
import {
  AdvancedReader,
  type AlignedSegment,
  type WorkData,
  type WorkPage,
} from "../../reader";
import { BAHYA_GATES, gateBySlug, gateIndex } from "../volume";

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

/** Bab 1 ships a hand-built English translation + phrase alignment. Splice it
 *  onto the JA pages exactly as the original single-gate route did. */
function buildBab1(json: (typeof BAHYA_GATES)[number]["json"]): WorkData {
  const enPar = enData.paragraphs;
  const nJa = json.pages.length;
  const nEn = enPar.length;
  const alignedByPage = alignedData.pages as Record<string, AlignedSegment[]>;
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
    english_translator: enData.translator,
    pages,
  };
}

/** Every other gate is JA-only: full text + tap-to-define, no English layer. */
function buildJaOnly(json: (typeof BAHYA_GATES)[number]["json"]): WorkData {
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

  const data = gate === "bab-1" ? buildBab1(g.json) : buildJaOnly(g.json);

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
