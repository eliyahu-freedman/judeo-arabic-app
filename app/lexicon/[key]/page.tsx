import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getLemma } from "@/lib/lexicon";
import { fmt } from "@/lib/corpusStats";

type Props = { params: Promise<{ key: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { key: raw } = await params;
  const key = decodeURIComponent(raw);
  const data = await getLemma(key);
  const head = data?.entries[0]?.lemma_ja ?? key;
  const gloss = data?.entries[0]?.gloss_en;
  return {
    title: `${head} — Lexicon`,
    description: gloss
      ? `${head} (${gloss}) in Judeo-Arabic: root, part of speech, glosses, and every attestation in Saadia's Tafsir.`
      : `${head} in the Judeo-Arabic lexicon: attested forms and concordance across Saadia's Tafsir.`,
    alternates: { canonical: `/lexicon/${encodeURIComponent(key)}` },
  };
}

/** Render a verse with the matched surface form(s) highlighted. Splits on the
 *  exact surface string — adequate for the unvocalised Tafsir text. */
function Kwic({ ja, surface }: { ja: string; surface: string }) {
  if (!surface || !ja.includes(surface)) {
    return <span dir="rtl" className="font-hebrew">{ja}</span>;
  }
  const parts = ja.split(surface);
  return (
    <span dir="rtl" className="font-hebrew">
      {parts.map((p, i) => (
        <span key={i}>
          {p}
          {i < parts.length - 1 && (
            <mark className="rounded-sm bg-wine-100 px-0.5 text-wine-700">
              {surface}
            </mark>
          )}
        </span>
      ))}
    </span>
  );
}

export default async function LemmaPage({ params }: Props) {
  const { key: raw } = await params;
  const key = decodeURIComponent(raw);
  const data = await getLemma(key);
  if (!data) notFound();

  const primary = data.entries[0];
  const head = primary?.lemma_ja ?? key;
  const verseCount = data.byBook.reduce((n, b) => n + b.rows.length, 0);

  return (
    <article className="mx-auto max-w-3xl px-6 py-12 sm:py-16">
      <nav className="mb-8 text-sm">
        <Link href="/lexicon" className="text-wine underline-offset-4 hover:underline">
          ← Lexicon
        </Link>
      </nav>

      {/* Headword block */}
      <header className="border-b border-ink/10 pb-8">
        <div className="flex flex-wrap items-baseline gap-x-5 gap-y-2">
          <h1 dir="rtl" className="font-hebrew text-5xl text-ink">
            {head}
          </h1>
          {primary?.lemma_ar && (
            <span dir="rtl" className="font-arabic text-3xl text-muted">
              {primary.lemma_ar}
            </span>
          )}
          {data.count > 0 && (
            <span className="font-mono text-sm text-wine">
              {fmt(data.count)}× · {verseCount}{" "}
              {verseCount === 1 ? "verse" : "verses"}
            </span>
          )}
        </div>
        {primary && (
          <div className="mt-4 flex flex-wrap gap-x-8 gap-y-2 text-sm">
            {primary.root && (
              <div>
                <span className="label block">Root</span>
                <span className="mt-0.5 block font-mono">√{primary.root}</span>
              </div>
            )}
            {primary.pos && (
              <div>
                <span className="label block">Part of speech</span>
                <span className="mt-0.5 block italic">{primary.pos}</span>
              </div>
            )}
            {primary.gloss_en && (
              <div>
                <span className="label block">English</span>
                <span className="mt-0.5 block">{primary.gloss_en}</span>
              </div>
            )}
            {primary.gloss_he && (
              <div>
                <span className="label block">Hebrew</span>
                <span dir="rtl" className="mt-0.5 block font-hebrew">
                  {primary.gloss_he}
                </span>
              </div>
            )}
          </div>
        )}
      </header>

      {/* Dictionary entries (incl. homographs) + notes */}
      {data.entries.length > 0 && (
        <section className="mt-8">
          {data.entries.length > 1 && (
            <p className="label mb-3">{data.entries.length} senses</p>
          )}
          <div className="space-y-4">
            {data.entries.map((e, i) => (
              <div
                key={e.id ?? i}
                className="rounded-sm border border-ink/10 bg-page p-5"
              >
                <div className="flex items-baseline justify-between gap-3">
                  <span className="text-ink">
                    {e.gloss_en}
                    {e.gloss_he && (
                      <span dir="rtl" className="font-hebrew text-ink/60">
                        {" "}
                        · {e.gloss_he}
                      </span>
                    )}
                  </span>
                  <span className="shrink-0 font-mono text-xs text-muted">
                    {e.pos}
                  </span>
                </div>
                {e.notes && (
                  <p className="apparatus mt-3 rounded-sm">{e.notes}</p>
                )}
                {e.saadia_note && (
                  <p className="apparatus mt-3 rounded-sm">
                    <span className="font-semibold not-italic text-ink">
                      In Saadia&apos;s Tafsir:{" "}
                    </span>
                    {e.saadia_note}
                  </p>
                )}
              </div>
            ))}
          </div>
        </section>
      )}

      {data.entries.length === 0 && (
        <p className="apparatus mt-8 rounded-sm">
          No dictionary entry yet for this form — showing its attestations in
          the Tafsir. Glossing is hand-curated highest-frequency-first; rarer
          words are added over time.
        </p>
      )}

      {/* Attested surface forms */}
      {data.variants.length > 0 && (
        <section className="mt-10">
          <h2 className="label mb-3">
            Attested forms ({data.variants.length})
          </h2>
          <div className="flex flex-wrap gap-2">
            {data.variants.map((vf) => (
              <span
                key={vf.surface}
                dir="rtl"
                className="inline-flex items-baseline gap-1.5 rounded-sm border border-ink/10 bg-page px-2.5 py-1"
              >
                <span className="font-hebrew text-ink">{vf.surface}</span>
                <span className="font-mono text-xs text-muted">{vf.count}</span>
              </span>
            ))}
          </div>
        </section>
      )}

      {/* Concordance, grouped by book */}
      {data.byBook.length > 0 && (
        <section className="mt-10">
          <h2 className="label mb-4">Concordance</h2>
          <div className="space-y-8">
            {data.byBook.map((group) => (
              <div key={group.bookSlug}>
                <h3 className="display mb-3 text-lg text-ink">
                  {group.book}{" "}
                  <span className="text-sm font-normal text-muted">
                    ({group.rows.length})
                  </span>
                </h3>
                <ul className="space-y-px overflow-hidden rounded-sm border border-ink/10">
                  {group.rows.map((row, i) => (
                    <li key={`${row.ch}-${row.v}-${i}`}>
                      <Link
                        href={`/tafsir/${group.bookSlug}/${row.ch}#verse-${row.ch}-${row.v}`}
                        className="flex items-baseline gap-3 bg-page px-4 py-2.5 transition-colors hover:bg-wine-50"
                      >
                        <span className="shrink-0 font-mono text-xs text-wine/80">
                          {row.ch}:{row.v}
                        </span>
                        <span className="min-w-0 grow text-right leading-relaxed">
                          <Kwic ja={row.ja} surface={row.surface} />
                        </span>
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            ))}
          </div>
        </section>
      )}

      {/* Across the library — the same word in Moreh, Bahya, Saadia, … */}
      {data.library && data.library.uses.length > 0 && (
        <section className="mt-10">
          <h2 className="label mb-1">Across the library</h2>
          <p className="mb-4 text-sm text-muted">
            {fmt(data.library.count)}× in the classical prose corpus — the Guide,
            Bahya, Saadia&apos;s Emunot, Qirqisani, the Kuzari.
          </p>
          {data.library.sample?.snippet && (
            <p
              dir="rtl"
              className="font-hebrew mb-4 rounded-sm border border-ink/10 bg-page px-4 py-3 leading-relaxed text-ink/80"
            >
              {data.library.sample.snippet}
            </p>
          )}
          <ul className="flex flex-wrap gap-2">
            {data.library.uses.map((u) => (
              <li key={u.href + u.work}>
                <Link
                  href={u.href}
                  className="inline-flex items-baseline gap-1.5 rounded-sm border border-ink/10 bg-page px-2.5 py-1 transition-colors hover:border-wine/40 hover:text-wine"
                >
                  <span>{u.work}</span>
                  <span className="font-mono text-xs text-muted">{u.n}</span>
                </Link>
              </li>
            ))}
          </ul>
          {data.library.truncated && (
            <p className="mt-2 text-xs text-muted">…and more.</p>
          )}
        </section>
      )}

      {data.count === 0 &&
        data.entries.length > 0 &&
        !(data.library && data.library.uses.length > 0) && (
          <p className="apparatus mt-8 rounded-sm">
            This headword is not attested in the indexed Tafsir corpus (it may
            appear as part of a different surface form).
          </p>
        )}
    </article>
  );
}
