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

/** Per-side matching state: claimed character ranges + a forward cursor. */
type SideState = { claimed: { start: number; end: number }[]; cursor: number };

const newSide = (): SideState => ({ claimed: [], cursor: 0 });

/**
 * Locate `needle` in `text` and claim its range so no later pair can reuse
 * it. Prefer the leftmost unclaimed occurrence at or after the side's cursor
 * (advancing the cursor past it, exactly like a forward scan); only when no
 * occurrence lies ahead does it fall back to the leftmost unclaimed
 * occurrence anywhere, without moving the cursor.
 *
 * The forward preference keeps short anchors (e.g. a lone "a") matching in
 * reading order, so data authored left-to-right resolves identically to the
 * old single-cursor walk. The backward fallback is what lets a JA word reach
 * its English/Hebrew counterpart across a word-order crossing — verb-subject
 * inversions, English-fronted negations — instead of clumping a whole clause
 * into one group.
 */
function claim(
  text: string,
  needle: string,
  side: SideState,
): { start: number; end: number } | null {
  const free = (idx: number, end: number) =>
    !side.claimed.some((c) => idx < c.end && end > c.start);
  const take = (idx: number, advance: boolean) => {
    const range = { start: idx, end: idx + needle.length };
    side.claimed.push(range);
    if (advance) side.cursor = range.end;
    return range;
  };
  for (let from = side.cursor; ; ) {
    const idx = text.indexOf(needle, from);
    if (idx === -1) break;
    if (free(idx, idx + needle.length)) return take(idx, true);
    from = idx + 1;
  }
  for (let from = 0; ; ) {
    const idx = text.indexOf(needle, from);
    if (idx === -1) return null;
    if (free(idx, idx + needle.length)) return take(idx, false);
    from = idx + 1;
  }
}

/**
 * Resolve a list of phrase pairs against the Hebrew, JA, and EN verse
 * strings. Each pair becomes one group id (0-indexed). Each side is matched
 * independently (see `claim`), and a side whose substring has no free
 * occurrence is silently dropped for that pair — so a missing Hebrew anchor
 * doesn't kill the JA↔EN match. Resulting spans are returned sorted by start
 * position (sliceByGroups requires that).
 */
export function resolveVerseAlignment(
  he: string,
  ja: string,
  en: string,
  pairs: AlignmentPair[],
): VerseAlignment {
  const out: VerseAlignment = { he: [], ja: [], en: [] };
  const heSide = newSide();
  const jaSide = newSide();
  const enSide = newSide();
  pairs.forEach((p, i) => {
    const jr = claim(ja, p.ja, jaSide);
    const er = claim(en, p.en, enSide);
    if (!jr || !er) return;
    out.ja.push({ ...jr, groupId: i });
    out.en.push({ ...er, groupId: i });
    if (p.he) {
      const hr = claim(he, p.he, heSide);
      if (hr) out.he.push({ ...hr, groupId: i });
    }
  });
  const bystart = (a: Span, b: Span) => a.start - b.start;
  out.he.sort(bystart);
  out.ja.sort(bystart);
  out.en.sort(bystart);
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
