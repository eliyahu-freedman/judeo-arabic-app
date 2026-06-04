/**
 * Zero-dependency tokeniser for Judeo-Arabic and Arabic-script text.
 *
 * Extracted from `lib/lookup.ts` so external tools (Python coverage scripts,
 * fixture tests, etc.) can import the canonical implementation without
 * pulling in the dictionary JSON path aliases. The runtime re-exports
 * `tokenizeJa` from `lib/lookup.ts` for back-compat with existing callers.
 */

export type JaToken = { kind: "word" | "sep"; text: string };

/**
 * Split a JA string into tokens for rendering. Words (Hebrew letters,
 * plus Arabic block, plus the ASCII apostrophe that JA uses for the
 * gershayim diacritic) are returned as {kind: "word"}; whitespace and
 * punctuation are returned as {kind: "sep"} so the renderer can preserve
 * spacing.
 */
export function tokenizeJa(text: string): JaToken[] {
  const out: JaToken[] = [];
  let buf = "";
  let bufKind: "word" | "sep" | null = null;
  const isWordChar = (c: string) =>
    // Hebrew block + Arabic letters/harakat (ء-ْ + superscript alef
    // ٰ) + ASCII apostrophe (JA gershayim). Arabic punctuation ، ؛ ؟
    // (،/؛/؟) sits below ء and stays a separator.
    /[֐-׿ء-ْٰ']/.test(c);

  for (const c of text) {
    const kind: "word" | "sep" = isWordChar(c) ? "word" : "sep";
    if (kind === bufKind) {
      buf += c;
    } else {
      if (buf) out.push({ kind: bufKind!, text: buf });
      buf = c;
      bufKind = kind;
    }
  }
  if (buf) out.push({ kind: bufKind!, text: buf });
  return out;
}
