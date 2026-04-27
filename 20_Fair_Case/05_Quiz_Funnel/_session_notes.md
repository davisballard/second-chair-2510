# Session Notes — Fair Case Quiz Funnel Brief

**Date:** 2026-04-27
**Convened by:** Nigel Bogle (liaison) on Davis's call
**Chair:** Luke Wroblewski
**Attendees (active):** Luke Wroblewski, Richard Shotton, Ed McCabe, Saul
**Attendees (silent observers):** Julian Cole, Chester Prides, Adam Ferrier
**Format:** Solo expert with advisors

---

## Davis's brief (verbatim opening)

> *"i want you to bring in abracadabra for a brief, we have our quiz funnel for Second Chair and Alex has based it off hundreds of forms but i want to make sure that all the theme design is perfect, both in terms of the questions in the flow to the design and ways to get people to actually fill it out, the social proof in the last section, secondary information below each step if needed to handle objections without overwhelming, Saul on what we need legally."*
>
> *"This is for the form in general but for the questions quiz funnel copy and stuff its specific to the WCTL Arizona non soft tissue campaign those are the edits to make."*
>
> *"Luke is going to be a big part of this."*

---

## Key exchanges

**Luke (Beat 5 clarifying questions, on the gate location):**
> "Davis, where does the soft-tissue exclusion actually filter? Form-level hard gate, form gate plus post-submit human review, or ad-level only?"

**Davis (head of agency):**
> "it has to be at ad level like i have but also at the quiz level too but i need to figure out where that question lies in the flow so they have momentum and are invested in it, but we wont send them leads that are explicitly soft-tissue but sometimes its unclear and we dont want to assume its not soft-tissue and not send it to them but also not send them clear soft-tissue cases."

**Luke (on receiving the brief):**
> "That changes the architecture. We don't need a single hard-gate question. We let *the combination* of three signals do the work — injury type, medical treatment, severity — and we triangulate. Clear soft-tissue is 'Minor severity + No medical treatment + a body-region answer that reads as whiplash-only.' Anything else passes through and Second Chair reviews."

**Luke (on Step 6):**
> "Step 6 as it sits today — 'Minor / Moderate / Severe / Life-Altering' — is broken. Most claimants don't have the medical literacy to self-classify 'Moderate vs Severe.' We're going to rewrite Step 6 as concrete checkbox injury types pulled directly from Section 5.1(d) of the WCTL agreement. That carries the gate logic AND solves the ambiguity simultaneously."

**Luke (on the logo, after Davis asked for a recommendation):**
> "Go Roman Navy wordmark. Charcoal is a neutral, not a brand color. The trust alignment from ad to form depends on the user pattern-matching the same chromatic signal — they saw torch + Roman Navy in the ad creative, they need to see torch + Roman Navy at the top of the quiz within 0.5 seconds or the trust handoff fails. Charcoal would float. Torch alone reads like a favicon, not a brand."

**Saul (on the TCPA consent text in the live quiz):**
> "The current default advertiser name is 'Second Chair through getafaircase.com.' That's wrong for one-to-one consent — Second Chair is the platform, but the consent must name the receiving firm. For Arizona, that's West Coast Trial Lawyers. The TrustedForm video has to show those exact words on the user's screen at the moment they hit Claim. If the certificate shows 'the law firm that serves my ZIP code' without naming WCTL, you just gave a class-action attorney the smoking gun."

**Shotton (on per-step trust badges):**
> "Each step has a distinct anxiety profile. Generic trust badges that rotate without logic are wasted impressions. Step 6 returns to '4.9/5 from 254 verified reviews' — same as Step 1 — and that's actually fine because both are 'is this real?' moments. The other steps need different signals. The current rotation isn't logic, it's just rotation."

**McCabe (on the 'Standard screening questions for the public quiz shell' subhead):**
> "That's placeholder copy. Internal stub that shipped to production. It reads as 'we forgot to write this.' Every screen has it. Kill the global subhead. Replace with question-specific reassurance microcopy keyed to that step's anxiety profile."

**Saul (final traffic-light verdict):**
> "Look, with everything in this doc shipped exactly as written, you're at GREEN. TCPA: green. State bar: green. Platform: green (the form doesn't run as an ad on Meta, so Personal Attributes don't apply here — but the ads driving traffic to the form must still pass that check separately, which is McCabe + my call on the ad creative side, not this doc). The form is bulletproof. Run it."

