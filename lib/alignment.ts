/**
 * Phrase-pair alignment between the biblical Hebrew, Saadia's JA, and the
 * English rendering.
 *
 * Data lives in data/tafsir-{book}-{chapter}-alignment.json as an ordered
 * list of {he?, ja, en} substring pairs per verse. `he` is optional for
 * backwards compatibility with the earlier {ja, en}-only files. At load
 * time we resolve each present substring to a character range via a
 * running cursor (so duplicate phrases are disambiguated by left-to-right
 * order).
 *
 * The reader uses the resolved spans to (a) render each side as runs of
 * text where each in-group run carries a group id, and (b) coordinate
 * hover highlighting across the Hebrew, JA, and English columns.
 */

export type AlignmentPair = {
  he?: string;
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
  /** Hebrew-side spans, sorted by start. Empty if no pair carried `he`. */
  he: Span[];
  /** JA-side spans, sorted by start. */
  ja: Span[];
  /** EN-side spans, sorted by start. */
  en: Span[];
};

/**
 * Resolve a list of phrase pairs against the Hebrew, JA, and EN verse
 * strings. Each pair becomes one group id (0-indexed). A side whose
 * substring isn't found at or after the current cursor is silently dropped
 * for that pair (so a missing Hebrew anchor doesn't kill the JA↔EN match).
 * Side cursors are only advanced when that side's substring resolved.
 */
export function resolveVerseAlignment(
  he: string,
  ja: string,
  en: string,
  pairs: AlignmentPair[],
): VerseAlignment {
  const out: VerseAlignment = { he: [], ja: [], en: [] };
  let heCursor = 0;
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
    if (p.he) {
      const hi = he.indexOf(p.he, heCursor);
      if (hi !== -1) {
        out.he.push({ start: hi, end: hi + p.he.length, groupId: i });
        heCursor = hi + p.he.length;
      }
    }
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
