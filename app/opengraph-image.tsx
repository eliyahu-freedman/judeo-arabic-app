import { ImageResponse } from "next/og";

export const alt = "Learn to read Judeo-Arabic — Saadia, Bahya, and the medieval Hebrew-script Arabic tradition";
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const PARCHMENT = "#f5efe2";
const INK = "#1f1a14";
const WINE = "#7a1f1f";
const MUTED = "#6b5f4d";

// Fetch Noto Serif Hebrew at build/request time so the Hebrew sample renders.
// Parses the Google Fonts CSS to extract the underlying woff2 URL.
async function loadHebrewFont(): Promise<ArrayBuffer | null> {
  try {
    const css = await fetch(
      "https://fonts.googleapis.com/css2?family=Noto+Serif+Hebrew:wght@500&display=swap",
      { headers: { "User-Agent": "Mozilla/5.0" } },
    ).then((r) => r.text());
    const match = css.match(/url\((https:\/\/[^)]+\.woff2)\)/);
    if (!match) return null;
    return await fetch(match[1]).then((r) => r.arrayBuffer());
  } catch {
    return null;
  }
}

export default async function OpengraphImage() {
  const hebrewFont = await loadHebrewFont();

  return new ImageResponse(
    (
      <div
        style={{
          width: "100%",
          height: "100%",
          background: PARCHMENT,
          display: "flex",
          flexDirection: "column",
          justifyContent: "space-between",
          padding: "72px 80px",
          fontFamily: "serif",
          color: INK,
        }}
      >
        <div
          style={{
            fontSize: 22,
            letterSpacing: "0.3em",
            textTransform: "uppercase",
            color: MUTED,
          }}
        >
          A reader-first introduction
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 40 }}>
          {hebrewFont && (
            <div
              style={{
                fontFamily: "Noto Hebrew",
                fontSize: 80,
                color: WINE,
                direction: "rtl",
                lineHeight: 1.2,
              }}
            >
              אול מא כ׳לק אללה
            </div>
          )}
          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              alignItems: "baseline",
              fontSize: 88,
              lineHeight: 1.05,
              letterSpacing: "-0.02em",
              color: INK,
            }}
          >
            <span>Learn to read&nbsp;</span>
            <span style={{ color: WINE, fontStyle: "italic" }}>Judeo-Arabic</span>
            <span>.</span>
          </div>
          <div
            style={{
              fontSize: 30,
              color: MUTED,
              lineHeight: 1.4,
              maxWidth: 900,
            }}
          >
            Saadia&apos;s Tafsir · Bahya&apos;s Chovot HaLevavot · alphabet,
            dictionary, and spaced-repetition review.
          </div>
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "flex-end",
            fontSize: 22,
            color: MUTED,
            letterSpacing: "0.15em",
            textTransform: "uppercase",
          }}
        >
          <div>judeo-arabic-app.vercel.app</div>
          <div>For Hebrew readers</div>
        </div>
      </div>
    ),
    {
      ...size,
      fonts: hebrewFont
        ? [{ name: "Noto Hebrew", data: hebrewFont, style: "normal", weight: 500 }]
        : undefined,
    },
  );
}
