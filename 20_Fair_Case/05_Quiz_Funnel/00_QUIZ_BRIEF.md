# Fair Case Quiz Funnel — Working Brief

**Date:** 2026-04-27
**Convened by:** Nigel (liaison)
**Chair:** Luke Wroblewski (UI/UX Conversion)
**Active room:** Luke Wroblewski, Richard Shotton, Ed McCabe, Saul
**Silent observers:** Julian Cole, Chester Prides, Adam Ferrier
**Source of truth (existing spec, March 2026):** `../04_Visual_Identity_Brief/FORM_DESIGN_BRIEF.md` — Luke + Chester's locked form spec
**This document:** layered campaign + audit brief on top of FORM_DESIGN_BRIEF, scoped to the WCTL Arizona non-soft-tissue pilot

---

## Why we're here

Alex's live quiz at https://www.getafaircase.com/quiz is running and Davis wants every screen pressure-tested before WCTL Arizona traffic hits it. Two failure modes are unacceptable:

1. **Soft-tissue lead lands in WCTL's inbox.** Section 5.1(d) of the WCTL Service Agreement defines non-soft-tissue by concrete injury type. An at-fault or whiplash-only lead is a $475 charge against the relationship and a credit dispute (Section 6.1).
2. **Qualified non-soft-tissue claimant abandons the quiz.** Pilot economics ($9,975 / 21 leads) leave no room for funnel leakage. Friction on a real broken-bone victim is the worst place to lose.

The brief covers both scopes Davis split:
- **Shell-wide** — UX, design system, trust scaffolding, compliance, brand mark. Applies to every Fair Case client.
- **WCTL Arizona–specific** — question copy, qualification logic, soft-tissue triangulation, AZ-specific compliance. Lives in `WCTL_AZ/` subfolder.

---

## Success criteria

The brief is successful if **all four** are true at WCTL launch:

1. **Zero soft-tissue leads delivered.** A claimant who selects only minor severity AND no medical treatment AND a body-region answer that reads as soft-tissue is intercepted by the form's soft-block screen, not delivered.
2. **Ambiguous cases pass through.** A claimant who picks "Minor" but had medical treatment, or "I'm not sure" on at-fault, gets through — Second Chair reviews before forwarding. Davis's exact framing: *"we wont send them leads that are explicitly soft-tissue but sometimes its unclear and we dont want to assume its not soft-tissue and not send it to them but also not send them clear soft-tissue cases."*
3. **Step-1-to-submit completion ≥ 22%** on WCTL Arizona traffic (current Fair Case shell baseline; WCTL ad-level pre-qualification should pull this up, not down).
4. **TCPA consent passes Saul's traffic light at green.** TrustedForm certificate captures the literal "West Coast Trial Lawyers" text on screen at submission.

---

## What's broken in the live quiz (full audit in `01_FLOW_AUDIT.md`)

Headline issues, full diagnosis in `01_FLOW_AUDIT.md`:

- **"Standard screening questions for the public quiz shell" appears as the subhead on every step.** This is placeholder copy Alex never replaced. Reads as internal stub, breaks trust.
- **Step 6 "Minor / Moderate / Severe / Life-Altering" is a self-classification problem.** Most claimants can't distinguish "Moderate" from "Severe." Section 5.1(d) defines the gate by concrete injury types — that's what the question must ask.
- **Step 1 "Other Vehicle Accident" is a leak.** Bus, SUV-on-SUV, golf-cart-in-parking-lot, single-car-no-other-party — all converge here. Either widen the explicit list or kill "Other" entirely.
- **The trust badge rotation has no rule, AND the recovery number is 11x undersold.** Live shows "$150M+ recovered for clients" — actual WCTL is **$1.7 Billion+** per `In_Depth/WCTL_Market_Intelligence_Brief.md` line 20. Live settlements table is generic placeholder data (none of those are real WCTL cases). Both fixes in `02_TRUST_SYSTEM.md` and `05_FINAL_STEP_SOCIAL_PROOF.md`.
- **Final-step CTA "Claim My Free Evaluation Now" is fine, but the legal disclaimer below it is undersized and unanchored.** Saul flags 12-13px floor + a clearly bounded disclaimer block.

---

## What's locked from FORM_DESIGN_BRIEF.md (don't redesign)

These were Luke + Chester's March decisions and they hold:

- One question per screen, auto-advance on single-select
- Inter for functional copy, Tiempos for the wordmark only
- White form background (Test A) — variant B (`#FAFAF7` warm cream) is a documented test
- CTA: Torch Amber `#C8821A` fill, Roman Navy `#0D1F3C` text, 52px min height, 8px radius
- Field state colors: `#D1D5DB` default, `#374151` focus, `#059669` valid, `#DC2626` error
- Trust signal placement principle: at the friction moment, not the top
- Custom Next.js + Vercel build with TrustedForm + Jornaya integration

---

## What changes from FORM_DESIGN_BRIEF.md (Davis's decisions today)

