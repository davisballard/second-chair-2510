# Market Baseline Pricing Framework

> **Type:** Internal pricing methodology — not for external distribution
> **Status:** Active
> **Date:** March 2026 · DMA→Market terminology migration 2026-04-23 · MOI recalibration (top-10 states) 2026-04-23
> **Supersedes:** `State_Lead_Pricing_By_State.md` (tier-based pricing)

> ✅ **MOI RECALIBRATION — TOP 10 STATES COMPLETE (2026-04-23, v1.1):** Section 3 below is fully recalibrated for the new state-pure-Market geometry. Top 10 states (CA, FL, TX, NY, IL, GA, PA, NJ, AZ, WA) — every Market re-scored from scratch using the 6 weighted factors. **40 Markets total** (CA expanded from 6→7 in v1.1: split former Greater LA + Coachella into CA-01 LA Core + CA-04 Inland Empire + Coachella, renumbered CA-03 through CA-07 by population). **Tofer locked at $265 for CA-06 Central Valley** (formerly CA-05 in v1.0) through current renewal window.
>
> ⚠️ **REMAINING:** Sections 3B and 3C (additional states beyond the top 10) still reference old Nielsen DMAs and need recalibration in a future pass. The Appendix at the bottom of this doc has not been updated yet — refer to Section 3 for the canonical top-10 numbers.

---

## Section 1: The Market Operating Index (MOI)

A composite score (1.0–10.0) reflecting what it costs Second Chair to deliver qualified leads in a given Market. Higher score = higher operating cost = higher lead price.

**The score is NOT a quality judgment.** Lead quality standard is the same in every market. The score explains the price.

### Six Weighted Factors

| Factor | Weight | What It Measures | Higher Score Means |
|--------|--------|-----------------|-------------------|
| **Competition & Media Cost** | 25% | Google CPC for PI keywords, vendor density, CPM environment | More expensive to buy attention |
| **Legal Viability Rate** | 25% | What % of MVAs become viable cases (fault system, no-fault thresholds, SOL length) | Harder to find viable leads — costs more per viable lead |
| **Market Size** | 15% | Market population, annual MVA volume | More people = more noise = harder to cut through |
| **Case Value Competition** | 15% | Average settlements, jury verdicts → attracts more competitors | Higher values attract more competition for those leads |
| **Uninsured Motorist Rate** | 10% | % of at-fault drivers with no insurance | More waste in the lead pool — dead leads that can't recover |
| **Market Quality X-Factors** | 10% | Tourist markets, transient populations, military relocations, seasonal patterns | More unreliable leads = higher waste rate |

### How Each Factor Is Scored (1–10)

**Competition & Media Cost (25%)**
- 1–3: CPC under $150, fewer than 500 PI firms in Market
- 4–6: CPC $150–$300, 500–2,000 PI firms
- 7–8: CPC $250–$400, 2,000–4,000 PI firms, heavy vendor density
- 9–10: CPC $300–$500+, 4,000+ PI firms, extreme saturation (LA, NYC)

**Legal Viability Rate (25%)**
- 1–3: At-fault state, pure comparative negligence, no threshold to clear, 2+ year SOL
- 4–5: At-fault state with modified comparative negligence (50–51% bar)
- 6–7: Choice no-fault (verbal threshold or full tort election) — must screen for tort status
- 8–9: No-fault with tort threshold (FL permanent injury, NJ verbal threshold)
- 10: Strictest no-fault threshold (NY serious injury — fracture/permanent limitation only)

**Market Size (15%)**
- 1–3: Market under 1M population
- 4–5: 1M–3M population
- 6–7: 3M–7M population
- 8–9: 7M–13M population
- 10: 13M+ population (LA, NYC)

**Case Value Competition (15%)**
- 1–3: Average PI settlement under $15K, limited plaintiff-friendly venue reputation
- 4–6: $15K–$22K average, moderate venue reputation
- 7–8: $22K–$28K average, known plaintiff-friendly venues (Cook County, Philadelphia)
- 9–10: $28K+ average, highest jury verdicts nationally

**Uninsured Motorist Rate (10%)**
- 1–3: Under 10% uninsured (NY at 8.6%, states with strong enforcement)
- 4–5: 10–14% uninsured (AZ 10.6%, PA 11.0%, national average ~15.4%)
- 6–7: 14–18% uninsured (TX 14.5%, NJ 14.1%, IL 15.2%)
- 8–10: 18%+ uninsured (CA 20.4%, FL 20.6%, GA 19.0%, WA 19.1%)

**Market Quality X-Factors (10%)**
- 1–3: Stable residential population, low seasonal variation
- 4–6: Moderate transient factors (military bases, college towns, moderate tourism)
- 7–8: Significant transient population (major tourist corridors, seasonal snowbird markets)
- 9–10: Extreme transient factors (Las Vegas strip, Orlando I-4 corridor)

### Data Sources

| Data Point | Source | Year |
|-----------|--------|------|
| Uninsured motorist rates | Insurance Research Council via Insurance Information Institute | 2023 (published 2025) |
| Market populations | Nielsen DMA rankings | 2024–2025 |
| Google Ads CPC | SpyFu/SEMrush benchmarks, iLawyer Marketing 2025 report, existing SC research | 2024–2025 |
| PI firm counts | Existing SC Market targeting research | 2025–2026 |
| Case values | Existing SC market analysis, jury verdict reporters | 2024–2025 |
| Fault systems / SOL | State statutes, III no-fault backgrounder | Current as of March 2026 |
| MVA volume | NHTSA CrashStats (2.44M injuries nationally in 2023) | 2023 |

---

## Section 2: Score-to-Price Mapping

Linear mapping from MOI score to lead price. The formula:

**Price = $175 + ($36.11 × (MOI Score − 1.0))**

Rounded to nearest $5. This produces:

| MOI Score Range | Lead Price Range | What This Means for the Attorney |
|----------------|-----------------|--------------------------------|
| **8.0–10.0** | $425–$500 | High operating cost market. Media costs are extreme, competition is intense. Same lead quality — price reflects our cost to operate here. |
| **6.0–7.9** | $355–$425 | Above-average operating costs. Strong market fundamentals with meaningful competition. |
| **4.0–5.9** | $285–$355 | Moderate operating costs. Balanced market — real volume, manageable competition. |
| **2.0–3.9** | $210–$285 | Lower operating costs. Less competition, lower media costs. Attorney's cost-per-signed-case math is often most favorable here. |
| **1.0–1.9** | $175–$210 | Lowest operating cost markets. Minimal competition. Clean economics. |

### Price Floor and Ceiling

- **Floor: $175/lead** — Below this, margin compression makes the market uneconomical for SC's quality standard.
- **Ceiling: $500/lead** — Capped for launch. Even NYC and LA don't exceed $500 at launch. Revisit after 6 months of operating data.
- **Exception: NYC capped at $525** — The only market that may exceed $500 due to extreme no-fault screening costs + media environment. Revisit quarterly.

### Margin Check

At every price point, SC must maintain 55%+ gross margin:

| Lead Price | Max Allowable Cost | Target Margin |
|-----------|-------------------|--------------|
| $500 | $225 | 55% |
| $400 | $180 | 55% |
| $300 | $135 | 55% |
| $200 | $90 | 55% |

SC's target cost is $75–$150/lead. Even at $150 cost, margins clear 55% at every price point above $335. Markets priced below $335 need to hit $75–$100 cost targets, which is achievable in low-competition Markets.

---

## Section 3: Top 10 States — Market Scoring and Pricing

> **Recalibrated 2026-04-23** for the new 109-Market state-pure framework (`04_Audience/Geo_Framework/National_Market_Definitions.md`). Each Market re-scored from scratch using the 6 weighted factors. Where a new Market combines multiple former Nielsen DMAs, the scores reflect the blended dynamics (population-weighted media costs, combined competitor universe, etc.) — NOT a simple average of constituent DMA scores.
>
> **Tofer-locked pricing:** Where a client has a signed agreement with locked CPL, the locked rate is shown inline as `(TF: $XYZ)` next to the new Market CPL. Tofer's signed Central Valley package locks $265 through current renewal window — this rate stays regardless of new MOI math. Future renewals will use the recalibrated CPL unless re-locked.
>
> **Score legend:** Each cell shows the 1.0–10.0 sub-score for that factor. MOI = weighted sum (Comp/Media 25% + Viability 25% + Size 15% + Case Value 15% + Uninsured 10% + X-Factors 10%). CPL = `$175 + $36.11 × (MOI − 1.0)`, rounded to nearest $5.

---

### 1. California

| | |
|---|---|
| **Fault System** | Pure comparative negligence (at-fault) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 20.4% (IRC 2023) |
| **Regulatory Notes** | SB37 compliance required for lead gen advertising |
| **Viability Notes** | No tort threshold — any injury can file. Pure comparative means even 99% at-fault plaintiff can recover 1%. Favorable for lead viability but high uninsured rate creates waste. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **CA-01** Greater LA Core | 13.7M | 9.5 | 3.0 | 10.0 | 9.0 | 8.5 | 7.0 | **8.0** | **$425** |
| **CA-02** Bay Area | 7.7M | 8.0 | 3.0 | 7.0 | 9.0 | 8.5 | 5.0 | **6.5** | **$375** |
| **CA-03** Sacramento + Far North | 5.0M | 4.0 | 3.0 | 6.0 | 4.5 | 8.5 | 4.0 | **4.6** | **$305** |
| **CA-04** Inland Empire + Coachella | 4.7M | 6.0 | 3.0 | 6.5 | 5.5 | 8.5 | 5.5 | **5.5** | **$340** |
| **CA-05** San Diego + Imperial | 3.5M | 6.0 | 3.0 | 5.5 | 5.5 | 8.5 | 6.0 | **5.4** | **$335** |
| **CA-06** Central Valley | 3.0M | 3.5 | 3.0 | 3.5 | 3.5 | 8.5 | 3.0 | **3.8** | **$275** *(TF: $265)* |
| **CA-07** Central Coast | 1.5M | 3.5 | 3.0 | 2.5 | 4.5 | 8.5 | 5.5 | **4.1** | **$285** |

