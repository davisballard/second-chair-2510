# Second Chair — {{FIRM_NAME}}

**Pricing and Projected ROAS Model**
*{{MONTH YEAR}}*

---

Second Chair is a third-party lead generation company for personal injury law firms. We build DMA-specific creative, place the media ourselves, deliver compliant and territory-exclusive leads, and report on Projected ROAS from day one using our Fit Score model. This document covers what it costs to run in {{FIRM_NAME}}'s {{N}} operating markets, and how we get to the projected return on ad spend for every cohort.

---

## Pricing — {{FIRM_NAME}}'s {{N}} DMAs

{{SECTION: California DMAs with lockdown discount IF applicable. If prospect has no CA operations, delete this section.}}

### California — {{N}} DMAs with 15% State Lockdown Discount

When all seven California DMAs are purchased together, a **15% state lockdown discount** applies across the board. One compliance framework under SB-37, one creative system, one unified campaign architecture.

| Market | MOI | List Price | CA Lockdown | {{FIRM_NAME}} Office Cities |
|---|---|---|---|---|
| | | | | |

**California blended (pop-weighted, with lockdown): ~${{X}} per lead**

### Non-California Markets

| Market | State | MOI | Cost Per Lead | {{FIRM_NAME}} Office Cities |
|---|---|---|---|---|
| | | | | |

---

## How The MOI Pricing Works

Every market has a different cost to operate in. Los Angeles has 5,000+ PI firms competing for attention and the strictest advertising compliance regime in the country. Bakersfield has a few hundred firms. The lead quality is the same everywhere — the price reflects what it costs us to reach and qualify people in that specific market.

We quantify this with the **Market Operating Index (MOI)** — a composite score from 1.0 to 10.0, built from six weighted factors:

| Factor | Weight | What It Measures |
|---|---|---|
| Competition & Media Cost | 25% | Cost per click for PI keywords, number of competing firms, CPM environment |
| Legal Viability Rate | 25% | What percentage of motor vehicle accidents become viable cases |
| Market Size | 15% | DMA population and annual accident volume |
| Case Value Competition | 15% | Average settlement values and jury verdicts in the market |
| Uninsured Motorist Rate | 10% | Percentage of at-fault drivers with no insurance |
| Market Quality Factors | 10% | Tourism, transient populations, seasonal patterns |

Each factor is scored 1–10, weighted, and combined. The MOI maps directly to price:

**Price = $175 + ($36.11 × (MOI − 1.0))**, rounded to the nearest $5.

Every MOI score is transparent and auditable.

---

## Portfolio Summary

| Region | DMAs | Offices | Blended Rate |
|---|---|---|---|
| | | | |
| **Full {{N}}-DMA portfolio** | **{{N}}** | **{{N}} cities** | **~${{X}}** |

---

## Starter Package Options

First packages are sold as pre-paid lead packages — **100 leads per DMA**. That's the quantity that gets past Meta's algorithm learning phase and into real optimized performance. Leads are delivered as we generate them; a 100-lead package in a single DMA fills in roughly 5–7 weeks.

| Option | DMAs | Leads | Investment |
|---|---|---|---|
| **1. Primary Market Only** | 1 | 100 | **${{X}}** |
| **2. Top 3 Markets** | 3 | 300 | **${{X}}** |
| **3. Full CA Lockdown** (if applicable) | 7 | 700 | **${{X}}** |
| **4. Full Footprint** | {{N}} | {{N}}00 | **${{X}}** |

Renewals run at 50+ leads per DMA. Every renewal benefits from the optimization of the first 100 — better targeting, better creative, lower CPL over time.

> Why 100 leads per DMA? See `../../01_Playbooks/Why_100_Leads_Per_DMA.md`

---

## How We Project Return On Ad Spend

The metric we lead with is **Projected Attorney Fee per Lead → Projected ROAS**. Every lead we deliver carries a dollar-denominated projection on day one — built from our Fit Score model × sign probability by lead grade × median attorney fee by case type. Aggregate the cohort, divide by spend, and you have Projected ROAS before any case has signed.

This is the number on the dashboard from the moment the first lead delivers.

> Full model: `../../../01_Identity/Projected_Attorney_Fee_Model.md`

### The Formula

```
Projected Attorney Fee per Lead = Expected Attorney Fee × Sign Probability

  Expected Fee = f(injury severity, case type, medical treatment, fault, recency)
  Sign Probability = f(Lead Grade: A / B / C / D)

Projected ROAS = Σ(Projected Attorney Fee per Lead) / Total Lead Cost
```

### Base Expected Attorney Fee by Case Type

Median settlement values (Insurance Information Institute, Miller & Zois, CasePeer 2025 data) × 33% standard pre-litigation contingency fee.

