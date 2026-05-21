import Link from "next/link";

const lessons = [
  {
    href: "/learn/first-50",
    status: "Live",
    title: "First 50 Words",
    body: "The fifty Judeo-Arabic words that show up most across Saadia's Tafsir — function words, common verbs, the cast of characters. Each card links straight into the Tafsir for a real example.",
    sample: "אללה · ארץ' · קאל · כ'לק · מוסי",
  },
  {
    href: "/learn/cognates",
    status: "Live",
    title: "You Already Know This",
    body: "Modern Hebrew words you already use that come straight from Arabic — and how Saadia used them a thousand years ago. From yallah and sababa to ראש, אם, and כלב.",
    sample: "יאללה · ראש · שמע · אחלה",
  },
  {
    href: "/learn/aramaic-cognates",
    status: "Live",
    title: "If You Know Onkelos…",
    body: "Forty Aramaic words that bridge straight to Arabic — and most of them are sitting in your weekly parashah. The interdental words (תלת, דהב, דכר) are the ones only Aramaic can teach: where Hebrew shifted its consonants, Aramaic and Arabic agree.",
    sample: "תלת · דהב · ארעא · בית · חמרא",
  },
  {
    href: "/learn/saadia-story",
    status: "Live",
    title: "Who Was Saadia?",
    body: "A short walk through the 10th century — and the choice one rabbi made that shaped how Arabic-speaking Jews would read Torah for the next thousand years. Ends with Saadia's own words.",
    sample: "ca. 882 – 942 CE · Egypt → Baghdad",
  },
  {
    href: "/learn/saadia-preface",
    status: "Live",
    title: "Saadia's Own Preface",
    body: "Saadia's preface to the Tafsir — in Judeo-Arabic alongside English. The opening, his theory of why the Torah teaches by story, and his plain statement of why he wrote this book. Most of it being published in English for the first time.",
    sample: "תפסיר תורה · ca. 930 CE",
  },
];

export default function LearnHub() {
  return (
    <div className="max-w-3xl mx-auto px-6 py-16 sm:py-24">
      <header className="mb-12">
        <p className="text-xs uppercase tracking-[0.3em] text-muted mb-3">
          Learn · short formats
        </p>
        <h1 className="text-4xl tracking-tight text-ink">
          A way <span className="text-wine italic">in</span>.
        </h1>
        <p className="mt-6 text-base text-ink/75 leading-relaxed max-w-xl">
          Bite-sized, browseable ways into Judeo-Arabic. No prior background
          required — start with the words you&apos;ll see most.
        </p>
      </header>

      <ul className="space-y-5">
        {lessons.map((l) => {
          const card = (
            <div
              className={`block rounded-md bg-page border p-7 transition-all ${
                l.href
                  ? "border-ink/10 hover:border-wine/40 hover:shadow-md hover:shadow-wine/5 cursor-pointer"
                  : "border-ink/10 opacity-60"
              }`}
            >
              <div className="flex items-baseline justify-between">
                <div className="text-xs uppercase tracking-[0.25em] text-muted">
                  {l.status}
                </div>
              </div>
              <div
                className={`mt-1 text-2xl text-ink transition-colors ${
                  l.href ? "group-hover:text-wine" : ""
                }`}
              >
                {l.title}
              </div>
              <p className="mt-3 text-[15px] text-ink/70 leading-relaxed">
                {l.body}
              </p>
              <div
                dir="rtl"
                className="font-hebrew text-xl text-ink/80 mt-5 leading-loose"
              >
                {l.sample}
              </div>
            </div>
          );
          return (
            <li key={l.title}>
              {l.href ? (
                <Link href={l.href} className="group block">
                  {card}
                </Link>
              ) : (
                card
              )}
            </li>
          );
        })}
      </ul>
    </div>
  );
}
