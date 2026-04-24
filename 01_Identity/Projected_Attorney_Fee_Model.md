# Projected Attorney Fee Model — The Second Chair Day-One Measurement Framework

> **Canonical source of truth for how Second Chair measures lead value and performance.**
> Last updated: April 2026
> Status: Active — this is the pitch framework Second Chair leads with on all PI sales calls going forward
> Owners: Davis (creative + strategy), Alex (platform implementation), Sasha (sales delivery)

---

## Why This Document Exists

Most lead gen vendors in the personal injury space measure themselves on Cost Per Lead (CPL) or Cost Per Signed Case (CPSC). Both metrics are inadequate:

- **CPL** is a vanity metric. It tells the firm what they paid to get a phone number. It says nothing about what that phone number is worth.
- **CPSC** is a lagging metric. It tells the firm what they paid per signed case 6-12 months after the fact — and it averages case values as if a soft-tissue whiplash is equivalent to a major trucking case. For a firm with any meaningful high-value case exposure, CPSC actively hides the truth.

**The problem Second Chair solves with this model:** a firm can see the projected value of every lead cohort on day one — before any case has signed, before any revenue data has been shared, and without asking the firm to violate any confidentiality obligation to clients.

**The metric that leads:** Projected Attorney Fee per Lead → Projected ROAS on the cohort.

This is the number that lives on the dashboard from the moment the first lead is delivered.

---

## The One-Line Definition

**Projected Attorney Fee (PAF):** the dollar value of expected attorney fees a single lead will generate, computed from its Fit Score breakdown × sign probability × median attorney fee by case type.

**Projected ROAS:** the aggregate projected attorney fees across a lead cohort, divided by the cost of that cohort. Expressed as a multiple (e.g., 5.6×).

Both metrics exist on day one. Neither requires the firm to share any signed case outcome data, settlement amount, or client-identifying information.

---

## Why This Is Different From Every Other Vendor

No vendor in the PI lead gen space projects per-lead value in dollars. They all report CPL (before the sign) or CPSC (months after the sign). Neither gives the firm a real read on the **value of what's in the pipeline** before case outcomes start arriving.

For a firm like West Coast Trial Lawyers — with a $55.6M defective tire verdict on record and meaningful high-value case exposure across commercial vehicles, medical malpractice, and serious injury categories — the case-value mix is everything. One $200,000 trucking case inside a 100-lead cohort changes the economics more than ten soft-tissue cases. CPSC averages that away. Projected Attorney Fee captures it by scoring each lead individually before the sign.

This is not marginal. For high-value firms, this is the only honest measurement.

---

## The Formula

```
Projected Attorney Fee per Lead = Expected Attorney Fee × Sign Probability

Where:
  Expected Attorney Fee = f(injury severity, case type, treatment status, fault, recency)
  Sign Probability = f(Lead Grade: A/B/C/D)

Projected ROAS = Σ(Projected Attorney Fee per Lead) / Total Lead Cost
```

---

## Lookup Table 1 — Base Expected Attorney Fee by Case Type

Median values from Second Chair's own PI Lead Gen Economics research (Julian Cole, Feb 2026), cross-referenced with Miller & Zois settlement analyses, Insurance Information Institute data, and 2025 CasePeer settlement averages.

| Case Type | Median Settlement | Base Expected Attorney Fee (33%) |
|---|---|---|
| Soft tissue / minor MVA | $20,000 | **$6,600** |
| Moderate MVA (fracture, herniated disc, ACL) | $75,000 | **$25,000** |
| Severe MVA (TBI, spinal, permanent impairment) | $300,000+ | **$100,000+** |
| Slip and fall | $35,000 | **$11,500** |
| Rideshare (Uber/Lyft) | $50,000 | **$16,500** |
| Trucking / commercial vehicle | $90,000 | **$30,000** |
| Medical malpractice | $300,000 | **$100,000** |
| Wrongful death | $1,000,000+ | **$330,000+** |

