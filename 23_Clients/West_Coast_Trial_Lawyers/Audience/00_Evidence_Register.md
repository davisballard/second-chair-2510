# 00 — Evidence Register
## Load-Bearing Numbers Across the WCTL Arizona Audience Playbook

**Prepared:** 2026-04-21
**Owner:** Davis (rigor audit)
**Purpose:** Single source of truth for every number that drives a downstream decision in Docs 01–06. If a number changes, it changes here first, then in the doc.
**Use:** When editing any Audience/ doc, reference the number's row below. Do not introduce a new load-bearing number without adding it here.

---

## Status Legend

| Status | Meaning | How to treat it |
|---|---|---|
| `sourced` | Cited to an external source (ADOT, NHTSA, Pew, Meta, WordStream, etc.). | Trustworthy. Re-check if the source updates. |
| `sourced-dated` | Sourced but time-sensitive (e.g., quarterly CPM). | Re-validate if campaign launches >90 days after the citation date. |
| `derived` | Calculated from other numbers in this register. | Trustworthy only as far as its inputs are. If an input is `internal estimate`, the derived number inherits that status. |
| `internal estimate` | Internal projection, industry-benchmark shorthand, or professional judgment. Not externally cited. | **Must be validated during Week 1 of campaign.** Label explicitly in the doc. |
| `extrapolated` | Inferred from adjacent data (e.g., national rate applied to state population). | Weakest evidence class. State the inference in-line and treat the result as a range, not a point. |
| `hard` | Contractual, budget, or platform-locked number. | Immutable for this pilot. |

---

## 1. Campaign / Budget Numbers (Hard)

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 1.1 | Total client payment | $9,975 | 06 §1; Service Agreement §4.1 | WCTL contract | `hard` | Contractual — immutable |
| 1.2 | Cost per delivered lead | $475 | 06 §1; Contract §4.2 | WCTL contract | `hard` | Contractual — immutable |
| 1.3 | Target delivered leads | 21 | 06 §1; Contract §4.3 | WCTL contract | `hard` | Contractual obligation |
| 1.4 | Total media spend | $7,750 | 03 §5; 06 §1 | Budget allocation | `hard` | Internal allocation; not client-facing |
| 1.5 | Meta media spend (Phase 1) | **$7,750** (was $6,250 pre-2026-04-22) | 06 §1 | Budget allocation | `hard` | 100% of Phase 1 media consolidated to Meta per 2026-04-22 architecture collapse. |
| 1.6 | Geofencing spend (Phase 1) | **$0** (was $625) — **deferred to Phase 2** | 06 §1 | 2026-04-22 architecture collapse | `hard` | Moved to Phase 2 exploratory channel proposal — not Phase 1 spend. |
| 1.7 | TikTok spend (Phase 1) | **$0** (was $625) — **deferred to Phase 2** | 06 §1 | 2026-04-22 architecture collapse | `hard` | Moved to Phase 2 — SAC rejection risk + sub-threshold budget made Phase 1 test not decision-quality. |
| 1.8 | Reddit spend (Phase 1) | **$0** (was $375) — **deferred to Phase 2** | 06 §1 | 2026-04-22 architecture collapse | `hard` | Moved to Phase 2. |
| 1.9 | Campaign duration | 4–6 weeks | 03, 06; Contract §5.3 | Contractual estimate | `hard` (upper bound) | Contractual; monitor Week 4 to decide extension |
| 1.10 | AZ statute of limitations (PI) | 2 years | 03, 06; Contract §6.1(d) | AZ Revised Statutes §12-542 | `sourced` | Legal — immutable |
| 1.11 | Case types in scope (Contract §1.3) | MVA, Trucking, Motorcycle, Pedestrian/Bicycle, Rideshare, Wrongful Death | Contract §1.3 | WCTL Service Agreement 2026-04-16 | `hard` | **DUI explicitly excluded.** Creative, architecture, and forecasting all flow from this list. Soft tissue / parking lot / fender-bender / property-damage-only also excluded per §1.4. |

---

