# WCTL Phase 1 Anchor Split-Test Plan

**Status:** Phase 1 split-test variable. Designed 2026-04-30 from Anchor Session.
**Anchor pattern reference:** `../../../02_Visual/Designed_Overlay_System.md §6 Pattern 6`
**Per-unit deployment:** `Anchor_Template_Spec.md`
**Operative Media Plan:** `../Audience/06_Media_Plan_And_Budget_Allocation.md`

---

## Hypothesis

The Fair Case Anchor (designed/editorial bottom-third overlay) wins on FB Feed placements where the AZ non-soft-tissue PI demo (30-54 commuter, lower-income working-class, FB-heavy) lives. Clean (no Anchor, kinetic-captions-only) wins on IG Reels placements where motorcycle riders + younger UGC-leaning audience lives. Single Advantage+ ad set distributes both; the algorithm pulls each variant to the surface where it earns its keep.

If both directions hold (Anchored ≤ Clean CPL on FB Feed AND Clean ≤ Anchored CPL on IG Reels), the per-persona deployment rule in `Anchor_Template_Spec.md` is validated → Anchor lifts to standard for all FB-Feed-native units in Phase 2.

If either direction fails → refine before mandating.

## Cohort Definition

| Cohort | Units | Surface fit (per AZ audience research) | Variants used |
|---|---|---|---|
| **Anchored** | ~13 of 32 — S1 Sarah cinematic + S2 Laura static + S5 Diana cinematic | Algorithm distributes heavier to FB Feed (designed register native) | A (Promise), B (Specificity), C (Speed), D (Reassurance) per persona-deployment table |
| **Clean** | ~19 of 32 — M1/M2/M3 Ty motorcycle + S5 Diana UGC + HN/EX Designed Statics + Sarah/Laura/Diana matched-clean controls | Algorithm distributes heavier to IG Reels (UGC + cinematic native) | n/a |

Both cohorts run simultaneously inside the single Advantage+ ad set per `06_Media_Plan §2` (one campaign / one ad set / 6+ creative variants — Anchor is creative-level diversity, not ad-set-level split).

## Validation Thresholds

After Week 1 / 100+ qualified-lead-conversion events (achievable per `06_Media_Plan §5.1` LPV optimization buys 6-9× the 50/week threshold):

| Metric | Anchored cohort hypothesis | If confirmed → action | If disconfirmed → action |
|---|---|---|---|
| **FB Feed CPL** (segmented) | Anchored CPL ≤ Clean CPL on FB Feed | Lift Anchor to standard for all FB-Feed-native units in Phase 2 | Investigate copy variant — is Variant B too cautious for FB Feed? Consider swap to Variant A |
| **IG Reels CPL** (segmented) | Clean CPL ≤ Anchored CPL on IG Reels | Confirm Anchor is FB-Feed-only pattern; never deploy on Reels-native creative | Re-test with Translucent Dark Scrim variant (Direction 3) at lower opacity |
| **Hook rate (3s VTR)** | No more than 10% degradation vs Clean baseline on either surface | Anchor isn't costing scroll-stops; ship it | If Anchor costs >10% hook rate on FB Feed → reduce panel opacity to 80% or revisit copy density |
| **Hold rate (75% completion)** | Anchored ≥ Clean | Designed register helps comprehension → Phase 2 expansion confirmed | If Anchored hold rate is meaningfully lower → Anchor is editorial-overdesigned for ad delivery; cut |
| **Quiz start rate (LPV → start)** | Anchored ≥ Clean across both surfaces | Anchor is doing its comprehension job (people understand the offer pre-click) | If Anchored quiz-start lower → CTA copy needs sharpening (try Variant A "Free case review" universally) |
| **Cost per qualified lead (CPL after non-soft-tissue filter)** | Anchored ≤ Clean within ±15% | Anchor doesn't degrade qualified-lead economics | If degraded → Anchor pulls higher-volume but lower-intent traffic; cut from non-FB placements |

## Reporting Cadence

Per `06_Media_Plan §8`, daily monitoring (Alex). Add to existing daily/weekly reports:

| Cadence | New Anchor reporting line |
|---|---|
| **Daily** | Anchored vs Clean impression share by placement (FB Feed / IG Feed / IG Reels / IG Stories) |
| **Every 3 days** | Anchored vs Clean CTR by placement; flag if Anchored CTR degrades >15% on FB Feed |
| **Weekly** | Anchored vs Clean CPL by placement; hook rate; hold rate; cost per qualified lead. Three-sentence summary for Robert. |
| **End of Week 1** | Validation against thresholds above. Ship/refine/cut decision documented. |

## Decision Rules

| Trigger | Action |
|---|---|
| **End of Week 1: Anchored CPL on FB Feed ≤ Clean CPL on FB Feed AND Clean CPL on IG Reels ≤ Anchored CPL on IG Reels** | Hypothesis confirmed both directions. Document for Phase 2. Maintain Phase 1 mix as-is. |
| **End of Week 1: Anchored wins both surfaces** | Anchor is universally net-positive — overrides per-persona rule. Add Anchor to motorcycle (Ty) units in Phase 2. |
| **End of Week 1: Anchored loses both surfaces** | Anchor is a net negative. Pause all anchored units. Run Phase 2 Clean-only and document Anchor failure for future Fair Case work outside lead-gen. |
| **End of Week 1: Anchored wins IG Reels but loses FB Feed** | Surprise result — implies the AZ audience-research persona-platform map is wrong. Pause Sarah/Laura/Diana anchored variants. Run Anchor on motorcycle/UGC instead next batch. |
| **Mixed result within ±15% on both surfaces** | Statistically inconclusive at Week 1 scale. Hold both cohorts running through Week 2; re-evaluate at Week 2 EOW with double the event sample. |

## Robert Framing for Wednesday Pre-Launch Review

"We're testing two versions of the same creative — one with our Fair Case Anchor (the persistent designed brand strip that holds context and CTA throughout the spot) and one Clean (no Anchor, our standard kinetic-captions approach). The hypothesis is grounded in the AZ demo: your trucking, pedestrian, and severe-MVA personas live on Facebook Feed where designed/editorial registers read native. The motorcycle and younger UGC personas live on Instagram Reels where UGC pattern-interrupt wins. We let the Advantage+ algorithm distribute both versions across placements, then segment Week 1 results by placement to validate. If the hypothesis holds, the Anchor becomes our Phase 2 standard for the FB-Feed-native units. If it doesn't, we have learning either way — and we kept the existing 32-unit package you reviewed intact, with the Anchor added as a controlled variable."

## Open Items

- Davis picks Higgsfield mockup direction Mon AM (Direction 1 or 4 recommended for FB-Feed-heavy AZ demo)
- Davis builds Figma Anchor template Mon-Tue
- Davis or Alex composites 6-9 anchored variants in CapCut Tue
- Update `06_Media_Plan §6.5` Anchor cohort line in reporting template before launch
- Robert pre-launch review Wed 2026-05-06
- Launch Thu 2026-05-07 (or per Robert sign-off timing)
- Week 1 validation Thu 2026-05-14 — apply decision rules above
