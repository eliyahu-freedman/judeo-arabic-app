// Ordered table of contents for the full Bahya (Ḥovot ha-Levavot) volume.
// Each gate's Judeo-Arabic text lives in data/bahya-<file>.json (built by
// scripts/build_bahya_gates.py). A gate that also has an English translation +
// phrase alignment (bab-1, bab-2 …) carries `english` + `aligned` here and the
// reader renders the English column with hover highlighting; gates without them
// ship JA-only with tap-to-define. Both the volume contents page and the [gate]
// reader route drive off this single list so labels and ordering never drift.

import type { AlignedSegment } from "../reader";

import hakdamah from "@/data/bahya-hakdamah.json";
import bab1 from "@/data/bahya-bab1.json";
import bab2 from "@/data/bahya-bab2.json";
import bab3 from "@/data/bahya-bab3.json";
import bab4 from "@/data/bahya-bab4.json";
import bab5 from "@/data/bahya-bab5.json";
import bab6 from "@/data/bahya-bab6.json";
import bab7 from "@/data/bahya-bab7.json";
import bab8 from "@/data/bahya-bab8.json";
import bab9 from "@/data/bahya-bab9.json";
import bab10 from "@/data/bahya-bab10.json";

// Per-gate English + phrase alignment (only for translated gates).
import bab1english from "@/data/bahya-bab1-english.json";
import bab1aligned from "@/data/bahya-bab1-aligned.json";
import bab2english from "@/data/bahya-bab2-english.json";
import bab2aligned from "@/data/bahya-bab2-aligned.json";
import bab3english from "@/data/bahya-bab3-english.json";
import bab3aligned from "@/data/bahya-bab3-aligned.json";
import bab4english from "@/data/bahya-bab4-english.json";
import bab4aligned from "@/data/bahya-bab4-aligned.json";
import bab5english from "@/data/bahya-bab5-english.json";
import bab5aligned from "@/data/bahya-bab5-aligned.json";
import bab6english from "@/data/bahya-bab6-english.json";
import bab6aligned from "@/data/bahya-bab6-aligned.json";
import hakdamahenglish from "@/data/bahya-hakdamah-english.json";
import hakdamahaligned from "@/data/bahya-hakdamah-aligned.json";
import bab7english from "@/data/bahya-bab7-english.json";
import bab7aligned from "@/data/bahya-bab7-aligned.json";
import bab8english from "@/data/bahya-bab8-english.json";
import bab8aligned from "@/data/bahya-bab8-aligned.json";
import bab9english from "@/data/bahya-bab9-english.json";
import bab9aligned from "@/data/bahya-bab9-aligned.json";
import bab10english from "@/data/bahya-bab10-english.json";
import bab10aligned from "@/data/bahya-bab10-aligned.json";

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
  /** URL segment, e.g. "hakdamah" or "bab-1". */
  slug: string;
  json: GateJson;
  /** Present only for translated gates: drives the English column + hover. */
  english?: EnglishJson;
  aligned?: AlignedJson;
};

export const BAHYA_GATES: Gate[] = [
  {
    slug: "hakdamah",
    json: hakdamah as GateJson,
    english: hakdamahenglish as EnglishJson,
    aligned: hakdamahaligned as AlignedJson,
  },
  {
    slug: "bab-1",
    json: bab1 as GateJson,
    english: bab1english as EnglishJson,
    aligned: bab1aligned as AlignedJson,
  },
  {
    slug: "bab-2",
    json: bab2 as GateJson,
    english: bab2english as EnglishJson,
    aligned: bab2aligned as AlignedJson,
  },
  {
    slug: "bab-3",
    json: bab3 as GateJson,
    english: bab3english as EnglishJson,
    aligned: bab3aligned as AlignedJson,
  },
  {
    slug: "bab-4",
    json: bab4 as GateJson,
    english: bab4english as EnglishJson,
    aligned: bab4aligned as AlignedJson,
  },
  {
    slug: "bab-5",
    json: bab5 as GateJson,
    english: bab5english as EnglishJson,
    aligned: bab5aligned as AlignedJson,
  },
  {
    slug: "bab-6",
    json: bab6 as GateJson,
    english: bab6english as EnglishJson,
    aligned: bab6aligned as AlignedJson,
  },
  {
    slug: "bab-7",
    json: bab7 as GateJson,
    english: bab7english as EnglishJson,
    aligned: bab7aligned as AlignedJson,
  },
  {
    slug: "bab-8",
    json: bab8 as GateJson,
    english: bab8english as EnglishJson,
    aligned: bab8aligned as AlignedJson,
  },
  {
    slug: "bab-9",
    json: bab9 as GateJson,
    english: bab9english as EnglishJson,
    aligned: bab9aligned as AlignedJson,
  },
  {
    slug: "bab-10",
    json: bab10 as GateJson,
    english: bab10english as EnglishJson,
    aligned: bab10aligned as AlignedJson,
  },
];

export const gateBySlug: Record<string, Gate> = Object.fromEntries(
  BAHYA_GATES.map((g) => [g.slug, g]),
);

export function gateIndex(slug: string): number {
  return BAHYA_GATES.findIndex((g) => g.slug === slug);
}
