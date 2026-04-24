# How Meta Campaigns Optimize — Second Chair Operations Reference

> **Type:** Internal operational reference — foundational to how SC runs campaigns
> **Date:** March 2026
> **Source:** `07_Research/01_Brand_Strategy_Research/02_Category_Deep_Dive/06_Media_Operations/Meta_Algorithm_Learning_And_Audience_Building.md`
> **Why this matters:** This doc explains why there's a 100-lead minimum per Market, how campaigns get better over time, and why creative quality is SC's structural advantage under Special Ad Category restrictions.

---

## 1. The Pixel

The Meta Pixel is a piece of code installed on SC's website (Get A Fair Case). It's not tied to any single campaign — it's persistent across everything. It tracks every visitor: what they do, how long they stay, whether they fill out a form, what device they're on, what time of day, where they are.

When someone converts (fills out the form), the Pixel records their behavioral fingerprint. This data accumulates in the ad account over time, regardless of which campaign or ad set drove the visit.

**Key points:**
- Pixel data does NOT reset when you start a new campaign
- It belongs to the ad account, not to any individual campaign or ad set
- A new campaign in month 3 has access to everything the Pixel learned in months 1 and 2
- This is why the second Market you launch performs better than the first — there's already data in the account

---

## 2. Special Ad Category — What It Means for SC

PI legal advertising runs under Meta's Special Ad Category. This restricts the targeting toolkit:

| Tool | Available? |
|------|-----------|
| Geographic targeting (Market/city) | Yes |
| Creative-based self-selection | Yes — this is SC's primary targeting method |
| Retargeting (website visitors, video viewers, form openers) | Yes |
| Customer list retargeting | Yes |
| CAPI / Pixel conversion optimization | Yes |
| Demographic targeting (age, gender, income) | No |
| Interest/behavioral targeting | No |
| Lookalike audiences | No |

**What this means:** Creative is the ONLY way to reach specific people within a Market. The ad that stops the right person mid-scroll while being invisible to everyone else is built through craft, not through platform filters. This is why SC's creative capability is the entire competitive advantage.

---

## 3. Algorithm Learning

When you launch an **ad set**, Meta's algorithm starts learning for that specific ad set. It doesn't yet know who to show the ads to, so it experiments — testing different people, times of day, placements — and watching what happens.

Even under SAC restrictions, the algorithm still learns from conversion events. When someone fills out the form, Meta records their behavioral fingerprint and finds more people on the platform whose aggregate behavior looks similar. It just can't expand into a separate lookalike audience — the optimization happens within the ad set's delivery model.

**The 50-event threshold:**
Meta's ideal is ~50 conversion events (form fills) per ad set per week to exit learning phase in about 2 weeks. At SC's realistic delivery rate of 1-3 leads/day per Market:

| Events/Week | Learning Phase Duration | Reality for SC |
|-------------|------------------------|----------------|
| 50+ | ~2 weeks | Only in high-volume Tier 1 Markets (LA, NYC) |
| 25-49 | 3-4 weeks | Strong performance Markets |
| 10-24 | 4-6 weeks | Most SC Markets will live here. Still works, just takes longer. |
| Under 10 | May never fully exit | Too thin. This is why very small lead packages don't work. |

**What resets learning (avoid during first 2-3 weeks):**
- Creating a new ad set
- Changing budget by more than ~20%
- Changing audience targeting
- Pausing and restarting

**What does NOT reset learning:**
- Adding a new creative (ad) to an existing ad set
- Minor creative swaps

**Key point:** New ad sets aren't starting from zero if there's existing Pixel data in the account. A new ad set in month 3 learns faster than one on day 1.

---

## 4. Campaign Structure for SC's Volume

At 1-3 leads/day per Market, SC cannot support multiple ad sets running simultaneously in the same Market. Each ad set needs conversion events to learn, and splitting a thin volume across 2-3 ad sets means none of them get enough data.

**The right structure at launch:**

```
Campaign: [Market Name]
└── Ad Set 1: Primary (100% of budget, full Market geography, broad audience)
    ├── Ad 1: Narrative storytelling (e.g., crash → family → action)
    ├── Ad 2: Same narrative, different opening hook
    ├── Ad 3: Educational angle (e.g., "68% accept the first offer")
    ├── Ad 4: Direct opportunity (e.g., "cases settled for millions")
    └── Ad 5: Different emotional register or format (still image vs. video)
```

- **One ad set.** All budget, all conversion events feeding one learning model.
- **3-5 ads (creatives) inside that ad set.** Different angles, hooks, formats. Meta rotates and tests them all simultaneously, shifting delivery to the winners.
- **Full Market geographic targeting.** Broad. The creative does the audience filtering, not the targeting settings.
- **Second ad set (Spanish, retargeting) launches AFTER** the primary ad set exits learning and there are 100+ leads generating enough site traffic for retargeting.

**Why 1 ad set, not 2-3:**
If SC generates 15 leads/week in a Market:
- 1 ad set: 15 events/week → exits learning in ~3-4 weeks
- 2 ad sets: ~7-8 each/week → exits learning in ~5-6 weeks
- 3 ad sets: ~5 each/week → might never exit learning

Concentrate the signal. Go deep with one ad set, then expand.

---

## 5. Creative IS the Targeting