**Contingency fee assumption:** 33.33% pre-litigation (standard). Post-filing rises to 40%, and trial can reach 40-45% — but 95% of PI cases settle before trial (Clio 2026), so the pre-litigation baseline is the conservative default.

**Sources:** PI_Lead_Gen_Economics.md (SC internal); Miller & Zois Settlement Analysis 2025; Insurance Information Institute 2022; CasePeer 2025 Settlement Examples; Advisement.com 2025; Nolo Attorney Fees 2024; 2025 web research cross-check.

---

## Lookup Table 2 — Sign Probability by Lead Grade

From PLATFORM_INTELLIGENCE.md scoring engine + industry benchmarks on exclusive lead conversion rates.

| Grade | Fit Score Composite | Quality Floor | Typical Sign Rate |
|---|---|---|---|
| **A** | ≥ 85 | ≥ 70 | **20-30%** |
| **B** | ≥ 65 | ≥ 50 | **12-20%** |
| **C** | ≥ 45 | ≥ 30 | **5-12%** |
| **D** | Below thresholds | — | **0-5%** |

**Note on industry benchmarks:** Exclusive web form leads convert at 15-25% overall (LawProNation, 2025). Grade A represents the top of that range. Grade D captures leads that survive the hard blocks (represented claimants, confirmed bots, missing consent) but still score low on fit.

---

## The Full Projection Math — Example

**Scenario:** 100-lead cohort delivered to a California firm in the Los Angeles Market at $360/lead.
**Spend:** $36,000