## 2. Arizona Population & Crash Data (Sourced)

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 2.1 | AZ total population | 7.58M (2025) | 01 §1 | U.S. Census, Data USA, Neilsberg | `sourced-dated` | Census re-release annually; acceptable |
| 2.2 | AZ adult population (18+) | ~5.8M | 04 §1 | Census age bands applied to 2.1 | `derived` | Trustworthy (Census age bands are solid) |
| 2.3 | Hispanic population | 32.1% / ~2.43M | 01 §1, §8 | Census | `sourced` | — |
| 2.4 | Maricopa County population | 4.73M (62%) | 01 §1 | Census | `sourced` | — |
| 2.5 | Pima County population | 1.09M (14%) | 01 §1 | Census | `sourced` | — |
| 2.6 | AZ total crashes 2024 | 121,107 | 01 §1 | ADOT 2024 Crash Facts | `sourced` | ADOT annual release |
| 2.7 | AZ fatal crashes 2024 | 1,117 | 01 §1 | ADOT | `sourced` | — |
| 2.8 | AZ injury crashes 2024 | 37,376 | 01 §1 | ADOT | `sourced` | — |
| 2.9 | AZ motorcycle crashes 2024 | 3,036 | 01 §2 | ADOT | `sourced` | — |
| 2.10 | AZ motorcycle fatalities 2024 | ~245 (est.) | 01 §2 | ADOT (2023 actual: 258) | `sourced-dated` | — |
| 2.11 | AZ truck/bus crashes 2024 | 2,750 | 01 §3 | Perez Law Group / FMCSA | `sourced` | — |
| 2.12 | AZ pedestrian crashes 2024 | 2,079 | 01 §4 | Ramos Law (ADOT derivative) | `sourced` | — |
| 2.13 | AZ pedestrian fatalities 2024 | 263 | 01 §4 | Ramos Law | `sourced` | — |
| 2.14 | AZ bicycle crashes 2024 | 1,379 | 01 §4 | Bicycle Accident Lawyers | `sourced` | — |
| 2.15 | AZ alcohol-related crashes 2024 | 5,520 | 01 §5 | Ramos Law | `sourced` | **Excluded per signed contract (2026-04-16).** Retained for addressable-market reference only. |
| 2.16 | AZ alcohol-related injury crashes 2024 | ~3,576 (298/mo) | 01 §5 | Ramos Law | `sourced` | **Excluded per signed contract.** |
| 2.17 | Moderate-to-severe MVA % of injury crashes | 15–20% | 01 §6 | — | `internal estimate` | Flag as estimate in Doc 1; validate against actual lead mix by Week 3 |

---

## 3. Monthly Non-Soft-Tissue Volume (Mixed)

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 3.1 | AZ total non-ST incidents/month (deduplicated) | 925–1,233 (pre-DUI-removal); **~750–1,050 in-scope** (after DUI exclusion) | 01 §1, 03 §3 | Derived from 2.6–2.14 with overlap dedup. DUI share subtracted. | `derived` | Both ranges retained for traceability. The in-scope ~750–1,050/mo figure is the operative addressable market. Capture rate math still comfortable well under 1% at 21-lead target. |
| 3.2 | Motorcycle non-ST incidents/month | 214 | 03 §3 | 2.9 ÷ 12 × 100% non-ST assumption | `derived` + `internal estimate` | Non-ST % is estimate (see 4.1); monthly derivation is sound |
| 3.3 | Trucking victim non-ST/month | 91 | 03 §3 | 2.11 ÷ 12 × 60–70% non-ST (victim-only) | `derived` + `internal estimate` | Non-ST % and victim-only % are estimates |
| 3.4 | Pedestrian + cyclist non-ST/month | 268 | 03 §3 | (2.12 + 2.14) ÷ 12 × 80% | `derived` + `internal estimate` | Non-ST % estimate |
| 3.5 | DUI victim non-ST/month | 298 | 03 §3 | 2.16 ÷ 12 | `sourced` | **Excluded per signed contract.** Retained for Phase 2 reference. |
| 3.6 | Moderate-severe MVA/month | 400–600 | 01 §6, 03 §3 | 2.8 ÷ 12 × 15–20% (see 2.17) | `derived` + `internal estimate` | — |
| 3.7 | Rideshare/month | ~17 | 01 §7, 03 §3 | Extrapolated from national rideshare rate applied to Phoenix volume | `extrapolated` | Acknowledge extrapolation at top of Doc 1 §7, not mid-doc |

