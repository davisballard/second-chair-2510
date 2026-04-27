# WCTL Arizona — Soft-Tissue Gate Logic

**Author:** Luke Wroblewski + Saul (compliance)
**Date:** 2026-04-27
**Constraint:** Davis's framing — *"we wont send them leads that are explicitly soft-tissue but sometimes its unclear and we dont want to assume its not soft-tissue and not send it to them but also not send them clear soft-tissue cases."*

---

## The architecture in one paragraph

Soft-tissue filtering happens at **two layers**: ad targeting (already in place — creative selects for non-soft-tissue intent at the click level) AND inside the form (this document). The form-side gate is **not a single hard-gate question**. It's a triangulation across three independent signals — Step 1 (injury type), Step 3 (medical treatment), Step 6 (injury markers checkbox). Three signals produce one of three outcomes per claimant: **clear non-soft-tissue → deliver to WCTL**, **ambiguous → Second Chair human review**, **clear soft-tissue → soft-block screen + redirect to better-fit resource**. The triangulation answers Davis's brief: clear soft-tissue out, ambiguous in for human review, qualified through.

---

## The three signals

| Signal | Source | Soft-tissue flag fires when |
|---|---|---|
| **S1: Vehicle/incident type** | Step 1 (`injury_type`) | "Something else" selected — routes to soft-decline before the gate even runs |
| **S3: Medical treatment** | Step 3 (`medical_treatment`) | `no` ("No medical treatment") selected |
| **S6: Injury markers** | Step 6 (`injury_markers` — new multi-select) | Only "None of these — soreness, bruising, or whiplash only" selected (no qualifying marker) |

> **Saul note:** S1 doesn't really live in the gate — it's a pre-filter. By the time we reach the gate, S1 is already a qualifying category from WCTL Section 1.3. The gate operates on S3 and S6 primarily, with auxiliary signals from Step 4 (at_fault) and Step 5 (has_attorney) handled separately as their own routing branches.

---

## The decision matrix

After Step 6 submission, evaluate the answer set:

```
┌─────────────────────────────────────────────────────────────────────┐
│  DECISION MATRIX                                                    │
├─────────────────────────────────────────────────────────────────────┤
│  S6 has ≥1 qualifying marker?                                       │
│    ├─ YES → S3 medical_treatment any value → DELIVER (unless        │
│    │       Step 4 = "partially at fault" → ROUTE TO HUMAN REVIEW)   │
│    │                                                                │
│    └─ NO (only "None of these" selected) →                          │
│        ├─ S3 = "no" → SOFT-BLOCK (clear soft-tissue)                │
│        ├─ S3 = "planning" → SOFT-BLOCK (clear soft-tissue, no       │
│        │                    medical signal yet)                     │
│        ├─ S3 = "yes_completed" or "yes_ongoing" → ROUTE TO HUMAN    │
│        │                    REVIEW (ambiguous — could be soft-      │
│        │                    tissue with PT or could be a not-yet-   │
│        │                    diagnosed disc / TBI)                   │
│        └─ S3 = absent → SOFT-BLOCK (data incomplete = treat as      │
│                                       soft-tissue conservatively)   │
└─────────────────────────────────────────────────────────────────────┘
```

### Three outcomes

**1. DELIVER → WCTL inbox**
Lead passes through. TrustedForm certificate captures the literal "West Coast Trial Lawyers" text on the consent step. Lead is sent within delivery SLA (Section 5.3 of WCTL agreement). Settlement estimator shown using the new multiplier model (`01_QUESTION_COPY.md`).

**2. ROUTE TO HUMAN REVIEW → Second Chair queue, not auto-delivered**
Lead lands in Second Chair's review queue. Sasha or designated reviewer makes a 1-2 minute call to the claimant within one business day to verify medical treatment specifics + fault context, then either greenlights to WCTL or soft-declines. The form-side experience for these claimants is identical to the DELIVER path — they don't know they were routed; from their perspective, the call from "the law firm" is a call from Second Chair acting as intake, then forwarding if confirmed.

**3. SOFT-BLOCK → soft-decline screen, no delivery, no consent capture**
Lead lands on a screen worded to preserve trust without lying:

> **Headline:** Thanks for sharing all that.
>
> **Body:** Based on what you've described, the firms we work with may not be the right fit for your case right now. The resources below are a better starting point — and if your situation changes (for example, if you discover an injury later that needed more medical attention), please come back.
>
> **Resource list:** State bar referral hotline (`https://www.azbar.org/findlawyer/`), Arizona free legal aid (`https://www.azlawhelp.org`).
>
> **Footer:** No CTA. Close gracefully.

> **Saul note:** The soft-block screen does NOT capture TCPA consent — by design. We never share a soft-tissue claimant's data with WCTL, period. We also don't capture the claimant's contact info because doing so creates a TCPA exposure surface for a lead we explicitly chose not to deliver. The claimant exits the funnel cleanly.

---

## The "ambiguous → human review" path in detail

This is the load-bearing part of Davis's instruction. *"Sometimes it's unclear and we don't want to assume it's not soft-tissue and not send it to them, but also not send them clear soft-tissue cases."*

**Trigger:** S6 = only "None of these" AND S3 ∈ {`yes_ongoing`, `yes_completed`}.

**Why this is ambiguous:** The claimant says they've had medical treatment but doesn't recognize their injury in the qualifying-marker list. Plausible explanations:
- They had a herniated disc but call it "back pain" and didn't know to check the disc box. Real qualifier — would land in WCTL's lap as a strong case.
- They had a concussion but the ER discharged them as "headache" and they didn't connect to the TBI box. Real qualifier.
- They've been in PT for whiplash for six months. Genuine soft-tissue.
- They had bruising and a doctor visit, no further care. Genuine soft-tissue.

