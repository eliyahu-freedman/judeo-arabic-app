import Image from "next/image";
import Link from "next/link";

export default function SaadiaStoryPage() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 pb-32">
      <header className="mb-10">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          <Link href="/learn" className="hover:text-wine">
            Learn
          </Link>{" "}
          · the story
        </p>
        <h1 className="text-4xl tracking-tight text-ink leading-tight">
          Who was <span className="text-wine italic">Saadia</span>?
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          A short walk through the 10th century — and the choice one rabbi
          made that shaped how Arabic-speaking Jews would read Torah for the
          next thousand years.
        </p>
      </header>

      {/* The comic — six panels in a single page-strip */}
      <figure className="mb-12">
        <div className="rounded-md overflow-hidden border border-ink/15 shadow-md shadow-wine/10 bg-page">
          <Image
            src="/comic/saadia-story.png"
            alt="A six-panel comic strip telling the story of Saadia Gaon. Panel 1: a Baghdad market street around 920 CE with domes, a minaret, and palm trees. Panel 2: a bearded man at a table with an open Hebrew Bible, hand to his forehead, while his teenage son shrugs. Panel 3: a stack of leather-bound codices and rolled scrolls with a wax seal bearing the Hebrew letter qof. Panel 4: a young Saadia at his writing desk in the Fayyum, Egypt, with a date palm and desert sunset through the window. Panel 5: Saadia, now older, on a throne under a wine canopy with a Star of David ornament, flanked by two elder rabbis. Panel 6: an open codex with illuminated Hebrew and Arabic initials, a quill resting across the binding."
            width={1200}
            height={1700}
            priority
            className="w-full h-auto"
          />
        </div>
        <figcaption className="mt-3 text-[11px] text-muted text-center italic">
          Saadia&apos;s story in six panels. Illustration generated for this
          site.
        </figcaption>
      </figure>

      {/* The pull quote — Saadia in his own voice */}
      <section className="rounded-md bg-wine/5 border border-wine/30 p-8 mb-10">
        <p className="text-[10px] uppercase tracking-[0.25em] text-wine mb-4">
          Saadia, in his own words
        </p>
        <blockquote
          dir="rtl"
          className="font-hebrew text-xl text-ink/90 leading-loose mb-5"
        >
          ואנמא ארסמת הדיא אלכתאב לאן בעץ&#x327; אלראגבין סאלני אן אפרד בסיט
          נץ אלתורה פי כתאב מפרד… אלא אכ&#x327;ראג&#x327; מעאני נץ אלתורה
          פקט.
        </blockquote>
        <blockquote className="text-[15px] text-ink/85 leading-relaxed italic">
          &ldquo;I authored this book only because certain seekers asked me
          to single out the plain text of the Torah in a separate book…
          only the bringing-forth of the meaning of the Torah&apos;s text
          itself. So that the audience might hear the meanings of the
          Torah — narrative, command, recompense — in a brief and orderly
          arrangement.&rdquo;
        </blockquote>
        <p className="text-[11px] text-muted mt-4">
          — Tafsir preface, §10.{" "}
          <Link
            href="/learn/saadia-preface"
            className="text-wine hover:underline"
          >
            Read the full preface →
          </Link>
        </p>
      </section>

      {/* The hook — the first verse */}
      <section className="rounded-md bg-page border border-ink/10 p-8 text-center">
        <p className="text-[10px] uppercase tracking-[0.25em] text-muted mb-4">
          Where it begins
        </p>
        <p
          dir="rtl"
          className="font-hebrew text-3xl text-ink leading-loose my-4"
        >
          אול מא כ&#x2019;לק אללה. אלסמאואת ואלארץ&#x2019;
        </p>
        <p className="text-base text-ink/80 italic">
          &ldquo;The first thing God created: the heavens and the
          earth.&rdquo;
        </p>
        <p className="mt-4 text-[14px] text-ink/70 leading-relaxed">
          Genesis 1:1, in the Arabic Saadia chose. Tap to read.
        </p>
        <Link
          href="/tafsir/bereshit/1"
          className="mt-6 inline-flex items-center gap-2 px-5 py-2.5 bg-wine text-page rounded-sm text-sm tracking-wider hover:bg-wine/90 transition-colors"
        >
          Read the Tafsir <span aria-hidden>→</span>
        </Link>
      </section>

      <nav className="mt-12 flex flex-wrap items-center gap-x-6 gap-y-2 text-sm">
        <Link href="/learn" className="text-ink/70 hover:text-wine">
          ← All lessons
        </Link>
        <Link
          href="/learn/saadia-preface"
          className="text-ink/70 hover:text-wine"
        >
          Saadia&apos;s own preface →
        </Link>
      </nav>
    </div>
  );
}
