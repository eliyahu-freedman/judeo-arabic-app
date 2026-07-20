import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import {
  AdvancedReader,
  type WorkData,
  type WorkPage,
  type AlignedSegment,
} from "../../reader";
import {
  QIRQISANI_GATES,
  gateBySlug,
  gateIndex,
  type QGate,
} from "../chapters";

// ── Static params ─────────────────────────────────────────────────────────────
export function generateStaticParams() {
  return QIRQISANI_GATES.map((g) => ({ bab: g.slug }));
}

// ── Shared JSON types (matches data/ file schemas) ────────────────────────────
type GatePage = { page_he: string; paragraphs?: string[] };
type GateJson = {
  work: string;
  section: string;
  section_ja?: string;
  subtitle?: string;
  author: string;
  script?: "arabic" | "hebrew";
  pages: GatePage[];
};
type EnglishJson = { translator: string; paragraphs: string[] };
type HebrewJson = { translator: string; paragraphs: string[] };
type AlignedJson = { pages: Record<string, AlignedSegment[]> };

// ── WorkData builders ─────────────────────────────────────────────────────────
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
    script: json.script ?? "arabic",
    pages,
  };
}

function buildJaOnly(json: GateJson): WorkData {
  return {
    work: json.work,
    section: json.section,
    subtitle: json.subtitle ?? "",
    author: json.author,
    english_translator: "",
    script: "arabic",
    intro: `${json.section} — in the original Judeo-Arabic of Yaʿqūb al-Qirqisānī (10th c.). Tap any word for a dictionary gloss. (English translation forthcoming.)`,
    pages: json.pages.map((p) => ({
      page_he: p.page_he,
      paragraphs: p.paragraphs,
    })),
  };
}

// ── Data loading ─────────────────────────────────────────────────────────────
async function loadGate(
  slug: string,
): Promise<{ data: WorkData; tibbon?: string[] }> {
  // M1 Bab 1: hand-authored legacy JSON with inline aligned + terms
  if (slug === "m1-bab-1") {
    const mod = await import("@/data/qirqisani-anwar-maqala1.json");
    return { data: { ...(mod.default as unknown as WorkData), workId: "qirqisani" } };
  }

  // M1 Babs 2-19: bilingual (Arabic base + English + Hebrew)
  const m1 = slug.match(/^m1-bab-(\d+)$/);
  if (m1) {
    const n = parseInt(m1[1], 10);
    const padded = String(n).padStart(2, "0");
    const [gateMod, enMod, alignedMod, heMod] = await Promise.all([
      import(`@/data/qirqisani-m1-bab${padded}.json`),
      import(`@/data/qirqisani-m1-bab${padded}-english.json`),
      import(`@/data/qirqisani-m1-bab${padded}-aligned.json`),
      import(`@/data/qirqisani-m1-bab${padded}-hebrew.json`),
    ]);
    const gate = gateMod.default as GateJson;
    const english = enMod.default as EnglishJson;
    const aligned = alignedMod.default as AlignedJson;
    const hebrew = heMod.default as HebrewJson;
    const data = english.paragraphs.length > 0
      ? buildAligned(gate, english, aligned)
      : buildJaOnly(gate);
    return { data, tibbon: hebrew.paragraphs };
  }

  // M2 Babs 1-28: bilingual (JA Hebrew-script base + English + Hebrew)
  const m2 = slug.match(/^m2-bab-(\d+)$/);
  if (m2) {
    const n = parseInt(m2[1], 10);
    const padded = String(n).padStart(2, "0");
    const [gateMod, enMod, alignedMod, heMod] = await Promise.all([
      import(`@/data/qirqisani-m2-bab${padded}.json`),
      import(`@/data/qirqisani-m2-bab${padded}-english.json`),
      import(`@/data/qirqisani-m2-bab${padded}-aligned.json`),
      import(`@/data/qirqisani-m2-bab${padded}-hebrew.json`),
    ]);
    const gate = gateMod.default as GateJson;
    const english = enMod.default as EnglishJson;
    const aligned = alignedMod.default as AlignedJson;
    const hebrew = heMod.default as HebrewJson;
    const data = english.paragraphs.length > 0
      ? buildAligned(gate, english, aligned)
      : buildJaOnly(gate);
    return { data, tibbon: hebrew.paragraphs };
  }

  // M3 Babs 1-25: bilingual (Arabic base + English, no Hebrew)
  const m3 = slug.match(/^m3-bab-(\d+)$/);
  if (m3) {
    const n = parseInt(m3[1], 10);
    const padded = String(n).padStart(2, "0");
    const [gateMod, enMod, alignedMod] = await Promise.all([
      import(`@/data/qirqisani-m3-bab${padded}.json`),
      import(`@/data/qirqisani-m3-bab${padded}-english.json`),
      import(`@/data/qirqisani-m3-bab${padded}-aligned.json`),
    ]);
    const gate = gateMod.default as GateJson;
    const english = enMod.default as EnglishJson;
    const aligned = alignedMod.default as AlignedJson;
    const data = english.paragraphs.length > 0
      ? buildAligned(gate, english, aligned)
      : buildJaOnly(gate);
    return { data };
  }

  // M5 Sha'arim 1-40: bilingual from Nemoy trilingual source
  const m5 = slug.match(/^m5-sha-(\d+)$/);
  if (m5) {
    const n = parseInt(m5[1], 10);
    const padded = String(n).padStart(2, "0");
    const [gateMod, enMod, alignedMod] = await Promise.all([
      import(`@/data/qirqisani-m5-sha${padded}.json`),
      import(`@/data/qirqisani-m5-sha${padded}-english.json`),
      import(`@/data/qirqisani-m5-sha${padded}-aligned.json`),
    ]);
    // sha'ar 18 has no paragraphs — fall back to JA-only
    const gate = gateMod.default as GateJson;
    const english = enMod.default as EnglishJson;
    const aligned = alignedMod.default as AlignedJson;
    const data = english.paragraphs.length === 0
      ? buildJaOnly(gate)
      : buildAligned(gate, english, aligned);
    return { data };
  }

  notFound();
}

