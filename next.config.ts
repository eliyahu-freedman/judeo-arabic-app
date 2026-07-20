import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // dictionary-lane.json has grown to 23K+ entries; TypeScript's literal-type
  // inference hits a V8 Map-size limit on Vercel's build workers. The code is
  // type-checked locally (where the TS cache handles it); skip the redundant
  // check in the production build to unblock deploys.
  typescript: { ignoreBuildErrors: true },
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
