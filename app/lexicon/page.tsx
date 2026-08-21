import type { Metadata } from "next";
import Link from "next/link";
import { corpusStats, fmt } from "@/lib/corpusStats";
import { searchLexicon } from "@/lib/lexicon";

export const metadata: Metadata = {
  title: "Lexicon",
  description:
    "Search the Judeo-Arabic lexicon — every word in Saadia's Tafsir, with root, part of speech, glosses, and attestations across the Pentateuch.",
  alternates: { canonical: "/lexicon" },
};

const EXAMPLES = [
  { q: "כלק", label: "כ׳לק — create" },
  { q: "אשתראך", label: "אשתראך — equivocity" },
  { q: "אסתעארה", label: "אסתעארה — metaphor" },
  { q: "create", label: "create (by gloss)" },
  { q: "ילד", label: "√w-l-d (by root)" },
];

export default async function LexiconPage({
  searchParams,
}: {
  searchParams: Promise<{ q?: string }>;
}) {
  const { q } = await searchParams;
  const query = (q ?? "").trim();
  const results = query ? await searchLexicon(query) : [];

  return (
    <div className="mx-auto max-w-5xl px-6 py-16 sm:py-20">
      <p className="label label-accent mb-4">The Lexicon</p>
      <h1 className="display text-4xl leading-tight sm:text-5xl">
        Search the Judeo-Arabic lexicon
      </h1>
      <p className="mt-4 max-w-2xl text-ink/70">
        {fmt(corpusStats.dictionaryEntries)} entries over{" "}
        {fmt(corpusStats.uniqueRoots)} roots, indexed against the{" "}
        {fmt(corpusStats.totalTokens)}-word Tafsir concordance — and now across
        the classical prose library too: the Guide, Bahya, Saadia&apos;s Emunot,
        the Kuzari. Search by Judeo-Arabic word, Arabic script, root,
        or English/Hebrew gloss; each entry shows where the word recurs across
        the authors.
      </p>

      {/* Search field */}
      <form action="/lexicon" role="search" className="relative mt-8 max-w-xl">
        <input
          type="search"
          name="q"
          defaultValue={query}
          autoFocus
          placeholder="כ׳לק · سماء · create · √k-t-b"
          aria-label="Search the Judeo-Arabic lexicon"
          className="w-full rounded-sm border border-ink/20 bg-page py-3 ps-4 pe-12 text-lg text-ink placeholder:text-ink/35 focus:border-wine focus:outline-none focus:ring-1 focus:ring-wine/30"
        />
        <button
          type="submit"
          aria-label="Search"
          className="absolute inset-y-0 end-2 my-2 flex items-center rounded-sm bg-wine px-3 text-parchment hover:bg-wine-700"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
            <circle cx="11" cy="11" r="7" />
            <line x1="21" y1="21" x2="16.5" y2="16.5" />
          </svg>
        </button>
      </form>

      {/* No query → landing */}
      {!query && (
        <div className="mt-8">
          <div className="flex flex-wrap items-center gap-2">
            <span className="label">Try</span>
            {EXAMPLES.map((ex) => (
              <Link
                key={ex.q}
                href={`/lexicon?q=${encodeURIComponent(ex.q)}`}
                className="rounded-sm border border-ink/15 bg-page px-3 py-1 text-sm text-ink/80 transition-colors hover:border-wine/40 hover:text-wine"
              >
                {ex.label}
              </Link>
            ))}
          </div>
          <div className="apparatus mt-8 rounded-sm">
            Every word also resolves in context: open any text in the{" "}
            <Link href="/tafsir/bereshit/1" className="font-semibold text-wine not-italic hover:underline">
              reader
            </Link>{" "}
            and tap a word for the same root, part of speech, and glosses, plus
            its concordance.
          </div>
        </div>
      )}

      {/* Query, no results */}
      {query && results.length === 0 && (
        <p className="mt-10 text-ink/70">
          No lexicon entry matches{" "}
          <span dir="rtl" className="font-hebrew text-ink">
            {query}
          </span>
          . Try the bare consonants (no prefixes), the Arabic root, or an
          English gloss.
        </p>
      )}

      {/* Results */}
      {results.length > 0 && (
        <>
          <p className="mt-10 label">
            {results.length}
            {results.length === 60 ? "+" : ""}{" "}
            {results.length === 1 ? "match" : "matches"}
          </p>
          <ul className="mt-3 divide-y divide-ink/10 border-y border-ink/10">
            {results.map((r) => (
              <li key={r.key + r.lemma_ja}>
                <Link
                  href={`/lexicon/${encodeURIComponent(r.key)}`}
                  className="group flex items-baseline justify-between gap-4 py-4 transition-colors hover:bg-page/60"
                >
                  <div className="min-w-0">
                    <div className="flex items-baseline gap-3">
                      <span
                        dir="rtl"
                        className="font-hebrew text-2xl text-ink group-hover:text-wine"
                      >
                        {r.lemma_ja}
                      </span>
                      {r.lemma_ar && (
                        <span dir="rtl" className="font-arabic text-lg text-muted">
                          {r.lemma_ar}
                        </span>
                      )}
                    </div>
                    <div className="mt-1 flex flex-wrap items-baseline gap-x-3 gap-y-0.5 text-sm text-ink/75">
                      {r.gloss_en && <span>{r.gloss_en}</span>}
                      {r.gloss_he && (
                        <span dir="rtl" className="font-hebrew text-ink/60">
                          {r.gloss_he}
                        </span>
                      )}
                    </div>
                    <div className="mt-1.5 flex flex-wrap gap-x-4 text-xs text-muted">
                      {r.root && (
                        <span className="font-mono">√{r.root}</span>
                      )}
                      {r.pos && <span className="italic">{r.pos}</span>}
                    </div>
                  </div>
                  <div className="shrink-0 text-right">
                    {r.count > 0 ? (
                      <span className="font-mono text-sm text-wine">
                        {fmt(r.count)}×
                      </span>
                    ) : (
                      <span className="text-xs text-muted">unattested</span>
                    )}
                    <span className="mt-1 block text-[10px] uppercase tracking-widest text-ink/40 transition-colors group-hover:text-wine">
                      open →
                    </span>
                  </div>
                </Link>
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}
