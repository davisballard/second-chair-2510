# Typography: Second Chair

**Last Updated:** March 2026
**Locked source:** `14_Visual_Identity/03_Typography_System.md`
**Selected option:** Option C — "The Law Review"
**Brand character:** Expert not Arrogant, Honest in the Specific, Respectful of Intelligence, Weighted not Heavy

---

## Core Philosophy

Typography IS the identity. Before anyone reads a single word, the typeface has already communicated. The system must be legible in black-and-white — hierarchy through typography, not color.

**Visual direction:** Cinematic. Intentionally produced. The craft is visible. Not found footage, not "ugly ads win," not UGC-style. Cinematic work that looks like someone who cared made it.

---

## Primary Type System (Option C — "The Law Review")

### The Register

The Harvard Law Review redesigned by Upstatement. The American Lawyer at its peak. The modern legal editorial publication that carries 150 years of institutional authority while looking like it belongs in 2026.

### Font Stack

| Role | Typeface | Source | CSS Variable |
|------|----------|--------|-------------|
| **Display / Headlines** | Tiempos Headline | Klim Type Foundry (klim.co.nz) | `--font-display` |
| **Body / Classic** | Adobe Caslon Pro | Adobe Fonts (fallback for Hoefler Text) | `--font-classic`, `--font-body` |
| **UI / Metadata** | Söhne | Klim Type Foundry (klim.co.nz) | `--font-ui` |
| **Monospace** | IBM Plex Mono | Google Fonts / IBM | `--font-mono` |

### Why These Typefaces

**Tiempos Headline:** Warm curves + sharp details. Simultaneously historical (18th-century serif tradition) and unmistakably contemporary. "Could have appeared on a 1989 AmLaw 100 masthead, executed with 2026 precision."

**Adobe Caslon Pro:** Declaration of Independence face. Seventh Circuit brief guidelines recommend Caslon. "When in doubt, use Caslon." The New Yorker body text. Pro version required for genuine small caps, old-style figures, and ligatures.

**Söhne:** Refined Akzidenz Grotesk with warmth. Institutional without coldness. Why this instead of Inter: Inter is the category convention. Söhne is outside the category — warmer, less tech-adjacent.

**IBM Plex Mono:** For data labels, legal citations, code references, CPSC reporting.

---

## Type Scale

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
| Footnote | Adobe Caslon Pro | Regular | 8–9pt | 130% | 0 | Sentence case |
| UI label | Söhne | Regular | 11–13pt | 130% | +5 | Title case |

---

## Typography Rules

### Non-Negotiable

1. **True optical small caps only.** CSS faux small caps (scaled-down capitals) are not acceptable. Use OpenType `smcp` feature. Every attorney who clerked in federal court submitted briefs in true small caps — they will notice.

2. **Hierarchy through typography, not color.** Remove all color from a document — the hierarchy must still be completely clear. Color (Burgundy) is for structural elements (rules) only.

