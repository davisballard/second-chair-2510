# Flow Audit — Live Quiz, Step by Step

**Author:** Luke Wroblewski (chair) with Richard Shotton (friction) and Ed McCabe (copy)
**Date:** 2026-04-27
**Method:** Heuristic audit of https://www.getafaircase.com/quiz against `../04_Visual_Identity_Brief/FORM_DESIGN_BRIEF.md` and `lead-gen/apps/lead-gen-frontend/src/lib/quiz-config.ts`

> **Luke:** Davis didn't give me drop-off data, so this is a heuristic audit, not a data audit. Every finding here gets validated by the analytics Alex is wiring up, but the issues called out are heuristics-class — they cost conversions whether or not we have the percentages yet.

---

## Cross-cutting findings (apply to every screen)

### ❌ The "Standard screening questions for the public quiz shell" subhead

**McCabe:** This is placeholder text. Internal stub copy that shipped to production. It reads as "we forgot to write this." Every screen has it.

**The fix:** Kill the global subhead. Replace with **question-specific reassurance microcopy** keyed to that step's anxiety profile (full copy in `WCTL_AZ/01_QUESTION_COPY.md`). Examples:

| Step | Question | Reassurance line under question |
|---|---|---|
| 1 | What happened? | One question at a time. Takes about 90 seconds. |
| 3 | Have you seen a doctor? | Treatment isn't required to qualify — we'll ask either way. |
| 4 | In your opinion, who caused the accident? | Honest answers help. Even partial fault doesn't stop most cases. |
| 6 | Which of these describe your injuries? | Check all that apply. Your answers stay private until you submit. |

### ❌ Trust-badge rotation has no rule

**Shotton:** The badges rotate without behavioral logic. Step 6 returns to "4.9/5 from 254 verified reviews" which we already showed at Step 1 — that's a wasted impression. Each step has a distinct anxiety profile, and the badge should answer it.

**The fix:** Anxiety-keyed map in `02_TRUST_SYSTEM.md`.

### ❌ Default font weight on questions reads light on mobile

**Chester (pulled in):** Question text needs Inter Semibold (600), 22-24px on mobile per `FORM_DESIGN_BRIEF.md`. Live screenshots look closer to 28-30px Bold. Visually heavy, slightly aggressive register. Consider stepping back to spec.

---

## Step 1 — "Let's start with what happened."

**Live state:** 6 options — Car / Truck / Motorcycle / Rideshare / Pedestrian / Other Vehicle Accident. Single-select, no auto-advance visible. Subhead: "Standard screening questions..."

### ❌ "Other Vehicle Accident" is a qualification leak

