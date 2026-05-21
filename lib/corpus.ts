"use client";

import { useEffect, useState } from "react";
import { normalizeToken } from "./lookup";

export type Occurrence = { ch: number; v: number; surface: string };

export type CorpusEntry = {
  /** Total number of token instances. */
  count: number;
  /** Every occurrence, in document order. May contain duplicates per (ch,v). */
  occurrences: Occurrence[];
};

/** On-disk shape: surfaces deduped per key, occurrences as [ch, v, sIdx].
 * Typed as number[] because TS widens JSON-imported tuples to plain arrays. */
type RawEntry = {
  count: number;
  surfaces: string[];
  occurrences: number[][];
};

type RawIndex = {
  corpora: string[];
  total_tokens: number;
  unique_keys: number;
  tokens: Record<string, RawEntry>;
};

export type Corpus = {
  label: string;
  totalTokens: number;
  getOccurrences: (rawToken: string) => CorpusEntry | null;
};

const PENTATEUCH = ["Bereshit", "Shemot", "Vayikra", "Bamidbar", "Devarim"];

function makeLabel(corpora: string[]): string {
  if (corpora.length === 0) return "(empty corpus)";
  const booksSeen = new Set(corpora.map((c) => c.split(" ")[0]));
  if (PENTATEUCH.every((b) => booksSeen.has(b))) return "the Pentateuch";
  if (booksSeen.size > 1) {
    return [...booksSeen]
      .sort((a, b) => PENTATEUCH.indexOf(a) - PENTATEUCH.indexOf(b))
      .join(", ");
  }
  const book = corpora[0].split(" ")[0];
  const chapters = corpora
    .map((c) => Number(c.split(" ")[1]))
    .filter((n) => Number.isFinite(n))
    .sort((a, b) => a - b);
  if (chapters.length === 1) return `${book} ${chapters[0]}`;
  return `${book} ${chapters[0]}–${chapters[chapters.length - 1]}`;
}

function buildCorpus(raw: RawIndex): Corpus {
  const label = makeLabel(raw.corpora);
  return {
    label,
    totalTokens: raw.total_tokens,
    getOccurrences(rawToken: string) {
      const key = normalizeToken(rawToken);
      if (!key) return null;
      const entry = raw.tokens[key];
      if (!entry) return null;
      return {
        count: entry.count,
        occurrences: entry.occurrences.map((o) => ({
          ch: o[0],
          v: o[1],
          surface: entry.surfaces[o[2]] ?? "",
        })),
      };
    },
  };
}

// Module-level singleton — the index is large (~1.6 MB) so we cache the
// fetch promise to avoid re-downloading across hook callers.
let _corpusPromise: Promise<Corpus> | null = null;

function loadCorpus(): Promise<Corpus> {
  if (_corpusPromise) return _corpusPromise;
  _corpusPromise = fetch("/corpus-index.json", { cache: "force-cache" })
    .then((r) => {
      if (!r.ok) throw new Error(`corpus-index fetch failed: ${r.status}`);
      return r.json() as Promise<RawIndex>;
    })
    .then(buildCorpus)
    .catch((err) => {
      // Clear the cached promise so a later mount can retry.
      _corpusPromise = null;
      throw err;
    });
  return _corpusPromise;
}

/** Hook: returns the loaded Corpus, or null while it's still fetching. */
export function useCorpus(): Corpus | null {
  const [corpus, setCorpus] = useState<Corpus | null>(null);
  useEffect(() => {
    let alive = true;
    loadCorpus().then((c) => {
      if (alive) setCorpus(c);
    });
    return () => {
      alive = false;
    };
  }, []);
  return corpus;
}

/** Unique (ch, v) refs from a list of occurrences, in first-seen order. */
export function uniqueVerses(
  occurrences: Occurrence[],
): { ch: number; v: number }[] {
  const seen = new Set<string>();
  const out: { ch: number; v: number }[] = [];
  for (const o of occurrences) {
    const k = `${o.ch}:${o.v}`;
    if (seen.has(k)) continue;
    seen.add(k);
    out.push({ ch: o.ch, v: o.v });
  }
  return out;
}

/** Group occurrences by surface form, return as [{surface, count}], desc. */
export function variantBreakdown(
  occurrences: Occurrence[],
): { surface: string; count: number }[] {
  const counts = new Map<string, number>();
  for (const o of occurrences) {
    counts.set(o.surface, (counts.get(o.surface) ?? 0) + 1);
  }
  return [...counts.entries()]
    .map(([surface, count]) => ({ surface, count }))
    .sort((a, b) => b.count - a.count);
}