This is the most important concept in SC's campaign model — and under SAC, it's the only way.

SC targets the entire Market with broad geographic targeting and uses **specific creative to self-select the right people.**

**How it works:**

The ad set targets everyone in the Denver Market. But:
- Ad 1 is a Spanish-language narrative with a Hispanic working-class family on the I-25 corridor → Hispanic commuters stop scrolling, everyone else keeps going
- Ad 2 is an English educational piece about insurance lowball offers → people dealing with insurance stop, everyone else keeps going
- Ad 3 is a direct opportunity play about settlement amounts → people who are action-ready stop

The person who stops, clicks, and fills out the form was **self-selected by the creative.** Meta watches who responded to which ad and builds the audience model from that actual behavior — not from assumptions about who should see what.

**Why this matters under SAC:**
Without demographic or interest targeting, the creative IS the only precision instrument. The more specific the creative, the more homogeneous the converters, the more precise Meta's model becomes within the ad set. Each specific creative generates its own audience signal. Over time, the algorithm gets smarter at finding the right people — it just does this within the ad set's delivery, not through a separate lookalike tool.

**What this means for campaign research:**
The deep market research SC does (archetypes, demographics, corridors, community patterns) informs the **creative**, not the audience filters. Research determines what ads to build. The ads do the targeting.

---

## 6. Retargeting Under SAC

While lookalike audiences are not available under SAC, retargeting IS. This becomes valuable after enough campaign data accumulates.

**What's available:**
- **Website visitor retargeting** — people who visited the landing page but didn't convert (need ~1,000 unique visitors for meaningful retargeting)
- **Video viewer retargeting** — people who watched 50%+ of a video ad (showed intent)
- **Lead form opener retargeting** — people who started the form but didn't submit (highest-intent retargeting pool)
- **Customer list retargeting** — upload past leads for re-engagement

**When to launch a retargeting ad set:**
After the primary ad set has been running for 3-4+ weeks and generated enough site traffic (~1,000 unique visitors). Run retargeting at ~10-15% of total budget. These are people who already showed interest — conversion rates are significantly higher than cold traffic.

---

## 7. CAPI (Conversions API)

Meta's Conversions API is a server-to-server data connection between SC's backend and Meta's ad system. Unlike the browser-based Pixel (degraded by iOS 14), CAPI sends conversion events directly from SC's server — bypassing browser-level tracking restrictions.

**Why it matters:**
- The Pixel alone, post-iOS 14, may only capture 60-70% of conversions
- CAPI fills the gap, giving Meta complete conversion data
- Without CAPI, the algorithm learns from incomplete data and underperforms
- This is especially critical under SAC where you can't compensate with targeting tools

**The competitive moat — signed case optimization:**
Most vendors optimize toward form fills. SC can pass signed case data back to Meta via CAPI. This tells Meta not "find people who fill out forms" but "find people who fill out forms AND whose cases get signed." The algorithm optimizes within the ad set toward higher-quality converters, even without lookalike audiences.

---

## 8. Why 100 Leads Per Market Is the Minimum First Package

| Reason | Detail |
|--------|--------|
| **Algorithm learning** | At SC's volume (10-20 events/week), ad sets need 3-6 weeks and ~50-100 events to exit learning. A 100-lead package provides enough runway. |
| **Retargeting threshold** | Need ~1,000 site visitors (roughly maps to 100+ leads at typical visit-to-lead ratios) before retargeting ad sets become viable. |
| **Data validity** | At 100 leads with a 10% sign rate, that's ~10 signed cases — enough to draw real conclusions about quality and CPSC. At 50, it's ~5. Too thin. |
| **Fair evaluation** | The first ~30 leads come during learning phase (worst performance). At 50 total, the client evaluates mostly on pre-optimization data. At 100, they see learning + stabilization + early optimization — the full arc. |
| **Creative research** | The first 100 leads tell you which creatives work, which audience segments respond, and what the market actually looks like — not what you assumed. This data drives every renewal. |

**Renewals at 50+** work because campaigns are already optimized. Every subsequent lead benefits from the first 100.

---

## 9. The Optimization Cycle

**First package (100 leads) = Research Phase**
- Wide net. Full Market. Multiple creative angles inside one ad set.
- Learn which creatives convert, which segments respond, what the market looks like.
- Algorithm exits learning. Retargeting audiences start building from site traffic.

**First renewal (50+ leads) = Refinement**
- Kill losing creatives. Scale winners. Test new variations against proven performers.
- Launch retargeting ad set if site traffic supports it.
- CPL declining. Lead quality improving.

**Ongoing renewals = Compounding Advantage**
- Pixel data deepening. Algorithm model refining within the ad set.
- CAPI feeding signed case data back to Meta.
- Retargeting pools growing.
- Creative iteration informed by real performance data, not guesses.
- Each renewal is better than the last.

**Cross-Market advantage:**
When SC launches a second Market, the Pixel already has data from the first. New campaigns learn faster. The more Markets SC operates in, the faster each new one optimizes.

---

*Second Chair — March 2026*
*This doc is referenced by: Starter_Options.md, Davis_Pitch_Materials.md, Discovery_Call_Script.md, AD_CREATION_WORKFLOW.md, B2C_Campaign_Brief.md, Colorado_Targeting.md*
