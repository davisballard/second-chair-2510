# WCTL Arizona — Quiz Question Copy

**Author:** Ed McCabe (copy lead) with Luke Wroblewski (flow), Saul (compliance), Richard Shotton (microcopy)
**Date:** 2026-04-27
**Scope:** Every line of copy on the seven quiz steps for the WCTL Arizona non-soft-tissue pilot. Replaces the live copy in `lead-gen/apps/lead-gen-frontend/src/lib/quiz-config.ts` for AZ traffic.

> **McCabe:** I rewrote everything once, then cut it in half, then asked Saul which words couldn't ship. That's the version below. If a line could be cut without losing the job, I cut it.

---

## Global rules across all steps

**Header (every step):** Fair Case wordmark + torch in Roman Navy `#0D1F3C`, non-clickable, centered (per `03_BRAND_MARK_AND_LAYOUT.md`).

**Top trust badge:** anxiety-keyed per step (per `02_TRUST_SYSTEM.md`).

**Progress bar:** Torch Amber fill, gray track, "Step X of 7" + percent on right.

**Subhead under question:** **Kill the live placeholder** ("Standard screening questions for the public quiz shell"). Replace with **per-question reassurance microcopy** (specified per step below). One short line, Inter Regular 14px, `#6B7280`. Never marketing copy. Always reassurance / cognitive load reduction.

**Affirmation after answer (200ms appearance, fades into next question):** one warm sentence per option, specified per step. McCabe-rewritten from the live `getAffirmation` function.

---

## Step 1 — What happened

**Top badge:** `★ 4.9/5 from 254 verified reviews` (legitimacy gate — first impression).

**Question (Inter Semibold 22-24px, Roman Navy):**
> Let's start with what happened.

**Reassurance subhead (Inter Regular 14px, `#6B7280`):**
> One question at a time. Takes about 90 seconds.

**Options (single-select, auto-advance):**

| Option | Icon | Affirmation (passes through) | Routing |
|---|---|---|---|
| Car Accident | 🚗 | *"Car accidents are the most common case we evaluate."* | → Step 2 |
| Truck or Commercial Vehicle | 🚛 | *"Trucking cases often carry significant claim value."* | → Step 2 |
| Motorcycle Accident | 🏍️ | *"Motorcycle injuries are taken seriously by every firm we work with."* | → Step 2 |
| Rideshare (Uber / Lyft) | 🚕 | *"Rideshare liability is more layered than a standard accident — there's usually more to recover."* | → Step 2 |
| Pedestrian or Bicycle | 🚶 | *"Pedestrian and cyclist cases tend to qualify quickly."* | → Step 2 |
| Wrongful Death (loved one) | 🕊️ | *"We're sorry. We'll handle the rest of this carefully."* | → Step 2 (with sensitive routing flag) |
| Something else | — | (no affirmation) | → **soft-decline screen** (see end of doc) |

> **McCabe note:** The live "Other Vehicle Accident" is replaced by "Something else" which routes off the funnel. Anything that doesn't fit one of the named categories is a non-fit for WCTL — better to acknowledge than dump.

> **Shotton note:** Wrongful Death affirmation needs to be the shortest. Any extra word reads as performance. Two sentences max, the second softer than the first.

---

## Step 2 — When it happened

**Top badge:** `🛡️ Handled securely · No upfront charge to submit` (carries from header — no rotation here).

**Question:**
> When did this happen?

**Reassurance subhead:**
> Approximate is fine — we don't need an exact date.

**Options (single-select, auto-advance):**

| Option | Affirmation | Routing |
|---|---|---|
| Less than 30 days ago | *"Acting early is smart. Evidence is freshest right now."* | → Step 3 |
| 1 – 6 months ago | *"You're well within Arizona's window for most claims."* | → Step 3 |
| 6 – 12 months ago | *"Still within the window. Let's keep going."* | → Step 3 |
| Over 1 year ago, but within 2 years | *"Within Arizona's 2-year statute of limitations. Cases like yours still qualify."* | → Step 3 |
| More than 2 years ago | (no affirmation) | → **statute-of-limitations soft-decline** (see end of doc) |
| I'm not sure | *"That's normal. We can usually narrow it down on the call."* | → Step 3 (flag: ambiguous date) |

