# Exit-Intent Popup Audit (Audit, Not Rebuild)

**Author:** Luke Wroblewski with Richard Shotton
**Date:** 2026-04-27
**Scope:** Davis confirmed Alex has an exit-intent popup already running. Davis's instruction: audit, don't rebuild.

---

## Status: pending verification

The Explore pass didn't surface a specific exit-intent component file in `lead-gen/apps/lead-gen-frontend/`. Either the popup is implemented in a sibling file the search didn't reach, or it's wired into the page-level component. Before this audit can be completed, an engineer (Alex) needs to point at the exact implementation file.

**Action:** Davis or Alex to confirm exit-intent file path. Once confirmed, finish this doc.

---

## Heuristic guidance until file is identified

Even without seeing the implementation, here's what we'd want to verify it does — and what we'd want to flag if it doesn't:

### What good exit-intent does

1. **Triggers only on intent signal.** Mouse moves toward the browser tab close, mobile back-button press, or 30+ seconds of inactivity on a question step. NOT on every page load. NOT on time-on-page alone.
2. **Triggers ONCE per session.** A claimant who closes the popup once and continues should never see it again that session. Re-popping is hostile UX.
3. **Trigger does NOT fire on Step 7 (contact step).** That's the highest-friction step; an exit-intent popup over a half-filled contact form is panic-inducing and pushes drop-off the wrong way.
4. **Copy frames the abandonment honestly, not desperately.** "Wait! Don't go!" is the wrong register. "If you're not sure this is for you, here's what to know" is the right register.
5. **Offers a clear NO option.** A close X in the corner. The user has agency.

### What bad exit-intent does (and we want to confirm Alex's doesn't)

- ⛔ Triggers on time-on-page alone (anyone reading slowly gets popup'd)
- ⛔ Re-triggers after dismissal (pure friction)
- ⛔ Uses fake urgency ("This offer expires in 5:00")
- ⛔ Adds fields the main funnel doesn't have ("Just give us your email and we'll send you a guide")
- ⛔ Asks for engagement that bypasses the form ("Get a free PDF guide instead")
- ⛔ Uses scare copy ("Statute of limitations is running out!" — Saul-flagged)

### Saul's traffic-light on common exit-intent copy patterns

| Phrase | Verdict |
|---|---|
| "Don't leave without your case review" | 🟡 Yellow — neutral, not great |
| "Time limits apply — don't wait" | 🟢 Green — factual statement, not false urgency |
| "Your case may be worth $X — find out" | 🔴 Red — A.R.S. ER 7.1 implied guarantee |
| "Still on the fence? Here's what we don't ask" | 🟢 Green — addresses real anxiety |
| "Most people finish in under 90 seconds" | 🟢 Green — friction-reduction signal, factual |

> **Saul:** Anything that promises a specific case value or implies you're missing out on money is a red flag. Anything that meets the claimant where the actual hesitation lives — "do I trust this?" "is this worth my time?" — is fair game.

---

## Recommended exit-intent copy (drop-in if Alex's needs replacement)

If, after auditing Alex's, the copy needs updating — here's a Saul-cleared, Shotton-validated, McCabe-tightened version:

**Headline:**
> Heading out?

**Body:**
> Most people finish this in under 90 seconds. If you're not sure this is for you, the most common reason people close this is that they don't realize the case review is genuinely free and doesn't commit them to anything.

**Two buttons:**
- Primary (Torch Amber): "Finish my evaluation"
- Secondary (text-only, `#6B7280`): "Close"

**Footer (small text):**
> *Get A Fair Case is operated by Second Chair. Your information is never shared without your consent.*

---

## What this doc does NOT cover

- The popup styling (lives in Alex's file when found, references `BRAND_SYSTEM_BRIEF` for color tokens)
- Trigger logic and JS implementation (Alex's domain, Luke advisory only)
- Analytics on popup show/dismiss/recover rates (separate analytics work)

---

*Pending: Alex to confirm exit-intent file path so this doc can be completed. Until then, this is a heuristic guide.*