**California Market Notes (v1.1, 2026-04-23):**
- **CA-01 Greater LA Core** (LA, Orange, Ventura, Inyo) — the coastal/urban LA Market, **split out from former Greater LA + Coachella in v1.1.** Anchor-preserved at MOI 8.0 / $425 to maintain continuity with Tofer pitch deck and Alex's prior pitches. CPC $250–$500+, 4,500–6,000 PI firms, Spanish-language campaigns mandatory.
- **CA-02 Bay Area** is the unchanged former SF–Oakland–San Jose DMA, just renamed. Premium case values from tech workforce. High media costs across all channels. Lower MVA volume per capita than LA.
- **CA-03 Sacramento + Far North** is the largest county-count Market (27 counties) — combines former Sac–Stockton–Modesto + Chico-Redding + Eureka + Reno-CA-slice + Medford-CA-slice DMAs. Sacramento dominates pricing dynamics; far north adds rural lead waste but minimal media cost.
- **CA-04 Inland Empire + Coachella** (San Bernardino + Riverside whole) — **NEW in v1.1, split out from Greater LA.** Combines Inland Empire freeway corridors (high MVA volume, growing population) + Palm Springs/Coachella desert. Reflects how PI firms actually segment LA-area opportunity: most LA-coastal firms don't compete in IE; most IE firms don't compete on the coast. **Sells separately from CA-01** — two whales possible in the geography instead of one.
- **CA-05 San Diego + Imperial** adds Imperial County (CA portion of former Yuma–El Centro DMA) to San Diego DMA. Imperial drags Comp/Media slightly below SD-only. SC team proximity advantage. Military demographics (Camp Pendleton). Mexico border adds claim complexity.
- **CA-06 Central Valley** combines former Fresno-Visalia + Bakersfield DMAs. Agricultural belt. Combined population 3.0M makes this a meaningful exclusivity package vs. the previous fragmented sub-1M DMAs. **Tofer locked at $265/lead through current renewal window — see `23_Clients/Tofer_and_Associates/Tofer_Service_Agreement.md`.** *(Note: was CA-05 in v1.0; renumbered to CA-06 in v1.1 to maintain pop-descending naming convention.)*
- **CA-07 Central Coast** combines former Monterey-Salinas + Santa Barbara-Santa Maria-SLO DMAs. Smallest CA Market (just clears 1M floor). Coastal tourism + agricultural Salinas + college market (UCSB, Cal Poly) elevate X-Factors.

**Revenue impact of v1.1 split:** Old CA-01 at $400 (single Market) becomes CA-01 at $425 + CA-04 at $340 (two Markets, two possible whales). Same ZIP universe, two exclusivity packages.

---

### 2. Florida

| | |
|---|---|
| **Fault System** | No-fault (PIP) with tort threshold; modified comparative negligence 51% bar (HB 837, March 2023) |
| **Statute of Limitations** | 2 years (reduced from 4 by HB 837) |
| **Uninsured Motorist Rate** | 20.6% (IRC 2023) — highest among top 10 states |
| **PIP Minimum** | $10,000/person |
| **Tort Threshold** | Permanent injury, significant scarring, or death — plaintiff must clear this to sue at-fault driver for pain and suffering |
| **Regulatory Notes** | HB 837 (2023) dramatically changed FL PI landscape: reduced SOL, shifted to modified comparative negligence, changed medical damages evidence rules. FL is the only state that doesn't require bodily injury liability insurance. |
| **Viability Notes** | No-fault screening required — leads must clear permanent injury threshold before they're viable tort claims. Combined with highest uninsured rate (20.6%) and HB 837 reforms, FL has the most waste in the lead funnel of any top state. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **FL-01** South Florida | 6.2M | 8.0 | 8.0 | 7.0 | 7.0 | 9.0 | 8.0 | **7.8** | **$420** |
| **FL-02** Tampa Bay | 5.0M | 6.0 | 8.0 | 6.0 | 5.5 | 9.0 | 7.5 | **6.9** | **$390** |
| **FL-03** Central FL / Orlando | 4.4M | 6.0 | 8.0 | 6.0 | 5.5 | 9.0 | 8.5 | **7.0** | **$390** |
| **FL-04** North FL / Jacksonville | 2.0M | 4.0 | 8.0 | 4.0 | 4.5 | 9.0 | 4.0 | **5.6** | **$340** |
| **FL-05** Panhandle | 2.2M | 3.0 | 8.0 | 4.0 | 4.0 | 9.0 | 6.0 | **5.5** | **$340** |
| **FL-06** SW Florida + Treasure Coast | 2.8M | 4.0 | 8.0 | 4.5 | 5.0 | 9.0 | 7.0 | **6.0** | **$355** |

**Florida Market Notes:**
- **FL-01 South Florida** (Miami–Dade, Broward, Palm Beach, Monroe). Largely the unchanged former Miami–Ft. Lauderdale DMA, just renamed and includes Monroe. Highest PI lead volume per capita in the US. 70%+ Hispanic — bilingual campaigns mandatory. No-fault screening + 20.6% uninsured = highest waste rate of any state. **Note:** West Palm Beach was previously its own DMA at MOI 6.3 / $365 — Palm Beach County now rolls into FL-01, lifting the county to FL-01's $420 pricing. Possible sub-Market split (FL-01a Miami-Broward, FL-01b Palm Beach) if a wealth-positioning client demands.
- **FL-02 Tampa Bay** combines Tampa–St. Petersburg + parts of former Lakeland-Winter Haven (Polk County). Larger combined Market (5.0M) lifts Size score and supports a small price increase from old Tampa-only ($370 → $390). I-4 western terminus. Large retiree population, different injury profiles and case values.
- **FL-03 Central FL / Orlando** (Orlando-Daytona-Melbourne core). Morgan & Morgan HQ market. I-4 corridor — "the most dangerous highway in America." Major tourist population creates high transient lead factor (visitors in MVAs leave state before filing) — drives X-Factors to 8.5.
- **FL-04 North FL / Jacksonville** (FL portion only — split off GA portion of former Jacksonville DMA per Rule 2). Slightly larger Market than old Jax-only thanks to Putnam, Baker. I-95 corridor. Military presence (NAS Jax, Mayport).
- **FL-05 Panhandle** combines former Pensacola–Ft. Walton (FL portion only — split from Mobile-Pensacola), Panama City, and Tallahassee (FL portion only). State-purify Rule 2 strips out the AL/MS/GA portions. Combined 2.2M creates a viable Market vs. previously fragmented sub-1M DMAs. Military (NAS Pensacola) + college (FSU/FAMU) + beach tourism elevate X-Factors.
- **FL-06 SW Florida + Treasure Coast** combines former Cape Coral–Ft. Myers + Gainesville + sliver of W. Palm Beach overflow. Heavy snowbird seasonality (Nov–Apr peaks). Possible seasonal pricing adjustment after 12 months of data.

---

### 3. Texas

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) — plaintiff must be less than 51% at fault |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 14.5% (IRC 2023) |
| **Regulatory Notes** | Straightforward at-fault system. No PIP requirement. Strong trucking/commercial vehicle corridor (I-35, I-10, I-45). |
| **Viability Notes** | Best margin state in our top 10. No no-fault threshold to screen through, moderate uninsured rate, CPC runs 40–60% below LA/NYC. High MVA volume driven by state size, speed limits, trucking corridors. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **TX-01** Dallas-Fort Worth Metroplex | 8.1M | 7.0 | 4.5 | 8.5 | 6.5 | 6.0 | 5.0 | **6.2** | **$365** |
| **TX-02** Greater Houston | 7.5M | 7.0 | 4.5 | 8.0 | 7.0 | 6.0 | 5.5 | **6.3** | **$365** |
| **TX-03** Austin + Hill Country | 2.5M | 4.5 | 4.5 | 4.0 | 4.5 | 6.0 | 4.0 | **4.5** | **$300** |
| **TX-04** San Antonio + South-Central | 2.6M | 4.0 | 4.5 | 4.5 | 4.5 | 6.0 | 5.0 | **4.6** | **$305** |
| **TX-05** Rio Grande Valley + Laredo + Corpus | 2.5M | 3.0 | 4.5 | 4.0 | 3.5 | 6.0 | 5.5 | **4.2** | **$290** |
| **TX-06** El Paso + West Texas | 1.3M | 3.0 | 4.5 | 3.0 | 4.0 | 6.0 | 5.5 | **4.1** | **$285** |
| **TX-07** East TX + Panhandle | 6.0M | 3.5 | 4.5 | 7.0 | 4.0 | 6.0 | 5.0 | **4.8** | **$310** |

