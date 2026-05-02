# WCTL Anchor Template Spec

**Status:** Phase 1 deployment spec. Built 2026-04-30 from Anchor Session.
**Pattern reference:** `../../../02_Visual/Designed_Overlay_System.md §6 Pattern 6 — The Anchor`
**Higgsfield mockup prompts:** `../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Higgsfield_Anchor_Mockup_Prompts.md`
**Split-test plan:** `Phase_1_Split_Test_Plan.md`

---

## What the Anchor is for WCTL

A persistent Fair Case-branded bottom-third overlay that gives half-listening / 0.5s-glance scrollers immediate brand+context+CTA throughout the entire spot. Designed for the FB-Feed-leaning portion of the AZ non-soft-tissue PI demo (30-54 commuters, 80% FB adoption / 58% daily — `../Audience/04_Platform_Behavior_And_Reach.md`). Deployed selectively per persona-platform fit; not applied as default across all 32 Phase 1 units.

## Fair Case Anchor Spec — Locked

| Element | Spec |
|---|---|
| **Position** | Bottom 35-40% of 9:16 frame (672-768px tall in 1080×1920); pinned, no animate-in/out |
| **Duration** | Frame 0 through CTA frame — full spot |
| **Background** | Roman Navy `#0D1F3C` solid (over light footage: 88-92% opacity); 0.5pt Torch Amber `#C8821A` rule at top edge |
| **Headline** | Tiempos Headline Medium 56-72pt white `#FFFFFF`, 1-2 lines, +20-30% line-length budget for Phase 2 Spanish |
| **Secondary** | Inter Medium 22-26pt Muted Navy Light `#A8B8CC`, 1 line |
| **Disclaimer** | Inter Regular 11-13pt Muted Navy Light at 70% opacity, 1 line, very bottom |
| **CTA prompt** | Inline Torch Amber `#C8821A` arrow `→` at end of secondary OR Torch Amber pill flush-right |
| **Brand mark** | Fair Case torch (Roman Navy mark + Torch Amber flame), 28-32pt height, top-right of Anchor zone |
| **Padding** | 48px L/R, 24px T/B |
| **Aesthetic direction** | TBD — Davis picks from 5 Higgsfield mockup directions; room recommends Direction 1 (Roman Navy Authority) or Direction 4 (Newspaper Strip Editorial) for FB-Feed-heavy AZ demo |

**1:1 deprecated** as of 2026-05-01 (Davis: "I never see them"). Anchor renders at 9:16 + 4:5 only.

## Variation Copy Library (Phase 1 English + Phase 2 Spanish-ready)

| Variant | Headline | Secondary | Disclaimer | Use for |
|---|---|---|---|---|
| **A — Promise** | Free case review | 45 seconds. No obligation. | Attorney advertising. Prior results do not guarantee outcomes. | Sarah trucking |
| **B — Specificity** | See what your case is worth | Reviewed by California-licensed attorneys. | Attorney advertising. Not legal advice. | Sarah trucking + Laura pedestrian |
| **C — Speed** | Hurt in a wreck? | We respond in under 24 hours. | Attorney advertising. Free consultation. | Diana cinematic |
| **D — Reassurance** | $0 upfront | You pay nothing unless we win. | Attorney advertising. Contingency-fee representation. | Diana cinematic |
| **E — Trust (Phase 2)** | Lo atendemos en español | Consulta gratuita. 24/7. | Anuncio legal. No garantizamos resultados. | Phase 2 Spanish pedestrian (Maryvale/South Phx) |

## Per-Unit Deployment Map (Phase 1)

