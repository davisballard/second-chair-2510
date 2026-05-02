# Fair Case — Brand System Brief

**Date:** March 2026
**Status:** Locked. This document governs all brand applications outside the quiz form.
**Companion documents:**
- `FORM_DESIGN_BRIEF.md` — governs the quiz funnel specifically
- `BRAND_IDENTITY_SESSION_RECORD.md` — session record, color correction addenda, Massimo's locked brief

---

## The Core Logic

One palette. Two contexts. The same two colors swap roles depending on the background.

```
Dark context (homepage, social posts, full-bleed sections):
  Roman Navy bg → White headlines → Torch Amber accents

Light context (form, white homepage sections, testimonials):
  White bg → Roman Navy headlines + mark → Torch Amber CTA + accents
```

**Torch Amber is always the accent.** It is never the dominant headline color. Headlines are white on dark, Roman Navy on light. Amber draws the eye to specific, deliberate elements: the torch flame in the mark, the CTA button, a single highlighted word, a stat number, an underline, an icon fill. Its power comes from restraint — one amber element on a navy page is a signal. Three amber elements is noise.

**The torch mark is the proof of concept.** Roman Navy body, Torch Amber flame. The brand palette IS the object. Every application of color in the system should feel like it could be explained the same way.

---

## Color Palette

| Name | Hex | Role |
|---|---|---|
| Roman Navy | `#0D1F3C` | Primary background (dark context), headlines (light context), mark/wordmark |
| Torch Amber | `#C8821A` | Accent — CTA button fill, torch flame, callout elements, single accent words |
| Torch Amber Dark | `#A86A10` | CTA hover state only |
| White | `#FFFFFF` | Headlines + body (dark context), background (light context) |
| Muted Navy Light | `#A8B8CC` | Secondary / caption text on dark backgrounds |
| Body Gray | `#374151` | Body copy on white backgrounds |
| Form Gray Light | `#6B7280` | Helper text, micro-copy, TCPA language |

---

## Typography

### The Two Typefaces

**Tiempos** — the brand voice. Humanist serif. Used for everything that speaks as the brand.
**Inter** — the functional voice. Humanist sans-serif. Used for everything that serves the user.

These are not in competition. They are different registers. Tiempos says "we built this." Inter says "here's what you need to do."

### Role Assignment

| Element | Typeface | Weight | Notes |
|---|---|---|---|
| H1 / Hero headline | Tiempos | Medium or Semibold | The brand speaking. |
| H2 / Section headline | Tiempos | Regular or Medium | Stays in the brand register. |
| Pull quote | Tiempos | Regular, italic | Emotional emphasis. |
| Wordmark ("Fair Case") | Tiempos | Medium | Only instance in the form UI. |
| H3 / Sub-section | Inter | Semibold | Transitions to functional. |
| Body copy | Inter | Regular (400) | All running text. |
| Captions, labels | Inter | Regular (400) | Small, muted. |
| CTA button text | Inter | Semibold (600) | Action, not brand voice. |
| Form UI (all) | Inter | Various | See Form Design Brief. |

### The Rule

Tiempos handles the brand register: hero text, section headlines, pull quotes, the wordmark. Inter handles everything else. If an element is asking the user to do something or giving them information, it's Inter. If it's speaking as the brand, it's Tiempos.

---

## Dark Context — Homepage Hero, Full-Bleed Sections, Social Posts

This is the primary brand expression. Roman Navy dominant, white for all text, Torch Amber as the accent signal.

### Color Application

| Element | Color | Hex |
|---|---|---|
| Background | Roman Navy | `#0D1F3C` |
| H1 / H2 (Tiempos) | White | `#FFFFFF` |
| Body copy (Inter) | White | `#FFFFFF` |
| Secondary / caption text | Muted Navy Light | `#A8B8CC` |
| Torch Amber accent uses | Torch Amber | `#C8821A` |
| CTA button fill | Torch Amber | `#C8821A` |
| CTA button text | Roman Navy | `#0D1F3C` |
| Mark / wordmark | White version | `#FFFFFF` |

### Where Torch Amber Appears (Dark Context)

Amber is used for one or two of the following per section — not all at once:

