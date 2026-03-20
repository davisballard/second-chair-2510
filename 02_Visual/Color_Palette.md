# Color Palette: Second Chair

**Last Updated:** March 2026
**Locked source:** `14_Visual_Identity/02_Color_System.md`
**Brand character:** Expert not Arrogant, Honest in the Specific, Respectful of Intelligence, Weighted not Heavy

---

## Color Strategy Overview

> Every color in this system has a physical origin — not a digital origin, not a trend reference. Cotton-rag letterhead (Cream), West Federal Reporter spine (Burgundy), courthouse limestone (Grey), brass door placard (Gold). Colors derived from things are not arbitrary.

### Brand Voice Alignment

Color communicates the brand's institutional authority and restraint. The category convention is navy, grey, white, red. Second Chair uses cream as the field and burgundy as the accent — permanently unclaimed territory in PI lead gen.

---

## Core Brand Colors

| Name | Hex | RGB | CSS Variable | Physical Origin |
|------|-----|-----|-------------|-----------------|
| **Cream** | `#FFF7F0` | R:245 G:240 B:232 | `--sc-cream` | Cotton-rag letterhead, Harvard Law Review paper |
| **Burgundy / Oxblood** | `#490A0A` | R:107 G:26 B:26 | `--sc-burgundy` | West Federal Reporter spine, oxblood leather chair |
| **Warm Charcoal** | `#1C1917` | R:44 G:44 B:44 | `--sc-charcoal` | Quality offset printing on cream paper |
| **Warm Grey** | `#6E6862` | R:140 G:134 B:128 | `--sc-grey` | Marble courthouse floors, Indiana limestone |
| **Oxford Navy** | `#0F1E3A` | R:27 G:42 B:74 | `--sc-navy` | Brooks Brothers suit, Oxford University Press binding |
| **Forest Green** | `#163A21` | R:30 G:77 B:43 | `--sc-green` | West state reporter spines, law school library |
| **Old Gold** | `#E8C165` | R:184 G:150 B:46 | `--sc-gold` | Brass door placards, West Reporter gold lettering |

---

## Usage Rules

