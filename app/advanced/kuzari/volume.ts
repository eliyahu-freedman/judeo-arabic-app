// Ordered table of contents for the full Kuzari (Kitāb al-Khazarī) volume.
// Each maqala's Judeo-Arabic text lives in data/kuzari-maqala-<N>.json
// (built by scripts/build_kuzari_gates.py). All five maqalat carry a full
// English translation with phrase-by-phrase hover highlighting.

import type { AlignedSegment } from "../reader";
import type { TermCard } from "@/lib/terms";

import maqala1 from "@/data/kuzari-maqala-1.json";
import maqala2 from "@/data/kuzari-maqala-2.json";
import maqala3 from "@/data/kuzari-maqala-3.json";
import maqala4 from "@/data/kuzari-maqala-4.json";
import maqala5 from "@/data/kuzari-maqala-5.json";

import maqala1english from "@/data/kuzari-maqala-1-english.json";
import maqala1aligned from "@/data/kuzari-maqala-1-aligned.json";
import maqala1terms from "@/data/kuzari-maqala-1-terms.json";

import maqala2english from "@/data/kuzari-maqala-2-english.json";
import maqala2aligned from "@/data/kuzari-maqala-2-aligned.json";

import maqala3english from "@/data/kuzari-maqala-3-english.json";
import maqala3aligned from "@/data/kuzari-maqala-3-aligned.json";

import maqala4english from "@/data/kuzari-maqala-4-english.json";
import maqala4aligned from "@/data/kuzari-maqala-4-aligned.json";

import maqala5english from "@/data/kuzari-maqala-5-english.json";
import maqala5aligned from "@/data/kuzari-maqala-5-aligned.json";

export type GatePage = { page_he: string; paragraphs?: string[] };
export type GateJson = {
  work: string;
  section: string;
  section_ja?: string;
  subtitle?: string;
  author: string;
  pages: GatePage[];
};

export type EnglishJson = { translator: string; paragraphs: string[] };
export type AlignedJson = { pages: Record<string, AlignedSegment[]> };

export type Gate = {
  /** URL segment, e.g. "maqala-1". */
  slug: string;
  json: GateJson;
  /** Present only for translated gates: drives the English column + hover. */
  english?: EnglishJson;
  aligned?: AlignedJson;
  /** Work-level philosophical term cards (maqala-1 only). */
  terms?: TermCard[];
};

export const KUZARI_GATES: Gate[] = [
  {
    slug: "maqala-1",
    json: maqala1 as GateJson,
    english: maqala1english as EnglishJson,
    aligned: maqala1aligned as AlignedJson,
    terms: maqala1terms as TermCard[],
  },
  {
    slug: "maqala-2",
    json: maqala2 as GateJson,
    english: maqala2english as EnglishJson,
    aligned: maqala2aligned as AlignedJson,
  },
  {
    slug: "maqala-3",
    json: maqala3 as GateJson,
    english: maqala3english as EnglishJson,
    aligned: maqala3aligned as AlignedJson,
  },
  {
    slug: "maqala-4",
    json: maqala4 as GateJson,
    english: maqala4english as EnglishJson,
    aligned: maqala4aligned as AlignedJson,
  },
  {
    slug: "maqala-5",
    json: maqala5 as GateJson,
    english: maqala5english as EnglishJson,
    aligned: maqala5aligned as AlignedJson,
  },
];

export const gateBySlug: Record<string, Gate> = Object.fromEntries(
  KUZARI_GATES.map((g) => [g.slug, g]),
);

export function gateIndex(slug: string): number {
  return KUZARI_GATES.findIndex((g) => g.slug === slug);
}
