# 07 — Production Order & Timeline

**For:** Internal (Davis) + reference for Robert on timeline asks
**Scope:** Production sequencing, AI generation stack, reference-portrait gate, Thu-Tue working window

---

## Stack

- **Stills:** ChatGPT Images 2.0 via Higgsfield (character-consistency feature for reference-portrait continuity across scenes)
- **Video:** Kling 3.0 Pro or Seedance 2.0 (whichever renders the specific scene better — test both on the first generation per character). Decision rule + model-specific prompting: `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Kling_3.md` and `Seedance_2.md`.
- **Not used:** Nano Banana, Flux, Midjourney (per SC AI creative approach — indistinguishable-from-real standard, not stylized output)
- **Style sheet Injection Blocks:** `Style_Sheets/Elevated_Documentary.md` §2 (Image) + §3 (Video); `Style_Sheets/UGC_Native.md` for Diana + S1-V3 UGC
- **Total AI inference cost across all 24 variants:** ~$10–20

## Reference-portrait gate

**All downstream production is blocked until four reference portraits are locked.** This is the critical path.

Run `Phase_1_Reference_Portrait_Prompts.md` verbatim in Higgsfield for each character. Generate 4 candidates per character, pick one per character, save to `Reference_Portraits/` with metadata.

**Side-specific prop verification before locking each portrait:**

| Character | Side-specific props to verify |
|-----------|-------------------------------|
| **Ty Rivera** | Scar above R eyebrow (dirtbike spill), leg brace/crutch L leg (intramedullary nail surgery on L femur) |
| **Sarah Mitchell** | Arm brace on L forearm (black canvas, Velcro), fading bruise on L temple (3-week healing, yellow-green), small chin scar |
| **Laura Henderson** | Cane in L hand (she was hit on R side, weight shifts to cane), ACE wrap on R ankle beneath jean cuff, small old kitchen-knife scar on L forearm |
| **Diana Nguyen** | R arm in fabric medical sling (diagonal strap L shoulder to R hip), mole above L upper lip, yellowing bruise along R jawline (fading) |