| Item | Old (March spec) | New (today) | Reason |
|---|---|---|---|
| Logo linking behavior | Links to homepage in new tab | **Non-clickable** | Davis: header is trust-handoff anchor only, not navigation. Removes friction of "wait, where would clicking take me?" |
| Logo color flexibility | Roman Navy mark on white | **Roman Navy mark on white — locked, no charcoal alternate** | Chromatic continuity from Fair Case ad → form is the trust mechanism. Charcoal floats off-brand. |
| Step 6 (severity) | Subjective scale: Minor/Moderate/Severe/Life-Altering | **Concrete injury checkboxes from WCTL Section 5.1(d)** | Subjective severity is unreliable AND doesn't carry the gate logic; injury type does both jobs. Detail in `WCTL_AZ/01_QUESTION_COPY.md`. |
| Soft-tissue qualification | Not specified | **Triangulation across Steps 1 + 3 + 6, soft-block + Second Chair review** | Davis: ambiguous through, clear soft-tissue blocked. Detail in `WCTL_AZ/02_SOFT_TISSUE_GATE.md`. |
| Per-step subhead | "Standard screening questions for the public quiz shell" | **Killed entirely; replaced with rotating reassurance microcopy keyed to question** | Placeholder text. Detail in `WCTL_AZ/01_QUESTION_COPY.md`. |
| Trust badge rotation | Not specified | **Per-step badge map keyed to anxiety profile** | Detail in `02_TRUST_SYSTEM.md`. |

---

## Working steps — completed this session

1. Step-by-step audit of all 7 live quiz screens → `01_FLOW_AUDIT.md`
2. Per-step trust badge strategy → `02_TRUST_SYSTEM.md`
3. Brand mark + header layout decision → `03_BRAND_MARK_AND_LAYOUT.md`
4. Objection-handling secondary copy framework → `04_OBJECTION_COPY_FRAMEWORK.md`
5. Final-step social proof + settlements + CTA → `05_FINAL_STEP_SOCIAL_PROOF.md`
6. Compliance pack (TCPA + AZ disclosures + advertising disclaimer) → `06_COMPLIANCE_PACK.md`
7. Audit of Alex's existing exit-intent → `07_EXIT_INTENT_AUDIT.md`
8. WCTL Arizona question copy rewrite → `WCTL_AZ/01_QUESTION_COPY.md`
9. WCTL Arizona soft-tissue gate logic → `WCTL_AZ/02_SOFT_TISSUE_GATE.md`
10. WCTL Arizona compliance overlay → `WCTL_AZ/03_AZ_COMPLIANCE.md`
11. Session log → `_session_notes.md`
12. Arizona ER 7.1 added to → `../../../../06_Legal/Rulebook/04_State_Bar_Rules.md`

---

## Future scope — Tofer (NOT building now, just noted)

A separate Fair Case quiz instance is planned for **Tofer** that covers **all PI injuries including soft-tissue** — opposite qualification posture from WCTL Arizona's non-soft-tissue exclusion.

**What this means architecturally:**
- The shell-wide briefs in this folder (`00_QUIZ_BRIEF.md`, `01_FLOW_AUDIT.md`, `02_TRUST_SYSTEM.md`, `03_BRAND_MARK_AND_LAYOUT.md`, `04_OBJECTION_COPY_FRAMEWORK.md`, `05_FINAL_STEP_SOCIAL_PROOF.md`, `06_COMPLIANCE_PACK.md`, `07_EXIT_INTENT_AUDIT.md`) all apply to the Tofer instance. They're shell-wide for a reason.
- The WCTL_AZ-specific briefs (everything in `WCTL_AZ/`) **do NOT apply.** Tofer gets its own client subfolder when built — provisionally `Tofer/` parallel to `WCTL_AZ/`.
- The soft-tissue gate logic in `WCTL_AZ/02_SOFT_TISSUE_GATE.md` is specifically inverted for Tofer: the qualifying-marker checkbox set in Step 6 expands to include soft-tissue markers (whiplash, sprains, soreness) AS qualifying, and the "None of these" option becomes the soft-block trigger only when no injury at all is reported.
- TCPA consent text names Tofer (or whichever firm) instead of WCTL.
- Substantiation file lives separately at `Abracadabra/08_Brands/Second_Chair/23_Clients/Tofer/_Research/tofer_substantiation.md`.

**Status:** Not building Tofer's quiz instance right now. Documenting the architectural assumption so when we DO build it, the shell-wide work doesn't get re-litigated and the only new docs needed are Tofer-specific (question copy, qualification logic, compliance overlay). The shell briefs already absorbed the right-sized abstraction.

> **Nigel:** Davis flagged this for the record. The architecture supports it — shell-wide vs client-specific split is exactly the structure that makes adding Tofer (or any future client) a sub-week project, not a re-brief.

---

## Implementation handoff (post-brief)

When Davis greenlights, the engineering edits land in the lead-gen repo:

- `lead-gen/apps/lead-gen-frontend/src/lib/quiz-config.ts` — STEPS_ORDER, INJURY_SEVERITY_OPTIONS rewrite to checkbox model, affirmation copy, settlement multipliers updated, `buildTcpaConsentText` advertiserName parameter set to `"West Coast Trial Lawyers"` for AZ traffic
- `lead-gen/apps/lead-gen-frontend/src/lib/components/quiz/ContactForm.svelte` — final-step layout matches `05_FINAL_STEP_SOCIAL_PROOF.md`
- `lead-gen/apps/lead-gen-frontend/src/lib/AuthoredQuestionnairePage.svelte` and `LegacyQuestionnairePage.svelte` — kill the placeholder subhead, swap in question-keyed reassurance microcopy from `WCTL_AZ/01_QUESTION_COPY.md`, update header with non-clickable Roman Navy wordmark per `03_BRAND_MARK_AND_LAYOUT.md`
- `lead-gen/apps/lead-gen-frontend/src/lib/landing-config.ts` — soft-tissue framing copy updated to match the form-side gate UX so messages don't contradict
- New: soft-block disqualification screen component (UX in `WCTL_AZ/02_SOFT_TISSUE_GATE.md`)

---

*The form's design quality IS the trust signal (per FORM_DESIGN_BRIEF.md). This brief sharpens that signal for the WCTL Arizona window — nothing more, nothing less.*
