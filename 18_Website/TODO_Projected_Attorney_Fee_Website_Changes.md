# TODO — 2ndchair.net Website Changes: Projected Attorney Fee Integration

> **Type:** Website implementation TODO (not for immediate action)
> **Created:** April 2026
> **Priority:** Medium — the WCTL pitch materials lead with this framing now; the website should match
> **Owner:** Davis (copy) + Alex (dashboard component)
> **Canonical source:** `01_Identity/Projected_Attorney_Fee_Model.md`
> **Related:** `ROUNDTABLE_AUDIT_2026-03-30.md` (which already flagged CPSC-primary as wrong)

---

## Why This Exists

The canonical metric framework has shifted. Second Chair now leads with **Projected Attorney Fee → Projected ROAS** as the day-one measurement, with CPSC tracking alongside as a confirmation metric. This is the position that the sales team is taking to clients (WCTL call, 2026-04-10, and forward). The website needs to catch up.

The March 30, 2026 roundtable audit already flagged CPSC-primary as the wrong framing (Problem #6 in that doc). This TODO picks up where that audit left off and adds the specific Projected Attorney Fee layer that the roundtable didn't know about yet.

---

## What Currently Lives On 2ndchair.net (Verbatim From The Site)

- **"Return on ad spend is your headline KPI. Cost per signed case tracks alongside it"** — this is the current positioning, and it's close but not quite what the new model says.
- Dashboard example: "ROAS / 4.8× ↑9% / CPSC / $2,605 ↓6%" — shows ROAS first, CPSC second. Good direction but doesn't show Projected Attorney Fee or Projected ROAS explicitly.
- "Cost per signed case sits below it. As your firm reports signed cases, it takes shape and compounds." — this is accurate but implies CPSC is the main number that firms will care about, which undersells the day-one story.
- "Two scores (Conversion Score + Case Value Score) tell you how to prioritize your intake queue" — this is already halfway there but the "Case Value Score" is not currently presented as a dollar-denominated projection.
- "Fit Score (0–100) / Quality Score Letter Grade A / B / C / D" — the platform infrastructure exists; the dashboard UI just needs to surface the dollar layer on top.

---

## What Needs To Change

### 1. The Intelligence Section — Reframe as Projected Attorney Fee

**Current position:** ROAS as headline KPI, CPSC tracks alongside.

**New position:** Projected Attorney Fee per lead → Projected ROAS as headline (visible day one), Sign Rate validation as the second layer, Actual ROAS / CPSC as the third layer.

**Specific copy changes needed:**

- Replace the current "Cost per signed case. Visible by default." messaging with something like: *"Every lead arrives with a Projected Attorney Fee attached — computed from injury type, case type, treatment status, fault position, and recency. Aggregate the cohort, divide by spend, and you see Projected ROAS on day one. Before any case has signed."*
- Replace "We report on your cost-per-signed-case — not CPL" with: *"We report Projected Attorney Fee per lead — not CPL, not just CPSC. Projected value reflects the case-value mix in ways both of those metrics hide."*
- Add a dashboard mockup row: **"Projected Attorney Fee per Lead: $2,340 avg · Projected ROAS: 6.5× · Sign Rate: 18% · CPSC: $2,005"** — with Projected ROAS as the largest visible number.
- Keep the Binet/Field "efficiency vs. effectiveness" argument — it still works, just with Projected ROAS as the effectiveness metric instead of Actual ROAS.

### 2. The Intelligence Dashboard Mockup

The dashboard mockup currently shows ROAS / CPSC / Leads / Sign %. The new mockup should show:

| Primary Display | Secondary Display |
|---|---|
| **Projected ROAS: 6.5× ↑4%** | Leads: 182/200 |
| **Projected Attorney Fee Avg: $2,340** | Sign Rate: 18% (validates projection) |
| | CPSC: $2,005 (alongside) |

The visual hierarchy needs to put Projected ROAS at the top, largest. Everything else is supporting.

### 3. The "How We Measure" Section (new section, or expand existing)

Build out a new section that walks through the Projected Attorney Fee model at a scannable level:

- **Step 1:** Every lead gets a Fit Score from our scoring engine
- **Step 2:** Fit Score × sign probability × median attorney fee by case type = Projected Attorney Fee per Lead
- **Step 3:** Aggregate across the cohort / spend = Projected ROAS
- **Step 4:** As sign rate data accumulates, the projection validates or tunes
- **Step 5:** If firm can share aggregate attribution (long-term), Projected ROAS refines into Actual ROAS

Include a link to a public-facing version of the lookup tables (or at least the base expected-fee table) — this is a trust signal. Nothing about the math is hidden.

### 4. Platform / Dashboard Implementation Notes (for Alex)

The platform already has the Fit Score engine running. What's missing is the dollar-denominated projection layer on top. The minimum shippable version:

- Add a `projected_attorney_fee` field to the lead schema
- Compute it server-side as: `base_fee[case_type] × sign_probability[grade]`
- Surface it in the firm portal as a per-lead display
- Aggregate it into a "Projected Cohort Fees" rollup on the dashboard
- Divide by spend to show "Projected ROAS" as the headline metric on the dashboard

The lookup tables for `base_fee` and `sign_probability` are in `01_Identity/Projected_Attorney_Fee_Model.md`. They should be database-stored (not hardcoded) so they can be adjusted per-market and per-firm over time.

**Timing:** This should be shippable before the first client onboards. We're pitching the projected dashboard in sales calls as if it exists, so it needs to exist by the time the first cohort delivers.

### 5. Homepage Hero — Optional Add

The current hero is "The leads other vendors can't produce" with credential proof. The hero doesn't need to change structurally, but a supporting line could be added that plants the Projected Attorney Fee differentiator at first glance:

> *"The only vendor that projects per-lead value in dollars on day one."*

This is optional — the hero is working. If added, it's a subtext line below the H1, not a replacement.

### 6. Sales-Page Copy — Pitch Language Alignment

The following copy blocks from the canonical pitch should appear in the B2B sales flow:

**Day-One Anchor:**
> *"Every lead we deliver has a Projected Attorney Fee attached to it. At our California rates, we're typically projecting $1,800-$2,800 of expected attorney fee per lead — a 5-to-8× projected ROAS visible from day one, before anyone has signed anything."*

**Differentiator:**
> *"No vendor in this space projects per-lead value in dollars. They report CPL (vanity) or CPSC 6-12 months after the fact (lagging). Projected Attorney Fee gives firms a real read on the value of the pipeline on day one."*

**CPSC-Is-Misleading:**
> *"CPSC averages every signed case as if they're equivalent. A firm that signs ten soft-tissue cases shows the same CPSC as a firm that signs nine soft-tissue plus one major trucking case — even though the revenue is completely different. Projected Attorney Fee reflects the case-value mix."*

**Confidentiality-Honest:**
> *"We know most PI settlements now come with NDAs. The whole reason we built Projected Attorney Fee as the day-one metric is that it doesn't depend on the firm sharing case outcome data. It lives on our side of the relationship. The measurement floor is solid from day one regardless of what the firm can or cannot share."*

---

## What NOT To Change

- **Don't remove CPSC from the site.** It still tracks alongside as a confirmation metric. Firms will still look for it. It just needs to be repositioned as secondary, not primary.
- **Don't remove ROAS either.** Actual ROAS is still the long-term trust metric. It still lives on the site. Projected ROAS is the new day-one layer on top.
- **Don't touch the "Honestly Won" philosophy.** Still accurate. Still the core argument. The metrics layer is supporting infrastructure, not a replacement for the philosophical positioning.
- **Don't touch the Four Phases section.** Still good. No metric changes needed there.
- **Don't touch the Compliance pipeline.** Unchanged.

---

## Implementation Checklist

### Copy Changes
- [ ] Intelligence section — reframe headline copy around Projected Attorney Fee → Projected ROAS
- [ ] Dashboard mockup — put Projected ROAS as the primary number, add Projected Attorney Fee line
- [ ] Add or expand "How We Measure" section with the 5-step model walkthrough
- [ ] Add the day-one anchor / differentiator / CPSC-is-misleading / confidentiality-honest copy blocks into relevant sales-page sections
- [ ] Review all existing copy for "cost per signed case is the number that matters" style overclaims and soften

### Dashboard / Platform Changes (for Alex)
- [ ] Add `projected_attorney_fee` field to lead schema
- [ ] Add `base_fee` and `sign_probability` database lookup tables (from `Projected_Attorney_Fee_Model.md`)
- [ ] Compute projected fee per lead on scoring completion
- [ ] Surface projected fee per lead in firm portal UI
- [ ] Add Projected Cohort Fees rollup on dashboard
- [ ] Add Projected ROAS as the headline metric on dashboard
- [ ] Allow projection weights to be tuned per-firm as sign rate data accumulates

### QA
- [ ] Cross-check all pitch language against `Projected_Attorney_Fee_Model.md` for consistency
- [ ] Cross-check sales page copy against `23_Clients/West_Coast_Trial_Lawyers/CALL_CHEATSHEET.md` — they should be aligned
- [ ] Confirm the website and the WCTL call materials are telling the same metric story
- [ ] Update `18_Website/ROUNDTABLE_AUDIT_2026-03-30.md` — add a note that Problem #6 has been addressed via Projected Attorney Fee reframe

---

## When To Do This

**Not urgent for the April 10 WCTL call.** The call materials lead with Projected Attorney Fee on their own; the website can lag for a few weeks without breaking anything.

**Urgent before the first WCTL cohort delivers.** Once WCTL (or any other client) is in onboarding and starts looking at the dashboard, Projected Attorney Fee needs to be surfaced there natively. Otherwise the pitch-vs-reality gap becomes visible.

**Suggested timeline:**
- Copy changes on the website: within 2 weeks (April 10 + 2 weeks = April 24)
- Dashboard implementation: before first cohort delivers (which could be as early as 4-6 weeks after contract signing)

---

## Related Files

- `01_Identity/Projected_Attorney_Fee_Model.md` — canonical source of truth for the model
- `01_Identity/BRAND_MASTER.md` — updated primary metric reference
- `01_Identity/SERVICE_PERSONAL_INJURY.md` — updated service description
- `19_Platform/PLATFORM_INTELLIGENCE.md` — platform Fit Score engine
- `18_Website/ROUNDTABLE_AUDIT_2026-03-30.md` — previous website audit (Problem #6 is now addressed by this TODO)
- `23_Clients/West_Coast_Trial_Lawyers/CALL_CHEATSHEET.md` — the sales call material that currently leads with this framing
- `23_Clients/West_Coast_Trial_Lawyers/In_Depth/Davis_Pitch_Materials.md` Section 9 — the full pitch language

---

*Second Chair — Website TODO: Projected Attorney Fee Integration — April 2026*
