# Session Note — Audience Playbook Rigor Refinement

**Date:** 2026-04-21
**Session type:** Abracadabra bring-in (NIGEL_BRING_IN_PROTOCOL)
**Attendees:** Nigel Bogle (liaison), Julian Cole (chair), Simon Croft, Byron Sharp, Richard Shotton (active); Mark Ritson, Les Binet (silent observers)
**Ask from Davis:** "I need to start doing research and strategy for the AZ campaign. I already have some stuff built out but I want to refine it and make it better."
**Scope Davis set during discovery:** Audience, targeting & media plan (the six `Audience/` docs). Output = sharpened internal playbook. Weak area = **rigor** — numbers and assumptions feel thin.

---

## What the room found

**Julian's read:** The craft is strong. The personas have specificity. The architecture logic is sound. What's thin is the layer *underneath* the craft — numbers that drive decisions aren't sourced, and thresholds aren't bound to decision rules. Doc 3 alone has three load-bearing figures a skeptical reviewer could knock over in minutes: the 65% quiz completion rate, the 40% non-soft-tissue pass rate, and the motorcycle representation rate of 60%.

**Shotton on methodology transparency:** The persona work is good — deprivation thinking is the right frame. But "Jon Steel's Natural Habitat Research + Deprivation Thinking" was cited as a protocol without being explained. Readers assume ethnography when the label doesn't specify otherwise. Decision: declare methodology honestly — demographic modeling + behavioral research + professional judgment, not ethnographic interviews. Label doesn't diminish the work; obscurity does.

**Sharp on the pipeline range:** The reachable-unrepresented-pipeline estimate of 2,775–7,400 is a 2.6× spread. At 2,775 the capture math is tight; at 7,400 it's trivial. That range is hiding a decision, not making one. The spread traces to the representation-rate estimates in Doc 3 — all of which are internal judgment with no AZ bar data, no intake survey, no WCTL historical data backing them. Decision: label as internal estimates, request WCTL historical data for Phase 2, flag the 2.6× as the single widest uncertainty in the playbook.

**Croft on kill criteria:** "If CTR <0.8%" is a category, not a decision. By when? Who decides? What action? "Pause and diagnose" isn't a decision either. Decision: every threshold in Doc 6 §6 gets bound to a full rule — metric, window, who, action, funnel-friction diagnosis protocol where relevant.

**Ritson (pulled in):** Build a single evidence register. Don't fix every number today — just *label* every number today. "Internal estimate, validated Week 1" is a perfectly respectable status. Unlabeled is not.

---

## Decisions made

1. **Create `00_Evidence_Register.md`** as a single-page index of every load-bearing number across the six docs. Status column: `sourced` / `sourced-dated` / `derived` / `internal estimate` / `extrapolated` / `hard`. Becomes the single source of truth — if a number changes, it changes there first.
2. **Three rigor moves applied across all six docs:** (a) source or label every load-bearing number, (b) add sensitivity where math is fragile, (c) bind every threshold to a decision rule.
3. **Do not rewrite creative or architecture.** The hooks are strong, the 2-ad-set decision is sound. Scope is rigor only.
4. **Sequencing:** Evidence Register first → Doc 3 (structural) → Doc 6 (operational, closest to launch) → Docs 1, 2, 4, 5.
5. **SB-37 vs. Arizona Bar jurisdiction:** Doc 5 had been treating SB-37 and AZ Bar rules as interchangeable compliance frameworks. Clarified: AZ Bar ER 7.1/7.3/7.5 is **legally required** for this pilot; SB-37 is **voluntary brand standard** adopted for Phase 4 CA readiness. Anything labeled "SB-37 principle" in Doc 5 is now flagged as voluntary brand consistency.
6. **Sofia (Rideshare) persona scope change:** Down-weighted to Phase-2 scaffolding. At ~17 non-ST incidents/month (Register 3.7, extrapolated), rideshare does not warrant dedicated Phase-1 creative. Persona retained for future volume.
7. **Sofia's own injury profile is partly soft-tissue-borderline** (cervical strain + disc bulge + annular tear + fractured wrist). Flagged inline — the wrist clearly qualifies, the cervical work is borderline. Consistent with down-weighting.
8. **New content added:** Evidence Register (§00); §5.5 Sensitivity Analysis in Doc 3; §6.5 Audience Exclusions + Lead-Quality-by-Timing in Doc 6; Post-Accident Engagement-Timing framework in Doc 2; Primary↔Backup Creative Mapping in Doc 5.

