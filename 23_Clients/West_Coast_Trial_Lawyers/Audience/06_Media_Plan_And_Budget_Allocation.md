> **⚠ PERSONA REFERENCES SUPERSEDED 2026-04-23.** Wherever this doc says "Marco" (e.g., §2 architecture diagram, §3.1 per-creative notes), read it as **Ty Rivera** per `Audience/Deep_Personas/Ty/`. The motorcycle protagonist pivoted 2026-04-22 from Marco (cruiser) to Ty (supersport).
>
> **This doc remains authoritative for:** budget allocation ($7,750 media / $975 production / $500 tech / $750 margin), single-ad-set consolidation rationale, CPL trajectory ($337–517 blended), learning-phase thresholds, refresh protocol, kill criteria, quiz funnel spec, and Pre-Launch Checklist.
>
> **This doc is NOT authoritative for persona-level casting, visual direction, or ad-copy details** — use `Deep_Personas/` and `Creative/Week_1_Approval_Package/` for those.

---

# Media Plan & Budget Allocation [MEDIA AUTHORITATIVE — PERSONA REFS SUPERSEDED]
## Arizona Non-Soft-Tissue PI Pilot Campaign — $10K

**Prepared:** April 13, 2026
**Lead Agents:** Simon Croft (Head of Media Buying — Budget Allocation) + Depesh Mandali (Meta Campaign Structure — OCEAN Framework)
**Campaign:** Second Chair x West Coast Trial Lawyers — $10K Arizona Pilot
**Status:** Executable media plan. This is the document the team works from on launch day.
**Platform:** 100% Meta (Facebook + Instagram via Advantage+ placements)

**Upstream documents:**
- Doc 0: Evidence Register — load-bearing numbers across all docs
- Doc 1: AZ Non-Soft-Tissue Demographics
- Doc 2: Case Type Personas
- Doc 3: Audience Sizing by Case Type — Ad Set Architecture Decision
- Doc 4: Platform Behavior & Advertising Reach Analysis

> **Rigor note (2026-04-21):** All load-bearing numbers in this doc are indexed in `00_Evidence_Register.md`. Every kill threshold and reallocation trigger in §6 and §7 now binds to a full decision rule (who, when, action). §6.5 (new) adds a lead-quality-by-timing framework and audience exclusion list. See Register §13 for the full Week-1 decision-rule chain.

> **Scope update (2026-04-21):** DUI case types excluded per signed Service Agreement §1.3. All Week 1 creative is AI-generated (no stock b-roll, no live shoots).

> **Architecture update (2026-04-22):** Collapsed to **one main campaign, one ad set, 6 launch creatives** (was two campaigns with 25/75 motorcycle split). Rationale in §2 below. Spanish pedestrian creative deferred to Phase 2 with dedicated budget (not starved as 1-of-7 in a broad ad set). Phase 1 launch set = 6 assets: M1/M2/M3 (Marco) + S1 (Sarah) + S2 (Laura) + S5 (Diana).

> **Budget collapse (2026-04-22):** Phase 1 is **Meta-only at $7,750** (retargeting within the same Meta account, no separate channel spend). Geofencing / TikTok / Reddit are deferred to Phase 2 as exploratory channels with dedicated budgets — not carved out of Phase 1 spend where a single sub-$1K allocation can't clear a learning phase. Doctrine: Simon's `Media_Buying_Systems.md` — do not starve channels below signal density; a $625 TikTok test without a reallocation mechanism is theatre, not learning. Expected Phase 1 output: ~21 leads (single point estimate, range 18-24 under sensitivity).

---

## Table of Contents

