# Fair Case — Website Architecture Blueprint
## `WEBSITE_ARCHITECTURE.md`

> **Document Purpose:** Section-by-section blueprint for the Fair Case one-pager website. Covers strategic purpose, copy direction, placeholder headlines, design notes, content status, and phase transitions for each section. Use this to brief design, copywriting, and build.
>
> **Traffic Context:** Primary entry is Instagram link-in-bio → website. The visitor has seen 1–3 Fair Case posts. She is on mobile. She is doing a credibility audit — deciding whether Fair Case is legitimate before she takes any action. The page carries the full trust-building burden. It will not be shared between colleagues the way the Second Chair site is; it will be seen once, evaluated in under sixty seconds, and either acted on or abandoned.
>
> **Primary Goal (Phase 1):** Educate, build trust, capture email notification interest. No law firm partner exists yet, so no lead intake form. Educational content IS the product. The page earns trust by giving useful information without asking for anything except an optional email.
>
> **Primary Goal (Phase 2):** Convert to quiz/lead capture when law firm partners are signed. The quiz replaces the email notification form in Section 7. The hero CTA becomes active. The noindex meta tag is removed.
>
> **Tone Principle:** Honest, plain-spoken, empowering. Not lawyerly, not corporate, not fear-based. The claimant is addressed as an intelligent adult making a real decision. Every sentence passes the test: would a reasonable person find this manipulative after reading it?
>
> **Last Updated:** March 2026 — Post-Roundtable, Phase 1 Build

---

## ROUNDTABLE RECORD

*The page structure, persuasion architecture, and content sequencing below emerged from a multi-session expert roundtable. Participants: Julian Cole (brand strategy / 4Cs), Jon Steel (account planning / consumer truth), Luke Wroblewski (UX / mobile-first / conversion), Ed McCabe (copy), Massimo Vignelli (visual system), Richard Shotton (behavioral science / persuasion architecture), Adam Ferrier (behavioral economics / motivation).*

**Core roundtable decisions:**