### Cream (#FFF7F0) — Primary Background
- **THE field.** All Second Chair content lives on cream.
- Never use pure white (#FFFFFF) as a background — cream replaces white as the base.
- Digital: `background-color` on `body` and all primary surfaces.
- Print: Specify Pantone AND paper stock (Crane Lettra 110lb).
- **The cream test:** If you print on standard white laser paper, it should look wrong.

### Burgundy (#490A0A) — Primary Accent
- Applied as: 0.5pt horizontal rules, single chart accent, foil on physical covers.
- **Never as a field/background color.** Burgundy is not a background.
- Never paired with any shade of red or warm orange.
- 0.5pt weight is consistent across ALL applications.
- **Competitive status:** Zero PI lead gen vendors use burgundy. Permanently unclaimed.

### Warm Charcoal (#1C1917) — Primary Text
- All body text, headlines, captions, footnotes.
- **Why not pure black (#000000):** Pure black on cream reads as harsh, digital. Charcoal reads as warm, printed, quality.

### Warm Grey (#6E6862) — Supporting Text
- Captions, footnotes, exhibit labels, page folios, source attributions.
- **Never for body text** — insufficient contrast for extended reading (~2.8:1 on cream).

### Oxford Navy (#0F1E3A) — Foreground Element
- Text on cream, borders, structural elements.
- **Never as the primary field color.** Category convention is navy backgrounds — Second Chair does the opposite.

### Forest Green (#163A21) — Secondary Variant
- State-market material, physical variants of stationery.
- Digital: Use very sparingly. Primarily a print/physical color.

### Old Gold (#E8C165) — Physical Only
- **Excluded from all digital contexts.** Contrast on cream is ~1.6:1 (near-invisible on screen).
- Applied as: Foil stamping, embossing, engraving, letterpress on physical items.
- Reverse text on Navy backgrounds (Gold letters on Navy) for engraved items.

---

## WCAG Contrast Ratios

### On Cream (#FFF7F0)

| Text Color | Ratio | Rating |
|---|---|---|
| Warm Charcoal (#1C1917) | ~10.1:1 | AAA |
| Oxford Navy (#0F1E3A) | ~9.8:1 | AAA |
| Burgundy (#490A0A) | ~7.4:1 | AA (all text) |
| Warm Grey (#6E6862) | ~2.8:1 | Captions/labels at 9pt+ only |
| Old Gold (#E8C165) | ~2.7:1 | Fail — decorative/physical only |

---

## Creative Mode Color Systems

### Mode 1: Brand Standard (Documents, Website, B2B Materials)

| Element | Color | Hex |
|---------|-------|-----|
| Background | Cream | #FFF7F0 |
| Primary Text | Warm Charcoal | #1C1917 |
| Headlines | Warm Charcoal | #1C1917 |
| Supporting Text | Warm Grey | #6E6862 |
| Structural Rules | Burgundy | #490A0A |
| Accent | Burgundy | #490A0A |
| Buttons | Charcoal bg / Cream text | #1C1917 / #FFF7F0 |
| Button Hover | Navy bg | #0F1E3A |

### Mode 2: Platform-Native Advertising (Meta Feed, Video)

For B2C advertising under Special Ad Categories, platform-native color conventions may be appropriate where brand colors would reduce performance:

| Element | Approach |
|---------|----------|
| Text overlays | White with dark outline (platform convention) |
| Hook text | High contrast — white on dark video |
| CTA | Platform-native styling |
| Brand presence | Minimal — let the cinematic production carry the brand |

### Disclosure Color Requirements (COMPLIANCE)

| Attribute | Minimum |
|---|---|
| Contrast Ratio | 4.5:1 minimum for body text |
| Recommended | 7:1+ for maximum readability |

| Text Color | Background | Ratio | Use For |
|---|---|---|---|
| Charcoal (#1C1917) | Cream (#FFF7F0) | ~10.1:1 | Standard (preferred) |
| Charcoal (#1C1917) | White (#FFFFFF) | ~16:1 | Fallback contexts |

---

## Colors Permanently Excluded

| Color | Reason |
|-------|--------|
| Pure white (#FFFFFF) as background | Reads as photocopier paper |
| Pure black (#000000) as text | Too harsh against cream |
| Any blue as primary/accent on identity materials | Category convention — differentiation requires avoiding it |
| Saturated reds | Urgency/ambulance-chaser signal |
| Orange as primary | Consumer brand warmth — wrong register |
| Purple | No physical origin in prestige legal world |
| Gradients of any kind | Not part of the visual system |
| Neon / RGB-maximum saturation | Reads as backlit digital, not print quality |

---

## CSS Design Tokens

```css
:root {
  /* Brand Colors (Primitives) */
  --sc-cream: #FFF7F0;
  --sc-burgundy: #490A0A;
  --sc-charcoal: #1C1917;
  --sc-grey: #6E6862;
  --sc-navy: #0F1E3A;
  --sc-green: #163A21;
  --sc-gold: #E8C165;

  /* Semantic Tokens */
  --sc-surface-primary: var(--sc-cream);
  --sc-text-primary: var(--sc-charcoal);
  --sc-text-secondary: var(--sc-grey);
  --sc-text-inverse: var(--sc-cream);
  --sc-text-brand: var(--sc-burgundy);
  --sc-border-brand: var(--sc-burgundy);
  --sc-border-subtle: var(--sc-grey);
  --sc-accent-primary: var(--sc-burgundy);

  /* Button */
  --sc-button-bg: var(--sc-charcoal);
  --sc-button-text: var(--sc-cream);
  --sc-button-bg-hover: var(--sc-navy);
}
```

### Figma Setup

```
— BRAND COLORS —
SC / Cream         #FFF7F0    (Primary background)
SC / Burgundy      #490A0A    (Primary accent)
SC / Charcoal      #1C1917    (Primary text)
SC / Gold          #E8C165    (Physical only — foil, embossing)
SC / Navy          #0F1E3A    (Foreground elements)
SC / Green         #163A21    (Secondary variant)
SC / Grey          #6E6862    (Supporting text)
```

---

## Pre-Flight Checklist

Before publishing any brand material:

- [ ] Background is Cream (#FFF7F0), not white
- [ ] Text is Charcoal (#1C1917), not pure black
- [ ] Burgundy used as accent/rule only, not as field color
- [ ] Gold not used in any digital context
- [ ] No gradients
- [ ] Disclosure text has 4.5:1+ contrast ratio
- [ ] Overall feel: institutional authority through restraint, not aggressive or loud

---

## Related Files

- [`14_Visual_Identity/02_Color_System.md`](../14_Visual_Identity/02_Color_System.md) — Full locked specification with Pantone values, print specs, data viz palette
- [`02_Visual/Typography.md`](Typography.md) — Typography system
- [`02_Visual/BRAND_DESIGN_SYSTEM.md`](BRAND_DESIGN_SYSTEM.md) — Complete visual system
- [`05_Restrictions/Platform_Rules.md`](../05_Restrictions/Platform_Rules.md) — Platform restrictions