// ── Metadata ──────────────────────────────────────────────────────────────────
export async function generateMetadata({
  params,
}: {
  params: Promise<{ bab: string }>;
}): Promise<Metadata> {
  const { bab } = await params;
  const g = gateBySlug[bab];
  if (!g) return {};
  return {
    title: `Qirqisānī, Kitāb al-Anwār — ${g.section} in Judeo-Arabic`,
    description: `${g.section} of Yaʿqūb al-Qirqisānī's Kitāb al-Anwār (10th c.) in the original Judeo-Arabic.`,
    alternates: { canonical: `/advanced/qirqisani-anwar/${bab}` },
  };
}

// ── Page component ────────────────────────────────────────────────────────────
export default async function QirqisaniGatePage({
  params,
}: {
  params: Promise<{ bab: string }>;
}) {
  const { bab } = await params;
  const g = gateBySlug[bab];
  if (!g) notFound();

  let data: WorkData;
  let tibbon: string[] | undefined;
  try {
    ({ data, tibbon } = await loadGate(bab));
  } catch {
    notFound();
  }

  const idx = gateIndex(bab);
  const prev = idx > 0 ? QIRQISANI_GATES[idx - 1] : null;
  const next = idx < QIRQISANI_GATES.length - 1 ? QIRQISANI_GATES[idx + 1] : null;

  return (
    <>
      <AdvancedReader data={data!} tibbon={tibbon} tibbonLabel="Hebrew Translation" />
      <nav className="max-w-3xl mx-auto px-6 pb-24 -mt-28 flex items-center justify-between gap-4 text-sm">
        {prev ? (
          <Link
            href={`/advanced/qirqisani-anwar/${prev.slug}`}
            className="text-wine hover:underline"
          >
            ← {prev.section}
          </Link>
        ) : (
          <span />
        )}
        <Link
          href="/advanced/qirqisani-anwar"
          className="text-muted hover:text-ink"
        >
          All gates
        </Link>
        {next ? (
          <Link
            href={`/advanced/qirqisani-anwar/${next.slug}`}
            className="text-wine hover:underline text-right"
          >
            {next.section} →
          </Link>
        ) : (
          <span />
        )}
      </nav>
    </>
  );
}