---

## Decisions made

1. **Folder:** `Abracadabra/08_Brands/Second_Chair/20_Fair_Case/05_Quiz_Funnel/` shell-wide, with `WCTL_AZ/` subfolder for client-specific copy and gate logic.
2. **Gate architecture:** Triangulation across Step 1 (injury type) + Step 3 (medical treatment) + Step 6 (rewritten injury markers checkbox). Three outcomes: deliver / Second Chair human review / soft-block.
3. **Step 6 rewrite:** Replace subjective severity scale with multi-select concrete injury checkboxes pulled verbatim from WCTL agreement Section 5.1(d).
4. **Logo treatment:** Roman Navy wordmark + Torch Amber flame, **non-clickable** (Davis's call), centered, sized below the per-step trust badge in the header stack. This **changes** FORM_DESIGN_BRIEF.md Section 5 which had the logo at top of stack and linking to homepage in new tab.
5. **Per-step subhead:** Kill the "Standard screening questions for the public quiz shell" placeholder. Replace with question-specific reassurance microcopy from McCabe.
6. **Trust badge rotation:** Anxiety-keyed, not random. Spec in `02_TRUST_SYSTEM.md`.
7. **TCPA consent text:** Must explicitly name "West Coast Trial Lawyers" for AZ traffic. Code change to `buildTcpaConsentText` defaults.
8. **Footer disclosure rewrite:** Drop the conditional "if one is identified" — WCTL Arizona is exclusive; the firm IS always identified for AZ ZIPs.
9. **Past-results disclaimer bump:** Live disclaimer is undersized at ~8px. Bump to 13px minimum, `#6B7280`.
10. **AZ ER 7.1 added to rulebook:** `Abracadabra/06_Legal/Rulebook/04_State_Bar_Rules.md` extended with Arizona section. Saul wrote.
11. **Step 1 "Other" replaced** with "Something else" routing to soft-decline + addition of Bicycle Accident and Wrongful Death as named options.
12. **Step 5 "Yes, I already have one"** soft-disqualifies via graceful exit screen (no funnel push-through).
13. **Step 2 "Over 1 year ago"** splits into "within 2 years" (continues) and "more than 2 years" (SOL soft-decline).
14. **Exit-intent popup:** audit, not rebuild. Pending Alex confirming the implementation file path.

---

## What got killed (or de-prioritized)

- **CTA copy redesign:** McCabe tested 25+ alternates against "Claim My Free Evaluation Now." Couldn't beat it. Kept verbatim.
- **Wrongful death sub-flow:** Acknowledged as needed (relationship-to-deceased follow-up question, different gate path) but **out of scope for the WCTL pilot's first 21 leads.** P1 follow-up.
- **Settlement timer / urgency counter:** Saul flagged red. Not added.
- **Spanish translation of consent text:** Out of scope for the pilot. Adds when needed; Saul reviews translation.
- **Stars-and-logo "As featured in" trust signal:** Not a credible signal for a regional pilot. Cut.

---

## Action items pre-launch

| Owner | Action |
|---|---|
| Sasha (Second Chair) | Produce substantiation file at `Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/_Research/wctl_substantiation.md` with backing data for $150M+, 97%, 4.9/5, 254 reviews, three settlement amounts |
| Sasha | Confirm WCTL intake actually runs 24/7 (or change badge to "same-day callback") |
| Alex (lead-gen) | Confirm exit-intent file path so `07_EXIT_INTENT_AUDIT.md` can be completed |
| Alex | Implement `01_QUESTION_COPY.md` changes in `quiz-config.ts` |
| Alex | Build `evaluateWctlAzGate()` per `02_SOFT_TISSUE_GATE.md` |
| Alex | Build three soft-decline screen components (Step 1 "Something else", Step 2 SOL exit, Step 5 already-represented) |
| Alex | Header restructure per `03_BRAND_MARK_AND_LAYOUT.md` (non-clickable wordmark, divider lines, badge placement) |
| Alex | Final-step layout per `05_FINAL_STEP_SOCIAL_PROOF.md` (demote green privacy block, update settlements headline, three trust cards + closing line) |
| Alex | TCPA consent text update — `buildTcpaConsentText({ advertiserName: "West Coast Trial Lawyers" })` for AZ traffic |
| Saul | Final pre-launch traffic-light review once implementation lands |
| Davis | Sign off on full deliverables before merge to production |

---

## Post-session updates (Davis follow-up)

After the room closed, Davis raised three items:

1. **Tofer's quiz will cover ALL injuries** (including soft-tissue), unlike WCTL's non-soft-tissue exclusion. Not building now, but architecturally documented in `00_QUIZ_BRIEF.md` so the shell-wide work is reusable when Tofer's instance is built.

2. **WCTL social proof was undersold by 11x in the live form.** Live "$150M+ recovered" → corrected to **"$1.7 Billion+ recovered"** per `WCTL_Market_Intelligence_Brief.md` line 20. Live generic placeholder settlements table replaced with three real WCTL recoveries (wrongful death $19.4M, truck $3.85M, pedestrian $1.75M) per `WCTL_Market_Intelligence_Brief.md` lines 27-35. Updates landed in `02_TRUST_SYSTEM.md` and `05_FINAL_STEP_SOCIAL_PROOF.md`.

3. **Saul ruled on geo-specificity of settlement amounts:** AZ ER 7.1 does NOT require state-specific case examples. Firm-general settlements (which for WCTL are heavily California-weighted) are compliant when (a) they're actual WCTL recoveries, (b) past-results disclaimer is shown, (c) case facts are reasonably comparable, (d) the firm is authorized to practice in AZ — which WCTL is per Service Agreement Section 11.2. Strategic note: a Phoenix-office recovery in the table would be more persuasive but isn't legally required. Full ruling in `WCTL_AZ/03_AZ_COMPLIANCE.md` Section 5A.

4. **Saul + Hegarty ruled on settlement numbers in Fair Case ads (separate from form):** Layered verdict. State bar = compliant; Meta platform = yellow zone (algorithm flags settlement-dollar creative even when ER 7.1 approves); WCTL brand fit = probable Neama veto (per Market Intel Brief line 53, "settlement promises" are exactly what he's trying to escape); SC creative register = wrong register (Elevated Documentary is empathy-driven, not greed-prime). **Recommendation: NO specific settlement amounts in ads. Aggregate "$1.7B+" is defensible with disclaimer, sparingly, only as a closing card — and only after Robert/Neama greenlight. "97% of qualifying cases reach a settlement or verdict" is the strongest authority signal for ad use.** Specific settlements belong ON the form (post-90-second commitment, evaluation context), not in ads (scroll context). Full ruling in `WCTL_AZ/03_AZ_COMPLIANCE.md` Section 5B.

---

## Files produced (this session)

**Shell-wide briefs (8):**
- `00_QUIZ_BRIEF.md`
- `01_FLOW_AUDIT.md`
- `02_TRUST_SYSTEM.md`
- `03_BRAND_MARK_AND_LAYOUT.md`
- `04_OBJECTION_COPY_FRAMEWORK.md`
- `05_FINAL_STEP_SOCIAL_PROOF.md`
- `06_COMPLIANCE_PACK.md`
- `07_EXIT_INTENT_AUDIT.md`

**WCTL Arizona-specific briefs (3):**
- `WCTL_AZ/01_QUESTION_COPY.md`
- `WCTL_AZ/02_SOFT_TISSUE_GATE.md`
- `WCTL_AZ/03_AZ_COMPLIANCE.md`

**Rulebook addition:**
- `Abracadabra/06_Legal/Rulebook/04_State_Bar_Rules.md` — new Arizona section (Section 5A)

---

## Memory: lead-gen path correction noted

Auto-memory said the SC website lives at `lead-gen/apps/second-chair-website/`. Live quiz code is at `lead-gen/apps/lead-gen-frontend/`. Memory updated.

---

## Nigel's close

> **Nigel:** Decisions: solo-expert format with Luke chairing was the right call. Triangulation gate is the win — saves us from a dumb single-question hard-gate that was always going to leak qualified claimants alongside the soft-tissue ones. Saul's at GREEN pending Sasha's substantiation file. Eleven docs in folder, one rulebook addition, one memory correction. Davis approved the brief at the end of plan mode. Implementation hands to Alex. I'll re-convene the room if anything red comes up at QA.

---

*Session log curated to key exchanges, decisions, kill list, and action items. Full discussion lived in chat.*
