# Fair Case — Form Design Brief

**Authors:** Luke Wroblewski (UI/UX Conversion) + Chester Prides (Web Design)
**Date:** March 2026
**Status:** Specification document. These are decisions, not hypotheses — except where explicitly marked as "test this."
**Purpose:** Define the Fair Case quiz funnel to the level of specificity needed to build it. Every decision here is grounded in conversion research, not aesthetic preference.

---

## The One-Line Brief

The Fair Case quiz form is not a form. It is a service. The claimant uses it to find out what she has — before she commits to anything, before she talks to a lawyer, before she makes a decision. The form's job is to make that process feel easy, private, fast, and worth her time.

If she finishes and thinks "that was actually helpful" — the form worked.
If she drops off because something felt confusing, slow, or suspicious — the form failed.
Everything below is in service of the first outcome.

---

## The Strategic Reality (Luke)

The Fair Case funnel is:

```
Meta Ad (Style A / B / C)
    ↓
Landing page (getafaircase.com)
    ↓
Quiz / Form (6 questions)
    ↓
Loading / Calculation screen
    ↓
Contact capture (name, phone, email)
    ↓
TCPA consent + Confirmation
    ↓
Lead delivered to law firm
```

**What this means for design:**

- **75%+ of traffic is mobile.** Design for a phone held in one hand. Every decision is made at 375px wide first.
- **One-time encounter.** This person will not come back. She either completes the form or she doesn't. There is no "we'll get her next time."
- **High emotional stakes.** She's not buying a product. She's deciding whether to pursue a legal claim after an accident. She is stressed. She is skeptical. She is being cautious. The form must reduce cognitive load and emotional friction simultaneously.
- **The brand signal is functional, not decorative.** The Fair Case mark at the top of the form is not branding for awareness. It is a quality signal that tells her: this was built by someone who cared, which means it's probably not a scam. The form's design quality IS the trust signal.

---

## Section 1 — Flow and Structure

### The Six-Question Sequence

Fair Case qualifies MVA (motor vehicle accident) claimants across six questions. The sequence follows the commitment-building principle: easiest question first, highest-friction (contact info) last.

**The optimal order:**