3. **The Exhibit convention.** "EXHIBIT N:" in Adobe Caslon Pro small caps, 8pt, Warm Grey (#6E6862), left-aligned, above every chart/table/data point. Non-negotiable. This is what makes Second Chair's data output immediately recognizable.

4. **Old-style figures** in body text (OpenType `onum`). They sit on the baseline like lowercase letters.

5. **Column width:** 60–75 characters per line (Bringhurst optimum).

6. **Leading:** 140–150% of point size for body text. Tighter for display (110–120%).

7. **Small caps tracking:** +25–35 units. Generous — small caps at tight tracking lose institutional quality.

### OpenType Features Required

| Feature | Code | Purpose |
|---------|------|---------|
| Small Caps | `smcp` | True optical small caps for H2, exhibit labels |
| Old-Style Figures | `onum` | Numerals in body text |
| Standard Ligatures | `liga` | fi, fl, etc. |

---

## Platform-Specific Typography

### Brand Materials (Documents, Decks, Website)

Use the full Tiempos / Caslon / Söhne system as specified above.

### Social Media Advertising (Platform-Native Modes)

For B2C advertising on Meta, platform-native typography may be more effective than brand typography. Two secondary modes are available:

**Native Mode (TikTok, Reels, Stories):**
- Use platform's native text tools — DO NOT burn in professional subtitles
- Native text reads as "content"; burnt-in text reads as "ad"
- Hook text: Large, centered, high contrast, upper-third of screen

**Lo-Fi Mode (Screenshot ads, government form aesthetic):**
- System fonts (SF Pro, Roboto) for screenshot mockups
- Courier New / Courier Prime for government form aesthetic
- Intentionally plain — the plainness IS the message

These modes are **secondary to the brand system** and used only where platform conventions require it.

### Disclosure Typography (COMPLIANCE)

| Attribute | Minimum Requirement |
|---|---|
| Font | Söhne Regular or Adobe Caslon Pro Regular |
| Size | 10px (8pt) minimum |
| Contrast | 4.5:1 ratio minimum |
| Placement | Visible, not hidden below fold |
| Weight | Regular — never light |

---

## Document Header Structure

```
[RUNNING HEAD in Söhne ALL CAPS, 7.5pt, Warm Grey — above 0.5pt Burgundy rule]

[SECTION TITLE in Caslon small caps, 15pt, Charcoal]

[HEADLINE in Tiempos Bold, 28–32pt, Charcoal]

[Body paragraph in Caslon Regular, 10.5pt, Charcoal, 16pt leading]

[Caption in Söhne ALL CAPS, 8pt, Warm Grey — below 0.5pt Burgundy rule]
```

This structure is legible in black-and-white. The only color: Burgundy rules (0.5pt) as structural dividers and Burgundy accent in data exhibits.

---

## CSS Implementation

```css
:root {
  /* Font Stacks */
  --font-display: 'Tiempos Headline', 'Georgia', serif;
  --font-classic: 'Adobe Caslon Pro', 'Hoefler Text', 'Georgia', serif;
  --font-body: 'Adobe Caslon Pro', 'Hoefler Text', 'Georgia', serif;
  --font-ui: 'Söhne', 'Helvetica Neue', 'Arial', sans-serif;
  --font-mono: 'IBM Plex Mono', 'Courier New', monospace;
}
```

### Font Sourcing

| Typeface | Source | Cost |
|----------|--------|------|
| Tiempos Headline | klim.co.nz | ~$200–400/weight (web+desktop) |
| Adobe Caslon Pro | Adobe Fonts (Creative Cloud) | Included in CC subscription |
| Söhne | klim.co.nz (same foundry as Tiempos) | Commercial license |
| IBM Plex Mono | Google Fonts / IBM | Free |

---

## Quick Reference

| Need | Use |
|------|-----|
| Document/deck headline | Tiempos Headline Bold |
| Section title (small caps) | Adobe Caslon Pro small caps |
| Body text | Adobe Caslon Pro Regular |
| Caption/label | Söhne Regular ALL CAPS |
| Exhibit label | Caslon Pro small caps, 8pt, Warm Grey |
| UI element | Söhne Regular |
| Data/code | IBM Plex Mono |
| Platform-native ad text | Platform tools (secondary mode) |
| Disclosure | Söhne Regular or Caslon Pro Regular, 10px min, 4.5:1+ contrast |

---

## Related Files

- [`14_Visual_Identity/03_Typography_System.md`](../14_Visual_Identity/03_Typography_System.md) — Full locked specification with all three options
- [`02_Visual/Color_Palette.md`](Color_Palette.md) — Color pairings for type
- [`02_Visual/BRAND_DESIGN_SYSTEM.md`](BRAND_DESIGN_SYSTEM.md) — Complete visual system
- [`03_Voice/Approved_Phrases.md`](../03_Voice/Approved_Phrases.md) — Copy to pair with typography