---

## Load-bearing surprises worth remembering

- **Doc 3 §3 monthly-incident sum (~1,388) didn't match Doc 1 headline (925–1,233).** The difference is dedup across overlapping categories (DUI-motorcycle, truck-pedestrian, DUI-MVA). Dedup math now shown explicitly in Doc 3.
- **DUI non-ST % inconsistency:** Doc 3 §3 treated all 298 monthly DUI injury crashes as 100% non-ST, while note §3.5 elsewhere said ~60%. Reconciled to 60% — the 298 figure is DUI *injury* crashes from ADOT, not specifically non-ST.
- **Budget framing mismatch between Doc 3 and Doc 6:** Doc 3 runs the architecture math on $7,750 Meta-only; Doc 6 allocates $6,250 to Meta + $1,500 to geofencing / TikTok / Reddit. Both docs now reference the mismatch explicitly; deciding which framing to hold is a pre-launch call.
- **Phase 1 CPL range of $620–$1,033 (67% uncertainty)** is not a forecast — it's the cost-of-learning band ($3,100 ÷ 3 = $1,033; $3,100 ÷ 5 = $620). Re-framed in Doc 6 as a narrowing band with expected CPL trajectory by week. Do NOT report Week-1 CPL to Robert as a weekly number; report rolling cumulative + trajectory.
- **Geofencing 3.1× hospital lift** is sourced but from a single vendor (Propellant Media case study). Register flags as directional, not guaranteed. Doc 4 now notes the single-source limitation inline.
- **TikTok rejection probability** has no sourced benchmark. Our working estimate: 30–50% rejection on first submission. Decision rule: Day 1–2 rejection → reallocate $625 to Meta within 48 hours; have a second educational-framed variant pre-produced for same-day re-submission.

---

## Files modified

| File | Change |
|---|---|
| `Audience/00_Evidence_Register.md` | **NEW** — single-page index of 70+ load-bearing numbers with status + validation plan |
| `Audience/01_AZ_Non_Soft_Tissue_Demographics.md` | Rigor banner; confidence interval on 925–1,233; 2.6× pipeline-spread note; rideshare extrapolation top-flagged |
| `Audience/02_Case_Type_Personas.md` | Methodology transparency banner; Sofia scope note (Phase-2 scaffolding); Post-Accident Engagement-Timing framework |
| `Audience/03_Audience_Sizing_By_Case_Type.md` | Rigor banner; dedup math explicit; DUI non-ST % reconciled; `[est]` labels across §5; new §5.5 sensitivity + decision rules; §12 25/75 split justified |
| `Audience/04_Platform_Behavior_And_Reach.md` | Rigor banner; AZ CPM moderation calc shown explicitly; TikTok rejection-probability working estimate; geofencing 3.1× single-source caveat |
| `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` | Rigor banner; SB-37 vs. AZ Bar jurisdiction clarified; §A self-qualification as Week-1 hypothesis; §G Primary↔Backup Creative Mapping |
| `Audience/06_Media_Plan_And_Budget_Allocation.md` | Rigor banner; Phase-1 CPL re-framed as cost-of-learning band; buffer math reconciled; §6 kill criteria re-bound to full decision rules; §6.5 Audience Exclusions + Lead-Quality-by-Timing framework |

---

## Open items

- **Request from Robert / WCTL:** Historical intake representation-rate data by case type, if shareable. Replaces Register 5.1–5.6 internal estimates with measured values for Phase 2 planning.
- **Pre-launch call:** Reconcile Doc 3 vs. Doc 6 budget framing before Week 1 launch. Pick one and update the other.
- **TikTok creative:** Produce a second educational-framed variant alongside the primary, so that a Day-1 rejection doesn't burn 48+ hours.
- **Sofia re-eval:** Revisit after Phase 1 to decide whether Phase 2 warrants dedicated rideshare creative.