The form can't disambiguate these from a checkbox. **A human can, in 90 seconds on a phone call.**

**Mechanism:** Second Chair operates as the intake gate before WCTL ever sees the lead. The claimant submits the form (full TCPA consent captured, naming WCTL as required). Second Chair's intake team calls within one business day, asks 2-3 verification questions ("Can you describe what your doctor said about your injuries?", "What kind of treatment have you received?", "Has anyone mentioned imaging or surgery?"), then:

- If clearly qualifying → forward to WCTL with intake notes
- If clearly soft-tissue → call ends warm, claimant gets the same redirect as the soft-block screen, lead is NOT forwarded. Lead does not appear in WCTL's queue and does not count against WCTL's 21-lead allotment.

> **Luke note:** From the claimant's perspective, the call from Second Chair feels identical to a "law firm intake" call. Friendly, professional, asks about their injury, says they'll follow up. There's no moment where the claimant feels gated. That preserves the brand experience and pulls the soft-tissue filter off the form-design surface.

> **Saul note (CRITICAL):** TCPA-wise, the consent at form submission must name **West Coast Trial Lawyers** — not "Second Chair" — because that's the named entity the claimant is consenting to be contacted by. Second Chair's intake call is technically permissible because Second Chair is acting as WCTL's authorized representative for intake (this is how every law firm runs — they have intake staff, sometimes outsourced, who call on their behalf before an attorney does). Document this in the WCTL service agreement letter of authorization (already covered under Section 8.1 — Provider obtains TCPA consent on Client's behalf). If WCTL later wants Second Chair to stop pre-screening, the gate moves from "human review" to "form delivers everything except soft-blocks" and we accept more credit cases. Davis's call.

---

## What the engineer builds

**File:** `lead-gen/apps/lead-pipeline-app/src/lib/lead-scoring.ts` (or a sibling file `wctl-az-gate.ts`)

```typescript
type GateOutcome = "deliver" | "review" | "soft_block";

function evaluateWctlAzGate(answers: Partial<QuizAnswers>): GateOutcome {
  const markers = answers.injury_markers ?? [];
  const hasQualifyingMarker = markers.some(m => QUALIFYING_MARKERS.has(m));
  const onlyNoneSelected = markers.length === 1 && markers[0] === "none_of_these";
  const treatment = answers.medical_treatment;

  // S6 has ≥1 qualifying marker
  if (hasQualifyingMarker) {
    // Auxiliary: at_fault = "partially_my_fault" → review
    if (answers.at_fault === "partially_my_fault") return "review";
    return "deliver";
  }

  // S6 = "None of these" only → check S3
  if (onlyNoneSelected) {
    if (treatment === "no" || treatment === "planning") return "soft_block";
    if (treatment === "yes_ongoing" || treatment === "yes_completed") return "review";
    return "soft_block"; // S3 absent or unexpected → conservative
  }

  // Should not reach here — defensive
  return "review";
}
```

**Wiring:**
- Form submission triggers `evaluateWctlAzGate()` server-side after Step 6 + Step 7 data lands.
- `"deliver"` → existing delivery pipeline to WCTL email (Section 5.2 of agreement).
- `"review"` → new Second Chair review queue (separate table or status flag).
- `"soft_block"` → no delivery; client-side renders the soft-block screen (no TCPA consent capture, no contact data persisted beyond what's needed for the screen and ad attribution).

**Order of operations matters:** the gate runs AFTER Step 6 submission but BEFORE the consent step. The dynamic consent loader in `ContactForm.svelte` (which already names the law firm based on ZIP) only loads if the gate returned `"deliver"` or `"review"`. Soft-block claimants never see the consent step.

---

## Verification — first 21 leads

Per `00_QUIZ_BRIEF.md` success criterion #1: zero soft-tissue leads delivered.

Verification at delivery:
1. Pull the first 21 delivered leads' raw quiz answers.
2. Confirm each has `injury_markers` containing ≥1 qualifying marker AND `at_fault ≠ "partially_my_fault"` (or, if `partially_my_fault`, that Second Chair human review confirmed).
3. Confirm each has TCPA TrustedForm certificate showing "West Coast Trial Lawyers" on screen.
4. Spot-check 3-5 with WCTL intake to confirm the named injuries hold up.

Verification of the soft-block path:
1. Pull soft-block events from analytics.
2. Confirm each shows `injury_markers === ["none_of_these"]` AND `medical_treatment ∈ {"no", "planning"}`.
3. Confirm zero of these claimants ended up in WCTL's inbox.

If verification finds a soft-tissue lead delivered: that's a bug in `evaluateWctlAzGate()` and ships as a P0 hotfix.

---

## Edge cases captured

- **Wrongful death (Step 1)** routes around the medical-treatment gate (the deceased can't have current treatment). Different qualification logic — needs `relationship_to_deceased` follow-up question. **Out of scope for the WCTL Arizona pilot's first 21 leads** — handle with a separate sub-flow or a manual override at intake. Document as P1 follow-up.

- **Claimant has a qualifying marker AND also self-identifies whiplash by checking BOTH a qualifying box and "None of these"** — the multi-select allows this. Treat as **deliver** (the qualifying marker takes priority). Disable "None of these" automatically when any qualifying marker is checked, with helper text "(Whiplash with another listed injury still qualifies — uncheck this if both apply.)".

- **Claimant changes Step 6 answer after Step 7** (e.g., uses browser back button) — the gate must re-evaluate on submission, not on Step 6 change. Single source of truth: the submitted record.

---

*Gate is locked. Implementation hands off to `wctl-az-gate.ts` per the spec above.*
