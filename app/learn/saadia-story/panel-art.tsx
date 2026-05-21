/**
 * SVG panel illustrations for /learn/saadia-story.
 *
 * Visual system:
 *   - 3:2 aspect (600 x 400 viewBox)
 *   - Mihrab-style arched cartouche around each scene
 *   - Palette restricted to: parchment bg, wine outline, ink accents
 *   - Silhouette + line-art style (no detailed faces, manuscript convention)
 */

const WINE = "var(--color-wine, #722f37)";
const WINE_DARK = "var(--color-wine-700, #5c252c)";
const INK = "var(--color-ink, #1c1a17)";
const MUTED = "var(--color-muted, #6b6357)";
const WINE_LIGHT = "var(--color-wine-100, #f2dddf)";

/** Shared mihrab-arch cartouche. Children render inside the arch (x:60–540, y:60–340). */
function Cartouche({ children }: { children: React.ReactNode }) {
  return (
    <svg
      viewBox="0 0 600 400"
      className="w-full h-auto"
      role="img"
      xmlns="http://www.w3.org/2000/svg"
    >
      {/* outer parchment background — slight inset */}
      <rect
        x="10"
        y="10"
        width="580"
        height="380"
        rx="2"
        fill="var(--color-parchment, #faf8f3)"
      />
      {/* mihrab arch: pointed at top, columns on sides, base bar */}
      {/* sides + base */}
      <path
        d="M 60 90
           L 60 340
           L 540 340
           L 540 90"
        fill="none"
        stroke={WINE}
        strokeWidth="2"
      />
      {/* horseshoe arch */}
      <path
        d="M 60 90
           C 60 40, 540 40, 540 90"
        fill="none"
        stroke={WINE}
        strokeWidth="2"
      />
      {/* keystone ornament at apex */}
      <circle cx="300" cy="52" r="4" fill={WINE} />
      <circle cx="300" cy="38" r="2.5" fill={WINE} />
      {/* corner ornaments — small lozenges */}
      <g fill={WINE}>
        <rect x="55" y="335" width="10" height="10" transform="rotate(45 60 340)" />
        <rect x="535" y="335" width="10" height="10" transform="rotate(45 540 340)" />
      </g>
      {/* clip the scene to the inside of the arch */}
      <clipPath id="arch-clip">
        <path
          d="M 60 340
             L 60 90
             C 60 40, 540 40, 540 90
             L 540 340 Z"
        />
      </clipPath>
      <g clipPath="url(#arch-clip)">{children}</g>
    </svg>
  );
}

