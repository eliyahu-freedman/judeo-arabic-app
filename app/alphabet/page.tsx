export default function AlphabetPage() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-14">
      <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
        Stage 1
      </p>
      <h1 className="text-4xl tracking-tight">
        <span className="text-ink">The </span>
        <span className="text-wine italic">Alphabet</span>
      </h1>
      <p className="mt-6 text-base text-ink/70 leading-relaxed max-w-xl">
        Five lessons covering Hebrew letters for Arabic phonemes, the
        diacritic letters (ג׳ ד׳ ח׳ ט׳ ת׳), the definite article אל, common
        orthographic ambiguities, and a first reading exercise.
      </p>
      <p className="mt-4 text-sm text-muted italic">Coming in M3.</p>
    </div>
  );
}
