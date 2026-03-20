# Second Chair Brand Design System

**Last Updated:** March 2026
**Locked visual source:** `14_Visual_Identity/` (Color System, Typography System, Logo Directions)
**Brand strategy source:** `13_Brand_Strategy/03_Brand_Architecture/Brand_Architecture.md`
**Scope:** B2B brand (parent brand) visual standards

---

## Overview

Second Chair's visual identity communicates institutional authority, honesty, and craft. The design system is derived from the prestige legal world — not from digital trends, competitive gap analysis, or tech startup conventions.

**Design Philosophy:**
- **Cinematic. Not naturalistic.** Intentionally produced. The craft is visible. The care is visible.
- Authority through typography, not color — hierarchy must be fully legible in black-and-white
- Cream replaces white as the base surface — never use pure white (#FFFFFF)
- Restraint as a distinctive asset — what we don't show matters as much as what we do

**Visual Direction (from Creative Brief):**
The claimant's world — a kitchen, a car, an evening — elevated to the emotional register of the decision being made. This is not found footage. It is not AI-generated content that tries to look like found footage. It is cinematic work that looks like someone who cared made it.

---

## Color Palette

> **Full specification:** `14_Visual_Identity/02_Color_System.md`

### Core Brand Colors

| Color | Hex | CSS Variable | Usage |
|-------|-----|-------------|-------|
| **Cream** | `#FFF7F0` | `--sc-cream` | Primary background — all documents, web, letterhead |
| **Burgundy / Oxblood** | `#490A0A` | `--sc-burgundy` | Primary accent — 0.5pt rules, chart accent, foil |
| **Warm Charcoal** | `#1C1917` | `--sc-charcoal` | Primary text — all body, headlines, captions |
| **Warm Grey** | `#6E6862` | `--sc-grey` | Supporting text — captions, footnotes, exhibit labels |
| **Oxford Navy** | `#0F1E3A` | `--sc-navy` | Foreground elements — not a field/background color |
| **Forest Green** | `#163A21` | `--sc-green` | Secondary variant — state-market material, print variants |
| **Old Gold** | `#E8C165` | `--sc-gold` | **Physical materials ONLY** — foil, embossing, engraving. Excluded from digital. |

### Color Usage Rules

- **Cream is the field.** All Second Chair content lives on cream. Never use pure white (#FFFFFF) as a background.
- **Burgundy is an accent, not a field.** Applied as 0.5pt horizontal rules, chart accents, foil. Never as a large background fill.
- **Warm Charcoal replaces pure black.** Never use #000000 — it reads as harsh and digital against cream.
- **Gold is physical only.** Contrast ratio on cream is ~1.6:1 (near-invisible on screen). Use only for foil stamping, embossing, letterpress.
- **No gradients of any kind.** Transitions are opacity and position, not color blending.

### WCAG Contrast

| Pair | Ratio | Rating |
|------|-------|--------|
| Charcoal on Cream | ~10.1:1 | AAA |
| Navy on Cream | ~9.8:1 | AAA |
| Burgundy on Cream | ~7.4:1 | AA (all text) |
| Grey on Cream | ~2.8:1 | Captions/labels at 9pt+ only |

### The 99%/1% Mandate as Visual Constraint

Under Meta Special Ad Categories, creative is the only targeting mechanism. Visual design must produce ads specific enough that the 1% self-select in while the 99% self-select out. Generic stock imagery fails this test.

---

## Typography

> **Full specification:** `14_Visual_Identity/03_Typography_System.md`
> **Selected option:** Option C — "The Law Review"

### Font Stack

| Role | Typeface | Source | CSS Variable |
|------|----------|--------|-------------|
| **Display / Headlines** | Tiempos Headline | Klim Type Foundry (klim.co.nz) | `--font-display` |
| **Body** | Adobe Caslon Pro (fallback for Hoefler Text) | Adobe Fonts | `--font-classic`, `--font-body` |
| **UI / Metadata** | Söhne | Klim Type Foundry (klim.co.nz) | `--font-ui` |
| **Monospace** | IBM Plex Mono | Google Fonts / IBM | `--font-mono` |

### Type Scale (Option C)

| Role | Typeface | Weight | Size | Leading | Tracking | Case |
|------|----------|--------|------|---------|----------|------|
| Display (cover, hero) | Tiempos Headline | Bold | 48–72pt | 110% | 0 | Title case |
| H1 (section title) | Tiempos Headline | Bold | 24–32pt | 120% | 0 | Title case |
| H2 (subsection) | Adobe Caslon Pro | Regular, small caps | 14–16pt | 130% | +25 | ALL SMALL CAPS |
| H3 (sub-subsection) | Adobe Caslon Pro | Italic | 11–12pt | 140% | 0 | Title case |
| Body | Adobe Caslon Pro | Regular | 10–11pt | 150% | 0 | Sentence case |
| Caption | Söhne | Regular | 8–9pt | 130% | +5 | ALL CAPS |
| Exhibit label | Adobe Caslon Pro | Regular, small caps | 7–8pt | 120% | +15 | "EXHIBIT N:" |
| Running head/folio | Söhne | Regular | 7–8pt | 120% | +5 | ALL CAPS |
| UI label | Söhne | Regular | 11–13pt | 130% | +5 | Title case |

### Typography Rules

- **True optical small caps only.** CSS faux small caps (scaled-down capitals) are not acceptable. Use OpenType `smcp` feature.
- **Hierarchy through typography, not color.** System must be legible in B&W. Color (Burgundy) for structural elements only.
- **The Exhibit convention:** "EXHIBIT N:" in Adobe Caslon Pro small caps, 8pt, Warm Grey — on every chart, table, data point. Non-negotiable.
- **Old-style figures** in body text (OpenType `onum`).
- **Column width:** 60–75 characters per line (Bringhurst optimum).

---

## Layout Patterns

### Document Header Structure (All Contexts)

```
[RUNNING HEAD in Söhne ALL CAPS, 7.5pt, Warm Grey — above 0.5pt Burgundy rule]

[SECTION TITLE in Caslon small caps, 15pt, Charcoal]

[HEADLINE in Tiempos Bold, 28–32pt, Charcoal]

[Body paragraph in Caslon Regular, 10.5pt, Charcoal, 16pt leading]

[Caption in Söhne ALL CAPS, 8pt, Warm Grey — below 0.5pt Burgundy rule]
```

### Grid & Spacing
- Generous margins — minimum 1.5" print, minimum 40px digital
- Clear vertical rhythm with consistent leading
- Content-first, decoration-last
- Scale differential: Display 2–3x larger than body (substantial, not subtle)

### Structural Elements
- **Burgundy rules (0.5pt)** as primary structural dividers — same weight across all applications
- **No decorative elements** that don't derive from a physical object in the prestige legal world
- **Alignment:** Left-aligned text for readability. Centered for impact statements only.

---

## UI Patterns

### Buttons / CTAs
- **Primary:** Warm Charcoal background, Cream text. Hover: Navy background.
- No heavy shadows or gradients
- Action-oriented text, ample padding

### Cards / Containers
- Subtle borders (Grey) or cream surface variations
- No heavy drop shadows
- Information hierarchy within cards

### Navigation
- Clean, minimal header
- Professional, restrained

---

## Competitive Context

**vs. Generic Lead Gen Companies:**
- Category convention: Navy backgrounds, grey, white, red, aggressive SaaS colors
- Second Chair: Cream backgrounds, Burgundy accents, editorial typography
- Burgundy is permanently unclaimed territory in PI lead gen — zero competitive interference

**Why This Works:**
- Signals institutional authority, not startup energy
- Stands out from crowded, noisy category through restraint
- Builds trust through craft that is visible and specific
- The attorney who sees this doesn't feel like they're being sold to

---

## CSS Design Tokens

```css
:root {
  /* Brand Colors */
  --sc-cream: #FFF7F0;
  --sc-burgundy: #490A0A;
  --sc-charcoal: #1C1917;
  --sc-grey: #6E6862;
  --sc-navy: #0F1E3A;
  --sc-green: #163A21;
  --sc-gold: #E8C165;

  /* Typography */
  --font-display: 'Tiempos Headline', 'Georgia', serif;
  --font-classic: 'Adobe Caslon Pro', 'Hoefler Text', 'Georgia', serif;
  --font-body: 'Adobe Caslon Pro', 'Hoefler Text', 'Georgia', serif;
  --font-ui: 'Söhne', 'Helvetica Neue', 'Arial', sans-serif;
  --font-mono: 'IBM Plex Mono', 'Courier New', monospace;

  /* Semantic Surfaces */
  --sc-surface-primary: var(--sc-cream);
  --sc-text-primary: var(--sc-charcoal);
  --sc-text-secondary: var(--sc-grey);
  --sc-border-brand: var(--sc-burgundy);
  --sc-accent-primary: var(--sc-burgundy);

  /* Button */
  --sc-button-bg: var(--sc-charcoal);
  --sc-button-text: var(--sc-cream);
  --sc-button-bg-hover: var(--sc-navy);
}
```

---

## Accessibility

- All text meets WCAG AA contrast requirements (AAA for primary text on cream)
- Font sizes readable at standard viewing distances
- Hierarchy supports screen readers
- Color is never the only indicator of meaning
- Warm Grey used only for captions/labels — never for body text (insufficient contrast)

---

## Related Files

- [`14_Visual_Identity/02_Color_System.md`](../14_Visual_Identity/02_Color_System.md) — Full color specification (locked)
- [`14_Visual_Identity/03_Typography_System.md`](../14_Visual_Identity/03_Typography_System.md) — Full typography system (locked)
- [`14_Visual_Identity/01_Logo_Directions.md`](../14_Visual_Identity/01_Logo_Directions.md) — Logo direction options
- [`13_Brand_Strategy/03_Brand_Architecture/Brand_Architecture.md`](../13_Brand_Strategy/03_Brand_Architecture/Brand_Architecture.md) — Brand architecture (locked)
- [`BRAND_POSITIONING_CORE.md`](../01_Identity/BRAND_POSITIONING_CORE.md) — Full positioning