---

*Curated notes, not transcript. Full session lives in the 2026-04-21 conversation.*

---

## Update 2026-04-21 PM — Creative concepting session + three corrections

Nigel bring-in round two, same day. Hegarty-led creative concepting on the 8 Week-1 launch assets (Doc 5 §G). Full drafts of hooks, body copy, CTAs, visual direction landed in `Creative/Week_1_Launch_Concepts.md`. After review, Davis flagged three corrections that rippled back through the playbook:

1. **DUI is out of scope.** WCTL's signed Service Agreement §1.3 (2026-04-16) excludes DUI. Earlier Audience/ drafts (written pre-contract) baked DUI in throughout. Response: S4 (DUI creative) removed from launch set → 7 assets total, not 8. DUI sections in Doc 1 §5 and Doc 2 §5 (James persona) banner'd as out-of-scope and preserved for Phase 2 reference. Doc 3 §12 Ad Set 2 creative variants and lead distribution updated — former DUI share (~3 leads / 20%) redistributes to MVA (40% → 50%) and Pedestrian (25% → 30%). Doc 6 §2 Campaign 2 structure drops to 6 variants. Evidence Register marks DUI rows (2.15, 2.16, 3.5, 4.3, 5.4) as excluded; adds new row 1.11 pinning the in-scope case list to Contract §1.3. The ROAS math holds at 7–9× — MVA absorbs most of the displaced DUI volume at similar settlement values.
2. **All creative is AI-generated.** No stock b-roll, no live shoots, no composite approaches. Per SC brand standard, AI imagery must be indistinguishable from real footage (no "AI slop"). Creative doc production routes updated across all 7 assets; Doc 5 §G timeline updated to reflect AI-only workflow.
3. **M3 hook swapped** from *"She said she didn't see you"* → *"A driver didn't see the rider."* Fully third-person, compliance-clean by default. Removes the counsel pre-review dependency that was in the original draft. Body copy adjusted to match third-person framing.

**Additional direction Davis gave during the rewrite:** each persona gets a **consistent protagonist character** (one AI-generated face maintained across all assets for that persona, anchored to a single reference image per character). Marco appears across M1/M2/M3; Sarah in S1; Miguel across S2/S3 (same character, two languages); Diana in S5. For Phase 1 testing discipline, face is locked per persona — hooks compete against a stable protagonist; face variation is a Phase 2 test when budget scales past ~150 weekly completions per ad set.

### Files touched in this update

| File | Change |
|---|---|
| `Creative/Week_1_Launch_Concepts.md` | S4 removed; M3 hook swapped; protagonist added to all 7 assets (Marco / Sarah / Miguel / Diana); all-AI production; Cross-Asset Summary and Production Standards rewritten |
| `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` | §G asset counts 8→7, 5 severe→4; video/static split 7/6; Primary↔Backup mapping trimmed; Persona-to-Creative Mapping strikes James row |
| `Audience/03_Audience_Sizing_By_Case_Type.md` | Scope-update banner at top; §12 Ad Set 2 creative variants table removes DUI; lead distribution redistributes 20% to MVA/Pedestrian; pipeline value table updated; Implementation Blueprint updated |
| `Audience/06_Media_Plan_And_Budget_Allocation.md` | Scope-update banner; Campaign 2 structure removes Creative 5 (DUI); quiz funnel Step 1 options updated; reallocation trigger wording updated |
| `Audience/01_AZ_Non_Soft_Tissue_Demographics.md` | §5 (DUI) banner'd as out-of-scope, preserved for Phase 2 reference |
| `Audience/02_Case_Type_Personas.md` | §5 (James persona) banner'd as out-of-scope; Cross-Persona and Engagement-Timing tables strike James rows |
| `Audience/00_Evidence_Register.md` | Rows 2.15, 2.16, 3.5, 4.3, 5.4 marked excluded; §3.1 shows pre- and post-DUI-removal ranges; new row 1.11 pins Contract §1.3 case list; §11.2 marked RESOLVED by scope change |