**Texas Market Notes:**
- **TX-01 DFW Metroplex** unchanged from former Dallas-Ft. Worth DMA. I-35 trucking corridor — trucking MVAs carry higher case values. CPC $120–$300, dramatically cheaper than coastal mega-markets.
- **TX-02 Greater Houston** unchanged from former Houston DMA. I-10/I-45 trucking. Energy-sector commercial vehicle volume.
- **TX-03 Austin + Hill Country** unchanged from former Austin DMA. Tech-driven growth, younger demographics. Competition increasing but still moderate.
- **TX-04 San Antonio + South-Central** unchanged from former San Antonio DMA. I-35 corridor, significant military presence (Joint Base San Antonio). Lower competition than DFW/Houston.
- **TX-05 Rio Grande Valley + Laredo + Corpus** combines former McAllen-Edinburg + Laredo + Corpus Christi DMAs. Combined 2.5M creates a viable multi-metro Market vs. previously fragmented sub-1M DMAs. **Bilingual campaigns mandatory.** Lower case values offset by very low competition.
- **TX-06 El Paso + West Texas** combines former El Paso (TX portion only — split from El Paso DMA which crosses into NM) + Odessa-Midland + San Angelo + Abilene-Sweetwater. Permian Basin oil sector adds commercial-vehicle volume + high-net-worth demographics in Midland.
- **TX-07 East TX + Panhandle** is a "rest-of-state" rollup combining Tyler-Longview + Waco-Temple-Bryan + Beaumont-Port Arthur (TX portion) + Amarillo (TX portion) + Lubbock + Wichita Falls (TX portion) + Sherman-Ada (TX portion). Combined 6.0M is large but spread across multiple metros — Size score reflects total pop, but Comp/Media stays low because none of the constituent metros are individually competitive.

---

### 4. New York

| | |
|---|---|
| **Fault System** | No-fault with serious injury threshold (strictest in the US) |
| **Statute of Limitations** | 3 years (most favorable among top states) |
| **Uninsured Motorist Rate** | 8.6% (IRC 2023) — lowest among top 10 states |
| **PIP Minimum** | $50,000/person (highest in the country) |
| **Serious Injury Threshold** | NY Insurance Law §5102(d): death, dismemberment, significant disfigurement, fracture, loss of fetus, permanent loss of use, permanent consequential limitation of use, significant limitation of use, or 90/180-day disability rule |
| **Regulatory Notes** | Strictest no-fault threshold nationally. Every lead must be screened against 9 categories. However: 3-year SOL gives more time, $50K PIP is generous, and 8.6% uninsured is the lowest in our top 10 — meaning almost every lead has an insured at-fault party. |
| **Viability Notes** | The screening cost is extreme but the yield on screened leads is high. Attorneys pay premium because leads that clear NY's threshold are genuinely case-ready. Highest case values in the country partially offset the screening burden. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **NY-01** NYC Metro (NY-only) | 12.0M | 9.5 | 10.0 | 9.0 | 10.0 | 3.0 | 6.5 | **8.7** | **$455** |
| **NY-02** Capital Region + North Country | 1.8M | 3.0 | 10.0 | 3.5 | 4.0 | 3.0 | 3.5 | **5.0** | **$320** |
| **NY-03** Western NY | 2.5M | 3.5 | 10.0 | 4.5 | 4.5 | 3.0 | 3.0 | **5.3** | **$330** |
| **NY-04** Central + Southern Tier | 1.5M | 3.0 | 10.0 | 3.0 | 3.5 | 3.0 | 3.0 | **4.8** | **$310** |

**New York Market Notes:**
- **NY-01 NYC Metro (NY-only)** is the NY counties of the former NYC DMA — state-purified per Rule 2 (NJ portion → NJ-01, CT portion → CT-01). Total Market pop drops from 20M to 12M, but NY-licensed competitive density and CPC dynamics are identical. Slight Size and X-Factors downshifts pull MOI from 8.9 to 8.7. Still the highest-priced US Market. **Compliance note:** Buying NY-01 only does NOT cover NJ/CT — different state bars, different exclusivity wrappers required.
- **NY-02 Capital Region + North Country** combines former Albany-Schenectady-Troy + Burlington-Plattsburgh (NY portion) + Watertown DMAs. Combined 1.8M creates a viable Market vs. previously fragmented sub-1M DMAs. State capital + Adirondacks rural mix + military (Fort Drum) add modest X-Factors.
- **NY-03 Western NY** combines Buffalo + Rochester + Erie (PA portion stripped per Rule 2). Combined 2.5M is materially larger than either constituent alone.
- **NY-04 Central + Southern Tier** combines Syracuse + Binghamton (NY portion only) + Elmira (NY portion only) + Utica. State-purify removes PA portions of Binghamton/Elmira. Combined 1.5M passes 1M floor.
- **NY-wide:** Strictest no-fault threshold in the country (9-category §5102(d) screening). Low uninsured rate (8.6%) + highest case values ($22K–$30K avg) partially offset screening burden. Upstate markets (NY-02, NY-03, NY-04) share the same screening infrastructure as NY-01 — economical to operate at smaller scale.

---

### 5. Illinois

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 15.2% (IRC 2023) |
| **Regulatory Notes** | At-fault state, no PIP/no-fault complexity. Straightforward system. |
| **Viability Notes** | Cook County (Chicago) is widely considered the most plaintiff-friendly venue in the US. This drives higher case values AND attracts more competition for those cases. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **IL-01** Chicago Metro | 8.5M | 8.0 | 4.5 | 8.5 | 8.5 | 6.5 | 5.0 | **6.8** | **$385** |
| **IL-02** Central IL | 2.0M | 3.5 | 4.5 | 4.0 | 4.0 | 6.5 | 3.5 | **4.2** | **$290** |
| **IL-03** Downstate + Quad Cities (IL) + Metro East | 2.0M | 3.5 | 4.5 | 4.0 | 4.5 | 6.5 | 4.0 | **4.3** | **$295** |

**Illinois Market Notes:**
- **IL-01 Chicago Metro** is Chicago DMA state-purified per Rule 2 (IN counties — Lake, Porter, LaPorte — split off to IN-02). Pop drops from 9.5M to 8.5M but Cook County dynamics dominate: 2,800–3,500 PI firms, "nuclear verdict" reputation, extreme CPC. Slight Size downshift drops MOI from 6.9 to 6.8.
- **IL-02 Central IL** combines former Peoria-Bloomington + Champaign-Springfield-Decatur DMAs. Combined 2.0M crosses 1M floor cleanly. Multi-university presence (Illinois State, U of I, Illinois Wesleyan).
- **IL-03 Downstate + Quad Cities (IL) + Metro East** combines Rockford + St. Louis (IL portion) + Quad Cities (IL portion) + Paducah (IL portion). State-purify removes MO/IA/KY/IN portions. Metro East benefits from East St. Louis venue effects (plaintiff-friendly Madison County).

---

### 6. Georgia

| | |
|---|---|
| **Fault System** | Modified comparative negligence (50% bar, strict — plaintiff at exactly 50% fault recovers nothing) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 19.0% (IRC 2023) |
| **Regulatory Notes** | Anti-running legislation favors compliant lead gen operations — attorneys caught using runners face serious penalties. This creates demand for legitimate lead gen partners. |
| **Viability Notes** | At-fault state with no no-fault threshold. The 50% bar is slightly stricter than the 51% bar (IL, TX) — plaintiff at exactly 50% fault is barred. High uninsured rate (19.0%) creates meaningful waste. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **GA-01** Atlanta Metro | 6.5M | 7.0 | 4.5 | 7.0 | 6.0 | 8.0 | 5.0 | **6.1** | **$360** |
| **GA-02** Savannah + Coastal | 1.5M | 3.5 | 4.5 | 3.5 | 4.5 | 8.0 | 5.0 | **4.5** | **$300** |
| **GA-03** Augusta + Columbus + Albany + Macon-W | 3.0M | 4.0 | 4.5 | 4.5 | 4.0 | 8.0 | 4.5 | **4.7** | **$310** |

**Georgia Market Notes:**
- **GA-01 Atlanta Metro** (GA portion of Atlanta DMA — AL spillover stripped per Rule 2). 6.5M, 1,800–2,200 PI firms. Alex has existing relationships here. Anti-running legislation creates a regulatory moat for compliant lead gen. CPC $150–$350. I-285/I-85 interchange is one of the highest-accident corridors in the Southeast.
- **GA-02 Savannah + Coastal** combines former Savannah (GA portion — SC stripped) + Macon-Eastern + Brunswick area. Combined 1.5M passes 1M floor. Port city + I-95 trucking corridor + coastal tourism. Higher case values from commercial vehicle MVAs.
- **GA-03 Augusta + Columbus + Albany + Macon-W** combines former Augusta (GA portion — SC stripped) + Columbus GA (GA portion — AL stripped) + Albany + Macon (W) + Tallahassee (GA portion — FL stripped). Combined 3.0M is meaningful. Military presence at Fort Benning, Fort Moody. Master's Tournament in Augusta adds annual tourism factor.

---

### 7. Pennsylvania

