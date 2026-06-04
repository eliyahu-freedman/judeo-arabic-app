import Link from "next/link";

export function ComingSoon({
  author,
  work,
  oneLiner,
  sample,
}: {
  author: string;
  work: string;
  oneLiner: string;
  sample?: string;
}) {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Stage 3 · Coming soon
        </p>
        <p className="text-xs tracking-wide text-ink/60 mb-2">{author}</p>
        <h1 className="text-4xl tracking-tight text-ink">
          <span className="text-wine italic">{work}</span>
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          {oneLiner}
        </p>
        {sample && (
          <p
            dir="rtl"
            className="font-hebrew text-2xl text-ink/80 mt-8 leading-loose"
          >
            {sample}
          </p>
        )}
        <p className="mt-10 text-sm italic text-muted">
          Reader coming soon.
        </p>
        <Link
          href="/advanced"
          className="mt-6 inline-flex items-center gap-2 border-b border-wine/30 pb-1 text-[11px] font-bold uppercase tracking-[0.18em] text-wine hover:border-wine"
        >
          ← Back to the Library
        </Link>
      </header>
    </div>
  );
}
