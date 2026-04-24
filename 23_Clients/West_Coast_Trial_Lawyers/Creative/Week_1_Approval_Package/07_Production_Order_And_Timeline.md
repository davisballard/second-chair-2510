# 07 — Production Order & Timeline

**For:** Internal (Davis) + reference for Robert on timeline asks
**Scope:** Production sequencing, AI generation stack, reference-portrait gate, Thu-Tue working window

---

## Stack

- **Stills:** ChatGPT Images 2.0 via Higgsfield (character-consistency feature for reference-portrait continuity across scenes)
- **Video:** Kling 3.0 Pro or Seedance 2.0 (whichever renders the specific scene better — test both on the first generation per character). Decision rule + model-specific prompting: `Abracadabra/04_Production/Giuseppe_Karma_(AI_Creative_Director)/Prompting_Guides/Kling_3.md` and `Seedance_2.md`.
- **Not used:** Nano Banana, Flux, Midjourney (per SC AI creative approach — indistinguishable-from-real standard, not stylized output)
- **Style sheet Injection Blocks:** `Style_Sheets/Elevated_Documentary.md` §2 (Image) + §3 (Video); `Style_Sheets/UGC_Native.md` for Diana + M2-V1 UGC + S1-V3 UGC
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
| **Rachel (Ty's fiancée — new)** | No injury props. Mid-20s to early-30s, working-class register matching Ty's demographic (per `Deep_Personas/Ty/01_Life_World.md`). Simple engagement ring L hand. Composed, steady, no model-aesthetic. Wardrobe: casual domestic (t-shirt + jeans or sweatpants). Face should read as the person who holds it together when Ty can't. |

**Critical:** if any side-specific prop renders incorrectly in the locked portrait (e.g., Sarah's brace appears on R forearm instead of L), the character will be *inconsistent* across the 5 variants that feature them. Regenerate until sides are correct. This is the single most common AI-portrait failure mode.

**Rachel note:** Only appears in M2-V4 (single-variant character), but still needs locked reference portrait for consistency within that variant's composed/couple frames. Generate alongside Ty Friday AM so consistency across Ty-Rachel couple shots in V4 is clean.

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
| **S1 primary** | **Hit by a Freightliner on I-17?** *(swapped 2026-04-23 — persona-accurate)* | A | Elevated |
| S1-V1 | Commercial insurance is different. So is the lawyer. | A | Elevated |
| S1-V2 | Their legal team was working before the ambulance arrived. | A | Elevated |
| S1-V3 Elevated | The first offer is rarely the fair offer. | B | Elevated |
| S1-V3 UGC | (same hook, UGC register) | B | UGC |
| **S1-V4** | **Hit by a semi on I-10?** *(swapped — broad-reach alt)* | A | Elevated |
| **S1-V5** | **FMCSA violations. Maintenance records. A $1M policy.** *(new — ultra-literate)* | B | Elevated |
| S2 primary | Hit while crossing the street? | A | Elevated (static) |
| S2-V1 | The crosswalk you crossed ten thousand times. | A | Elevated (static) |
| S2-V2 | You weren't the one driving. | A | Elevated (static) |
| S2-V3 | The street is still there. She isn't, yet. | B | Elevated (static) |
| S2-V4 | Gilbert & Warner changed in 1.5 seconds. | A | Elevated (static) |
| **S2-V5** | **You walked the same route every morning. Your dog still needs those walks.** *(new — Maggie appears)* | B | Elevated (static) |
| S5 primary | Broken bones. Bills don't stop. | A | UGC |
| S5-V1 | Three kids. Two incomes. One crash. | B | UGC |
| S5-V2 | Who knew where the permission slips were? | B | UGC |
| S5-V3 | They offered eighteen thousand. The ER alone was six. | A | UGC |
| S5-V4 | Concussion won't let you sleep. Neither will the bills. | B | UGC |
| **S5-V5** | **Three kids. One stable paycheck. One summer-to-winter cycle. One crash.** *(new — construction-family)* | B | UGC |
| M1 primary | Riders don't ask for sympathy. They ask for what's fair. | A | Elevated |
| M1-V1 | Every rider knows what happened. The court should too. | A | Elevated |
| M1-V2 | A rider doesn't need pity. He needs a receipt. | A | Elevated |
| M1-V3 | Six thousand Arizona riders. One got hit this month. He wasn't speeding. | B | Elevated |
| M2 primary | What the crash took is still being taken. | A | Elevated |
| M2-V1 Elevated | Bills don't stop because you can't work. | A | Elevated |
| M2-V1 UGC | (same hook, UGC register) | B | UGC |
| M2-V2 | Twelve thousand for the wedding. Now it's for the surgery. | B | Elevated |
| **M2-V3** | **Southern and Dobson. 4:45 PM. Full sun. She never looked right.** | **C** | **Elevated (dramatization)** |
| **M2-V4** | **Your wedding was supposed to be this spring. Your recovery might not let that happen.** *(new — Rachel in frame)* | B | Elevated |
| M3 primary | A driver didn't see the rider. | A | Elevated (static) |
| M3-V1 | The rider saw the car. The car didn't see the rider. | B | Elevated (static) |
| M3-V2 | Forty-five in a forty-five. Witness: the skid marks. | A | Elevated (static) |
| M3-V3 | The helmet didn't fail. The driver did. | B | Elevated (static) |

**Totals:** 28 hook lines, **30 render units** (including S1-V3 dual-register + M2-V1 dual-register duplicates). Tier A = 16, Tier B = 12, Tier C = 2.

**Reference portraits required:** 5 characters (up from 4) — Ty, Sarah, Laura, Diana, **+ Rachel (new for M2-V4)**. Generate Rachel alongside Ty on Friday AM.

---

## Thu–Tue working window (Davis solo)

### Thu 2026-04-23 — Today
- ✅ Agency session complete (Nigel bring-in protocol 7 beats)
- ✅ Plan approved
- ✅ `Week_1_Approval_Package/` folder created with 00–08 files drafted
- ✅ Session notes written to `_Research/`
- ✅ Existing `Week_1_Launch_Concepts.md` stamped + moved to `Archive/Week_1_Launch_Concepts_2026-04-21.md`
- **Remaining today:** optional — start Tier A text-swap prompt drafting from existing Week 1 concept scenes; review locked persona voice lines for any final variant copy tweaks

### Fri 2026-04-24
- **AM:** Run `Phase_1_Reference_Portrait_Prompts.md` in Higgsfield. Generate 4 candidates × **5 characters** (Ty, Sarah, Laura, Diana, **Rachel — new**). Rachel brief drafted from `Deep_Personas/Ty/01_Life_World.md` relationship context.
- **PM:** Verify side-specific props on each candidate. Lock one portrait per character. Save to `Reference_Portraits/<character_name>_locked.png` with metadata. Once locked, all downstream scene generation is unblocked.

### Sat 2026-04-25 — Tier A production (16 units)
- Primary scene architectures for each of the 6 concepts (rendered once, text-swap thereafter): ~2-3hr
- Text-swap variants: S1 primary (I-17 Freightliner), S1-V1, S1-V2, S1-V4 (I-10 semi), S2 primary, S2-V1, S2-V2, S2-V4, S5 primary, S5-V3, M1 primary, M1-V1, M1-V2, M2 primary, M2-V1 Elevated, M3 primary, M3-V2
- Time: ~5-7hr total
- Note: S1 primary-V4 geography swap means two different freeway b-roll shots (I-17 mountain descent vs I-10 flat desert) — render both early so text-swaps land cleanly

### Sun 2026-04-26 — Tier B production (12 units)
- New scene compositions: S1-V3 Elevated + S1-V3 UGC (phone-call composition), **S1-V5 (FMCSA evidence artifacts — DOT door, driver log, maintenance sticker, $1M policy doc)**, S2-V3 (poetic restraint), **S2-V5 (Laura porch + Maggie Golden Retriever)**, S5-V1 (family system), S5-V2 (invisible labor), S5-V4 (2-4AM low-light), **S5-V5 (construction-family / F-150 + paired pay-stub composition)**, M1-V3 (group ride), M2-V1 UGC, M2-V2 (wedding-fund), **M2-V4 (Ty + Rachel domestic scene — engagement photo + composed couple frame)**, M3-V1 (split-frame), M3-V3 (helmet still-life)
- Time: ~10-14hr total. If running long, defer lower-priority variants (M3-V1, M3-V3, S1-V5) to Monday AM.

### Mon 2026-04-27 AM — Tier C (1 unit)
- **M2-V3 Moment-Before Dramatization.** Intersection approach, Nissan Rogue rendering, cut-to-black timing, Ty recovery cut. "Dramatization" overlay burned in.
- Storyboard frames first (5-6 sketch or rough-render frames) — these go to WCTL counsel before full generation.
- Time: ~4-6hr with iteration.

### Mon 2026-04-27 PM — QA + doc finalization
- Review all 24+ rendered units against indistinguishable-from-real standard
- Verify side-specific prop continuity across every asset featuring each character
- Mute-compliant text legibility check on mobile (open each on phone with sound off)
- Regenerate any failures
- Finalize `Week_1_Approval_Package/` docs 00–08 with rendered stills embedded
- Draft email to Robert with package attached (and separate email to WCTL counsel for M2-V3 heightened review)

### Tue 2026-04-28 AM — Send to Robert + counsel
- Package email to Robert (all 8 files + link to `Week_1_Approval_Package/` folder structure)
- Separate email to WCTL counsel for M2-V3 heightened review
- Target response window: Fri 2026-05-01 (5 business days from send)

### Tue-Fri 2026-04-28 / 05-01 — Approval window
- WCTL review and counsel clearance
- Any edits or resubmissions happen this window

### Sat-Sun 2026-05-02/03 — Final fixes + Meta submission
- Any WCTL-requested edits produced
- Sun EOD: submit 6 launch primaries to Meta Special Ad Category review (48-hour window)

### Tue 2026-05-05 — LAUNCH
- 6 primary creatives live in single consolidated Meta ad set
- Pre-Launch Checklist (per Doc 6 Appendix) complete: quiz funnel live, pixel events firing, TCPA consent approved, lead scoring configured, retargeting audience built-paused

### Week 2 onward — Variant rotation
- Weekly refresh per Doc 6 §7 — swap underperforming primaries with top-variant challengers based on CTR/VTR/CPL data
- If M2-V3 cleared and launched, monitor its CPM carefully for Meta rate-limiting signals (~20%+ CPM lift vs. baseline = reach suppression)

---

## Production economics note

**Total AI inference cost for all 24+ variants: ~$10–20.** This isn't a typo.

Traditional agency production budgeting ($150-300/hr creative director time × significant iteration hours on broadcast-style assets) doesn't apply to SC's AI-gen pipeline. The real cost is Davis's time on prompting, QA, and final compositing — which is already budgeted into the $975 creative production line item in the signed proposal.

**Implication:** Production volume is NOT the constraint. The constraint is Meta's learning-phase threshold (~50 conversions/week at this budget, which caps how many creatives can be live simultaneously in one ad set without starving each below learning floor). That's a **rotation discipline** — "how many go live this week vs. hold for refresh," not "how many can we afford to produce."

All 24 variants produced. 6 live at launch. 18 in the refresh pool, rotated in on data.
