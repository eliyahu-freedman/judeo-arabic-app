#!/usr/bin/env npx tsx
/**
 * Thin stdin→stdout CLI wrapper around `tokenizeJa` from `lib/tokenize.ts`.
 *
 * Exists so Python tools (e.g. `scripts/coverage_report.py`) can tokenise
 * Judeo-Arabic strings using the *exact* runtime tokeniser without
 * re-implementing the char-class regex and risking drift.
 *
 * Usage:
 *   $ echo '{"text":"אול מא כ'\''לק אללה"}' | npx tsx scripts/_tokenize_ja_cli.ts
 *   [{"kind":"word","text":"אול"},{"kind":"sep","text":" "},...]
 *
 * Protocol: one JSON object per stdin line, each `{ "text": "..." }`.
 *   For each line write one JSONL response, an array of `{kind, text}`.
 *
 * Word tokens only? Pass --words to filter sep tokens out, emitting just the
 * word strings as a flat array per input line. This is what the coverage
 * script wants.
 */
import { tokenizeJa } from "../lib/tokenize";
import * as readline from "node:readline";

const wordsOnly = process.argv.includes("--words");

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
  const tokens = tokenizeJa(parsed.text);
  if (wordsOnly) {
    const words = tokens.filter((t) => t.kind === "word").map((t) => t.text);
    process.stdout.write(JSON.stringify(words) + "\n");
  } else {
    process.stdout.write(JSON.stringify(tokens) + "\n");
  }
});