- The page must deliver genuine value without lead capture. Phase 1 constraint is not a limitation — it is a brand asset. Giving information without asking for anything is the most powerful trust signal available.
- Educational content IS the product in Phase 1. The page earns the right to ask for an email (and, eventually, a case intake) by providing specific, useful information first.
- The email notification form (Phase 1) operates under CAN-SPAM, not TCPA. It is legally clean and does not require a named law firm. It is a marketing list, not a legal intake.
- The $33,700 gap stat is the single most powerful anchor on the page. It makes the invisible visible — the claimant is inside a system built against her, and that one number is the specific fact that makes her see it. It goes in the first content section after the hero, as early as possible.
- The three behavioral barriers (minimization instinct, optimism bias about insurers, present bias) must each be addressed in dedicated content. They are the reason people who have viable cases never act on them.
- Persona recognition cards create the "that's exactly my situation" moment that closes the credibility audit. They do not describe demographics — they describe behavioral situations.
- Design mirrors the Second Chair website structure (nav, sections, buttons, footer treatment) adapted to Fair Case palette. Shared parent brand signal; distinct consumer-facing voice.
- Mobile-first is non-negotiable. 75%+ of Instagram traffic arrives on a phone held in one hand. Every layout decision starts at 375px.
- The Torch Amber restraint rule (from Massimo's locked brief) applies to the one-pager: one amber element per section maximum. Amber draws the eye to deliberate, specific elements. Multiple amber elements in a section is noise.

---

## THE LEGAL CONSTRAINT THAT SHAPES EVERYTHING

### Phase 1 / Phase 2 Split

This is not a content decision — it is a compliance reality that determines the page's architecture.

**The TCPA requirement:** The Telephone Consumer Protection Act requires that any lead intake form capturing a phone number for attorney contact purposes must name the specific law firm that will contact the claimant. The required disclosure language is:

> *"By submitting this form, I provide my express written consent to receive calls and/or text messages from [SPECIFIC NAMED FIRM] at the phone number provided..."*

The bracketed firm name must be a real, contracted law firm — not "a participating firm," not "our legal partners," not a placeholder. If no firm exists, that disclosure is a false statement. Submitting a lead form under that condition creates TCPA liability with no defensible consent record.

**Therefore: No lead capture form in Phase 1.**

The quiz funnel — Fair Case's core product — requires a named law firm partner before it can legally operate. Until that partner is contracted, no quiz, no intake form, no phone number field.

**What IS allowed in Phase 1:** A standard email notification list operating under CAN-SPAM. "Get notified when Fair Case launches in your area" — email address and state, nothing else, no phone number, no TCPA consent required. This is standard marketing list behavior and is legally clean without a law firm partner.

**Phase 2 adds:** The full quiz intake (six questions), TCPA consent with the specific firm name, TrustedForm certificate capture, Jornaya LeadiD, and the lead routing pipeline to the contracted firm.

**The Phase 2 trigger:** A signed law firm partner agreement. Nothing else gates Phase 2. When the first partner is contracted, the site transitions: hero CTA activates, Section 7 swaps the email form for the quiz CTA, and the `<meta name="robots" content="noindex, nofollow">` tag is removed.

---

## DESIGN SYSTEM — SECOND CHAIR → FAIR CASE MAPPING

The Fair Case website shares a structural vocabulary with the Second Chair website. Same grid logic, same sticky nav behavior, same dark/light section alternation, same glassmorphism card treatment. The palette and typographic register differ.

| Element | Second Chair | Fair Case |
|---------|-------------|-----------|
| Dark background | Oxblood `#490A0A` | Roman Navy `#0D1F3C` |
| Accent color | Gold `#FFDD72` | Torch Amber `#C8821A` |
| Light background | Cream `#EDE1D4` | White `#FFFFFF` |
| Text on dark | `#FFF7F0` | `#FFFFFF` |
| Body text on light | Charcoal `#1C1917` | Body Gray `#374151` |
| Muted text on dark | `rgba(255,247,240,0.65)` | Muted Navy `#A8B8CC` |
| Display headline | TiemposHeadline (italic) | TiemposHeadline (upright) |
| UI / functional font | Sohne | Inter |
| Body font | ACaslon / TiemposText | Inter |
| Section dividers on light | `rgba(73,10,10,0.15)` | `rgba(13,31,60,0.12)` |
| Section dividers on dark | `rgba(255,221,114,0.22)` | `rgba(200,130,26,0.22)` |
| CTA button | Gold fill, dark text | Amber fill `#C8821A`, Navy text `#0D1F3C` |
| Hover state | Gold dark variant | Amber Dark `#A86A10` |

**The typographic register difference is intentional.** Second Chair uses TiemposHeadline italic because it speaks to attorneys with B2B editorial authority. Fair Case uses TiemposHeadline upright because it speaks directly to the claimant — plain-spoken, not editorial. Same typeface, different register. The upright weight reads as more direct and trustworthy to a consumer audience under stress.

**The warm/cool shift is intentional.** Oxblood reads as prestige and craft — right for a boutique creative firm. Roman Navy reads as authority and trustworthiness — right for a service that helps people navigate legal and financial decisions. The palette change was a deliberate brand positioning decision, not a cosmetic one.

---

## HOMEPAGE — FULL SECTION MAP

**URL:** `getafaircase.com` (one-pager, no sub-pages in Phase 1)
**Design framework:** Roman Navy full-bleed for hero, persona cards, and footer. White for all content sections. Amber accent one element per section. Grid overlay on hero and dark sections.
**Section alternation:** Dark → Light → Dark → Light → Dark → Light → Dark — strict alternation mirrors SC rhythm, prevents the all-navy fatigue Massimo flagged.

---

### SECTION 1 — NAV

**Strategic purpose:** Lightweight, credentialed, persistent. Does not distract from the hero. Carries the "Learn More" link as a scroll anchor so the visitor can navigate immediately without reaching the bottom.

**Color context:** Roman Navy `#0D1F3C`. Sticky, always dark regardless of what section is below.

**Layout:** 84px height. Amber rule (`rgba(200, 130, 26, 0.48)`) top and bottom border. Container: amber rule left and right vertical rails. Logo left with amber border-right divider. CTA right with amber border-left divider. Mobile: hamburger at ≤768px.

**Copy direction:**
- Nav CTA Phase 1: "Learn More" — text link, scrolls to Section 3 (The Gap).
- Nav CTA Phase 2: "Get a Fair Case" — amber button with double-border glassmorphism treatment, links to quiz.

**Design notes:** Mirrors SC nav exactly — same 84px height, same border treatment, same logo-left/CTA-right structure. The amber rule border system (top, bottom, left rail, right rail on container) is the shared structural vocabulary.

**Amber element:** The amber rule borders count as the section's amber. CTA button fill in Phase 2.

**Content status:** Implemented in `final-website/`.

---

### SECTION 2 — HERO

**Strategic purpose:** Three jobs simultaneously. (1) State the brand's core position in one headline that stops the person scrolling Instagram. (2) Signal this is legitimate — free, no upfront cost, worth sixty seconds. (3) Orient someone who knows nothing about Fair Case so they understand what they're looking at and what to do next.

**Color context:** Roman Navy `#0D1F3C`, full-bleed. White headline. Muted Navy `#A8B8CC` for sub-line. Amber arrow accent on pill. Subtle grid overlay.

**Layout:** Centered column, max-width 720px. Vertical stack: pill → H1 → sub-line → scroll indicator. Grid overlay background (SVG, navy-tinted).

**Copy direction:**
- Pill badge: "Free · No upfront cost →" — locked.
- H1: "Your rights. / Your case. / Your call." — locked. Three parallel possessives. "Your call" carries triple meaning: your decision, your phone call, your right to act.
- Sub-line: "You deserve to know what your case is worth." — locked. The brand promise from the brief, verbatim.
- Phase 1 CTA: Scroll-down chevron pointing to The Gap section. Subtle, animated.
- Phase 2 CTA: Amber double-border button "Get a Fair Case" → quiz.

**Amber element:** The arrow on the pill badge. One amber element.

**Content status:** Implemented in `final-website/`.

---

### SECTION 3 — THE GAP

**Strategic purpose:** Make the invisible visible. The claimant is inside a system built by the insurance company, running in the insurance company's favor — and most of the time she has no idea. The $33,700 gap is the specific, sourced fact that makes her see it. Not anger, not fear — recognition.

**Color context:** White `#FFFFFF`. Light section, first after hero.

**Layout:** Centered, max-width 680px. Large dollar figure in headline. Supporting copy below. Disclaimer below that.

**Copy direction:**

*Headline (Tiempos Medium, Roman Navy, large):*
> "The settlement gap is $33,700."
> *"$33,700" in Torch Amber `#C8821A`.*

*Supporting copy (Inter Regular, Body Gray):*
> "Accident victims who consulted an attorney before accepting a settlement averaged $47,300. Those who didn't averaged $13,600. Same injuries. Same accidents."
> "68% of accident victims accept the first offer without consulting an attorney. 91% later found their compensation was insufficient."

*Required disclaimer (Inter Regular, Form Gray `#6B7280`, small):*
> "Past results do not guarantee future outcomes. Figures based on California settlement data research."

**Jon Steel note:** This is the section that makes the invisible visible. The $33,700 gap is the one specific fact that makes her see the system. The copy must state it plainly — no emotional amplification, no exclamation marks. The fact is the argument.

**Amber element:** "$33,700" in Torch Amber within the headline. Nothing else amber in this section.

**Phase 1 vs Phase 2:** No change. Fully operational on day one.

**Content status:** Statistics sourced in `CONSUMER_PERSONAS.md`. Implemented in `final-website/`.

---

### SECTION 4 — WHAT YOU SHOULD KNOW

**Strategic purpose:** Address the three behavioral barriers directly — in the language of information, not persuasion. Each column handles one barrier. The insurance company gave her their frame on day one. This section gives her a competing frame, built from specific true facts.

**Color context:** Roman Navy `#0D1F3C`, full-bleed dark. Grid overlay.

**Layout:** Three-column grid (mirrors SC Moat section). Equal-width columns. Thin amber vertical dividers between columns (`rgba(200, 130, 26, 0.20)`). On mobile: vertical stack, dividers become horizontal rules.

**Copy direction — Column 1: THE SYSTEM**
- *Label:* "The System" — Inter, uppercase, muted amber
- *Headline:* "The adjuster's job is not to help you."
- *Body:* The insurance company employs the adjuster. Their job is to settle for as little as possible. They call within hours because the sooner they call, the less informed you are. This isn't vilification — it's how the system works.

**Copy direction — Column 2: THE COST**
- *Label:* "The Cost"
- *Headline:* "It costs nothing to find out what you have."
- *Body:* Personal injury attorneys work on contingency. No upfront cost. No fee unless the case settles or wins. The consultation itself is free. Most people don't know this.

**Copy direction — Column 3: THE DEADLINE**
- *Label:* "The Deadline"
- *Headline:* "Time limits are real. Know yours."
- *Body:* Every state has a statute of limitations — a deadline after which your case is permanently closed. In Colorado, it's three years. In other states, it may be less.

**Richard Shotton note:** These three columns map precisely to the three behavioral barriers. Column 1 breaks optimism bias about insurers. Column 2 breaks the minimization instinct — reframing from "suing" to "finding out." Column 3 breaks present bias with real deadlines. The register is information, not persuasion.

**Amber element:** Column labels in muted amber. Vertical dividers in amber rgba.

**Phase 1 vs Phase 2:** Column 3 can add a dynamic state-specific SOL figure in Phase 2 when geo-targeting is active.

**Content status:** Implemented in `final-website/`.

---

### SECTION 5 — HOW IT WORKS

**Strategic purpose:** Remove the fear of the unknown. The claimant's biggest barrier after "I don't want to sue" is "I don't know what will happen." Each step is anchored with a time cost — time, not money, is the real barrier on mobile.

**Color context:** White `#FFFFFF`. Light section.

**Layout:** Three numbered steps in horizontal row on desktop, vertical stack on mobile. Vertical rule dividers between steps. Section heading above.

**Copy direction:**
- *Section heading:* "How it works." — Tiempos Medium, Roman Navy
- *Step 01:* "Take a free quiz." — 60 seconds, no commitment, no personal info to start.
- *Step 02:* "Speak with an attorney." — Free, confidential, no obligation. Contingency.
- *Step 03:* "Know what you have." — Clear answer before you decide anything. One call. Ten minutes.

**Luke Wroblewski note:** Time anchors ("sixty seconds," "ten minutes") are conversion mechanics, not copy flourishes. An overwhelmed person will not decline a sixty-second quiz. She will decline an undefined process.

**Amber element:** Step numbers "01," "02," "03" in Torch Amber.

**Phase 1 vs Phase 2:** Phase 2 adds amber CTA button after Step 3: "Get a Fair Case" → quiz.

**Content status:** Implemented in `final-website/`.

---

### SECTION 6 — FOR PEOPLE LIKE YOU

**Strategic purpose:** Create the "that's exactly my situation" recognition moment. The claimant needs to see herself before she acts. Not a demographic segment — a behavioral situation she has actually been in.

**Color context:** Roman Navy `#0D1F3C`, full-bleed dark. Grid overlay.

**Layout:** Four persona-recognition cards in 2×2 grid on desktop, stacked on mobile. Glassmorphism panels: `border: 1px solid rgba(200,130,26,0.20)`, `background: rgba(255,255,255,0.03)`, `backdrop-filter: blur(2px)`. Section label above.

**Copy direction:**
- *Section label:* "Situations We See" — Inter, uppercase, muted amber
- *Card 1:* "The call from the adjuster." — Rear-ended, adjuster was friendly, before responding — hear what the case is worth.
- *Card 2:* "The bills that keep arriving." — Months later, bills arriving, offer didn't cover them. Most people believe it's too late. In most cases, it isn't.
- *Card 3:* "The rideshare accident." — Passenger, didn't cause anything. Options that haven't been explained.
- *Card 4:* "It's been a while." — Months ago, window may seem closed. In many states, it hasn't.

Third-person framing throughout (avoids Meta "you" + condition ban).

**Adam Ferrier note:** Recognition over persuasion. The claimant doesn't need to be convinced she has a problem. She needs to see that someone understands her specific situation. "That's exactly what happened to me" is the trust outcome.

**Amber element:** Card border in amber rgba. Section label in muted amber.

**Phase 1 vs Phase 2:** No change.

**Content status:** Persona situations sourced in `CONSUMER_PERSONAS.md`. Implemented in `final-website/`.

---

### SECTION 7 — NOTIFICATION / CTA

**Strategic purpose:** The ask. Phase 1: email notification — minimum viable ask, one field. Phase 2: quiz entry point with full TCPA consent architecture.

**Color context:** White `#FFFFFF`. Light section.

**Layout:** Centered, max-width 600px. Headline above, form below, disclosure below form.

**PHASE 1 — Email Notification Form**

*Headline:* "We're expanding. Be the first to know." — Tiempos Medium, Roman Navy
*Body:* "Fair Case is launching in select markets. Enter your email to be notified when we're available in your area."
*Form:* Email (required) + State dropdown (optional) + Submit button
*Submit label:* "Notify Me"
*Disclosure:* "We'll email you once when Fair Case is available in your area. No spam. Unsubscribe anytime."
*Backend:* Formspree (free tier) or similar

**Ed McCabe note:** The Phase 1 headline must not promise connection with an attorney. "We're expanding" is accurate and creates anticipation without misleading. The form asks for almost nothing — email plus optional state — the minimum viable commitment.

**PHASE 2 — Quiz CTA with TCPA Consent**

Replaces the email form entirely with:
- Headline: "Find out what your case is worth."
- CTA button → quiz
- Full TCPA consent with specific firm name
- TrustedForm + Jornaya active
- All three mandatory disclosures present

**Amber element:** Submit/CTA button fill.

**Content status:** Phase 1 implemented in `final-website/`. Phase 2 blocked on law firm partner.

---

### SECTION 8 — FOOTER

**Strategic purpose:** Functional. Brand close. Legal compliance. Light trust reinforcement.

**Color context:** Roman Navy `#0D1F3C`, full-bleed dark. Grid overlay.

**Layout:** Three-column grid (mirrors SC footer exactly). Thin amber vertical dividers. Legal strip below with amber rule above.

**Column 1 — Brand:**
- Fair Case full logo (white version, amber flame)
- Descriptor: "Understand your rights. Know what your case is worth."

**Column 2 — Navigate:**
- Label: "Navigate"
- Links: The Gap / What You Should Know / How It Works / Get Notified

**Column 3 — Connect:**
- Label: "Connect"
- Links: Instagram (@getafaircase) / Email

**Legal strip:**
> "This is an advertisement for legal services." · "© 2026 Fair Case" · Privacy Policy

Phase 2 adds: "You are not contacting an attorney directly. Your information will be shared with a participating law firm. Past results do not guarantee future outcomes."

**Amber element:** Vertical dividers between columns in amber rgba.

**Content status:** Implemented in `final-website/`.

---

## PHASE 2 TRANSITION CHECKLIST

Trigger: Signed law firm partner agreement.

- [ ] Hero CTA: scroll indicator → amber button "Get a Fair Case" → quiz
- [ ] Nav CTA: "Learn More" → amber button "Get a Fair Case"
- [ ] Section 5: Add amber CTA button after Step 3
- [ ] Section 7: Replace email form with quiz CTA + TCPA consent
  - [ ] Specific firm name in all consent language
  - [ ] TCPA checkbox unchecked by default, above submit
  - [ ] TrustedForm active and capturing
  - [ ] Jornaya LeadiD active
  - [ ] Lead routing tested
- [ ] Footer: Add lead-gen disclosure + outcome disclaimer to legal strip
- [ ] Meta: Remove `noindex, nofollow`
- [ ] Privacy Policy page must exist at linked URL
- [ ] State-specific SOL figures populated (Colorado: 3 years)
- [ ] Full compliance checklist from `DISCLOSURE_REQUIREMENTS.md` completed

---

## OPEN QUESTIONS

1. **Form backend (Phase 1)** — Formspree free tier (50 submissions/month) is lowest friction. Alternatives: Netlify Forms, Airtable embed. Decision needed for Section 7 backend integration.

2. **State-specific SOL figures** — Colorado: 3 years (C.R.S. § 13-80-101). Before expanding: CA 2 years, NY 3 years, FL 2 years (changed 2023 — verify), TX 2 years. Verify against current bar rules before use.

3. **Privacy Policy page** — Must exist before Phase 2. Needs to cover: data collection, use, sharing with law firm partners, CAN-SPAM unsubscribe, TCPA consent record retention.

4. **Contact email** — Footer needs a Fair Case email. `hello@getafaircase.com` or `info@getafaircase.com`. Confirm and set up.

---

## DESIGN SYSTEM QUICK REFERENCE

| Element | Value |
|---------|-------|
| Dark background | Roman Navy `#0D1F3C` |
| Light background | White `#FFFFFF` |
| Accent | Torch Amber `#C8821A` |
| Hover | Amber Dark `#A86A10` |
| Headline on dark | White, Tiempos upright |
| Headline on light | Roman Navy, Tiempos upright |
| Body on dark | White, Inter Regular |
| Body on light | Body Gray `#374151`, Inter Regular |
| Secondary on dark | Muted Navy `#A8B8CC` |
| Nav/section rules (dark) | `rgba(200, 130, 26, 0.48)` |
| Section dividers (light) | `rgba(13, 31, 60, 0.12)` |
| Section dividers (dark) | `rgba(200, 130, 26, 0.22)` |
| Font: brand | TiemposHeadline, Georgia, serif |
| Font: functional | Inter, system-ui, sans-serif |
| Container max | 1280px |
| Outer margin (desktop) | 80px |
| Nav height | 84px |
| Amber restraint | One amber element per section maximum |
| Section alternation | Dark → Light → Dark → Light → Dark → Light → Dark |

---

*Document owner: Davis Ballard*
*Next action: Review one-pager build → form backend decision → Phase 1 live*
*Phase 2 trigger: Signed law firm partner agreement*