1. [Budget Overview](#1-budget-overview)
2. [Campaign Structure](#2-campaign-structure)
3. [Budget Allocation by Phase](#3-budget-allocation-by-phase)
4. [Daily Spend Schedule](#4-daily-spend-schedule)
5. [Optimization Events & Pixel Setup](#5-optimization-events--pixel-setup)
6. [Kill Criteria & Reallocation Rules](#6-kill-criteria--reallocation-rules)
7. [Reallocation Triggers](#7-reallocation-triggers)
8. [Reporting Cadence](#8-reporting-cadence)
9. [Lead Delivery Workflow](#9-lead-delivery-workflow)
10. [Phase 2 Expansion Triggers](#10-phase-2-expansion-triggers)
11. [Risk Mitigation](#11-risk-mitigation)

---

## 1. Budget Overview

**Total client payment:** $9,975 (Service Agreement §4.1 — contractual)
**Target delivered leads:** 21 (Contract §4.3)

| Line Item | Amount | % of Total | Notes |
|-----------|--------|-----------|-------|
| **Media — Meta (FB+IG)** | $7,750 | 77.7% | 100% of Phase 1 media. Facebook + Instagram via Advantage+ placements. Retargeting runs within the same Meta account (see §2) — no separate channel budget. |
| **Creative production** | $975 | 9.8% | AI-generated video + static (Phase 1 English-only per 2026-04-22 scope). ChatGPT Images 2.0 character-consistency workflow. |
| **Funnel / tech** | $500 | 5.0% | Quiz funnel hosting, pixel implementation, verification pipeline, TCPA compliance, TrustedForm. |
| **Second Chair margin** | $750 | 7.5% | Operating margin. |
| **Total** | **$9,975** | **100%** | |

**Total media spend: $7,750 — Meta only.**

### Phase 2 Exploratory Channels (Deferred, Not in Phase 1 Budget)

Geofencing (hospitals / orthopedic / collision repair), TikTok, and Reddit were spec'd as supplementary channels in earlier drafts. Under the 2026-04-22 architecture collapse, they are **deferred to Phase 2** with dedicated budgets, not carved out of Phase 1 spend. Rationale (Simon, `Media_Buying_Systems.md`):

- A $625 TikTok allocation can't clear the Meta-equivalent learning signal *and* survive 30-50% SAC rejection probability without a clean reallocation mechanism.
- A $625 geofencing test requires DSP infrastructure (Sasha) that is Phase 2 scope; standing it up for a single flight produces sunk setup cost with no repeatable learning.
- A $375 Reddit buy at platform CPCs produces ~250-500 clicks — below any decision-quality signal threshold.

If Phase 1 lands against the 21-lead target, Phase 2 proposal includes a dedicated multi-channel diversification pass (see §10) with budgets scaled to clear each channel's learning threshold.

### What the $7,750 Meta Spend Buys (Estimated, Calibrated)

| Metric | Estimate | Source |
|--------|----------|--------|
| CPM (AZ legal, Special Ad Category) | $35 midpoint ($30-$45 range) | Register 7.1, 7.2 |
| Impressions | ~172,000-258,000 | $7,750 / CPM |
| Unique reach (est. freq. 2.5) | ~69,000-103,000 | Impressions / 2.5 |
| CTR | 1.0% | Register 7.7 (kill threshold 0.8%) |
| Clicks | ~1,720-2,580 | |
| Landing page views | ~1,550-2,320 | ~90% of clicks load the page |
| Quiz starts (60% of LPVs) | ~930-1,390 | Register 6.1 calibrated |
| Quiz completions (40% of starts) | ~370-560 | Register 6.2 calibrated |
| NST-qualified (15% of completions) | ~56-84 | Register 6.3 calibrated |
| Contact submitted (80%) | ~44-67 | Register 6.4 |
| Verification pass (85%) | ~38-57 | Register 6.5 |
| Delivered leads (40% final) | **~15-23** | Register 6.6 — midpoint ~19, target 21 |
| Cost per delivered lead (media) | **~$337-$517** | |

**Revenue math:** 21 leads × $475/lead = $9,975 (matches contract). Single-channel Meta architecture delivers against the target without multi-channel optionality — tradeoff accepted: less upside, but every dollar consolidated into one learning model that clears threshold by 4× on LPV optimization (see §5).

---

## 2. Campaign Structure

### Meta Ads Manager Setup

Campaign runs under **Special Ad Category: Social Issues** (the required classification for legal advertising under Meta's policies). This locks targeting to broad — no age, gender, interest, or behavioral narrowing. Arizona statewide. Creative does the targeting.

> **Architecture update (2026-04-22):** This section was previously specced as two campaigns (Motorcycle + Severe Injury) plus retargeting. Updated to **one main campaign with one ad set running all 6 creatives**, plus the retargeting campaign (unchanged). Rationale: at this budget ($7,750 media), consolidating into one ad set produces ~200 weekly completions — 4× the Meta learning threshold, vs. threshold-level in the split architecture. Motorcycle creative's 5/5 identity-based self-qualification (Doc 3 §10) protects its audience reach without needing a locked budget share, because motorcycle creative is structurally useless to non-riders. The algorithm can't meaningfully cannibalize motorcycle — it will naturally serve motorcycle creative to engagement-qualified riders regardless of budget competition.

```
CAMPAIGN 1: WCTL-AZ-Pilot
├── Objective: Traffic (Landing Page Views)
├── Special Ad Category: Social Issues
├── Geographic Target: Arizona (statewide)
├── Audience: Broad (all adults, no narrowing — SAC restriction)
├── Placements: Advantage+ (Facebook Feed, Instagram Feed, Stories, Reels, Audience Network)
├── Budget: $7,750 total / ABO at $220/day (Phase 1)
│
└── Ad Set 1: AZ-Statewide-Broad-AllNonSoftTissue
    ├── M1: Motorcycle — Identity — Video · Marco protagonist
    │   "Riders don't ask for sympathy. They ask for what's fair."
    │   Marco on wall with bike, garage interior empty spot. 15-30 sec.
    │
    ├── M2: Motorcycle — Loss — Video · Marco protagonist
    │   "What the crash took is still being taken."
    │   Marco at kitchen table, bills + paused laptop. 15-30 sec.
    │
    ├── M3: Motorcycle — Injustice — Static · Marco protagonist
    │   "A driver didn't see the rider."
    │   Marco at intersection + empty side mirror.
    │
    ├── S1: Trucking — David vs. Goliath — Video · Sarah protagonist
    │   "Hit by a semi on I-10?"
    │   Sarah in passenger seat, insurance policy close-up, corporate room vs. kitchen table. 15-30 sec.
    │
    ├── S2: Pedestrian (English) — Innocence — Static · Laura protagonist
    │   "Hit while crossing the street?"
    │   Laura at suburban Phoenix crosswalk at dusk.
    │
    └── S5: General Severe MVA — Financial crisis — Video · Diana protagonist
        "Broken bones. Bills don't stop."
        Diana at kitchen table, mounting envelopes, arm sling. 15-30 sec.

(Excluded/deferred: S3 Spanish pedestrian creative — deferred to Phase 2 with dedicated budget. DUI excluded per Contract §1.3.)


CAMPAIGN 2: WCTL-AZ-Retargeting (Activates end of Week 2 when pixel accumulates 500+ LPVs)
├── Objective: Traffic (Landing Page Views)
├── Special Ad Category: Social Issues
├── Geographic Target: Arizona (statewide)
├── Audience: Custom — Website visitors, 7-day window + Quiz-starters-who-didn't-complete 14-day window
├── Placements: Advantage+
├── Budget: $0 Weeks 1-2; ~$6/day test end of Week 2; $12-24/day Weeks 3-5 (within $7,750 envelope, reallocated from main campaign daily caps)
│
└── Ad Set 1: Website-Visitors-7-Day
    ├── Creative 1: Urgency / statute messaging
    │   "You started the quiz but didn't finish. Arizona's 2-year deadline
    │    doesn't wait. Pick up where you left off — 60 seconds."
    │
    └── Creative 2: Social proof messaging
        "Thousands of Arizonans have already checked what their case is worth.
         Your turn — it's free and takes 60 seconds."
```

### Why One Campaign, One Ad Set

Doc 3 §8 (Option C) established that at this budget, consolidating all spend into a single ad set produces maximum learning signal (~200 weekly completions, 4× threshold). The previous spec here (2 campaigns with a 25/75 motorcycle budget lock) was a compromise meant to protect motorcycle reach from algorithmic cannibalization. On reconsideration for the 2026-04-22 architecture decision:

1. **Signal density wins at this budget.** 200 weekly completions in one ad set vs. 50/152 split across two — the single-ad-set approach exits or approaches exit of the Meta learning phase faster, producing more efficient delivery on every dollar.
2. **Motorcycle's self-qualification replaces the budget lock.** Marco's identity-based creative (Doc 3 §10, 5/5 distinctiveness) only resonates with riders. The algorithm learns within days which impressions generate motorcycle clicks and serves more motorcycle creative to those audience subsets. Budget lock was trying to solve a problem that self-qualifying creative already solves.
3. **Operational simplicity.** One campaign, one ad set, six creatives, one reporting view. Alex doesn't split attention across two campaigns' learning curves, one set of kill/reallocate triggers applies to the whole pilot.

**Risk we accept:** If motorcycle creative dramatically under-performs on CTR relative to severe-injury creative, Meta will allocate less to motorcycle. Monitor this weekly; if motorcycle impressions drop below 15% of ad set impressions by Week 2, manually boost via creative-level bid or split motorcycle into its own ad set at $1,500 for the remainder of the campaign (hot-swap architecture).

### Why a Single Ad Set

Multiple creative variants within that single ad set let the algorithm test and distribute across case types (motorcycle / trucking / pedestrian / MVA) and hook angles (identity / loss / injustice / severity). The algorithm does the segmentation with data. We provide the creative diversity. Splitting creative into multiple ad sets would starve each one at this budget.

---

## 3. Budget Allocation by Phase

### Phase 1: Testing (Weeks 1-2)

| Parameter | Value |
|-----------|-------|
| **Budget** | ~$3,100 (40% of $7,750 media) |
| **Daily spend** | ~$220/day |
| **Ad set daily** | ~$220/day (single ad set, all 6 creatives compete for allocation) |
| **Expected internal split** | Algorithm will distribute. Motorcycle creative expected ~20-30% of impressions (riders self-qualify via identity creative); trucking/pedestrian/MVA expected ~70-80% (larger audience, more event volume). |
| **Retargeting daily** | $0 |
| **Optimization** | ABO (Ad Set Budget Optimization) -- budgets fixed at ad set level |
| **Goal** | Find winning creatives. Let the algorithm through the learning phase. Gather baseline CTR, CPC, quiz start rate data. |

**What happens in Phase 1:**
- All 6 creative variants go live simultaneously in the single ad set (M1, M2, M3, S1, S2, S5).
- Meta's algorithm distributes impressions across all 6 creatives, testing which audience-creative pairings generate the most landing page views.
- **Do not touch anything for the first 5 days.** The algorithm needs uninterrupted data collection. Pausing/editing creatives during learning resets the learning phase.
- Day 5-7: First performance check. Identify which creatives are above/below CTR and CPC thresholds (see Section 6). **Motorcycle impression share check** — if <15% of ad set impressions are motorcycle creative, flag for Week 2 review (hot-swap consideration per §2).
- Day 7: Execute first kill/keep decisions.
- Day 10-14: Second performance check. Monitor quiz start and completion rates. Identify funnel drop-off points.

**Expected Phase 1 output:**
- Impressions: ~30,000-44,000
- Clicks: ~300-440
- Quiz starts: ~210-310
- Delivered leads: **3-5** (higher CPL during learning — this is expected and acceptable)
- Data: Clear creative performance ranking across all 6 variants

### Phase 2: Optimization (Weeks 2-3)

| Parameter | Value |
|-----------|-------|
| **Budget** | ~$2,325 (30% of $7,750 media) |
| **Daily spend** | ~$165/day main + $6/day retargeting test end of Week 2 |
| **Ad set daily** | ~$159/day main ad set (tapered from $220 as total spend tapers) |
| **Retargeting daily** | **$0 Week 2 days 1-3 → $6/day day 4 onward** (activates when 7-day pixel custom audience hits 200+ people, expected mid-Week 2 under calibrated funnel) |
| **Optimization** | Main campaign remains ABO. Retargeting campaign runs ABO at low budget. |
| **Goal** | Scale winners. Kill losers. Activate retargeting while Week 1-2 abandoners are still inside the 7-day custom-audience window — Depesh's `Lead_Gen_Playbook.md`: highest-intent retargeting audience is quiz-starters-who-didn't-complete, and the 7-day window closes fast. |

**What happens in Phase 2:**
- Pause underperforming creatives (any creative that failed kill criteria in Phase 1).
- Remaining creatives get proportionally more budget — the algorithm concentrates delivery on what works.
- If one creative dominates (e.g., trucking video at 3× the CTR of everything else), consider pausing it for 48 hours to force redistribution, then reactivating.
- **Motorcycle impression-share check:** if motorcycle creative (M1/M2/M3) collectively holds <15% of ad set impressions, consider hot-swap to split motorcycle into dedicated ad set per §2 contingency.
- Monitor quiz completion and lead quality. If quiz completion rate is below 15% of starts, investigate funnel friction (see Section 6).

**Expected Phase 2 output:**
- Impressions: ~23,000-33,000
- Clicks: ~230-330
- Delivered leads: **7-9** (CPL improving as algorithm optimizes on winning creatives)
- Data: Validated creative winners, stable CPC/CTR, initial funnel conversion benchmarks

### Phase 3: Scale (Weeks 3-5)

| Parameter | Value |
|-----------|-------|
| **Budget** | ~$2,325 (30% of $7,750 media) |
| **Daily spend** | ~$115-$165/day main + $12-$24/day retargeting |
| **Ad set daily** | ~$100-$145/day main (tapered across Weeks 3-5) |
| **Retargeting daily** | **$12-$24/day** (scaled with pixel data — already activated end of Week 2) |
| **Optimization** | ABO or CBO based on Phase 2 performance. Algorithm should be post-learning or near-exit. |
| **Goal** | Maximize delivery on proven winners. Harvest leads at lowest CPL. Retargeting compounds — people who quiz-started in Weeks 1-2 are the warmest audience in Weeks 3-5. |

**What happens in Phase 3:**
- Only winning creatives remain active (likely 3-5 of the original 6, down from all 6).
- Daily budgets taper slightly as the campaign approaches total spend cap.
- **Retargeting campaign activates** if there are 500+ website visitors in the pixel by Week 4. This re-engages people who clicked but didn't complete the quiz.
- Begin preparing creative refresh assets in case of fatigue (CTR declining week-over-week on a previously strong creative).
- Focus shifts from media optimization to lead quality review: Are delivered leads resulting in consultations? Is Robert's team following up? What's the initial sign rate signal?

**Expected Phase 3 output:**
- Impressions: ~23,000-33,000
- Clicks: ~230-330
- Delivered leads: **8-10** (lowest CPL phase -- algorithm is mature, only winners running)
- Retargeting delivers: **1-2 additional leads** if activated
- Data: Full campaign performance dataset, creative winners documented, funnel conversion rates locked

### Total Expected Output Across All Phases

| Phase | Duration | Budget | Daily Spend | Expected Leads | Expected CPL (Media) |
|-------|----------|--------|-------------|----------------|---------------------|
| Testing | Weeks 1-2 | $3,100 | $220/day | 3-5 | **~$620–$1,033** (cost-of-learning band) |
| Optimization | Weeks 2-3 | $2,325 | $165/day | 7-9 | ~$258-$332 |
| Scale | Weeks 3-5 | $2,325 | $115-$165/day | 8-10 | ~$233-$291 |
| **Total** | **5 weeks** | **$7,750** | — | **~21 (18-24 range)** | **~$337-$430 blended** |

**About the Phase 1 CPL range (Register 8.9):** The $620–$1,033 band is a 67% uncertainty range, and it's that wide because Phase 1 is the learning phase — a handful of leads land on a small sample of spend, so small changes in lead count produce large CPL swings ($3,100 ÷ 3 = $1,033; $3,100 ÷ 5 = $620). The range is not a forecast; it's the **cost-of-learning band**. Expected behavior:

| Week | Expected CPL narrowing |
|------|----------------------|
| Day 1–3 | No stable signal. Do not compute CPL. |
| Day 4–7 | CPL likely near or above $1,033 (1–2 leads on ~$1,100 spend) |
| Day 8–14 | CPL narrows to $700–$900 range as second-week leads arrive |
| End of Week 2 | Phase 1 CPL lands inside the published band |
| Start of Week 3 | Expect step-change downward as optimization kicks in |

**Do not report Phase 1 CPL to Robert as a weekly number.** Report it as a rolling cumulative + trajectory. Weekly Phase 1 CPLs are statistically noisy and will frighten him.

The CPL trajectory is the story to tell Robert: Week 1 CPL will be ugly. That is the cost of the algorithm learning who converts. By Week 3–5, the CPL drops to a fraction of Week 1 because we killed losers and scaled winners. **First 25% of spend produces worst CPL. Last 25% produces best CPL.** Set this expectation upfront.

---

## 4. Daily Spend Schedule

### Week-by-Week Breakdown

| Week | Phase | Campaign 1: WCTL-AZ-Pilot (single ad set) | Campaign 2: Retargeting | Total Daily | Weekly Total |
|------|-------|-------------------------------------------|-------------------------|-------------|-------------|
| **1** | Testing | $220/day | $0 | $220/day | $1,540 |
| **2** | Testing / Opt | $214/day | $6/day (day 4+ once pixel ≥200 in custom audience) | $220/day avg | $1,540 |
| **3** | Optimization | $147/day | $18/day | $165/day | $1,155 |
| **4** | Scale | $118/day | $24/day | $142/day | $994 |
| **5** | Scale | $98/day | $24/day | $122/day | $854 |
| | | | | | |
| **Totals** | | **$5,527** | **$556** | | **$6,083** |

**Remaining buffer:** $7,750 - $6,083 = **$1,667 reserve** (21.5% of total media budget).

**Reading the buffer correctly:** The $1,667 is NOT a second layer on top of the Phase-by-phase spend reserves. The 40/30/30 phase allocation ($3,100/$2,325/$2,325) is a planning envelope; the daily schedule above sums to $6,083, which is $1,667 less than the full $7,750 envelope. In other words: the daily caps in the table above are conservative, and the $1,667 is the unscheduled headroom between those conservative caps and the full envelope. It is a single buffer, not a buffer on top of a buffer.

This reserve exists because:
1. Meta rarely spends exactly 100% of daily budget every day. Actual delivery typically runs 85–95% of set budget, especially during learning — so conservative daily caps are appropriate.
2. Weekend delivery often dips (lower scroll volume on Sundays).
3. The reserve provides flexibility for reallocation if a creative breaks out and warrants a budget increase mid-campaign.

**How to deploy the reserve:**
- If the pilot campaign is pacing under budget, increase daily caps by 10-15% in Weeks 3-5 to ensure full spend.
- If a creative is a clear winner by Week 3, allocate reserve as additional daily budget.
- If the campaign is pacing to underspend by >$500 at Week 4, extend to Week 6 at the same daily rates rather than increasing daily spend.
- **Do not front-load the reserve into Weeks 1-2.** The algorithm is still learning; more money during learning = more money spent inefficiently.

### Budget Accounting Check

| Item | Amount |
|------|--------|
| Scheduled media (5 weeks) | $6,083 |
| Reserve / flex | $1,667 |
| **Total media budget (Meta only)** | **$7,750** |
| Creative production | $975 |
| Funnel / tech | $500 |
| Margin | $750 |
| **Total client payment (contract)** | **$9,975** |

---

## 5. Optimization Events & Pixel Setup

### Primary Optimization Event: Landing Page Views

**Why landing page views -- not quiz completions, not lead submissions.**

| Optimization Event | Expected Weekly Volume (Whole Campaign) | vs. 50/week Threshold | Verdict |
|-------------------|----------------------------------------|----------------------|---------|
| Lead submissions (delivered) | ~4/week | 0.08x | Impossible. Algorithm has no signal to learn from. |
| Quiz completions | **~89-133/week** (calibrated, Register 8.1) | **1.8-2.7x threshold** | Viable on single ad set but thin cushion. Option for Week 3+ shift once pixel accumulates more data. |
| Quiz starts | ~221-332/week (Register — 60% of 369-554 clicks) | 4.4-6.6x | Safe, still mid-funnel. |
| **Landing page views** | **~310-440/week** | **6.2-8.8x** | **Best option for Week 1-2. Maximizes signal density while keeping event relevant to intent.** |
| Link clicks | ~369-554/week | 7.4-11x | Counts bounces. Landing page views are clicks that actually loaded the page — higher quality signal. |

At ~$7,750 spend across 5 weeks, we get ~1,720-2,580 total clicks but only ~18-24 delivered leads (target 21). That is ~4 leads per week — not even 10% of Meta's 50/week learning threshold for deep events.

**Landing page views (~310-440/week) in one ad set give the single-ad-set campaign 6-9× the learning threshold — strongest signal density of any architecture we evaluated.** The algorithm learns which impressions produce page loads, and the quiz itself filters from there. At Week 3, once ~100+ calibrated weekly quiz completions have accumulated (Register 8.1), we can consider shifting optimization to quiz completions for a sharper-intent signal.

**When to shift optimization event:** If the campaign scales to $25K+ (Phase 2), shift optimization to quiz completions. At that budget, weekly completion volume will clear the 50/week threshold per ad set. Never optimize for lead submissions until weekly volume exceeds 50 delivered leads/week (requires ~$100K+/month spend).

### Pixel Implementation

| Component | Setup Required | Tracking Purpose |
|-----------|---------------|-----------------|
| **Meta Pixel (base code)** | Install on all quiz funnel pages | Tracks all page views, enables retargeting audiences |
| **PageView event** | Auto-fires on pixel load | Base tracking on every page |
| **Landing Page View (standard event)** | Fire on quiz landing page load | **Primary optimization event.** This is what Meta optimizes toward. |
| **ViewContent** | Fire on quiz Step 1 (accident type selection) | Tracks quiz engagement start |
| **Lead (standard event)** | Fire on quiz completion (contact info submitted) | Tracks quiz completions for reporting |
| **CompleteRegistration** | Fire when lead passes all qualification filters and is delivered | Tracks delivered leads for CPL reporting |
| **Custom event: QuizStart** | Fire on first quiz interaction | Tracks quiz start rate vs. landing page views |
| **Custom event: InjuryFilterPass** | Fire when user passes non-soft-tissue injury filter | Tracks qualification rate |

### Event Flow

```
User clicks ad
    → Landing page loads → [Landing Page View event fires] ← PRIMARY OPTIMIZATION EVENT
        → User starts quiz → [QuizStart custom event fires]
            → User selects accident type → [ViewContent fires]
                → User passes injury severity filter → [InjuryFilterPass fires]
                    → User submits contact info → [Lead event fires]
                        → Lead passes verification + QA → [CompleteRegistration fires]
```

### Retargeting Audiences (Built Automatically by Pixel)

| Audience | Definition | Use |
|----------|-----------|-----|
| Website visitors - 7 day | Anyone who triggered Landing Page View in last 7 days | Campaign 3 retargeting |
| Website visitors - 30 day | Anyone who triggered Landing Page View in last 30 days | Broader retargeting if needed |
| Quiz starters who didn't complete | QuizStart fired but Lead did not fire, last 14 days | Highest-intent retargeting audience |
| Video viewers 50%+ | Watched 50%+ of any video creative | Mid-funnel awareness retargeting |

**Minimum audience size for retargeting:** Meta requires ~200 people in a custom audience before it can serve ads. At calibrated ~310-440 weekly LPVs, the 7-day website visitor audience hits 200 by mid-Week 2 (Day 10-12), making retargeting **activatable end of Week 2** — not Week 3-4. Earlier activation matters because Meta custom audiences use a 7-day window; quiz-starters-who-abandoned in Weeks 1-2 fall out of the retargetable pool if activation slips to Week 4. Direct measurable loss of delay = ~1-2 retargeting-sourced leads (5-10% of total). Depesh's `Lead_Gen_Playbook.md` governs: activate retargeting as soon as audience size qualifies, don't wait for "full" Phase 3.

---

## 6. Kill Criteria & Reallocation Rules

> **Format:** Every threshold below is bound to a full decision rule: **Metric → Threshold → Observation window → Who decides → Action → Funnel-friction diagnosis (if funnel) → Recovery path.** No orphan "investigate" categories — every "investigate" has a named protocol.

### Creative-Level Kill Criteria

| Metric | Threshold | Observation window | Who | Action | Rationale |
|--------|-----------|-------------------|-----|--------|-----------|
| **CTR** | <0.8% after 1,000 impressions | Day 5–7 rolling | Alex (daily) → Davis (decision) | **Pause creative.** Document in weekly report. If >2 creatives pause in same week, pull Davis in for creative review before backups launch. | At $35–50 CPM, 0.8% CTR = $4.38–$6.25 CPC — at the high end of acceptable. Below, CPC is unsustainable. |
| **CPC** | >$6.00 sustained over 3 days | Day 7+ rolling | Alex → Davis | **Pause creative.** Check CTR — if both CTR <0.8% AND CPC >$6.00, the creative is dead, not underperforming. | $6.00 CPC produces ~14 delivered leads against the 21 target. |
| **CTR + zero quiz starts** | <1.0% CTR AND zero quiz starts after 500 impressions | Day 3–5 | Alex (same-day) | **Pause creative immediately.** No 5-day rule — this is a broken handoff, not a learning issue. Document which creative-LP pairing failed for Week-2 creative iteration. | Creative attracting curiosity clicks that don't convert. The creative-to-funnel handoff is broken. |
| **Frequency** | >4.0 on any creative | Weekly check starting Week 3 | Alex | **Rotate:** pause the fatigued creative, activate the matched backup variant from §G (Doc 5). Do not launch a net-new concept — iterate on the winning hook. | Creative fatigue. Same people seeing same ad too many times. |

### Funnel-Level Kill Criteria

Each funnel metric below maps to a Register validation plan (6.1, 6.2, 6.3). If the actual number comes in below threshold, the funnel-friction diagnosis protocol below kicks in.

| Metric | Threshold | Observation window | Who | Action | Diagnosis protocol |
|--------|-----------|-------------------|-----|--------|--------------------|
| **Quiz start rate** (Register 6.1 — target 60%) | **<45% of landing page views** (25% below calibrated target; aligns with Simon's Media_Buying_Systems.md 1.25-1.5× miss band) | After 100 LPVs (expected Day 7–10) | Alex → Davis if fires | **Revise landing page.** Specifically: (1) shorten headline if >8 words, (2) move quiz CTA above the fold, (3) check mobile page load <3s, (4) verify trust badges render. Ship revision within 48 hours of fire. | Use Meta LP View → QuizStart funnel drop in Ads Manager. Use a heatmap tool (Hotjar or Microsoft Clarity session recordings) to identify what people click on before bouncing. |
| **Quiz completion rate** (Register 6.2 — target 40%) | **<30% of starts** (25% below calibrated target) | After 50 starts (expected Day 10–14) | Alex → Davis | **Revise quiz flow.** Specifically: (1) identify highest-drop-off step from the pixel event sequence (QuizStart → ViewContent → InjuryFilterPass → Lead), (2) if drop between ViewContent and InjuryFilterPass → simplify Step 3 injury severity question (too medically specific), (3) if drop after InjuryFilterPass → contact step is the friction, reduce required fields, (4) add a progress bar if not present, (5) test 8-step vs. 5-step. Ship revision within 72 hours. | Step-by-step drop-off data from pixel events. Microsoft Clarity recordings of quiz sessions (opt-in only) to see hesitation points. If no Clarity: survey a sample of quiz abandoners via post-exit redirect. |
| **Non-soft-tissue pass rate** (Register 6.3 — target 15%) | **<10% of completions** (33% below calibrated target — wider band because the 15% baseline is already aggressive vs. PI industry norm) | After 50 completions (expected Day 14+) | Alex → Davis | **Revise creative copy + quiz Step 3.** Specifically: (1) add "broken bones, surgery, hospital" to every hook still active, (2) remove any creative that relies on "injured?" or "hurt?" as a qualifier, (3) refresh with Doc 5 §A Strategy 4 (negative self-qualification) phrases, (4) tighten quiz Step 3 injury-severity options (remove "unsure" as pass-through). Ship within 72 hours. | Pull the last 50 completed quizzes, categorize by stated injury. If >60% self-report whiplash / minor sprain despite passing Step 3, the injury question isn't filtering — revise the quiz, not the ads. |

### Campaign-Level Kill Criteria

| Metric | Threshold | Observation window | Who | Action |
|--------|-----------|-------------------|-----|--------|
| **CPL (cost per delivered lead)** | >$600 after 10 delivered leads | Expected Week 3 | Davis (decision), Alex (execution) | **Restructure campaign.** Options in priority order: (1) emergency creative refresh if CTR is the cause, (2) quiz redesign if completion rate is the cause, (3) consolidate to 1 campaign if motorcycle ad set is the drag. Decision within 48 hours; execution within 72. |
| **Any ad set with zero delivered leads** | After $500 spend in that ad set | Rolling | Alex (trigger), Davis (decision) | **Pause ad set.** Run the funnel-friction diagnosis above for that specific ad set. Do not resume until the diagnosis lands on one of: quiz routing issue, verification failure, or creative targeting issue — and each has a different fix. |
| **Campaign spend pacing >120% of schedule** | More than 20% ahead of daily plan | Weekly | Alex | **Reduce daily caps by 10–15%** to bring pacing back to plan. Meta sometimes overspends by up to 25%. |
| **Campaign spend pacing <70% of schedule** | More than 30% under daily plan | Day 3–5 | Alex (trigger), Davis (investigate) | **Diagnose delivery.** Check: Special Ad Category review status, creative rejection flags, bid floor. Fix root cause before adjusting budget. |

### Creative Refresh Protocol

When Week 3+ rotation fires (either creative fatigue or CTR kill):

1. **Backup creative already exists** in Doc 5 §G backup asset table. Do not launch net-new concepts — iterate on the winning hook.
2. **Alex pauses the fatigued creative**, activates the pre-produced backup variant in the same ad set (no new ad set — preserves learning).
3. **48-hour observation window** on the backup before any further change.
4. **If backup also fails** (same CTR issue within 72 hours), the hook itself is dead, not the execution. Escalate to Davis for net-new concept work; do not auto-launch.
5. **Document in weekly report**: which creative paused, why, which backup activated, initial performance.

### The 5-Day Rule

**Do not make any optimization decisions in the first 5 days of any new creative or ad set.** The algorithm is in its initial exploration phase. Early data is noisy and unrepresentative. A creative that looks terrible on Day 2 may be the best performer by Day 7 once the algorithm finds its audience.

Exception: If a creative is rejected by Meta's ad review OR triggers the "CTR + zero quiz starts" broken-handoff rule above, address immediately. Do not wait 5 days for a rejected ad or a broken handoff.

---

## 6.5 Audience Exclusions & Lead-Quality-By-Timing

### Audience Exclusion List

Under Special Ad Categories we cannot target-exclude by interest, behavior, or demographic. We CAN exclude custom audiences — which is where wasted spend hides. Build and exclude:

| Exclusion audience | How to build | Why | When to enable |
|---|---|---|---|
| **WCTL existing clients / website visitors** | Pixel-based custom audience from wctrials.com visitors (180-day window) + upload of hashed email list of existing clients if Robert provides | They're already represented. Every impression to them is wasted spend. Also a bad brand experience. | Pre-launch — Day 0 |
| **Prior Second Chair quiz completers (all states)** | Custom audience from our own quiz funnel across all campaigns | Someone who already completed our quiz shouldn't see our AZ pilot ad. | Pre-launch — Day 0 |
| **Known litigator flags** (internal list) | Upload if/when we have a list | Prevents bot/scraper engagement from burning spend. | When list available |
| **WCTL's own Meta Page engagers** | Engagement audience from WCTL's Facebook page | People already actively engaged with WCTL likely already have a relationship. | Pre-launch — Day 0, if WCTL shares Page access |

**Exclusion mechanics:** In Meta Ads Manager → Ad Set → Audience → exclude custom audiences. Applies to every ad set in all three campaigns (Motorcycle, Severe Injury, Retargeting).

**Verify exclusions are working:** Week 2, pull the delivered leads list and cross-check against WCTL's existing-client list. If any match, the exclusion isn't firing — debug pixel or the uploaded list.

### Lead-Response-Timing Framework

> **Naming clarification (I-14 fix 2026-04-22):** This framework is about **how quickly people respond to our ads** (campaign delivery timing), not about how old their accident is (accident recency is captured separately in quiz Step 2). Earlier drafts mixed these up — a "Week 1 lead" is someone who saw our ad on Day 3 and filled out the quiz, independent of whether their accident was 2 weeks ago or 18 months ago.

Delivered leads arrive at different points in the 4–6 week campaign window. **Response timing** carries signal about the lead. Expected distribution (anchored to Doc 2 personas' post-accident psychology timeline):

| Window | Expected share of leads | What this window is capturing | Quality signal | Decision rule |
|---|---|---|---|---|
| **Week 1** | 10–15% | Early responders. People who already knew they needed a lawyer (prior bad experience, pre-research) | Expected quality: mixed. Some high-intent, some "professional claimants." | **If Week 1 leads >25% of total**, flag as quality risk — we may be attracting people too close to trauma (poor decision-makers) or over-represented claim-shoppers. Review grade distribution before Week 2 scale decisions. |
| **Weeks 2–4** | 40–55% | The bulk. People who realized the injury was serious enough to need a lawyer. Marco (Month 1) and Diana (Month 1–2) timelines land here. | Expected quality: baseline. This is what the model projects. | **If Weeks 2–4 deliver <30% of total leads**, the funnel isn't reaching the optimal engagement window — likely a creative hook issue, not a media issue. |
| **Week 5+** | 20–30% | Late responders. Insurance lowball received, conservative treatment failed, realized settlement inadequate. Marco (Month 3–6) timeline. | Expected quality: higher case value, longer recovery evidence = stronger claim. | **If Week 5+ share is high AND sign rate on these leads is high**, Phase 2 should extend campaign windows, not compress them. |

**Why this matters:** Without this framework, Robert sees a skewed delivery curve and panics. "Week 1 only gave me 2 leads!" is the expected shape, not a failure. With this framework, we set his expectations upfront and interpret the curve correctly at each checkpoint.

**Report this in the weekly update to Robert.** Include: cumulative lead count + this-week share + expected share for this window. Three numbers, one sentence.

---

## 6.6 Anchor Cohort Definition + Surface-Aware Format Rules (added 2026-04-30)

> **What's new:** Phase 1 creative now includes a controlled split-test variable — the Fair Case "Anchor" persistent bottom-frame overlay (Pattern 6, see `../../../02_Visual/Designed_Overlay_System.md §6`). This section defines the cohort, the surface-aware static-vs-video rule, and the validation thresholds. Cohort assignment lives in `../Creative/Anchor_Template_Spec.md`; full split-test plan in `../Creative/Phase_1_Split_Test_Plan.md`.

### Anchor Cohort vs. Clean Cohort

Both cohorts run inside the single Advantage+ ad set. Algorithm distributes naturally to the placements where each cohort earns its keep. No budget split, no separate ad set.

| Cohort | Units | Expected placement skew |
|---|---|---|
| **Anchored** (~13 units) | S1 Sarah trucking cinematic + S2 Laura pedestrian static + S5 Diana cinematic | FB Feed-heavy (designed/editorial register native to FB scroll) |
| **Clean** (~19 units) | M1/M2/M3 Ty motorcycle + S5 Diana UGC + HN/EX Designed Static Brand Units + matched-clean controls | IG Reels-heavy (UGC + cinematic motion native to Reels scroll) |

### Surface-Aware Static-vs-Video Rule

| Unit type | Surface | Format treatment |
|---|---|---|
| **S2 Laura static** | FB Feed | Pure static image post (FB Feed renders static at full impression weight; don't force motion where stillness is the editorial point) |
| **S2 Laura static** | IG Reels / Stories | Render as 4-7s ambient-motion video with audio bed (-18 LUFS); IG Reels surface downranks pure static |
| **HN/EX Designed Statics** | FB Feed | Pure static fine |
| **HN/EX Designed Statics** | IG Reels / Stories | Render as 4-7s ambient-motion |
| **All cinematic + UGC units** | All surfaces | Already video |

**Operational:** Davis or Alex builds 2 versions of each static unit — pure JPG for FB Feed placement, 4-7s MP4 with subtle motion + audio for IG Reels/Stories. Meta supports per-placement creative customization in Advantage+; the algorithm serves the right version to the right surface.

### Anchor Validation Thresholds (Week 1)

After Week 1 / 100+ qualified-lead-conversion events:

| Metric | Hypothesis | If confirmed | If disconfirmed |
|---|---|---|---|
| **FB Feed CPL (Anchored vs Clean)** | Anchored ≤ Clean on FB Feed | Lift Anchor to Phase 2 standard for FB-Feed-native units | Investigate variant copy + opacity |
| **IG Reels CPL (Anchored vs Clean)** | Clean ≤ Anchored on IG Reels | Confirm Anchor is FB-Feed-only pattern; never deploy on Reels-native creative | Re-test Translucent Dark Scrim variant |
| **Hook rate** | No more than 10% degradation either surface | Anchor isn't costing scroll-stops; ship | Reduce panel opacity or revisit copy density |
| **Hold rate (75%)** | Anchored ≥ Clean | Designed register helps comprehension | Anchor is editorial-overdesigned for ad delivery; cut |

Full decision rules in `../Creative/Phase_1_Split_Test_Plan.md`.

### Reporting Add-On

Daily / 3-day / weekly cadence per §8 unchanged; add to existing reports:

- **Daily:** Anchored vs Clean impression share by placement (FB Feed / IG Feed / IG Reels / IG Stories)
- **Every 3 days:** Anchored vs Clean CTR by placement; flag if Anchored CTR degrades >15% on FB Feed
- **Weekly:** Anchored vs Clean CPL by placement, hook rate, hold rate, cost per qualified lead — three-sentence summary for Robert
- **End of Week 1:** Validation against thresholds above; ship/refine/cut decision documented

---

## 7. Reallocation Triggers

### Architecture Hot-Swap (Single-Ad-Set → Two-Ad-Set Contingency)

The 2026-04-22 decision was to run one campaign / one ad set with all 6 creatives. This holds as long as motorcycle creative gets fair impression share from the algorithm. If it doesn't, we hot-swap to the two-ad-set architecture.

| Trigger | Condition | Action | Budget impact |
|---------|-----------|--------|---------------|
| **Motorcycle impression-share collapse** | M1/M2/M3 collectively hold <15% of ad set impressions at end of Day 7 | **Hot-swap:** split motorcycle into its own ad set at $45/day (~$1,500 remaining budget). Severe-injury ad set at $180/day (~$6,050 remaining). Preserves motorcycle reach at the cost of fragmenting learning. | Moves ~$1,500 into dedicated motorcycle ad set |
| **Motorcycle outperforms everything else** | Motorcycle CPL is <50% of average non-motorcycle CPL after 5+ motorcycle leads | Let the algorithm keep allocating. This is the win case — no action needed. Document for Phase 2 scale. | None |
| **Motorcycle completely fails** | Zero delivered leads from M1/M2/M3 after $1,500 spent on motorcycle creative (as estimated by impression share × total spend) | Pause M1/M2/M3. Redirect remaining spend to the 3 severe-injury creatives. Note lesson for Phase 2 (maybe motorcycle needs CA-specific casting, not AZ generic). | Full motorcycle remainder to severe-injury |
| **Severe Injury completely fails** | Zero delivered leads from S1/S2/S5 after $2,500 spend | Emergency pause. Full campaign audit. This should not happen given the audience size. If it does, the problem is funnel/tech, not media. | N/A — diagnose root cause |

### Creative Reallocation Within the Ad Set

The ad set has 6 creative variants. The algorithm distributes impressions across them. If the distribution becomes lopsided:

| Trigger | Condition | Action |
|---------|-----------|--------|
| **One case type dominates impressions at the expense of others** | Any one case-type creative (e.g., all trucking) consumes >50% of ad set impressions AND other case types have produced zero leads | Manually pause the dominant creative for 48 hours to force the algorithm to explore other variants. Reactivate after the pause. |
| **One creative consumes >60% of budget with mediocre CPL** | Single creative has majority of spend but CPL is at or above campaign average | The algorithm is stuck in a local optimum. Pause that creative for 48 hours to force exploration. Reactivate. |
| **Specific case-type produces zero leads by Week 2** | Any of {motorcycle / trucking / pedestrian / MVA} has zero delivered leads at end of Week 2 | Pause that case-type's creative. Creative-to-funnel handoff is broken OR audience for that case-type isn't there. Document for Phase 2 planning. |

### Emergency Creative Refresh Trigger

| Trigger | When | Action |
|---------|------|--------|
| Total campaign CPL trending >$500 by Week 3 | After 50% of media spend is consumed | Pause lowest 2-3 performers. Launch 2-3 new creative variants developed during Phase 1-2 monitoring. New creatives should iterate on the winning hooks (same emotional angle, different visual/copy execution). Budget: use reserve funds or pull from creative production budget. |
| CTR declining week-over-week on top performer for 2 consecutive weeks | Week 3+ | Creative fatigue. The top performer is wearing out. Launch a variant that uses the same hook with fresh visual treatment. Do not pause the original -- let the algorithm decide which performs better. |

---

## 8. Reporting Cadence

### Daily Monitoring (Alex)

| Metric | Where to Check | Flag If |
|--------|---------------|---------|
| Spend pacing | Meta Ads Manager → Campaign level | >120% or <70% of daily plan |
| CPL | Meta Ads Manager + lead delivery log | >$500 per lead on a rolling 3-day basis |
| CTR by creative | Meta Ads Manager → Ad level | Any creative <0.8% after 1,000 impressions |
| Lead delivery count | Email to Robert + dashboard | Leads not delivered within 15 minutes of quiz completion |
| Campaign status | Meta Ads Manager | Any campaign/ad set/ad in "Rejected" or "Not Delivering" status |

### Every 3 Days — Creative Performance Review (Davis + Alex)

| Deliverable | Detail |
|-------------|--------|
| Creative performance ranking | Rank all active creatives by: CTR, CPC, quiz start rate, delivered leads, CPL. Identify top 3 and bottom 3. |
| Kill/scale decisions | Execute kill criteria from Section 6. Pause underperformers. Document why. |
| Budget reallocation check | Assess if any reallocation triggers from Section 7 are met. Execute if so. |
| Funnel health check | Review quiz start rate, completion rate, non-soft-tissue pass rate. Flag if any are below thresholds. |

### Weekly — Full Performance Review (Davis + Alex + Sasha)

| Deliverable | Detail |
|-------------|--------|
| Weekly performance summary | Total spend, total leads, CPL, CTR, CPC, quiz conversion rates, lead grade distribution. Week-over-week trend. |
| Robert status update | Concise summary for Robert: leads delivered this week, cumulative leads, CPL trend (improving/stable/degrading), any quality concerns. Tone: professional, data-driven, forward-looking. |
| Budget reallocation memo | If any budget shifts were made or are proposed, document rationale. |
| Creative pipeline | Status of any new creative variants in development. Estimated delivery date. |
| Funnel optimization notes | Any quiz changes made or proposed. A/B test results if running. |

### Bi-Weekly — ROAS & Quality Assessment (Davis, delivered to Robert)

| Deliverable | Detail |
|-------------|--------|
| ROAS projection update | Based on leads delivered, estimated case values by type, projected sign rate (using whatever early signal Robert provides), calculate projected ROAS for the campaign. |
| Cohort quality assessment | Breakdown of delivered leads by: case type, injury severity, recency of accident, Fit Score/Grade distribution. Are we delivering the right mix? |
| Phase 2 recommendation | By the bi-weekly check in Week 4, provide a preliminary recommendation on whether to scale, hold, or adjust the Phase 2 proposal. |

### Reporting Tools & Access

| Tool | Purpose | Who Has Access |
|------|---------|---------------|
| Meta Ads Manager | Campaign performance, creative metrics, audience insights | Davis, Alex, Sasha |
| Lead delivery dashboard | Real-time lead count, grade distribution, delivery status | Davis, Alex, Robert (read-only) |
| Lead delivery email log | Individual lead records sent to Robert's team | Robert's designated email |
| Google Sheets / tracking doc | Weekly summary, cumulative metrics, budget pacing | Davis, Alex, Sasha |

---

## 9. Lead Delivery Workflow

### End-to-End Flow: Ad Impression to Lead Delivery

```
Step 1: USER SEES AD
├── User scrolling Facebook/Instagram
├── Sees one of our 6 Phase 1 creative variants
└── Clicks CTA ("Find out what your case is worth" / "Take the 60-second quiz")

Step 2: LANDING PAGE
├── User lands on quiz funnel page
├── Meta Pixel fires: Landing Page View (optimization event)
├── Page displays: headline, trust badges, quiz CTA, TCPA consent language
└── User clicks "Start Quiz" → QuizStart event fires

Step 3: QUIZ FUNNEL (6-8 steps)
├── Step 1: What type of accident? (motorcycle / truck / pedestrian / other MVA)
│   → ViewContent event fires
├── Step 2: When did the accident happen? (<1 month / 1-6 months / 6-12 months / 1-2 years / 2+ years)
│   → 2+ years = screen out (statute of limitations)
├── Step 3: How serious were your injuries? (broken bones/surgery/hospital stay / soft tissue / unsure)
│   → Soft tissue = screen out with polite redirect
│   → InjuryFilterPass event fires for non-soft-tissue
├── Step 4: Do you already have an attorney? (Yes / No / Not sure)
│   → Yes = screen out
├── Step 5: Were you at fault? (No / Partially / Yes / Not sure)
│   → Yes = screen out
├── Step 6: Contact information (name, phone, email)
│   → TCPA 1-to-1 consent displayed: "By submitting, you consent to be contacted
│     by West Coast Trial Lawyers regarding your potential case."
│   → User submits → Lead event fires
└── Step 7: Confirmation page
    → "Thank you. A representative from West Coast Trial Lawyers will contact you
       within 15 minutes during business hours."

Step 4: LEAD SCORING (automated, <60 seconds)
├── Fit Score calculated:
│   - Accident type weight (trucking = highest, general MVA = lowest)
│   - Injury severity weight (surgery/hospital > broken bones > other)
│   - Recency weight (< 6 months > 6-12 months > 12-24 months)
│   - Fault assessment weight (not at fault > partially > unsure)
├── Quality Score calculated:
│   - Valid phone number (format check + carrier lookup)
│   - Valid email (format check + deliverability)
│   - No duplicate (cross-check against previous submissions)
│   - Geographic check (AZ area code or AZ IP)
├── Grade assigned: A / B / C / D
│   - A: High Fit + High Quality (trucking/motorcycle, recent, not at fault, verified contact)
│   - B: Good Fit + Good Quality
│   - C: Moderate Fit or Quality concern
│   - D: Low Fit or Quality issue — review before delivery
└── D-grade leads held for manual review. A/B/C delivered automatically.

Step 5: LEAD DELIVERY (within 15 minutes of quiz completion)
├── Email sent to Robert's designated email address containing:
│   - Lead name
│   - Phone number
│   - Email address
│   - Accident type (motorcycle / truck / pedestrian / MVA)
│   - Injury description (from quiz responses)
│   - Accident recency
│   - Fault assessment
│   - Fit Score (numeric)
│   - Grade (A/B/C/D)
│   - TCPA consent timestamp + IP address + consent language version
│   - UTM parameters (which campaign, ad set, and creative generated this lead)
├── Dashboard updated in real-time
└── CompleteRegistration pixel event fires

Step 6: ROBERT'S TEAM FOLLOW-UP (their process, not ours)
├── Robert's team receives the lead
├── 7-day multi-channel follow-up process (their existing SOP):
│   - Call within 15 minutes of lead delivery (business hours)
│   - Text within 30 minutes
│   - Email within 1 hour
│   - Follow-up sequence over 7 days
├── Sign or decline the case
└── We track: consultation rate, sign rate (if Robert shares this data)
```

### Delivery SLA

| Metric | Target |
|--------|--------|
| Time from quiz completion to email delivery | <15 minutes (business hours), <1 hour (after hours) |
| Lead accuracy (valid contact info) | >90% |
| TCPA consent documentation included | 100% -- every lead |
| Grade A/B leads as % of total delivered | >60% |
| Dashboard update latency | Real-time (within 2 minutes of delivery) |

### What We Do NOT Do

- We do not call leads. Robert's team does all follow-up.
- We do not guarantee sign rates. We deliver qualified, consented leads. Conversion is Robert's team's responsibility.
- We do not deliver soft-tissue leads under this campaign. If a soft-tissue lead somehow passes the quiz filters (user misrepresented injury), we flag it and do not charge. It is not a delivered lead.
- We do not share raw lead data with anyone other than Robert's designated recipient. TCPA consent names West Coast Trial Lawyers specifically.

---

## 10. Phase 2 Expansion Triggers

### What Success Looks Like

| Metric | Threshold for Phase 2 Proposal | What It Signals |
|--------|-------------------------------|----------------|
| **Total delivered leads** | 20+ within $10K budget | Funnel works. Media economics are viable. |
| **Sign-worthy leads** | 3-4+ leads that Robert's team considers sign-worthy (regardless of actual sign) | Lead quality is sufficient. The quiz is filtering correctly. |
| **CPL trend** | CPL declining week-over-week from Week 2 onward | Algorithm is learning and improving. More budget = better performance. |
| **Sign rate** | 12-15%+ of delivered leads (if Robert reports this) | Leads are converting. Pipeline value is real. |
| **Robert satisfaction** | Robert expresses interest in continuing or scaling | Client relationship is intact. |

### Phase 2 Proposal Parameters

**Trigger:** If pilot delivers 3-4+ sign-worthy leads within $10K.

**Phase 2 budget:** $25,000 - $50,000 over 8-12 weeks.

**Phase 2 additions:**

| Channel | Budget Allocation | Rationale |
|---------|------------------|-----------|
| **Meta scale-up** | 60-70% of Phase 2 media | Proven channel. Scale winning creatives. Add new creative variants. Shift optimization event to quiz completions (volume now supports it). |
| **YouTube pre-roll** | 15-20% of Phase 2 media | Motorcycle content targeting (ride videos, gear reviews). Contextual alignment is strongest on YouTube. Search intent targeting for PI-related Google queries. |
| **Programmatic geofencing** | 10-15% of Phase 2 media | Hospital/ER geofencing in Maricopa and Pima counties. High-intent audience. Hospital clicks are 3.1x more likely to convert. Sasha builds the DSP infrastructure during the pilot so it is ready for Phase 2. |
| **Expanded creative** | Separate line item | Testimonial videos (if WCTL provides client testimonials), longer-form story ads, carousel ads testing on Meta, YouTube pre-roll scripts (5-second hook critical). |

**Phase 2 states:**
1. **Arizona scale-up first.** Prove the model at $25K-$50K in AZ before expanding geographically.
2. **Washington second.** WCTL operates in WA. Apply AZ learnings to WA campaign. Different state = different accident data, different CPMs, different competitive landscape. WA requires its own pilot phase (could be smaller -- $10K-$15K -- since creative and funnel templates transfer).

### Phase 2 Timeline

| Week | Milestone |
|------|-----------|
| Pilot Week 5 | Final performance data in. Phase 2 recommendation drafted. |
| Pilot + 1 week | Phase 2 proposal presented to Robert. |
| Pilot + 2-3 weeks | Phase 2 contract signed (if approved). YouTube and programmatic setup begins. |
| Phase 2 Week 1 | Meta scale-up launches with increased budget. YouTube pilot creative in production. |
| Phase 2 Week 3 | YouTube pre-roll goes live. Programmatic geofencing goes live. |
| Phase 2 Week 8-12 | Phase 2 performance review. Washington expansion decision. |

---

## 11. Risk Mitigation

| # | Risk | Probability | Impact | Mitigation |
|---|------|------------|--------|------------|
| 1 | **Pixel learning takes longer than expected.** Algorithm doesn't settle into efficient delivery by Week 2. | Medium | CPL stays elevated through Phase 2. Fewer total leads (15-18 instead of target 21). | Optimize for landing page views (highest event volume). Do not touch campaigns in first 5 days. Patience through Week 2 -- this is the expected cost of learning. If still elevated by Week 3, execute creative refresh. |
| 2 | **Soft-tissue clicks eating budget.** Ads attract fender-bender victims who click, start the quiz, and are filtered out -- wasting media spend. | Medium | Non-soft-tissue pass rate drops below 15% (calibrated target, Register 6.3), reducing delivered leads. Media cost per qualified lead rises. | Strong creative self-qualification: copy must emphasize "broken bones, surgery, hospital stay" explicitly. Quiz screens out soft tissue at Step 3. Monitor non-ST pass rate weekly. **If <10% of completions** (matches §6 kill threshold), revise creative copy + quiz Step 3 to be more exclusive. |
| 3 | **Low quiz completion rate.** Users start the quiz but abandon before submitting contact info. | Medium | Fewer leads per click. CPL rises. | A/B test quiz length: 8 steps vs. 5 steps. Test adding a progress bar ("Step 3 of 6 -- almost done"). Identify which step has highest drop-off and simplify. Reduce required fields. Test mobile optimization (majority of Meta traffic is mobile). |
| 4 | **Robert unhappy with early results.** Week 1-2 CPL is high, lead volume is low. Robert questions the investment. | Low-Medium | Client churn risk. Reputational damage to Second Chair. | **Set expectations upfront before launch.** Email to Robert: "The first 25% of spend ($2,500) will produce the fewest leads at the highest cost. This is the algorithm learning. By Week 3, CPL will drop significantly. We'll send weekly updates showing the improving trend." Weekly updates must show the trajectory, not just the snapshot. |
| 5 | **Creative fatigue after Week 3.** Top-performing creatives see declining CTR as the same users see them repeatedly. | Low-Medium | CPL rises in Phase 3. Final lead count comes in at 15-18 instead of target 21. | Have Week 2 rotation creatives (M4-M6, S6-S8) ready by end of Week 1 (produced during the campaign, not before launch). Iterate on winning hooks with new visuals/copy, not new concepts. Monitor frequency metric — Simon's `Media_Buying_Systems.md` threshold: rotate when frequency >3.0 (cold) or >5.0 (retargeting). |
| 6 | **Meta account issues.** Ad creatives rejected for policy violations. Account flagged or restricted. | Low | Campaign delayed or paused. Lost days = lost budget efficiency (calendar time wasted). | Submit all creatives for review 48 hours before intended launch date. Ensure all copy complies with Special Ad Category guidelines (no guarantees, no implied results, no before/after claims). Have backup Meta Business Manager account provisioned. Keep TCPA consent language approved by counsel. |
| 7 | **Lead quality dispute.** Robert claims delivered leads are not qualified (wrong injury type, already represented, etc.). | Low | Trust erosion. Potential refund request. | Every lead includes full quiz response data, TCPA consent proof, and Fit Score. If Robert disputes a lead, review the quiz data. If the lead legitimately misrepresented their situation in the quiz, replace the lead at no charge. If the lead is accurate but Robert's team failed to convert, that is a follow-up execution issue, not a lead quality issue. Document the difference upfront. |
| 8 | **Competitive surge.** Another PI firm launches a large Meta campaign in AZ during our pilot, driving up CPMs. | Low | CPMs rise from $35-50 to $50-70. Budget buys fewer impressions. Leads drop to 14-17. | We cannot control competitor behavior. If CPMs spike: (a) check if it's temporary (competitor may be running a short burst), (b) shift more budget to Instagram Reels/Stories placements (typically lower CPMs), (c) extend campaign to 6 weeks at lower daily spend to ride out the spike. |

---

## Appendix: Pre-Launch Checklist

Complete before campaign goes live.

| # | Task | Owner | Status |
|---|------|-------|--------|
| 1 | Meta Business Manager verified and in good standing | Alex | [ ] |
| 2 | Meta Pixel installed on all quiz funnel pages and firing correctly | Alex / Dev | [ ] |
| 3 | All pixel events tested (LPV, QuizStart, ViewContent, Lead, CompleteRegistration, InjuryFilterPass) | Alex / Dev | [ ] |
| 4 | Quiz funnel live and tested end-to-end (mobile + desktop) | Alex | [ ] |
| 5 | TCPA consent language reviewed and approved | Davis / Counsel | [ ] |
| 6 | Lead scoring system configured (Fit Score + Quality Score + Grade) | Alex / Dev | [ ] |
| 7 | Lead delivery email template built and tested | Alex | [ ] |
| 8 | Robert's designated email confirmed | Davis | [ ] |
| 9 | Dashboard access provisioned for Robert (read-only) | Alex | [ ] |
| 10 | All 6 Phase 1 creative variants produced and uploaded to Ads Manager (M1, M2, M3, S1, S2, S5). Week 2 rotation variants in development — not required for Day 1 launch. | Creative team | [ ] |
| 11 | All creatives submitted for Meta review (48 hrs before launch) | Alex | [ ] |
| 12 | Campaigns structured per Section 2 (3 campaigns, correct budgets, correct objectives) | Alex | [ ] |
| 13 | Special Ad Category set to "Social Issues" on all campaigns | Alex | [ ] |
| 14 | Geographic targeting confirmed: Arizona statewide | Alex | [ ] |
| 15 | Placements set to Advantage+ on all ad sets | Alex | [ ] |
| 16 | Daily budgets set per Week 1 schedule (Section 4) | Alex | [ ] |
| 17 | Retargeting campaign built but paused (ready to activate Week 3-4) | Alex | [ ] |
| 18 | Expectations email sent to Robert (CPL trajectory, reporting cadence, timeline) | Davis | [ ] |
| 19 | Reporting Google Sheet created with weekly template | Alex | [ ] |
| 20 | Backup creative variants in development for Week 3 refresh | Creative team | [ ] |

---

## Appendix: Key Numbers Reference Card

Print this. Tape it to the monitor. These are the numbers that govern every decision.

| Metric | Target | Alarm |
|--------|--------|-------|
| Total media budget | $7,750 (Meta only) | -- |
| Campaign duration | 5 weeks | Extend to 6 if underspending |
| Total delivered leads | 21 (range 18-24) | <15 by Week 4 = emergency review |
| CPL (media cost per delivered lead) | $337-$517 | >$600 sustained = restructure |
| CTR (creative level) | >1.0% | <0.8% = pause creative |
| CPC | $3.50-$5.00 | >$6.00 = pause creative |
| Quiz start rate (from LPV) | **60% calibrated** (Register 6.1) | **<45% = revise landing page** |
| Quiz completion rate (from start) | **40% calibrated** (Register 6.2) | **<30% = revise quiz flow** |
| Non-soft-tissue pass rate | **15% calibrated** (Register 6.3) | **<10% = revise creative + quiz Step 3** |
| Ad set daily budget (Phase 1) | ~$220/day (single ad set) | -- |
| Expected motorcycle impression share | 20-30% | <15% after Week 1 = hot-swap trigger (see §2) |
| Retargeting activation | **End of Week 2** (day 10-12) | Need 200+ in 7-day custom audience |
| First optimization decision | Day 7 | Do not touch before Day 5 |
| Phase 2 trigger | 3-4+ sign-worthy leads | -- |

---

*Second Chair x West Coast Trial Lawyers -- Media Plan & Budget Allocation -- April 2026*
*Lead Agents: Simon Croft (Media Buying) + Depesh Mandali (Meta Campaign Structure)*
*This document is the operational execution plan. Work from this on launch day.*
