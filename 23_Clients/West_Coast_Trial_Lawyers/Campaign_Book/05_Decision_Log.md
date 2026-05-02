# Decision Log — WCTL AZ Pilot

**Purpose:** Chronological log of decisions made on this campaign — what was decided, why, by whom, when. Add to this when shifting strategic levers; check this when questioning past calls.

---

## Decisions Made (Chronological)

### 2026-04-10 — Discovery call with Robert (locked the brief shape)

- **Decided:** $10K AZ pilot vs. WA pilot vs. CA pilot
- **Why:** AZ produces 60% more non-soft-tissue/month than Seattle; WCTL has established AZ office; capture rate math is comfortable (0.3-0.8% vs WA's 0.8-2.2%)
- **By:** Davis + Robert
- **Source:** `../April_10_Meeting_Notes.md`

### 2026-04-13 — Pricing + ROAS model locked

- **Decided:** $475/lead non-soft-tissue (vs. $315 standard blended) → 21 leads at $9,975 contract
- **Why:** Non-soft-tissue audience is 30-40% of all injury crashes (smaller targetable pool, higher CPMs); funnel filters aggressively at injury severity step (more disqualified clicks); but lead value to WCTL is 2-3× higher (every lead is takeable). At $475 the firm pays 1.6% of expected attorney fee vs 2.1-2.6% for blended.
- **By:** Davis + Sasha (pricing model)
- **Source:** `../WCTL_Arizona_Pilot_Proposal.md`

### 2026-04-16 — Service Agreement signed

- **Decided:** Contract executed; DUI cases excluded per §1.3
- **Why:** Robert wanted to scope the pilot tight before scaling
- **By:** Davis (Second Chair) + Robert (WCTL)
- **Source:** `../WCTL_Service_Agreement.md`

### 2026-04-21 — Audience research rigor pass

- **Decided:** Calibrated funnel rates (quiz start 60%, completion 40%, NST pass 15%) — supersedes earlier over-optimistic rates
- **Why:** Original rates compounded to ~150 leads which is inconsistent with 21-lead contractual target. Back-solved to realistic rates that compound correctly.
- **By:** Julian + Jon Steel (rigor session)
- **Source:** `../Audience/00_Evidence_Register.md` §6.x

### 2026-04-22 — Single-ad-set architecture (Option C) locked

- **Decided:** Pivot from 2-ad-set Modified Option B to 1-ad-set Option C with all 6 creatives running together
- **Why:** At $7,750 budget, single ad set produces ~200 weekly completions (4× learning threshold); split architecture would put motorcycle ad set at ~50 (threshold). Motorcycle creative's 5/5 identity-based self-qualification protects reach without budget lock.
- **By:** Simon Croft + Depesh (architecture decision)
- **Hot-swap contingency:** If motorcycle <15% impression share at Day 7, split to two-ad-set
- **Source:** `../Audience/03_Audience_Sizing_By_Case_Type.md` §12 + `../Audience/06_Media_Plan_And_Budget_Allocation.md` §2

### 2026-04-22 — Spanish creative deferred to Phase 2

- **Decided:** Drop S3 Spanish pedestrian creative from Phase 1 launch; Phase 2 dedicated Spanish ad set
- **Why:** A single Spanish unit at Phase 1 budget (~$625 share) would starve below signal density. Phase 2 captures Maryvale + South Phx properly with dedicated budget.
- **By:** Simon (allocation discipline)
- **Source:** `../Audience/06_Media_Plan_And_Budget_Allocation.md` architecture-update banner

### 2026-04-22 — Motorcycle persona pivoted Marco → Ty

- **Decided:** Motorcycle protagonist is Ty Rivera (supersport, 32, HVAC tech, Chandler) not Marco (cruiser)
- **Why:** Demographic + visual register fit better; identity-creative resonance higher with younger AZ rider demo
- **By:** Indigo + Giuseppe (production decision)
- **Source:** `../Audience/Deep_Personas/Ty/`

### 2026-04-22 — Multi-channel deferred (TikTok / Reddit / Geofencing → Phase 2)

- **Decided:** Phase 1 is 100% Meta; Phase 2 adds multi-channel
- **Why:** Per Simon's Media_Buying_Systems doctrine: don't starve channels below signal density. $625 TikTok / $375 Reddit / $625 geofencing each fail to clear learning threshold without reallocation mechanism.
- **By:** Simon
- **Source:** `../Audience/06_Media_Plan_And_Budget_Allocation.md` §1

### 2026-04-23 — Designed Overlay System locked (5 patterns)

- **Decided:** Five SC signature patterns codified — Exhibit, Hero Number, Burgundy Rule, Hook Card, Peak Card
- **Why:** Standardize the overlay execution layer across SC ads while preserving the "default zero overlays, earn the place" discipline
- **By:** Production room — Giuseppe + Massimo + Graham Fink + Ed McCabe + Indigo
- **Source:** `../../../02_Visual/Designed_Overlay_System.md`

### 2026-04-23 — Motion-Still format added

- **Decided:** Add Motion-Still as 4th format (later expanded to 6th in catalogue)
- **Why:** Bridges static into Reels surface; cheap iteration on what would otherwise be Reels-suppressed pure-static units
- **By:** Production room
- **Source:** `../Audience/05_Creative_Strategy_And_Ad_Set_Architecture.md`

### 2026-04-25 — Hook Card + Peak Card patterns added

- **Decided:** Add patterns 4-5 to overlay system as CapCut-native text layers built to sit OVER footage (not chroma-keyed compositions)
- **Why:** Sound-off scroll-stop + VO-emphasis problems on Reels needed solutions the existing 3 patterns didn't cover
- **By:** Massimo + Giuseppe
- **Source:** `../../../02_Visual/Designed_Overlay_System.md` §6 patterns 4-5

### 2026-04-28 — Strategy Review with Robert (32 units shipped)

- **Decided:** 32-unit Phase 1 creative package shipped to Robert; format-mix doctrine explained
- **Why:** Pre-launch creative visibility per Service Agreement §7.1; Robert needs to see + approve before any ad runs
- **By:** Davis (presented) + Robert (reviewed)
- **Source:** `../_Research/Strategy_Review_Session_2026-04-28.md`

### 2026-04-30 — Anchor sixth pattern added (split-test)

- **Decided:** Add Pattern 6 "The Anchor" — persistent Fair Case-branded bottom-third overlay; deploy on ~13 of 32 units (Sarah/Laura/Diana cinematic); leave Clean on Ty motorcycle + Diana UGC
- **Why:** Davis intuited the half-listening-scroller comprehension job no other pattern serves. Reconciled with SC's "default zero overlays" by making it the FIRST persistent + FIRST Fair Case-palette pattern, deployed per persona-platform fit (FB-Feed-native, not all-or-nothing).
- **By:** Abracadabra room — Nigel chairs, Julian frames, Depesh reality, Indigo performance lens, Giuseppe production, Massimo overlay-rule gate, Ed McCabe copy hierarchy
- **Source:** `../_Research/Anchor_Session_2026-04-30.md` + `../Creative/Anchor_Template_Spec.md`

### 2026-04-30 — Format mix corrected to AZ addressable market

- **Decided:** Phase 1 format mix shifts to ~40% Anchored coverage (FB-Feed-native units) + render-as-video only for IG Reels surface (FB Feed pure static fine); FB-vs-IG estimate corrected from generic 60-70% IG to AZ-specific ~45-55% / ~45-55%
- **Why:** Davis's correction: "the budget should fit the addressable market, not generic Meta strategy." AZ non-soft-tissue PI demo is FB-heavy (30-54 commuter, 80% FB / 58% daily); Hispanic 32% Phoenix lower-income FB+Spanish-FB; motorcycle + younger UGC IG-leaning.
- **By:** Davis (correction) + room synthesis
- **Source:** `../_Research/Anchor_Session_2026-04-30.md` + `../Audience/06_Media_Plan_And_Budget_Allocation.md` §6.6

### 2026-04-30 — AI crash footage clarified as in-bounds for AZ

- **Decided:** AI-generated crash footage IS permissible in the AZ pilot creative when it meets SC's craft bar (high-quality, indistinguishable from real footage, non-shock-factor)
- **Why:** AZ doesn't have SB-37. The "no AI crash footage slop" rule that holds in CA was carried forward into the Campaign Book by mistake; Davis flagged the over-broad refusal. The actual SC discipline is against AI SLOP (waxy/HDR/uncanny) and against SHOCK FACTOR (fear-based scare tactics) — not against AI-rendered crash imagery per se. Crash sequences that look real and serve narrative purpose are in-bounds for AZ.
- **Action items:** Future CA / multi-state Phase 2 will need state-by-state review of crash-imagery rules
- **By:** Davis (correction)
- **Source:** Campaign Book session 2026-04-30 follow-up

### 2026-04-30 — Campaign Book hub built

- **Decided:** Build agency-style campaign book at `../Campaign_Book/` with 5 navigable briefs + index
- **Why:** Davis needs central hub to visualize whole pilot, shift levers, walk Robert through. Strategic substance exists across 7+ docs — synthesis layer was missing.
- **By:** Account team — Nigel synthesis, Julian Comms Plan, Simon Media Mix, Indigo Creative Slate
- **Source:** This file + sibling 00-04 briefs + `../_Research/Campaign_Book_Build_Session_2026-04-30.md`

---

## Open Items / Pending Decisions

| Item | Owner | Decision needed by |
|---|---|---|
| Higgsfield mockup direction pick (5 directions) | Davis | Mon 2026-05-04 AM |
| Anchor variant copy assignments per unit (table proposed in `Anchor_Template_Spec.md`) | Davis | Tue 2026-05-05 |
| M2-V3 counsel review resolution | Davis + Saul | Before Wed launch |
| Robert framing — "split-test variable" vs "two creative versions" | Davis | Wed 2026-05-06 morning |
| Robert sign-off on Phase 1 launch | Robert | Wed 2026-05-06 |
| Phase 2 Spanish creative scope (if Anchor validates) | Davis + Sasha | Week 4 |
| Phase 2 multi-channel scope (TikTok / YouTube / geofencing) | Davis + Sasha | Week 4 |

---

## Decisions That Won't Change Without Strong Evidence

- **Single-ad-set architecture** (signal density at this budget)
- **Optimization event = LPV** (deeper events would starve learning at $7,750)
- **Special Ad Category compliance** (legal requirement, no toggle)
- **TCPA 1-to-1 consent naming WCTL** (compliance + brand commitment)
- **No settlement-promise hero claims / no fake awards / no shock-factor scare tactics / no AI slop** (SC creative-brief refusal list — AI crash footage IS permissible in AZ where it's high-craft + non-shock-factor; AZ has no SB-37)
- **Email delivery Phase 1 only** (Salesforce integration is Phase 2)
- **Robert pre-launch creative review on every ad** (Service Agreement §7.1)
