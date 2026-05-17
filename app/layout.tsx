import type { Metadata } from "next";
import Link from "next/link";
import { Geist } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
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
      className={`${geistSans.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col bg-stone-50 text-stone-900">
        <header className="border-b border-stone-200 bg-white">
          <nav className="max-w-5xl mx-auto px-6 py-4 flex items-center justify-between">
            <Link href="/" className="font-serif text-lg tracking-tight">
              Judeo-Arabic
            </Link>
            <ul className="flex gap-6 text-sm">
              <li>
                <Link
                  href="/alphabet"
                  className="hover:text-stone-600 transition-colors"
                >
                  Alphabet
                </Link>
              </li>
              <li>
                <Link
                  href="/tafsir"
                  className="hover:text-stone-600 transition-colors"
                >
                  Tafsir
                </Link>
              </li>
              <li>
                <Link
                  href="/advanced"
                  className="hover:text-stone-600 transition-colors"
                >
                  Advanced
                </Link>
              </li>
            </ul>
          </nav>
        </header>
        <main className="flex-1">{children}</main>
        <footer className="border-t border-stone-200 py-4 text-center text-xs text-stone-500">
          Prototype. Texts: Saadia (Tafsir Bereshit 1), Bahya (Introduction).
        </footer>
      </body>
    </html>
  );
}
