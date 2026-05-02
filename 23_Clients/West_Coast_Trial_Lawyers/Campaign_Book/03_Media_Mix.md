# Media Mix — WCTL AZ Pilot

**Authored by:** Simon Croft (Head of Media Buying) + Depesh Mandalia (Meta paid social)
**Status:** Locked architecture per 2026-04-22 single-ad-set decision; Anchor cohort layered 2026-04-30
**Source-of-truth deep doc:** `../Audience/06_Media_Plan_And_Budget_Allocation.md` (761 lines, full operational plan)
**This file:** the at-a-glance levers Davis can shift without opening the deep doc

---

## The Mix in One Table

| Channel | Surface | Budget % | Format types | Anchor cohort | Expected leads |
|---|---|---|---|---|---|
| **Meta — Advantage+** | FB Feed | algo-driven (~30-35%) | Cinematic primary, Cinematic still, Designed static, Anchored variants | **YES — Anchored cohort runs** | ~7-8 |
| **Meta — Advantage+** | IG Feed | algo-driven (~15-20%) | Cinematic primary, Cinematic still, Designed static | YES — Anchored runs (versatile) | ~3-5 |
| **Meta — Advantage+** | IG Reels | algo-driven (~25-30%) | UGC, Motion-Still, Cinematic motion | NO — Clean cohort runs | ~6-7 |
| **Meta — Advantage+** | IG Stories | algo-driven (~10-15%) | UGC, Motion-Still | NO — Clean cohort runs | ~2-3 |
| **Meta — Advantage+** | FB Reels | algo-driven (~5-10%) | Motorcycle (identity-trigger), UGC | NO — Clean cohort runs | ~1-2 |
| **Meta — Audience Network** | Off-platform | algo-driven (residual) | Whatever Meta serves | n/a | ~0-1 |
| **Meta — Retargeting (separate campaign)** | All Advantage+ surfaces | $556 (7.2% of media) | 2 retargeting variants (urgency / social proof) | Activates end Week 2 | ~1-2 |
| **TOTAL** | | **$7,750 media** | 6 format types + Anchor variant layer | ~13 anchored / ~19 clean | **~21 (range 18-24)** |

**Davis controls:** the creative diversity inside the single ad set (which formats run, what split between Anchored/Clean). **Davis does NOT control:** the FB-vs-IG-vs-Reels-vs-Stories split — that's Advantage+ algorithmic distribution based on which creatives perform on which surface.

## Channel Decision — Why 100% Meta

| Channel | Considered | Decision | Rationale |
|---|---|---|---|
| **Meta (FB + IG)** | ✅ | **PRIMARY** | 75% of AZ adults reachable; 80% of 30-49 demo on FB daily; PI-vertical native; Advantage+ + Special Ad Category proven |
| TikTok | ❌ | Phase 2 | $625 allocation can't clear learning + 30-50% SAC rejection without reallocation mechanism |
| Reddit | ❌ | Phase 2 | $375 buy = ~250-500 clicks, below decision-quality signal threshold |
| Programmatic geofencing (hospitals / collision repair) | ❌ | Phase 2 | DSP setup is Phase 2 scope (Sasha) — single-flight setup is sunk cost |
| YouTube pre-roll | ❌ | Phase 2 | Strong contextual fit for motorcycle but needs $25K+ to clear |
| Google Search (PI keywords) | ❌ | Out of scope | Different funnel + bid model + creative; would need separate pilot |

**One channel, one ad set, one optimization model — at $7,750 this produces 4× the learning signal vs. any split architecture.** Doctrine: don't starve channels below signal density.

## Format × Surface Allocation

This is the lever Davis can adjust:

| Format | Primary surface | Secondary surface | Anchor? | Phase 1 unit count |
|---|---|---|---|---|
| Cinematic Primary Video | FB Feed | IG Feed, FB Reels | YES (Sarah, Diana cinematic) | ~8-10 units |
| Cinematic Photographic Still | FB Feed | IG Feed | YES (Laura) | ~5 units |
| UGC-Native Video | IG Reels | IG Stories, FB Reels | NO | ~2-3 units (Diana UGC) |
| Motion-Still | IG Reels | IG Stories | NO | ~3 units (MS-Laura, MS-Diana, MS-Ty) |
| DR Copy-Led Print Still | FB Feed | n/a | TBD (currently no) | ~1-2 units (DR-M1) |
| Designed-Static Brand Units | FB Feed | n/a | NO (already designed objects) | 2 units (HN-1.7B, EX-Settlement-Gap) |
| **Motorcycle (identity arc)** | IG Reels + FB Reels | IG Feed | NO (identity-trigger) | ~12 units (M1/M2/M3 × 4 each) |
| **Anchor variants (sixth pattern)** | FB Feed | IG Feed | YES — they ARE the Anchor cohort | ~13 units composited from existing footage |
| **Total** | | | | **~32-45 units** |