### Open items still on Davis's plate

1. **Lock 4 protagonist reference images** (Marco, Sarah, Laura, Diana). Generate 3–4 candidates each, pick one per character, lock reference. Must happen before any asset production.
2. **Send Week 1 Launch Concepts doc to Robert** for directional approval first, then creative approval per Service Agreement §7.1 (5 business-day turnaround on the final).
3. **AI production stack** — ChatGPT Images 2.0 per Davis's 2026-04-22 note. Accuracy not a concern; prompts can be as detailed as character briefs specify.

---

## Update 2026-04-22 — Casting + architecture + scope simplification

Second creative concepting pass, same week. Davis raised three strategic questions that produced substantive changes:

1. **Casting — homophily / AZ demographic alignment.** The original 4 protagonists I drafted cast 0 white characters despite AZ being 51% White. Davis correctly flagged this as a reach miss — homophily bias (documented across all demographic groups) means white viewers are less likely to engage with minority-specific creative than vice versa, so the broad-net assets need majority-representative casting. Resolution: **Marco revised to white (Arizona-weathered rider), Diana revised to white (Arizona working mom). Sarah kept as racially-ambiguous mixed white-Latina (already broad). New character Laura added as white suburban-Phoenix pedestrian protagonist for S2 English.** The persona psychological profiles in Doc 2 remain exactly as written — only the on-screen casting reflects the AZ demographic math. Full character briefs in `Creative/Week_1_Launch_Concepts.md` under Protagonist Character Briefs.

2. **Spanish creative (S3 Miguel) — deferred to Phase 2.** Decision to drop S3 from Phase 1 launch. Rationale: at Phase 1 budget, Spanish as 1-of-7 creatives in a broad AZ ad set will likely be starved by the algorithm (narrower audience = fewer events → de-prioritized). Operational complexity is real (Spanish copywriter hire, Spanish funnel build, WCTL Spanish intake confirmation, separate Spanish compliance review). Phase 2 gets a dedicated Spanish ad set with meaningful budget to prove the channel properly. Miguel's persona and character brief retained in the Phase 2 planning material — not deleted, just parked. Phase 1 English-only launch simplifies the pilot and makes for a cleaner proof-of-concept narrative to Robert.

3. **Campaign architecture — collapsed to one campaign / one ad set.** Simon's revised read (answering Davis's direct question): the original two-campaign / 25-75 split architecture was a compromise for motorcycle budget protection, at the cost of signal-density fragmentation. At this budget, ONE ad set with all 6 creatives produces ~200 weekly completions (4× Meta learning threshold) vs. threshold-level in the split architecture. Motorcycle creative's 5/5 identity-based distinctiveness protects its reach naturally — the algorithm will serve motorcycle creative to riders because it's useless to non-riders. **Hot-swap contingency** (Doc 6 §7) defined: if motorcycle drops below 15% impression share at Day 7, split to two ad sets with a dedicated $1,500 motorcycle budget for the remainder of the campaign.

### Net Phase 1 launch set

- **6 assets, all English, single ad set:** M1, M2, M3 (Marco white motorcycle), S1 (Sarah trucking), S2 (Laura pedestrian EN), S5 (Diana MVA)
- **4 locked protagonists:** Marco, Sarah, Laura, Diana — one AI reference image per character
- **One campaign (WCTL-AZ-Pilot)** + retargeting campaign activating Week 4
- **~$220/day Phase 1** single-ad-set budget, tapering to ~$110-165/day across Phases 2-3
- **Deferred to Phase 2:** Spanish creative (S3), two-ad-set architecture (hot-swap only)

### Files touched in this update