---

## 4. Non-Soft-Tissue % by Case Type (Internal Estimates — All Need Validation)

These percentages drive how many of the monthly incidents in §3 actually qualify for our funnel. Every one is an internal estimate.

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 4.1 | Motorcycle non-ST % | ~100% | 01 §2; 03 §3 | Physics of motorcycle crashes (no crumple zone) | `internal estimate` | Validate against actual quiz-filter pass rate for motorcycle creative in Week 2 |
| 4.2 | Trucking victim non-ST % | 60–70% | 01 §3; 03 §3 | — | `internal estimate` | Validate against actual pass rate for trucking creative in Week 2 |
| 4.3 | DUI victim non-ST % | ~60% | 03 §3 | — | `internal estimate` | **Excluded per signed contract.** DUI is out of scope; this estimate is moot for the pilot. Retained for Phase 2. |
| 4.4 | Pedestrian/cyclist non-ST % | ~80% | 03 §3 | — | `internal estimate` | Validate Week 2 |
| 4.5 | Moderate-severe MVA non-ST % | By definition 100% of this subset | 03 §3 | Definitional | `derived` | The uncertainty is in 2.17, not this |

---

## 5. Representation Rates (Internal Estimates — Drive Reachable Pipeline)

Every one of these drives 3.x → reachable pipeline in Doc 3 §4. None is sourced. Collectively they move the reachable pipeline by a factor of ~2.6× (2,775 vs. 7,400).

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 5.1 | Motorcycle representation rate | ~60% | 03 §3 | — | `internal estimate` | No clean Week-1 validation — this is a backlog/market metric. Flag as estimate; accept range |
| 5.2 | Trucking representation rate | ~65% | 03 §3 | — | `internal estimate` | Same |
| 5.3 | Pedestrian/cyclist representation rate | ~45% | 03 §3 | — | `internal estimate` | Same |
| 5.4 | DUI victim representation rate | ~50% | 03 §3 | — | `internal estimate` | **Excluded per signed contract.** |
| 5.5 | Moderate-severe MVA representation rate | ~55% | 03 §3 | — | `internal estimate` | Same |
| 5.6 | Rideshare representation rate | ~40% | 03 §3 | — | `internal estimate` | Same (low volume; low impact on decision) |

---

## 6. Funnel Conversion Rates (Internal Estimates — HIGHEST LEVERAGE)

These six numbers determine how many clicks turn into delivered leads. Every downstream projection (weekly quiz completions, learning phase health, CPL, lead volume) rides on them. None is externally sourced.

**Calibration 2026-04-22:** The original rates compounded to ~6.6% click→delivered — a 7× overstatement vs. the 0.95% implied by the 21-lead contractual target. Rates recalibrated by back-solving from the target. "Former" column shows the original over-optimistic values; "Calibrated" is the current working estimate. Week 1 actuals still validate.