- **The torch flame** in the mark (always amber, regardless of context)
- **A single accent word** within a headline — one word set in amber to carry the emotional weight of the sentence. Example: "You deserve *fair*." — "fair" in amber, rest in white. Use sparingly; most headlines are entirely white.
- **A short label or eyebrow text** above a headline — "Free. In minutes." in amber above a white H1
- **A stat number or key figure** — "93%" in amber with white label below
- **A horizontal rule or divider** in amber between sections
- **Icon fills** — torch icons, checkmarks, small decorative elements

### What Amber Does NOT Do (Dark Context)

- Full headlines in amber — too styled, reads as a brand theme not a quality brand
- Multiple amber text elements on the same screen
- Amber body copy — illegible and overwhelming

---

## Light Context — White Homepage Sections, Testimonials, White Cards

Used when the page needs to breathe or when content is text-heavy and requires high legibility at length.

### Color Application

| Element | Color | Hex |
|---|---|---|
| Background | White | `#FFFFFF` |
| H1 / H2 (Tiempos) | Roman Navy | `#0D1F3C` |
| Body copy (Inter) | Body Gray | `#374151` |
| Secondary text | Form Gray Light | `#6B7280` |
| CTA button fill | Torch Amber | `#C8821A` |
| CTA button text | Roman Navy | `#0D1F3C` |
| Mark / wordmark | Roman Navy version | `#0D1F3C` |

### Where Torch Amber Appears (Light Context)

- **CTA button** — same as form; amber fill, navy text
- **Underlines on linked headlines** or key terms
- **Icon fills** — checkmarks in a feature list, small torch icons
- **Callout box borders** — a left-border on a pull quote or stat callout
- **A highlighted stat or number** — "Free case review in 3 minutes" with "3 minutes" in amber

---

## The Mark in Brand Contexts

The Fair Case mark is a two-color combination lockup: torch symbol + "Fair Case" wordmark in Tiempos.

### Mark Color Variants

| Context | Mark Color | When |
|---|---|---|
| On Roman Navy background | White mark, Torch Amber flame | Homepage hero, social posts, dark sections |
| On white background | Roman Navy mark, Torch Amber flame | Form header, white homepage sections, letterhead |
| On Torch Amber background | Roman Navy mark, Roman Navy flame | Edge case — avoid unless tested |
| On photography | White mark with Roman Navy or dark overlay | Ad creative, video watermarks |

### Mark Usage Rules

- The torch flame is always Torch Amber — in every version, on every background. This is the one invariant.
- The mark does not animate in brand contexts (it may have a subtle entrance animation on the homepage, but no loop or hover animation).
- Minimum clear space: equal to the height of the "F" in the wordmark on all sides.
- Do not stretch, rotate, recolor (outside the approved variants), or place on a busy background without an overlay.

---

## Homepage Architecture

The homepage serves one purpose: move the visitor to the quiz form. It is not a brand awareness exercise. Every section exists to handle an objection or build enough trust that she clicks "Get My Free Case Review."

### Recommended Section Structure

**1. Hero (Dark — Roman Navy)**
Full-bleed Roman Navy. White Tiempos headline. Torch Amber as a single accent element (a word, a label, a stat). CTA button. The mark at top-left or top-center.

The headline is the strategic message — the one thing the brand needs to communicate before she does anything else. "You deserve a fair case." Not a feature list. Not a guarantee. The emotional truth.

**2. How It Works (Light — White)**
Three-step explainer. Roman Navy Tiempos H2. Inter body. Torch Amber checkmarks or step numbers. This is where she learns what will happen when she clicks. Objection handled: "What am I signing up for?"

**3. What You Could Recover (Dark or Light)**
The value proposition in concrete terms — not promises, but ranges. "Personal injury settlements in [state] average $X." Anchored to her situation. Torch Amber for the key figures.

**4. It's Free. Always. (Light)**
The cost objection addressed directly. Attorneys work on contingency. No upfront cost. Ever. Roman Navy headline, Inter body, clear and simple. This is not a section that needs visual drama — clarity is the design.

**5. CTA / Form Entry (Dark)**
The final push before the quiz loads or the form embeds. Roman Navy background. Strong white headline. One amber CTA button. Nothing else.

---

## Social Posts — System

Social posts use the dark context as the primary template. Roman Navy background, white type, Torch Amber accent.

### Post Anatomy

**Header area:** The mark (white version with amber flame) in the top-left or top-center.

