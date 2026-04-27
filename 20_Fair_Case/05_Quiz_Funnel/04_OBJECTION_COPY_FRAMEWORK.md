# Objection-Handling Secondary Copy — The "Disclosure on Tap" Pattern

**Author:** Richard Shotton (cognitive load) with Ed McCabe (copy) and Luke Wroblewski (UX)
**Date:** 2026-04-27
**Davis's brief:** *"secondary information below each step if needed to handle objections without overwhelming."*

---

## The pattern in one sentence

For the small subset of claimants who need more context to commit, surface a single tap-to-expand "Why are we asking?" link below each question — claimants who don't need it never see it; claimants who do, get a one-paragraph answer.

---

## Why this pattern (not "supportive copy under every question")

**Shotton:** Cognitive load research is unambiguous on this — every visible element on a screen taxes the read. A claimant who already trusts the question doesn't need an explanation; explaining anyway adds friction to *their* path. The objection-handling copy must be available but not present by default.

**The wrong move:** Add 2-3 lines of supportive copy under every question. This makes every screen 25% denser, slows the scan, and reads as defensive ("why are they explaining this so much?").

**The right move:** A single muted "Why we're asking →" link below the question's options. Tap to expand. One paragraph appears in-place (no modal, no page navigation). Tap to collapse.

---

## Per-step expansion copy

Format spec: Inter Regular 14px, `#374151`, expands inline below the options block. Animation: 200ms slide-down. Background: `#F9FAFB` (very light gray) with 8px border-radius and 16px padding to clearly separate from the question UI.

---

### Step 1 — What happened

**Tap target:** "Why we're asking →"

**Expanded copy:**
> Different accident types involve different laws, insurance rules, and liability rules. Truck cases involve federal trucking regulations; motorcycle cases sometimes involve helmet-law arguments; pedestrian cases turn on right-of-way and visibility. Naming the type early helps us send your case to the right specialist.

> **McCabe:** No "we ask this because we care about you" — that's the language of bad form copy. Say what the answer DOES, not what it represents.

---

### Step 2 — When it happened

**Tap target:** "Why we're asking →"

**Expanded copy:**
> Arizona has a 2-year statute of limitations on most personal injury cases. Cases more than 2 years old usually can't be filed, with some exceptions (like injuries that were not immediately discoverable). The window matters; the exact day usually doesn't.

> **Saul note:** This is a useful place to plant the SOL fact — when the claimant is willing to look. Plants the seed of "time matters" without alarmism.

---

### Step 3 — Medical treatment

**Tap target:** "Why we're asking →"

**Expanded copy:**
> Medical records are often the strongest evidence of what an injury cost — physically and financially. We ask about treatment so an attorney can ballpark whether your case has the documentation it needs. If you haven't seen a doctor yet but plan to, that's not a deal-breaker; it just changes the next steps.

---

### Step 4 — Fault

**Tap target:** "Why we're asking →"

**Expanded copy:**
> Arizona is a comparative-fault state — partial fault rarely kills a claim, but the percentage of fault directly reduces your recovery. We're asking your honest read so an attorney can tell you the realistic range. "I'm not sure" is a perfectly normal answer; police reports and witness accounts usually settle it.

---

### Step 5 — Existing representation

**Tap target:** "Why we're asking →"

**Expanded copy:**
> If you already have an attorney, your existing relationship is your best advocate — switching mid-case rarely helps. If you've consulted with someone briefly but didn't hire them, they're not your attorney. We're asking to make sure we don't accidentally interfere with a real existing case.

---

### Step 6 — Injury markers

**Tap target:** "Why we're asking →"

**Expanded copy:**
> The law firms in our network focus on cases with documented physical injuries — fractures, surgery, hospitalization, disc damage, head injuries, and similar. They're not the right fit for cases involving only soreness or whiplash without other injuries. Telling us what's on your medical record helps us point you to the right place from the start.

> **Shotton note:** The phrase "from the start" is doing work here — it reframes the soft-tissue exclusion as a kindness to the claimant ("we'll point you somewhere better right away") rather than a gate ("we don't want your case"). Same fact, different emotional valence.

---

### Step 7 — Contact + consent

**Tap target:** "What happens to my information →"

**Expanded copy:**
> When you submit, your contact information goes to Second Chair (the company that operates this site) for a quick review. If your case fits the law firm that serves your ZIP code, your information is forwarded to that firm's intake team — which for Arizona is West Coast Trial Lawyers. They'll call within one business day. If your case doesn't fit, we don't share your information with anyone, and we contact you to point you to a better resource.

> **Saul note:** This is the most important expansion in the entire form. It tells the literal truth about the data flow at the precise moment the claimant is being asked to submit. A claimant who taps "What happens to my information" and reads this paragraph then commits with eyes open. That's stronger consent than language they didn't read.

---

## What expansion copy NEVER does

- **Sells.** No "we'll get you the best result." No "thousands of victims trust us." This is reassurance, not marketing.
- **Repeats the trust badge.** The badge says one thing, the expansion says another. Don't restate.
- **Asks for action.** No "click here to learn more," no secondary CTAs. The expansion ends; the claimant returns to the question.
- **Exceeds 3 sentences for any step except Step 7.** Step 7 gets 4 sentences because the data-flow truth requires more.
- **Names compliance terms by their formal names.** "TCPA" is a phrase Saul uses — the claimant reads "automated calls and texts" in plain English. The technical compliance language lives in the consent block; the expansion uses the human translation.

---

## Engagement target

**Don't track expansion taps as a success metric.** Per Shotton: an expansion tap rate of 5% means 5% needed it. An expansion tap rate of 30% would actually be a problem — it would mean a third of claimants don't trust the form's primary read and need help. The right level of engagement is *low*. A claimant who flies through without ever tapping is a claimant who trusts the form, which is what we want.

> **Luke note:** The metric we DO care about is whether expansion taps correlate with completion. If claimants who tapped on Step 6 expansion completed at a higher rate than non-tappers, the expansion did its job — it absorbed an objection that would have been a drop-off. If completion is flat regardless of tap, the expansion is decorative and we kill it. Wire this in analytics.

---

## Implementation handoff

**Component:** `<QuestionExpansion>` shared component, takes a single `text` prop and a tap target label.

**Placement:** Below the options block, above the per-step Continue button (when applicable — Steps 6 and 7 use Continue; Steps 1-5 auto-advance).

**State:** Collapsed by default. Tracks open/close in component state. Closes automatically when the user advances to the next question (no need to remember preferences).

**Accessibility:** Tap target is a real `<button>` not a styled `<div>`. ARIA expanded state. Screen-reader text describes the expansion.

---

*Objection copy framework locked. Six question expansions + one consent expansion. None of them visible by default.*
