#!/usr/bin/env npx tsx
/**
 * stdin→stdout CLI that resolves each Judeo-Arabic word in a string through the
 * EXACT runtime resolver (`lookup` from lib/lookup.ts) and reports what the
 * reader would show (hits[0]) plus how many homograph hits exist.
 *
 * Exists so the Python dictionary-audit tooling sees precisely what a reader
 * sees on tap, without re-implementing lookup/candidate-chain (no drift).
 *
 * Protocol: one JSON object per stdin line, `{ "text": "..." }`.
 *   For each line, write one JSONL array of per-WORD records (sep tokens
 *   dropped), each:
 *     { surface, n_hits, entry: null | { id, lemma_ja, lemma_ar, root, pos,
 *       gloss_en, source, matched: "lemma" | "variant" } }
 *   `matched` says whether hits[0] matched the surface as its base lemma or
 *   only via an inflected `variants[]` entry — the signal the audit flags on.
 */
import { tokenizeJa, lookup, normalizeFinals, candidateForms, type Entry } from "../lib/lookup";
import * as readline from "node:readline";

function matchedHow(e: Entry, surface: string): "lemma" | "variant" {
  const cands = new Set(candidateForms(surface));
  if (cands.has(normalizeFinals(e.lemma_ja))) return "lemma";
  return "variant";
}

function resolve(surface: string) {
  const hits = lookup(surface);
  if (!hits.length) return { surface, n_hits: 0, entry: null };
  const e = hits[0];
  return {
    surface,
    n_hits: hits.length,
    entry: {
      id: e.id,
      lemma_ja: e.lemma_ja,
      lemma_ar: e.lemma_ar,
      root: e.root,
      pos: e.pos,
      gloss_en: e.gloss_en,
      source: e.source ?? "",
      matched: matchedHow(e, surface),
    },
  };
}

const rl = readline.createInterface({ input: process.stdin });
rl.on("line", (line) => {
  if (!line.trim()) {
    process.stdout.write("\n");
    return;
  }
  let parsed: { text: string };
  try {
    parsed = JSON.parse(line);
  } catch {
    process.stderr.write(`bad input line: ${line}\n`);
    process.stdout.write("[]\n");
    return;
  }
  const words = tokenizeJa(parsed.text)
    .filter((t) => t.kind === "word")
    .map((t) => t.text);
  process.stdout.write(JSON.stringify(words.map(resolve)) + "\n");
});
