// Ordered table of contents for the full Bahya (Ḥovot ha-Levavot) volume.
// Each gate's Judeo-Arabic text lives in data/bahya-<file>.json (built by
// scripts/build_bahya_gates.py). Bab 1 additionally has a hand-built English
// translation + phrase alignment; every other gate ships JA-only with
// tap-to-define. Both the volume contents page and the [gate] reader route
// drive off this single list so labels and ordering never drift.

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

export type GatePage = { page_he: string; paragraphs?: string[] };
export type GateJson = {
  work: string;
  section: string;
  section_ja?: string;
  subtitle?: string;
  author: string;
  pages: GatePage[];
};

export type Gate = {
  /** URL segment, e.g. "hakdamah" or "bab-1". */
  slug: string;
  json: GateJson;
};

export const BAHYA_GATES: Gate[] = [
  { slug: "hakdamah", json: hakdamah as GateJson },
  { slug: "bab-1", json: bab1 as GateJson },
  { slug: "bab-2", json: bab2 as GateJson },
  { slug: "bab-3", json: bab3 as GateJson },
  { slug: "bab-4", json: bab4 as GateJson },
  { slug: "bab-5", json: bab5 as GateJson },
  { slug: "bab-6", json: bab6 as GateJson },
  { slug: "bab-7", json: bab7 as GateJson },
  { slug: "bab-8", json: bab8 as GateJson },
  { slug: "bab-9", json: bab9 as GateJson },
  { slug: "bab-10", json: bab10 as GateJson },
];

export const gateBySlug: Record<string, Gate> = Object.fromEntries(
  BAHYA_GATES.map((g) => [g.slug, g]),
);

export function gateIndex(slug: string): number {
  return BAHYA_GATES.findIndex((g) => g.slug === slug);
}
