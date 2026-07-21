import type { WorkData, WorkPage } from "@/app/advanced/reader";

/**
 * Portuguese sidecar for a Moreh Nevukhim chapter.
 *
 * Mirrors the Tafsir's `-portuguese.json` sidecars, but shaped for the Moreh
 * data model: instead of a flat `{verse: pt}` map, a Moreh chapter is a list of
 * pages, each with an ordered `aligned` array (and/or free-flow `paragraphs`).
 * The sidecar therefore keys Portuguese by `page_he`, then supplies arrays that
 * run parallel to the source's `aligned` / `paragraphs`.
 *
 * Authored against the Judeo-Arabic (not the English or the Hebrew) for
 * reverse-translatability — see MOREH-PORTUGUESE-GHOST.md for the register and
 * the driverless generation loop that fills these in.
 */
export type MorehPortuguese = {
  _status?: string;
  _model?: string;
  _note?: string;
  pages: Record<
    string,
    {
      /** Parallel to the page's `aligned[]`; index i is the PT of segment i. */
      aligned?: (string | null)[];
      /** Parallel to the page's `paragraphs[]`. */
      paragraphs?: (string | null)[];
    }
  >;
};

/**
 * Thread a Portuguese sidecar onto a chapter's WorkData, non-destructively.
 * Segments/paragraphs without a Portuguese entry are left untouched, so a
 * partially-translated chapter renders whatever exists. Returns `data`
 * unchanged when `pt` is null (no sidecar on disk yet).
 */
export function mergePortuguese(
  data: WorkData,
  pt: MorehPortuguese | null | undefined,
): WorkData {
  if (!pt || !pt.pages) return data;
  return {
    ...data,
    pages: data.pages.map((page) => {
      const p = pt.pages[page.page_he];
      if (!p) return page;
      const next: WorkPage = { ...page };
      if (page.aligned && p.aligned) {
        next.aligned = page.aligned.map((seg, i) => {
          const ptText = p.aligned?.[i];
          return ptText ? { ...seg, pt: ptText } : seg;
        });
      }
      if (page.paragraphs && p.paragraphs) {
        next.portuguese_paragraphs = page.paragraphs.map(
          (_, i) => p.paragraphs?.[i] ?? "",
        );
      }
      return next;
    }),
  };
}

/**
 * Load a chapter's Portuguese sidecar by its base data name (e.g.
 * "moreh-bab4", "moreh-p2-bab7"), returning null when none exists yet. The
 * dynamic import shares the `@/data/*.json` webpack context already used for
 * the source chapters, so a missing sidecar simply rejects and is swallowed.
 */
export async function loadPortuguese(
  baseName: string,
): Promise<MorehPortuguese | null> {
  try {
    const mod = await import(`@/data/${baseName}-portuguese.json`);
    return mod.default as MorehPortuguese;
  } catch {
    return null;
  }
}
