# Second Chair — Tofer & Associates

**Pricing and Projected ROAS Model**
*April 2026*

---

Second Chair is a third-party lead generation company for personal injury law firms. We build Market-specific creative, place the media ourselves, deliver compliant and territory-exclusive leads, and report on Projected ROAS from day one using our Fit Score model. This document covers what it costs to run in Tofer & Associates' Los Angeles market — and, as the firm expands, how pricing scales across California.

---

## Pricing — Los Angeles (Tofer's Operating Market)

| Market | MOI | Cost Per Lead | Tofer Office Cities |
|---|---|---|---|
| **Los Angeles** | 8.0 | **$425** | Beverly Hills (HQ), Hawthorne, Upland, Woodland Hills |

All four Tofer offices sit within the Los Angeles Market. The single-Market price reflects actual operational cost in the most competitive PI market in the country — no lockdown discount applies for a single market.

## If Tofer Expands Within California — Lockdown Pricing

When all seven California Markets are purchased together, a **15% state lockdown discount** applies across the board. The discount exists because running one compliance framework under SB-37, one creative system, and one unified campaign architecture across the full California footprint creates real operational efficiency that we pass through. For a firm with aggressive California expansion plans, this materially changes the per-lead math.

| Market | MOI | List Price | CA Lockdown |
|---|---|---|---|
| **Los Angeles** | 8.0 | $425 | **$360** |
| SF–Oakland–San Jose | 6.7 | $380 | $325 |
| Riverside–San Bernardino | 5.5 | $340 | $290 |
| San Diego | 5.5 | $340 | $290 |
| Sacramento | 4.7 | $310 | $265 |
| Fresno–Visalia | 3.7 | $270 | $230 |
| Bakersfield | 3.4 | $260 | $220 |

**California lockdown blended (pop-weighted): ~$320 per lead.**

Lockdown is all-or-nothing across the 7 Markets. Scattered partial-state footprints stay at list price because the operational efficiency isn't there.

---

## How The MOI Pricing Works

Every market has a different cost to operate in. Los Angeles has 5,000+ PI firms competing for attention and the strictest advertising compliance regime in the country. Bakersfield has a few hundred firms. The lead quality is the same everywhere — the price reflects what it costs us to reach and qualify people in that specific market.

We quantify this with the **Market Operating Index (MOI)** — a composite score from 1.0 to 10.0, built from six weighted factors:

| Factor | Weight | What It Measures |
|---|---|---|
| Competition & Media Cost | 25% | Cost per click for PI keywords, number of competing firms, CPM environment |
| Legal Viability Rate | 25% | What percentage of motor vehicle accidents become viable cases |
| Market Size | 15% | Market population and annual accident volume |
| Case Value Competition | 15% | Average settlement values and jury verdicts in the market |
| Uninsured Motorist Rate | 10% | Percentage of at-fault drivers with no insurance |
| Market Quality Factors | 10% | Tourism, transient populations, seasonal patterns |

Each factor is scored 1–10, weighted, and combined. The MOI maps directly to price:

**Price = $175 + ($36.11 × (MOI − 1.0))**, rounded to the nearest $5.

Every MOI score is transparent and auditable. You can see exactly why LA costs what LA costs.

---

## Starter Package — Los Angeles

First packages are sold as pre-paid lead packages — **100 leads per Market**. That's the quantity that gets past Meta's algorithm learning phase and into real optimized performance. Leads are delivered as we generate them; a 100-lead LA package typically fills in roughly 5–7 weeks.

| Option | Markets | Leads | Investment |
|---|---|---|---|
| **Option 1 — Los Angeles Only (MVP)** ⭐ | 1 | 100 | **$42,500** |

Renewals run at 50+ leads per Market. Every renewal benefits from the optimization of the first 100 — better targeting, better creative, lower CPL over time.

> Why 100 leads per Market? See `../../01_Playbooks/Why_100_Leads_Per_Market.md`

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

Median settlement values (Insurance Information Institute, Miller & Zois, CasePeer 2025 data) × 33% standard pre-litigation contingency fee. 95% of PI cases settle before trial, so the pre-litigation baseline is the conservative default.

