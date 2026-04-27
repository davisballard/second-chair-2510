# Trust System — Per-Step Badge Map

**Author:** Richard Shotton (behavioral) with Luke Wroblewski (placement) and Saul (defensibility)
**Date:** 2026-04-27
**Source of truth foundation:** `../04_Visual_Identity_Brief/FORM_DESIGN_BRIEF.md` Section 4 — trust signals at the friction moment, not the top.

> **Shotton:** Each step in the quiz has its own anxiety profile. Generic trust badges that rotate without logic are wasted impressions. The badge at each step needs to answer the question the user is silently asking at *that* moment. That's not branding — that's behavioral targeting at the screen level.

---

## The five live badges (already designed, defensible)

The quiz code already has five trust badges built. They're well-written; the issue is rotation logic, not copy.

| Badge | Live copy | WCTL-substantiated rewrite | Defensibility (Saul) |
|---|---|---|---|
| ★ Reviews | `4.9/5 from 254 verified reviews` | (verify with Sasha — count must reflect WCTL's actual review aggregate, not Fair Case shell average) | ✅ Defensible if substantiated |
| 🛡️ Success rate | `97% client success rate` | **`97% of qualifying cases reach a settlement or verdict`** | ⚠️ "Success rate" too vague; rewritten version is harder to challenge |
| 💲 No fee | `No fee unless we win your case` | (unchanged) | ✅ Standard contingency disclosure |
| 📈 Recovered | `$150M+ recovered for clients` | **`$1.7 Billion+ recovered for clients*`** | ✅ Substantiated by `WCTL_Market_Intelligence_Brief.md` line 20. Live "$150M+" undercuts WCTL by 11x. The asterisk links to the past-results disclaimer. |
| 🕒 Consultation | `Free consultation — available 24/7` | (verify with Sasha — change to "Free consultation — same-day callback" if WCTL intake doesn't actually run 24/7) | ✅ Defensible if substantiated |

**Action items before launch:**
1. **Update `$150M+` → `$1.7 Billion+`** in `lead-gen/apps/lead-gen-frontend/src/lib/trust-signals.ts` (or wherever this is configured). Verbatim from WCTL public-facing data.
2. Rewrite "97% client success rate" → "97% of qualifying cases reach a settlement or verdict." Update copy in `quiz-config.ts` or `trust-signals.ts`.
3. Add `*` to "$1.7 Billion+ recovered for clients" linking to the final-step disclaimer.
4. Confirm review count + source with Sasha. WCTL has 12 years of operation and substantial review presence; the 254 figure may need adjustment up or down based on what's actually verifiable.
5. Confirm WCTL intake actually runs 24/7. If not, change to "Free consultation — same-day callback."

---

## The anxiety profile of each step

Each step in the quiz raises a different silent question in the claimant's head. The right badge answers that question.

| Step | Question | Silent claimant anxiety | Best-fit badge | Why |
|---|---|---|---|---|
| 1 | What happened? | "Is this site real?" | ★ **`4.9/5 from 254 verified reviews`** | First impression. Legitimacy gate. Social proof beats every other signal at the front door. |
| 2 | When did it happen? | "Will I be told no for waiting too long?" | 🛡️ **`Handled securely · No upfront charge to submit`** (header carries — no rotation needed) | Anxiety here is procedural, not financial. The header trust elements already cover this. |
| 3 | Have you seen a doctor? | "Will I be charged for this?" / "Do I need to have insurance/income to qualify?" | 💲 **`No fee unless we win your case`** | The medical question primes the cost question. Answer it before they ask. |
| 4 | Who caused the accident? | "What if my answer kills my case?" | 📈 **`$1.7 Billion+ recovered for clients\*`** | Authority signal at the moment of self-doubt. The new $1.7B figure (substantiated, not the live "$150M+") lands harder at this moment. |
| 5 | Are you working with an attorney? | "Will this take forever?" / "When can I talk to someone?" | 🕒 **`Free consultation — available 24/7`** (or "same-day callback") | Speed/access answer. Lowers the perceived commitment. |
| 6 | Which describe your injuries? | "I don't know if my injury counts" / "What if I check the wrong thing?" | ★ **`4.9/5 from 254 verified reviews`** | Highest cognitive load step in the entire form (it's a 12-option multi-select). Return to the strongest, simplest legitimacy signal. |
| 7 | Contact + consent | "Will I be spammed?" / "Is my info safe?" | 🛡️ **`97% of qualifying cases reach a settlement or verdict`** | Authority + outcome at the highest-friction moment. NOT lock-icon-as-badge — that lives in the privacy line. |

> **Shotton note:** The reuse of the ★ Reviews badge at Step 1 and Step 6 is intentional, not lazy. Both are moments of "is this real?" anxiety — Step 1 because it's first, Step 6 because the cognitive load is highest. The other steps don't need the same signal. Repetition with purpose is fine; rotation for rotation's sake is what's broken in the live quiz.

> **Luke note:** Each badge is a single sentence above the question, centered, Inter Regular 14px. Same line height across all steps. The colored icon prefix (✅ shield, $ dollar, 📈 chart, 🕒 clock, ★ star) is the visual differentiator — not the badge background or color. Backgrounds stay neutral; the icon does the lifting.

---

## Density rules

**Per step: ONE primary trust badge** above the question. Period.

The live form sometimes shows multiple "✅ No upfront charge to submit | 🔒 Handled securely" — that pair is two badges side-by-side. **That pair stays in the persistent header**, NOT as a per-step badge. They're frame elements, not per-step signals.

So the visual stack on every step is:

```
[Persistent header: Fair Case wordmark / progress bar / 🛡️ persistent header pair]
[Per-step trust badge — single, anxiety-keyed]
[Question]
[Reassurance subhead]
[Options]
[Footer disclosure]
```

**Three layers of trust:** persistent header (legitimacy at all times), per-step badge (answer the screen's anxiety), final-step social proof block (close the deal). Each layer does a distinct job.

---

## What each layer does NOT do

- **Persistent header** does not include marketing claims (no "best," no "fastest"). Only static factual signals: secure handling, "no upfront charge to submit." These never change between steps.
- **Per-step badges** do not stack — one per step. Two badges on a screen is noise.
- **Final-step social proof block** (settlements + cards) does not appear on any step before Step 7. The settlement amounts are reserved for the moment they're earned. Showing them at Step 1 dilutes the closing impact.

---

## Implementation notes for the engineer

`lead-gen/apps/lead-gen-frontend/src/lib/trust-signals.ts` (or wherever `STEP_TRUST_SIGNALS` is configured):

```typescript
const WCTL_AZ_TRUST_BADGES: Record<QuizStep, TrustBadge> = {
  injury_type:        { icon: "★",  text: "4.9/5 from 254 verified reviews" },
  incident_date:      { icon: null, text: null }, // header carries
  medical_treatment:  { icon: "$",  text: "No fee unless we win your case" },
  at_fault:           { icon: "📈", text: "$1.7 Billion+ recovered for clients*" },
  has_attorney:       { icon: "🕒", text: "Free consultation — same-day callback" },
  injury_markers:     { icon: "★",  text: "4.9/5 from 254 verified reviews" },
  contact:            { icon: "🛡️", text: "97% of qualifying cases reach a settlement or verdict" },
};
```

The asterisk on the `at_fault` badge links to the final-step disclaimer block.

---

*Trust system locked. Pre-launch action items: substantiate the review count + success-rate phrasing + 24/7 vs same-day claim with Sasha.*