> **Saul note:** A.R.S. § 12-542 is the 2-year SOL. Section 5.1(a) of the WCTL agreement specifies a 24-month recency window. The "more than 2 years" branch protects WCTL from out-of-window leads (Section 6.1(d) credit-eligible) AND tells the claimant something true and useful instead of routing them to a dead end.

---

## Step 3 — Medical treatment

**Top badge:** `$ No fee unless we win your case` (cost objection at the moment medical/cost concerns surface).

**Question:**
> Have you seen a doctor about your injuries?

**Reassurance subhead:**
> Treatment isn't required to qualify — we'll ask either way.

**Options (single-select, auto-advance):**

| Option | Affirmation | Gate flag |
|---|---|---|
| Yes — I'm currently in treatment | *"Ongoing treatment strengthens almost every case."* | strong |
| Yes — treatment is complete | *"Completed treatment gives us clean records to work with."* | strong |
| Not yet, but I'm planning to | *"Seeing a doctor matters for both your health and your case. Worth doing soon."* | medium |
| No medical treatment | (no affirmation, advances quietly) | **soft-tissue flag #1** |

> **Luke note:** "No medical treatment" is one of three triangulation signals (full logic in `02_SOFT_TISSUE_GATE.md`). The form doesn't react at this step — just records it. A claimant who picks this option does not yet know they're being routed.

---

## Step 4 — Fault

**Top badge:** `📈 $1.7 Billion+ recovered for clients*` (proof at the moment of self-doubt). Asterisk resolves to past-results disclaimer per `02_TRUST_SYSTEM.md` and `05_FINAL_STEP_SOCIAL_PROOF.md`. **Substantiation:** $1.7B is the canonical WCTL aggregate per Davis confirmation 2026-04-27 and `Abracadabra/08_Brands/Second_Chair/05_Restrictions/arizona/13_Substantiation_File_Spec.md`.

**Question:**
> In your opinion, who caused the accident?

**Reassurance subhead:**
> Honest answers help. Even partial fault doesn't stop most cases.

**Options (single-select, auto-advance):**

| Option | Affirmation | Routing |
|---|---|---|
| It was not my fault | *"This is one of the strongest factors in a case."* | direct path |
| I may be partially at fault | *"Arizona is a comparative-fault state — partial fault rarely kills a claim."* | flag: partial fault → Second Chair review before delivery |
| I'm not sure | *"That's normal. An attorney can usually figure out fault from the police report."* | flag: ambiguous fault → Second Chair review |

**Pre-tap nudge (appears below "I'm not sure" only, Inter Regular 13px `#6B7280`):**
> Pick the closest answer — an attorney sorts the rest.

> **Shotton note:** Without that nudge, "I'm not sure" becomes the lazy default and we lose signal. With it, claimants who genuinely aren't sure still pick it; lazy ones move to one of the real answers.

> **Saul note:** Section 5.1(b) requires the lead is not the at-fault party. "Partially at fault" stays in the funnel but routes to human review — Section 6.1(a) at-fault credit risk is mitigated by Second Chair filtering.

---

## Step 5 — Existing representation

**Top badge:** `🕒 Free consultation — available 24/7` (lowers barrier just before the highest-friction screens).

**Question:**
> Are you currently working with an attorney?

**Reassurance subhead:**
> If you are, that's great — we'll just point you in the right direction.

**Options (single-select, auto-advance):**

| Option | Affirmation | Routing |
|---|---|---|
| No, I don't have an attorney | *"Got it. Let's keep going."* | → Step 6 |
| Yes, I already have one | (no affirmation) | → **already-represented graceful exit** (see end of doc) |
| I'm not sure | *"Some people consulted a lawyer briefly and don't think of it as 'having' one. We'll figure it out on the call."* | → Step 6 (flag: verify on intake call) |

> **Saul note:** Section 5.1(e) requires confirmation of no current representation. "Yes, I already have one" used to push through the funnel — that was a Section 6.1(c) credit case. Now it gracefully exits.

---

## Step 6 — Injury markers (THE GATE QUESTION — REWRITTEN)

**Top badge:** `★ 4.9/5 from 254 verified reviews` (high-cognitive-load step — return to the strongest legitimacy signal).

**Question:**
> Which of these describe your injuries?

**Reassurance subhead:**
> Check all that apply. Your answers stay private until you submit.

