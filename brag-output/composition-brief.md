# Hyperframes Composition Brief: Judeo-Arabic — A Digital Reader & Lexicon

## Objective

Create a short, prestige launch video for the Judeo-Arabic app — a free digital reader and tap-to-define lexicon for medieval Judeo-Arabic texts.

## Output

- Composition directory: `brag-output/composition/`
- Rendered video: `brag-output/brag.mp4`
- Format: landscape — 1920×1080
- Duration: 20 seconds

## Source Material

- Project root: `/Users/eliyahufreedman/Code/judeo-arabic-app/`
- Primary files read: `README.md`, `app/page.tsx`, `app/globals.css`, `app/tafsir/reader.tsx`
- Product name: **Judeo-Arabic**
- Tagline / strongest claim: "The medieval Judeo-Arabic library, read in the original."
- Key UI or visual moment to recreate: The Tafsir verse reader — verse card with Hebrew on top, Judeo-Arabic below, tap a word, lexicon panel slides in
- Copy that must appear verbatim:
  - "The medieval Judeo-Arabic library, read in the original."
  - "אול מא כ׳לק אללה" (Saadia Gaon's Tafsir, Genesis 1:1)
  - "אלסמאואת ואלארץ׳" (Genesis 1:1 continuation)
  - "SAADIA GAON · TAFSIR AL-TORAH · GENESIS 1:1"
  - "Saadia · Bahya · Rambam · Halevi"
  - "judeo-arabic-app.vercel.app"

## Creative Direction

- Tone preset: `polished`
- Creative direction: "ancient manuscript meets modern reader — understated scholarly prestige, slow reveal"
- Interpretation: Slow fades, generous holds, parchment warmth. No hype. No motion for motion's sake. Every reveal gives the text room to breathe. Typography is serifed and warm. Copy is minimal. The product's audacity — making a 10th-century manuscript readable by any Hebrew reader — is the punchline, not a joke. Treat the material with the gravity it deserves.
- Angle: Saadia Gaon translated the Torah into Arabic in 928 CE. It has been sitting, inaccessible, for a thousand years. This app makes it readable. Not a translation. The original.
- Hook: Full-screen wine red. Judeo-Arabic text of Genesis 1:1 materializes on screen — cream letters on deep red, like ink surfacing on vellum.
- Outro / punchline: Stats arrive one by one. Then the name — **Judeo-Arabic** — at full weight. A deep bell rings.
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Fast cuts or kinetic typography that break the scholarly register
  - Any motion that feels modern or tech-startup

## Visual Identity

- Background (hero/outro): `#faf8f3` (parchment)
- Background (manuscript scene 1): `#722f37` (wine)
- Accent: `#722f37` (wine)
- Text (primary): `#1c1a17` (ink)
- Text (muted): `#6b6357`
- Parchment cream for Judeo-Arabic text on wine background: `#faf8f3` at 95% opacity
- Ghost text: `#faf8f3` at 40% opacity
- Display font: Lora (load from Google Fonts — serif, used for headlines)
- Script font: Noto Serif Hebrew (load from Google Fonts — used for ALL Judeo-Arabic and Hebrew text, right-to-left)
- Arabic gloss font: Amiri (load from Google Fonts — used for any Arabic-script glosses in the lexicon panel)
- Visual references: wine + parchment manuscript section; subtle atmospheric radial gradient (wine tones); ghostly giant letterforms in the hero background

## Storyboard

Use `brag-output/brag-plan.md` as the creative contract.

Scene summary:
1. **Manuscript** — 4s — Wine background; Judeo-Arabic text of Gen 1:1 materializes in layers (text, ghost line, attribution); no SFX; music fades in at ~1.5s
2. **Claim** — 4s — Parchment; eyebrow + headline + stats appear sequentially; `drop_001.ogg` under stats arrival; music steady
3. **The Reader** — 8s — Recreated Tafsir verse card; simulated cursor taps two words in sequence; lexicon panel slides in twice; click + drop SFX; beat-lock card entrance near 8.74s strong cue
4. **Scale & Name** — 4s — Dark background; three stat lines arrive one by one; then **Judeo-Arabic** name at full weight; `impactBell_heavy_000.ogg` on name reveal; music fades; beat-lock stats near 17.47s, name near 22.93s

## Audio

- Audio role: warm, barely-there scholarly bed — barely audible beneath the visuals, like paper in a quiet library
- Audio arc: silence → faint music arrival at 1.5s → steady quiet bed through reader → fade to near-silence → bell rings on name → silence
- Music: `assets/music/happy-beats-business-moves-vol-12-by-ende-dot-app.mp3`
- Music treatment: fade in from 0 to 0.22 between 1.0–2.5s; hold at 0.22 through scenes 1–3; begin fade to 0.06 at ~17s; nearly inaudible under the closing bell
- Music cue guidance: Bundled preset at `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`. Strong cues to target: 8.74s (0.99) → Tafsir card entrance; 17.47s (0.99) → first stat line; 22.93s (1.00) → name reveal. Beat grid available for sequential stat spacing.
- Audio-reactive treatment: subtle; use music RMS/bass to gently breathe the wine background glow in scene 1, and to give the lexicon panel a hair of warm presence on bass. No waveform or equalizer visuals. Do not affect text legibility.
- Audio-coupled moments:
  - Scene 1 — no SFX; let the text materialise in silence into music
  - Scene 2 — `interface/drop_001.ogg` (soft) under the stats line arrival
  - Scene 3 — `ui/mouseclick1.ogg` (or `interface/click_001.ogg`) on each cursor word-tap; `interface/drop_001.ogg` as each lexicon panel slides in
  - Scene 4 — optional very soft `interface/drop_001.ogg` on each stat line; `impact/impactBell_heavy_000.ogg` at name reveal, volume 0.75; bell rings cleanly into near-silence
- SFX selection guidance: sparse and precise — 4–5 SFX total, chosen for polish not density. Prefer low HF-risk files. The bell is the loudest moment; everything else should be nearly imperceptible.
- SFX analysis guidance: `~/.claude/skills/brag/assets/sfx/sfx-analysis.md`
- Exact SFX choice: Hyperframes chooses filenames, timestamps, density, and volume based on the implemented animation.
- Audio files: copy chosen music and SFX into `brag-output/composition/assets/`

## Hyperframes Instructions

Use the current `hyperframes` skill and CLI workflow.

Requirements:
- Scene 1 must use the wine background (#722f37) with Judeo-Arabic text on it in parchment cream — this is the visual identity anchor of the video.
- The Tafsir reader simulation in scene 3 must show a real-looking verse card with Hebrew above and Judeo-Arabic below, plus a visible cursor tap and a lexicon panel (root, POS, English gloss).
- All text must be readable at the full scene duration (slow reveals, generous holds). Do not pull text off screen before it can be read.
- The Noto Serif Hebrew font must render correctly in RTL direction for all Judeo-Arabic and Hebrew text. Load from Google Fonts.
- Music enters slowly — do not start at full volume on frame 0.
- The bell SFX should ring cleanly at the name reveal with the music already faded, so it lands with full weight.
- Total duration is 20 seconds.
- Run lint and validate before render.
