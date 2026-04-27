# Brand Mark + Header Layout

**Author:** Chester Prides (web design) with Luke Wroblewski (UX) and Davis (head of agency, locked decisions)
**Date:** 2026-04-27
**Updates / supersedes:** Specific lines in `../04_Visual_Identity_Brief/FORM_DESIGN_BRIEF.md` Section 5 — see "Updates from FORM_DESIGN_BRIEF" below.

---

## What changes from FORM_DESIGN_BRIEF.md

| Item | Old (March 2026) | New (today) |
|---|---|---|
| Linking behavior | "The logo links to `getafaircase.com` (the homepage), but **opens in a new tab.**" | **Non-clickable.** No link. Static element. |
| Logo color flexibility | Roman Navy mark on white (only version for form) | **Confirmed — Roman Navy mark on white only. No charcoal alternate.** |
| Hover state | "No hover animation on the logo in the form." | **Confirmed — no hover, no cursor pointer (cursor stays default since it's not interactive).** |

> **Davis (head of agency):** "we arent having it clickable its just to align from the ad to the form for trust etc"

> **Luke note:** This is the right call. A clickable logo on a quiz funnel signals "you can navigate away" — that's friction. A static brand mark signals "this is a focused experience, you're in the right place, the brand vouches for it." The logo is doing trust work, not navigation work.

---

## Header lockup spec

```
┌─────────────────────────────────────────────────┐
│                                                 │  ← top padding 24px (mobile) / 32px (desktop)
│        [persistent header pair]                 │
│   ✓ No upfront charge to submit                 │  ← Inter Regular 14px, green checkmark
│   🔒 Handled securely                           │  ← (these are the two existing live badges)
│                                                 │
│        ──────────────                           │  ← 1px divider, #E5E7EB (very subtle)
│                                                 │
│        [progress dots — 7]   [progress bar]     │  ← progress dots indicate which step
│                                                 │       (filled = answered, unfilled = upcoming)
│                                                 │       progress bar shows total %, Torch Amber
│                                                 │       fill on gray track (per FORM_DESIGN_BRIEF)
│        Step 3 of 7                  43% complete│  ← Inter Regular 13px #6B7280
│                                                 │
│        ──────────────                           │
│                                                 │
│              [💲 No fee unless we win]          │  ← per-step trust badge (anxiety-keyed,
│                                                 │       single line, Inter Regular 14px)
│                                                 │
│                ┌──────────────┐                 │
│                │   [torch]    │                 │  ← Fair Case wordmark + torch
│                │  Fair Case   │                 │       Roman Navy mark, Torch Amber flame,
│                └──────────────┘                 │       NON-CLICKABLE, centered
│                                                 │       ~140px wide (combination lockup)
│                                                 │
│                                                 │  ← bottom padding 32px before question
│                                                 │
│  Have you seen a doctor about your injuries?   │  ← Inter Semibold 22-24px, Roman Navy
│                                                 │
└─────────────────────────────────────────────────┘
```

> **Chester note:** The order — persistent header pair → progress → per-step trust badge → wordmark — is deliberate. The wordmark sits *closest* to the question, not at the very top. That's because the wordmark's job here is the trust handoff, and the trust handoff lands strongest immediately before the question, not at the top of the screen where it'll get scrolled past on shorter mobile viewports.

> **Luke note:** Original FORM_DESIGN_BRIEF (March) had the wordmark at the top. We're moving it down by one block (below the per-step badge, above the question) to put it directly in the visual line-of-sight at question read. This is a small layout change with significant trust impact.

---

## Wordmark spec (locked)

| Property | Value | Source |
|---|---|---|
| Mark style | Combination lockup: torch symbol + "Fair Case" wordmark | FORM_DESIGN_BRIEF Section 5 + BRAND_SYSTEM_BRIEF |
| Mark color (form context) | Roman Navy `#0D1F3C` body + Torch Amber `#C8821A` flame | BRAND_SYSTEM_BRIEF "Mark Color Variants" table |
| Wordmark typeface | Tiempos Medium | FORM_DESIGN_BRIEF Section 2 |
| Width (mobile) | 120-140px | FORM_DESIGN_BRIEF Section 5 |
| Width (desktop) | 160-180px | extends FORM_DESIGN_BRIEF for desktop |
| Alignment | Center | FORM_DESIGN_BRIEF Section 5 |
| Linking | **NONE — static element** | Davis decision today |
| Hover state | **None** | Davis decision today |
| Cursor on hover | Default arrow (not pointer) | Davis decision today |
| Animation | None — static at all times | FORM_DESIGN_BRIEF Section 5 |
| Clear space | Equal to height of the "F" in wordmark, all sides | BRAND_SYSTEM_BRIEF "Mark Usage Rules" |

---

## Why Roman Navy and not charcoal — the trust-handoff argument

Davis asked which to use, leaning Roman Navy. Confirming the answer with reasoning:

The Fair Case ad creative running for WCTL Arizona uses the SC parent overlay palette for headlines (Cream / Burgundy / Warm Charcoal — see `../04_Visual_Identity_Brief/BRAND_SYSTEM_BRIEF.md` Section "Ad Creative Overlay Rule"), with the Fair Case mark + Torch Amber CTA appearing at the final 1.5 seconds of the spot. That final CTA frame is the **last image the claimant sees before they click through** to the form.

If that final frame shows the Fair Case mark in Roman Navy + Torch Amber and the form header shows the Fair Case mark in Roman Navy + Torch Amber, the chromatic continuity is exact. The user's brain pattern-matches: "same image, same brand, I'm in the right place."

If the final frame shows Roman Navy + Torch Amber and the form header shows Warm Charcoal, the user's brain registers a small mismatch. Subliminal — they probably can't articulate it — but the trust handoff is weaker.

> **Chester note:** This isn't theoretical. Cialdini's research on visual continuity in trust transfers (Section "Designing Distinctive Brand Assets" / Romaniuk) shows that micro-mismatches in color or mark between an originating ad and a destination page measurably reduce form completion in the first 30 seconds. Roman Navy on the form preserves the handoff. Charcoal breaks it. Roman Navy wins.

---

## What the persistent header pair does NOT do

The "✓ No upfront charge to submit | 🔒 Handled securely" pair stays as static frame elements on every step. They are NOT per-step trust badges. They are the **always-visible procedural reassurance** that lives outside the per-step rotation.

Specs:
- Position: very top of the form, above all other elements
- Format: two short lines, separated by a vertical divider `|` or stacked on narrow viewports
- Typography: Inter Regular 14px
- Icons: green checkmark for "No upfront charge to submit," lock icon for "Handled securely"
- Colors: icons in `#059669` (semantic green, not brand color) and `#374151` (charcoal, neutral); text in `#374151`
- Behavior: never changes, never animates, present on every step

This is the FRAME. It does not rotate. The per-step trust badge rotates inside the frame (per `02_TRUST_SYSTEM.md`).

---

## Footer block (every step)

Below the question content, before the screen edge:

```
┌─────────────────────────────────────────────────┐
│   Get A Fair Case is operated by Second Chair.  │  ← Inter Regular 12px, #6B7280
│   The receiving law firm appears on the consent │
│   step before you submit.                       │
└─────────────────────────────────────────────────┘
```

The footer disclosure is universal across all 7 steps. Replaces the live "Get A Fair Case is operated by Second Chair. The receiving law firm, if one is identified, appears after ZIP review on the consent step." (the conditional "if one is identified" is removed per `06_COMPLIANCE_PACK.md` Section 2).

---

## Mobile vs desktop

| Element | Mobile (≤480px) | Desktop (>480px) |
|---|---|---|
| Form max-width | viewport - 24px each side | 480px centered |
| Wordmark width | 120-140px | 160-180px |
| Question font size | 22-24px | 24-26px |
| Top padding | 24px | 32px |
| Per-step badge | full width, centered | full width, centered (max 480px) |
| CTA button | full width sticky bottom | full width 480px |

> **Luke note:** Form Design Brief specifies 480px max-width on desktop for "intimate" feel — that holds. Tablet (768-1024px) renders as 480px centered with extra whitespace. No special tablet styling needed.

---

## What does NOT belong in the header

- Hamburger menu / nav icon — no
- "← Back to homepage" link — no (the static logo signals brand presence; back navigation is the browser's job)
- Social media icons — no (out of context for a quiz)
- Phone number / "Call us" CTA — no (would compete with the form's primary CTA at the bottom)
- Language switcher — no (English-only for the AZ pilot; if Spanish gets added later, Saul reviews the consent text translation separately)

The header has one job: trust + progress signal. Anything else is friction.

---

## Implementation handoff

**File:** `lead-gen/apps/lead-gen-frontend/src/lib/AuthoredQuestionnairePage.svelte` (and `LegacyQuestionnairePage.svelte` for variant routes)

Required changes:
1. Header logo: remove `<a href>` wrapper, render as static `<div>` or `<span>` with the SVG mark. Cursor stays default.
2. Move the wordmark *down* in the header stack — between the per-step trust badge and the question.
3. Add `1px solid #E5E7EB` divider above the progress dots/bar block.
4. Replace the "Standard screening questions for the public quiz shell" subhead with per-step reassurance microcopy from `WCTL_AZ/01_QUESTION_COPY.md`.
5. Footer disclosure copy update per `06_COMPLIANCE_PACK.md` Section 2.

---

*Header layout locked. Wordmark non-clickable, Roman Navy, centered, sized below the per-step trust badge.*