| # | Number | Calibrated value (current) | Former (overstated) | Doc/Section | Status | Validation plan |
|---|---|---|---|---|---|---|
| 6.1 | **Quiz start rate (click → start)** | **60%** | 70% | 03 §5; 06 §5 | `internal estimate — calibrated 2026-04-22` | **Validate by end of Day 7.** If actual <45%, revise landing page. |
| 6.2 | **Quiz completion rate (start → complete)** | **40%** | 65% | 03 §5; 06 §5 | `internal estimate — calibrated 2026-04-22` | **Validate by end of Day 10–14.** If <30% of starts, revise quiz. |
| 6.3 | **Non-soft-tissue pass rate (complete → qualify)** | **15%** | 40% | 03 §5; 06 §5 | `internal estimate — calibrated 2026-04-22`. Former was wildly optimistic; industry reality: most paid-social PI clickers are soft-tissue. | **Validate by end of Day 14.** If <10%, revise creative + quiz Step 3. |
| 6.4 | Contact submission rate | **80%** | 85% | 03 §5 | `internal estimate — calibrated 2026-04-22` | Validate Week 2 |
| 6.5 | Verification pass rate | 85% | 85% | 03 §5 | `internal estimate` (unchanged) | Validate Week 2 |
| 6.6 | Final deliverable rate of verified | **40%** | ~50% | 03 §5 | `internal estimate — calibrated 2026-04-22`. Tighter manual QA + fraud + dedupe cut than originally modeled. | Validate Week 2 |
| 6.7 | Full-funnel click → delivered lead | **~0.98%** | ~6.6% (product of former) / 0.95% (observed target) | 03 §5 | `derived` — now compounds correctly to the 21-lead contractual target. | The former table stated 0.95% as a top-line outcome but the intermediate rates multiplied to 6.6% — a 7× internal inconsistency. Resolved 2026-04-22 by recalibrating. |

---

## 7. Media Performance Benchmarks (Mixed)

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 7.1 | CPM — campaign working estimate | $35 | 03 §5 | Midpoint of 7.2 | `derived` | Update after Week 1 actual |
| 7.2 | AZ legal FB CPM — estimated range | $30–$45 | 04 §2 | National legal CPM ($49.70) moderated by AZ market + SAC + season | `internal estimate` (inference chain) | **Show calc in Doc 4 §2. Validate Day 3–5 actuals.** |
| 7.3 | National FB legal CPM 2025 average | $49.70 | 04 §2 | WordStream / Data-Axle 2025 | `sourced-dated` | Q1 2026 re-check already happened (=$14.26 seasonal) |
| 7.4 | Jan 2026 FB legal CPM | $14.26 | 04 §2 | Same | `sourced-dated` | Seasonal anomaly — do NOT plan against |
| 7.5 | National FB legal CPC | $4.10 | 04 §2 | WordStream 2025 | `sourced-dated` | — |
| 7.6 | AZ campaign FB CPC estimated | $3.50–$5.00 | 04 §2; 03 §5 | Inferred from 7.2, 7.5 | `internal estimate` | Validate Day 3–5 |
| 7.7 | CTR working estimate | 1.0% | 03 §5 | Industry benchmark | `internal estimate` | Validate Day 5–7; kill threshold at 0.8% |
| 7.8 | TikTok CPM | $5–$9 | 04 §4; 06 §1 | Platform benchmark | `sourced` (platform docs) | — |
| 7.9 | Reddit CPC | $0.75–$1.50 | 04 §6?; 06 §1 | Platform benchmark | `sourced` | — |
| 7.10 | Geofencing display CPM | $8–$15 | 06 §1 | DSP benchmarks | `sourced` | — |
| 7.11 | Geofencing hospital-location lift vs. broad display | 3.1× | — | **UNSOURCED** | `deprecated Phase 1` — geofencing deferred to Phase 2 per 2026-04-22 architecture collapse | If Phase 2 includes geofencing, cite source or remove the claim before launch. |
| 7.12 | TikTok PI ad rejection probability | 30-50% Day-1 rejection (Doc 4 §4 inference) | 04 §4 | — | `deprecated Phase 1` — TikTok deferred to Phase 2 per 2026-04-22 architecture collapse | Revisit in Phase 2 channel proposal if TikTok retained. |
| 7.13 | Meta learning phase threshold | 50 optimization events / week / ad set | 03 §2, 06 §5 | Meta documented | `sourced` | — |
| 7.14 | Retargeting minimum audience size | ~200 | 06 §5 | Meta documented | `sourced` | — |
| 7.15 | Learning phase penalty | 15–25% worse delivery | 03 §9 | "Industry data consistently shows" (unsourced) | `internal estimate` | **Source or label. Materially affects Option A vs. B comparison** |

---

## 8. Projected Outputs (Derived — Reliability Inherits from Inputs)