| Case Type | Median Settlement | Expected Attorney Fee |
|---|---|---|
| Soft tissue / minor MVA | $20,000 | **$6,600** |
| Moderate MVA (fracture, herniated disc, ACL) | $75,000 | **$25,000** |
| Severe MVA (TBI, spinal, permanent impairment) | $300,000+ | **$100,000+** |
| Slip and fall | $35,000 | **$11,500** |
| Rideshare (Uber/Lyft) | $50,000 | **$16,500** |
| **Trucking / commercial vehicle** | **$90,000** | **$30,000** |
| Medical malpractice | $300,000 | **$100,000** |
| Wrongful death | $1,000,000+ | **$330,000+** |

*Note for Tofer: given the firm's #1 Truck vs. Car LA 2024 recognition, the trucking case-value line is worth highlighting. Tofer's case mix likely skews toward higher-value segments than the industry baseline.*

### Sign Probability by Lead Grade

Every lead is scored by our dual-scoring engine (Fit Score + Quality Score) and assigned a composite Grade. The grade maps to sign probability based on industry benchmarks for exclusive web-form leads.

| Grade | Composite Fit Score | Sign Probability |
|---|---|---|
| **A** | 85+ | 20–30% |
| **B** | 65–84 | 12–20% |
| **C** | 45–64 | 5–12% |
| **D** | Below 45 | 0–5% |

### Example — 100-Lead Los Angeles Cohort at $42,500 Spend

| Grade | # Leads | Avg Expected Fee | Sign Probability | Projected Fee per Lead | Cohort Contribution |
|---|---|---|---|---|---|
| A | 20 | $25,000 | 25% | $6,250 | **$125,000** |
| B | 35 | $17,500 | 16% | $2,800 | **$98,000** |
| C | 30 | $10,000 | 8% | $800 | **$24,000** |
| D | 15 | $5,000 | 2% | $100 | **$1,500** |
| **Total** | **100** | — | — | — | **~$248,500** |

**Projected ROAS: $248,500 ÷ $42,500 ≈ 5.8×**

Conservative scenario (lower fee assumptions, lower sign rates): ~4.5×.
Optimistic scenario (better case mix given Tofer's trucking strength): ~7.5×.

**Defensible day-one range for Tofer LA: 4.5 to 7.5× Projected ROAS.**

### How The Projection Validates Over Time

As Tofer's intake team (Carlos's team) works through the cohort and reports back which leads signed, the projected model validates or tunes against actual behavior:

- If the actual sign rate matches the grade distribution, the projection holds
- If signs come in above projection, the projection widens upward
- If signs come in below projection, the model tightens and we adjust lead quality

The firm shares only what it's able to share — typically a simple yes/no per lead on sign status. No settlement amounts, no client-identifying details, nothing that would touch confidentiality obligations. The projected ROAS remains the primary dashboard metric regardless.

**For Carlos specifically:** this plugs directly into his existing Looker dashboard stack. We deliver lead-level Projected Attorney Fee and Fit Score via portal/webhook → his Zapier workflows → his Looker KPIs. The measurement layer is additive, not a rip-and-replace.

---

## Non-Soft-Tissue Option — If Tofer Wants High-Value Cases Only

Tofer's #1 Truck vs. Car LA 2024 recognition and their catastrophic-injury focus suggests they may want leads filtered to **non-soft-tissue only** — trucking, severe MVA (fracture/TBI/spinal), wrongful death, pedestrian/cyclist, DUI victim, rideshare. No whiplash or minor sprains.

> Viability methodology: `../../../07_Research/02_Sales_Intelligence/Market_Analysis/Non_Soft_Tissue_Viability_Framework.md`

### LA Market Non-Soft-Tissue Viability

| Metric | All-PI | Non-Soft-Tissue Only |
|---|---|---|
| Est. monthly incidents (LA Market) | 8,000-10,000 | **1,500-2,000** |
| Viability threshold (≥200/month) | ✅ far exceeds | **✅ far exceeds (7-10x threshold)** |
| Leads per day | 1-3 | 0.3-0.8 |
| 100-lead package fills in | 5-7 weeks | 8-14 weeks |
| **Verdict** | Standard product | **Highly viable for LA** |