**Format:** **Multi-select checkboxes**, NOT radio buttons. Not auto-advance — claimant taps "Continue" after selecting. (FORM_DESIGN_BRIEF Section 1 supports manual-advance for multi-select.)

**Options (Inter Regular, with optional secondary description per Section 5.1(d)):**

| Option | Description (optional, expands on tap) | Gate value |
|---|---|---|
| Broken or fractured bones | Includes hairline fractures, breaks, dislocations | qualifying |
| Surgery (had or scheduled) | Any surgical procedure related to the accident | qualifying |
| Hospital stay (overnight or longer) | Admitted to a hospital, not just an ER visit | qualifying |
| Herniated, bulging, or ruptured disc | Diagnosed by MRI or doctor | qualifying |
| Concussion or traumatic brain injury (TBI) | Including loss of consciousness or post-concussion symptoms | qualifying |
| Lacerations needing stitches or scarring | Cuts that required stitches, staples, or left visible scars | qualifying |
| Burns | Second-degree or worse | qualifying |
| Dental or facial injury | Lost teeth, broken jaw, facial fractures | qualifying |
| Spinal cord injury or paralysis (full or partial) | Including any loss of function | qualifying — high priority |
| Internal injuries | Organ damage, internal bleeding | qualifying |
| Permanent disability or scarring | Long-term loss of function or visible scarring | qualifying |
| **None of these — soreness, bruising, or whiplash only** | (no expand) | **soft-tissue flag #2** |

**Continue button (sticky, Torch Amber):** "Continue"

**Affirmation after Continue (varies by selection set):**

- Any qualifying option selected → *"This is the kind of detail that gives an attorney something to work with."*
- "None of these" selected alone → (no affirmation, quiet advance — the gate logic decides next step)

> **Luke note:** This is the question Section 5.1(d) of the WCTL agreement asks. The answer set is the same vocabulary the credit policy uses, so a "qualifying" form answer matches what counts as a non-credit lead. We removed the self-classification problem ("Moderate vs Severe") and replaced it with concrete, verifiable injury markers.

> **McCabe note:** "None of these — soreness, bruising, or whiplash only" is the explicit soft-tissue self-disclosure. Naming whiplash directly is what makes the gate work. A claimant who genuinely had only whiplash will check it; a claimant with a herniated disc won't.

> **Saul note:** The list maps 1:1 to Section 5.1(d). If WCTL audits a delivered lead and the claimant didn't have one of these injuries, that's now a deterministic credit case (Section 6.1(b)) — but the form-level filter should mean it almost never happens.

---

## Step 7 — Contact + consent (final)

(Layout, social proof, settlements table, and CTA spec live in `../05_FINAL_STEP_SOCIAL_PROOF.md`. Question copy below.)

**Top badge:** `🛡️ 97% client success rate` (closing-step authority signal).

**Headline:**
> Your evaluation is ready.

**Subhead:**
> Where should we send your case review?

**Privacy line above CTA (replaces the green block at top):**
> 🔒 Your information is private. Second Chair reviews each request before any law firm sees it.

**Field labels:** First name · Last name · Phone number · Email address · ZIP code

**Helper under phone:**
> A specialist from West Coast Trial Lawyers will call within one business day. If they're not the right fit, that's the end — no follow-up calls.

**Helper under ZIP:**
> Used to confirm your case falls in our service area.

**TCPA consent text (full, locked by Saul — see `06_COMPLIANCE_PACK.md`):**
> By clicking "Claim My Free Evaluation Now," I authorize Second Chair through getafaircase.com to share my request with **West Coast Trial Lawyers**, the law firm that serves my ZIP code. I authorize West Coast Trial Lawyers and its intake team to call and text me at the phone number I provided, including via automated dialing or prerecorded messages. Consent is not required to receive legal services. Message and data rates may apply. Submitting this form does not create an attorney-client relationship.

**CTA button:** **"Claim My Free Evaluation Now"** (Torch Amber `#C8821A`, Roman Navy text, 52px height)

**Below CTA disclaimer block (Inter Regular 13px, `#6B7280`, single bordered paragraph):**
> This is an attorney advertisement. Submitting this request is free and does not require you to hire a lawyer. Statutes of limitations apply to all cases. Past results do not guarantee a similar outcome. West Coast Trial Lawyers is the law firm that may contact you and is solely responsible for any legal services it provides. Second Chair operates the Get A Fair Case intake platform and is not a law firm.

