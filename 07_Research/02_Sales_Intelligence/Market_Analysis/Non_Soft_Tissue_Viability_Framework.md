# Non-Soft-Tissue Market Viability Framework

> **Type:** Central reference — universal across all prospects
> **Purpose:** Determines whether a DMA has enough non-soft-tissue PI case volume to support a filtered campaign (trucking, severe MVA, wrongful death, pedestrian/cyclist, DUI victim, rideshare — excluding whiplash/minor sprains)
> **Source methodology:** WCTL Arizona pilot audience research (2026-04)
> **Related:** `Projected_Attorney_Fee_Model` at `../../01_Identity/Projected_Attorney_Fee_Model.md`

---

## Why This Matters

Most PI lead gen runs **all case types** — the full funnel from whiplash to wrongful death. The default SC product is all-PI. But some clients want **non-soft-tissue only**: higher case value, higher attorney fee, fewer but more valuable leads.

Non-soft-tissue filtering reduces addressable volume by **~80%** but increases average case value by **3-4x**. Whether a DMA can support this depends on raw incident volume — too small and the Meta algorithm can't learn efficiently.

This framework gives the viability check for any DMA, any prospect.

---

## The Formula

```
Monthly Incident Volume (non-soft-tissue)
  = Total monthly motor vehicle crashes in DMA
  × Non-soft-tissue rate (~15-20% of all crashes produce non-soft-tissue injuries)

Unrepresented Pipeline (annual)
  = Monthly non-ST volume × (1 - representation rate) × 12
    where representation rate = 45-65% depending on case type

Meta-Reachable Pipeline
  = Unrepresented Pipeline × 0.75 (platform penetration rate)

Algorithm Viability
  = Requires ≥50 weekly optimization events per ad set
  = Approximately ≥200 monthly non-ST incidents in the DMA
```

### Minimum Viability Thresholds

| Threshold | Minimum | Comfortable | Strong |
|---|---|---|---|
| Monthly non-ST incidents | ≥200 | ≥500 | ≥1,000 |
| Meta-reachable pipeline (6-mo) | ≥150 | ≥500 | ≥2,000 |
| Weekly quiz completions per ad set | ≥50 | ≥100 | ≥200 |
| Avg case value (settlement) | ≥$75K | ≥$100K | ≥$150K |

**Below 200 monthly incidents = NOT viable for non-soft-tissue-only campaign.** Default to all-PI.

---

## Non-Soft-Tissue Case Type Breakdown

| Case Type | % of Non-ST Volume | Avg Settlement | Expected Attorney Fee (33%) | Notes |
|---|---|---|---|---|
| **Moderate-to-Severe MVA** | 39-49% | $75,000-$300,000+ | $25,000-$100,000+ | Fracture, herniated disc, TBI, spinal |
| **DUI Victim** | 24-32% | $100,000-$500,000 | $33,000-$165,000 | Punitive damages often available |
| **Pedestrian/Cyclist** | 22-29% | $50,000-$250,000 | $16,500-$82,500 | Urban/commute corridors |
| **Motorcycle** | 17-23% | $112,500 median | $37,500 | High severity, high case value |
| **Trucking/Commercial** | 7-10% | $90,000-$500,000+ | $30,000-$165,000+ | FMCSA violations often compound |
| **Rideshare** | 1-2% | $50,000 | $16,500 | Requires bundling (too low volume standalone) |

### Representation Rates by Case Type

| Case Type | Estimated Representation Rate | Unrepresented Gap |
|---|---|---|
| Motorcycle | 60% | 40% |
| Moderate-to-Severe MVA | 55% | 45% |
| Pedestrian/Cyclist | 45% | 55% |
| DUI Victim | 50% | 50% |
| Trucking | 65% | 35% |
| Rideshare | 40% | 60% |

Higher representation = more competition for the unrepresented share. Trucking has highest representation but also highest case value, so the economics still work.

---

## How Non-Soft-Tissue Changes The SC Product

### Lead volume
- **All-PI:** ~1-3 leads/day per DMA at scale
- **Non-ST only:** ~0.3-0.8 leads/day per DMA (roughly 1/3 to 1/4 of all-PI volume)
- **100-lead package fills in:** ~8-14 weeks (vs. 5-7 for all-PI)