**Critical:** if any side-specific prop renders incorrectly in the locked portrait (e.g., Sarah's brace appears on R forearm instead of L), the character will be *inconsistent* across the variants that feature them. Regenerate until sides are correct. This is the single most common AI-portrait failure mode.

### Jason — already locked

Jason Reardon (45, concrete foreman, Apache Junction, AZ — male volume slot) reference portrait was locked 2026-04-29 from the Bold Sister-Line Concept Room session. Saved at `Reference_Portraits/jason_reference_locked_v1.png` with metadata at `jason_reference_lock.md`. Side-specific lock: walker/cane on the LEFT (left femur fracture), calloused right palm visible, wedding band on left ring finger, 5-day stubble, Carhartt overshirt unbuttoned, slip-on Crocs (Weeks 1–5) or unlaced Red Wing Iron Rangers (Weeks 6+). Usable for whichever J2 wild register-bend gets selected for build-out, plus J1 standard when built.

**Reference portraits required: 5 characters** — Ty, Sarah, Laura, Diana, Jason. All locked.

---

## Production tiering summary

| Tier | Description | Time estimate | Units |
|------|-------------|---------------|-------|
| **A** | Text-swap on locked scene architecture (reuse primary scene, swap text overlay + maybe one new prop shot) | ~30min per variant | 16 units |
| **B** | New scene, locked character (requires new Kling/Seedance generation) | ~1-2hr per variant with iteration | 12 units |
| **C** | High-risk or new-composition variant (dramatization, poetic restraint) | ~4-6hr with iteration + counsel loop | 2 units |

### Unit-by-unit production tier

| Unit | Variant | Tier | Register |
|------|---------|------|----------|
| **S1 primary (S1.mov)** | **Hit by a Freightliner on I-17?** *(produced — persona-accurate)* | B | Cinematic + Motion-Still |
| S1-V1 | Commercial insurance is different. So is the lawyer. | A | Cinematic motion |
| S1-V2 | Their legal team was working before the ambulance arrived. | A | Cinematic motion |
| S1-V3 Elevated | The first offer is rarely the fair offer. | B | Cinematic motion |
| S1-V3 UGC | (same hook, UGC register) | B | UGC |
| S1-V4 | Hit by a semi on I-10? *(broad-reach alt)* | A | Cinematic motion |
| S1-V5 | FMCSA violations. Maintenance records. A $1M policy. *(ultra-literate)* | B | Cinematic motion |
| **S2 primary (S2.mov)** | **$18,000 for $74,000 in bills?** *(produced — late-funnel offer-validation)* | B | Cinematic Documentary |
| **L1 primary (L1.mov)** | **Hit while crossing the street?** *(produced — motion-still primary, MS-Laura)* | B | Cinematic Documentary motion-still |
| L1-V1 | The crosswalk you crossed ten thousand times. | A | Cinematic still |
| L1-V2 | You weren't the one driving. | A | Cinematic still |
| L1-V3 | The street is still there. She isn't, yet. | B | Cinematic still |
| L1-V4 | Gilbert & Warner changed in 1.5 seconds. | A | Cinematic still |
| L1-V5 | You walked the same route every morning. Your dog still needs those walks. *(Maggie appears)* | B | Cinematic still |
| **D1 primary (D1.mov)** | **Broken bones. Bills don't stop.** *(produced — Cinematic + UGC hybrid)* | B | Cinematic Documentary |
| D1-V1 | Three kids. Two incomes. One crash. | B | UGC |
| D1-V2 | Who knew where the permission slips were? | B | UGC |
| D1-V3 | They offered eighteen thousand. The ER alone was six. | A | UGC |
| D1-V4 | Concussion won't let you sleep. Neither will the bills. | B | UGC |
| D1-V5 | Three kids. One stable paycheck. One summer-to-winter cycle. One crash. *(construction-family)* | B | UGC |
| **T1 primary (M1.mov)** | **Riders don't ask for sympathy, they ask for what's fair.** *(produced)* | B | Cinematic motion |
| T1-V1 | Every rider knows what happened. The court should too. | A | Cinematic motion |
| T1-V2 | A rider doesn't need pity. He needs a receipt. | A | Cinematic motion |
| T1-V3 | Six thousand Arizona riders. One got hit this month. He wasn't speeding. | B | Cinematic motion |
| **T2 primary (T4(2).mov)** | **Hit on a motorcycle? Find out what the law says about your case.** *(produced — dashcam-evidence video)* | B | Cinematic Dashcam-Evidence |
| T2-V1 (planned) | A driver didn't see the rider. | A | Cinematic still |
| T2-V2 (planned) | The rider saw the car. The car didn't see the rider. | B | Cinematic still |
| T2-V3 (planned) | Forty-five in a forty-five. Witness: the skid marks. | A | Cinematic still |
| T2-V4 (planned) | The helmet didn't fail. The driver did. | B | Cinematic still |

**Totals:** 6 produced launch units (S1 primary, S2 primary, L1 primary, D1 primary, T1 primary, T2 primary) + planned variants for refresh rotation. M2 (Ty Loss) cohort dropped from this launch window.

**Jason J1 + J2 status:** both ship in the Week 1 package as directional. Neither has produced units at package-send. **J1** (standard, Cinematic Documentary) is a placeholder pending build-out. **J2** inventories 5 wild register-bend directions (Documentary / Tutorial / Cutscene / Listing / Radio) — Davis selects one for build-out + hook-variant development post Week 1. Production rows for the selected J2 bend land in this table once locked. Reference portrait for Jason already locked 2026-04-29 — production isn't gated on portrait work.

**Reference portraits required:** 5 characters — Ty, Sarah, Laura, Diana, Jason. All locked.

---

## Production status

- ✅ All 6 launch primaries produced (S1 trucking, S2 underpayment, L1 pedestrian motion-still, D1 MVA, T1 motorcycle identity, T2 motorcycle injustice/dashcam)
- ✅ M2 (Ty Loss) cohort dropped from this launch window
- ✅ Jason J1 (standard placeholder) + J2 (5 wild register-bend ideas inventory) added to package as directional; reference portrait locked 2026-04-29; build-out kicks off post Week 1 once Davis selects a J2 direction for primary
- Approval package being routed to Robert + WCTL counsel for sign-off ahead of Meta SAC review
- Target launch: 2026-05-05 (4 days out)
- After Meta SAC clearance: 6 primary creatives live in single consolidated Meta ad set
- Pre-Launch Checklist (per Doc 6 Appendix): quiz funnel live, pixel events firing, TCPA consent approved, lead scoring configured, retargeting audience built-paused

### Week 2 onward — Variant rotation
- Weekly refresh per Doc 6 §7 — swap underperforming primaries with top-variant challengers based on CTR/VTR/CPL data
- Planned variants (S1 V1-V5, L1 V1-V5 statics, D1 V1-V5 UGC, T1 V1-V3, T2 V1-V4 statics) rotate in on data

---

## Production economics note

**Total AI inference cost for all 24+ variants: ~$10–20.** This isn't a typo.

Traditional agency production budgeting ($150-300/hr creative director time × significant iteration hours on broadcast-style assets) doesn't apply to SC's AI-gen pipeline. The real cost is Davis's time on prompting, QA, and final compositing — which is already budgeted into the $975 creative production line item in the signed proposal.

**Implication:** Production volume is NOT the constraint. The constraint is Meta's learning-phase threshold (~50 conversions/week at this budget, which caps how many creatives can be live simultaneously in one ad set without starving each below learning floor). That's a **rotation discipline** — "how many go live this week vs. hold for refresh," not "how many can we afford to produce."

All 24 variants produced. 6 live at launch. 18 in the refresh pool, rotated in on data.
