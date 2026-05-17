import type { Metadata } from "next";
import Link from "next/link";
import { Lora, Noto_Serif_Hebrew, Amiri } from "next/font/google";
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

export const metadata: Metadata = {
  title: "Judeo-Arabic — Learn to Read",
  description:
    "A reader-first introduction to Judeo-Arabic for Hebrew readers: alphabet, Saadia's Tafsir, and medieval philosophical prose.",
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
        <header className="border-b border-ink/10 bg-page/80 backdrop-blur supports-[backdrop-filter]:bg-page/60">
          <nav className="max-w-5xl mx-auto px-6 py-5 flex items-center justify-between">
            <Link
              href="/"
              className="text-lg tracking-tight text-ink hover:text-wine transition-colors"
            >
              Judeo-Arabic
            </Link>
            <ul className="flex gap-7 text-sm uppercase tracking-widest text-ink/70">
              <li>
                <Link
                  href="/alphabet"
                  className="hover:text-wine transition-colors"
                >
                  Alphabet
                </Link>
              </li>
              <li>
                <Link
                  href="/tafsir"
                  className="hover:text-wine transition-colors"
                >
                  Tafsir
                </Link>
              </li>
              <li>
                <Link
                  href="/advanced"
                  className="hover:text-wine transition-colors"
                >
                  Advanced
                </Link>
              </li>
            </ul>
          </nav>
        </header>
        <main className="flex-1">{children}</main>
        <footer className="border-t border-ink/10 py-5 text-center text-xs tracking-wider uppercase text-ink/50">
          Prototype · Saadia (Tafsir Bereshit 1) · Bahya (Introduction)
        </footer>
      </body>
    </html>
  );
}