**Saul (pulled in):** Section 1.3 of the WCTL Service Agreement names exactly six case types. "Other" pulls in bus accidents (qualifies), parking lot fender-benders (excluded), bike accidents (qualifies as pedestrian-class? unclear), single-vehicle no-other-party (likely doesn't qualify). The agreement is binary; the form question shouldn't paper over that.

**The fix (full copy in `WCTL_AZ/01_QUESTION_COPY.md`):**
- Add **"Bicycle Accident"** as an explicit option (qualifies under WCTL pedestrian/bicycle category).
- Add **"Wrongful Death (loved one)"** as an explicit option (qualifies; currently has no path).
- Replace **"Other Vehicle Accident"** with **"Something else"** which routes to a soft-decline / "we don't currently handle this case type — try a different resource" screen rather than dumping unqualified leads into the funnel.

### ⚠️ No auto-advance on selection (heuristic — verify)

**Luke:** FORM_DESIGN_BRIEF Section 1 specifies auto-advance on single-select. Live screenshots show radio circles waiting for a separate Continue tap. If that's accurate, every step costs an extra tap on mobile. Alex to verify.

### ✅ Six options on one screen is okay here

Six is at the upper bound of what Hick's Law tolerates without paralysis, but these are highly distinct categories and the icons help. Not a problem.

---

## Step 2 — "When did this happen?"

**Live state:** 4 options — <30 days / 1–6 mo / 6–12 mo / Over 1 year. (Code shows a 5th "I'm not sure" option that doesn't render in the screenshot — verify.) Subhead: "Standard screening questions..." Top trust badge: "97% client success rate."

### ❌ Missing "I'm not sure" option in UI

**Code review:** `INCIDENT_DATE_OPTIONS` in `quiz-config.ts:42-48` includes `not_sure`. Screenshot shows only 4 options. Either render is broken or option was suppressed. This matters: a claimant who can't pin the date down to a 6-month window will abandon rather than guess. Restore the option.

### ⚠️ "Over 1 year ago" doesn't disclose Arizona's 2-year SOL

**Saul (pulled in):** Arizona statute of limitations on PI is **2 years from injury date** (A.R.S. § 12-542). A claimant who picks "Over 1 year ago" with a date 13–24 months back still qualifies; >24 months in the live data ranges fails Section 5.1(a) of the WCTL agreement (24-month recency window). The current UI gives no signal.

**The fix:** Split "Over 1 year ago" into:
- "Over 1 year ago, but within 2 years" → continues
- "More than 2 years ago" → soft-decline screen ("Arizona has a 2-year limit on most personal injury claims. A consultation may still help — here's a free legal aid resource.")

### ✅ Affirmation copy after this step is good

`getAffirmation` lines like "Acting quickly is smart. Evidence is strongest right now." earn their place.

---

## Step 3 — "Have you seen a doctor for your injuries?"

**Live state:** 4 options — Yes ongoing / Yes complete / Not yet planning to / No medical treatment. Top badge: "$0 — No fee unless we win your case."

### ❌ "No medical treatment" is one of three soft-tissue gate signals

**Luke + Saul:** Section 5.1(d) of the WCTL agreement requires "non-soft-tissue injuries including but not limited to: broken bones, surgical intervention, hospitalization..." If a claimant says "No medical treatment" and later picks "Minor" at Step 6, that's a CLEAR soft-tissue case. This question is one leg of the triangulation gate (full logic in `WCTL_AZ/02_SOFT_TISSUE_GATE.md`).

**The fix:** Keep the question, but its answer routes into the gate logic — no UI change at this step, but `medical_treatment === "no"` becomes a flag.

### ⚠️ "Not yet, but planning to" needs nuance

**McCabe:** A claimant who hasn't seen a doctor 9 months post-accident but says "planning to" is signaling a weak case. Either:
- Add a follow-up: "When are you planning to see a doctor?" with options that include "Within the next 7 days" → strong, "Sometime soon" → weak, OR
- Accept the friction and let the gate downstream do the work

Recommended: don't add a follow-up. Don't extend the funnel. Let the gate resolve it.

---

## Step 4 — "In your opinion, who caused the accident?"

**Live state:** 3 options — Not my fault / Partially at fault / I'm not sure. Top badge: "$150M+ recovered for clients."

### ✅ Question phrasing is right

**McCabe:** "In your opinion" is the magic phrase. It deflects self-incrimination ("I caused it") into a psychologically safer claim ("I think the other person caused it"). Good copy.

### ❌ "I'm not sure" is too generous

**Shotton:** When 30%+ of users pick "I'm not sure" at a fault question, that becomes the lazy default. The behavioral fix is to make "I'm not sure" the THIRD option (it is) AND add a one-line nudge under it: *"Pick the closest answer — an attorney sorts the rest."* This converts "not sure" into a meaningful signal vs. an escape hatch.

### ⚠️ Per Section 5.1(b), at-fault leads are credit-eligible

**Saul:** Section 5.1(b) requires the claimant is not the at-fault party (or not primary at-fault in shared-fault). Today the form passes "Partially at fault" through. Section 6.1(a) allows credit for at-fault leads, but credit is replacement, not refund — every credit slows delivery. Tighter form-side filtering protects WCTL from receiving leads that get clawed back.

**The fix:** Don't change the question — change the downstream weighting. "Partially at fault" passes through to Second Chair human review (not direct delivery to WCTL). Documented in `WCTL_AZ/02_SOFT_TISSUE_GATE.md`.

---

## Step 5 — "Are you currently working with an attorney?"

**Live state:** 3 options — No / Yes / I'm not sure. Top badge: "Free consultation — available 24/7."

### ❌ "Yes, I already have one" should soft-disqualify, not continue

**Saul:** Section 5.1(e) requires *"Lead confirms they do not currently have an attorney."* If a claimant says "Yes," WCTL can't take this lead — it's a credit case under Section 6.1(c). Today the funnel pushes through.

**The fix:** "Yes, I already have one" → graceful exit screen:

> **You're already represented.**
> Your existing attorney is your best advocate. If you'd like a second opinion, that conversation should start with them. We won't take it from here.
> *[no CTA, just close]*

This is a kindness AND a credit-prevention measure.

### ✅ "I'm not sure" passes through

Some claimants worked with a lawyer briefly and dropped them. "Not sure" is honest — Second Chair's intake call resolves it.

---

## Step 6 — "How would you describe your injuries?"

**Live state:** 4 options — Minor (Bruises, small cuts, soreness) / Moderate (Sprains, fractures, whiplash) / Severe (Surgery required) / Life-Altering (TBI, spinal). Top badge: "4.9/5 from 254 verified reviews."

### ❌❌❌ This question is broken on three axes (the headline finding)

**Luke:** This is the most consequential rewrite in the brief.

1. **Self-classification failure.** Most claimants don't have the medical literacy to distinguish "Moderate" from "Severe." A herniated disc that requires PT but not surgery — is that Moderate or Severe? A concussion with two days of nausea — Moderate or Severe? The labels force a guess that the data downstream treats as truth.

2. **Doesn't carry the WCTL gate logic.** Section 5.1(d) defines non-soft-tissue by **specific injury types**: broken bones, surgical intervention, hospitalization, herniated/bulging disc, TBI, concussion, lacerations requiring medical treatment, burns. The form should ask the question Section 5.1(d) asks.

3. **The current "Moderate" option includes "whiplash"** — which is the canonical soft-tissue example and the explicit exclusion in Section 1.4. Today, a whiplash-only claimant picks "Moderate" and gets through. That's a delivered soft-tissue lead.

**The fix (full rewrite in `WCTL_AZ/01_QUESTION_COPY.md`):** Convert Step 6 from a 4-option severity radio into a multi-select checkbox of concrete injury markers pulled from Section 5.1(d), with "None of these — soreness, bruising, or whiplash only" as the explicit soft-tissue self-disclosure option. Combined with Step 1 (injury type) and Step 3 (medical treatment), this drives the gate logic in `WCTL_AZ/02_SOFT_TISSUE_GATE.md`.

### ⚠️ Settlement multipliers tied to current severity scale need to be remapped

**Code:** `quiz-config.ts:149` — `severityMult: { minor: 0.6, moderate: 1.0, severe: 2.5, life_altering: 5.0 }`. After the Step 6 rewrite, this scale doesn't apply. New mapping in `WCTL_AZ/01_QUESTION_COPY.md`.

---

## Step 7 — "Your evaluation is ready." (Contact capture)

**Live state:** First name, Last name, Phone (tel input), Email, ZIP, dynamic consent loader, Recent Settlements table, three trust cards (97% / 4.9/5 / $0), Claim CTA, advertising disclaimer below.

### ❌ "Your request is handled securely. Second Chair reviews it first..." block is correct content but visually too heavy

**Chester:** The green-tinted reassurance block at the top of Step 7 is doing the right job (privacy reassurance at the highest-friction moment) but the green tint reads like a system alert. Per FORM_DESIGN_BRIEF Section 4, trust signals here should be subtle and tucked above the CTA, not banner-style at the top.

**The fix:** Demote to a single line: lock icon + *"Your information is private. Second Chair reviews requests before any law firm sees them."* immediately above the CTA button, not at the top of the form.

### ❌ "If your request is accepted, a law firm may call or text this number" undersells

**McCabe:** This phrasing is technically defensive but emotionally cold. "May call or text" reads as a passive threat. The claimant needs to know what *will* happen, not what *might.*

**The fix:** *"A specialist from West Coast Trial Lawyers will call within one business day. If they're not the right fit, that's the end — no follow-up calls."* Specific firm name (per TCPA 2025 one-to-one consent), specific timeline, explicit cap on contact frequency. Passes Saul's traffic-light at green and reads warmer.

### ❌ "Past results do not guarantee a similar outcome." disclaimer is in 8px gray

**Saul:** Below the settlement amounts. Currently muted to the point of invisibility. Per FORM_DESIGN_BRIEF Section 2, helper text is 13px minimum. AZ ER 7.1 doesn't specify font size but ABA guidance and platform policies expect *legibly disclosed*. 8px is hiding it.

**The fix:** Bump to 13px, `#6B7280`. Document in `06_COMPLIANCE_PACK.md`.

### ✅ ZIP code → law-firm match flow is solid

Reading the consent text dynamically based on ZIP is exactly the FCC 2025 architecture (per `../../../../06_Legal/Rulebook/01_TCPA_Consent_2025.md` Section 2). Don't change the mechanism. Do change what's named in the consent text — for AZ traffic, it must specifically say "West Coast Trial Lawyers" (full copy in `06_COMPLIANCE_PACK.md`).

### ⚠️ "Claim My Free Evaluation Now" — keep, but contextualize

**McCabe:** The CTA is fine as written (action-specific per Test #2 in FORM_DESIGN_BRIEF Section 6, ICE 9.0). Keep it. What matters more is the *closing line* immediately above — that's where the action is sold. See `05_FINAL_STEP_SOCIAL_PROOF.md`.

### ⚠️ "First Name (John) Last Name (Smith)" placeholders

**Luke:** "John Smith" placeholder text is standard but slightly generic. A/B priority is low — leave for now.

---

## Priority order for implementation

When Davis greenlights, ship in this order:

| Priority | Fix | Effort | Risk if not shipped |
|---|---|---|---|
| **P0** | Step 6 rewrite — concrete injury checkboxes | M | Soft-tissue leads delivered; credit disputes; relationship damage |
| **P0** | Step 1 — replace "Other" with explicit list + soft-decline route | S | Soft-tissue leakage via "Other" dump |
| **P0** | Step 5 — "Yes, I already have one" → graceful exit | S | Section 6.1(c) credits |
| **P0** | Per-step subhead — kill placeholder, install reassurance microcopy | S | Trust signal damage on every screen |
| **P0** | Final consent text — name "West Coast Trial Lawyers" specifically | S | TCPA 2025 violation; uninsurable risk |
| **P1** | Step 6 settlement multipliers — remap to checkbox model | M | Estimator inaccuracy |
| **P1** | Step 7 — privacy block demotion + dynamic firm name in confirmation | S | Cold final-step UX |
| **P1** | Trust badge map — anxiety-keyed rotation | S | Wasted trust impressions |
| **P1** | Step 2 — split "Over 1 year ago" by SOL boundary | S | Out-of-window leads (Section 6.1(d) credits) |
| **P2** | Header lockup — Roman Navy wordmark, non-clickable | S | Brand-handoff signal weakened (not breaking) |
| **P2** | Past-results disclaimer — bump to 13px | XS | Compliance hardening |
| **P2** | Header subhead — replace placeholder | (subset of P0) | Already in P0 list |
| **P3** | Auto-advance verification on single-select | XS | One extra tap per screen on mobile |
| **P3** | Question font weight — step back to spec | XS | Mild visual aggression |

---

*Audit complete. Continue to per-doc deliverables.*
