# Media Plan & Budget Allocation
## Arizona Non-Soft-Tissue PI Pilot Campaign — $10K

**Prepared:** April 13, 2026
**Lead Agents:** Simon Croft (Head of Media Buying — Budget Allocation) + Depesh Mandali (Meta Campaign Structure — OCEAN Framework)
**Campaign:** Second Chair x West Coast Trial Lawyers — $10K Arizona Pilot
**Status:** Executable media plan. This is the document the team works from on launch day.
**Platform:** 100% Meta (Facebook + Instagram via Advantage+ placements)

**Upstream documents:**
- Doc 1: AZ Non-Soft-Tissue Demographics
- Doc 2: Case Type Personas
- Doc 3: Audience Sizing by Case Type — Ad Set Architecture Decision
- Doc 4: Platform Behavior & Advertising Reach Analysis

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

**Total client payment:** $10,000

| Line Item | Amount | % of Total | Notes |
|-----------|--------|-----------|-------|
| **Media — Meta (FB+IG)** | $6,250 | 62.5% | Primary lead gen engine. Facebook + Instagram via Advantage+ placements. |
| **Media — Geofencing** | $625 | 6.25% | Hospitals, trauma centers, orthopedic offices, collision repair shops. Sasha leads DSP setup. Launches Week 2-3. |
| **Media — TikTok test** | $625 | 6.25% | 2-3 creatives adapted for platform. If ads pass review, continue. If rejected, reallocate to Meta. |
| **Media — Reddit test** | $375 | 3.75% | r/phoenix, r/legaladvice, r/motorcycles, keyword targeting. Quiz funnel link. |
| **Creative production** | $875 | 8.75% | Video (UGC-style), static images, copy variants, Spanish-language assets, platform adaptations for TikTok/Reddit. |
| **Funnel / tech** | $500 | 5.0% | Quiz funnel hosting, pixel implementation, verification pipeline, TCPA compliance, geofencing DSP access. |
| **Second Chair margin** | $750 | 7.5% | Operating margin. |
| **Total** | **$10,000** | **100%** | |

**Total media spend across all channels: ~$7,875**

### What the Multi-Channel Media Spend Buys (Estimated)

**Meta (FB+IG) — $6,250:**

| Metric | Estimate | Source |
|--------|----------|--------|
| Impressions | ~125,000 - 179,000 | At $35-$50 CPM (AZ legal, Special Ad Category) |
| Unique reach (est. freq. 2.5) | ~50,000 - 72,000 | Impressions / 2.5 |
| Clicks | ~1,250 - 1,790 | At 1.0% CTR |
| Quiz starts | ~875 - 1,253 | 70% of clicks |
| Quiz completions | ~569 - 814 | 65% of starts |
| Pass injury filter | ~228 - 326 | 40% of completions |
| Delivered leads | **~16 - 18** | After verification |
| Cost per lead (media) | **~$350 - $390** | |

**Geofencing (Hospitals/Ortho/Body Shops) — $625:**

| Metric | Estimate | Source |
|--------|----------|--------|
| Impressions | ~42,000 - 78,000 | At $8-$15 CPM |
| Clicks | ~63 - 234 | At 0.15-0.30% CTR (display, but 3.1x hospital lift) |
| Quiz completions | ~12 - 47 | Higher intent than Meta — these people HAVE injuries |
| Delivered leads | **~1 - 3** | Pre-qualified by physical location |
| Cost per lead (media) | **~$208 - $625** | Potentially the cheapest leads in the campaign |

**TikTok Test — $625:**

| Metric | Estimate | Source |
|--------|----------|--------|
| Impressions | ~69,000 - 125,000 | At $5-$9 CPM (dramatically cheaper than Meta) |
| Clicks | ~417 - 1,250 | At 0.6-1.0% CTR |
| Quiz completions | ~42 - 125 | If ads pass review |
| Delivered leads | **~1 - 3** | IF ads run. $0 if rejected. |
| Cost per lead (media) | **~$208 - $625** | Could be the best CPL channel or produce nothing |

**Reddit Test — $375:**

| Metric | Estimate | Source |
|--------|----------|--------|
| Clicks | ~250 - 500 | At $0.75-$1.50 CPC |
| Quiz starts | ~100 - 300 | 40-60% start rate (high intent) |
| Quiz completions | ~40 - 120 | |
| Delivered leads | **~1 - 3** | Research-mode users, higher qualification rate |
| Cost per lead (media) | **~$125 - $375** | Potentially lowest CPL of any channel |