| Screen | Question | Type | Why It's Here |
|---|---|---|---|
| 1 | "Were you in an accident?" | Yes / No (large buttons) | Easiest yes in the sequence. Establishes foot-in-the-door. Auto-advance on selection. |
| 2 | "What type of accident?" | Multiple choice (car / truck / motorcycle / rideshare / pedestrian) | Low friction. Large tap targets. No typing. Auto-advance. |
| 3 | "When did the accident happen?" | Date selector (approximate is fine — "In the last 30 days / 30–90 days / 3–12 months / Over a year ago") | Ranges, not exact date. Removes anxiety about remembering. Auto-advance. |
| 4 | "Were you injured?" | Yes / No + optional "Tell us briefly" text field if Yes | The first question with any text entry. Positioned after three taps — the user is invested. Optional text field reduces anxiety (they're not required to write an essay). |
| 5 | "Have you spoken with an insurance adjuster?" | Yes / No / Not yet | Intelligence question. Routes the lead quality signal. Auto-advance. |
| 6 | "Has an attorney contacted you about this accident?" | Yes / No | Disqualifier check. If Yes, conditional logic redirects (attorney is already involved — graceful exit). |

**→ Loading / Calculation Screen**

**→ Contact Capture**
- Full name
- Phone number
- Email address

**→ TCPA Consent + Submit**

**→ Confirmation Screen**

---

### One Question Per Screen — Non-Negotiable

Every question lives on its own screen. No exceptions. This is Luke's most evidence-backed principle for quiz funnels:

- **Feels faster** even though total questions are the same
- **Builds momentum** — each tap forward is a micro-commitment (Cialdini's commitment and consistency)
- **Enables drop-off analysis per question** — you can see exactly which question loses people, and fix it
- **Auto-advance on single-select** — when a claimant taps "Yes," the form advances immediately without needing a separate "Continue" button. This removes one tap from every question.

---

### The Loading / Calculation Screen

This screen is critical and non-obvious. It exists between the last qualification question and the contact capture step.

**What it does:** Creates a sunk cost + curiosity gap. The user has answered six questions. They've invested two minutes. The loading screen says: your answers are being analyzed. Something of value is being prepared for them. They want the payoff.

**What it shows:**
```
Reviewing your case details...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓  Accident type confirmed
✓  Eligibility window verified
    Calculating estimated case value...

[████████████░░░░░] 78%
```

**Duration:** 3–4 seconds of animated progress. Not instant. The artificial pause is the point.

**Copy on the lines:** Specific, not generic. "Eligibility window verified" is more credible than "Processing." Each line names something real about the qualification process.

**Design:** Dark background (deep warm charcoal from the brand palette) with warm amber progress bar and checkmarks. This is the one moment where the full brand palette is used — it creates a visual inflection point that signals "something is happening" before she enters the highest-friction section (contact info).

---

### The Contact Capture Screen

This is the highest-friction screen in the flow. She has been willing to tap through six questions. Now she is being asked for her name and phone number. This is where most drop-off occurs, and this is where the design must work hardest.

**The frame:** This is not "fill in your contact information." It is:

> **"Where should we send your free case review?"**
>
> A Fair Case specialist will call within 5 minutes during business hours.

**Fields:**
1. Full Name (top-aligned label, large field, autocomplete="name")
2. Phone Number (tel input, number pad keyboard, input mask: (___) ___-____, autocomplete="tel")
3. Email Address (email input, @ keyboard, autocomplete="email")

**Field order rationale:** Name first (lowest friction), phone second (higher friction — but by now they're invested), email third (expected, standard).

**Sticky CTA:** "Get My Free Case Review" fixed to the bottom of the screen. Full width. Warm amber fill, white text, high contrast.

**Trust signals at this screen only:** Not at the top. Not in the hero. Here:
- Lock icon + "Your information is private and secure"
- "No cost to you — ever. Attorneys work on contingency."
- "We'll call once to connect you with an attorney. No spam."

These three lines live immediately above the sticky CTA button. Positioned at the point of highest friction, not at the top where she'll ignore them.

---

### The Confirmation Screen

**Purpose:** Expectation setting. She submitted. What happens next?

```
You're all set, [First Name].

A specialist will call you within 5 minutes
during business hours to discuss your case.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What to expect:
• A brief 5-minute call
• No pressure, no obligation
• Free, confidential evaluation

[Fair Case mark]
```

**No links. No upsell. No email capture (already have it).** The confirmation screen is closure, not an opportunity.

---

## Section 2 — Typography

### The Two-Font System

Fair Case uses two typographic standards. They serve different contexts. They do not conflict.

**Font 1: Inter (Form and Funnel)**

Inter is the form font. This is not a creative decision — it is a conversion decision.

Why Inter:
- Designed specifically for screen legibility at small sizes
- 100% open source, zero licensing, zero load-time cost
- Excellent mobile rendering across all platforms and OS
- Used by Stripe, Linear, Vercel — the standard for high-trust digital products
- Humanist enough to carry warmth; clean enough for zero cognitive friction
- Zero associative baggage (unlike system fonts, which vary by platform)

**Font 2: Tiempos (Brand and Wordmark)**

Tiempos is the brand font. It appears in:
- The "Fair Case" wordmark in the combination mark
- Social post headlines
- Landing page hero headline
- Homepage headlines

Tiempos does NOT appear as body copy in the form, does NOT appear as question labels, does NOT appear on buttons. Its role in the form is the wordmark only.

**The principle:** The form reads in Inter. The brand speaks in Tiempos. The claimant may not consciously notice the distinction. She will notice that the form feels easy to read, and she will feel the quality signal from the wordmark. Both are true simultaneously.

---

### Form Typography Scale

All values are in pixels, desktop baseline. Mobile scales apply proportionally.

| Element | Font | Weight | Size | Line Height | Notes |
|---|---|---|---|---|---|
| Question text | Inter | Semibold (600) | 22–24px | 1.3 | The primary read. Large, confident, unambiguous. |
| Answer options (large button) | Inter | Medium (500) | 16–18px | 1.4 | Full-width tap targets. Not tiny radio buttons. |
| Field label | Inter | Medium (500) | 14px | 1.5 | Above the field. Clear, short. |
| Field input text | Inter | Regular (400) | 16px | — | 16px minimum prevents iOS auto-zoom on focus. |
| Helper / micro-copy | Inter | Regular (400) | 13px | 1.5 | Muted color (#6B7280 or equivalent). |
| CTA button | Inter | Semibold (600) | 16–18px | — | Action copy. Not sentence case — should feel like an instruction. |
| Progress step | Inter | Regular (400) | 12–13px | — | "Step 2 of 6" or progress bar percentage. |
| Trust micro-copy | Inter | Regular (400) | 12–13px | 1.5 | Muted, present but not competing. |
| Confirmation headline | Inter | Bold (700) | 24–28px | 1.2 | "You're all set" moment. |
| Wordmark ("Fair Case") | Tiempos | Medium | Logo-scale | — | Only instance of Tiempos in the form. |

**The 16px floor:** No text in the form goes below 16px for input fields. iOS Safari auto-zooms when focused input text is below 16px. This zoom behavior breaks the layout, disorients the user, and directly causes abandonment.

---

## Section 3 — Color in the Form

### The Background Hierarchy

The form is not amber. The brand is amber. This distinction matters.

**Form background:** `#FFFFFF` (pure white) as the default to test against.

Chester's view: Pure white is the highest-contrast, lowest-friction form background that exists. It produces the strongest legibility for every text color. It reads as clean, professional, and in the same visual register as every high-trust form on the internet (Typeform, Google Forms, Stripe checkout). The question is not "does white work" — it does. The question is whether a warm off-white outperforms it for Fair Case specifically.

**Test: White vs. Warm Cream**

| Variant | Background | Hypothesis |
|---|---|---|
| A (Control) | `#FFFFFF` pure white | Maximum legibility, familiar trust signal |
| B | `#FAFAF7` warm off-white | Subtle warmth, coherent with brand palette, may improve emotional register |

This is Test #1 in the testing hierarchy. Run it with at least 500 completions per variant before calling it.

---

### The Brand Color in the Form

The brand system is navy + amber. Their roles in the form are distinct:

- **Roman Navy (`#0D1F3C`):** The logo, the torch body, the wordmark. Authority and legibility on white.
- **Torch Amber (`#C8821A`):** The torch flame, the CTA button, the progress bar. Action and warmth.

**1. The Fair Case mark (logo area)**
The combination mark (torch symbol + "Fair Case" wordmark) at the top of the form. Roman Navy mark on white — this is the primary and only version for the form. The torch mark is two-color: Roman Navy body (`#0D1F3C`), Torch Amber flame (`#C8821A`). The wordmark ("Fair Case") is Roman Navy. Roman Navy on white passes WCAG AA at all logo sizes without question.

**2. The CTA button**
The primary "Continue," "Get My Free Case Review," and final submit button. Amber fill, white text. This is the single most important brand touch in the form — the moment the claimant takes action, she taps the fire. The visual association between "action" and "amber" is the identity in practice.

**Button spec:**
- Background: Torch Amber `#C8821A`
- Text: Roman Navy `#0D1F3C` (5.57:1 contrast ratio — passes WCAG AA; white text on this amber only achieves ~2.95:1 and fails)
- Weight: Semibold, Inter, 16–18px
- Border-radius: 8px (friendly, not sharp — not pill-shaped, not perfectly square)
- Height: 52px minimum (exceeds the 48px Material Design minimum; thumb-friendly)
- Full width on mobile

**Hover state (desktop):** Torch Amber dark `#A86A10`, Roman Navy text. No animation — instant state change.
**Pressed state:** 15% darker amber. Transform: scale(0.98).

**The visual logic:** The mark is Roman Navy background + Torch Amber torch. The button is Torch Amber background + Roman Navy text. The two brand colors swap roles between logo and CTA — the system mirrors itself.

**3. The progress bar fill and loading screen**
Progress bar: Torch Amber fill (`#C8821A`) on a light gray track (`#E5E7EB`).
Loading screen: The one moment where the full brand palette inverts — Roman Navy background (`#0D1F3C`), Torch Amber progress fill, white text.

---

### What the Form Does NOT Do

- No amber backgrounds on question screens (the amber CTA is the only amber element on a white form)
- No amber text on white (insufficient contrast for legibility at body text sizes)
- No amber borders or outlines on fields (selected field state uses a muted blue or dark charcoal outline — this is a universal UX convention and breaking it causes confusion)
- No heavy use of the torch mark within the form questions — one instance at the top, that's it

The brand color earns its visual impact by appearing rarely. One amber button on a white form is dramatic. Three amber elements on the same screen is noise.

---

### Field State Colors

| State | Border | Background | Text |
|---|---|---|---|
| Default | `#D1D5DB` (light gray) | `#FFFFFF` | `#111827` (near-black) |
| Focused | `#374151` (dark charcoal) | `#FFFFFF` | `#111827` |
| Valid (checkmark) | `#059669` (green) | `#FFFFFF` | `#111827` |
| Error | `#DC2626` (red) | `#FFF1F1` (very light red tint) | `#DC2626` for error message |

Field state colors are functional, not branded. The claimant's brain has been trained by decades of form UX that green = valid and red = error. Breaking that convention in service of brand color consistency is a conversion mistake.

---

## Section 4 — Trust Signals

### Where They Go (and Where They Don't)

The research is clear on trust signal placement: **trust signals placed at the point of friction are 3x more effective than trust signals placed at the top of the form.**

Putting "Your information is secure" in the hero — where the claimant hasn't committed to anything yet — produces almost no conversion lift. Putting it directly above the submit button — where she is deciding whether to hand over her phone number — produces significant lift.

**Trust signal placement map:**

| Moment | Trust Signal | Why Here |
|---|---|---|
| Top of form (logo area) | Fair Case mark — the quality signal | First impression. Legitimacy gate. |
| Above contact fields | Lock icon + "Your information is private and secure" | She's about to give her phone number. This is the anxiety moment. |
| Below phone number field | "We'll call once to connect you with a qualified attorney. No spam." | Addresses the #1 objection: "will I get bombarded with calls?" |
| Above CTA button | "No cost to you — ever. Attorneys work on contingency." | Addresses the #2 objection: "am I getting into something expensive?" |
| Confirmation screen | "What to expect" — the three-step explanation | Post-conversion expectation-setting. Reduces no-shows on the intake call. |

**What is NOT included:**
- SSL badges (Norton, McAfee) — add cognitive noise and often read as attempts to compensate for looking suspicious. The form's quality of execution is a stronger trust signal.
- Star ratings or review counts — not enough established reviews at launch to use this credibly. Add in Phase 2 when real review volume exists.
- Testimonials — they compete with the question for attention. Reserve for the landing page.

---

### TCPA Language

TCPA compliance language appears once, directly above the final submit button on the contact capture screen. It does not appear before that point.

**Placement:** Below the trust micro-copy, above the CTA.

**Format:** Small text, muted color, full sentence. Not a checkbox (checkboxes reduce conversion; the language of the button click constitutes consent when properly structured — verify with compliance).

**Copy direction (not final — legal review required):**
> "By clicking 'Get My Free Case Review,' you consent to be contacted by Fair Case and its attorney network via phone, text, and email regarding your case. Message and data rates may apply. See our Privacy Policy."

The TCPA language must be present and compliant. It should not be hidden (light gray on white at 9px is hiding it — that creates liability). It should be readable at 12–13px in a muted but legible color (`#6B7280`).

---

## Section 5 — The Logo at the Top of the Form

### What It Is

The Fair Case combination mark (torch symbol + "Fair Case" wordmark) appears centered or left-aligned at the top of every screen in the quiz. It is:

- A quality signal ("someone built this")
- A brand recall anchor ("this is Fair Case")
- NOT a primary navigation element

### Specs

**Alignment:** Center-aligned on mobile. This is the standard for quiz/form flows — centered logos signal "this is a focused experience," left-aligned signals "this is a site with navigation." Since there is no navigation, center alignment is appropriate.

**Size:** Small enough to not compete with the question, large enough to be clearly legible. Target: 120–140px wide for the combination lockup on mobile. The torch symbol alone: 28–32px height.

**Color:** Navy (`#0D1F3C`) mark on white. This is the only version for form contexts — amber on white does not hold contrast at small logo sizes. The torch mark is two-color: navy body, amber flame (`#C8821A`). Massimo confirms the flame rendering at logo scale in Session 2.

**Linking behavior:** The logo links to `getafaircase.com` (the homepage), but **opens in a new tab.** This is the standard for funnel-top logos — the claimant can navigate away if she chooses, but the form tab remains open. She doesn't lose her progress.

**Chester's note:** No hover animation on the logo in the form. Hover states on logos signal "this is a navigation element — you can go somewhere." In a quiz context, that signal is friction. Static mark only.

---

## Section 6 — Testing Hierarchy

### What to Test in What Order

Luke's ICE framework applied to Fair Case's specific hypotheses. Start at the top. Do not jump to lower-priority tests before upper ones are resolved.

| Priority | Test | Impact | Confidence | Ease | ICE Score | Hypothesis |
|---|---|---|---|---|---|---|
| 1 | Form background: Pure white vs. warm cream | High | Medium | High | 8.0 | Warm cream produces warmer emotional register without sacrificing legibility |
| 2 | CTA button copy: "Continue" vs. action-specific ("See If I Qualify") | High | High | High | 9.0 | Specific action copy outperforms generic "Continue" at each step |
| 3 | CTA button color: Warm amber vs. high-contrast dark charcoal | High | Medium | High | 8.0 | Warm amber (brand color) converts as well as or better than conventional dark button |
| 4 | Progress indicator: Step counter ("Step 2 of 6") vs. progress bar | Medium | Medium | High | 7.0 | Progress bar produces stronger goal-gradient effect than step numbers |
| 5 | Phone field micro-copy: None vs. "We'll call once about your case" | High | High | High | 9.0 | Trust micro-copy at the phone field reduces drop-off at highest-friction step |
| 6 | Loading screen: 3-second animation vs. instant advance | Medium | Medium | Medium | 6.7 | Artificial pause increases contact capture completion via sunk cost |
| 7 | Question 1 format: Large yes/no buttons vs. standard radio | Medium | High | High | 8.3 | Large tap-target format increases completion of step 1 vs. small radio inputs |
| 8 | Contact field order: Name/Phone/Email vs. Phone/Name/Email | Medium | Low | High | 6.0 | Name first reduces anxiety; phone first builds commitment on highest-friction field |

**Statistical threshold:** 95% confidence. Minimum 200 completions per variant before calling. Account for day-of-week variation by running each test for at least 10 days.

**What not to test at launch:** Logo color (too few data points), font choice (too high cost to implement multiple variants), TCPA language (compliance, not conversion).

---

## Section 7 — Platform Recommendation

### Chester's Call

**Build on a custom lightweight quiz platform or purpose-built code — not Webflow or Typeform out of the box.**

Here's why:

**Why not Webflow:**
Webflow's form handling is built for static forms, not multi-step quiz funnels. Conditional logic requires custom code or third-party embed. The quiz sequence Fair Case needs — auto-advance on selection, loading animation, conditional question routing — requires JavaScript that fights Webflow's native form architecture. The build complexity is high and the maintenance cost is higher.

**Why not Typeform:**
Typeform produces excellent quiz experiences and is close to the Fair Case format. The problem: brand control is limited. The Fair Case mark at the top, the custom color on the CTA button, the specific loading screen, the TrustedForm and Jornaya TCPA compliance integrations — all of these require workarounds or are unavailable in Typeform's standard plans. TCPA compliance at the standard required for legal lead gen specifically requires full control over the consent language and its placement.

**Recommended path: Custom-coded quiz on a lightweight stack**

Specifically: Next.js (React) deployed on Vercel, with:
- Custom quiz state management (simple — six steps, conditional logic on Q6)
- TrustedForm certificate generation (they provide a JavaScript snippet — requires full code control)
- Jornaya LeadiD integration (same — requires custom placement)
- Full CSS control for Fair Case brand tokens (color, typography, spacing)
- A/B testing via a lightweight library (Optimizely, or split.io for the testing hierarchy above)
- Analytics: Segment or direct GA4 integration with step-level event tracking

**Build timeline estimate:** 2–3 weeks for a senior developer to build the core quiz and contact capture. Add 1 week for TrustedForm/Jornaya integration. Add 1 week for QA and device testing.

**Alternative if timeline is compressed:** Use a purpose-built legal lead gen quiz platform (Instapages or a similar conversion-focused builder with TCPA compliance built in) as the interim solution, with the custom build following once the team has conversion data to build against.

---

## Section 8 — The Full Spec at a Glance

### Form Shell

| Element | Spec |
|---|---|
| Background | `#FFFFFF` (test vs. `#FAFAF7` warm cream) |
| Max width (desktop) | 480px centered — form feels intimate on desktop |
| Padding (mobile) | 24px horizontal, 16px vertical |
| Logo area height | 56–64px (center-aligned mark + wordmark) |
| Progress indicator | Thin bar below logo area (4px height, amber fill, gray track) |

### Typography

| Element | Font | Weight | Size |
|---|---|---|---|
| Question | Inter | 600 | 22–24px |
| Answer button text | Inter | 500 | 16–18px |
| Field label | Inter | 500 | 14px |
| Field input | Inter | 400 | 16px (floor) |
| Helper text | Inter | 400 | 13px |
| CTA button | Inter | 600 | 16–18px |
| Trust micro-copy | Inter | 400 | 12–13px |
| Wordmark | Tiempos | Medium | Logo scale |

### Color Tokens

| Token | Value | Use |
|---|---|---|
| `--color-roman-navy` | `#0D1F3C` | Logo mark, wordmark, torch body, loading screen background |
| `--color-torch-amber` | `#C8821A` | CTA button fill, progress bar fill, torch flame element |
| `--color-torch-amber-dark` | `#A86A10` | CTA button hover state |
| `--color-bg` | `#FFFFFF` | Form background (A) |
| `--color-bg-warm` | `#FAFAF7` | Form background (B — test) |
| `--color-text-primary` | `#111827` | Question text, field input |
| `--color-text-secondary` | `#6B7280` | Helper text, trust micro-copy |
| `--color-field-border` | `#D1D5DB` | Default field border |
| `--color-field-focus` | `#374151` | Focused field border |
| `--color-valid` | `#059669` | Valid field indicator |
| `--color-error` | `#DC2626` | Error state |

### Interactive States

| State | Treatment |
|---|---|
| Answer button (default) | White fill, `#D1D5DB` border, `#111827` text |
| Answer button (hover) | `#F9FAFB` fill (very light gray) |
| Answer button (selected) | `--color-roman-navy` fill, white text, no border |
| CTA button (default) | `--color-torch-amber` fill (`#C8821A`), `--color-roman-navy` text (`#0D1F3C`) |
| CTA button (hover) | `--color-torch-amber-dark` fill (`#A86A10`), `--color-roman-navy` text |
| CTA button (pressed) | 15% darker + scale(0.98) |
| Field (focus) | `--color-field-focus` border, no fill change |
| Field (valid) | `--color-valid` right-edge icon (checkmark) |
| Field (error) | `--color-error` border + error message below |

---

## Reference Documents

| Document | Location |
|---|---|
| Brand Identity Session Record + Brief | `04_Visual_Identity_Brief/BRAND_IDENTITY_SESSION_RECORD.md` |
| Visual Identity Session Brief | `04_Visual_Identity_Brief/VISUAL_IDENTITY_SESSION_BRIEF.md` |
| B2C Creative Production Brief (ad styles) | `04_Visual_Identity_Brief/B2C_CREATIVE_PRODUCTION_BRIEF.md` |
| B2C Strategy Overview | `01_B2C_Strategy/B2C_STRATEGY_OVERVIEW.md` |
| Consumer Personas (Maria Rodriguez) | `01_B2C_Strategy/CONSUMER_PERSONAS.md` |
| Disclosure Requirements (TCPA compliance) | `02_Social/DISCLOSURE_REQUIREMENTS.md` |

---

*Form Design Brief — March 2026. Luke Wroblewski (conversion) + Chester Prides (web design). This document governs the quiz funnel build. The brand identity session record governs the mark, color, and type system that this brief applies within conversion constraints.*
