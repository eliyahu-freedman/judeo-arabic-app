import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // lib/tafsirIndex.ts reads data/tafsir-{book}-{ch}.json at request time via
  // fs.readFile. The paths are dynamic, so Next's static tracing can't infer
  // them — list them explicitly so Vercel bundles them into the function.
  outputFileTracingIncludes: {
    "/tafsir/**": ["./data/tafsir-*.json"],
  },
};

export default nextConfig;