| Case Type | Median Settlement | Expected Attorney Fee |
|---|---|---|
| Soft tissue / minor MVA | $20,000 | **$6,600** |
| Moderate MVA (fracture, herniated disc, ACL) | $75,000 | **$25,000** |
| Severe MVA (TBI, spinal, permanent impairment) | $300,000+ | **$100,000+** |
| Slip and fall | $35,000 | **$11,500** |
| Rideshare (Uber/Lyft) | $50,000 | **$16,500** |
| Trucking / commercial vehicle | $90,000 | **$30,000** |
| Medical malpractice | $300,000 | **$100,000** |
| Wrongful death | $1,000,000+ | **$330,000+** |

### Sign Probability by Lead Grade

| Grade | Composite Fit Score | Sign Probability |
|---|---|---|
| **A** | 85+ | 20–30% |
| **B** | 65–84 | 12–20% |
| **C** | 45–64 | 5–12% |
| **D** | Below 45 | 0–5% |

### Example — 100-Lead {{PRIMARY_DMA}} Cohort at ${{X}} Spend

| Grade | # Leads | Avg Expected Fee | Sign Probability | Projected Fee per Lead | Cohort Contribution |
|---|---|---|---|---|---|
| A | 20 | | | | |
| B | 35 | | | | |
| C | 30 | | | | |
| D | 15 | | | | |
| **Total** | **100** | — | — | — | **~${{X}}** |

**Projected ROAS: ${{X}} ÷ ${{spend}} ≈ {{N}}×**

**Defensible day-one range: {{N}} to {{N}}× Projected ROAS.**

### How The Projection Validates Over Time

As the intake team works through the cohort and reports back which leads signed, the projected model validates or tunes against actual behavior. The firm shares only what it's able to share — typically a simple yes/no per lead on sign status. No settlement amounts, no client-identifying details, nothing that would touch confidentiality obligations.

---

## Non-Soft-Tissue Option — High-Value Cases Only

> **Include this section IF:** the prospect's DMA passes viability (≥200 monthly non-ST incidents) AND the firm has a known strength in trucking/catastrophic/wrongful death, or asks for high-value filtering.
> **Viability framework:** `../../../07_Research/02_Sales_Intelligence/Market_Analysis/Non_Soft_Tissue_Viability_Framework.md`
> **Remove this section IF:** DMA is not viable for non-ST, or the prospect has no interest in case-type filtering.

### {{PRIMARY_DMA}} Non-Soft-Tissue Viability

| Metric | All-PI | Non-Soft-Tissue Only |
|---|---|---|
| Est. monthly incidents | {{X}} | {{Y}} |
| Viable? (≥200/mo) | ✅ | {{✅ / ❌}} |
| Leads per day | 1-3 | 0.3-0.8 |
| 100-lead fills in | 5-7 weeks | 8-14 weeks |

### Non-Soft-Tissue Pricing — {{PRIMARY_DMA}}

| | All-PI (standard) | Non-Soft-Tissue Only |
|---|---|---|
| **Cost per lead** | ${{LIST}} | **${{LIST + ~$75}}** (narrower audience, higher CPA) |
| **100-lead investment** | ${{X}} | **${{Y}}** |
| **Avg projected attorney fee per lead** | ~$2,485 | **~$4,500-$7,000** |
| **Projected ROAS** | {{N}}-{{N}}× | **{{N}}-{{N}}×** (higher — fee growth outpaces cost increase) |

### Non-Soft-Tissue Starter Options

| Option | Case Types | Leads | Investment |
|---|---|---|---|
| **A — All Non-ST** | Trucking + severe MVA + pedestrian + DUI + motorcycle + rideshare | 100 | ${{Y}} |
| **B — Split Test (recommended)** | 50 all-PI + 50 non-ST | 100 | ${{blended}} |

---

## What's Included In Every Package

- **Territory exclusivity** in purchased DMAs — one firm per market, no sharing
- **DMA-specific creative** built from scratch for each market (no national templates)
- **{{state-specific compliance}} compliant creative** — no prohibited content, mandatory disclosures, full documentability
- **FCC 2025 one-to-one consent** with TrustedForm certificate on every lead
- **Full data package per lead** — contact, accident details, injury type, fit score, consent proof
- **Real-time dashboard** — Projected Attorney Fee per lead, Projected ROAS on the cohort, lead grade, delivery status, every ad running under the firm's name
- **Optional approval workflow** — review and approve ads before they go live, on a standing basis
- **Portal / email / webhook delivery** — whatever fits intake workflow

## Key Terms

**Territory Exclusivity** — When {{FIRM_NAME}} holds a DMA, no competing PI firm can purchase from Second Chair in that market.

**California State Lockdown** — 15% discount applies when all seven California DMAs are purchased together.

**Non-California Markets** — Priced at list. Each state is independent creative, compliance, and campaign work.

**Package Structure** — 100 leads per DMA for first package. Renewals at 50+ leads per DMA.

---

*Second Chair — {{FIRM_NAME}} — {{MONTH YEAR}}*
*Contact: sasha@2ndchair.net*
*Pricing valid through {{DATE}}. Territory availability subject to change.*