| | |
|---|---|
| **Fault System** | Choice no-fault — drivers choose limited tort (can't sue for pain/suffering unless serious injury) or full tort (can always sue) at policy purchase |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 11.0% (IRC 2023) |
| **PIP Minimum** | $5,000/person |
| **Tort Election** | Limited tort = lower premiums but can only sue for pain/suffering if "serious injury" (similar to NY threshold). Full tort = higher premiums but full lawsuit rights. ~75% of PA drivers choose limited tort. |
| **Viability Notes** | Every lead must be screened for tort election status. ~75% limited tort means 3/4 of leads face a threshold before they can pursue pain and suffering claims. Full tort leads are more valuable. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **PA-01** Greater Philadelphia (PA portion) | 4.0M | 7.0 | 7.0 | 6.0 | 7.5 | 5.0 | 4.0 | **6.4** | **$370** |
| **PA-02** Pittsburgh + Western PA | 2.4M | 4.5 | 7.0 | 4.0 | 5.0 | 5.0 | 3.0 | **5.0** | **$320** |
| **PA-03** Central PA | 2.6M | 4.0 | 7.0 | 4.5 | 5.0 | 5.0 | 3.0 | **5.0** | **$320** |
| **PA-04** Northern + Northwest PA | 1.6M | 3.0 | 7.0 | 3.5 | 4.0 | 5.0 | 3.0 | **4.4** | **$300** |

**Pennsylvania Market Notes:**
- **PA-01 Greater Philadelphia (PA portion)** is the Philadelphia DMA state-purified per Rule 2 (NJ portion → NJ-02, DE portion → DE-01, MD portion → MD-01). Pop drops from 4.1M to 4.0M. Plaintiff-friendly Philly venue. Must screen every lead for limited vs. full tort election — meaningful operational cost. Sasha proximity. CPC $150–$320.
- **PA-02 Pittsburgh + Western PA** combines former Pittsburgh (PA portion — WV/OH stripped) + Johnstown-Altoona. Strong regional market with loyal local firm ecosystem. Steel/industrial heritage means more commercial vehicle traffic.
- **PA-03 Central PA** combines former Harrisburg-Lancaster-Lebanon-York + Wilkes-Barre-Scranton DMAs. Combined 2.6M makes this a more viable Market than either alone. I-76/I-83/I-81 corridors. Mix of suburban (Lancaster), capital (Harrisburg), and rural demographics.
- **PA-04 Northern + Northwest PA** combines former Erie + Elmira (PA portion only) + Binghamton (PA portion only). State-purify removes NY portions of Elmira/Binghamton. Combined 1.6M passes 1M floor.

---

### 8. New Jersey

| | |
|---|---|
| **Fault System** | Choice no-fault — verbal threshold (can only sue for pain/suffering with permanent injury) or zero threshold / full tort |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 14.1% (IRC 2023) |
| **PIP Minimum** | $15,000/person; liability minimums increased to $35K/$70K/$25K (Jan 2025) |
| **Verbal Threshold** | "Permanent injury" required to sue for pain and suffering. Most NJ drivers choose the verbal threshold (lower premiums). |
| **Viability Notes** | Similar screening burden to PA — must determine tort election. Verbal threshold creates a gate that most leads must clear. Dense PI firm concentration in northern NJ (NYC spillover) and southern NJ (Philly spillover). |

In the new state-pure framework, NJ has its own two Markets (state-purified per Rule 2 from former NYC and Philadelphia DMAs). NJ exclusivity now sells separately from NY/PA exclusivity — three different state-pure products instead of one cross-state DMA.

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **NJ-01** North NJ + NYC-NJ portion | 6.8M | 7.5 | 7.0 | 7.5 | 8.5 | 5.5 | 5.0 | **7.1** | **$395** |
| **NJ-02** South NJ + Philly-NJ portion | 2.5M | 5.5 | 7.0 | 4.5 | 6.5 | 5.5 | 4.0 | **5.7** | **$345** |

**New Jersey Market Notes:**
- **NJ-01 North NJ + NYC-NJ portion** (Bergen, Hudson, Essex, Morris, Passaic, Sussex, Union, Middlesex, Somerset, Hunterdon, Warren, Monmouth, Ocean). NJ counties of former NYC DMA, sharing NYC media market dynamics but operating under NJ verbal-threshold tort rules. NJ wealth (especially Bergen/Morris) drives Case Value to 8.5.
- **NJ-02 South NJ + Philly-NJ portion** (Camden, Burlington, Gloucester, Atlantic, Cape May, Cumberland, Salem, Mercer). NJ counties of former Philadelphia DMA. Atlantic City casino/tourism + Princeton wealth (Mercer) + Jersey Shore seasonal swings.
- **NJ-wide:** Same verbal-threshold tort screening burden as the PA limited-tort flow. Verbal threshold = "permanent injury" required for pain & suffering suit. Most drivers (verbal threshold = lower premiums) face the gate.
- **Compliance note:** Buying NJ does NOT cover NYC/Philadelphia core. NY-licensed firms pitching NJ residents need NJ bar admission or PHV. Same for PA-licensed firms in NJ-02.

---

### 9. Arizona

| | |
|---|---|
| **Fault System** | Pure comparative negligence (at-fault) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 10.6% (IRC 2023) |
| **Regulatory Notes** | ABS law permits PE-owned law firms — creates different competitive dynamics (well-capitalized firms buying leads at scale). |
| **Viability Notes** | Clean at-fault system with no threshold. Low uninsured rate for a Sun Belt state. The ABS (Alternative Business Structures) law means PE-backed firms operate here with bigger budgets, potentially driving up media costs faster than other comparable markets. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **AZ-01** Phoenix + Northern AZ | 5.5M | 5.5 | 3.0 | 7.0 | 5.0 | 5.0 | 5.0 | **4.9** | **$315** |
| **AZ-02** Tucson + SE AZ | 1.9M | 3.0 | 3.0 | 3.5 | 3.5 | 5.0 | 4.0 | **3.5** | **$265** |

**Arizona Market Notes:**
- **AZ-01 Phoenix + Northern AZ** combines Phoenix DMA + Flagstaff-Prescott + Yuma-El Centro (AZ portion only — CA portion of Yuma-El Centro DMA → CA-05). Combined 5.5M slightly larger than old Phoenix-only. Fast population growth. High Spanish-speaking percentage — bilingual campaigns recommended. ABS law means PE-owned firms compete aggressively for leads. I-10/I-17 interchange generates high MVA volume.
- **AZ-02 Tucson + SE AZ** is the unchanged former Tucson (Sierra Vista-Nogales) DMA. 1.9M crosses 1M floor cleanly. I-10 corridor. Border (Nogales). Military presence (Davis-Monthan AFB) + university (U of A) add modest transient factor.

---

### 10. Washington

| | |
|---|---|
| **Fault System** | Pure comparative negligence (at-fault) |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | 19.1% (IRC 2023) |
| **Regulatory Notes** | Higher insurance minimums than many states. 3-year SOL is favorable for lead gen (more time for attorneys to pursue). |
| **Viability Notes** | Clean at-fault system, no threshold. The high uninsured rate (19.1%) is the main negative — nearly 1 in 5 drivers has no insurance. 3-year SOL partially compensates by giving more runway. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **WA-01** Greater Seattle + Western WA | 5.5M | 6.0 | 3.0 | 6.5 | 6.5 | 8.0 | 4.5 | **5.5** | **$335** |
| **WA-02** Eastern WA | 2.3M | 3.0 | 3.0 | 4.0 | 3.5 | 8.0 | 3.5 | **3.8** | **$275** |

**Washington Market Notes:**
- **WA-01 Greater Seattle + Western WA** combines Seattle-Tacoma + Portland-OR (WA portion = SW WA / Vancouver-Camas, ~500K) + Yakima. State-purify removes OR portion of Portland DMA → OR-01. Combined 5.5M is meaningfully larger than old Seattle-only. Existing SC operations. Tech demographics drive higher average case values (higher income = higher economic damages). I-5 corridor. Rainy conditions contribute to higher MVA rates per capita.
- **WA-02 Eastern WA** combines Spokane (WA portion only — ID panhandle stripped) + Tri-Cities WA + Wenatchee. State-purify removes ID portion of Spokane DMA → ID-01. Combined 2.3M crosses 1M floor cleanly. Military (Fairchild AFB) + agricultural Yakima Valley + Hanford nuclear cleanup workforce.

---

## Section 3B: Additional States — Tier 1–2 Market Scoring

The following states contain Markets that score into Tier 1–2 (MOI 5.0+) and require canonical sub-dimensional breakdowns. Added March 2026 to support the full Market Ranked List (`04_Audience/Market_Ranked_List.md`).

---

### 11. Michigan

| | |
|---|---|
| **Fault System** | No-fault with serious impairment threshold (among the strictest nationally, second only to NY) |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | ~20% (IRC 2023) |
| **PIP Minimum** | $50,000 to unlimited (choice — MI reformed PIP in 2019 to allow tiered coverage) |
| **Serious Impairment Threshold** | "Serious impairment of body function" — an objectively manifested impairment of an important body function that affects the person's general ability to lead a normal life |
| **Viability Notes** | MI's no-fault system creates screening costs comparable to NY. The 2019 PIP reform introduced tiered coverage options, complicating the screening landscape further. High uninsured rate (~20%) compounds screening waste. However, 3-year SOL and viable leads clearing the threshold are high-value. Declining population in Detroit Market but still a top-15 market nationally. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Detroit** | 4.4M | 6.0 | 9.0 | 6.5 | 6.0 | 8.0 | 3.5 | **6.8** | **$385** |
| **Grand Rapids** | 0.8M | 3.0 | 9.0 | 2.5 | 4.5 | 8.0 | 3.0 | **5.2** | **$325** |
| **Flint–Saginaw** | 0.6M | 2.5 | 9.0 | 2.0 | 4.0 | 8.0 | 3.0 | **4.9** | **$315** |
| **Lansing** | 0.5M | 2.0 | 9.0 | 1.5 | 3.5 | 8.0 | 4.0 | **4.7** | **$310** |

**Michigan X-Factors:**
- Detroit: Top-15 US Market by population despite decades of population decline. ~1,500–2,000 PI firms. MI's strict no-fault screening pushes operating costs up significantly — similar to NY upstate markets in pricing dynamics. CPC $150–$300 (lower than coastal but higher than Midwest average due to attorney density). Auto industry heritage means high vehicle density and MVA volume per capita.
- Grand Rapids: Growing west MI metro. Lower competition than Detroit. Same MI no-fault screening requirement drives viability score to 9.0, pushing this small market into Tier 2 pricing despite modest population. Furniture/manufacturing sector = commercial vehicle traffic.
- Flint/Saginaw: Post-industrial corridor in central MI. Declining population but still ~0.6M Market. MI no-fault keeps MOI elevated. Lower case values than Detroit. Very low competition.
- Lansing: State capital, Michigan State University. MI no-fault screening drives viability to 9.0. College population adds moderate transient factor. Low media costs.

---

### 12. Massachusetts

| | |
|---|---|
| **Fault System** | No-fault with threshold ($2,000 in medical expenses or "serious injury") |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | ~6.2% (IRC 2023) — among the lowest nationally |
| **PIP Minimum** | $8,000/person |
| **Threshold** | $2,000 in reasonable medical expenses OR serious injury (death, dismemberment, significant disfigurement, fracture, loss of sight/hearing). The $2K medical threshold is relatively low — most MVAs with any treatment will cross it. |
| **Viability Notes** | MA's no-fault threshold is the easiest to clear among no-fault states (only $2K in medical bills). This means more leads survive screening than in NY, FL, or MI. Combined with the lowest uninsured rate in our portfolio (~6.2%) and high case values (Northeast market), MA offers strong unit economics despite high media costs. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Boston** | 4.8M | 7.5 | 7.5 | 6.5 | 7.0 | 2.5 | 4.0 | **6.4** | **$370** |
| **Springfield–Holyoke** | 0.6M | 3.0 | 7.5 | 2.0 | 5.0 | 2.5 | 3.0 | **4.2** | **$290** |

**Massachusetts X-Factors:**
- Boston: Top-10 US Market. ~2,000+ PI firms. Northeast CPC environment ($300–$450). High case values driven by high cost of living, high income demographics, and plaintiff-friendly venue reputation. Major university/hospital concentration means sophisticated medical documentation on injury claims. Lowest uninsured rate in our scored states (~6.2%) means almost every lead has an insured at-fault party — significantly less funnel waste than FL or CA. No existing SC team relationships in market.
- Springfield/Holyoke: Western MA, I-91 corridor. Small market but benefits from MA no-fault system (viability 7.5) and very low uninsured rate. Lower case values and competition than Boston. Clean economics at $290/lead.

---

### 13. DC / Maryland / Virginia (Contributory Negligence)

| | |
|---|---|
| **Fault System** | Contributory negligence in all three jurisdictions (DC, MD, VA) — plaintiff at ANY fault recovers nothing |
| **Statute of Limitations** | DC: 3 years, MD: 3 years, VA: 2 years |
| **Uninsured Motorist Rate** | DC: ~10%, MD: ~13%, VA: ~9% (IRC 2023) |
| **Regulatory Notes** | DC, MD, and VA are three of only five US jurisdictions using pure contributory negligence (along with AL and NC). This is the harshest liability standard — if the plaintiff is even 1% at fault, they recover zero. |
| **Viability Notes** | Contributory negligence is structurally hostile to PI lead gen. More leads become non-viable because any contributory fault bars recovery entirely. This doesn't create the same screening cost as no-fault (there's no threshold to screen against), but it does mean a higher percentage of leads will be rejected by attorneys during case evaluation. The cases that survive are strong — clear liability, documented injuries, clean facts. Washington DC Market is large (6.4M) with high case values driven by federal workforce income levels. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Washington DC** | 6.4M | 7.0 | 5.5 | 7.0 | 7.0 | 5.0 | 5.0 | **6.2** | **$365** |
| **Baltimore** | 2.8M | 5.0 | 5.5 | 4.5 | 5.5 | 5.5 | 3.5 | **5.0** | **$320** |
| **Norfolk–Virginia Beach** | 1.8M | 4.0 | 5.5 | 4.0 | 5.0 | 4.0 | 6.0 | **4.7** | **$310** |
| **Richmond** | 1.0M | 3.5 | 5.5 | 3.0 | 4.5 | 4.0 | 3.5 | **4.1** | **$285** |

