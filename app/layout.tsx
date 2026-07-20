import type { Metadata } from "next";
import Link from "next/link";
import { Lora, Noto_Serif_Hebrew, Amiri } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import AuthButton from "@/components/AuthButtonWrapper";
import "./globals.css";

const lora = Lora({
  variable: "--font-lora",
  subsets: ["latin"],
  display: "swap",
});

const notoHebrew = Noto_Serif_Hebrew({
  variable: "--font-noto-serif-hebrew",
  subsets: ["hebrew"],
  display: "swap",
  weight: ["400", "500", "600", "700"],
});

const amiri = Amiri({
  variable: "--font-amiri",
  subsets: ["arabic"],
  display: "swap",
  weight: ["400", "700"],
});

const SITE_URL = "https://judeo-arabic-app.vercel.app";
const SITE_NAME = "Judeo-Arabic";
const DEFAULT_TITLE =
  "Learn Judeo-Arabic — Saadia, Bahya, and the medieval Hebrew-script Arabic tradition";
const DEFAULT_DESCRIPTION =
  "A reader-first introduction to Judeo-Arabic for Hebrew readers. Saadia Gaon's Tafsir on the Torah and Bahya ibn Paquda's Chovot HaLevavot in the original Judeo-Arabic, with parallel Hebrew and English translations and a tap-to-define dictionary based on Joshua Blau.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: { default: DEFAULT_TITLE, template: "%s · " + SITE_NAME },
  description: DEFAULT_DESCRIPTION,
  applicationName: SITE_NAME,
  keywords: [
    "Judeo-Arabic",
    "learn Judeo-Arabic",
    "Saadia Gaon",
    "Tafsir al-Torah",
    "Bahya ibn Paquda",
    "Chovot HaLevavot",
    "medieval Arabic",
    "Hebrew-script Arabic",
    "Joshua Blau",
    "Karaite",
    "Geniza",
    "Sephardic Hebrew",
  ],
  alternates: { canonical: "/" },
  openGraph: {
    type: "website",
    siteName: SITE_NAME,
    title: DEFAULT_TITLE,
    description: DEFAULT_DESCRIPTION,
    url: SITE_URL,
    locale: "en_US",
  },
  twitter: {
    card: "summary_large_image",
    title: DEFAULT_TITLE,
    description: DEFAULT_DESCRIPTION,
  },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true, "max-image-preview": "large" },
  },
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html
      lang="en"
      className={`${lora.variable} ${notoHebrew.variable} ${amiri.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-parchment text-ink font-serif">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "LearningResource",
              name: SITE_NAME,
              url: SITE_URL,
              description: DEFAULT_DESCRIPTION,
              inLanguage: ["en", "he"],
              learningResourceType: ["Course", "Reader", "Dictionary"],
              educationalLevel: "intermediate",
              teaches: [
                "Judeo-Arabic script",
                "Saadia Gaon's Tafsir",
                "Bahya ibn Paquda's Chovot HaLevavot",
                "Medieval Hebrew-script Arabic vocabulary",
              ],
              about: [
                { "@type": "Thing", name: "Judeo-Arabic" },
                { "@type": "Person", name: "Saadia Gaon" },
                { "@type": "Person", name: "Bahya ibn Paquda" },
              ],
              isAccessibleForFree: true,
            }),
          }}
        />
        <header className="border-b border-ink/10 bg-page/80 backdrop-blur supports-[backdrop-filter]:bg-page/60">
          <nav className="mx-auto flex max-w-5xl items-center justify-between gap-6 px-6 py-4">
            <Link
              href="/"
              className="display text-2xl text-ink transition-colors hover:text-wine"
            >
              Judeo-Arabic
            </Link>

            {/* Desktop: full nav + lexicon search (md+) */}
            <div className="hidden items-center gap-7 md:flex">
              <ul className="flex gap-7 text-sm uppercase tracking-widest text-ink/70">
                <li>
                  <Link href="/foundations" className="hover:text-wine transition-colors">
                    Foundations
                  </Link>
                </li>
                <li>
                  <Link href="/tafsir" className="hover:text-wine transition-colors">
                    Tafsir
                  </Link>
                </li>
                <li>
                  <Link href="/advanced" className="hover:text-wine transition-colors">
                    Library
                  </Link>
                </li>
                <li>
                  <Link href="/lexicon" className="hover:text-wine transition-colors">
                    Lexicon
                  </Link>
                </li>
                <li>
                  <Link href="/about" className="hover:text-wine transition-colors">
                    About
                  </Link>
                </li>
              </ul>
              {/* Plain GET form — no client JS; routes to the lexicon page. */}
              <form action="/lexicon" role="search" className="relative">
                <input
                  type="search"
                  name="q"
                  placeholder="Search the lexicon…"
                  aria-label="Search the Judeo-Arabic lexicon"
                  className="w-44 rounded-sm border border-ink/15 bg-page py-1.5 pe-8 ps-3 text-sm text-ink placeholder:text-ink/40 focus:border-wine focus:outline-none focus:ring-1 focus:ring-wine/30 lg:w-52"
                />
                <span
                  aria-hidden
                  className="pointer-events-none absolute inset-y-0 end-2.5 flex items-center text-ink/40"
                >
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                    <circle cx="11" cy="11" r="7" />
                    <line x1="21" y1="21" x2="16.5" y2="16.5" />
                  </svg>
                </span>
              </form>

              <div className="flex items-center gap-3">
                {process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK && (
                  <a
                    href={process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="rounded-sm bg-wine px-3 py-1.5 text-sm font-medium text-parchment hover:bg-wine-700 transition-colors"
                  >
                    Support
                  </a>
                )}
                <AuthButton />
              </div>
            </div>

            {/* Mobile/tablet: no-JS disclosure menu (keeps layout a server
                component). Lists every nav item + a search field. */}
            <details className="relative md:hidden">
              <summary className="flex cursor-pointer list-none items-center rounded-sm p-1.5 text-ink/80 hover:text-wine [&::-webkit-details-marker]:hidden">
                <span className="sr-only">Open menu</span>
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" aria-hidden>
                  <line x1="3" y1="6" x2="21" y2="6" />
                  <line x1="3" y1="12" x2="21" y2="12" />
                  <line x1="3" y1="18" x2="21" y2="18" />
                </svg>
              </summary>
              <div className="absolute end-0 top-full z-50 mt-2 w-60 rounded-sm border border-ink/15 bg-page p-2 shadow-lg shadow-ink/10">
                <ul className="flex flex-col text-sm uppercase tracking-widest text-ink/80">
                  {[
                    ["/foundations", "Foundations"],
                    ["/tafsir", "Tafsir"],
                    ["/advanced", "Library"],
                    ["/lexicon", "Lexicon"],
                    ["/about", "About"],
                  ].map(([href, label]) => (
                    <li key={href}>
                      <Link
                        href={href}
                        className="block rounded-sm px-3 py-2 hover:bg-parchment hover:text-wine"
                      >
                        {label}
                      </Link>
                    </li>
                  ))}
                </ul>
                <form
                  action="/lexicon"
                  role="search"
                  className="mt-2 border-t border-ink/10 px-1 pt-3"
                >
                  <input
                    type="search"
                    name="q"
                    placeholder="Search the lexicon…"
                    aria-label="Search the Judeo-Arabic lexicon"
                    className="w-full rounded-sm border border-ink/15 bg-page px-3 py-2 text-sm text-ink placeholder:text-ink/40 focus:border-wine focus:outline-none focus:ring-1 focus:ring-wine/30"
                  />
                </form>
                <div className="mt-2 flex items-center justify-between border-t border-ink/10 px-1 pt-3">
                  {process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK ? (
                    <a
                      href={process.env.NEXT_PUBLIC_STRIPE_PAYMENT_LINK}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="rounded-sm bg-wine px-3 py-1.5 text-sm font-medium text-parchment hover:bg-wine-700 transition-colors"
                    >
                      Support
                    </a>
                  ) : (
                    <span />
                  )}
                  <AuthButton />
                </div>
              </div>
            </details>
          </nav>
        </header>
        <main className="flex-1">{children}</main>
        <Analytics />
        <footer className="border-t border-ink/10 mt-12 bg-page/40">
          <div className="max-w-5xl mx-auto px-6 py-10">
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-8 text-sm">
              <div>
                <div className="label mb-3">I · Foundations</div>
                <ul className="space-y-2 text-ink/75">
                  <li><Link href="/foundations" className="hover:text-wine">The path</Link></li>
                  <li><Link href="/alphabet" className="hover:text-wine">Alphabet</Link></li>
                  <li><Link href="/learn/cognates" className="hover:text-wine">Hebrew–Arabic cognates</Link></li>
                  <li><Link href="/learn/first-50" className="hover:text-wine">First 50 words</Link></li>
                  <li><Link href="/learn" className="hover:text-wine">All lessons</Link></li>
                </ul>
              </div>
              <div>
                <div className="label mb-3">II · Tafsir</div>
                <ul className="space-y-2 text-ink/75">
                  <li><Link href="/tafsir" className="hover:text-wine">Saadia&apos;s Tafsir</Link></li>
                  <li><Link href="/learn/saadia-preface" className="hover:text-wine">Saadia&apos;s preface</Link></li>
                  <li><Link href="/learn/saadia-story" className="hover:text-wine">Who was Saadia?</Link></li>
                  <li><Link href="/review" className="hover:text-wine">Daily review</Link></li>
                </ul>
              </div>
              <div>
                <div className="label mb-3">III · Library</div>
                <ul className="space-y-2 text-ink/75">
                  <li><Link href="/advanced" className="hover:text-wine">The Library</Link></li>
                  <li><Link href="/lexicon" className="hover:text-wine">Lexicon</Link></li>
                  <li><Link href="/what-is-judeo-arabic" className="hover:text-wine">What is Judeo-Arabic?</Link></li>
                  <li><Link href="/resources" className="hover:text-wine">Resources</Link></li>
                  <li><Link href="/about" className="hover:text-wine">About</Link></li>
                </ul>
              </div>
              <div>
                <div className="label mb-3">Contact</div>
                <ul className="space-y-2 text-ink/75">
                  <li>
                    <a href="mailto:freedmaneli@gmail.com" className="hover:text-wine">
                      freedmaneli@gmail.com
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div className="mt-10 border-t border-ink/10 pt-6">
              <p className="text-[11px] leading-relaxed text-ink/70">
                Glosses paraphrase E. W. Lane&apos;s{" "}
                <em>Arabic-English Lexicon</em> (Perseus TEI), with
                Judeo-Arabic notes from Joshua Blau ז״ל. Saadia&apos;s{" "}
                <em>Tafsir</em> (Derenbourg) and Bahya (ibn Tibbon) via Sefaria;
                library page images from the Friedberg Jewish Manuscript
                Society. Full provenance and bibliography on the{" "}
                <Link href="/about" className="text-wine underline-offset-2 hover:underline">
                  methodology page
                </Link>
                .
              </p>
              <div className="mt-5 flex flex-col gap-2 border-t border-ink/5 pt-5 text-[11px] text-ink/60 sm:flex-row sm:items-center sm:justify-between">
                <span>
                  Edited by Eli Freedman · text &amp; translations CC BY-NC 4.0
                </span>
                <span className="text-ink/45">
                  Cite: <em>Judeo-Arabic: A Digital Reader &amp; Lexicon</em>,
                  ed. E. Freedman, judeo-arabic-app.vercel.app
                </span>
              </div>
            </div>
          </div>
        </footer>
      </body>
    </html>
  );
}