// Panel 1 — Baghdad market, ~920 CE
export function Panel1Art() {
  return (
    <Cartouche>
      {/* sky gradient suggestion (no actual gradient — flat) */}
      <rect x="60" y="40" width="480" height="200" fill={WINE_LIGHT} opacity="0.4" />
      {/* horizon line */}
      <line x1="60" y1="240" x2="540" y2="240" stroke={WINE} strokeWidth="1" />
      {/* skyline silhouettes — domes, minaret, walls */}
      {/* left wall + dome */}
      <path
        d="M 80 240 L 80 180 L 130 180 L 130 240 Z"
        fill={INK}
      />
      <path
        d="M 110 180 C 110 150, 150 150, 150 180 L 110 180 Z"
        fill={INK}
      />
      <rect x="128" y="160" width="4" height="20" fill={INK} />
      {/* minaret */}
      <rect x="180" y="120" width="14" height="120" fill={INK} />
      <path d="M 178 120 L 196 120 L 196 110 L 178 110 Z" fill={INK} />
      <path d="M 187 110 L 180 95 L 194 95 Z" fill={INK} />
      <circle cx="187" cy="92" r="2" fill={INK} />
      {/* central larger dome */}
      <path d="M 230 240 L 230 200 L 360 200 L 360 240 Z" fill={INK} />
      <path
        d="M 240 200 C 240 150, 350 150, 350 200 L 240 200 Z"
        fill={INK}
      />
      <rect x="293" y="135" width="4" height="20" fill={INK} />
      <circle cx="295" cy="132" r="3" fill={INK} />
      {/* right palm tree */}
      <rect x="430" y="170" width="4" height="70" fill={WINE_DARK} />
      <path
        d="M 432 170
           C 415 165, 405 145, 412 140
           M 432 170
           C 449 165, 460 145, 453 140
           M 432 170
           C 425 158, 410 158, 405 162
           M 432 170
           C 440 158, 455 158, 460 162"
        fill="none"
        stroke={WINE_DARK}
        strokeWidth="2"
        strokeLinecap="round"
      />
      {/* small right building */}
      <rect x="475" y="200" width="50" height="40" fill={INK} />
      <path d="M 472 200 L 528 200 L 500 188 Z" fill={INK} />
      {/* ground market — figures */}
      <rect x="60" y="240" width="480" height="100" fill="var(--color-parchment, #faf8f3)" />
      {/* a couple of robed figures (silhouettes) */}
      <g fill={WINE_DARK}>
        <ellipse cx="180" cy="280" rx="12" ry="20" />
        <ellipse cx="180" cy="262" rx="6" ry="6" />
        <ellipse cx="230" cy="285" rx="13" ry="22" />
        <ellipse cx="230" cy="266" rx="6" ry="6" />
        <ellipse cx="370" cy="278" rx="11" ry="18" />
        <ellipse cx="370" cy="261" rx="5" ry="5" />
      </g>
      {/* market stall — arched booth */}
      <g stroke={INK} strokeWidth="1.5" fill="none">
        <path d="M 290 290 L 290 270 C 290 260, 340 260, 340 270 L 340 290" />
        <line x1="285" y1="290" x2="345" y2="290" />
      </g>
      {/* ground hint texture */}
      <line x1="60" y1="335" x2="540" y2="335" stroke={MUTED} strokeWidth="0.5" />
    </Cartouche>
  );
}

// Panel 2 — Father at table with Tanakh
export function Panel2Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* back wall — arched window */}
      <path
        d="M 240 70 L 240 150 L 360 150 L 360 70 C 360 50, 240 50, 240 70 Z"
        fill={WINE_LIGHT}
        opacity="0.3"
        stroke={INK}
        strokeWidth="1.2"
      />
      <line x1="300" y1="50" x2="300" y2="150" stroke={INK} strokeWidth="0.8" />
      <line x1="240" y1="100" x2="360" y2="100" stroke={INK} strokeWidth="0.8" />
      {/* table */}
      <rect x="150" y="270" width="300" height="14" fill={WINE_DARK} />
      <rect x="160" y="284" width="6" height="56" fill={WINE_DARK} />
      <rect x="434" y="284" width="6" height="56" fill={WINE_DARK} />
      {/* open book on table */}
      <g>
        <path
          d="M 250 250 L 240 270 L 360 270 L 350 250 Z"
          fill="var(--color-parchment, #faf8f3)"
          stroke={INK}
          strokeWidth="1.2"
        />
        <line x1="300" y1="252" x2="300" y2="270" stroke={INK} strokeWidth="1" />
        {/* lines of text suggestion */}
        <line x1="252" y1="258" x2="293" y2="258" stroke={MUTED} strokeWidth="0.8" />
        <line x1="252" y1="263" x2="293" y2="263" stroke={MUTED} strokeWidth="0.8" />
        <line x1="307" y1="258" x2="348" y2="258" stroke={MUTED} strokeWidth="0.8" />
        <line x1="307" y1="263" x2="348" y2="263" stroke={MUTED} strokeWidth="0.8" />
      </g>
      {/* oil lamp */}
      <g>
        <ellipse cx="420" cy="250" rx="18" ry="6" fill={WINE_DARK} />
        <ellipse cx="420" cy="250" rx="14" ry="3" fill={INK} />
        {/* flame */}
        <path
          d="M 408 248 C 405 240, 411 232, 410 244 Z"
          fill={WINE}
        />
      </g>
      {/* father — seated left, leaning forward, hand to head */}
      <g fill={INK}>
        <ellipse cx="195" cy="200" rx="16" ry="22" />
        <ellipse cx="195" cy="170" rx="13" ry="14" />
        {/* beard suggestion */}
        <path d="M 188 178 C 188 195, 202 195, 202 178" fill={WINE_DARK} />
        {/* arm reaching to forehead */}
        <path d="M 195 188 C 175 178, 165 170, 168 158 L 178 158 C 178 165, 188 175, 200 184 Z" />
      </g>
      {/* son — seated right, shrugging */}
      <g fill={INK}>
        <ellipse cx="405" cy="205" rx="14" ry="20" />
        <ellipse cx="405" cy="178" rx="11" ry="12" />
        {/* shrugged shoulders */}
        <path d="M 388 195 L 380 188 L 384 184 L 392 191 Z" />
        <path d="M 422 195 L 430 188 L 426 184 L 418 191 Z" />
      </g>
    </Cartouche>
  );
}