**DC/MD/VA X-Factors:**
- Washington DC: 6.4M Market spanning DC, suburban MD (Montgomery, Prince George's, Frederick), and Northern VA (Fairfax, Arlington, Loudoun). Federal workforce = high income = high economic damages in PI cases. Government contractors and lobbyists drive premium case values. I-95/I-495 (Capital Beltway) among the most congested corridors in the US — high MVA volume. Moderate transient factor from government rotations and diplomatic community. CPC $200–$400 (Northeast-level pricing). Cross-state compliance: contributory negligence in all three jurisdictions, but each has different procedural rules.
- Baltimore: Separate Market from DC. I-95 corridor, port city. Lower case values than DC metro. More blue-collar demographics. Moderate competition. Less attractive than DC but benefits from MD's 3-year SOL.
- Norfolk/Virginia Beach/Hampton Roads: VA's largest military concentration — Norfolk Naval Station (world's largest naval base), Langley AFB, multiple shipyards. Military personnel and dependents create significant transient population (X-factor 6.0). VA contributory negligence applies. I-64 corridor. CPC $150–$250.
- Richmond: VA state capital. Smaller market, lower competition. VA contributory negligence limits viability. I-95/I-64 junction. Stable residential demographics.

---

### 14. Minnesota

| | |
|---|---|
| **Fault System** | No-fault with threshold ($4,000 in medical expenses or 60-day disability) |
| **Statute of Limitations** | 6 years (longest in the US for PI) |
| **Uninsured Motorist Rate** | ~10% (IRC 2023) |
| **PIP Minimum** | $40,000/person (second-highest nationally after NY) |
| **Threshold** | Medical expenses exceeding $4,000 OR disability for 60+ days OR permanent disfigurement, permanent injury, or death |
| **Viability Notes** | MN's no-fault threshold is moderate — $4K in medical bills or 60 days of disability. More leads survive screening than in NY or MI, but fewer than in MA ($2K threshold). The 6-year SOL is the longest in the country — a major advantage for lead gen because leads remain viable far longer. Low uninsured rate (~10%) means clean funnel. Combined with $40K PIP (generous coverage), MN offers solid unit economics. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Minneapolis–St. Paul** | 3.7M | 5.0 | 7.5 | 6.0 | 5.5 | 4.0 | 3.0 | **5.6** | **$340** |

**Minnesota X-Factors:**
- Minneapolis–St. Paul: Twin Cities metro, ~3.7M Market population (cross-state with western WI). ~1,200–1,800 PI firms. Midwest CPC environment ($200–$350). Harsh winter driving conditions contribute to higher MVA rates per capita during November–March. 6-year SOL is a major operational advantage — leads generated today remain viable for years. Low uninsured rate means less funnel waste. No existing SC relationships in market. Stable residential population, minimal transient factors.

---

### 15. Tennessee

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 1 year (shortest in the US, tied with LA) |
| **Uninsured Motorist Rate** | ~20% (IRC 2023) |
| **Regulatory Notes** | Standard at-fault state with no PIP/no-fault complexity. The critical factor is the 1-year SOL — the shortest in the country. |
| **Viability Notes** | TN's 1-year SOL fundamentally changes the lead gen calculus. Leads older than 6–8 months are often too close to the deadline for attorneys to take on. This compresses the conversion window significantly vs. states with 2–3 year SOLs. Combined with the highest uninsured rate (~20%) among at-fault states, TN has more funnel waste than its tort system would otherwise suggest. Scored at 5.0 viability (0.5 above standard modified 51% states) to reflect the SOL pressure. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Nashville** | 1.9M | 5.0 | 5.0 | 4.5 | 5.0 | 8.0 | 6.0 | **5.3** | **$330** |
| **Memphis** | 1.3M | 4.0 | 5.0 | 4.0 | 4.0 | 8.0 | 4.5 | **4.7** | **$310** |
| **Knoxville** | 0.9M | 3.5 | 5.0 | 2.5 | 4.0 | 8.0 | 4.0 | **4.3** | **$295** |

**Tennessee X-Factors:**
- Nashville: Fast-growing metro (~1.9M Market). Music tourism and bachelor/bachelorette party industry creates meaningful transient MVA population — visitors in accidents who may leave state before pursuing claims. I-24/I-40/I-65 interchange is a major accident corridor. Growing attorney market as population expands. CPC $150–$300 (Southeast average). The 1-year SOL means SC must prioritize lead freshness — any delay in delivery or attorney follow-up directly erodes the conversion window.
- Memphis: Cross-state Market (TN/MS/AR). TN dominates population. I-40 corridor, FedEx hub generates significant commercial vehicle traffic. Lower case values than Nashville. The 1-year SOL applies to TN-side leads; MS and AR portions have longer SOLs (3 years each) but different fault systems.
- Knoxville: East TN, I-40/I-75 junction. University of Tennessee adds moderate college-town transient factor. Lower competition than Nashville or Memphis. Same 1-year SOL constraint.