### Lead cost
- **All-PI LA:** $425/lead (MOI 8.0 list)
- **Non-ST LA:** $475-$525/lead (estimated — narrower audience = higher CPA, but testing required). Use **$500/lead as working estimate** until campaign data validates.
- Premium reflects: more targeted creative, narrower Meta audience, higher CPC for severe-injury keywords, more qualification steps in the funnel

### Projected Attorney Fee per lead
- **All-PI cohort:** ~$2,485 avg projected fee/lead (from standard model)
- **Non-ST cohort:** ~$4,500-$7,000 avg projected fee/lead (case-value mix jumps 2-3x)

### Projected ROAS
- **All-PI LA at $425:** 4.5-7.5× projected
- **Non-ST LA at $500:** **6-10× projected** (higher fee per lead more than offsets higher CPL)

### Why ROAS can be BETTER on non-ST despite higher CPL
The numerator (projected attorney fee) grows faster than the denominator (lead cost). A $500 lead projecting $5,500 in attorney fee = 11× per lead. Even at conservative sign rates, the portfolio ROAS exceeds all-PI.

---

## Viability Quick-Check by Top DMAs

| DMA | Population | Est. Monthly MVA Crashes | Est. Non-ST Volume | **Viable for Non-ST?** |
|---|---|---|---|---|
| **Los Angeles** | 13.2M | ~8,000-10,000 | **~1,500-2,000** | **YES — highly viable** (7-10x threshold) |
| **New York** | 7.2M | ~5,000+ | **~800-1,000** | YES — strong |
| **Phoenix-Mesa** | 5.0M | ~3,500 | **~600-800** | YES — strong (AZ pilot validated at 925-1,233/mo) |
| **SF-Oakland-San Jose** | 4.7M | ~2,800 | **~450-600** | YES — comfortable |
| **Riverside-San Bernardino** | 4.6M | ~3,000 | **~500-700** | YES — comfortable |
| **San Diego** | 3.3M | ~2,000 | **~350-450** | YES — comfortable |
| **Seattle-Tacoma** | 4.0M | ~2,200 | **~350-500** | YES — comfortable |
| **Las Vegas** | 2.3M | ~1,500 | **~250-350** | YES — at threshold |
| **Sacramento** | 2.6M | ~1,600 | **~270-380** | YES — at threshold |
| **Fresno-Visalia** | 1.1M | ~700 | **~120-160** | **BORDERLINE** — may need all-PI |
| **Bakersfield** | 0.9M | ~600 | **~100-130** | **BORDERLINE** — may need all-PI |
| **Reno** | 0.5M | ~350 | **~60-80** | **NO** — too small for non-ST only |

---

## Data Sources

- **Crash data:** State DOT crash facts databases (ADOT, CHP/SWITRS for CA, etc.)
- **Injury severity distribution:** NHTSA CrashStats, FMCSA Large Truck & Bus Crash Facts
- **Population:** U.S. Census Bureau, DMA population estimates
- **Representation rates:** Legal services utilization studies, NAIC claims data
- **Platform penetration:** Pew Research Center 2025 social media adoption data (80% FB use among 30-49, 58% daily)
- **Funnel conversion:** WCTL AZ pilot validated: 1.0% CTR → 70% quiz start → 65% completion → 40% case-type filter → 85% submission → 85% verification ≈ 0.95% full-funnel conversion

---

## How To Use This In A Prospect Conversation

**Default position:** All-PI lead gen. This is the standard SC product — all case types, full funnel.

**Non-ST filter is an option when:**
1. The prospect explicitly asks for high-value cases only
2. The prospect's firm has a known strength in trucking, catastrophic, or wrongful death (like Tofer's #1 Truck vs. Car LA 2024)
3. The DMA passes viability threshold (≥200 monthly non-ST incidents)

**How to position it on the call:**
> *"The default product is all case types — the full PI funnel. That gives you the highest lead volume and the broadest optimization surface for the algorithm. But if Tofer's strength is trucking and severe cases, we can filter to non-soft-tissue only. Fewer leads — maybe 6-8 per month in LA instead of 30-60 — but each lead projects significantly higher attorney fee value. The projected ROAS actually goes UP because the case-value mix jumps 2-3x while the cost increase is modest."*

**Ready to show both tables:** Standard all-PI pricing + non-ST pricing side-by-side in the proposal.

---

*Second Chair — Non-Soft-Tissue Viability Framework — Central Reference*
*Methodology validated: WCTL Arizona pilot (2026-04)*