**LA is one of the strongest Markets in the country for non-soft-tissue** — dense freeway network (I-5, I-10, I-15, I-110, 405, 101), heavy commercial truck routes, high rideshare density on Westside, significant pedestrian/cyclist exposure in urban corridors.

### Non-Soft-Tissue Pricing — Los Angeles

| | All-PI (standard) | Non-Soft-Tissue Only |
|---|---|---|
| **Cost per lead** | $425 | **$500** (est. — narrower audience, higher CPA) |
| **100-lead investment** | $42,500 | **$50,000** |
| **Avg projected attorney fee per lead** | ~$2,485 | **~$5,500** (case-value mix jumps 2-3x) |
| **Projected ROAS (100-lead cohort)** | 4.5-7.5× | **7-10×** |

**Why the ROAS goes UP despite higher CPL:** The numerator (projected attorney fee) grows faster than the denominator (lead cost). A $500 lead projecting $5,500 in fee value = 11× per lead at the midpoint. Even at conservative sign rates, the portfolio ROAS exceeds all-PI.

### Non-Soft-Tissue Case Mix in LA (estimated)

| Case Type | % of Non-ST Volume | Avg Settlement | Expected Attorney Fee |
|---|---|---|---|
| **Moderate-to-Severe MVA** | 39-49% | $75K-$300K+ | $25,000-$100,000+ |
| **DUI Victim** | 24-32% | $100K-$500K | $33,000-$165,000 |
| **Pedestrian/Cyclist** | 22-29% | $50K-$250K | $16,500-$82,500 |
| **Motorcycle** | 17-23% | $112,500 median | $37,500 |
| **Trucking/Commercial** | 7-10% | $90K-$500K+ | $30,000-$165,000+ |
| **Rideshare** | 1-2% | $50K | $16,500 |

*Note: Tofer's trucking strength means the firm's real case-value realization on trucking leads is likely above median — the ROAS upside on a non-ST cohort could be significant.*

### Starter Package Options — Non-Soft-Tissue

| Option | Case Types | Leads | Investment | Est. Projected ROAS |
|---|---|---|---|---|
| **A — All Non-ST (recommended)** | Trucking + severe MVA + pedestrian + DUI + motorcycle + rideshare | 100 | **$50,000** | 7-10× |
| **B — Trucking + Severe MVA Only** | Trucking + fracture/TBI/spinal MVA only | 100 | **$55,000** (narrower still) | 8-12× |
| **C — Split Test** | 50 all-PI + 50 non-ST | 100 | **$46,250** (blended) | Comparison data |

**Recommended if non-ST:** Option A or Option C (split test). Option C gives Carlos direct comparison data in his Looker dashboards — all-PI cohort performance vs. non-ST cohort, same timeframe. That's the data Alex needs to make the Phase 2 decision.

---

## What's Included In The Package

- **Territory exclusivity** in Los Angeles — one firm per Market, no sharing
- **Market-specific creative** built from scratch for LA metro (Westside, South Bay, Valley, Inland Empire edge) — no national templates
- **SB-37 compliant creative** — no prohibited content, mandatory disclosures, full documentability
- **FCC 2025 one-to-one consent** with TrustedForm certificate on every lead
- **Full data package per lead** — contact, accident details, injury type, Fit Score grade, Projected Attorney Fee, consent proof
- **Real-time dashboard** — Projected Attorney Fee per lead, Projected ROAS on the cohort, lead grade distribution, delivery status, every ad running under Tofer's name
- **Integration-friendly delivery** — portal, email, webhook, or custom — designed to plug into existing intake/automation stacks (relevant for Carlos's Zapier + Looker setup)
- **Optional approval workflow** — review and approve ads before they go live, on a standing basis

## Key Terms

**Territory Exclusivity** — When Tofer holds LA, no competing PI firm can purchase from Second Chair in the LA Market. Not "exclusive leads." Exclusive market.

**No Guarantee** — We do not offer CPSC guarantees. Our position and reasoning are explained in full if the topic comes up.

**Package Structure** — 100 leads for the first package. Renewals at 50+ leads. Leads delivered as generated (~1–3/day in LA).

---

*Second Chair — Tofer & Associates — April 2026*
*Contact: sasha@2ndchair.net*
*Pricing valid through June 30, 2026. Territory availability subject to change.*
