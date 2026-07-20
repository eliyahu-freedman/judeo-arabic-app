import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import {
  AdvancedReader,
  type WorkData,
  type WorkPage,
} from "../../reader";
import {
  KUZARI_GATES,
  gateBySlug,
  gateIndex,
  type AlignedJson,
  type EnglishJson,
  type GateJson,
} from "../volume";
import type { TermCard } from "@/lib/terms";

export function generateStaticParams() {
  return KUZARI_GATES.map((g) => ({ gate: g.slug }));
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
    title: `Kuzari — ${section} in Judeo-Arabic`,
    description: subtitle
      ? `${section} (${subtitle}) of Yehuda HaLevi's Kuzari in its original 12th-century Judeo-Arabic, with tap-to-define dictionary on every word.`
      : `${section} of Yehuda HaLevi's Kuzari in its original 12th-century Judeo-Arabic, with tap-to-define dictionary on every word.`,
    alternates: { canonical: `/advanced/kuzari/${gate}` },
  };
}

/** A translated gate: splice English + aligned segments onto the JA pages.
 *  Only pages that have an entry in aligned.pages get hover highlighting;
 *  the rest render JA-only (no English column, no hover). */
function buildAligned(
  json: GateJson,
  english: EnglishJson,
  aligned: AlignedJson,
  terms?: TermCard[],
): WorkData {
  const alignedByPage = aligned.pages;
  const alignedPageCount = Object.keys(alignedByPage).length;
  const partialCoverage = alignedPageCount < json.pages.length;

  const pages: WorkPage[] = json.pages.map((p) => ({
    page_he: p.page_he,
    paragraphs: p.paragraphs,
    aligned: alignedByPage[p.page_he],
  }));

  const intro = partialCoverage
    ? `${json.section} of ${json.work} in its original 12th-century Judeo-Arabic. The opening pages carry a working English translation by ${english.translator} with phrase-by-phrase hover highlighting; the rest of the maqala is Judeo-Arabic with tap-to-define. (English translation in progress.)`
    : undefined;

  return {
    work: json.work,
    section: json.section,
    subtitle: json.subtitle ?? "",
    author: json.author,
    english_translator: english.translator,
    intro,
    terms,
    pages,
  };
}

/** JA-only gate: full text + tap-to-define, no English layer. */
function buildJaOnly(json: GateJson): WorkData {
  return {
    work: json.work,
    section: json.section,
    subtitle: json.subtitle ?? "",
    author: json.author,
    english_translator: "",
    intro: `${json.section}${
      json.subtitle ? ` — ${json.subtitle}` : ""
    } — in the original 12th-century Judeo-Arabic. Tap any word for a dictionary gloss. (English translation forthcoming.)`,
    pages: json.pages.map((p) => ({
      page_he: p.page_he,
      paragraphs: p.paragraphs,
    })),
  };
}

export default async function KuzariGatePage({
  params,
}: {
  params: Promise<{ gate: string }>;
}) {
  const { gate } = await params;
  const g = gateBySlug[gate];
  if (!g) notFound();

  const data =
    g.english && g.aligned
      ? buildAligned(g.json, g.english, g.aligned, g.terms)
      : buildJaOnly(g.json);

  const idx = gateIndex(gate);
  const prev = idx > 0 ? KUZARI_GATES[idx - 1] : null;
  const next = idx < KUZARI_GATES.length - 1 ? KUZARI_GATES[idx + 1] : null;

  return (
    <>
      <AdvancedReader data={data} />
      <nav className="max-w-3xl mx-auto px-6 pb-24 -mt-28 flex items-center justify-between gap-4 text-sm">
        {prev ? (
          <Link
            href={`/advanced/kuzari/${prev.slug}`}
            className="text-wine hover:underline"
          >
            ← {prev.json.section}
          </Link>
        ) : (
          <span />
        )}
        <Link href="/advanced/kuzari" className="text-muted hover:text-ink">
          All maqalat
        </Link>
        {next ? (
          <Link
            href={`/advanced/kuzari/${next.slug}`}
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
