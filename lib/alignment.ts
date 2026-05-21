/**
 * Phrase-pair alignment between Saadia's JA and the English rendering.
 *
 * Data lives in data/tafsir-{book}-{chapter}-alignment.json as an ordered
 * list of {ja, en} substring pairs per verse. At load time we resolve those
 * substrings to character ranges via a running cursor (so duplicate phrases
 * are disambiguated by left-to-right order).
 *
 * The reader uses the resolved spans to (a) render both sides as runs of
 * text where each in-group run carries a group id, and (b) coordinate hover
 * highlighting between the two sides.
 */

export type AlignmentPair = {
  ja: string;
  en: string;
};

/** A character range on one side, tagged with the shared group id. */
export type Span = {
  start: number;
  end: number;
  groupId: number;
};

export type VerseAlignment = {
  /** JA-side spans, sorted by start. */
  ja: Span[];
  /** EN-side spans, sorted by start. */
  en: Span[];
};

/**
 * Resolve a list of phrase pairs against the JA and EN verse strings.
 * Each pair becomes one group id (0-indexed). If a phrase isn't found at
 * or after the current cursor, that pair is dropped (so one bad row doesn't
 * tank the whole verse).
 */
export function resolveVerseAlignment(
  ja: string,
  en: string,
  pairs: AlignmentPair[],
): VerseAlignment {
  const out: VerseAlignment = { ja: [], en: [] };
  let jaCursor = 0;
  let enCursor = 0;
  pairs.forEach((p, i) => {
    const ji = ja.indexOf(p.ja, jaCursor);
    const ei = en.indexOf(p.en, enCursor);
    if (ji === -1 || ei === -1) return;
    out.ja.push({ start: ji, end: ji + p.ja.length, groupId: i });
    out.en.push({ start: ei, end: ei + p.en.length, groupId: i });
    jaCursor = ji + p.ja.length;
    enCursor = ei + p.en.length;
  });
  return out;
}

/**
 * Cut a string into runs given a list of in-group spans. Returns alternating
 * { groupId: number | null, text: string } segments covering the whole string.
 * Spans must be sorted by start and non-overlapping.
 */
export function sliceByGroups(
  text: string,
  spans: Span[],
): { groupId: number | null; text: string }[] {
  const out: { groupId: number | null; text: string }[] = [];
  let cursor = 0;
  for (const s of spans) {
    if (s.start > cursor) {
      out.push({ groupId: null, text: text.slice(cursor, s.start) });
    }
    out.push({ groupId: s.groupId, text: text.slice(s.start, s.end) });
    cursor = s.end;
  }
  if (cursor < text.length) {
    out.push({ groupId: null, text: text.slice(cursor) });
  }
  return out;
}