> **Architecture note (2026-04-22):** Rows 8.2 and 8.3 reflect the former two-ad-set split (25/75 motorcycle/severe). Under the updated single-ad-set architecture (Doc 6 §2), these are superseded by 8.2a below. 8.2 and 8.3 retained for hot-swap contingency math.

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 8.1 | Weekly quiz completions — campaign level | **89–133** (was 168–252 overstated) | 03 §2 | Derived from 7.1, 7.7, calibrated 6.1, 6.2 | `derived — recalibrated 2026-04-22` | Actual tracked weekly. If <70 by Day 10, flag quiz flow revision per Doc 6 §6 decision rule. |
| 8.2a | **Weekly quiz completions — single ad set (current architecture)** | **~89–133** | 06 §2 | All campaign spend in one ad set | `derived` | **~2× Meta learning threshold on quiz completions. Landing-page-view optimization (Doc 6 §5) provides ~9-10× threshold, which is what we actually optimize on in Week 1-2.** |
| 8.2 | Weekly quiz completions — Motorcycle ad set (hot-swap only) | ~22 | 03 §12 | 25% of 8.1 | `derived` | Applies only if hot-swap trigger fires. Would be below quiz-completion threshold — but LPV-optimization still clears. |
| 8.3 | Weekly quiz completions — Severe Injury ad set (hot-swap only) | ~67 | 03 §12 | 75% of 8.1 | `derived` | Hot-swap contingency math. |
| 8.3a | Weekly NST-qualified completions | **~13–20** | 03 §2 | 8.1 × Register 6.3 (15%) | `derived` | These are the actual addressable leads before contact/verify/final filters. |
| 8.3b | Weekly delivered leads | **~3.6–5.4 (midpoint ~4/week)** | 06 §3 | 8.3a × 80% × 85% × 40% | `derived` | Matches 21-lead target over 5 weeks. |
| 8.4 | Meta delivered leads (Phase 1 = all leads) | **~18–24** (target 21) | 06 §1 | Derived from 6.x, 7.x, full $7,750 Meta | `derived — recalibrated 2026-04-22` | Validate weekly |
| 8.5 | ~~Geofencing delivered leads~~ | **Phase 2 only** (was 1–3 in multi-channel model) | — | — | `deprecated Phase 1` | Revisit in Phase 2 channel diversification |
| 8.6 | ~~TikTok delivered leads~~ | **Phase 2 only** (was 0–3) | — | — | `deprecated Phase 1` | Revisit Phase 2 |
| 8.7 | ~~Reddit delivered leads~~ | **Phase 2 only** (was 1–3) | — | — | `deprecated Phase 1` | Revisit Phase 2 |
| 8.8 | Combined delivered leads (Phase 1 = Meta-only) | **~18–24** | 06 §1 | = 8.4 (no supplementary channels in Phase 1) | `derived` | Same as 8.4; multi-channel combined math deprecated 2026-04-22 |
| 8.9 | Phase 1 CPL (cost-of-learning) | $620–$1,033 | 06 §3 | $3,100 / 3–5 leads | `derived` | 67% range is width of uncertainty; frame explicitly as cost-of-learning band |
| 8.10 | Phase 2 CPL | $258–$332 | 06 §3 | $2,325 / 7–9 leads | `derived` | — |
| 8.11 | Phase 3 CPL | $233–$291 | 06 §3 | $2,325 / 8–10 leads | `derived` | — |
| 8.12 | Blended CPL (media) | $350–$390 | 06 §1 | Weighted across phases | `derived` | — |

---

## 9. Case Values & ROAS Model (Internal Estimates — Downstream Reporting)

