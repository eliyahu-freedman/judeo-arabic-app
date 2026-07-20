export type XrefLayer = "mt" | "guide" | "iggerot" | "teshuvot" | "internal";

export type XrefEntry = {
  source: string;
  ref: string;
  sefaria_ref?: string;
  note: string;
  layer: XrefLayer;
};

/** Mishnah-keyed cross-references for one chapter: "m1" → entries */
export type ChapterXrefs = Record<string, XrefEntry[]>;

/** Full tractate xref file format */
export type TractateXrefs = {
  tractate: string;
  chapters: Record<string, ChapterXrefs>;
};

export const LAYER_LABELS: Record<XrefLayer, string> = {
  mt: "Mishneh Torah",
  guide: "Guide for the Perplexed",
  iggerot: "Iggerot HaRambam",
  teshuvot: "Teshuvot HaRambam",
  internal: "Commentary — internal",
};