**Headline:** Tiempos, white, large. One to six words. The idea, not the explanation.

**Torch Amber accent:** One element — an underline under the headline, a short amber label above it ("Know this."), a stat number in amber, or a decorative divider.

**Body / supporting copy:** Inter, white or muted `#A8B8CC`, smaller. The context for the headline. Optional — many posts are headline only.

**Footer / handle:** `@getafaircase` in Inter, muted, bottom of the post.

### Post Types

| Type | Tiempos headline | Amber accent | Body copy |
|---|---|---|---|
| Stat post | Large number or % | The number itself | Explanation in Inter below |
| Myth/fact | "Myth:" or "Fact:" as amber eyebrow | The label | Headline in white Tiempos |
| Rights reminder | Short declarative statement | Underline or amber word | Optional Inter sub-copy |
| Quote / testimony | The quote in Tiempos | Amber quotation mark or attribution line | Attribution in Inter, muted |
| CTA post | "Find out in minutes." | Amber short label above | Handle + URL in footer |

### What Social Posts Do NOT Do

- Bright, colorful backgrounds (no gradient, no off-brand color)
- Mixed typefaces beyond Tiempos + Inter
- Multiple amber elements competing on the same post
- Stock photography as the primary visual (if photography is used, it is in the Style C / restrained cinematic register — see `B2C_CREATIVE_PRODUCTION_BRIEF.md`)

---

## Design Tokens — Full System

These extend the form tokens. All form tokens remain unchanged.

```css
/* Brand — Core */
--color-roman-navy:        #0D1F3C;
--color-torch-amber:       #C8821A;
--color-torch-amber-dark:  #A86A10;

/* Text */
--color-text-white:        #FFFFFF;
--color-text-muted-navy:   #A8B8CC;   /* secondary text on dark backgrounds */
--color-text-body:         #374151;   /* body copy on white backgrounds */
--color-text-muted:        #6B7280;   /* captions, helper text */

/* Backgrounds */
--color-bg-dark:           #0D1F3C;   /* Roman Navy — dark sections */
--color-bg-light:          #FFFFFF;   /* white — light sections */
--color-bg-warm:           #FAFAF7;   /* warm off-white — form test B, subtle warmth */

/* Typography */
--font-brand:              'Tiempos', Georgia, serif;
--font-ui:                 'Inter', system-ui, sans-serif;
```

---

## Ad Creative Overlay Rule (added 2026-04-25)

Fair Case's color palette is built for landing-page, form, and brand-identity contexts — surfaces where the background is fully under our control. **It is NOT a video-overlay palette.** Roman Navy `#0D1F3C` and Torch Amber `#C8821A` cannot serve as letter-fill for headlines sitting over warm-graded video footage: Roman Navy reads as a low-contrast murky letter against most documentary grades, and Torch Amber dies in the warm/amber zone of typical client footage.

For ad creative — every video ad running under the Fair Case brand for any client — the rule is:

| Layer | Palette | Source |
|-------|---------|--------|
| Hook Card / Peak Card / on-video headlines / kinetic captions | **SC parent overlay palette**: Cream `#FFF7F0`, Warm Charcoal `#1C1917`, Burgundy `#490A0A` | `../../02_Visual/Designed_Overlay_System.md` §6 Patterns 4 + 5 |
| Final CTA frame (last 1.5s of the spot) | **Fair Case brand palette**: Roman Navy chip + Torch Amber CTA + torch mark | This document |
| Landing page / form (post-click) | **Fair Case brand palette** | This document + `FORM_DESIGN_BRIEF.md` |

This aligns with the production rule already in operation: Fair Case branding is added in the final CapCut pass at the CTA frame, never baked into Higgsfield generation or used as letter-fill in headline overlays.

### UGC Branding Exception