| # | Number | Value | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 9.1 | Median settlement — moderate MVA | $75,000 | 03 §3 | Industry benchmark | `internal estimate` | Validate against WCTL historical close data if shared |
| 9.2 | Median settlement — motorcycle | $75,000–$150,000 | 03 §3 | Industry benchmark | `internal estimate` | Same |
| 9.3 | Median settlement — trucking | $90,000+ | 03 §3 | Industry benchmark | `internal estimate` | Same |
| 9.4 | Median settlement — pedestrian/cyclist | $75,000–$300,000 | 03 §3 | Industry benchmark | `internal estimate` | Same |
| 9.5 | Median settlement — DUI victim | $75,000 + punitive | 03 §3 | Industry benchmark | `internal estimate` | Same |
| 9.6 | Median settlement — severe/wrongful death | $300,000–$1,000,000+ | 03 §3 | Industry benchmark | `internal estimate` | Same |
| 9.7 | Median settlement — rideshare | $50,000 | 03 §3 | Industry benchmark | `internal estimate` | Low impact (volume negligible) |
| 9.8 | Attorney fee (contingency) | 33% | 03 §3 | Industry standard | `sourced` | — |
| 9.9 | Projected sign rate | 12–15% | 03 §3; 06 §10 | Internal assumption based on WCTL non-ST intake | `internal estimate` | **WCTL's team controls this — depends on feedback cadence. Request historical baseline from Robert.** |
| 9.10 | Projected pipeline value (21 leads) | $595K–$613K | 03 §12 | Derived from 9.1–9.9 | `derived` | Revalidate post-mix |
| 9.11 | Projected ROAS (at 12–15% sign rate) | 7–9× | 03 §12 | $595K–$613K × 12–15% ÷ $10K | `derived` | Depends on 9.9 |

---

## 10. Compliance Framework (Mixed — Fix Required in Doc 5)

| # | Reference | Jurisdiction | Doc/Section | Source | Status | Validation plan |
|---|---|---|---|---|---|---|
| 10.1 | SB-37 | **California only** | 05 (referenced) | CA legislature | `sourced` | **Doc 5 references SB-37 in AZ context — remove or clearly mark as CA-aspirational for brand consistency** |
| 10.2 | AZ Ethics Rules 7.1, 7.3, 7.5 | Arizona | 05 §F | AZ Rules of Professional Conduct | `sourced` | Authoritative for AZ |
| 10.3 | Meta Special Ad Categories — Social Issues | Platform-global | 03, 04, 05, 06 | Meta policy | `sourced` | — |
| 10.4 | TCPA 1-to-1 consent (TrustedForm) | Federal | 06; Contract §5.1(g) | 47 USC §227; FCC 2024 ruling | `sourced` | — |
| 10.5 | Third-person language requirement | Platform + Bar best practice | 05 §F | Meta policy + Bar rules convergence | `sourced` | — |

---

## 11. Known Inconsistencies To Fix

These are contradictions between docs that the register surfaces:

| # | Contradiction | Docs | Fix |
|---|---|---|---|
| 11.1 | Monthly non-ST volume: Doc 1 says 925–1,233, Doc 3 category sum = ~1,388 | 01 vs. 03 | Show dedup math in Doc 3 §3 explicitly (overlap between e.g. motorcycle+DUI) |
| 11.2 | DUI non-ST % — Doc 3 treated 298 injury crashes as 100% non-ST; 4.3 said 60% | 01 vs. 03 | **RESOLVED 2026-04-21 by scope change.** DUI excluded per signed contract §1.3 — the inconsistency no longer affects the operative plan. Both numbers retained in their docs as Phase 2 reference. |
| 11.3 | ~~Meta budget: Doc 3 (§5) = $7,750 Meta-only; Doc 6 (§1) = $6,250 Meta + $1,500 other channels~~ | 03 vs. 06 | **RESOLVED 2026-04-22.** Doc 6 collapsed to $7,750 Meta-only per architecture decision; both docs now align on Meta-only. Geofencing / TikTok / Reddit deferred to Phase 2 (Register 1.6–1.8). |
| 11.4 | Budget buffer: Doc 6 §4 lists $1,667 reserve; Phase 1 allocation at 40% already includes ~41% reserve vs. scheduled spend | 06 | Reconcile buffer math (see Doc 6 punch list) |
| 11.5 | Facebook reach: Doc 1 §1 references ~4.1M AZ FB users; Doc 4 §2 says 2.87M 25–64 (subset) | 01 vs. 04 | Doc 4 is correct for the 25–64 band; Doc 1 should cite 4.1M total with cross-ref to Doc 4 for age-subset |
| 11.6 | CPM Doc 3 "$35" vs. Doc 4 "$30–45" band | 03 vs. 04 | Doc 3 should cite 7.2 as source, state $35 as midpoint |