---

### 16. Nevada

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~10% (IRC 2023) |
| **Regulatory Notes** | Standard at-fault state. Nevada was previously removed from the Top 10 Market Targets per strategic decision — included here for scoring completeness. |
| **Viability Notes** | NV's tort system is straightforward — no no-fault, no unusual thresholds. Low uninsured rate for a Western state (~10%). The defining characteristic is the extreme tourism/transient X-factor in Las Vegas, which drives up waste: tourists in MVAs who leave the state, visitors with out-of-state insurance creating coverage complications, and seasonal volume patterns tied to convention/event calendar. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Las Vegas** | 2.3M | 5.0 | 4.5 | 4.5 | 5.0 | 4.5 | 9.5 | **5.2** | **$325** |

**Nevada X-Factors:**
- Las Vegas: 2.3M Market population, but the effective MVA population is much larger due to ~40M annual visitors. The Strip and surrounding resort corridor generates high tourist-involved MVA volume where claimants leave the state post-accident — a lead quality challenge. Convention traffic creates predictable volume spikes (CES in January, etc.). Rideshare MVAs (Uber/Lyft to/from casinos) are a growing segment. CPC $200–$350. X-Factor score of 9.5 is the highest in our portfolio — only Orlando (8.5) comes close. **Note:** Strategic hold per team decision. Scoring included for market universe completeness.

---

## Section 3C: Additional States — Tier 3 Market Scoring

Remaining states with Tier 3 Markets (MOI 4.0–4.9). Added March 2026.

---

### 17. Colorado

| | |
|---|---|
| **Fault System** | Modified comparative negligence (50% bar) |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | ~16% (IRC 2023) |
| **Viability Notes** | At-fault state with 50% bar (same as GA). 3-year SOL is favorable. Existing SC operations in CO. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Denver** | 3.0M | 5.0 | 4.5 | 5.0 | 5.0 | 6.5 | 3.5 | **4.9** | **$315** |
| **Colorado Springs** | 0.8M | 3.0 | 4.5 | 2.5 | 4.0 | 6.5 | 5.0 | **4.0** | **$285** |

**Colorado X-Factors:**
- Denver: Growing metro (~3.0M Market). West region CPC ($200–$300). I-25/I-70 corridors. Existing SC market operations. Moderate competition.
- Colorado Springs: Major military presence (Fort Carson, USAFA, Peterson SFB, Schriever SFB) drives X-factor to 5.0. Military transient population creates lead quality variation.

---

### 18. Hawaii

| | |
|---|---|
| **Fault System** | No-fault (PIP required) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~8% (IRC 2023) |
| **PIP Minimum** | $10,000/person |
| **Viability Notes** | HI no-fault system with a serious injury threshold. Island geography means all MVAs are local — no interstate complexity. Tourism and military (Pearl Harbor, Schofield Barracks, Hickam) create extreme transient/X-factor. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Honolulu** | 1.0M | 3.0 | 7.0 | 3.0 | 5.0 | 3.5 | 8.0 | **4.9** | **$315** |

**Hawaii X-Factors:**
- Honolulu: Island Market — all of Oahu plus outer islands. ~10M annual visitors create massive transient MVA population. Military concentration (Pearl Harbor, multiple bases) adds to transient factor. Isolated media market — limited national vendor competition. Higher cost of living = higher case values than mainland markets of similar size.

---

### 19. North Carolina (Contributory Negligence)

| | |
|---|---|
| **Fault System** | Contributory negligence — plaintiff at ANY fault recovers nothing |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | ~7% (IRC 2023) — low |
| **Viability Notes** | NC is one of five contributory negligence jurisdictions. The all-or-nothing rule kills more leads than standard at-fault states. However, 3-year SOL is favorable and very low uninsured rate (~7%) means minimal insurance-related waste. Large, growing metros (Charlotte, Raleigh-Durham) with significant PI firm presence. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Charlotte** | 2.7M | 5.5 | 5.5 | 4.5 | 5.0 | 3.0 | 3.0 | **4.8** | **$310** |
| **Raleigh–Durham** | 1.6M | 4.5 | 5.5 | 4.0 | 5.0 | 3.0 | 4.5 | **4.6** | **$305** |

**North Carolina X-Factors:**
- Charlotte: Banking capital of the Southeast. 2.7M Market, growing rapidly. I-77/I-85 corridors. Despite large population, contributory negligence + low uninsured rate limit the MOI. Case values are moderate.
- Raleigh-Durham: Research Triangle (Duke, UNC, NC State). College/tech demographics. Growing metro. Contributory negligence limits viability. College transient population = moderate X-factor (4.5).

---

### 20. Oregon

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~12% (IRC 2023) |
| **Viability Notes** | Standard at-fault system. Portland is the only significant Market. Higher-than-average case values for the West region. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Portland** | 2.0M | 5.0 | 4.5 | 4.5 | 5.5 | 5.0 | 3.0 | **4.7** | **$310** |

**Oregon X-Factors:**
- Portland: West Coast metro, I-5 corridor. Rainy climate contributes to higher MVA rates. Growing market with increasing competition. Case values above Midwest average due to West Coast cost of living. CPC $200–$350.

---

### 21. Indiana

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~14% (IRC 2023) |
| **Viability Notes** | Standard at-fault state. Indianapolis is the primary Market. Crossroads of America — I-65/I-70/I-69 intersection generates high through-traffic MVA volume. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Indianapolis** | 2.0M | 4.5 | 4.5 | 4.5 | 4.5 | 6.0 | 4.0 | **4.6** | **$305** |

**Indiana X-Factors:**
- Indianapolis: "Crossroads of America" — I-65/I-70/I-69 intersection creates high through-traffic MVA volume. Indianapolis Motor Speedway events generate periodic tourism spikes. Midwest CPC ($200–$300). Moderate PI firm density.

---

### 22. Ohio

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | 12.4% (IRC 2023) |
| **Viability Notes** | Standard at-fault state. Three major Markets (Columbus, Cincinnati, Cleveland) plus smaller markets. Midwest CPC environment. Moderate uninsured rate. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Columbus** | 2.0M | 4.5 | 4.5 | 4.5 | 4.5 | 5.0 | 4.0 | **4.5** | **$300** |
| **Cincinnati** | 2.2M | 4.5 | 4.5 | 4.5 | 4.5 | 5.0 | 3.0 | **4.4** | **$300** |
| **Cleveland** | 1.8M | 4.5 | 4.5 | 4.0 | 5.0 | 5.0 | 3.0 | **4.4** | **$300** |

**Ohio X-Factors:**
- Columbus: State capital, Ohio State University. Growing metro. OSU adds moderate college transient factor (X-factor 4.0). I-70/I-71 corridors.
- Cincinnati: Cross-state Market (OH/KY/IN). OH dominates population. KY portion is choice no-fault (different screening requirements). I-71/I-75 corridors. Stable residential market.
- Cleveland: Lake Erie metro, I-90/I-77 corridors. Higher case values than Columbus/Cincinnati due to plaintiff-friendly Cuyahoga County venue reputation. Declining population but still significant.

---

### 23. Connecticut

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~7% (IRC 2023) — low |
| **Viability Notes** | At-fault state with straightforward system. Fairfield County (southwestern CT) is part of the NYC Market. The Hartford–New Haven Market covers the rest of the state. High cost of living drives higher case values. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Hartford–New Haven** | 1.5M | 5.0 | 4.5 | 4.0 | 6.0 | 3.0 | 3.0 | **4.5** | **$300** |

**Connecticut X-Factors:**
- Hartford/New Haven: Northeast CPC environment ($250–$400). Two major metros in one Market. Insurance industry HQ (Hartford) means sophisticated defense bar. Yale (New Haven) and UConn add academic medical center documentation advantages for plaintiff cases. Low uninsured rate = clean funnel.

---

### 24. Alabama (Contributory Negligence)

| | |
|---|---|
| **Fault System** | Contributory negligence — plaintiff at ANY fault recovers nothing |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~18% (IRC 2023) — high |
| **Viability Notes** | AL is the harshest combination in our portfolio: contributory negligence (any fault = zero recovery) + high uninsured rate (~18%). Both factors increase lead funnel waste. Viability scored at 6.0 (highest among contributory negligence states) to reflect the compounding effect. Despite this, AL has multiple Markets with military presence that provide unique lead sources. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Birmingham** | 1.1M | 3.5 | 6.0 | 3.0 | 4.0 | 7.5 | 3.0 | **4.5** | **$300** |
| **Huntsville–Decatur** | 0.6M | 2.5 | 6.0 | 2.0 | 3.5 | 7.5 | 5.0 | **4.2** | **$290** |
| **Mobile** | 0.7M | 2.5 | 6.0 | 2.0 | 3.5 | 7.5 | 3.0 | **4.0** | **$285** |