// Panel 3 — Karaite pamphlets / stack of codices
export function Panel3Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* base shadow */}
      <ellipse cx="300" cy="320" rx="170" ry="10" fill={MUTED} opacity="0.2" />
      {/* stack of codices */}
      <g>
        {/* bottom book */}
        <rect x="190" y="290" width="220" height="25" fill={WINE_DARK} stroke={INK} strokeWidth="1" />
        <line x1="190" y1="297" x2="410" y2="297" stroke={INK} strokeWidth="0.6" opacity="0.5" />
        <line x1="190" y1="309" x2="410" y2="309" stroke={INK} strokeWidth="0.6" opacity="0.5" />
        {/* middle book */}
        <rect x="205" y="260" width="200" height="30" fill={WINE} stroke={INK} strokeWidth="1" />
        <line x1="205" y1="268" x2="405" y2="268" stroke="var(--color-parchment, #faf8f3)" strokeWidth="0.6" opacity="0.7" />
        <line x1="205" y1="284" x2="405" y2="284" stroke="var(--color-parchment, #faf8f3)" strokeWidth="0.6" opacity="0.7" />
        {/* top book — slightly tilted */}
        <g transform="rotate(-4 300 240)">
          <rect x="215" y="225" width="170" height="30" fill={INK} />
          <line x1="220" y1="232" x2="380" y2="232" stroke={WINE_LIGHT} strokeWidth="0.6" />
          <line x1="220" y1="248" x2="380" y2="248" stroke={WINE_LIGHT} strokeWidth="0.6" />
        </g>
      </g>
      {/* wax seal on top — Star-of-David hexagram simplified */}
      <g transform="translate(300 180)">
        <circle r="32" fill={WINE} stroke={WINE_DARK} strokeWidth="1.5" />
        <path
          d="M 0 -18 L 16 9 L -16 9 Z M 0 18 L -16 -9 L 16 -9 Z"
          fill="none"
          stroke={WINE_LIGHT}
          strokeWidth="2"
        />
        <text
          x="0"
          y="3"
          textAnchor="middle"
          fontSize="14"
          fontFamily="serif"
          fill={WINE_LIGHT}
        >
          ק
        </text>
      </g>
      {/* small scroll above — slightly opened */}
      <g transform="translate(140 200)">
        <rect width="60" height="36" fill="var(--color-parchment, #faf8f3)" stroke={INK} strokeWidth="1" />
        <circle cx="0" cy="18" r="6" fill={WINE_DARK} />
        <circle cx="60" cy="18" r="6" fill={WINE_DARK} />
        <line x1="10" y1="12" x2="50" y2="12" stroke={MUTED} strokeWidth="0.6" />
        <line x1="10" y1="18" x2="50" y2="18" stroke={MUTED} strokeWidth="0.6" />
        <line x1="10" y1="24" x2="50" y2="24" stroke={MUTED} strokeWidth="0.6" />
      </g>
      {/* second scroll — opposite side */}
      <g transform="translate(400 195)">
        <rect width="60" height="40" fill="var(--color-parchment, #faf8f3)" stroke={INK} strokeWidth="1" />
        <circle cx="0" cy="20" r="6" fill={WINE_DARK} />
        <circle cx="60" cy="20" r="6" fill={WINE_DARK} />
        <line x1="10" y1="14" x2="50" y2="14" stroke={MUTED} strokeWidth="0.6" />
        <line x1="10" y1="20" x2="50" y2="20" stroke={MUTED} strokeWidth="0.6" />
        <line x1="10" y1="26" x2="50" y2="26" stroke={MUTED} strokeWidth="0.6" />
      </g>
    </Cartouche>
  );
}