### Combined Expected Output

| Channel | Media Spend | Expected Leads | CPL Range |
|---------|-------------|----------------|-----------|
| Meta (FB+IG) | $6,250 | 16-18 | $350-$390 |
| Geofencing | $625 | 1-3 | $208-$625 |
| TikTok | $625 | 0-3 | $208-$625 (or $0 if rejected) |
| Reddit | $375 | 1-3 | $125-$375 |
| **Total** | **$7,875** | **~18-27** | **~$290-$440 blended** |

The multi-channel approach has a higher ceiling (up to 27 leads) than Meta-only (20-22) while maintaining the same floor (~18 leads if supplementary channels underperform). The supplementary channels are designed as optionality — if any channel fails, that budget reallocates to Meta with no structural damage to the campaign.

**Revenue math at $475/lead:** 21 leads × $475 = $9,975. At the ceiling of 27 leads, that's $12,825 — exceeding the $10K client payment and improving Second Chair's margin. The multi-channel approach turns a break-even pilot into a potentially profitable one.

---

## 2. Campaign Structure

### Meta Ads Manager Setup

All campaigns run under **Special Ad Category: Social Issues** (the required classification for legal advertising under Meta's policies). This locks targeting to broad -- no age, gender, interest, or behavioral narrowing. Arizona statewide. Creative does the targeting.

```
CAMPAIGN 1: WCTL-AZ-Motorcycle
├── Objective: Traffic (Landing Page Views)
├── Special Ad Category: Social Issues
├── Geographic Target: Arizona (statewide)
├── Audience: Broad (all adults, no narrowing — SAC restriction)
├── Placements: Advantage+ (Facebook Feed, Instagram Feed, Stories, Reels, Audience Network)
├── Budget: $1,938 total / ABO at $55/day (Phase 1)
│
└── Ad Set 1: AZ-Statewide-Broad-Motorcycle
    ├── Creative 1: Identity hook — Video (UGC style)
    │   "Arizona riders know the risk. After a crash, know your rights."
    │   Desert highway, rider POV, helmet/gear. 15-30 sec.
    │
    ├── Creative 2: Loss hook — Static image + text overlay
    │   "One ride changed everything. Find out what your case is worth."
    │   Motorcycle + open road, overlay text, warm tones.
    │
    ├── Creative 3: Injustice hook — Video
    │   "The driver said they didn't see you. Their insurance company says you're fine. You're not."
    │   Split-screen: rider's reality vs. insurance denial. 15-20 sec.
    │
    └── Creative 4: Identity hook — Static (Spanish variant)
        "Motociclistas de Arizona — despues del choque, conozca sus derechos."
        Same visual language as Creative 1, Spanish copy.


CAMPAIGN 2: WCTL-AZ-Severe-Injury
├── Objective: Traffic (Landing Page Views)
├── Special Ad Category: Social Issues
├── Geographic Target: Arizona (statewide)
├── Audience: Broad (all adults, no narrowing — SAC restriction)
├── Placements: Advantage+ (Facebook Feed, Instagram Feed, Stories, Reels, Audience Network)
├── Budget: $5,813 total / ABO at $165/day (Phase 1)
│
└── Ad Set 1: AZ-Statewide-Broad-Multi-Variant
    ├── Creative 1: Trucking — Anger/injustice hook — Video
    │   "Hit by a truck on Arizona's highways? Their insurance is $1M+."
    │   Semi on I-10, size contrast, David vs. Goliath framing. 15-30 sec.
    │
    ├── Creative 2: Trucking — Fact-driven — Static
    │   "Commercial trucks carry $1M+ insurance policies. If a truck hit you, find out what your case is worth."
    │   I-10 corridor imagery, stat overlay.
    │
    ├── Creative 3: Pedestrian (English) — Innocence hook — Video
    │   "Hit while crossing the street? You weren't the one driving."
    │   Crosswalk, nighttime urban intersection, vulnerability. 15-20 sec.
    │
    ├── Creative 4: Pedestrian (Spanish) — Family impact — Video
    │   "Le atropellaron cruzando la calle? Usted no era quien manejaba."
    │   Same visual language, Spanish copy. Targets Maryvale/South Phoenix
    │   (29% Spanish-primary households). 15-20 sec.
    │
    ├── Creative 5: DUI victim — Accountability hook — Static
    │   "A drunk driver changed your life. It's not too late to hold them accountable."
    │   Nighttime, headlights, injustice framing.
    │
    ├── Creative 6: General severe MVA — Financial crisis — Video
    │   "Seriously injured in an accident? Broken bones, surgery, mounting bills —
    │    find out what your case is worth."
    │   Hospital/recovery imagery, bills stacking, empathetic tone. 15-30 sec.
    │
    └── Creative 7: General severe MVA — Life disruption — Static
        "Your life stopped. The bills didn't. See what your injury case is worth — free, 60 seconds."
        Cast/crutches imagery, bills on table, warm direct tone.


CAMPAIGN 3: WCTL-AZ-Retargeting (Activates Week 4 if pixel has sufficient data)
├── Objective: Traffic (Landing Page Views)
├── Special Ad Category: Social Issues
├── Geographic Target: Arizona (statewide)
├── Audience: Custom — Website visitors, 7-day window
├── Placements: Advantage+
├── Budget: $0 initially, up to $24/day from Phase 3 reallocation
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

### Why Two Campaigns Instead of One

Doc 3 established that 2 ad sets is the optimal architecture at this budget. The question is whether those 2 ad sets live in one campaign or two.

**Two separate campaigns** because:

1. **Budget control.** With separate campaigns, the 25/75 budget split between Motorcycle and Severe Injury is locked. If they shared a campaign under CBO (Campaign Budget Optimization), Meta's algorithm would distribute budget based on cost-per-landing-page-view efficiency -- and motorcycle creative's higher CTR among riders could cannibalize budget from the larger severe injury pool, or vice versa. Separate campaigns let us control the split.

2. **Learning isolation.** Each campaign's pixel learning is independent. Motorcycle builds its own delivery model. Severe Injury builds its own. This prevents one category's performance from distorting the other's optimization.

3. **Cleaner reporting.** Motorcycle performance vs. Severe Injury performance is visible at the campaign level without drilling into ad set breakdowns.

### Why a Single Ad Set Per Campaign

At $7,750 total media, splitting either campaign into multiple ad sets would starve each one. Doc 3 showed that even a 2-ad-set architecture puts the Motorcycle set right at the 50 completions/week learning threshold. Adding more ad sets within either campaign would push sets below that threshold, wasting budget in perpetual learning.

Each campaign gets one ad set. Multiple creative variants within that single ad set let the algorithm test and distribute across case types (in Campaign 2) or across hooks (in Campaign 1). The algorithm does the segmentation with data. We provide the creative diversity.

---

## 3. Budget Allocation by Phase

### Phase 1: Testing (Weeks 1-2)

| Parameter | Value |
|-----------|-------|
| **Budget** | ~$3,100 (40% of $7,750 media) |
| **Daily spend** | ~$220/day |
| **Motorcycle daily** | $55/day (25%) |
| **Severe Injury daily** | $165/day (75%) |
| **Retargeting daily** | $0 |
| **Optimization** | ABO (Ad Set Budget Optimization) -- budgets fixed at ad set level |
| **Goal** | Find winning creatives. Let the algorithm through the learning phase. Gather baseline CTR, CPC, quiz start rate data. |

**What happens in Phase 1:**
- All 11 creative variants go live simultaneously (4 in Campaign 1, 7 in Campaign 2).
- Meta's algorithm distributes impressions across all creatives, testing which audience-creative pairings generate the most landing page views.
- **Do not touch anything for the first 5 days.** The algorithm needs uninterrupted data collection. Pausing/editing creatives during learning resets the learning phase.
- Day 5-7: First performance check. Identify which creatives are above/below CTR and CPC thresholds (see Section 6).
- Day 7: Execute first kill/keep decisions.
- Day 10-14: Second performance check. Monitor quiz start and completion rates. Identify funnel drop-off points.

**Expected Phase 1 output:**
- Impressions: ~30,000-44,000
- Clicks: ~300-440
- Quiz starts: ~210-310
- Delivered leads: **3-5** (higher CPL during learning -- this is expected and acceptable)
- Data: Clear creative performance ranking for both campaigns

### Phase 2: Optimization (Weeks 2-3)

| Parameter | Value |
|-----------|-------|
| **Budget** | ~$2,325 (30% of $7,750 media) |
| **Daily spend** | ~$165/day (but concentrated on fewer, winning creatives) |
| **Motorcycle daily** | $41/day |
| **Severe Injury daily** | $124/day |
| **Retargeting daily** | $0 |
| **Optimization** | Remains ABO. Shift to CBO only if one campaign has a clear runaway winner. |
| **Goal** | Scale winners. Kill losers. Improve CPL by concentrating spend on proven performers. |

**What happens in Phase 2:**
- Pause underperforming creatives (any creative that failed kill criteria in Phase 1).
- Remaining creatives get proportionally more budget -- the algorithm concentrates delivery on what works.
- If Campaign 2 has a dominant creative (e.g., trucking video is 3x the CTR of DUI static), consider shifting internal creative weight but do NOT add new ad sets.
- If Campaign 1 (Motorcycle) is dramatically outperforming Campaign 2: consider shifting 5-10% of budget from Severe Injury to Motorcycle (see Section 7 reallocation triggers).
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
| **Daily spend** | ~$115-$165/day (varies by week as budget tapers) |
| **Motorcycle daily** | $29-$41/day |
| **Severe Injury daily** | $75-$112/day |
| **Retargeting daily** | $12-$24/day (if pixel data supports it) |
| **Optimization** | ABO or CBO based on Phase 2 performance. Algorithm should be post-learning or near-exit. |
| **Goal** | Maximize delivery on proven winners. Harvest leads at lowest CPL. Launch retargeting if pixel has 500+ landing page views. |

**What happens in Phase 3:**
- Only winning creatives remain active (likely 2-3 in Campaign 1, 3-5 in Campaign 2).
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
| Testing | Weeks 1-2 | $3,100 | $220/day | 3-5 | ~$620-$1,033 |
| Optimization | Weeks 2-3 | $2,325 | $165/day | 7-9 | ~$258-$332 |
| Scale | Weeks 3-5 | $2,325 | $115-$165/day | 8-10 | ~$233-$291 |
| **Total** | **5 weeks** | **$7,750** | — | **~20-22** | **~$350-$390** |

The CPL trajectory is the story to tell Robert: Week 1 CPL will be ugly. That is the cost of the algorithm learning who converts. By Week 3-5, the CPL drops to a fraction of Week 1 because we killed losers and scaled winners. **First 25% of spend produces worst CPL. Last 25% produces best CPL.** Set this expectation upfront.

---

## 4. Daily Spend Schedule

### Week-by-Week Breakdown

| Week | Phase | Campaign 1: Motorcycle | Campaign 2: Severe Injury | Campaign 3: Retargeting | Total Daily | Weekly Total |
|------|-------|----------------------|--------------------------|------------------------|-------------|-------------|
| **1** | Testing | $55/day | $165/day | $0 | $220/day | $1,540 |
| **2** | Testing / Opt | $55/day | $165/day | $0 | $220/day | $1,540 |
| **3** | Optimization | $41/day | $124/day | $0 | $165/day | $1,155 |
| **4** | Scale | $35/day | $95/day | $12/day | $142/day | $994 |
| **5** | Scale | $30/day | $80/day | $12/day | $122/day | $854 |
| | | | | | | |
| **Totals** | | **$1,512** | **$4,403** | **$168** | | **$6,083** |

**Remaining buffer:** $7,750 - $6,083 = **$1,667 reserve.**

This reserve exists because:
1. Meta rarely spends exactly 100% of daily budget every day. Actual delivery typically runs 85-95% of set budget, especially during learning.
2. Weekend delivery often dips (lower scroll volume on Sundays).
3. The reserve provides flexibility for reallocation if a creative breaks out and warrants a budget increase mid-campaign.

**How to deploy the reserve:**
- If Campaign 1 or 2 is pacing under budget, increase daily caps by 10-15% in Weeks 3-5 to ensure full spend.
- If a creative is a clear winner by Week 3, allocate reserve as additional daily budget on that campaign.
- If the campaign is pacing to underspend by >$500 at Week 4, extend to Week 6 at the same daily rates rather than increasing daily spend.
- **Do not front-load the reserve into Weeks 1-2.** The algorithm is still learning; more money during learning = more money spent inefficiently.

### Budget Accounting Check

| Item | Amount |
|------|--------|
| Scheduled media (5 weeks) | $6,083 |
| Reserve / flex | $1,667 |
| **Total media budget** | **$7,750** |
| Creative production | $1,000 |
| Funnel / tech | $500 |
| Margin | $750 |
| **Total campaign budget** | **$10,000** |

---

## 5. Optimization Events & Pixel Setup

### Primary Optimization Event: Landing Page Views

**Why landing page views -- not quiz completions, not lead submissions.**

| Optimization Event | Expected Weekly Volume (Whole Campaign) | vs. 50/week Threshold | Verdict |
|-------------------|----------------------------------------|----------------------|---------|
| Lead submissions (delivered) | ~4/week | 0.08x | Impossible. Algorithm has no signal to learn from. |
| Quiz completions | ~140-200/week | 2.8-4.0x campaign level, but only ~50/week for Motorcycle ad set | Marginal for Motorcycle. Risky. |
| Quiz starts | ~215-310/week | 4.3-6.2x | Safe, but still mid-funnel. |
| **Landing page views** | **~310-440/week** | **6.2-8.8x** | **Best option. Maximizes signal density while keeping event relevant to intent.** |
| Link clicks | ~310-440/week | Similar to LPV | Counts bounces. Landing page views are clicks that actually loaded the page -- higher quality signal. |

At ~$7,750 spend across 5 weeks, we get ~1,550-2,210 total clicks but only ~20-22 delivered leads. That is ~4 leads per week -- not even 10% of Meta's 50/week learning threshold. Even quiz completions, at ~200/week across the whole campaign, only give the Motorcycle ad set ~50/week (right at the edge).

**Landing page views (~310-440/week total, ~78-110/week for Motorcycle) give both ad sets comfortable clearance above the learning threshold.** The algorithm learns which impressions produce page loads, and the quiz itself filters from there.

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

**Minimum audience size for retargeting:** Meta requires ~200 people in a custom audience before it can serve ads. At ~300-440 clicks/week, the 7-day website visitor audience should hit 200 by end of Week 2, making Campaign 3 activatable by Week 3-4.

---

## 6. Kill Criteria & Reallocation Rules

### Creative-Level Kill Criteria

| Metric | Threshold | Action | When to Check | Rationale |
|--------|-----------|--------|---------------|-----------|
| **CTR** | <0.8% after 1,000 impressions | Pause creative | Day 5-7 | Below 0.8% CTR means the creative is not resonating. At $35-50 CPM, a 0.8% CTR produces $4.38-$6.25 CPC -- at the high end of acceptable. Below that, CPC is unsustainable. |
| **CPC** | >$6.00 sustained over 3 days | Pause creative | Day 7+ | $6.00 CPC means $7,750 buys only ~1,292 clicks. At our funnel rates, that produces ~14 delivered leads -- below the 20-22 target. |
| **CTR + zero quiz starts** | <1.0% CTR AND zero quiz starts after 500 impressions | Pause creative immediately | Day 3-5 | Creative is attracting curiosity clicks that don't convert. The creative-to-funnel handoff is broken. |
| **Frequency** | >4.0 on any creative | Rotate or pause | Week 3+ | Creative fatigue. The same people are seeing the same ad too many times. Performance will degrade. |

### Funnel-Level Kill Criteria

| Metric | Threshold | Action | When to Check | Rationale |
|--------|-----------|--------|---------------|-----------|
| **Quiz start rate** | <20% of landing page views after 100 LPVs | Revise landing page | Day 7-10 | If fewer than 1 in 5 people who land on the page start the quiz, the page is not compelling enough. Test: simplify headline, make quiz CTA more prominent, reduce page load time. |
| **Quiz completion rate** | <15% of starts after 50 starts | Revise quiz flow | Day 10-14 | If fewer than 1 in 6 quiz starters finish, the quiz is too long, too confusing, or asks a question that causes drop-off. Test: reduce from 8 steps to 5. Test: add progress bar. Test: identify which step has highest drop-off and simplify it. |
| **Non-soft-tissue pass rate** | <25% of completions after 50 completions | Investigate creative targeting | Day 14+ | If more than 75% of quiz completers are soft-tissue, the creative is not self-qualifying strongly enough. The ads are attracting fender-bender victims instead of serious injury cases. Revise creative copy to emphasize "broken bones, surgery, hospital stay" more explicitly. |

### Campaign-Level Kill Criteria

| Metric | Threshold | Action | When to Check | Rationale |
|--------|-----------|--------|---------------|-----------|
| **CPL (cost per delivered lead)** | >$600 after 10 delivered leads | Restructure campaign | Week 3 | At $600/lead, $7,750 media produces only ~13 leads. Below the 20-22 target and below profitability. Options: emergency creative refresh, quiz redesign, or consider consolidating to 1 campaign (merge motorcycle into severe injury). |
| **Any ad set with zero delivered leads** | After $500 spend in that ad set | Pause ad set, investigate | Rolling | $500 with zero leads means the creative-to-lead pipeline is broken for that case type. Do not keep spending. Investigate: Is the quiz routing working? Are leads failing verification? Is the creative attracting the wrong audience? |
| **Campaign spend pacing >120% of schedule** | More than 20% ahead of daily budget plan | Reduce daily budgets | Weekly check | Meta sometimes overspends daily budgets by up to 25%. If this is consistent, the campaign will exhaust budget before Week 5. Reduce daily caps to bring pacing back to plan. |
| **Campaign spend pacing <70% of schedule** | More than 30% under daily budget plan | Investigate delivery issues | Day 3-5 | Under-delivery means Meta cannot find enough people to serve ads to at your bid/budget. Check: Is the campaign flagged for Special Ad Category review? Is the creative rejected? Is the audience too narrow (it shouldn't be -- we're targeting all of AZ)? |

### The 5-Day Rule

**Do not make any optimization decisions in the first 5 days of any new creative or ad set.** The algorithm is in its initial exploration phase. Early data is noisy and unrepresentative. A creative that looks terrible on Day 2 may be the best performer by Day 7 once the algorithm finds its audience.

Exception: If a creative is rejected by Meta's ad review, address immediately. Do not wait 5 days for a rejected ad.

---

## 7. Reallocation Triggers

### Budget Reallocation Between Campaigns

| Trigger | Condition | Action | Maximum Shift |
|---------|-----------|--------|---------------|
| **Motorcycle outperforms Severe Injury** | Motorcycle CPL is <50% of Severe Injury CPL after 5+ leads each | Shift budget to 35% Motorcycle / 65% Severe Injury | 10% shift ($775) |
| **Motorcycle underperforms** | Motorcycle CPL is >2x Severe Injury CPL after $1,000 spend | Shift budget to 15% Motorcycle / 85% Severe Injury | 10% shift ($775) |
| **Motorcycle completely fails** | Zero delivered leads from Motorcycle after $1,200 spend (>60% of its budget) | Pause Campaign 1. Move remaining motorcycle budget to Campaign 2. Add motorcycle-style creative as a new variant in Campaign 2's ad set. | Full reallocation of remaining motorcycle budget |
| **Severe Injury completely fails** | Zero delivered leads after $2,500 spend | Emergency pause. Full campaign audit. This should not happen given the audience size. If it does, the problem is funnel/tech, not media. | N/A -- diagnose root cause |

### Creative Reallocation Within Campaign 2

Campaign 2 has 7 creative variants covering trucking, pedestrian (EN/ES), DUI, and general severe MVA. The algorithm distributes impressions across them. If the distribution becomes lopsided:

| Trigger | Condition | Action |
|---------|-----------|--------|
| **Spanish creative underdelivering** | Spanish variants receive <10% of Campaign 2 impressions after 10 days | Option A: Duplicate the Spanish creative as a new variant with slightly different headline to give it a fresh start. Option B: If budget allows, create a small separate ad set ($5/day minimum) exclusively for Spanish creative to force exposure. |
| **Trucking creative dominates** | Trucking variants consume >50% of Campaign 2 impressions AND deliver lowest CPL | This is a good problem. Let it run. But monitor: if trucking dominates AND general severe/pedestrian/DUI variants are producing zero leads, the algorithm may be over-concentrating. Manually pause the dominant trucking creative for 48 hours to force redistribution, then reactivate. |
| **One creative consumes >60% of budget with mediocre CPL** | Single creative has majority of spend but CPL is at or above campaign average | The algorithm is stuck in a local optimum. Pause that creative for 48 hours to force the algorithm to explore other variants. Reactivate after the pause. |
| **All non-trucking creatives underperform** | By Week 3, trucking is the only case type producing leads in Campaign 2 | Consider splitting trucking into its own campaign (3 campaigns total). This is the one scenario where adding a third campaign may be justified -- but only if the remaining budget per campaign stays above $500. |

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
├── Sees one of our 11 creative variants
└── Clicks CTA ("Find out what your case is worth" / "Take the 60-second quiz")

Step 2: LANDING PAGE
├── User lands on quiz funnel page
├── Meta Pixel fires: Landing Page View (optimization event)
├── Page displays: headline, trust badges, quiz CTA, TCPA consent language
└── User clicks "Start Quiz" → QuizStart event fires

Step 3: QUIZ FUNNEL (6-8 steps)
├── Step 1: What type of accident? (motorcycle / truck / pedestrian / DUI / other MVA)
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
│   - Accident type (motorcycle / truck / pedestrian / DUI / MVA)
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
| 1 | **Pixel learning takes longer than expected.** Algorithm doesn't settle into efficient delivery by Week 2. | Medium | CPL stays elevated through Phase 2. Fewer total leads (16-18 instead of 20-22). | Optimize for landing page views (highest event volume). Do not touch campaigns in first 5 days. Patience through Week 2 -- this is the expected cost of learning. If still elevated by Week 3, execute creative refresh. |
| 2 | **Soft-tissue clicks eating budget.** Ads attract fender-bender victims who click, start the quiz, and are filtered out -- wasting media spend. | Medium | Non-soft-tissue pass rate drops below 40%, reducing delivered leads. Media cost per qualified lead rises. | Strong creative self-qualification: copy must emphasize "broken bones, surgery, hospital stay" explicitly. Quiz screens out soft tissue at Step 3. Monitor non-ST pass rate weekly. If <25%, revise creative copy to be more exclusive. |
| 3 | **Low quiz completion rate.** Users start the quiz but abandon before submitting contact info. | Medium | Fewer leads per click. CPL rises. | A/B test quiz length: 8 steps vs. 5 steps. Test adding a progress bar ("Step 3 of 6 -- almost done"). Identify which step has highest drop-off and simplify. Reduce required fields. Test mobile optimization (majority of Meta traffic is mobile). |
| 4 | **Robert unhappy with early results.** Week 1-2 CPL is high, lead volume is low. Robert questions the investment. | Low-Medium | Client churn risk. Reputational damage to Second Chair. | **Set expectations upfront before launch.** Email to Robert: "The first 25% of spend ($2,500) will produce the fewest leads at the highest cost. This is the algorithm learning. By Week 3, CPL will drop significantly. We'll send weekly updates showing the improving trend." Weekly updates must show the trajectory, not just the snapshot. |
| 5 | **Creative fatigue after Week 3.** Top-performing creatives see declining CTR as the same users see them repeatedly. | Low-Medium | CPL rises in Phase 3. Final lead count comes in at 16-18 instead of 20-22. | Have 2-3 backup creative variants ready by Week 2 (produced during the campaign, not before launch). Iterate on winning hooks with new visuals/copy, not new concepts. Monitor frequency metric -- if >4.0, rotate. |
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
| 10 | All 11 creative variants produced and uploaded to Ads Manager | Creative team | [ ] |
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
| Total media budget | $7,750 | -- |
| Campaign duration | 5 weeks | Extend to 6 if underspending |
| Total delivered leads | 20-22 | <15 by Week 4 = emergency review |
| CPL (media cost per delivered lead) | $350-$390 | >$500 sustained = restructure |
| CTR (creative level) | >1.0% | <0.8% = pause creative |
| CPC | $3.50-$5.00 | >$6.00 = pause creative |
| Quiz start rate (from LPV) | 60-70% | <20% = revise landing page |
| Quiz completion rate (from start) | 55-65% | <15% = revise quiz flow |
| Non-soft-tissue pass rate | 35-45% | <25% = revise creative |
| Motorcycle daily budget (Phase 1) | $55/day | -- |
| Severe Injury daily budget (Phase 1) | $165/day | -- |
| Retargeting activation | Week 3-4 | Need 500+ LPVs in pixel first |
| First optimization decision | Day 7 | Do not touch before Day 5 |
| Phase 2 trigger | 3-4+ sign-worthy leads | -- |

---

*Second Chair x West Coast Trial Lawyers -- Media Plan & Budget Allocation -- April 2026*
*Lead Agents: Simon Croft (Media Buying) + Depesh Mandali (Meta Campaign Structure)*
*This document is the operational execution plan. Work from this on launch day.*
