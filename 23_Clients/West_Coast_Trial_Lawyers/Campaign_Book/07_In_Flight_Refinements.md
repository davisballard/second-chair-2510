# In-Flight Refinements (Tier 1) — Apply Friday→Tuesday

**Authored by:** Depesh Mandalia + Indigo Sato + Hegarty (register call)
**Status:** Locked 2026-05-01 PM after lead-gen research synthesis session
**Source-of-truth session log:** `../_Sessions/2026-05-01_Lead_Gen_Research_Synthesis.md`
**Companion doc:** `08_Phase_2_Pivots.md` (architectural changes deferred to Phase 2)
**Variant slate authority:** `06_Variant_Slate_Plan.md` is unchanged; this doc layers on top

---

## How to use this doc

These are creative-by-creative changes Davis applies during the Friday→Tuesday production cycle. **No new builds; no scope creep.** Every change either swaps inside an existing build slot, drops production overhead, or is configured at upload time in Meta Ads Manager. Net production hours = neutral-to-positive.

Read this alongside `06_Variant_Slate_Plan.md` Friday morning. Where they conflict, this doc supersedes (it's newer).

---

## 1. CTA Meta button — A/B test 'Get Quote' + 'Free Quote' against 'Learn More'

**Change:** When uploading creatives to Meta Ads Manager Tuesday, configure three CTA button variants across the ad set:
- **'Get Quote'** (primary test — research consensus says action-y CTAs beat 'Learn More' when offer is specific)
- **'Free Quote'** (PI-vertical-aligned — quiz funnel IS functionally a free quote)
- **'Learn More'** (control — Meta's most-used default)

**Why:** 'Get Quote', 'Sign Up', 'Download' beat 'Learn More' in lead-gen benchmarks when the offer is specific. WCTL's quiz produces a case-value estimate within 45 seconds — that's a free quote. Aligns CTA copy with what the user actually receives.

**Production cost:** Zero. In-Ads-Manager configuration only.

**Owner:** Depesh sets up Tuesday before Wednesday launch.

**For J2 swing units specifically:** also test **'Sign Up'** as the CTA — pairs with the Mike Rowe register's action-y voice.

---

## 2. Aspect ratio crops — drop 1:1, build 9:16 + 4:5 only

**Change:** New builds Friday→Tuesday produce **9:16 native + 4:5 crop only.** No 1:1 square.

**Why:** Meta's published data: 4:5 = +1% CTR vs 1:1; 9:16 = +7% CTR vs 1:1. 1:1 is dominated by both alternatives. Building 1:1 crops adds ~30 min/video for negative expected value.

**Affects:** All J1 builds (3 units), all J2 builds (3 units), Diana cinematic V1, Diana UGC swing, Sarah V1, Laura V1, J1-V2-TalkingHead. Total ~10 fresh units × 30 min saved = **~5 hours freed.**

**Already-shipped units:** keep their existing 1:1 crops. Don't go back and rebuild.

**Owner:** Davis applies during generation Fri-Mon.

---

## 3. Sound-off discipline — every kinetic CTA resolve must read sound-off

**Change:** Every video built this cycle must have its closing CTA / kinetic resolve readable with sound completely off. Karaoke captions throughout (already specified) carry the VO content.

**Why:** Meta data: 85% of FB video views are sound-off. 40% of ads "fail to communicate" without sound. Captions = +12% view time (Meta own research).

**Application detail:**
- **J1 cinematic units:** the closing CTA "Free case review →" or whatever the kinetic resolve is must be on-screen text, not VO-only
- **J2 Mike Rowe units:** same; doc-cam grammar with karaoke captions throughout
- **J1-V2-TalkingHead:** Jason's spoken hook IS the karaoke caption — verbatim with bold karaoke style throughout

**Production cost:** Zero new — already the plan per `feedback_ad_post_workflow.md`. Just affirm during CapCut pass.

**Owner:** Davis during CapCut finalization of each unit.

---

## 4. **J1-V2 swap: drop financial-squeeze cinematic → build J1-V2-TalkingHead** (BIGGEST CHANGE)

**Change:** Replace J1-V2 in the build sequence:
- **OUT:** J1-V2 cinematic-documentary "Five months out of work. The bills don't slow down because you do." (financial-squeeze)
- **IN:** J1-V2-TalkingHead — Jason direct-to-camera, plain-spoken, parasocial register

### J1-V2-TalkingHead spec

| Field | Spec |
|---|---|
| Format | Talking-head video, direct-to-camera |
| Length | 20-25s |
| Aspect | 9:16 native + 4:5 crop |
| Setting | Jason's kitchen table OR workshop bench (Davis picks the one with better Higgsfield reference output) |
| Wardrobe | Work shirt, civvies — same as J1 cinematic continuity |
| Camera | Static or barely-handheld eye-level mid-shot, no movement, plain register |
| VO | ElevenLabs Bill voice (weathered, blue-collar profile) — Jason speaking to camera |
| Captions | Bold karaoke caption verbatim with VO |
| Anchor cohort | Clean (no panel — talking-head needs face to fill frame) |

**Hook (locked by Hegarty in the room):**
> *"Twenty-two years on jobsites. I never thought I'd be the guy who needed a lawyer."*

**Beat structure:**
- 0-3s: Hook delivered direct-to-camera, eye contact, slight head tilt
- 3-12s: Plain-spoken middle — *"They told me to take thirty-eight grand and walk away. I have two kids. I work concrete. Five months without a paycheck doesn't go away because the offer's clean."*
- 12-18s: Pivot — *"My lawyer at West Coast Trial Lawyers said no. He said let me see if it's fair first."*
- 18-22s: CTA resolve — kinetic text *"See what your case is actually worth →"* over Jason's stillness
- 22-25s: Logo / Free Case Review tag

**Why the swap:**
- Original J1-V2 hook ("Five months out of work...") thematically overlapped J1-V1 lowball-anchor frame. Diminishing return on a third loss-aversion variant.
- Talking-head is the empirical PI winner per Morgan & Morgan / Witherite / Sweet James. Literature is thin but practitioner consensus is clear.
- Tests cinematic-doc vs talking-head register on the SAME persona (J1-Primary cinematic vs J1-V2-TalkingHead) — clean A/B inside the slate.
- Per Shotton's parasocial framing: if talking-head wins, Phase 2 commits to recurring persona. Phase 1 needs the data point.

**Production slot:** Saturday 5/3 alongside J2 outputs (same pipeline). If pace tight, bumps to Sunday 5/4 — still inside envelope.

**Production cost:** No increase — same Higgsfield + Kling + ElevenLabs + CapCut pipeline as cinematic units. Different camera grammar only.

**Owner:** Davis builds Saturday (or Sunday). Indigo locks final hook copy with Davis Friday morning before generation.

---

## 5. OPTIONAL — Text-only swing in Sunday slot if pace allows

**Change:** If Friday + Saturday production stays on pace, add 1 text-only static ad to Sunday slot.

**Why:** Motion 2026 surprise finding — text-only ads at 11.6% hit rate vs 6.97% high-production video, drawn from $1.3B Meta spend / 550K ads. Counterintuitive but high-confidence data.

**Spec options** (Davis picks):

**Option A — Authority figure:**
- 1080×1350 (4:5) static
- Plain background (cream or charcoal) with single bold number
- Tiempos Bold 200pt: **"$1.7B"**
- Inter Medium 28pt below: "Recovered for accident victims since 2009. Free case review."
- Fair Case torch + WCTL attribution at bottom

**Option B — Contrarian PI hook:**
- 1080×1350 (4:5) static
- Plain background
- Tiempos Medium 56pt:
> "Most personal injury ads look like ads.
>
> This isn't one."
- Inter Medium 24pt below: "Free case review in 45 seconds. AZ residents only."
- Fair Case torch at bottom

**Production cost:** ~30-60 minutes in ChatGPT Image 2 → CapCut. ~$2-5.

**If skip:** No problem. Sunday slot is Diana cinematic V1 + Diana UGC swing + (optional) M3 confirm. Text-only goes in Phase 2 swap-pool inventory.

**Owner:** Davis decides Sunday morning whether pace allows.

---

## 6. Day 7 read calibration — 37% hook-rate fatigue is normal

**Change:** Don't pause hooks on hook-rate decline alone. Refresh hook copy on the same footage and continue.

**Why:** Research finding — hook rate fatigues 37% on average after 7 days for the same hook. A hook that launched at 30% hook rate and is at 19% by Day 7 isn't *failing* — it's *fatigued*. Pausing is overreaction.

**Application:**
- **If hook rate drops below 25% by Day 5-7 BUT the unit launched above 30%:** that's fatigue. Refresh hook copy (same footage, new opening line / kinetic caption text), reupload, keep running.
- **If hook rate below 20% from launch with no recovery by Day 7:** that's failure. Pause.
- **If hook rate below 15% from launch:** dead on arrival. Pause Day 3.

**Owner:** Depesh applies in Day 7 monitoring report.

---

## 7. Day 5 Anchor gate — compare FB Feed only, not blended

**Change:** When evaluating the Day 5 Anchor hook-rate gate (per `06_Variant_Slate_Plan.md`), compare:
- Anchor unit FB Feed delivery hook rate
- Matched Clean unit FB Feed delivery hook rate (filter to FB Feed only — drop IG Reels delivery from the comparison)

**Why:** Reels run 5-10pp lower hook rate than Feed at baseline. If Clean cinematic units are running both Feed and Reels, their *blended* hook rate is dragged down by the Reels mix. Comparing Anchor (FB-Feed-only by structural physics) to Clean's blended number gives Anchor an artificial advantage. Apples-to-apples requires placement-segmenting.

**Application:** in Ads Manager, segment hook-rate report by placement, compare FB Feed Anchor vs FB Feed Clean cinematic on the same source footage.

**Owner:** Depesh / Davis at Day 5 read.

---

## Net production-hour impact

| Change | Hours impact |
|---|---|
| 1:1 crop drop | **+5 hours freed** |
| J1-V2 swap (cinematic → talking-head) | Neutral (same pipeline, same slot) |
| Optional text-only swing | -1 to -2 hours if Davis takes it |
| All other changes (CTA, sound-off, calibrations) | Zero |
| **Net:** | **+3 to +5 hours freed** vs original plan |

That headroom absorbs Saturday-iteration if Saul kicks J2 outputs back, OR allows a Phase 2 swap-pool early-start (J2-B Trade Tutorial first frames) if Davis wants.

## Friday→Tuesday production order (revised, this version supersedes `06_Variant_Slate_Plan.md`)

| Day | Build | Hours est. |
|---|---|---|
| **Fri 5/2** | J1 ×3 (J1-Primary + J1-V1 + J1-V2-TalkingHead) | 5-7h (talking-head ~same time as cinematic; 1:1 crop drop saves ~30m × 3) |
| **Sat 5/3** | J2 Mike Rowe ×3 + Saul fence review EOD | 5-7h |
| **Sun 5/4** | Diana cinematic V1 + Diana UGC swing + (optional) text-only swing + (optional) M3 confirm | 4-6h |
| **Mon 5/5** | Sarah V1 + Laura V1 (fresh) + 4 Anchor composite variants (FB Feed only) | 4h fresh + 3h Anchor + ~1h CTA setup prep = ~8h |
| **Tue 5/6** | M2-V3 counsel + J2 fence finalized + Robert sign-off + Meta upload + CTA A/B configuration | All-day buffer |
| **Wed 5/7** | LAUNCH | — |

## Pre-launch checklist additions (in addition to existing `06_Variant_Slate_Plan.md` verification)

Tuesday EOD before launch:
- [ ] CTA button A/B configured: 'Get Quote' + 'Free Quote' + 'Learn More' across ad set
- [ ] J1-V2-TalkingHead built and Saul-reviewed
- [ ] All new units verify 9:16 + 4:5 crops (no 1:1)
- [ ] Sound-off readability spot-checked on every video (3-second glance test)
- [ ] Day 5 / Day 7 read framework calibrations communicated to whoever monitors

## What this doc does NOT do

- Does not change the 8-hook ceiling or TAM-weighted allocation (`06_Variant_Slate_Plan.md` authoritative)
- Does not change Anchor split-test structure (`06_Variant_Slate_Plan.md` authoritative; this doc only refines the comparison method)
- Does not add new personas or hooks
- Does not restructure ad set architecture (still single Advantage+ ad set + retargeting)
- Does not change Phase 1 budget or pacing