| File | Change |
|---|---|
| `Creative/Week_1_Launch_Concepts.md` | S3 section removed; Miguel character brief removed (parked for Phase 2); Laura character brief added; Marco / Diana briefs revised to white casting; legend + casting summary + cross-asset summary updated (7→6 assets, 4 protagonists); open items + next steps simplified (no Spanish copywriter hire, no Spanish intake dependency) |
| `Audience/06_Media_Plan_And_Budget_Allocation.md` | §2 Campaign Structure rewritten: two campaigns → one main campaign + retargeting, one ad set with all 6 creatives; phase budget tables updated; §4 daily schedule simplified; §5 optimization events updated; §7 reallocation triggers rewritten with hot-swap contingency |
| `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` | Scope banner noting Spanish deferral + single-ad-set architecture; §G asset table S3 removed; launch set 7→6; Persona-to-Creative mapping Miguel row struck, Laura row added |
| `Audience/03_Audience_Sizing_By_Case_Type.md` | §12 architecture-update banner pointing to Option C (single ad set) as the operative Phase 1 architecture; Modified Option B retained as reasoning |
| `Audience/00_Evidence_Register.md` | §8 projected outputs updated with 8.2a (single-ad-set weekly completions ~168–252, 4–5× threshold); 8.2/8.3 marked hot-swap contingency only |

### Open items after this update

1. **Lock 4 protagonist reference images** (Marco, Sarah, Laura, Diana) — generate 3–4 candidates each, Davis picks.
2. **Robert directional approval** on the concepts doc before full production.
3. **Final creative approval** from Robert per Service Agreement §7.1 after mockups are generated.
4. **Meta ad review submission** 48-72 hours before intended launch.
5. **Phase 2 planning should include:** Spanish creative build, Miguel persona activation, dedicated Spanish ad set, Spanish intake capability with WCTL, rideshare (Sofia) re-evaluation.

---

## UPDATE LOG — 2026-04-22 PM — Full shit-test execution (Abracadabra + 03_Media bring-in)

Davis requested a full adversarial shit-test before committing to protagonist image generation and Robert approval. "Make sure everything is perfect before I go forward."

### Session structure

- **Phase 1 (AM):** Launched 3 Explore agents in parallel with adversarial framing to do deep reads of file clusters (Rigor / Strategy / Execution). Produced 38 findings: 12 blockers, 15 important, 11 polish. Written to `_Research/shit_test_review_2026-04-22.md`.
- **Phase 2 (PM):** Davis approved "execute all blockers + 15 important sequentially" and requested `03_Media` doctrine anchoring since the fixes are operational-media territory that hadn't been consulted yet.

### 03_Media bring-in

Added Depesh Mandalia (Meta paid social), Simon Croft (media buying systems), and Indigo Sato (performance creative) to the room as doctrine authors on fix calls. Specific anchors:

- Simon's `Media_Buying_Systems.md` — kill criteria 1.25-1.5× target miss band, frequency 3.0/5.0 thresholds, don't-starve-channels doctrine
- Simon's `CPL_CPM_Dashboard_Framework.md` — next-dollar allocation, decision rules
- Depesh's `Special_Ad_Categories.md` — SAC-compliant campaign structure for PI (Social Issues category)
- Depesh's `Lead_Gen_Playbook.md` — retargeting timing (7-day window), instant-form vs landing-page decision
- Indigo's `Creative_Testing_Framework.md` — 3-2-2 testing, Week 2 rotation, 20-30% testing budget

### Execution outcome

**12/12 BLOCKERS resolved.** Budget math reconciled ($9,975 contract / $7,750 Meta-only), kill thresholds aligned Register ↔ Doc 6 ↔ §13, retargeting activation shifted Week 4 → end of Week 2, Creative doc coherence fixed (21-lead target stated, 4 protagonists correct, Ad Set 1/2 renamed, Spanish deferral explicit), persona-vs-casting callout added, C3/C4 deactivated, DUI dedup math inline.

**15/15 IMPORTANT resolved.** Stale funnel rates in Doc 4 §10 calibrated, Doc 3 Option tables banner-flagged as pre-calibration, Modified Option B recast as historical reasoning, Marco age reconciled, third-person M-series verification added to Doc 5 §F, AZ-counsel review required in compliance, prop consistency spec expanded per-character, 7-step funnel locked, Persona-to-Creative Mapping ad-set column updated, gender split rationale expanded, self-qualification kill path escalation added, Sofia Phase 2 banner added, "Lead-Response-Timing" rename with clarification.