| Unit | Persona | Surface fit | Anchor? | Variant pairing | Why |
|---|---|---|---|---|---|
| **S1 Sarah Trucking — primary cinematic** | 25-54 commuter, FB-heavy | FB Feed-native | **YES** | Variant A | Trucking commuter demo lives on FB Feed; designed-editorial register native |
| **S1 V1-V4 (Sarah variants)** | Same | FB Feed-native | **YES** | Variant B | Specificity ("Reviewed by California-licensed attorneys") matches Sarah's clinical composure |
| **S2 Laura Pedestrian — static (5 units)** | 25-44 / 55-64, lower-income FB-heavy + Spanish FB | FB Feed-native | **YES** | Variant B | Quiet-dignity register + Anchor reads as WSJ print-ad bottom strip; trust signal |
| **S5 Diana Cinematic — primary (~3 units)** | 25-44 working-mother, FB highest daily use | FB Feed-native | **YES** | Variants C + D split | C ("respond in 24 hrs") for urgency framing; D ("$0 upfront") for financial-relief framing |
| **S5 Diana UGC variants (~2 units)** | Same | IG Reels / Stories-native | **NO — Clean** | n/a | UGC pattern-interrupt depends on looking like content not ad; Anchor breaks the mechanic |
| **M1 Ty Identity (4 units)** | 25-44 male rider, IG Reels + FB Reels | IG Reels-native + identity self-qualification | **NO — Clean** | n/a | Riders pattern-match on the rider, not the brand panel |
| **M2 Ty Loss (4 units)** | Same | IG Reels-native | **NO — Clean** | n/a | Same — identity-trigger preserved |
| **M3 Ty Injustice (4 units)** | Same | IG Reels-native + static-with-object discipline | **NO — Clean** | n/a | M3's object-story register is editorial-still; Anchor would feel pasted-on |
| **HN-1.7B + EX-Settlement-Gap (Designed Static Brand Units, 2 units)** | Authority signal | FB Feed-native | **NO additional Anchor** | n/a | Already designed objects (Hero Number / Exhibit patterns); double-overlay creates fight |

**Net Phase 1 Anchor coverage:** ~13 anchored units / ~32 total = **~40% of the package**. Not 6%, not 100%. Forty percent — the share of the addressable market that's FB-Feed-native.

## Production Path

1. **Mon 2026-05-04 AM:** Davis runs the 5 Higgsfield mockup prompts (`../../../../04_Production/Giuseppe_Karma_(AI_Creative_Director)/Higgsfield_Anchor_Mockup_Prompts.md`) at 2 variants each = 10 mocks. Cost ~$0.40-$0.80.
2. **Mon 2026-05-04 PM:** Davis lays mocks side-by-side in Figma, picks aesthetic direction by FB-Feed fit + brand-feel.
3. **Mon-Tue 2026-05-04/05:** Davis builds Figma component with linked text overrides for the 4 English variants (A/B/C/D); E held for Phase 2.
4. **Tue 2026-05-05:** Davis or Alex composites the Anchor over existing Sarah/Laura/Diana cinematic footage in CapCut. ~6-9 new anchored variant units. Existing footage unchanged; only Anchor layer added.
5. **Wed 2026-05-06:** Robert pre-launch review. Show one Sarah-Anchored + one Sarah-Clean side-by-side. Frame as Phase 1 split-test variable per `Phase_1_Split_Test_Plan.md`.
6. **Thu 2026-05-07 onward:** Launch. Validate per Week 1 placement-segmented metrics.

## Branding Integrity Notes

- The Anchor is the FIRST and ONLY SC pattern that carries the Fair Case torch logo in the overlay layer. Everywhere else, branding lives in the final CTA frame (per Giuseppe Principle 6 + `feedback_branding_last_pass.md`).
- The Anchor panel sits ABOVE the Meta UI (Like / Comment / Share rail) by default safe-zone padding (250px from frame bottom). On Reels surface, the algorithm crops slightly differently — verify Anchor doesn't intrude on the Meta system Learn More button.
- The Torch Amber `#C8821A` flame in the brand mark is the ONE invariant per Fair Case identity rule — never altered, even when the rest of the Anchor adapts opacity or color treatment.

## Pre-Ship Verification

Before any anchored unit ships, run the same `Designed_Overlay_System.md §10` checklist plus these Anchor-specific items:

- [ ] Anchor occupies bottom 35-40% only (not creeping above mid-frame)
- [ ] Headline reads in <0.5s glance (test by half-second screenshot view)
- [ ] Spanish copy length pre-tested doesn't break layout (even if Phase 1 is English-only — sets up Phase 2)
- [ ] Fair Case torch logo top-right at correct size, Torch Amber flame intact
- [ ] No Hook Card or Peak Card placed in bottom third (would conflict spatially)
- [ ] Always-on captions live in their 250px bottom-center safe zone above the Anchor (no overlap)
- [ ] Anchor variant pairing matches the persona-deployment table above (no mismatched copy)
- [ ] At-a-glance FB Feed read test: open the spot in a phone Facebook app simulator, scroll past at normal pace, check whether the Anchor delivers brand+message+CTA in the half-second of visibility