**Alabama X-Factors:**
- Birmingham: Largest AL metro. I-65/I-20 junction. Moderate PI firm density. Contributory negligence + 18% uninsured is a tough combination — but firms in AL are accustomed to this and value clean, pre-screened leads.
- Huntsville/Decatur: Redstone Arsenal (US Army), NASA Marshall Space Flight Center. Significant military/defense contractor population = transient X-factor (5.0). Growing tech hub.
- Mobile: Gulf Coast port city. I-10/I-65 corridors. Lower case values. Some overlap with Pensacola FL Market in the Mobile Bay area.

---

### 25. Utah

| | |
|---|---|
| **Fault System** | No-fault with threshold ($3,000 in medical expenses or serious injury) |
| **Statute of Limitations** | 4 years |
| **Uninsured Motorist Rate** | ~8% (IRC 2023) — low |
| **PIP Minimum** | $3,000/person |
| **Viability Notes** | UT's $3K no-fault threshold is among the lowest nationally — most MVAs with treatment will cross it. Combined with low uninsured rate and 4-year SOL, UT has clean lead economics. Viability scored at 5.5 (below MA's 7.5 and above standard at-fault 4.5) because the threshold exists but is easy to clear. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Salt Lake City** | 1.9M | 4.0 | 5.5 | 4.5 | 4.5 | 3.5 | 3.0 | **4.4** | **$300** |

**Utah X-Factors:**
- Salt Lake City: ~1.9M Market. I-15 corridor, Wasatch Front. Moderate competition. Ski tourism creates seasonal MVA variation (winter ice/snow conditions). 4-year SOL is among the most favorable nationally. Low uninsured rate = clean funnel.

---

### 26. Kentucky

| | |
|---|---|
| **Fault System** | Choice no-fault — drivers choose between full tort and basic reparations benefit (no-fault) |
| **Statute of Limitations** | 2 years (1 year for PIP benefits) |
| **Uninsured Motorist Rate** | ~11% (IRC 2023) |
| **PIP Minimum** | $10,000/person |
| **Viability Notes** | KY choice no-fault is similar to PA/NJ — leads must be screened for tort election status. Drivers choosing basic reparations face a threshold before pursuing pain/suffering claims. Viability scored at 6.5 (between PA at 7.0 and standard at-fault at 4.5). |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Louisville** | 1.0M | 3.5 | 6.5 | 3.0 | 4.5 | 5.0 | 3.0 | **4.4** | **$300** |
| **Lexington** | 0.5M | 2.5 | 6.5 | 1.5 | 4.0 | 5.0 | 4.0 | **4.0** | **$285** |

**Kentucky X-Factors:**
- Louisville: I-65/I-64/I-71 junction. Cross-state metro with southern IN. Kentucky Derby/bourbon tourism adds minor seasonal factor. Moderate PI firm density.
- Lexington: University of Kentucky, horse racing industry. College population adds transient X-factor (4.0). Small market but KY choice no-fault premium keeps MOI at 4.0.

---

### 27. Missouri

