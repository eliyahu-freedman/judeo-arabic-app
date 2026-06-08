import { candidateForms, normalizeFinals } from "./lookup";
import morehNotes from "@/data/blau-notes-moreh.json";
import qirqisaniNotes from "@/data/blau-notes-qirqisani.json";

/**
 * A per-work Blau overlay note. These surface a *special Judaeo-Arabic sense*
 * (from Joshua Blau's Dictionary of Medieval Judaeo-Arabic Texts) for a word in
 * one specific Advanced-reader work, and are rendered ONLY when reading that
 * work — so a sense attached to the Moreh never appears in the Kuzari, Bahya,
 * Qirqisani, or Saadia readers. This is the Blau analogue of the Tafsir
 * reader's `saadia_note` / divergence overlay: the shared dictionary
 * (starter + lane) carries the neutral classical gloss shown everywhere; the
 * rare work-bound JA sense lives here.
 */
export type WorkNote = {
  lemma_ja: string;
  lemma_ar?: string;
  root?: string;
  blau_sense_en: string;
  blau_sense_he?: string;
  attested_in?: string;
  variants?: string[];
};

type WorkNotesFile = { work: string; notes: WorkNote[] };

// Registry of per-work overlays, keyed by the work id set on WorkData.workId.
// Add `kuzari`, `qirqisani`, etc. here as their overlays are authored.
const REGISTRY: Record<string, WorkNotesFile> = {
  moreh: morehNotes as WorkNotesFile,
  qirqisani: qirqisaniNotes as WorkNotesFile,
};

export function loadWorkNotes(workId: string | undefined): WorkNote[] {
  if (!workId) return [];
  return REGISTRY[workId]?.notes ?? [];
}

/**
 * Find the Blau overlay note (if any) for a tapped token in a given work.
 * Matches with the exact same candidate chain as the dictionary lookup
 * (`candidateForms` + `normalizeFinals`), so prefixed/inflected surface forms
 * resolve identically to how the gloss card resolves them.
 */
export function lookupWorkNote(
  workId: string | undefined,
  rawToken: string | null,
): WorkNote | null {
  if (!workId || !rawToken) return null;
  const notes = loadWorkNotes(workId);
  if (!notes.length) return null;

  const cands = new Set(candidateForms(rawToken));
  // Prefer a note whose lemma_ja IS the tapped form over one that only matched
  // via an inflected variant (mirrors rankHits in lib/lookup.ts).
  const lemmaMatch = notes.find((n) => cands.has(normalizeFinals(n.lemma_ja)));
  if (lemmaMatch) return lemmaMatch;
  for (const n of notes) {
    const keys = [n.lemma_ja, ...(n.variants ?? [])].map(normalizeFinals);
    if (keys.some((k) => cands.has(k) || cands.has(normalizeFinals(k)))) {
      return n;
    }
  }
  return null;
}