For UGC-register ads (where the visual register is iPhone-candid, not designed) — even the CTA frame deviates: **the torch mark does NOT appear in the ad creative itself.** The CTA reads as text-only `See Options` in Inter Bold with a single Torch Amber accent word. The torch mark and full Fair Case branding appear post-click on the landing page. Locked per `../../23_Clients/West_Coast_Trial_Lawyers/Creative/Week_1_Review_Upgrades/Agency_Creative_Review.md` (Massimo's UGC branding note).

### Why this rule exists

The Fair Case "two colors swap roles depending on background" logic was built for surfaces with controlled backgrounds. Ad creative places type over uncontrolled video footage. The SC parent overlay system already solves the over-video legibility problem with Cream + Warm Charcoal + Burgundy (anchored to Bass + Clair + the West Federal Reporter spine, etc., per `../../07_Research/04_Visual_Research/12_Designed_Overlay_System_Research/Research_Notes.md`). Fair Case ads inherit that solution for the headline layer; Fair Case's own palette stays where it belongs — at the CTA chip and on the form.

---

## The Anti-Rules

Things that look like they fit but don't:

**No amber backgrounds as a section fill.** Torch Amber is a button color and a flame color. A full amber background section looks like a warning banner. Never.

**No Tiempos in Inter's territory.** If an element is functional — a label, a form field, a nav link, button text — it's Inter. Tiempos in functional contexts reads as decorative, which undermines its authority in brand contexts.

**No Roman Navy text on white at small sizes with anything other than full weight.** Roman Navy is dark enough to work, but at 13px regular weight it can feel heavy. Use `#374151` for body copy on white — it's slightly lighter and reads more comfortably at length.

**No full pages of Roman Navy without a white section to breathe.** The homepage should alternate dark and light sections. All-navy reads as oppressive at length. The rhythm of dark and light is part of the design.

**Do not introduce a third typeface.** Tiempos + Inter is the system. Nothing else.

---

## Anchor Extension (added 2026-04-30)

The Fair Case brand palette is built for landing-page and form contexts — controlled-background surfaces. It is NOT a video-overlay palette by default. Roman Navy `#0D1F3C` and Torch Amber `#C8821A` cannot serve as letter-fill for headlines sitting over warm-graded video footage; that's why the SC parent palette (Cream / Warm Charcoal / Burgundy) handles editorial overlays in Fair Case ad creative.

**Exception: The Anchor.** Pattern 6 in the SC Designed Overlay System (`../../02_Visual/Designed_Overlay_System.md §6 Pattern 6`) is the FIRST and ONLY video overlay that uses the Fair Case brand palette directly — because the Anchor IS the brand-identity layer of the spot. It earns its place by being persistent (full-spot duration) and brand-bearing (carries the torch logo in the overlay layer).

**Anchor palette use:**
- **Background:** Roman Navy `#0D1F3C` solid (over light footage: 88-92% opacity)
- **Top-edge rule:** 0.5pt Torch Amber `#C8821A`
- **Headline:** white `#FFFFFF` (Tiempos Headline Medium 56-72pt)
- **Secondary + Disclaimer:** Muted Navy Light `#A8B8CC` (Inter)
- **CTA prompt:** Torch Amber `#C8821A` arrow or pill button
- **Brand mark:** Fair Case torch (Roman Navy mark + Torch Amber flame, the one invariant)

**Multilingual readiness for Phase 2 Spanish:** the Anchor's Tiempos + Inter typography stack handles Spanish characters natively. Layout reserves +20-30% line-length budget so Spanish copy ("Lo atendemos en español" / "Consulta gratuita. 24/7.") doesn't break the headline wrap or push the secondary line into the disclaimer zone. If Spanish copy strains, increase Anchor height from 35% to 38% of frame.

**Editorial overlay rule unchanged:** all OTHER on-video overlays in Fair Case ad creative (Hook Card, Peak Card, Exhibit, Hero Number) continue to use the SC parent palette (Cream / Warm Charcoal / Burgundy). The Anchor and editorial overlays can coexist in the same spot — Anchor in the bottom 35-40%, editorial overlays in the top or middle of frame.

**UGC creative exception preserved:** UGC ad creative (Diana UGC variants, etc.) does NOT carry the Anchor and does NOT carry the Fair Case torch logo in the ad creative itself. CTA reads as text-only (Inter Bold + Torch Amber accent word). The torch logo appears post-click on the landing page. This rule, locked in `Agency_Creative_Review.md`, is not affected by the Anchor pattern.

---

*Brand System Brief — March 2026 (Anchor Extension added 2026-04-30). Governs homepage, social posts, and all brand materials outside the quiz form. Read alongside `FORM_DESIGN_BRIEF.md` for the complete Fair Case design system. Read alongside `../../02_Visual/Designed_Overlay_System.md` for video-overlay rules.*