| | |
|---|---|
| **Fault System** | Pure comparative negligence |
| **Statute of Limitations** | 5 years (among the longest nationally) |
| **Uninsured Motorist Rate** | ~14% (IRC 2023) |
| **Viability Notes** | MO pure comparative negligence is the most plaintiff-favorable fault system — any injury at any fault level can pursue recovery. 5-year SOL is the second-longest for PI (after MN's 6 years). Both factors are favorable for lead gen. Low viability score (3.0) reflects the ease of converting leads — fewer funnel barriers. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **St. Louis** | 2.8M | 5.0 | 3.0 | 4.5 | 5.0 | 6.0 | 3.0 | **4.3** | **$295** |
| **Kansas City** | 2.3M | 4.5 | 3.0 | 4.5 | 4.5 | 6.0 | 3.0 | **4.1** | **$285** |

**Missouri X-Factors:**
- St. Louis: Cross-state Market (MO/IL). MO pure comparative dominates. I-70/I-44/I-55 junction. Gateway to the West — significant through-traffic. IL portion uses modified 51% (different rules). CPC $200–$300.
- Kansas City: Cross-state Market (MO/KS). MO pure comparative dominates. I-70/I-35 junction. KS portion uses modified 50% + no-fault hybrid (different screening). CPC $180–$280.

---

### 28. Wisconsin

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 3 years |
| **Uninsured Motorist Rate** | ~13% (IRC 2023) |
| **Viability Notes** | Standard at-fault state with 3-year SOL (favorable). Moderate uninsured rate. Milwaukee is the primary Market. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Milwaukee** | 1.6M | 4.0 | 4.5 | 4.0 | 4.5 | 5.5 | 3.0 | **4.3** | **$295** |

**Wisconsin X-Factors:**
- Milwaukee: I-94/I-43 corridors. Midwest CPC ($200–$300). Moderate PI firm density. Harsh winter driving conditions increase MVA rates November–March. Some overlap with Chicago Market for southern WI counties.

---

### 29. Louisiana

| | |
|---|---|
| **Fault System** | Pure comparative negligence |
| **Statute of Limitations** | 1 year (shortest nationally, tied with TN) |
| **Uninsured Motorist Rate** | ~14% (IRC 2023) |
| **Viability Notes** | LA has the same 1-year SOL challenge as TN — leads older than 6–8 months are often too close to deadline for attorneys. Pure comparative negligence is favorable, but the compressed conversion window significantly increases waste. Viability scored at 3.5 (0.5 above standard pure comparative) to reflect SOL pressure. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **New Orleans** | 1.0M | 3.5 | 3.5 | 3.0 | 4.5 | 6.0 | 8.0 | **4.3** | **$295** |

**Louisiana X-Factors:**
- New Orleans: Extreme tourism market (Mardi Gras, Jazz Fest, Super Bowl events, conventions). X-factor 8.0 driven by tourist-involved MVAs where claimants leave the state. I-10 corridor. Port city with commercial vehicle traffic. 1-year SOL requires aggressive lead freshness management — possibly the tightest conversion window in the portfolio.

---

### 30. Oklahoma

| | |
|---|---|
| **Fault System** | Modified comparative negligence (51% bar) |
| **Statute of Limitations** | 2 years |
| **Uninsured Motorist Rate** | ~20% (IRC 2023) — high |
| **Viability Notes** | Standard at-fault state but with very high uninsured rate (~20%), similar to FL and CA. This creates significant lead funnel waste. Oil/energy industry presence means commercial vehicle traffic. |

| Market | Pop. | Comp/Media (25%) | Viability (25%) | Size (15%) | Case Value (15%) | Uninsured (10%) | X-Factors (10%) | **MOI** | **CPL** |
|-----|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Oklahoma City** | 1.5M | 3.5 | 4.5 | 4.0 | 4.0 | 8.0 | 3.5 | **4.4** | **$300** |
| **Tulsa** | 1.0M | 3.0 | 4.5 | 3.0 | 3.5 | 8.0 | 3.0 | **4.0** | **$285** |

**Oklahoma X-Factors:**
- Oklahoma City: State capital, I-35/I-40/I-44 junction. Oil/energy industry commercial vehicles. CPC $150–$250. High uninsured rate (~20%) is the primary MOI driver.
- Tulsa: I-44 corridor. Oil/energy sector. Lower competition than OKC. Same high uninsured rate challenge.

---

## Section 4: Pricing Modifiers

### Multi-Market Bundle Discounts

| Bundle Size | Discount | Example |
|------------|---------|---------|
| 2–3 Markets in same state | 10% off individual Market pricing | Dallas ($365) + Houston ($365) + San Antonio ($300) = $1,030 × 0.90 = **$927/month for 3 leads each** |
| 4+ Markets in same state or full state | 15% off individual Market pricing | All 7 CA Markets at list = $2,325 × 0.85 = **$1,976** |

**Rules:**
- Each Market must be explicitly named in the contract
- Bundle discount applies to the CPL, not the total volume
- Example: Dallas at 10% off = $365 × 0.90 = **$329/lead** (bundled)
- No stacking — 15% is the max discount regardless of bundle size

### What Is NOT a Separate Modifier

- **No-fault complexity:** Already baked into the Legal Viability Rate factor (25% of MOI). FL, NY, NJ, PA leads cost more because viability screening is built into the score — no hidden surcharge.
- **Spanish-language campaigns:** Not a modifier. SC runs bilingual by default in markets where demographics require it (Miami, LA, Phoenix, border TX markets). This is operating cost, not upcharge.
- **Seasonal variation:** Not a modifier at launch. If Cape Coral volume drops 50% in summer, we'll address that operationally, not with seasonal pricing. Revisit after 12 months of data.

---

## Section 5: How to Present on a Sales Call

### The Standard Pitch

> "We price by market based on what it costs us to operate there. Every Market gets a score on our Market Operating Index — six factors including media costs, competition density, the legal environment, uninsured motorist rates, and market-specific dynamics. [City] scores a [X.X]. That puts your lead price at $[Y]. The quality standard is the same in every market — the score, and the price, reflects our operating cost, not what you receive."

### When Asked "Why Is My Market a [Score]?"

Walk through the specific factors. Be concrete, not abstract.

**Example — Atlanta (MOI 6.1, $360/lead):**

> "Atlanta scores a 6.1 because media costs are above average — you're competing with 1,800-plus PI firms for Google clicks in the $150 to $350 range. The competition for PI attention in metro Atlanta is real. But the legal environment is favorable — Georgia is an at-fault state with no serious injury threshold to clear, and your statute of limitations is two years. The main drag on your score is the uninsured rate — Georgia's at 19%, which means roughly one in five leads we generate will have an uninsured at-fault party. That's waste we have to account for. Compare that to Dallas at 6.2 — similar media costs, but Texas has a lower uninsured rate at 14.5% and those I-35 trucking corridors generate high-value cases. Your markets score almost identically, and the price reflects that."

**Example — NYC (MOI 8.9, $460/lead):**

> "New York scores an 8.9 — one of the highest in the country. Three reasons: First, media costs are extreme — $200 to $450 per click on Google, and you're competing with 5,000 to 7,000 PI firms. Second, New York has the strictest no-fault threshold in the US — every lead has to clear the serious injury definition under Insurance Law 5102. Fracture, permanent limitation, 90/180-day disability. That screening costs us real money. Third, it's a 20-million-person Market — the sheer volume of noise we have to cut through is unmatched. The two things working in New York's favor are the low uninsured rate — only 8.6%, meaning almost every lead has an insured at-fault party — and the highest case values in the country. But the operating cost is what it is."

**Example — Fresno (MOI 3.7, $270/lead):**

> "Fresno scores a 3.7 — one of the more efficient markets we operate in. Media costs are low, competition is limited, and California's pure comparative negligence system means no threshold to screen through. The uninsured rate is the same statewide at 20.4%, which hurts, but the low competition means your cost per lead is $270. Your cost-per-signed-case math in Fresno is going to be more favorable than in most markets."

### When Asked "Can You Get Me a Better Price?"

> "The price is the price for the market. It's based on what it costs us to operate there — not a negotiated margin. What I can do is look at a multi-Market bundle if you operate in more than one market. That's where the discount structure lives."

---

## Section 6: Cross-State Market Rules

**Principle: Price follows the Market. Compliance follows the state.**

A Market that spans multiple states gets one MOI score and one lead price. But the leads generated in each state are screened and documented according to that state's legal requirements.

### NYC Market (New York, New Jersey, Connecticut)

| | |
|---|---|
| **MOI Score** | 8.9 |
| **Lead Price** | $460 |
| **NY leads** | Screened against NY Insurance Law §5102(d) serious injury threshold (9 categories) |
| **NJ leads** | Screened for verbal threshold vs. full tort election |
| **CT leads** | Screened under CT rules (CT is an at-fault state, no no-fault — simpler screening) |

The attorney buying the NYC Market gets leads from all three states. The price is the same regardless of which state the lead originates in. SC handles the compliance screening internally.

### Philadelphia Market (Pennsylvania, New Jersey, Delaware)

| | |
|---|---|
| **MOI Score** | 6.5 |
| **Lead Price** | $375 |
| **PA leads** | Screened for limited tort vs. full tort election |
| **NJ leads** | Screened for verbal threshold vs. full tort election |
| **DE leads** | At-fault state, no no-fault screening required |

Same principle — one price, SC handles the multi-state compliance internally.

### Other Cross-State Markets in Our Top 10

Most other Markets in our top 10 states don't cross state lines in practice (LA, Chicago, Atlanta, Dallas, Houston, Miami, Phoenix, Seattle are all contained within their state). The cross-state rule primarily affects:
- NYC Market (NY/NJ/CT)
- Philadelphia Market (PA/NJ/DE)
- Cincinnati Market (OH/KY/IN) — not in initial top 10 but relevant for expansion
- Memphis Market (TN/MS/AR) — not in initial top 10
- Kansas City Market (MO/KS) — not in initial top 10

---

## Section 7: The Custom Mix Add-On (Future — Not This Session)

> **Status:** Placeholder — full framework to be developed in follow-up session with strategy, creative, behavioral, and production input.

Second Chair will offer targeted campaigns for specific high-value case types as an add-on above baseline pricing. The concept:

**What it is:** Attorneys configure what percentage of their leads come from targeted vs. standard campaigns. Standard campaigns cast a wide net for all MVA leads. Targeted campaigns pursue specific case types (trucking accidents, rideshare MVAs, pedestrian/cyclist, commercial vehicle, DUI-caused MVAs) that carry higher case values.

**Why it's priced differently:** Targeted campaigns have unknown conversion rates per market. We can't guarantee volume the way we can with standard MVA campaigns. Risk-adjusted pricing reflects the uncertainty — attorneys pay a premium for the targeting, but only on the targeted portion of their lead flow.

**What the follow-up session needs to define:**
1. Targetable case-type categories and which ones SC can credibly deliver
2. Risk-adjusted pricing methodology for each category
3. The custom mix configurator UX — how attorneys set their mix
4. Minimum baseline volume requirements (can't go 100% targeted — must maintain a standard floor)
5. How targeted campaign performance data feeds back into pricing adjustments over time

---

## Appendix: Complete MOI Score and Price Table

All Markets in our top 10 states, sorted by MOI score (descending).

| Rank | Market | State | MOI | CPL | Key Driver |
|------|-----|-------|-----|-----|-----------|
| 1 | New York City | NY | 8.9 | $460 | Strictest no-fault + extreme media costs + 20M pop |
| 2 | Los Angeles | CA | 8.0 | $425 | Largest PI Market + extreme CPC + vendor saturation |
| 3 | Miami–Ft. Lauderdale | FL | 7.8 | $420 | No-fault screening + highest uninsured (20.6%) + vendor density |
| 4 | Chicago | IL | 6.9 | $390 | Cook County verdicts + 9.5M pop + high CPC |
| 5 | Orlando | FL | 6.8 | $385 | No-fault + tourist corridor + Morgan & Morgan HQ |
| 6 | San Francisco–Oakland–San Jose | CA | 6.7 | $380 | Premium case values + high media costs |
| 7 | Philadelphia | PA | 6.5 | $375 | Tort election screening + plaintiff-friendly venue |
| 8 | Tampa–St. Petersburg | FL | 6.4 | $370 | No-fault + retiree population |
| 9 | Houston | TX | 6.3 | $365 | Trucking capital + energy sector + 7.5M pop |
| 10 | Dallas–Ft. Worth | TX | 6.2 | $365 | I-35 trucking + 8.1M pop |
| 11 | Atlanta | GA | 6.1 | $360 | 6.2M pop + Alex relationships + anti-running regs |
| 12 | Riverside–San Bernardino | CA | 5.5 | $340 | IE freeways + high MVA volume |
| 13 | San Diego | CA | 5.5 | $340 | SC team proximity + military + moderate competition |
| 14 | Buffalo | NY | 5.5 | $340 | No-fault screening (same as NYC) + low competition |
| 15 | Jacksonville | FL | 5.5 | $340 | No-fault + I-95 + lower competition than South FL |
| 16 | Cape Coral–Fort Myers | FL | 5.5 | $340 | No-fault + snowbird seasonality |
| 17 | Seattle–Tacoma | WA | 5.4 | $335 | Existing SC ops + tech demographics + high uninsured |
| 18 | Rochester | NY | 5.1 | $325 | No-fault screening + small upstate market |
| 19 | Pittsburgh | PA | 5.0 | $320 | Tort election screening + regional loyalty |
| 20 | Phoenix–Mesa | AZ | 4.9 | $315 | Fast growth + ABS law (PE firms) |
| 21 | Albany | NY | 4.8 | $310 | No-fault screening + state capital |
| 22 | Sacramento | CA | 4.7 | $310 | Growing metro + moderate competition |
| 23 | San Antonio | TX | 4.5 | $300 | I-35 + military + low competition |
| 24 | Austin | TX | 4.4 | $300 | Tech growth + younger demographics |
| 25 | Syracuse | NY | 4.4 | $300 | No-fault screening + smallest upstate |
| 26 | Savannah | GA | 4.0 | $285 | Trucking corridor + port city |
| 27 | Fresno | CA | 3.7 | $270 | Ag belt + low competition |
| 28 | McAllen–Edinburg | TX | 3.6 | $270 | Border + bilingual + low competition |
| 29 | El Paso | TX | 3.6 | $270 | Border + bilingual + low competition |
| 30 | Bakersfield | CA | 3.4 | $260 | Ag belt + small market |
| 31 | Rockford | IL | 3.4 | $260 | Small market + limited firm count |
| 32 | Tucson | AZ | 3.3 | $255 | Small market + I-10 corridor |
| 33 | Spokane | WA | 3.3 | $255 | Small market + low competition |
| 34 | Peoria | IL | 3.1 | $250 | Smallest market in top 10 states |

**Weighted Average CPL (all 34 Markets, population-weighted): ~$390**
**Weighted Average CPL (top 10 Markets by population): ~$415**
**Weighted Average CPL (Markets ranked 11–34): ~$315**

---

## Cross-Reference

| Document | Relationship |
|----------|-------------|
| `State_Lead_Pricing_By_State.md` | **Superseded** — tier-based pricing replaced by MOI scoring |
| `Pricing_Architecture.md` | Competitive context — where SC sits in the market |
| `GEO_EXCLUSIVITY_POLICY.md` | Territory policy — updated to reference MOI scoring |
| `FINANCIAL_PROJECTIONS.md` | Revenue model — updated with MOI-weighted pricing |
| `Top_10_Market_Targets.md` | Market-level data — MOI scores build on this foundation |
| `Geo_Exclusive_Whale_Client_Model.md` | Revenue modeling — tier pricing replaced by MOI-based pricing |

---

*Second Chair — March 2026*