**11 POLISH deferred by design.** Documented in findings doc. None block launch.

### Launch readiness

RED (AM audit) → AMBER (post-blocker fixes) → **🟢 GREEN (post-important fixes)**. Playbook internally consistent, budget-reconciled, compliance-layered, and cold-read-defensible.

### Files touched in this update

| File | Change |
|---|---|
| `Audience/06_Media_Plan_And_Budget_Allocation.md` | §1 budget collapsed to Meta $7,750; §2 retargeting activates end of Week 2; §3 Phase 2/3 allocations updated; §4 daily schedule reflects retargeting Week 2+; §5 pixel note rewritten; §5 optimization events table calibrated; §6 kill thresholds aligned to Register (45/30/10); §6.5 renamed Lead-Response-Timing; §9 event flow updated; §11 risk mitigation calibrated; Appendix pre-launch checklist item 10 fixed; Appendix Key Numbers Reference Card fully calibrated |
| `Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md` | §A hypothesis escalation path added (15/10/8% tiers); §C matrix active variants C1/C2/C5 = 3 + motorcycle 3 = 6; C3 + C4 section headers banner-deactivated; §F Motorcycle Third-Person Verification checklist + AZ counsel review; Persona-to-Creative Mapping updated to Single ad set; Budget summary reconciled to $9,975 |
| `Audience/04_Platform_Behavior_And_Reach.md` | §10 funnel rates recalibrated (70/65/40 → 60/40/15), end-to-end math reworked |
| `Audience/03_Audience_Sizing_By_Case_Type.md` | §6 reading-guide banner added; §12 Modified Option B framed as Historical Reasoning superseded 2026-04-22 |
| `Audience/02_Case_Type_Personas.md` | Persona ≠ Casting callout added at top with mapping table; §6 Sofia Phase 2 scaffold banner |
| `Audience/01_AZ_Non_Soft_Tissue_Demographics.md` | §5 DUI banner includes dedup math (gross 1,080 − DUI 298 = ~750-1,050 pilot-eligible) |
| `Audience/00_Evidence_Register.md` | Rows 1.5–1.8 updated for Meta-only collapse; 7.11 + 7.12 deprecated to Phase 2; 8.4–8.8 updated; 11.3 marked resolved; §13 decision rules aligned (45/30/10 thresholds) |
| `Creative/Week_1_Launch_Concepts.md` | 21-lead business objective added to header; 4 Locked Reference Characters (was "5") with Miguel Phase 2 footnote; "Ad Set 1/2" headers renamed to case-type groupings with single-ad-set note; Open Item #4 Spanish deferral; M1 Marco age 35→38 with persona-vs-casting note; prop consistency expanded per-character; gender split rationale expanded; AZ counsel review added; 7-step funnel locked |
| `_Research/shit_test_review_2026-04-22.md` | Verdict flipped RED → GREEN; FIX EXECUTION LOG section appended with per-finding resolution + doctrine anchor cites |

### Next actions (Davis owns)

1. **Protagonist reference image lock** — generate Marco, Sarah, Laura, Diana candidates using locked briefs (ChatGPT Images 2.0 character-consistency mode).
2. **Send Creative doc to Robert** for directional approval (hooks + visual direction + rationale, no mockups yet) per Service Agreement §7.1 / §7.2 — two-step approval is safer than one big one.
3. **Generate 6 Phase 1 creatives** after directional sign-off.
4. **AZ-licensed counsel review** of final creative before Meta submission per the newly-explicit compliance checklist item.
5. **Meta ad review submission** 48-72 hours before intended launch.
6. **Phase 2 scope proposal** (drafted by Week 4): Spanish ad set with dedicated budget, multi-channel diversification (geofencing / TikTok / Reddit with budgets calibrated to clear each channel's signal threshold), rideshare segment evaluation, WA expansion.