**The format-mix decision Davis can shift:** if motorcycle creative is over-served vs. severe-injury, the hot-swap contingency in `../Audience/06_Media_Plan §7` activates a two-ad-set split. Don't shift this manually before Day 7.

## Budget Tapering by Phase

| Phase | Weeks | Budget | Daily Spend | Why |
|---|---|---|---|---|
| Testing | 1-2 | $3,100 (40%) | $220/day | Algorithm learning; expect ugly Week-1 CPL ($620-$1,033 cost-of-learning band) |
| Optimization | 2-3 | $2,325 (30%) | $165/day | Pixel locks on winners; CPL drops sharply |
| Scale | 3-5 | $2,325 (30%) | $115-$165/day | Best CPL phase ($233-$291); only winners running |
| **Reserve** | flex | $1,667 (21.5%) | flex | Buffer for creative breakouts or extension to Week 6 |
| **Total media** | 5 weeks | **$7,750** | tapered | |

**Optimization event:** Landing Page Views (not quiz completions, not lead submissions). At $7,750 this gives ~310-440 weekly LPVs = 6-9× the 50/wk learning threshold. If campaign scales to $25K+, shift optimization to quiz completions.

## Anchor Cohort Allocation (added 2026-04-30)

| Cohort | Units | Budget | Expected surface skew | Expected lead share |
|---|---|---|---|---|
| **Anchored** | ~13 (Sarah cinematic + Laura static + Diana cinematic) | algo-driven (no separate budget) | FB Feed-heavy | ~10-12 leads (47-57%) |
| **Clean** | ~19 (Ty motorcycle + Diana UGC + HN/EX + matched controls) | algo-driven | IG Reels-heavy | ~9-11 leads (43-53%) |

**Validation thresholds (Week 1):** Anchored ≤ Clean CPL on FB Feed; Clean ≤ Anchored CPL on IG Reels. If both confirm → Phase 2 standard. (Full plan: `../Creative/Phase_1_Split_Test_Plan.md`)

## Static-as-Video Rule (Surface-Aware)

| Unit | Surface | Format treatment |
|---|---|---|
| S2 Laura static | FB Feed | Pure JPG (FB renders static at full weight) |
| S2 Laura static | IG Reels / Stories | 4-7s ambient-motion MP4 + audio bed |
| HN/EX Designed Statics | FB Feed | Pure JPG |
| HN/EX Designed Statics | IG Reels / Stories | 4-7s ambient-motion MP4 + audio bed |
| All cinematic + UGC | All surfaces | Already video |

**Operational:** build 2 versions of each static unit; Advantage+ per-placement creative customization serves the right one.

## Reallocation Triggers (Watch List)

| Trigger | Day | Action | Budget impact |
|---|---|---|---|
| Motorcycle <15% impression share | Day 7 | Hot-swap to two-ad-set architecture | ~$1,500 carved off |
| Any creative <0.8% CTR after 1k impressions | Day 5-7 | Pause that creative | None |
| Quiz start rate <45% of LPVs | Day 7-10 | Revise landing page (48hr) | None |
| Quiz completion rate <30% of starts | Day 10-14 | Revise quiz flow (72hr) | None |
| Non-soft-tissue pass rate <10% of completions | Day 14+ | Revise creative copy + quiz Step 3 | None |
| Anchored CPL > Clean CPL on FB Feed (Week 1) | Day 7 | Refine Anchor variant or cut | None |

(Full kill criteria + diagnosis protocol: `../Audience/06_Media_Plan §6`)

## Reporting Cadence (Davis ⇄ Robert)

| Cadence | What Davis sees | What Robert sees |
|---|---|---|
| Daily | Spend pacing, CPL, CTR, lead delivery, campaign status | Lead deliveries (real-time email + dashboard) |
| Every 3 days | Creative performance ranking; kill/scale decisions | n/a |
| Weekly | Performance summary, week-over-week trend, lead grade distribution | 3-sentence professional update; lead count cumulative + trend |
| Bi-weekly | ROAS projection update; cohort quality assessment; Phase 2 recommendation | Same |
| End Week 1 | Anchor split-test validation + ship/refine/cut decision | Inclusion in weekly update |

## What's NOT in This Mix (and Why — Quick Reference)

- **No budget allocated to Spanish creative** — Phase 2 dedicated ad set captures Maryvale + South Phx properly
- **No budget allocated to TikTok / Reddit / geofencing / YouTube** — Phase 2 multi-channel add if pilot validates
- **No live transfers** — email delivery only Phase 1; Salesforce integration Phase 2
- **No DUI** — Service Agreement §1.3 excludes
