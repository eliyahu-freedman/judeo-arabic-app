import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // lib/tafsirIndex.ts reads data/tafsir-{book}-{ch}.json at request time via
  // fs.readFile. The paths are dynamic, so Next's static tracing can't infer
  // them — list them explicitly so Vercel bundles them into the function.
  // The lexicon search + lemma pages (lib/lexicon.ts) read the same files to
  // build their book-aware concordance, so they need the data traced too.
  outputFileTracingIncludes: {
    "/tafsir/**": ["./data/tafsir-*.json"],
    "/lexicon": ["./data/tafsir-*.json"],
    "/lexicon/**": ["./data/tafsir-*.json"],
  },
};

export default nextConfig;
