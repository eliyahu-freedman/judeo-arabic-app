import index from "@/data/moreh-verse-index.json";

type Occ = { n: number; snippet: string };
type Verse = { v: string; ref: string; occ: Occ[] };
type Book = { book: string; verses: Verse[] };
const DATA = index as { books: Book[] };

/**
 * A compact "Scripture cited in this chapter" list, rendered BELOW the reader
 * (outside the alignment renderer, so it can't disturb hover/token slicing).
 * Each verse links out to Sefaria. Derived from data/moreh-verse-index.json.
 */
export function VersesCited({ n }: { n: number }) {
  const rows: { label: string; ref: string }[] = [];
  for (const b of DATA.books) {
    for (const vs of b.verses) {
      if (vs.occ.some((o) => o.n === n)) {
        rows.push({
          label: b.book === "Mishnah & Talmud" ? vs.v : `${b.book} ${vs.v}`,
          ref: vs.ref,
        });
      }
    }
  }
  if (rows.length === 0) return null;

  return (
    <section className="max-w-2xl mx-auto px-6 pb-20 -mt-6">
      <h2 className="text-[10px] uppercase tracking-[0.3em] text-muted mb-3">
        Scripture cited in this chapter
      </h2>
      <div className="flex flex-wrap gap-x-3 gap-y-1.5 text-sm">
        {rows.map((r) => (
          <a
            key={r.ref}
            href={`https://www.sefaria.org/${r.ref}`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-ink/70 hover:text-wine transition-colors whitespace-nowrap"
          >
            {r.label} ↗
          </a>
        ))}
      </div>
    </section>
  );
}
