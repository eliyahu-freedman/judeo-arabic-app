# Saadia Story — AI image prompts

Drop-in prompts for replacing the SVG illustrations on `/learn/saadia-story`
with AI-generated art. Designed for **Midjourney v6+ / Sora / GPT Image /
Imagen 3**.

## House style (paste at the top of every generation)

> Stylized editorial illustration in a manuscript-illumination aesthetic.
> Limited palette: deep wine red (#722f37), warm parchment (#faf8f3), and
> ink (#1c1a17). Flat, decorative, **no photorealism, no AI sheen.** Think
> *Aharon April / Ben Shahn / 1950s Hebrew children's-book woodcut*, not
> Midjourney default fantasy. **No Latin lettering, no Latin alphabet
> anywhere in the image.** No watermarks. 3:2 aspect ratio. Generously
> framed with negative space — the illustration sits inside a mihrab-style
> arched cartouche.

Append to every prompt: `--ar 3:2 --style raw --stylize 100` *(Midjourney)*
or `aspect ratio 3:2, stylized illustration, not photorealistic` *(others)*.

---

## Panel 1 — Baghdad market

> A 10th-century Baghdad marketplace at dawn. Stylized cityscape silhouette
> in deep wine red against a warm parchment sky — domes, minarets, a tall
> minaret with crescent finial, palm trees in silhouette. Foreground: two
> robed figures with their backs to us, walking toward a market stall with
> an arched canopy. Style: woodcut / editorial illustration / Ben Shahn,
> two-color flat illustration, **NO Latin lettering**, NO faces visible,
> mihrab-arched composition.

**Notes for review:** check that there's no Latin signage, no Arabic
calligraphy in script (we don't want fake words). Domes should look
Mesopotamian, not generic-fantasy.

---

## Panel 4 — Young Saadia in Fayyum

> A young scholar around 25 years old, seated cross-legged at a low wooden
> writing desk in 9th-century Egypt. He wears a simple turban and dark
> robe; his face is in three-quarter profile, looking down at parchment.
> A quill in his right hand, an inkwell beside him, a stack of three
> leather-bound codices to his left. Through an arched window behind him:
> a flat horizon, one date palm, suggestions of Fayyum dunes at sunset in
> deep wine tones. Style: stylized editorial illustration / 1950s Hebrew
> children's-book woodcut, two-color flat illustration in wine + parchment
> + ink only, **NO Latin lettering**, peaceful concentration, NOT
> photorealistic.

**Notes for review:** scholar should look young (early 20s, not bearded
elder). No Latin or Arabic visible in the manuscript he's writing on
(blank parchment is fine). Avoid Orientalist clichés — no harem, no
hookahs.

---

## Panel 5 — Saadia receives the Gaonate, 928 CE

> A formal investiture scene in a 10th-century Iraqi rabbinic academy.
> Center: a seated figure on a wooden throne under a wine-red embroidered
> canopy (chuppah-style, with a tassel), wearing a turban and dark robe,
> face in three-quarter profile, hands folded. Flanking him on either side
> at slightly smaller scale: two older bearded rabbinic figures, standing,
> facing the central seated one — they appear to be presenting him with
> the office. A six-pointed star ornament sits at the top of the canopy.
> Style: stylized editorial illustration / medieval Jewish manuscript
> illumination, two-color flat illustration in wine + parchment + ink
> only, **NO Latin lettering**, no Arabic script visible, ceremonial
> composition, NOT photorealistic.

**Notes for review:** the central figure should look ~45-50 (his actual
age in 928, not young). No Christian iconography (no halos). The two
flanking figures should look older / respectful, not subservient.

---

## Panel 6 — Open manuscript, Hebrew + Arabic

> An open codex resting on a wooden surface, viewed from slightly above.
> The book is opened to two facing pages: the right page is filled with
> dense **horizontal lines of script** (suggesting Hebrew, RTL — but no
> actual letters, just rhythmic horizontal strokes); the left page is the
> same but with a slightly different rhythm (suggesting Arabic). An
> illuminated initial in deep wine sits at the top of each page — one in
> wine, one in darker wine. A reed quill rests diagonally across the
> binding. The page edges show the warmth of aged parchment. Style:
> stylized editorial illustration / medieval Jewish-Islamic manuscript
> illumination, two-color flat illustration in wine + parchment + ink
> only, **NO Latin lettering**, NO recognizable Arabic or Hebrew letters
> (we don't want fake words — keep it abstracted to line-rhythm), NOT
> photorealistic.

**Notes for review:** the script should NOT be readable. If the AI
generates fake-Arabic or fake-Hebrew that looks real, regenerate. We want
clearly stylized horizontal strokes, not gibberish-script. The
illuminated initial blocks at the top of each page are the only colored
text-area.

---

## Recommended service order

1. **Midjourney v6.1** — best for the stylized woodcut look. Use
   `--style raw --stylize 100 --ar 3:2`. Iterate 4 times per panel.
2. **GPT Image (OpenAI)** — good for compositional control if Midjourney
   keeps adding fake letters. Slower but more accurate to instructions.
3. **Imagen 3 (Google)** — backup option, tends to add unwanted detail.

Avoid Stable Diffusion default models for this — they add Western/fantasy
flavor that doesn't match the site.

## Wiring the images in

When you have PNGs, drop them in `public/comic/`:

```
public/comic/panel-1.png
public/comic/panel-4.png
public/comic/panel-5.png
public/comic/panel-6.png
```

Then ping me and I'll switch those four `<Panel1Art />` calls in
`app/learn/saadia-story/page.tsx` to render `<img src="/comic/panel-1.png" />`
in place of the SVG, while leaving panels 2, 3, 7 (the decorative ones) on
SVG.