---

## 12. What's NOT in This Register (Out of Scope for Rigor Pass)

- **Persona content itself** (Marco's bio, Diana's story, etc.) — these are creative scaffolding, not load-bearing numbers. Methodology transparency is the rigor move for Doc 2, not persona-by-persona validation.
- **Creative hook wording and visual choices** — Doc 5's craft is strong; not auditing.
- **Qualitative descriptions of trauma, lifestyle, media consumption** — not numeric claims.
- **Source URLs** — already well-documented in Doc 1 §12 and inline throughout Doc 4. This register refers to sources by name.

---

## 13. Decision Rules That Depend On These Numbers

When the register's validation plan fires (Week 1 actuals come in), these are the decisions it triggers:

- **If 6.1 (quiz start rate) actual <45% of LPVs at Day 7** → Revise landing page (Doc 6 §6)
- **If 6.2 (quiz completion rate) actual <30% of starts at Day 10** → Revise quiz flow (Doc 6 §6)
- **If 6.3 (non-ST pass rate) actual <10% of completions at Day 14** → Revise creative copy + quiz Step 3 (Doc 6 §6)
- **If 7.2 (AZ CPM) actual > $50 sustained 3 days** → Budget reallocation trigger (Doc 6 §7)
- **If motorcycle impression share <15% of ad set at Day 7** → Hot-swap to two-ad-set architecture (Doc 6 §7; replaces former "<40 weekly completions → shift split" rule, which referenced the two-ad-set architecture deprecated 2026-04-22)
- **If 7.11 geofencing lift or 7.12 TikTok approval assumptions become load-bearing** → Moot under Phase-1 Meta-only architecture (2026-04-22); revisit in Phase 2 channel diversification proposal

---

## 14. Fault Distribution & Rider Liability (Rigor Note — 2026-04-22)

**Purpose:** Answer the "are motorcyclists mostly at fault for their own crashes?" objection if Robert or any WCTL stakeholder raises it. Added following Davis's fault-distribution sanity check on the supersport-persona pivot. Load-bearing numbers live in the tables below; the §14.5 narrative framing is the actual pitch language.

### 14.1 Multi-vehicle moto crashes (~75% of all moto crashes)

| # | Number | Value | Source | Status |
|---|---|---|---|---|
| 14.1.1 | Multi-vehicle share of all motorcycle crashes | ~75% | Hurt Report (USC 1981 foundational study); replicated in modern NTSB analyses | `sourced` |
| 14.1.2 | Multi-vehicle crashes where the OTHER DRIVER is at fault | 60–66% | Hurt Report (66%), MAIDS European report (60%), modern NTSB analysis (~64%, 88 of 138 cases) | `sourced` |
| 14.1.3 | Most common other-driver-fault scenario | Left-turn failure-to-yield — driver didn't see motorcyclist | Hurt Report + ADOT | `sourced` |

### 14.2 Single-vehicle moto crashes (~25% of all moto crashes — NOT our target)

| # | Number | Value | Source | Status |
|---|---|---|---|---|
| 14.2.1 | Single-vehicle share of all moto crashes | ~25% | Hurt Report, NHTSA | `sourced` |
| 14.2.2 | Single-vehicle crashes where the rider is at fault | ~67% | Hurt Report ("rider error present as precipitating factor in ~2/3 of single-vehicle cases") | `sourced` |
| 14.2.3 | Typical rider-error causes | Overbraking slide-out, running wide on a curve due to excess speed | Hurt Report | `sourced` |

**Note:** Single-vehicle crashes are NOT our PI target — no third-party defendant means no recoverable case. These riders don't contact WCTL.

### 14.3 Arizona-specific fault context