**Typical cohort mix (based on SC's scoring distribution):**

| Grade | # Leads | Avg Expected Fee | Avg Sign Probability | Projected Fee per Lead | Projected Cohort Fees |
|---|---|---|---|---|---|
| A | 20 | $25,000 (moderate MVA base) | 25% | $6,250 | **$125,000** |
| B | 35 | $17,500 (skewed toward moderate) | 16% | $2,800 | **$98,000** |
| C | 30 | $10,000 (mostly soft tissue) | 8% | $800 | **$24,000** |
| D | 15 | $5,000 (marginal) | 2% | $100 | **$1,500** |
| **Total** | **100** | — | — | — | **~$248,500** |

**Projected ROAS: $248,500 ÷ $36,000 ≈ 6.9×**

**The conservative version** (lowering all assumptions 25%): still lands at ~$186,000 projected fees, **~5.2× ROAS**.

**The optimistic version** (higher sign rates, better case mix): ~$320,000+ projected fees, **~8.9× ROAS**.

**Defensible range to quote on sales calls: 5 to 8× projected ROAS** for California Markets on day one.

This matches and slightly exceeds 2ndchair.net's published "3.5-7× ROAS" positioning, giving us room to be honest about the range without over-promising.

---

## How Projected ROAS Relates To Other Metrics

### Projected ROAS → Sign Rate Validation (ongoing)

As the firm reports sign events back (binary yes/no per lead), the projected model validates or adjusts:
- If actual sign rate matches the grade distribution (A signing at ~25%, B at ~16%, etc.), the projection stays on track
- If sign rate is below projection, the model adjusts and we tune lead quality
- If sign rate is above projection, the projection widens upward

**What the firm shares:** Just the yes/no per lead. No settlement data, no client names, no confidentiality concerns. This is a conversion event, not case data.

### Projected ROAS → Actual ROAS (long-term, when available)

Once cases start to close (typically 6-12+ months in for simple cases, 12-24+ for complex), the projected model can be refined against actuals — **if and only if** the firm is able to share aggregate revenue attribution from the lead source. Most PI settlements carry NDAs, so per-case attribution is rare. Aggregate attribution (total attorney fees across all signed cases from the source over a period) is the realistic ceiling for most firms.

**What Second Chair will NOT ask for:**
- Per-case settlement amounts
- Client-identifying case outcome data
- Anything that would violate Rule 1.6 confidentiality or a settlement NDA

**What Second Chair will accept gratefully if offered:**
- Aggregate attorney fee totals from the source (rolled up, no per-case detail)
- Time-bound aggregate reports (quarterly, annually)
- General confirmation the projected model is landing within tolerance

### CPSC as the Alongside Metric

Cost Per Signed Case still tracks alongside Projected ROAS as a secondary confirmation metric. Both improve together over time. But CPSC is not the primary metric Second Chair leads with — because:

1. **CPSC is lagging.** It requires 6-12+ months of case resolution data before it's meaningful.
2. **CPSC averages case values.** It hides the difference between a firm signing ten soft-tissue cases and a firm signing nine soft-tissue plus one major trucking case.
3. **CPSC creates comparison shopping.** Firms benchmark vendors on "who has the lower CPSC" without asking what's in the mix.

Projected Attorney Fee solves all three problems by computing per-lead value on day one, reflecting the case-value mix from the moment delivery begins.

---

## Verbatim Pitch Language (for Sales Calls)

### The Day-One Anchor

> *"Every lead we deliver has a Projected Attorney Fee attached to it — built from injury type, case type, treatment status, fault position, and recency. Across a 100-lead cohort in LA, we project the average attorney fee value to land somewhere between $1,800 and $2,800 per lead depending on the case mix. At $360 per lead cost, that's a projected 5 to 8 times return on ad spend — visible from day one, before anyone has signed anything."*

### The "How" Follow-Up

> *"The projection math uses published median settlement values by injury type — the Insurance Information Institute data, the Miller & Zois analyses, the same numbers your own firm would reference. We multiply by the sign probability tied to our lead grade — A-grade converts at 20-30%, B at 12-20%, and so on. It's a model you can audit line by line. No black box. The projected ROAS updates as your team reports which leads actually signed — if the sign rate matches the grade distribution, we stay on track. If it doesn't, we tune."*

### The Differentiator

> *"No vendor in this space reports like this. Most vendors either report CPL — what you paid to get a phone number — or CPSC after 6 to 12 months once cases start to close. Neither one shows you the VALUE of what's in the pipeline before the cases sign. Projected Attorney Fee is the only metric that gives you a real read on day one, because it's computed from what we actually control: the quality of the leads we generate."*

### The CPSC-Is-Misleading Callout

> *"One more thing on why we don't lead with cost per signed case. CPSC averages every signed case as if they're equivalent. A firm that signs ten soft-tissue cases shows the same CPSC as a firm that signs nine soft-tissue plus one major trucking case — even though the revenue is completely different. Projected Attorney Fee reflects the case-value mix because it scores each lead individually before the sign happens. For a firm with meaningful high-value case exposure, that distinction matters."*

### The Confidentiality-Honest Line

> *"We know most PI settlements now come with NDAs — that's the industry reality. We're not asking you to waive anything or violate any client confidentiality. The whole reason we built Projected Attorney Fee as the day-one metric is that it doesn't depend on you sharing case outcome data. It lives on our side of the relationship. If and when you're in a position to share aggregate attribution later, we refine it against actuals. But the measurement floor is solid from day one."*

---

## The Measurement Stack — Two Simple Tiers

### Tier 1 — Projected Attorney Fee + Projected ROAS (Day One)

**What Second Chair shows, unprompted:**
- Every lead's Projected Attorney Fee (dollar value)
- The cohort's aggregate Projected Attorney Fee
- The cohort's Projected ROAS (projected fees ÷ spend)

**What the firm shares to make this work:** Nothing. Zero data required.

**This is the primary metric.** This is what the pitch leads with. This is what the dashboard leads with.

### Tier 2 — Sign Rate Validation (when the firm is ready)

**What Second Chair asks for:** A simple yes/no per lead — did this sign.

**What the firm shares:** A conversion event, not case data. Not protected by privilege. Not restricted by Rule 1.6. Delivered via webhook, dashboard, or manual update.

**What Second Chair does with it:** Validates the projected model. If projections match signs, the model holds. If not, we tune.

### Tier 3 (Optional, Long-Term) — Aggregate Actual ROAS

**Only if the firm can share.** Totally acceptable if they can't.

**What Second Chair asks for:** Aggregate attorney fee totals from the source over time — no per-case detail.

**What the firm shares:** A rolled-up dollar number, no client-identifying information.

**What Second Chair does with it:** Refines Projected ROAS into Actual ROAS.

---

## Implementation Notes

### What's In The Dashboard

The Second Chair dashboard displays Projected Attorney Fee per lead and aggregate Projected ROAS on the cohort view. Every lead arrives with its fit score, grade, and dollar-denominated projection.

### What Clients Can Audit

The projection math is transparent. The base fee lookup table (Case Type → Median Fee), the sign probability table (Grade → Sign Rate), and the formula (Expected Fee × Sign Probability) are all available for client review. Nothing is hidden.

### How The Model Refines Over Time

As sign rate data accumulates (Tier 2), the projection weights adjust per-market. A firm that consistently signs at 28% from A-grade leads will see their projected ROAS widen upward. A firm signing below projection will see it tighten. The model is not static — it's calibrated against the real behavior of each firm's intake team.

---

## What This Replaces

This document supersedes the following CPSC-primary framings in prior Second Chair materials:

- `01_Identity/BRAND_MASTER.md` — "Primary Metric: Cost-Per-Signed-Case (CPSC)" → should be updated to reflect Projected Attorney Fee as primary, CPSC alongside
- `01_Identity/SERVICE_PERSONAL_INJURY.md` — "Cost-per-signed-case (CPSC) — reported by default" → should be updated to reflect Projected Attorney Fee as the day-one metric
- `22_Outreach/07_Prospects/Jacoby_Meyers/*` — older CPSC-anchored pitch materials (historical reference only; do not use for new clients)

The website (2ndchair.net) currently leads with ROAS as the headline KPI and CPSC alongside (per the March 30, 2026 roundtable audit). The website will need to add Projected Attorney Fee as the day-one surfaced metric. See `18_Website/TODO_Projected_Attorney_Fee_Website_Changes.md` for the implementation checklist.

---

## Sources

**Case value data:**
- `07_Research/01_Brand_Strategy_Research/01_Consumer_Deep_Dive/02_The_Lead_Machine/PI_Lead_Gen_Economics.md` (Julian Cole + Binet & Field, February 2026)
- Miller & Zois Settlement Analysis 2025
- Insurance Information Institute collision data 2022
- CasePeer 2025 Settlement Examples
- Advisement.com 2025 PI Averages
- Nolo Attorney Fees 2024
- On Point Legal Leads median jury award data 2024
- Clio 2026 Legal Trends Report

**Platform scoring mechanics:**
- `19_Platform/PLATFORM_INTELLIGENCE.md` — Fit Score and Quality Score engine, Grade composite formula, routing logic

**Industry benchmarks:**
- LawProNation Exclusive vs. Shared MVA Leads 2025 Analysis
- Taqtics Law Firm Lead Generation 2024
- RankWebs CPL Personal Injury Marketing 2024
- LegalBrandMarketing Lead Pricing 2024

**Website positioning:**
- `18_Website/ROUNDTABLE_AUDIT_2026-03-30.md` — Nigel Bogle roundtable establishing ROAS as headline KPI, CPSC alongside

**Confidentiality framework:**
- Model Rule 1.6 (ABA) / California Business & Professions Code § 6068(e)
- ABA guidance on attorney-vendor privilege
- Industry practice on aggregate marketing attribution from PI firms to lead vendors

---

*Second Chair — Projected Attorney Fee Model — April 2026*
*This is the canonical source. All other pitch materials should align to this framing.*