---

## Soft-decline / graceful exit screens

These three screens are not Step 8 — they're branch endpoints from earlier steps.

### A) "Something else" path (from Step 1)

**Headline:** Thanks for telling us.
**Body (Inter Regular 16px):** Right now, the firms we work with focus on motor vehicle, motorcycle, pedestrian, bicycle, and wrongful death cases. If your situation is different, the resources below are a better starting point.
**Resource list:** State bar referral hotline (`https://www.azbar.org/findlawyer/`), Arizona free legal aid (`https://www.azlawhelp.org`).
**Footer:** "If anything changes, you can come back any time." No CTA.

### B) Statute-of-limitations soft-decline (from Step 2 "more than 2 years")

**Headline:** Arizona has a 2-year limit on most personal injury claims.
**Body:** Your accident may be outside that window, which means most attorneys won't take a case at this stage. There are a few exceptions — for instance, if the injury wasn't immediately discoverable. A free conversation with the resources below can confirm whether anything still applies.
**Resource list:** Arizona free legal aid (`https://www.azlawhelp.org`), state bar referral hotline.
**Footer:** No CTA. Don't push further — pushing here is bad-faith.

### C) Already-represented exit (from Step 5 "Yes, I have an attorney")

**Headline:** You're already represented.
**Body:** Your existing attorney is your best advocate for this case. If you'd like a second opinion, that conversation should start with them — they have the file and the context. We won't take it from here.
**Footer:** No CTA. Close gracefully.

> **Shotton note:** All three exits violate the conventional "always have a CTA" rule on purpose. The behavioral move is honesty — a claimant who senses we're trying to monetize their dead-end will tell two friends to never trust Fair Case. A claimant who experiences a clean, useful redirect tells two friends Fair Case is legit. The brand value of the soft-decline screens is higher than the marginal lead they could generate.

---

## Settlement-estimator multiplier remap

Live `quiz-config.ts:149` — `severityMult: { minor: 0.6, moderate: 1.0, severe: 2.5, life_altering: 5.0 }` — no longer applies after Step 6 rewrite.

**New multiplier model:** based on count and category of injury markers selected.

| Selection pattern | Multiplier |
|---|---|
| "None of these" only | (gate hits — no estimator shown, soft-decline path instead) |
| 1 qualifying marker | 1.5× |
| 2-3 qualifying markers | 2.5× |
| 4+ qualifying markers | 4.0× |
| Spinal cord / paralysis selected | 5.5× (highest priority) |
| Permanent disability selected | 4.5× |

> **Note:** Multipliers replace `severityMult` only. `treatmentMult` (medical_treatment) and `faultMult` (at_fault) stay unchanged in `quiz-config.ts:147-148`.

---

## Implementation diff (handoff to lead-gen)

For the implementation engineer (Alex):

**File:** `lead-gen/apps/lead-gen-frontend/src/lib/quiz-config.ts`

1. Add new constant `INJURY_MARKERS` (multi-select, replaces `INJURY_SEVERITY_OPTIONS` for AZ traffic — flag-gate or variant config)
2. Update `STEPS_ORDER` step name `injury_severity` → `injury_markers`
3. Update `getAffirmation` function with the McCabe-rewritten copy from this doc
4. Update `getSettlementEstimate` — replace `severityMult` lookup with `markersMult` keyed to selection count + special-priority markers
5. Update `INJURY_TYPE_OPTIONS` per Step 1 changes (add bicycle, add wrongful death, replace "other" with "something_else" routing flag)
6. Update `INCIDENT_DATE_OPTIONS` — add `over_2_years` distinct from `over_1_year`
7. Add `buildTcpaConsentText({ advertiserName: "West Coast Trial Lawyers" })` invocation on AZ traffic — currently default advertiser is the platform name
8. New components: three soft-decline screens (A/B/C above)
9. Kill the global "Standard screening questions..." subhead in `AuthoredQuestionnairePage.svelte` and `LegacyQuestionnairePage.svelte`; replace with per-step reassurance microcopy from this doc

---

*All copy in this doc is locked unless Saul flags red on AZ ER 7.1 review (see `03_AZ_COMPLIANCE.md`).*