| # | Number | Value | Source | Status |
|---|---|---|---|---|
| 14.3.1 | AZ moto crashes occurring with no fault of the rider (all crash types) | ~47% | AZ PI firm aggregate citing ADOT-derivative data (esquirelaw.com, 2025) | `sourced` |
| 14.3.2 | Mesa moto crashes from failure-to-yield + left-turn-without-dedicated-arrow + alcohol + older drivers | 63% of all Mesa moto collisions | City of Mesa crash analysis | `sourced` |
| 14.3.3 | Multi-vehicle share of AZ 2023 moto crashes | 62.6% (1,980 of 3,165) | ADOT 2023 Crash Facts | `sourced` |
| 14.3.4 | AZ comparative negligence rule | Pure comparative — rider's recovery reduced proportional to their fault, never eliminated | A.R.S. § 12-2505 | `sourced` |

### 14.4 Supersport-specific (post-2026-04-22 pivot to Ty Rivera persona)

| # | Number | Value | Source | Status |
|---|---|---|---|---|
| 14.4.1 | Supersport fatal crash rate per 10,000 registered bikes | 22.5–22.6 | Dulaney, Lauer & Thomas study + Motorcycle Industry Council data | `sourced` |
| 14.4.2 | Cruiser fatal crash rate per 10,000 registered bikes | 5.6–5.7 | Same source | `sourced` |
| 14.4.3 | Supersport fatality rate vs. cruiser | ~4x higher per registered bike | Derived from 14.4.1 / 14.4.2 | `derived` |
| 14.4.4 | Supersport fatalities involving rider speed | 57% | MIC / NHTSA | `sourced` |
| 14.4.5 | Left-turn driver's duty to yield under AZ law | Presumptively at fault in intersection crashes REGARDLESS of oncoming-vehicle speed; speed reduces rider's recovery proportionally but doesn't eliminate the driver's liability | A.R.S. § 28-772 + AZ case law interpretation | `sourced` |

### 14.5 The pitch language (for Robert / any WCTL stakeholder)

**Objection:** "Aren't motorcyclists mostly at fault for their own crashes?"

**Answer (sourced):** No. Three-quarters of motorcycle crashes are multi-vehicle, and in those, the other driver is at fault 60–66% of the time per the Hurt Report, MAIDS, and NTSB. In AZ specifically, ADOT data confirms the most common cause is drivers failing to yield or making left turns without seeing the motorcyclist — exactly the scenario our M3 creative ("A driver didn't see the rider") speaks to. The remaining ~25% of crashes that are single-vehicle rider-error cases are NOT our PI target: no third-party defendant means no case to sign. Those riders don't call WCTL.

**Our creative filters for clean-liability cases.** The M3 hook ("A driver didn't see the rider") explicitly self-qualifies to the driver-fault multi-vehicle subset. M1 and M2 are emotional/identity/loss hooks that don't depend on fault allocation. WCTL's ad spend reaches riders most likely to be (a) injured in a crash that wasn't their fault and (b) aware they have a case worth pursuing.

**Supersport-specific (Ty Rivera persona):** Even after the 2026-04-22 pivot to the sportbike archetype — which has a 4x per-capita crash rate and a speed-involvement tail in fatalities — the left-turn driver's duty to yield applies REGARDLESS of rider speed. AZ's pure comparative-negligence rule reduces a rider's recovery proportionally to any fault but never eliminates it: a rider found 20% at fault on a $500K claim still recovers $400K. Supersport riders hit at intersections by left-turning drivers are a clean-liability subset within a 4x-higher-crash-rate population. Math works.

**Validation during pilot:** Track sign rate by self-reported crash-cause in the quiz funnel (Step 3 "What happened?"). Expected pattern: "driver at fault" leads sign at 3–5× the rate of "I was at fault" or "not sure" leads. If the fault-filter doesn't hold that spread, re-tune M3 hook to filter harder — e.g., explicit "hit by a left-turning driver" phrasing.

---

*Evidence Register for Second Chair × WCTL Arizona Pilot — maintained alongside Audience/ docs 01–06. If a load-bearing number changes, update this file first.*