// Panel 4 — Young Saadia in Fayyum at his desk
export function Panel4Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* window behind — palm + horizon */}
      <rect x="380" y="80" width="120" height="150" fill={WINE_LIGHT} opacity="0.35" stroke={INK} strokeWidth="1" />
      <line x1="440" y1="80" x2="440" y2="230" stroke={INK} strokeWidth="0.6" />
      <line x1="380" y1="155" x2="500" y2="155" stroke={INK} strokeWidth="0.6" />
      {/* horizon dunes in window */}
      <path
        d="M 380 200 C 400 192, 420 196, 440 200 C 460 204, 480 198, 500 202 L 500 230 L 380 230 Z"
        fill={WINE}
        opacity="0.5"
      />
      {/* palm tree in window */}
      <rect x="395" y="160" width="3" height="40" fill={WINE_DARK} />
      <path
        d="M 396 160 C 384 156, 376 144, 380 138 M 396 160 C 408 156, 416 144, 412 138 M 396 160 C 388 152, 376 154, 372 158 M 396 160 C 404 152, 416 154, 420 158"
        fill="none"
        stroke={WINE_DARK}
        strokeWidth="1.5"
        strokeLinecap="round"
      />
      {/* desk */}
      <rect x="100" y="270" width="280" height="12" fill={WINE_DARK} />
      <rect x="108" y="282" width="6" height="50" fill={WINE_DARK} />
      <rect x="366" y="282" width="6" height="50" fill={WINE_DARK} />
      {/* manuscript on desk */}
      <g>
        <rect x="180" y="255" width="160" height="18" fill="var(--color-parchment, #faf8f3)" stroke={INK} strokeWidth="1" />
        <line x1="190" y1="262" x2="330" y2="262" stroke={MUTED} strokeWidth="0.5" />
        <line x1="190" y1="266" x2="320" y2="266" stroke={MUTED} strokeWidth="0.5" />
      </g>
      {/* inkwell */}
      <g transform="translate(135 248)">
        <rect width="20" height="22" rx="2" fill={INK} />
        <ellipse cx="10" cy="2" rx="9" ry="3" fill={INK} />
      </g>
      {/* stack of books beside */}
      <g>
        <rect x="120" y="200" width="38" height="10" fill={WINE} />
        <rect x="115" y="210" width="48" height="10" fill={WINE_DARK} />
        <rect x="118" y="220" width="42" height="10" fill={INK} />
      </g>
      {/* young Saadia — seated, writing */}
      <g>
        {/* body */}
        <path
          d="M 250 245 C 235 245, 225 260, 228 285 L 272 285 C 275 260, 265 245, 250 245 Z"
          fill={INK}
        />
        {/* head */}
        <circle cx="250" cy="232" r="14" fill={INK} />
        {/* turban hint */}
        <path d="M 236 224 C 240 215, 260 215, 264 224 Z" fill={WINE} />
        {/* arm with quill */}
        <path
          d="M 255 260 L 285 252 L 295 250"
          stroke={INK}
          strokeWidth="6"
          strokeLinecap="round"
          fill="none"
        />
        {/* quill */}
        <path
          d="M 295 250 L 320 230"
          stroke={WINE_DARK}
          strokeWidth="2"
          strokeLinecap="round"
        />
        <path
          d="M 320 230 C 315 220, 318 218, 322 222"
          fill={WINE_DARK}
        />
      </g>
    </Cartouche>
  );
}

