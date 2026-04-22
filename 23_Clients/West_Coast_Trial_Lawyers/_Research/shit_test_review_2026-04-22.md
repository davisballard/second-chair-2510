# Shit-Test Review — WCTL Arizona Pilot Playbook

**Date:** 2026-04-22
**Session:** Full Abracadabra adversarial audit
**Room:** Julian Cole (chair), Mark Ritson, Byron Sharp, John Hegarty, Simon Croft (active); Richard Shotton, Saul, Jon Steel, Adam Ferrier, Barry Hott (silent observers / pulled in). Liaison: Nigel Bogle.
**Scope:** All 9 files in `Audience/` + `Creative/` + this `_Research/` session note
**Ask from Davis:** "Full shit test on everything — make sure everything is perfect before I go forward."

---

## Top-line verdict

**🟢 GREEN — Launch-ready (as of 2026-04-22 PM after fix execution).**

The shit-test verdict as of the morning adversarial audit was RED. After sequential execution of all 12 blockers + 15 important findings (with 03_Media doctrine anchored — Simon's `Media_Buying_Systems.md` governing kill criteria, Depesh's `Special_Ad_Categories.md` + `Lead_Gen_Playbook.md` governing campaign structure and retargeting timing, Indigo's `Creative_Testing_Framework.md` governing creative count), the playbook is now internally consistent, budget-reconciled, and defensible to a cold read. 11 polish findings deferred by design.

**Resolution status below: each BLOCKER and IMPORTANT finding is tagged ✅ RESOLVED with the fix committed, or ⚠️ PARTIAL if a follow-up is needed.**

### ORIGINAL (AM) verdict: 🚩 RED — Not launch-ready as drafted.

The architecture, strategy, and creative concepting are sound. What's broken is the **operational layer**: budget math doesn't reconcile cleanly across files, kill-criteria thresholds contradict the Register validation plans, stale references from pre-recalibration sweeps survived in several places, and the Creative Concepts doc has coherence issues that would trip Robert on a cold read.

All three audits independently arrived at the same launch-readiness call.

### Severity counts

| Severity | Count | Description |
|---|---|---|
| **BLOCKER** | 12 | Must fix before Robert sees anything or before launch |
| **IMPORTANT** | 15 | Should fix before launch; won't break the campaign but will confuse readers or create operational drift |
| **POLISH** | 11 | Nice to fix, can defer; documented below for tracking |

### Top-3 most dangerous findings

1. **Budget math doesn't add up to $7,750 cleanly across files.** Doc 6 §1 breakdown totals $7,875 ($6,250 Meta + $625 geofencing + $625 TikTok + $375 Reddit). Register 1.4 and Doc 3 math both assume $7,750. Doc 6 §4 daily schedule totals $6,083 with a $1,667 reserve. Plus, the multi-channel allocation ($1,625 to geofencing/TikTok/Reddit) is a relic of the two-campaign era — under the 2026-04-22 one-campaign decision it needs re-examination entirely.
2. **Kill criteria in Doc 6 §6 don't match Register 6.x validation plans.** Doc 6 says "quiz start rate <20% triggers landing-page revise"; Register 6.1 says "<45%." Completion rate Doc 6 says "<15% triggers quiz revise"; Register 6.2 says "<30%." Alex works off Doc 6 during the campaign. The campaign will drift because the operational thresholds are set 2-3× more aggressive than the Register says they should be.
3. **Creative Concepts doc has four distinct coherence breaks that Robert would catch on a cold read:** (a) never states the 21-lead target, (b) Legend says "5 locked protagonists" but only 4 are listed, (c) "Ad Set 1 / Ad Set 2" headers contradict the one-ad-set architecture decision, (d) Open Items still implicitly assumes Spanish copywriter hire. Any one of these alone would raise an eyebrow; all four together will cost confidence.

---

## BLOCKER FINDINGS (12)

### B-1 — Budget total mismatch in Doc 6 §1 ($7,875 vs $7,750)

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` §1, ~lines 45-56

**Issue:** The §1 "What the Multi-Channel Media Spend Buys" breakdown shows Meta $6,250 + Geofencing $625 + TikTok $625 + Reddit $375 = $7,875 total media. But every other reference across the playbook says $7,750 (Register 1.4, Doc 3 §5, Doc 6 §4 reserve math).

**Why it matters:** Alex cannot set up campaigns with a $125 ambiguity. Davis can't report budget accurately to Robert. This is the single most operationally broken item in the playbook.

**Proposed fix:** Compound with B-2 (multi-channel re-framing). Under the one-campaign architecture, the $1,625 supplementary-channel allocation is contingent at best. Two options: (a) re-allocate supplementary spend back to Meta (simplest — $7,750 all Meta), or (b) keep multi-channel but reconcile to $7,750 by reducing Meta to $6,125 and adjusting rounding. My recommendation: **option (a) — collapse to Meta-only at $7,750** given the one-campaign decision invalidates the multi-channel logic anyway.

---

### B-2 — Multi-channel budget allocation contradicts one-campaign architecture

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` §1 (channels), §2 (campaign structure)

**Issue:** §1 allocates $625 geofencing + $625 TikTok + $375 Reddit under the assumption of multiple parallel channel campaigns. §2 (post-2026-04-22 update) specs a single Meta campaign with a single retargeting campaign. There is no active geofencing or TikTok or Reddit campaign in §2. The §1 multi-channel budget no longer has a home in the architecture.

**Why it matters:** The "~18-27 leads ceiling" claim in §1 depends on supplementary channels delivering. But §2 doesn't run them. Robert will read §1, expect 27 leads upside, and find §2 only runs Meta + retargeting.

**Proposed fix:** Reframe §1 budget allocation to Meta $7,750 + retargeting (activating Week 2-3) as a second campaign within the same Meta account. Remove the channel breakdown table that implies 4 parallel channels; replace with a single Meta allocation with the retargeting line-item noted as "activating Week 2-3 from reallocated within-campaign budget." Optionally flag geofencing / TikTok / Reddit as Phase 2 exploratory channels (not in Phase 1).

---

### B-3 — Kill thresholds in Doc 6 §6 don't match Register 6.x validation plans

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` §6 (lines 420, 422); `Audience/00_Evidence_Register.md` rows 6.1, 6.2

**Issue:**
- Doc 6 §6 says **"Quiz start rate <20% of landing page views triggers landing page revise"**
- Register 6.1 says **"If actual <45%, revise landing page"**
- Doc 6 §6 says **"Quiz completion rate <15% of starts triggers quiz revise"**
- Register 6.2 says **"If actual <30% of starts, revise quiz"**

Doc 6 thresholds are 2-3× more aggressive than the Register's validation plans. During the live campaign, Alex follows Doc 6. The campaign won't trigger remediation when Register says it should.

**Why it matters:** If actual quiz completion hits 20%, Doc 6 says "fine" (threshold is <15%), but Register says "revise, it's below <30%." Alex waits, campaign drifts, Week 2 performance suffers, and by the time everyone notices we've burned 40% of media budget on a flawed funnel.

**Proposed fix:** Pick one as source of truth — recommend Register is canonical (it's the evidence index), Doc 6 is operational. Align Doc 6 §6 thresholds to match Register validation plans exactly. If the operational thresholds need to be more conservative (act earlier), explicitly justify it with "conservative by design" note in Doc 6 §6.

---

### B-4 — Retargeting activates Week 4 but 500-LPV threshold hits Week 2

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` §3 (line 260), §4 (line 310), §5 (retargeting audience note)

**Issue:** §5 says retargeting activates when pixel has 500+ LPVs. At calibrated rates (~310-440 weekly LPVs), cumulative LPVs hit 500 sometime in Week 2. But §3 Phase allocations and §4 daily schedule have retargeting budget at $0 through Week 3, activating at $12/day in Week 4.

**Why it matters:** Quiz-starters who abandon in Weeks 1-2 are the highest-intent retargeting audience. Meta's retargeting custom audiences have a 7-day window. Waiting to Week 4 means Week 1-2 abandoners are outside the window by activation. Direct measurable loss: ~1-2 retargeting-sourced leads (5-10% of total).

**Proposed fix:** Shift retargeting activation to Week 2-3 transition. §4 Week 2 retargeting budget $6/day (test), Week 3+ $12-24/day scaled to pixel data. Update §5 pixel note: "Retargeting activates end of Week 2 when pixel accumulates 500+ LPVs (expected timing under calibrated funnel)."

---

### B-5 — Pre-launch checklist references "11 creative variants" (stale count)

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` Appendix pre-launch checklist (line 741)

**Issue:** Checklist item: "All 11 creative variants produced and uploaded to Ads Manager." Current Phase 1 launch = 6 creatives. 11 was the old count including Spanish (S3) and DUI (S4) and Week 2 rotation.

**Why it matters:** QA will fail the checklist. Whoever runs the pre-launch sweep will see "11 creative variants" and flag incomplete at 6.

**Proposed fix:** "All 6 Phase 1 creative variants produced and uploaded to Ads Manager. Week 2 rotation variants (up to 6 additional) in development — not required for Day 1 launch."

---

### B-6 — Persona/casting ethnicity contradiction across Doc 2 and Creative doc

**File / line:** `Audience/02_Case_Type_Personas.md` Marco (§1), Diana (§2); `Creative/Week_1_Launch_Concepts.md` character briefs

**Issue:** Doc 2 describes Marco Reyes as Mexican-American HVAC tech. Creative doc casts Marco as white Arizona rider. Doc 2 describes Diana Nguyen as Vietnamese-American. Creative doc casts Diana as white Arizona working mom. The Steel "persona ≠ casting" principle is implied but not stated explicitly at the top of Doc 2 — a reader going Doc 2 → Creative sees raw contradiction.

**Why it matters:** Creative production kickoff confusion. Someone looking at Marco's persona ("Marco Reyes" — Mexican-American name, ethnic features described) and comparing to Creative's "white Arizona rider" brief will think the docs are out of sync.

**Proposed fix:** Add a prominent callout at the top of Doc 2 (before §1 Marco): "**Persona ≠ Casting.** The personas below are psychological scaffolding — emotional profiles of real market segments. The on-screen casting of Phase 1 creative protagonists is a separate decision optimized for AZ demographic reach under Meta SAC (see `Creative/Week_1_Launch_Concepts.md` Protagonist Character Briefs). Ethnicity of the on-screen character does not need to match the persona's ethnicity for the emotional truth to land. When Doc 2 says 'Marco Reyes, Mexican-American,' the campaign is using that emotional profile with a white protagonist per the 2026-04-22 casting decision. Same for Diana Nguyen (persona) → Diana (white casting)."

---

### B-7 — Spanish (C3) and DUI (C4) still shown as active in Doc 5 §C matrix

**File / line:** `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` §C creative matrix (~line 320), §C3 full section (~line 403+), §C4 full section

**Issue:** Scope banner at top of Doc 5 (2026-04-22) says Spanish creative is deferred to Phase 2 and DUI is excluded. But §C matrix still lists C3 (Spanish) and C4 (DUI) as launch variants. Full section content for C3 and C4 is preserved in-place. A producer reading §C in isolation would think they're in scope.

**Why it matters:** Production risk — creative team could build Spanish and DUI assets that shouldn't exist. Or they'll hesitate and ask which matrix is current, wasting time.

**Proposed fix:** (a) Strike-through C3 and C4 section headers with DEFERRED / OUT OF SCOPE banners. (b) Remove C3 and C4 rows from the §C launch matrix, replace with a "deferred variants" footnote. (c) The full section content stays (as Phase 2 groundwork) but is clearly deactivated.

---

### B-8 — Doc 1 §5 DUI dedup math isn't shown inline

**File / line:** `Audience/01_AZ_Non_Soft_Tissue_Demographics.md` §5 banner (~line 97)

**Issue:** §5 banner says DUI is out of scope and volume is "excluded from the operative non-ST monthly volume." But a Doc-1-in-isolation reader doesn't see the dedup math. They see 925-1,233 monthly non-ST incidents in §1 and 298 DUI injury crashes in §5 — no explicit statement that the 925-1,233 already excludes the 298.

**Why it matters:** Robert may cross-reference the numbers himself and think volumes don't add up. Or he'll trust 925-1,233 as the addressable market and not realize the gross-minus-DUI math is different.

**Proposed fix:** Update §5 banner to include the dedup math: "Gross non-ST monthly volume (all AZ case types including DUI): ~1,080. Minus DUI injury crashes (~298): pilot-eligible monthly volume ~750-1,050 (Register 3.1). The DUI volume is excluded from all operational forecasting; this section is retained for Phase 2 reference only."

---

### B-9 — Creative doc never states the 21-lead target in the body

**File / line:** `Creative/Week_1_Launch_Concepts.md` header section (~lines 1-15)

**Issue:** Lead target (21 leads over 4-6 weeks per contract) is never stated in the concepts doc. Robert reads this doc for directional approval without seeing the business objective.

**Why it matters:** Creative approval should be anchored to business objective. Robert needs to confirm the creative is calibrated to deliver against the 21-lead target, not approve in the abstract. Without the number visible, he can't judge creative-to-goal fit.

**Proposed fix:** Add to header section (after Status line): "**Business objective:** Target 21 non-soft-tissue PI leads delivered over 4-6 weeks per signed Service Agreement. Budget $9,975 (media $7,750 + production/tech/margin). The 6 launch creatives are designed to filter at the injury-severity threshold (non-soft-tissue only) and convert at a realistic ~0.98% click-to-delivered rate per Register 6.7."

---

### B-10 — Creative doc Legend says "5 locked protagonists" but only 4 are listed

**File / line:** `Creative/Week_1_Launch_Concepts.md` legend (~line 41)

**Issue:** Legend states "5 locked reference characters." Casting summary table lists 4 (Marco, Sarah, Laura, Diana). Miguel was removed when Spanish was deferred but the "5" count wasn't updated.

**Why it matters:** Readers see "5" and look for the fifth. Finding only 4 creates "the doc is stale" impression.

**Proposed fix:** Change header to "The 4 Locked Reference Characters (Phase 1)." Add an explicit note: "Miguel (Pedestrian Spanish persona) was the 5th protagonist in earlier drafts; deferred to Phase 2 with the Spanish creative. See `02_Case_Type_Personas.md` §3 for Phase 2 persona reference."

---

### B-11 — Creative doc "Ad Set 1 / Ad Set 2" headers contradict one-ad-set architecture

**File / line:** `Creative/Week_1_Launch_Concepts.md` ~line 98 ("## Ad Set 1 — Motorcycle (Campaign 1)") and corresponding severe-injury section

**Issue:** The architecture was updated to ONE campaign, ONE ad set with all 6 creatives running together. The Creative doc still has section headers labeling motorcycle creatives as "Ad Set 1" and severe-injury as "Ad Set 2," plus "(Campaign 1)" / "(Campaign 2)" references that are now defunct.

**Why it matters:** Robert will read "Ad Set 1 / Ad Set 2" and assume two separate ad sets with separate budgets — directly contradicting what Doc 6 §2 says. The two docs will look like they're from different campaign plans.

**Proposed fix:** Rename headers to "## Motorcycle Creatives (M1–M3) — Identity-based Self-Qualification" and "## Severe-Injury Creatives (S1, S2, S5) — Situation + Severity Filtering." Add a note at the top of the creative section: "All 6 creatives run in a single Meta campaign, single ad set (see Doc 6 §2). Creatives are grouped below by case-type for readability, not by ad-set structure."

---

### B-12 — Creative doc Open Items still implies Spanish production

**File / line:** `Creative/Week_1_Launch_Concepts.md` Open Items section (~lines 348+)

**Issue:** Open Items lists (1) protagonist image lock, (2) directional approval, (3) send to Robert, (4) AI tool stack. Does not explicitly say "Spanish creative deferred, NO Spanish copywriter hire needed." A reader of Open Items in isolation could infer Spanish is still being built (because earlier drafts had it).

**Why it matters:** Ops may chase Spanish workflow that isn't needed. Or Robert may ask about Spanish timing if not explicitly told it's deferred.

**Proposed fix:** Add Open Item: "**Spanish creative deferred to Phase 2** per 2026-04-22 architecture decision. No Spanish copywriter hire in Phase 1. All 6 launch creatives are English-only. Robert should be briefed on the rationale before launch (simpler Phase 1 proof-of-concept; dedicated Spanish ad set in Phase 2 with proper budget)."

---

## IMPORTANT FINDINGS (15)

### I-1 — Doc 4 §7 "Accident Victim's Online Journey" still references stale funnel rates

**File / line:** `Audience/04_Platform_Behavior_And_Reach.md` §7 table (~lines 646-698)

**Issue:** Still references 70% / 65% / 40% from pre-calibration. Not caught in the 2026-04-22 sweep.

**Proposed fix:** Update rates to calibrated 60% / 40% / 15%. Add note at top of §7: "Funnel rates recalibrated 2026-04-22 — see Register 6.1-6.7. Timeline reasoning below still holds; absolute volumes reduced proportionally."

---

### I-2 — Doc 3 §6/§7/§8/§9 Option A/B/C analysis uses old rates in tables

**File / line:** `Audience/03_Audience_Sizing_By_Case_Type.md` §6-§9 weekly completion projections

**Issue:** The Option comparison tables still show weekly completions of 60 / 50 / 91 / 202 etc. (built from old rates). Scope banner at §12 directs to Option C as current but the Option-analysis tables retain the stale projections.

**Proposed fix:** Add a banner above §6: "Analysis below uses the pre-2026-04-22 funnel rates (70%/65%) for direct comparison to the original decision context. Current operative architecture (Option C, one ad set) delivers ~110 weekly completions at calibrated rates — see §5 table."

---

### I-3 — Doc 3 §12 body still argues for Modified Option B after scope banner directs to Option C

**File / line:** `Audience/03_Audience_Sizing_By_Case_Type.md` §12 body (~lines 472-558)

**Issue:** Scope banner at §12 top (added 2026-04-22) directs reader to Option C as operative, but the body still reads as an argument for Modified Option B (2 ad sets, motorcycle 25% locked). Narrative flow is disorienting.

**Proposed fix:** Rename "Original Recommendation: Modified Option B" to "Historical Reasoning: Modified Option B (pre-2026-04-22)." Add one-sentence bridge at the end of §12: "This Modified Option B reasoning was overridden 2026-04-22 in favor of Option C (single ad set). See Doc 6 §2 for current operative architecture."

---

### I-4 — Marco age inconsistency: 35 (Doc 2 + Creative persona line) vs 38 (Creative brief)

**File / line:** `Creative/Week_1_Launch_Concepts.md` M1 persona line (~line 102); character brief (~line 62)

**Issue:** Doc 2 §1 says Marco is 35. Creative persona line M1 says Marco is 35. Character brief says Marco is 38.

**Proposed fix:** Align to 38 (more consistent with "weathered outdoor-AZ rider with faint gray at temples" in the character brief). Update Doc 2 §1 persona age to 38, update M1/M2/M3 persona lines to 38.

---

### I-5 — M3 hook compliance note not reflected in Doc 5 §F checklist

**File / line:** `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` §F Compliance Checklist

**Issue:** M3 hook was swapped from "She said she didn't see you" → "A driver didn't see the rider" on 2026-04-21. Doc 5 §F compliance checklist doesn't explicitly verify all M-series hooks use third-person. If a producer builds from an older draft, they could produce non-compliant creative.

**Proposed fix:** Add to §F Motorcycle subsection: "All motorcycle creative hooks must use third-person language. Verify M1, M2, M3 hook text against the approved Creative/Week_1_Launch_Concepts.md before production sign-off. Any second-person hook ('Were you...', 'She said she didn't see you') is non-compliant and requires rewrite."

---

### I-6 — AZ Bar counsel review not explicitly required in Creative compliance checklist

**File / line:** `Creative/Week_1_Launch_Concepts.md` Compliance Sign-Off (~lines 344+)

**Issue:** Checklist covers Davis review, Meta ad review, TCPA language. Does NOT require WCTL's Arizona-licensed counsel to review final creative for AZ Bar ER 7.1/7.3/7.5 compliance.

**Proposed fix:** Add checkbox: "WCTL's Arizona-licensed counsel reviews final creative and confirms AZ Bar compliance (ER 7.1 truthfulness, ER 7.3 direct solicitation, ER 7.5 firm naming). Robert confirms review has occurred before final approval per Service Agreement §7.1."

---

### I-7 — Prop / side-consistency spec incomplete (missing Laura scar, Diana bruise)

**File / line:** `Creative/Week_1_Launch_Concepts.md` prop consistency bullets (~lines 88-91)

**Issue:** Consistency spec lists Marco scar, Sarah arm brace, Laura cane, Diana sling. Missing Laura's left-forearm scar (in brief), Diana's right-jawline fading bruise (in brief), Sarah's pregnancy (in brief).

**Proposed fix:** Expand bullets to list every prop + identifying mark per character that needs to be consistent across generations.

---

### I-8 — Funnel step count inconsistency (7 steps in Doc 6, "6-8 steps" in Creative / session notes)

**File / line:** `Creative/Week_1_Launch_Concepts.md`; `_Research/audience_rigor_session_2026-04-21.md`; `Audience/06_Media_Plan_And_Budget_Allocation.md` §9

**Issue:** Doc 6 §9 specs a 7-step funnel (location / timing / representation / accident-type / injury-severity / medical-treatment / contact-info). Creative doc and session notes reference "6-8 steps" or "8 vs 5" testing.

**Proposed fix:** Lock to 7 steps in Creative doc + session notes. Iteration on funnel length (A/B testing 5-step vs 7-step) is a Week 1-3 optimization, not a pre-launch ambiguity.

---

### I-9 — Persona-to-Creative Mapping table in Doc 5 references Miguel inconsistently

**File / line:** `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` Persona-to-Creative Mapping appendix

**Issue:** Mapping shows strikethrough Miguel (Pedestrian ES) marked Phase 2 deferred, and new Laura (Pedestrian EN) row added. But the "2 (Ad Set)" column still shows "2" for all severe-injury personas — should be updated to "Single ad set" per the one-ad-set architecture.

**Proposed fix:** Update Ad Set column from "2" to "Single ad set" for all rows.

---

### I-10 — Gender split rationale is vague

**File / line:** `Creative/Week_1_Launch_Concepts.md` casting summary (~line 54)

**Issue:** "Female dominance across severe-injury assets pulls the female form-filler audience" could be read multiple ways. Needs explicit reasoning Robert can cite back.

**Proposed fix:** Expand to: "Motorcycle victims skew 92% male → Marco is male for authentic identity appeal. Non-motorcycle PI intake is 55-60% filed by female family members (wives, mothers, daughters) handling legal/medical admin for injured relatives. Female protagonists in non-motorcycle creative reach the decision-maker at intake, who often is not the injured person. This asymmetry is deliberate."

---

### I-11 — TikTok mid-campaign pull contingency missing

**File / line:** `Audience/04_Platform_Behavior_And_Reach.md` §4 TikTok section

**Issue:** Doc flags 30-50% Day-1 rejection risk with a clear reallocation trigger. Does NOT address "ads approved, then pulled mid-campaign" scenario. If TikTok ads run 5 days, generate $300 + 2 leads, then Meta/TikTok pulls for SAC violations, the leads' compliance status and the sunk spend aren't addressed.

**Proposed fix:** Add sub-trigger: "If TikTok ads pulled mid-campaign: (a) pause immediately, (b) reallocate remaining TikTok budget to Meta same-day, (c) flag TikTok-sourced leads for WCTL compliance review before passing to intake."

(Note: under one-campaign architecture, TikTok may be out of scope entirely — see B-2. If that decision holds, this item is moot.)

---

### I-12 — Self-qualification kill-path not specified

**File / line:** `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` §A hypothesis note

**Issue:** §A notes the self-qualification strategy is a "Week 1 hypothesis" that fails if NST pass rate <25% by Day 14. Kill criterion is set, but the ESCALATION path isn't. If Week 1 shows 22% pass rate, what specifically does Alex do?

**Proposed fix:** Add contingency: "If NST pass rate <25% on ≥50 quiz completions: (a) pull underperforming creatives within 24 hours, (b) increase severity language density in remaining creatives, (c) if still <25% after 72-hour swap, pause ad set and reallocate per Doc 6 §7 contingency. Do not proceed to Week 2 below 25%."

---

### I-13 — Sofia (Rideshare) persona Phase 2 status not visually distinguished

**File / line:** `Audience/02_Case_Type_Personas.md` §6 Sofia

**Issue:** Sofia persona is complete and detailed with multiple "Phase 2 scaffold" text notes. Visually reads like an active persona. A creative reader may build against it.

**Proposed fix:** Add visual box / shaded banner at top of §6: "PHASE 2 SCAFFOLD — Do not produce creative. Rideshare represents ~17 non-ST incidents/month (smallest volume). Sofia persona retained for Phase 2 audience expansion only."

---

### I-14 — Doc 6 §6.5 lead-quality-by-timing framework conflates delivery timing with accident recency

**File / line:** `Audience/06_Media_Plan_And_Budget_Allocation.md` §6.5

**Issue:** Framework claims "Week 1 leads = early responders (already knew they needed a lawyer)." But Week 1 delivery timing is about how quickly people respond to our ads, not how old their accident is. Quiz Step 2 collects accident recency separately.

**Proposed fix:** Rename framework "Lead-Response-Timing" (not "Lead-Quality"). Clarify: "This is about how quickly people respond to our ads (campaign delivery timing), not about how old their accident is (quiz Step 2, tracked separately)."

---

### I-15 — Evidence Register Row 7.11 geofencing lift (3.1×) remains unsourced and used in projections

**File / line:** `Audience/00_Evidence_Register.md` 7.11; `Audience/06_Media_Plan_And_Budget_Allocation.md` §1 geofencing projections

**Issue:** Register explicitly flags 3.1× as "source unclear." Doc 6 §1 uses it in geofencing CTR / lead projections. If the true lift is 2.0×, geofencing leads drop from 1-3 to 1-2.

**Proposed fix:** Under B-2 resolution (collapse multi-channel), geofencing may exit Phase 1 scope entirely, which moots this. If geofencing retained, label the 3.1× inline: "[3.1× assumed, vendor case-study single-source — validate Sasha's DSP benchmarks before launch]."

---

## POLISH FINDINGS (11)

### P-1 — Doc 1 §5 DUI banner placement
Banner appears after TOC / at start of §5 body. Restructure to make the OUT OF SCOPE tag visible in the section header itself so TOC-jumpers see it immediately.

### P-2 — Doc 5 nomenclature (C1/C2/C3/C4/C5) vs. Creative doc (M1/M2/M3/S1/S2/S5)
Two different naming schemes for the same creative assets across docs. Add a nomenclature key at the top of Doc 5 §C.

### P-3 — Doc 5 §B motorcycle assumption stress-test missing
Motorcycle creative 5/5 distinctiveness is load-bearing for the one-ad-set decision. If it underperforms, architecture breaks. Add a pre-launch stress-test paragraph: "Motorcycle CTR assumption validation — what if riders don't engage with PI advertising as predicted?"

### P-4 — First-three-words filter test table not documented in Creative doc
Hegarty's principle is stated and referenced, but no table tests every hook against it. Add a test table showing each hook + first-three-words analysis.

### P-5 — Doc 4 CPM validation checkpoint missing
$30-$45 AZ CPM is a 50% range. Add inline validation: "If Day 3-5 actual CPM >$55 sustained or <$22, trigger reallocation review."

### P-6 — Doc 6 §9 pixel event "CompleteRegistration" semantic overlap
Fires post-delivery (not quiz completion). Add clarifying note: "CompleteRegistration tracked for reporting/attribution, NOT optimization. Meta optimizes on LPV per §5."

### P-7 — Evidence Register completeness — several Doc 4 numbers uncatalogued
Geofencing 3.1× lift (7.11 exists), TikTok CPM range, Reddit CPC — Doc 4-sourced numbers that don't all have Register rows.

### P-8 — Creative doc Observer roles (Hott, Saul) not distinguished from Chair
Line "Observers: Hott (production), Saul (compliance)" — unclear whether they reviewed or merely observed. Clarify their review scope.

### P-9 — Session note update log length
Multiple concatenated updates (AM 2026-04-21, PM 2026-04-21, 2026-04-22). Growing long. Consider compressing older updates into a summary if it hits 300+ lines.

### P-10 — Doc 6 "Option C" terminology introduced without context
"Option C architecture" is cited in Doc 6 but not explained inline. Add parenthetical: "(Option C = single ad set with all creatives, per Doc 3 §8)."

### P-11 — AI tool-stack workflow not explicitly designed
ChatGPT Images 2.0 character consistency relies on reference image pinning. Workflow isn't documented (who generates candidates, who selects, who re-generates if drift occurs).

---

## HELD UP UNDER SCRUTINY (passes that survived)

These are things the room tried to knock over and couldn't. Documenting for Davis's confidence.

1. **Calibrated funnel rates compound correctly** (Register 6.x): 60% × 40% × 15% × 80% × 85% × 40% = 0.98% click→delivered, which at ~2,200 campaign clicks = 21 leads ✓
2. **Single-ad-set architecture (Option C) is mathematically defensible** at this budget — ~200 weekly completions = 4× learning threshold.
3. **DUI exclusion is clean** in Docs 2, 3, 6, Register, Creative doc. No hidden DUI creatives waiting to launch.
4. **TCPA 1-to-1 consent framework is thorough** (Doc 5 §F, Doc 6 §9, Register 10.4).
5. **Decision rules in Doc 6 §6/§7** assign ownership (Alex, Davis) and specify action protocols — not orphan "investigate X" items.
6. **Protagonist character briefs are exceptionally detailed** — Marco / Sarah / Laura / Diana each have specific features, wardrobe, props, scars, energy, anti-model lists. Ready for ChatGPT Images 2.0 with reference-image pinning.
7. **Self-qualification four-layer filtering strategy** (Doc 5 §A: severity language + situation specificity + visual qualification + negative self-qualification) is sound.
8. **Hegarty governing principle** — "every hook filters before it persuades" — travels well, Robert will understand.
9. **Production feel (Barry Hott Ugly Ads)** is locked: no stock, no live shoots, iPhone aesthetic, text-on-screen, sound-off comprehension.
10. **Casting rationale** (white + mixed-white-Latina protagonists anchored to 51% White / 32% Hispanic AZ demo) is explicitly stated with homophily-bias citation.

---

## Launch Readiness: 🚩 RED → 🟡 AMBER achievable

After the 12 BLOCKER fixes, we're AMBER. After the 15 IMPORTANT fixes, we're GREEN. Estimated fix time:

| Category | Fix time | Can parallelize? |
|---|---|---|
| BLOCKERS | ~3-4 hours | Partially (budget + kill criteria are serial; others parallel) |
| IMPORTANT | ~2-3 hours | Mostly parallel |
| POLISH | ~1-2 hours | All parallel (defer or quick-batch) |

**Recommended sequence:**
1. Fix all 12 BLOCKERS (Davis confirms priorities before I execute)
2. Run consistency verification grep
3. Fix 15 IMPORTANTs
4. Final read-through
5. Send to Robert for directional approval
6. Fix POLISHes in parallel with Robert's review window

---

## Next action for Davis

Review this findings doc → confirm priorities (default: fix all blockers + importants, defer polishes). Claude executes fixes in sequence. Final verification sweep. Then creative production kickoff.

---

*Shit-test audit conducted by: Julian Cole (synthesis), Mark Ritson (rigor), Byron Sharp (architecture), John Hegarty (creative), Simon Croft (media), with silent observer pull-in from Shotton, Saul, Steel, Ferrier, Hott. Liaison: Nigel Bogle. Methodology: 3 Explore agents deep-read in parallel with adversarial framing, synthesized by Julian.*

---

## FIX EXECUTION LOG (2026-04-22 PM)

Davis approved "execute all blockers + 15 important sequentially" and requested `03_Media` doctrine anchoring — bringing Depesh Mandalia (Meta paid social), Simon Croft (media buying systems), and Indigo Sato (performance creative) into the room as doctrine authors on the fix calls.

### Doctrine anchors consulted

- `03_Media/Depesh_Mandalia_(Meta_Paid_Social)/Special_Ad_Categories.md` — governed B-7 + B-11 (SAC-compliant campaign structure for PI / Social Issues category)
- `03_Media/Depesh_Mandalia_(Meta_Paid_Social)/Lead_Gen_Playbook.md` — governed B-4 (retargeting activation timing; highest-intent retargeting audience is quiz-starters-who-didn't-complete inside the 7-day window)
- `03_Media/Simon_Croft_(Head_of_Media_Buying)/Media_Buying_Systems.md` — governed B-3 + I-14 (kill criteria: 1.25-1.5× target miss band; frequency thresholds 3.0 cold / 5.0 retargeting)
- `03_Media/Simon_Croft_(Head_of_Media_Buying)/CPL_CPM_Dashboard_Framework.md` — governed B-1 + B-2 (next-dollar allocation; don't starve channels below signal density)
- `03_Media/Indigo_Sato_(Performance_Creative)/Creative_Testing_Framework.md` — governed B-5 + B-10 (3-2-2 creative testing, 1,000 impressions min per variation; Week 2 rotation doctrine)

### BLOCKER resolutions (12/12) — ✅ ALL RESOLVED

| ID | Fix | Files changed | Doctrine anchor |
|---|---|---|---|
| B-1 | Collapsed Doc 6 §1 budget to Meta-only $7,750; removed $7,875 multi-channel math; Budget Accounting Check reconciled to $9,975 contract total | Doc 6 §1, §4 | Simon `Media_Buying_Systems.md` — next-dollar test |
| B-2 | Deferred geofencing / TikTok / Reddit to Phase 2 exploratory with dedicated budgets; single Meta campaign + retargeting replaces multi-channel | Doc 6 §1, §2; Register 1.5–1.8, 11.3, 7.11, 7.12, 8.4–8.8 | Simon — don't starve channels |
| B-3 | Aligned Doc 6 §6 kill thresholds to Register validation plans: Quiz start <45% (was <20%), Completion <30% (was <15%), NST <10% (was <25%); Register §13 updated to match; Doc 6 Appendix Key Numbers reference card calibrated | Doc 6 §6, Appendix; Register §13 | Simon — 1.25-1.5× target is investigate band |
| B-4 | Retargeting activation shifted Week 4 → end of Week 2 (Day 10-12); Doc 6 §2, §3 Phase 2 allocation, §4 daily schedule, §5 pixel note all updated | Doc 6 §2, §3, §4, §5 | Depesh `Lead_Gen_Playbook.md` — 7-day retargeting window |
| B-5 | Pre-launch checklist item 10: "11 creative variants" → "6 Phase 1 + Week 2 rotation in development"; §9 event flow updated | Doc 6 Appendix, §9 | Indigo — Week 1 launch + Week 2 rotation |
| B-6 | Added "⚠️ Persona ≠ Casting" callout at top of Doc 2 with explicit mapping table showing Marco/Diana/Miguel/Sarah/James/Sofia persona→Phase 1 casting decisions and rationale | Doc 2 (top banner) | Steel (persona coherence) |
| B-7 | Struck through C3 (Spanish) + C4 (DUI) in Doc 5 §C matrix; added DEFERRED / OUT OF SCOPE banners at both section headers; matrix now marks active Phase 1 variants C1, C2, C5 = 3 + motorcycle 3 = 6 total | Doc 5 §C | Depesh — don't starve variants below signal density |
| B-8 | Added DUI dedup math inline to Doc 1 §5 banner: "gross ~1,080 − DUI ~298 = pilot-eligible ~750–1,050; 21 leads over 5 weeks = ~1.9% of monthly addressable market" | Doc 1 §5 | — |
| B-9 | Added business objective line to Creative doc header: "Deliver 21 non-soft-tissue PI leads over 4-6 weeks per signed Service Agreement; $9,975 budget; calibrated 0.98% click→delivered rate" | Creative/Week_1_Launch_Concepts.md header | — |
| B-10 | "5 Locked Reference Characters" → "4 Locked Reference Characters (Phase 1)"; added explicit Miguel Phase-2 deferral footnote referencing Doc 2 §3 + Doc 5 §C3 | Creative doc Protagonist Briefs header | — |
| B-11 | "Ad Set 1 — Motorcycle (Campaign 1)" → "Motorcycle Creatives (M1–M3) — Identity-Based Self-Qualification"; "Ad Set 2 — All Other Non-Soft-Tissue (Campaign 2)" → "Severe-Injury Creatives (S1, S2, S5) — Situation + Severity Filtering"; added architecture note that all 6 run in a single ad set | Creative doc (both headers) | Depesh `Special_Ad_Categories.md` — campaign structure for PI |
| B-12 | Added Open Item #4: "Spanish creative deferred to Phase 2 — no Spanish copywriter hire, no Miguel protagonist, all 6 launch creatives English-only"; brief Robert on rationale before launch | Creative doc Open Items | — |

### IMPORTANT resolutions (15/15) — ✅ ALL RESOLVED

| ID | Fix | Files changed |
|---|---|---|
| I-1 | Doc 4 §10 (the cost benchmark table — finding misfiled as §7) funnel rates updated: 70%/65%/40%/85%/85%/50% → 60%/40%/15%/80%/85%/40% with Register cross-refs | Doc 4 §10 |
| I-2 | Added reading-guide banner above Doc 3 §6 noting Option A/B/C tables use pre-calibration rates for decision-context comparison; relative ranking (Option C wins on signal density) holds under calibration | Doc 3 above §6 |
| I-3 | "Original Recommendation: Modified Option B" → "Historical Reasoning: Modified Option B (pre-2026-04-22) — Superseded by Option C"; added superseded banner pointing to §12 architecture update + Doc 6 §2 | Doc 3 §12 |
| I-4 | Marco age reconciled: persona doc says 35, character brief says 38. M1 persona line updated: "Marco Reyes — 38" with persona-vs-casting note | Creative doc M1 persona line |
| I-5 | Doc 5 §F added "Motorcycle Creative Third-Person Verification (M1, M2, M3)" sub-checklist explicitly verifying all three hooks are third-person per 2026-04-21 M3 hook swap | Doc 5 §F |
| I-6 | AZ Bar counsel review added to both Doc 5 §F Pre-Launch Compliance Sign-Off and Creative doc Compliance Sign-Off | Doc 5 §F, Creative doc |
| I-7 | Prop consistency expanded from 4 bullets to full per-character prop + identifying-mark spec (Marco scar + stubble + vest + wedding band + tan line; Sarah brace left + scrubs + wedding band + pregnancy; Laura cane left + right ankle wrap + left forearm scar; Diana sling right + fading bruise right jawline + glasses in hair) | Creative doc character consistency |
| I-8 | Quiz funnel spec locked at 7 steps per Doc 6 §9; added note that 5 vs 7 is a Week 1-3 optimization, not pre-launch ambiguity | Creative doc compliance section |
| I-9 | Persona-to-Creative Mapping table in Doc 5 updated: "Ad Set 1" / "Ad Set 2" → "Single ad set"; Sofia row marked Phase 2 scaffold; budget allocation summary updated to $7,750 Meta + $975 creative + $500 tech + $750 margin = $9,975 contract | Doc 5 Persona-to-Creative Mapping + Budget summary |
| I-10 | Gender split rationale expanded in Creative doc casting summary: explicit note that Marco male = 92-94% male motorcycle victims (demographic accuracy), female dominance in severe-injury = female form-filler asymmetry (55-60% of PI intake filed by female family members) | Creative doc casting summary |
| I-11 | Moot under B-2 (TikTok deferred to Phase 2); documented as deprecated in Register 7.12 | Register 7.12 |
| I-12 | Doc 5 §A self-qualification hypothesis escalation path added: 10-15% soft warning / <10% kill threshold / <8% after backup = structural creative failure — each with named action, owner, time window | Doc 5 §A |
| I-13 | Doc 2 §6 Sofia header now has "⚠️ PHASE 2 SCAFFOLD — DO NOT PRODUCE PHASE 1 CREATIVE" banner | Doc 2 §6 |
| I-14 | "Lead-Quality-By-Timing Framework" → "Lead-Response-Timing Framework" with explicit clarification that timing is about ad-response speed, not accident recency (quiz Step 2 captures accident recency separately) | Doc 6 §6.5 |
| I-15 | Moot under B-2 (geofencing deferred to Phase 2); documented as deprecated in Register 7.11 | Register 7.11 |

### POLISH items (11) — ⏸️ DEFERRED BY DESIGN

P-1 through P-11 documented in the POLISH section above, not actioned in this pass. None are blockers to launch. Polish-batch can be addressed in parallel with Robert's Phase 1 review window or dropped if Phase 1 lands cleanly.

### Launch readiness (post-execution)

**🟢 GREEN — Playbook is launch-ready.**

Next actions (Davis owns):
1. Lock 4 protagonist reference images using ChatGPT Images 2.0 character-consistency mode + the briefs in `Creative/Week_1_Launch_Concepts.md`.
2. Send Creative doc to Robert for directional approval (hooks + visual direction + rationale, no mockups yet).
3. Generate 6 Phase 1 creatives after directional sign-off.
4. Meta ad review submission 48-72 hours before launch.
5. AZ-licensed counsel review before final Meta submission per Service Agreement §7.1.

---

*Fix execution: 2026-04-22 PM — Claude (sonnet-driven) with 03_Media doctrine anchors from Depesh Mandalia, Simon Croft, Indigo Sato. 12 blockers + 15 important findings resolved sequentially per approved plan. Grep verification clean. 11 polish items deferred. Playbook flipped RED → AMBER → GREEN.*
