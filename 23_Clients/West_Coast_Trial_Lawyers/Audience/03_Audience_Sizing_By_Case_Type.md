# Audience Sizing by Case Type — Ad Set Architecture Decision
## Arizona Non-Soft-Tissue PI Campaign

**Prepared:** April 13, 2026
**Lead Agents:** Julian Cole (Media Strategy) + Byron Sharp (Brand Growth Science)
**Campaign:** Second Chair x West Coast Trial Lawyers — $10K Arizona Pilot
**Status:** Internal strategy document — feeds directly into Creative Strategy (Doc 5)
**Key question:** Which case types are large enough for dedicated Meta ad sets, and which should be bundled?

---

## Table of Contents

1. [The Core Problem](#1-the-core-problem)
2. [How Meta's Algorithm Learns — Byron Sharp on Minimum Viable Signal](#2-how-metas-algorithm-learns)
3. [Arizona Incident Volume by Case Type](#3-arizona-incident-volume-by-case-type)
4. [Reachable Pipeline Sizing — Case-by-Case](#4-reachable-pipeline-sizing)
5. [Budget Math Per Ad Set — Three Architecture Options](#5-budget-math-per-ad-set)
6. [Option A: 3 Ad Sets (Detailed)](#6-option-a-3-ad-sets)
7. [Option B: 2 Ad Sets (Detailed)](#7-option-b-2-ad-sets)
8. [Option C: 1 Ad Set / Broad (Detailed)](#8-option-c-1-ad-set--broad)
9. [Head-to-Head Comparison](#9-head-to-head-comparison)
10. [Creative Distinctiveness Assessment](#10-creative-distinctiveness-assessment)
11. [Creative Production Cost Analysis](#11-creative-production-cost-analysis)
12. [Definitive Recommendation](#12-definitive-recommendation)
13. [Implementation Blueprint](#13-implementation-blueprint)

---

## 1. The Core Problem

We have $10,000 total budget. After margin, creative, and tech costs, approximately **$7,750 goes to Meta media spend**. We need to deliver ~21 qualified non-soft-tissue leads in 4-6 weeks across six distinct case types in Arizona.

The question is not whether any individual case type has a large enough *Meta audience* — under Special Ad Categories, we target all of Arizona (~4.1M Facebook adults). The audience is always the same: everyone in the state. What changes between ad sets is the **creative**, not the targeting.

The real question has three parts:

1. **Signal density:** Given the monthly incident volume per case type, will a case-type-specific ad set generate enough conversions for Meta's algorithm to learn which impressions lead to quiz completions?
2. **Creative distinctiveness:** Does this case type look and feel different enough from other case types that dedicated creative meaningfully improves self-qualification and conversion?
3. **Production economics:** Does the creative production cost of a dedicated ad set justify the expected lift over bundling it into a broader set?

Byron Sharp's principle applies here: **reach drives growth, and the algorithm needs sufficient signal density to find efficient reach.** A starved ad set doesn't just underperform — it actively wastes budget by spending through the learning phase without ever exiting it.

---

## 2. How Meta's Algorithm Learns

### The Learning Phase

Every new ad set enters Meta's "learning phase." During this period, the algorithm is testing different users, placements, and times to discover who converts. The learning phase ends when the ad set accumulates approximately **50 optimization events per week**.

**What counts as an "optimization event" depends on the campaign objective:**

| Objective | Optimization Event | Typical Threshold |
|-----------|-------------------|-------------------|
| Traffic (Link Clicks) | Link click | 50 clicks/week/ad set |
| Landing Page Views | Landing page view | 50 views/week/ad set |
| Conversions (Quiz Completion) | Quiz completion event | 50 completions/week/ad set |
| Conversions (Lead Submission) | Lead submission | 50 submissions/week/ad set |

**Critical insight:** If we optimize for the deepest funnel event (lead submission), we need 50 lead submissions per week per ad set. At our budget and volume, that is impossible for ANY case type — we expect ~21 total delivered leads over the entire campaign. Even optimizing for quiz completions (~1,006 total over 4-6 weeks), no single case type will generate 50 completions per week in its own ad set.

**This means every ad set in our campaign will remain in the learning phase for its entire duration.** The question is not "which ad sets exit the learning phase?" — none will. The question is: **which architecture minimizes the damage of perpetual learning and gets the most efficient delivery?**

### Byron Sharp's Reach Principle Applied

Byron Sharp's work demonstrates that growth comes from reaching light buyers — people who rarely think about your category. In our context, the "light buyers" are accident victims who haven't yet engaged with any PI advertising. The algorithm finds these people by testing broadly and learning from early signals.

Key implications:

- **Consolidation is mathematically superior at low budgets.** Fewer ad sets = more signal per ad set = faster (even if incomplete) learning = more efficient delivery.
- **The algorithm does not care about your case type taxonomy.** It cares about who clicks, who completes the quiz, and who converts. A single ad set with motorcycle, trucking, and pedestrian creative lets the algorithm figure out which creative resonates with which people — it does the segmentation for you, but with data rather than assumptions.
- **Splitting budget across too many ad sets is the single most common mistake** in budget-constrained Meta campaigns. It feels strategic. It is actively destructive.

### The Math That Governs Everything

| Metric | Value |
|--------|-------|
| Total media spend | $7,750 |
| Campaign duration | 4-6 weeks |
| Weekly media spend | $1,292-$1,938 |
| CPM (estimated) | $35 |
| Weekly impressions (total) | 36,900-55,400 |
| CTR | 1.0% |
| Weekly clicks (total) | 369-554 |
| Quiz start rate | 70% |
| Weekly quiz starts (total) | 258-388 |
| Quiz completion rate | 65% |
| Weekly quiz completions (total) | 168-252 |

**168-252 quiz completions per week across the entire campaign.** Every additional ad set divides this already-thin signal further.

---

## 3. Arizona Incident Volume by Case Type

### Monthly Incident Data

| Case Type | Monthly Crashes | Monthly Injuries | Monthly Non-ST Incidents (Est.) | % of Total Non-ST | Avg Case Value (Settlement) |
|-----------|----------------|-----------------|--------------------------------|-------------------|---------------------------|
| Moderate-to-Severe MVA | N/A (derived) | N/A | **400-600** | **39-49%** | $75,000 |
| DUI Victim Injuries | 460 | 298 | **298** | **24-32%** | $75,000 (+ punitive) |
| Pedestrian + Cyclist | 288 | ~268 | **268** | **22-29%** | $75,000-$300,000 |
| Motorcycle | 264 | 214 | **214** | **17-23%** | $75,000-$150,000 |
| Trucking / Commercial | 229 | 91 | **91** | **7-10%** | $90,000+ ($1M+ policies) |
| Rideshare | ~17-33 | ~10-20 | **~17** | **1-2%** | $50,000 ($1M policy) |

**Notes:**
- Categories overlap. A motorcycle crash involving a DUI offender appears in both motorcycle and DUI columns. A pedestrian hit by a truck appears in both pedestrian and trucking. Total non-soft-tissue is not the sum of rows — it's 925-1,233/month after deduplication.
- "Non-ST incidents" are estimated at: motorcycle ~100% (nearly all motorcycle injuries are non-soft-tissue), trucking victims ~60-70%, pedestrian/cyclist ~80%, DUI victims ~60%, moderate-severe MVA is by definition the non-soft-tissue subset of all MVA.
- Rideshare volume is extremely low and not separately tracked by ADOT. The estimate is extrapolated from national rideshare accident rates applied to Phoenix market volume.

### Cumulative Unrepresented Pipeline (6-12 Month Backlog)

Arizona's statute of limitations is 2 years. People who had a qualifying accident in the past 6-12 months and haven't retained an attorney form the "pipeline" our ads intercept.

| Case Type | Monthly Volume | 6-Month Pipeline | 12-Month Pipeline | Representation Rate (Est.) | Unrepresented 6-Mo | Unrepresented 12-Mo |
|-----------|---------------|-----------------|-------------------|---------------------------|--------------------|--------------------|
| Moderate-to-Severe MVA | 500 (midpoint) | 3,000 | 6,000 | ~55% | **1,350** | **2,700** |
| DUI Victim | 298 | 1,788 | 3,576 | ~50% | **894** | **1,788** |
| Pedestrian + Cyclist | 268 | 1,608 | 3,216 | ~45% | **884** | **1,769** |
| Motorcycle | 214 | 1,284 | 2,568 | ~60% | **514** | **1,027** |
| Trucking / Commercial | 91 | 546 | 1,092 | ~65% | **191** | **382** |
| Rideshare | 17 | 102 | 204 | ~40% | **61** | **122** |
| **TOTAL (deduplicated)** | **925-1,233** | — | — | — | **2,775** | **7,400** |

**Representation rate notes:**
- Motorcycle is highest because hospital referrals and roadside contact by attorneys is aggressive for visible motorcycle crashes.
- Trucking is highest because the severity and commercial insurance involvement triggers immediate attorney outreach.
- Pedestrian/cyclist is lowest because many victims in lower-income neighborhoods have less access to and awareness of legal services.
- DUI victim moderate because the criminal case against the drunk driver sometimes obscures the victim's civil claim.

---

## 4. Reachable Pipeline Sizing

### Meta-Reachable Unrepresented Pipeline

Not every unrepresented accident victim is on Facebook/Instagram. Using platform data from Doc 4:

- ~71% of AZ adults are on Facebook
- Advantage+ placements include Instagram, reaching an incremental ~10-15% who are Instagram-only
- Effective Meta reach: ~75% of AZ adults

| Case Type | Unrepresented Pipeline (6-12 Mo) | x 75% Meta Reachable | Meta-Reachable Unrepresented |
|-----------|--------------------------------|----------------------|------------------------------|
| Moderate-to-Severe MVA | 1,350-2,700 | x 0.75 | **1,013-2,025** |
| DUI Victim | 894-1,788 | x 0.75 | **671-1,341** |
| Pedestrian + Cyclist | 884-1,769 | x 0.75 | **663-1,327** |
| Motorcycle | 514-1,027 | x 0.75 | **386-770** |
| Trucking / Commercial | 191-382 | x 0.75 | **143-287** |
| Rideshare | 61-122 | x 0.75 | **46-92** |
| **TOTAL** | **2,775-7,400** | — | **2,081-5,550** |

### What These Numbers Mean for the Algorithm

The Meta algorithm is not searching through 4.1M Arizonans to find 386 motorcycle victims. It is serving ads to everyone in Arizona, and the **creative self-qualifies** — only motorcycle crash victims will engage with motorcycle creative.

The "Meta-reachable unrepresented pipeline" represents the maximum number of people in Arizona at any given time who:
1. Had a qualifying non-soft-tissue accident
2. Don't already have an attorney
3. Are on Facebook or Instagram
4. Could theoretically see our ad and self-qualify into the funnel

This is the universe. Our campaign needs to reach a fraction of it — at a 0.3-0.8% capture rate on the total pool, we get our 21 leads.

**But for ad set architecture, the question is: how does the algorithm *learn* which impressions work?** It learns from clicks and quiz completions. The more events per ad set, the faster the algorithm narrows its delivery to efficient impressions. A case type with 386 reachable unrepresented victims produces fewer click and completion events than one with 2,025 — and that event differential is what determines whether an ad set thrives or starves.

---

## 5. Budget Math Per Ad Set — Three Architecture Options

### Shared Assumptions

| Parameter | Value |
|-----------|-------|
| Total media spend | $7,750 |
| Campaign duration | 5 weeks (midpoint of 4-6) |
| CPM | $35 |
| CTR | 1.0% |
| CPC (derived) | $3.50 |
| Quiz start rate (from click) | 70% |
| Quiz completion rate | 65% |
| Non-soft-tissue pass rate | 40% |
| Contact submission rate | 85% |
| Verification pass rate | 85% |
| Final deliverable rate | ~50% of verified |
| Full-funnel conversion (click to delivered lead) | ~0.95% |

### Per-Ad-Set Performance at Different Budget Splits

| # of Ad Sets | Budget per Ad Set | Weekly Spend per Ad Set | Weekly Impressions per Ad Set | Weekly Clicks per Ad Set | Weekly Quiz Completions per Ad Set | Total Leads per Ad Set (5 wks) |
|--------------|------------------|------------------------|------------------------------|-------------------------|-----------------------------------|-------------------------------|
| **1** | $7,750 | $1,550 | 44,286 | 443 | 202 | **~21** |
| **2** (equal) | $3,875 | $775 | 22,143 | 221 | 101 | **~10-11** |
| **3** (equal) | $2,583 | $517 | 14,762 | 148 | 67 | **~7** |
| **4** | $1,938 | $388 | 11,071 | 111 | 51 | **~5** |
| **5** | $1,550 | $310 | 8,857 | 89 | 40 | **~4** |

### Learning Phase Reality Check

| # of Ad Sets | Weekly Quiz Completions per Ad Set | vs. 50/week Threshold | Status |
|--------------|-----------------------------------|-----------------------|--------|
| **1** | 202 | 4.0x above | **Approaches exit** (if optimizing for quiz completions) |
| **2** | 101 | 2.0x above | **In learning, but accumulating signal** |
| **3** | 67 | 1.3x above | **Marginal — barely clearing threshold** |
| **4** | 51 | ~1.0x | **On the edge — will not reliably exit** |
| **5** | 40 | 0.8x below | **Permanently in learning** |

**This table is the most important data in this document.** At 3 ad sets, each set barely clears the quiz completion threshold. At 4 or more, ad sets are permanently starved. And this is with *equal* budget splits — any unequal split creates one stronger and one or more weaker ad sets.

Furthermore: we would likely optimize for a *deeper* event than quiz completion (e.g., lead submission or quiz + injury filter pass), which further reduces the weekly event count and makes the learning threshold harder to hit.

---

## 6. Option A: 3 Ad Sets

### Structure

| Ad Set | Case Types | Creative Approach | Monthly AZ Incident Volume | Budget Allocation |
|--------|-----------|-------------------|---------------------------|-------------------|
| **A1: Motorcycle** | Motorcycle only | Identity-based. Rider imagery, helmet/gear, desert roads, "fellow riders" language. Visually distinct from all other PI advertising. | 264 crashes, 214 injuries | 30% ($2,325) |
| **A2: Trucking** | Trucking/commercial only | David vs. Goliath. I-10/I-40 corridor imagery, semi trucks, anger/injustice framing. Emphasize $1M+ commercial policies. | 229 crashes, 91 injuries | 25% ($1,938) |
| **A3: General Severe Injury** | Moderate MVA + Pedestrian/Cyclist + DUI Victim + Rideshare | Broad injury language. Broken bones, surgery, hospital, "seriously injured in an accident?" Financial distress framing. | 600-900+ combined | 45% ($3,488) |

### Performance Projections

| Metric | A1: Motorcycle | A2: Trucking | A3: General Severe | Total |
|--------|---------------|-------------|-------------------|-------|
| Budget | $2,325 | $1,938 | $3,488 | $7,750 |
| Weekly spend | $465 | $388 | $698 | $1,550 |
| Total impressions | 66,429 | 55,357 | 99,643 | 221,429 |
| Total clicks | 664 | 554 | 996 | 2,214 |
| Weekly clicks | 133 | 111 | 199 | 443 |
| Quiz completions | 302 | 252 | 453 | 1,006 |
| Weekly quiz completions | 60 | 50 | 91 | 202 |
| Delivered leads (est.) | ~6 | ~5 | ~10 | **~21** |

### Algorithm Learning Assessment

| Ad Set | Weekly Quiz Completions | vs. 50/week Threshold | Learning Status |
|--------|------------------------|-----------------------|-----------------|
| A1: Motorcycle | 60 | 1.2x | **Marginal** — barely above threshold. Any CPM spike or CTR dip drops it below. |
| A2: Trucking | 50 | 1.0x | **Critical** — exactly at threshold. Will likely not exit learning. |
| A3: General Severe | 91 | 1.8x | **Adequate** — should accumulate sufficient signal. |

### Option A Verdict

**Motorcycle (A1)** is teetering on the edge. It has enough creative distinctiveness to justify a dedicated set (see Section 10), but the budget leaves almost no margin. One bad week of CPMs and it stalls.

**Trucking (A2)** is the problem. At 25% of budget, it lands exactly at the 50-completion threshold — meaning it will functionally never exit learning. Trucking has the highest case values ($1M+ policies), which makes every lead extraordinarily valuable, but the algorithm won't find those leads efficiently if the ad set is starved.

**General Severe (A3)** works as a catchall but its creative has to serve four different case types (moderate MVA, pedestrian, DUI, rideshare), which dilutes self-qualification. A person hit by a drunk driver and a person injured while crossing the street have very different emotional contexts, but they'd see the same creative.

**Risk assessment:** High. Two of three ad sets are at or below the learning threshold. The campaign would likely produce fewer total leads than a more consolidated approach because the algorithm is spending more of the budget in inefficient "learning" delivery.

---

## 7. Option B: 2 Ad Sets

### Structure

| Ad Set | Case Types | Creative Approach | Monthly AZ Incident Volume | Budget Allocation |
|--------|-----------|-------------------|---------------------------|-------------------|
| **B1: Vehicle-Type-Specific** | Motorcycle + Trucking | Two distinct creative sets within one ad set. Motorcycle creative (rider identity) and trucking creative (I-10 semi-truck) run as separate ads within the same ad set. Algorithm distributes between them. | 493 crashes combined, 305 injuries combined | 40% ($3,100) |
| **B2: General Severe Injury** | Moderate MVA + Pedestrian/Cyclist + DUI Victim + Rideshare | Broad serious injury creative + pedestrian-specific creative + DUI-specific creative. Multiple ads within one ad set. | 600-900+ combined | 60% ($4,650) |

### Performance Projections

| Metric | B1: Vehicle-Type | B2: General Severe | Total |
|--------|-----------------|-------------------|-------|
| Budget | $3,100 | $4,650 | $7,750 |
| Weekly spend | $620 | $930 | $1,550 |
| Total impressions | 88,571 | 132,857 | 221,429 |
| Total clicks | 886 | 1,329 | 2,214 |
| Weekly clicks | 177 | 266 | 443 |
| Quiz completions | 403 | 604 | 1,006 |
| Weekly quiz completions | 81 | 121 | 202 |
| Delivered leads (est.) | ~8-9 | ~12-13 | **~21** |

### Algorithm Learning Assessment

| Ad Set | Weekly Quiz Completions | vs. 50/week Threshold | Learning Status |
|--------|------------------------|-----------------------|-----------------|
| B1: Vehicle-Type | 81 | 1.6x | **Good** — clear of threshold with margin for CPM volatility. |
| B2: General Severe | 121 | 2.4x | **Strong** — well above threshold. Algorithm will optimize. |

### Option B Verdict

**Vehicle-Type (B1)** consolidates motorcycle and trucking into one ad set while running distinct creative for each. The algorithm sees 81 weekly quiz completions — enough to learn. It will naturally allocate more impressions to whichever creative (motorcycle or trucking) generates more engagement. This is a feature, not a bug: the algorithm is doing the case-type-level optimization that we'd otherwise be guessing at.

**General Severe (B2)** gets 60% of budget and strong signal density. Multiple creative variants within this ad set (pedestrian-specific, DUI-specific, general injury, Spanish-language) give the algorithm several hooks to test. The 121 weekly completions provide solid learning ground.

**The key advantage of Option B:** Both ad sets have breathing room above the learning threshold. Neither is at risk of stalling. The campaign can absorb a bad CPM week without collapsing a critical ad set.

**The tradeoff:** Motorcycle and trucking creative share an ad set, which means the algorithm decides how to split impressions between them. If motorcycle creative outperforms (likely — more visually distinct, identity-driven), trucking creative may get deprioritized. This could mean fewer trucking leads, which are the highest-value leads in the campaign.

---

## 8. Option C: 1 Ad Set (Broad)

### Structure

| Ad Set | Case Types | Creative Approach | Monthly AZ Incident Volume | Budget Allocation |
|--------|-----------|-------------------|---------------------------|-------------------|
| **C1: All Non-Soft-Tissue** | Everything: Motorcycle + Trucking + Moderate MVA + Pedestrian/Cyclist + DUI Victim + Rideshare | 5-6 distinct creative variants within one ad set. Each creative self-qualifies for its case type. Algorithm distributes budget across all variants. | 925-1,233 combined | 100% ($7,750) |

### Creative Variants Within Single Ad Set

| Creative # | Case Type | Visual Approach | Copy Hook |
|-----------|-----------|----------------|-----------|
| C1-a | Motorcycle | Rider on desert highway, helmet/gear | "Arizona riders know the risk. After a crash, know your rights." |
| C1-b | Trucking | Semi on I-10 corridor, David vs. Goliath | "Hit by a truck on Arizona's highways? The trucking company has lawyers. You should too." |
| C1-c | Pedestrian | Crosswalk, nighttime urban, intersection | "Hit while crossing the street? You weren't the one driving." |
| C1-d | DUI Victim | Nighttime, headlights, injustice | "A drunk driver changed your life. It's not too late to hold them accountable." |
| C1-e | General Severe | Hospital, broken bones, bills | "Seriously injured in an accident? Broken bones, surgery, or worse — find out what your case is worth." |
| C1-f | Spanish (Pedestrian/MVA) | Crosswalk/intersection, family | "Lastimado en un accidente? Huesos rotos, cirugia -- sepa lo que vale su caso." |

### Performance Projections

| Metric | C1: All Non-Soft-Tissue | Notes |
|--------|------------------------|-------|
| Budget | $7,750 | 100% concentrated |
| Weekly spend | $1,550 | Maximum signal density |
| Total impressions | ~221,429 | Same total as all options |
| Total clicks | ~2,214 | Same total |
| Weekly clicks | ~443 | Maximum per ad set |
| Quiz completions | ~1,006 | Same total |
| Weekly quiz completions | **~202** | **4.0x above learning threshold** |
| Delivered leads (est.) | **~21** | Same total |

### Algorithm Learning Assessment

| Ad Set | Weekly Quiz Completions | vs. 50/week Threshold | Learning Status |
|--------|------------------------|-----------------------|-----------------|
| C1: All | 202 | 4.0x | **Excellent** — strongest learning signal of any option. Closest to exiting learning phase. |

### How the Algorithm Handles Multiple Creatives in One Ad Set

This is the question people get wrong most often: "If I put motorcycle and pedestrian creative in one ad set, won't the algorithm just pick the best one and ignore the rest?"

**How it actually works:**

1. Meta's Advantage+ creative optimization tests all creative variants across the full audience.
2. Each creative gets an initial testing budget (~$5-10 per creative before the algorithm starts favoring).
3. The algorithm identifies which creative resonates with which *subsets* of the audience. Motorcycle creative will naturally perform better with motorcycle riders. Pedestrian creative will naturally perform better in west Phoenix neighborhoods with pedestrian-heavy populations.
4. The algorithm allocates more impressions to the creative-audience combinations that generate the most optimization events (quiz completions).
5. Lower-performing creative gets less spend but does not get fully shut off — the algorithm continues to test periodically.

**Net effect:** The algorithm does the case-type segmentation that Option A tries to force manually. But it does it with data — not with our assumptions about which case type deserves what budget percentage.

### Option C Verdict

**Maximum algorithmic efficiency.** Every dollar contributes to a single learning model. The 202 weekly quiz completions give the algorithm 4x the minimum signal it needs. It will rapidly identify which creative-audience pairings work and shift spend accordingly.

**The risk:** If one creative dramatically outperforms the others (e.g., motorcycle creative gets 3x the CTR of trucking creative), the algorithm may starve lower-performing creatives. This could mean trucking — the highest case value — gets deprioritized because the *click-through rate* is lower, even though the *lead value* is higher. Meta's algorithm optimizes for the event you tell it to optimize for (quiz completions), not for your downstream economics.

**Mitigation:** Set minimum spend thresholds per creative variant using Meta's "Flexible Ad" rules, or use Dynamic Creative Optimization (DCO) to ensure each creative gets minimum exposure. Alternatively, manually monitor creative distribution weekly and pause/reactivate to force rebalancing.

---

## 9. Head-to-Head Comparison

### Performance Metrics

| Metric | Option A (3 Ad Sets) | Option B (2 Ad Sets) | Option C (1 Ad Set) |
|--------|---------------------|---------------------|---------------------|
| Total media spend | $7,750 | $7,750 | $7,750 |
| Weakest ad set weekly completions | **50** (Trucking) | **81** (Vehicle-Type) | **202** (only ad set) |
| Weakest ad set vs. 50/wk threshold | **1.0x** (at risk) | **1.6x** (safe) | **4.0x** (excellent) |
| # of ad sets at or below threshold | **2 of 3** | **0 of 2** | **0 of 1** |
| Estimated total delivered leads | ~19-21 | ~21 | ~21 |
| Lead quality consistency | Higher (dedicated creative) | Good (2-tier creative) | Variable (algorithm-driven) |
| Creative production cost | **Highest** (3 full creative sets) | **Moderate** (2 creative sets) | **Lowest** (1 set, 5-6 variants) |
| Optimization flexibility | Low (budget locked per set) | Moderate | **Highest** (algorithm self-optimizes) |
| Risk of wasted spend in learning | **High** (2 starved sets) | Low | **Lowest** |

### Algorithm Signal Quality

| Option | Total Weekly Signal (Quiz Completions) | Signal Per Ad Set | Efficiency Rating |
|--------|---------------------------------------|-------------------|-------------------|
| A | 202 | 50-91 (uneven) | Poor — 2 of 3 sets are borderline |
| B | 202 | 81-121 (balanced) | Good — both sets are viable |
| C | 202 | 202 (concentrated) | Excellent — maximum learning |

### Lead Estimation Sensitivity

Because starved ad sets deliver less efficiently (higher effective CPMs, more budget burned in learning), the actual lead production differs:

| Option | Ideal Leads (no learning penalty) | Estimated Learning Penalty | Realistic Lead Estimate |
|--------|----------------------------------|--------------------------|------------------------|
| A | 21 | -15% to -25% (2 starved sets) | **16-18** |
| B | 21 | -5% to -10% | **19-20** |
| C | 21 | 0% to -5% | **20-21** |

**The learning penalty is real.** Industry data consistently shows that ad sets stuck in the learning phase deliver 15-30% worse cost-per-result than ad sets that have exited. With two of three ad sets in Option A perpetually learning, the campaign loses 3-5 leads to inefficiency.

---

## 10. Creative Distinctiveness Assessment

The strongest argument for dedicated ad sets is creative distinctiveness. If a case type's visual and emotional language is radically different from other case types, dedicated creative that speaks exclusively to that audience will outperform generic creative — potentially enough to offset the algorithmic penalty of a smaller ad set.

### Case-by-Case Creative Distinctiveness Score

| Case Type | Visual Identity | Emotional Angle | Self-Qualification Power | Creative Distinctiveness (1-5) |
|-----------|----------------|----------------|--------------------------|-------------------------------|
| **Motorcycle** | **Extremely high.** Rider on open road, helmet, gear, desert highway. Instantly recognizable to riders, instantly irrelevant to non-riders. | Freedom disrupted. Community. "Fellow rider." Identity-based, not situation-based. | **Strongest.** A motorcycle ad literally only resonates with riders. Perfect self-qualifier. | **5/5** |
| **Trucking** | **High.** Semi truck imagery, I-10 desert corridor, size contrast. | David vs. Goliath. Anger. "They have a fleet of lawyers." | **Good.** Truck imagery signals who this is for, but anyone in a serious crash might relate to the anger framing. | **4/5** |
| **Pedestrian/Cyclist** | **High.** Crosswalk, nighttime street, urban intersection. | Pure innocence. "You were doing everything right." | **Good.** Pedestrian imagery speaks to pedestrians but "hit while crossing the street" is a very specific trigger. | **4/5** |
| **DUI Victim** | **Moderate.** Nighttime, headlights, blur. Visually similar to general "nighttime crash" imagery. | Injustice. "They were drunk. You pay the price." | **Moderate.** The emotional hook is strong but the visual isn't instantly distinct from general MVA. | **3/5** |
| **Moderate-to-Severe MVA** | **Low.** Generic car crash aftermath, hospital, bills. | Financial crisis. "Seriously injured?" | **Low.** This is the "everything else" bucket. Creative is necessarily broad. | **2/5** |
| **Rideshare** | **Moderate.** Uber/Lyft app interface, phone, car interior. | "It wasn't your ride — it was their crash." | **Moderate.** Specific to rideshare users. But at 17 incidents/month, the audience is microscopic. | **3/5** (irrelevant at this volume) |

### What This Tells Us

- **Motorcycle is the only case type where creative distinctiveness alone justifies a dedicated ad set** — even at reduced budget. Motorcycle creative is identity-based advertising, not situation-based advertising. Riders self-identify. The creative does nearly all the targeting work.
- **Trucking has strong distinctiveness but not enough to overcome the algorithmic penalty** at this budget. The David vs. Goliath emotional angle is powerful, but trucking creative can run within a multi-ad-set and still self-qualify effectively.
- **DUI and pedestrian** have good creative hooks but their visual language overlaps enough with general injury creative that they don't *need* dedicated ad sets to self-qualify.
- **Rideshare** is a non-factor at 17 incidents/month. Any rideshare lead that comes through will come through the general injury funnel.

---

## 11. Creative Production Cost Analysis

Creative production is not free. Every dedicated ad set needs:
- 2-3 creative variants (image, video, carousel) at minimum
- Copy variations (headline, body, CTA) for each variant
- Spanish-language versions for high-Hispanic case types (pedestrian)
- Landing page / quiz entry customization

### Production Cost Estimate by Option

| Component | Option A (3 Ad Sets) | Option B (2 Ad Sets) | Option C (1 Ad Set) |
|-----------|---------------------|---------------------|---------------------|
| Distinct creative sets needed | 3 full sets | 2 full sets (4 creative variants across 2 sets) | 1 set (5-6 creative variants) |
| Estimated creative pieces | 9-12 | 6-8 | 5-6 |
| Production hours | 15-20 hrs | 10-14 hrs | 8-10 hrs |
| Estimated creative cost | $500-$750 | $375-$500 | $250-$375 |
| Landing page/quiz variants | 3 entry points | 2 entry points | 1 entry point (quiz routes internally) |
| Creative cost as % of media | 6.5-9.7% | 4.8-6.5% | 3.2-4.8% |

**At a $7,750 media budget, every $100 shifted from media to creative production = ~2,857 fewer impressions = ~29 fewer clicks = ~1 fewer quiz completion.** Creative quality matters enormously, but creative *quantity* has diminishing returns when the algorithm can't distribute it efficiently.

### The Math on Creative ROI

For a dedicated ad set to justify its creative production cost, the lift in conversion rate from case-type-specific creative must exceed the loss from reduced algorithmic signal.

**Example — Motorcycle dedicated ad set (Option A) vs. motorcycle creative within broad ad set (Option C):**

| Factor | Dedicated Ad Set (A1) | Creative Within Broad Set (C1-a) |
|--------|----------------------|----------------------------------|
| Budget allocated to motorcycle | $2,325 (30%) | Algorithm-determined (~20-35%) |
| Weekly quiz completions in ad set | 60 | 202 (shared) |
| Learning phase status | Marginal | Strong |
| Expected CTR on motorcycle creative | 1.3% (higher, dedicated) | 1.1% (slightly lower in broad set) |
| Motorcycle impressions | 66,429 | ~44,000-77,000 (algorithm-driven) |
| Motorcycle clicks | ~863 (at 1.3%) | ~484-847 (at 1.1%) |
| Motorcycle quiz completions | ~393 | ~220-385 |
| Motorcycle delivered leads | ~4-5 | ~3-5 |

The dedicated ad set produces marginally more motorcycle clicks due to higher CTR, but the difference is within the margin of error. And the broad ad set achieves this without the risk of learning phase starvation.

---

## 12. Definitive Recommendation

### Recommended Architecture: Modified Option B — 2 Ad Sets with Motorcycle Separation at Minimum Viable Budget

After evaluating all three options, the optimal architecture is a **hybrid** that captures motorcycle's creative distinctiveness while maintaining strong algorithmic signal in the primary ad set:

| Ad Set | Case Types | Budget | Weekly Spend | Weekly Quiz Completions | Learning Status |
|--------|-----------|--------|-------------|------------------------|-----------------|
| **Ad Set 1: Motorcycle** | Motorcycle only | **25% ($1,938)** | $388 | ~50 | **Threshold** — acceptable risk given motorcycle's creative self-qualification power |
| **Ad Set 2: All Other Non-Soft-Tissue** | Trucking + Moderate MVA + Pedestrian/Cyclist + DUI Victim + Rideshare | **75% ($5,813)** | $1,163 | ~152 | **Strong** — 3x above threshold, excellent learning |
| **Total** | | **$7,750** | $1,550 | 202 | |

### Why This Architecture

**1. Motorcycle earns a dedicated ad set on creative distinctiveness alone.**

Motorcycle is the only case type that scores 5/5 on creative distinctiveness. It is identity-based advertising — riders self-identify instantly with motorcycle imagery. This is not a case-type creative; it is a *community* creative. The self-qualification power is so strong that even a marginal learning signal (50 completions/week) will produce efficient delivery because the click-through rate on motorcycle creative to motorcycle riders is structurally higher than any other creative-audience pairing in this campaign. The algorithm needs fewer events to learn because the signal is cleaner.

Byron Sharp would note: motorcycle riders are a *category entry point*. They know they ride. The creative triggers an existing identity. This is fundamentally different from "seriously injured in an accident?" which tries to trigger a recent *experience* — a weaker psychological hook.

**2. Everything else benefits from consolidation.**

Trucking, pedestrian, DUI, moderate MVA, and rideshare are all *situation-based* case types. The creative hooks are strong but they are triggered by recent experience, not pre-existing identity. The algorithm is better at matching situation-based creative to the right people when it has more data to work with. At 152 weekly quiz completions, Ad Set 2 will learn quickly which creative variants work and allocate budget accordingly.

Within Ad Set 2, run these creative variants:

| Creative | Visual | Hook | Expected Performance |
|----------|--------|------|---------------------|
| Trucking | Semi on I-10, size contrast | "Hit by a truck? Their insurance is $1M+. Find out what your case is worth." | High CTR among highway commuters |
| Pedestrian (English) | Crosswalk, nighttime | "Hit while crossing the street? You weren't the one driving." | Strong in urban Phoenix, Tucson |
| Pedestrian (Spanish) | Same visual, Spanish copy | "Le atropellaron cruzando la calle? Usted no era quien manejaba." | Unlocks Maryvale/South Phoenix 29% Spanish-primary |
| DUI Victim | Night, headlights | "A drunk driver changed your life. Hold them accountable." | Strong emotional resonance, broad appeal |
| General Severe Injury | Hospital, cast, bills | "Seriously injured? Broken bones, surgery — find out what your case is worth." | Broadest net, catches everything else |

**3. The budget math works.**

| Ad Set | Budget | Est. Impressions | Est. Clicks | Est. Quiz Completions | Est. Delivered Leads |
|--------|--------|-----------------|-------------|----------------------|---------------------|
| Motorcycle | $1,938 | 55,357 | 554 | 252 | **~5-6** |
| All Other | $5,813 | 166,071 | 1,661 | 754 | **~15-16** |
| **Total** | **$7,750** | **221,429** | **2,214** | **1,006** | **~20-22** |

Expected lead distribution by case type (within All Other ad set, based on algorithm-driven creative allocation):

| Case Type | Est. % of Ad Set 2 Leads | Est. Leads | Reasoning |
|-----------|--------------------------|-----------|-----------|
| Moderate-to-Severe MVA | 40% | ~6 | Largest incident pool, broadest creative appeal |
| Pedestrian/Cyclist (English + Spanish) | 25% | ~4 | Strong creative, emotional resonance, Spanish variant adds reach |
| DUI Victim | 20% | ~3 | Strong emotional hook, high engagement |
| Trucking | 12% | ~2 | Smaller injury volume (91/month) but highest case value |
| Rideshare | 3% | ~0-1 | Extremely low volume, incidental capture only |

**4. ROAS is maximized by case diversity, not case concentration.**

| Lead Mix | Est. Leads | Weighted Avg Settlement | Projected Attorney Fees (at 12-15% sign rate) |
|----------|-----------|------------------------|-----------------------------------------------|
| Motorcycle | 5-6 | $112,500 | $93,750-$112,500 total pool |
| Moderate MVA | 6 | $75,000 | $150,000 total pool |
| Pedestrian/Cyclist | 4 | $150,000 | $200,000 total pool |
| DUI Victim | 3 | $75,000+ punitive | $75,000+ total pool |
| Trucking | 2 | $90,000+ | $60,000+ total pool |
| Rideshare | 0-1 | $50,000 | $16,500 total pool |
| **Total** | **~21** | — | **$595,250-$613,000 total pipeline value** |

At 12-15% sign rate across the pipeline: **~$71K-$92K in projected attorney fees from $10K investment = 7-9x ROAS.**

### What This Architecture Does NOT Do

- **It does not guarantee trucking leads.** The algorithm may deprioritize trucking creative within Ad Set 2 if it underperforms on CTR. This is a known risk. Trucking leads are the highest value but may come in at lower volume than their incident rate would suggest.
- **It does not guarantee Spanish-language leads.** Spanish creative may underperform on pure click-through if the algorithm favors English creative. Monitor weekly and manually boost Spanish creative if it gets less than 10% of Ad Set 2 impressions.
- **It does not exit the learning phase.** At this budget, no architecture does. But this one gets closer than any other option.

---

## 13. Implementation Blueprint

### Week 0: Campaign Setup

| Task | Detail |
|------|--------|
| Create Campaign | Single campaign, Special Ad Category: Social Issues, Arizona statewide, Advantage+ placements |
| Ad Set 1: Motorcycle | Daily budget: $55.37. Optimization event: Landing page views (lowest viable funnel event to maximize event count). Broad audience, AZ statewide. |
| Ad Set 2: All Other Non-ST | Daily budget: $166.09. Same optimization event. Broad audience, AZ statewide. |
| Creative: Ad Set 1 | 2-3 motorcycle variants (video + image + carousel). Rider identity creative. |
| Creative: Ad Set 2 | 5 creative variants minimum (trucking, pedestrian EN, pedestrian ES, DUI, general severe). |
| Funnel | Single quiz funnel with case-type routing at Step 4 ("What type of accident?"). All ad sets drive to the same quiz. |

### Optimization Event Decision

**Optimize for Landing Page Views, not quiz completions.** Here is why:

At our budget, optimizing for quiz completions (a deeper funnel event) would produce ~202 weekly events across both ad sets — marginal for the motorcycle set. Optimizing for landing page views instead gives us ~388 weekly events per the motorcycle ad set and ~1,163 across the campaign. This dramatically increases signal density.

The tradeoff: the algorithm optimizes for *clicks that become page views*, not *clicks that become quiz completions*. This may bring in slightly lower-intent traffic. But at this budget, the additional signal is worth the slightly noisier audience — the quiz itself filters out low-intent visitors.

**If the campaign scales beyond $10K:** shift optimization to quiz completions or lead submissions once the event volume supports it.

### Weekly Monitoring Protocol

| Week | Action |
|------|--------|
| Week 1 | Monitor delivery and creative distribution. Confirm both ad sets are spending. Check motorcycle ad set is not flagged by Meta for Special Ad Category compliance. |
| Week 2 | Review creative performance within Ad Set 2. If any creative has <5% of impressions, investigate. If Spanish creative is underdelivering, consider boosting its bid. Check motorcycle CTR vs. plan. |
| Week 3 | Mid-campaign optimization. Pause lowest-performing creative variant (if one is clearly losing). Reallocate spend if one ad set is dramatically outperforming (shift up to 10% of budget). |
| Week 4-5 | Steady state. Let algorithm run. Focus on lead quality review from delivered leads so far. Begin preparing Phase 2 recommendations. |
| Week 6 | Campaign wrap. Full performance analysis by ad set, creative, case type, and lead grade. |

### Budget Reallocation Triggers

| Trigger | Action |
|---------|--------|
| Motorcycle ad set CPM >$50 for 3+ days | Shift 10% of motorcycle budget to Ad Set 2. Motorcycle creative becomes a variant within Ad Set 2. |
| Motorcycle ad set CTR >1.5% | Consider shifting 5-10% from Ad Set 2 to motorcycle to capitalize on strong performance. |
| Any Ad Set 2 creative variant with 0 quiz completions after 7 days | Pause that creative. It is not resonating. |
| Spanish creative <5% of Ad Set 2 impressions after 10 days | Create a separate Spanish-language ad set at minimum budget ($5/day) to force exposure. |
| Total campaign pacing >15% ahead of schedule by Week 3 | Reduce daily budgets to extend campaign to full 6 weeks for maximum learning. |

---

## Summary Table — Final Architecture

| Ad Set | Case Types | Budget | % of Spend | Weekly Quiz Completions | Learning Status | Creative Variants |
|--------|-----------|--------|-----------|------------------------|-----------------|-------------------|
| **Motorcycle** | Motorcycle | $1,938 | 25% | ~50 | Threshold (acceptable) | 2-3 rider-identity pieces |
| **All Other Non-ST** | Trucking + MVA + Pedestrian + DUI + Rideshare | $5,813 | 75% | ~152 | Strong | 5+ variants incl. Spanish |
| **Total** | All non-soft-tissue | **$7,750** | 100% | 202 | Campaign-level: good | 7-8 total creative pieces |

**Expected output:** ~20-22 delivered leads across all case types. ~5-6 motorcycle, ~15-16 all other. Projected pipeline value: $595K-$613K. Projected ROAS at 12-15% sign rate: 7-9x.

**The single most important principle in this document:** At $7,750 media spend, consolidation is not a compromise — it is the mathematically correct strategy. The algorithm is smarter than our case-type taxonomy. Let it work.

---

*This document feeds directly into the Creative Strategy document (Doc 5). The creative team should build 7-8 total creative variants aligned to the ad set architecture above.*

*Second Chair x West Coast Trial Lawyers — Audience Sizing & Ad Set Architecture — April 2026*