// Panel 5 — Saadia receiving the Gaonate
export function Panel5Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* canopy / chuppah-style top above the central figure */}
      <g>
        <path
          d="M 220 130 L 380 130 L 380 100 C 380 80, 220 80, 220 100 Z"
          fill={WINE}
        />
        {/* tassel */}
        <line x1="300" y1="80" x2="300" y2="65" stroke={WINE_DARK} strokeWidth="2" />
        <circle cx="300" cy="62" r="4" fill={WINE_DARK} />
        {/* canopy support poles */}
        <rect x="216" y="100" width="4" height="180" fill={WINE_DARK} />
        <rect x="380" y="100" width="4" height="180" fill={WINE_DARK} />
        {/* star atop canopy */}
        <g transform="translate(300 50)" fill={WINE} stroke={WINE_DARK} strokeWidth="1">
          <path d="M 0 -10 L 6 8 L -8 -2 L 8 -2 L -6 8 Z" />
        </g>
      </g>
      {/* central figure (Saadia, seated) */}
      <g>
        {/* throne / chair */}
        <rect x="270" y="230" width="60" height="80" fill={WINE_DARK} />
        <rect x="266" y="225" width="68" height="10" fill={WINE} />
        {/* body */}
        <path
          d="M 300 195 C 282 195, 272 215, 275 250 L 325 250 C 328 215, 318 195, 300 195 Z"
          fill={INK}
        />
        {/* head */}
        <circle cx="300" cy="185" r="14" fill={INK} />
        {/* turban */}
        <path d="M 285 178 C 290 167, 310 167, 315 178 Z" fill={WINE} />
        {/* beard hint */}
        <path d="M 292 192 C 294 200, 306 200, 308 192" fill={WINE_DARK} />
      </g>
      {/* left flanking figure */}
      <g>
        <path
          d="M 150 240 C 138 240, 130 255, 132 285 L 168 285 C 170 255, 162 240, 150 240 Z"
          fill={INK}
          opacity="0.85"
        />
        <circle cx="150" cy="230" r="11" fill={INK} opacity="0.85" />
        <path d="M 139 224 C 142 216, 158 216, 161 224 Z" fill={WINE_DARK} opacity="0.85" />
      </g>
      {/* right flanking figure */}
      <g>
        <path
          d="M 450 240 C 438 240, 430 255, 432 285 L 468 285 C 470 255, 462 240, 450 240 Z"
          fill={INK}
          opacity="0.85"
        />
        <circle cx="450" cy="230" r="11" fill={INK} opacity="0.85" />
        <path d="M 439 224 C 442 216, 458 216, 461 224 Z" fill={WINE_DARK} opacity="0.85" />
      </g>
      {/* floor */}
      <line x1="60" y1="320" x2="540" y2="320" stroke={MUTED} strokeWidth="0.8" />
    </Cartouche>
  );
}

// Panel 6 — Open manuscript: Hebrew + Arabic facing pages
export function Panel6Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* desk surface */}
      <line x1="80" y1="320" x2="520" y2="320" stroke={MUTED} strokeWidth="0.8" />
      {/* open book — two pages */}
      <g>
        {/* page shadows beneath */}
        <ellipse cx="300" cy="305" rx="220" ry="12" fill={MUTED} opacity="0.25" />
        {/* left page (Hebrew side from reader POV, right-to-left script) */}
        <path
          d="M 90 110 L 90 290 C 90 285, 290 280, 300 290 L 300 105 C 290 110, 100 105, 90 110 Z"
          fill="var(--color-parchment, #faf8f3)"
          stroke={INK}
          strokeWidth="1.5"
        />
        {/* right page (Arabic side) */}
        <path
          d="M 300 105 L 300 290 C 310 280, 510 285, 510 290 L 510 110 C 500 105, 310 110, 300 105 Z"
          fill="var(--color-parchment, #faf8f3)"
          stroke={INK}
          strokeWidth="1.5"
        />
        {/* spine */}
        <line x1="300" y1="105" x2="300" y2="290" stroke={INK} strokeWidth="2" />
        {/* illuminated initial — left page */}
        <rect x="245" y="125" width="32" height="32" fill={WINE} />
        <text
          x="261"
          y="151"
          fontSize="22"
          textAnchor="middle"
          fill="var(--color-parchment, #faf8f3)"
          fontFamily="serif"
        >
          א
        </text>
        {/* text lines — left page (RTL feel, lines start from right margin) */}
        <g stroke={INK} strokeWidth="0.7" opacity="0.7">
          <line x1="120" y1="135" x2="240" y2="135" />
          <line x1="120" y1="148" x2="240" y2="148" />
          <line x1="120" y1="161" x2="240" y2="161" />
          <line x1="120" y1="174" x2="240" y2="174" />
          <line x1="105" y1="187" x2="280" y2="187" />
          <line x1="105" y1="200" x2="280" y2="200" />
          <line x1="105" y1="213" x2="280" y2="213" />
          <line x1="105" y1="226" x2="280" y2="226" />
          <line x1="105" y1="239" x2="280" y2="239" />
          <line x1="105" y1="252" x2="270" y2="252" />
          <line x1="105" y1="265" x2="220" y2="265" />
        </g>
        {/* illuminated initial — right page */}
        <rect x="323" y="125" width="32" height="32" fill={WINE_DARK} />
        <text
          x="339"
          y="151"
          fontSize="22"
          textAnchor="middle"
          fill="var(--color-parchment, #faf8f3)"
          fontFamily="serif"
        >
          أ
        </text>
        {/* text lines — right page */}
        <g stroke={INK} strokeWidth="0.7" opacity="0.7">
          <line x1="360" y1="135" x2="480" y2="135" />
          <line x1="360" y1="148" x2="480" y2="148" />
          <line x1="360" y1="161" x2="480" y2="161" />
          <line x1="360" y1="174" x2="480" y2="174" />
          <line x1="320" y1="187" x2="495" y2="187" />
          <line x1="320" y1="200" x2="495" y2="200" />
          <line x1="320" y1="213" x2="495" y2="213" />
          <line x1="320" y1="226" x2="495" y2="226" />
          <line x1="320" y1="239" x2="495" y2="239" />
          <line x1="320" y1="252" x2="485" y2="252" />
          <line x1="320" y1="265" x2="420" y2="265" />
        </g>
      </g>
      {/* quill resting across the book */}
      <g>
        <path
          d="M 480 90 L 380 280"
          stroke={WINE_DARK}
          strokeWidth="2"
          strokeLinecap="round"
        />
        <path
          d="M 480 90 C 470 80, 472 70, 488 78 C 482 84, 482 88, 480 90 Z"
          fill={WINE_DARK}
        />
        <path
          d="M 480 90 C 488 84, 494 78, 500 86 C 492 92, 484 92, 480 90 Z"
          fill={WINE_DARK}
        />
      </g>
    </Cartouche>
  );
}

// Panel 7 — Calligraphic flourish around the first verse
// (Used decoratively; the verse text is rendered as React text on the page.)
export function Panel7Art() {
  return (
    <Cartouche>
      <rect x="60" y="40" width="480" height="300" fill="var(--color-parchment, #faf8f3)" />
      {/* decorative flourishes — interlace + foliate */}
      <g stroke={WINE} strokeWidth="1.5" fill="none">
        {/* top scroll */}
        <path d="M 150 110 C 180 90, 220 90, 250 110 C 280 130, 320 130, 350 110 C 380 90, 420 90, 450 110" />
        <path d="M 175 110 C 175 105, 185 105, 185 110" />
        <path d="M 415 110 C 415 105, 425 105, 425 110" />
        {/* bottom scroll mirrored */}
        <path d="M 150 290 C 180 310, 220 310, 250 290 C 280 270, 320 270, 350 290 C 380 310, 420 310, 450 290" />
        <path d="M 175 290 C 175 295, 185 295, 185 290" />
        <path d="M 415 290 C 415 295, 425 295, 425 290" />
      </g>
      {/* center ornament — six-pointed star within roundel */}
      <g transform="translate(300 200)">
        <circle r="56" fill="none" stroke={WINE} strokeWidth="1.5" />
        <circle r="42" fill="none" stroke={WINE} strokeWidth="0.8" />
        <g stroke={WINE_DARK} strokeWidth="1.5" fill="none">
          <path d="M 0 -32 L 28 16 L -28 16 Z" />
          <path d="M 0 32 L -28 -16 L 28 -16 Z" />
        </g>
        <circle r="6" fill={WINE} />
      </g>
      {/* corner foliage */}
      <g stroke={WINE_DARK} strokeWidth="1.2" fill="none" opacity="0.7">
        <path d="M 90 130 C 105 125, 115 140, 110 155" />
        <path d="M 510 130 C 495 125, 485 140, 490 155" />
        <path d="M 90 270 C 105 275, 115 260, 110 245" />
        <path d="M 510 270 C 495 275, 485 260, 490 245" />
      </g>
    </Cartouche>
  );
}
