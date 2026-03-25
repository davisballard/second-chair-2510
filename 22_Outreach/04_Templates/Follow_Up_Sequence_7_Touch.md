# 7-Touch Email Sequence

> **Lead:** Ed McCabe (copy), Roma (structure)
> **Source:** Validated against 00_Research_Findings.md + B2B Sales Language Guide
> **Updated:** March 24, 2026
> **Note:** Adapt merge fields per tier. Tier 1 gets fully personalized versions of these. Tier 2-3 use as-is with merge fields.

---

## Sequence Overview

| Touch | Day | Type | Subject Line |
|-------|-----|------|-------------|
| 1 | Day 0 (Tue) | Credentials + honestly won pitch | PI leads for {{firmName}} |
| 2 | Day 3 (Fri) | CPSC reframe | Re: PI leads for {{firmName}} |
| 3 | Day 7 (Tue) | "Show you the advertising" | quick question, {{firstName}} |
| 4 | Day 10 (Fri) | Pain point — compliance angle | Re: quick question, {{firstName}} |
| 5 | Day 17 (Fri) | Different angle — intake quality | thought you'd find this relevant |
| 6 | Day 22 (Wed) | Breakup | closing the loop |

**Auto-pause entire sequence on any reply.**

---

## Touch 1 — Day 0: Credentials + Honestly Won Pitch

**Subject:** PI leads for {{firmName}}

```
{{firstName}},

I run Second Chair -- a PI lead gen company. Three founders, careers in advertising, product, and media.

Davis Ballard: 18 years of strategy and creative across Disney, Google, Samsung, the NFL, and NBA. Alex DuBelko: built the TradeStation mobile trading platform -- 1M users, 100% FINRA and SEC compliant. He built our product and compliance infrastructure. I spent 15 years in programmatic media for ASOS, Bose, Coach, Diageo, and PepsiCo.

Our belief: the leads you buy should be as honestly won as the cases you take.

Worth 30 minutes to show you what we'd build for {{city}}?

Sasha Zinshtein
Co-Founder, Second Chair
[phone]

Second Chair | [Address]
Reply STOP to opt out.
```

**~105 words. Formula: Credentials → philosophy → CTA.**

---

## Touch 2 — Day 3: CPSC Reframe

**Subject:** Re: PI leads for {{firmName}}

```
{{firstName}} -- quick follow-up.

Most lead vendors sell on cost per lead. We measure on cost per signed case.

The difference matters. A $200 lead that doesn't convert costs more than a $400 lead that signs. We build advertising that produces claimants with accurate expectations -- they convert at intake because the ad told them the truth.

If you know your current cost per signed case, I can show you how we'd compare in {{city}}. If you don't know it, that's actually the more interesting conversation.

Sasha
Second Chair | [Address]
Reply STOP to opt out.
```

**~85 words. Formula: Reframe the metric → imply they might not be tracking the right thing → CTA.**

---

## Touch 3 — Day 7: Show the Advertising

**Subject:** quick question, {{firstName}}

```
{{firstName}},

One thing we do that other lead gen vendors don't: we show you the advertising before you commit to anything.

No pitch deck. No projections. Just the actual creative we'd run in your market.

If the advertising isn't up to your standard, no hard feelings. If it is, we talk about what a pilot looks like.

30 minutes?

Sasha
Second Chair | [Address]
Reply STOP to opt out.
```

**~60 words. Formula: Differentiator (show the ads) → low commitment → CTA. This is Second Chair's proof move.**

---

## Touch 4 — Day 10: Compliance Angle

**Subject:** Re: quick question, {{firstName}}

```
{{firstName}} -- one more thing worth mentioning.

Every lead we deliver comes with full TCPA compliance documentation. TrustedForm certified. Court-admissible consent records. Your firm's name in the consent path, not buried in a list of 15 vendors.

Most lead gen vendors can't tell you how the lead was generated. We can show you the exact ad, the exact landing page, and the exact consent record.

Worth a conversation if compliance matters to your firm.

Sasha
Second Chair | [Address]
Reply STOP to opt out.
```

**~75 words. Formula: Compliance differentiator → contrast with vendors → CTA.**

---

## Touch 5 — Day 17: Intake Quality Angle

**Subject:** thought you'd find this relevant

```
{{firstName}},

The firms we work with keep telling us the same thing: intake is easier when the claimant arrives with accurate expectations.

No promises to walk back. No settlement numbers the ad invented. The claimant knows what they have before the call.

That's what happens when the advertising tells the truth instead of manufacturing panic.

If your intake team is spending time managing expectations down, we should talk.

Sasha
Second Chair | [Address]
Reply STOP to opt out.
```

**~70 words. Formula: Social proof (firms tell us) → name the pain (intake is damage control) → imply the fix → CTA.**

---

## Touch 6 — Day 22: Breakup

**Subject:** closing the loop

```
{{firstName}},

I've reached out a few times and haven't heard back. Totally respect that -- you're busy.

I'll close out my file on this. If the timing changes or you want to see what we'd build for {{city}}, I'm here.

Either way, appreciate your time.

Sasha Zinshtein
Co-Founder, Second Chair
[phone]
2ndchair.net

Second Chair | [Address]
Reply STOP to opt out.
```

**~60 words. Formula: Acknowledge silence → close the loop → leave the door open. Note: this email CAN include the 2ndchair.net link since it's the final touch and breakup emails benefit from giving them a way to self-serve.**

---

## Merge Fields

| Field | Source | Example |
|-------|--------|---------|
| `{{firstName}}` | Managing partner or marketing director | Tommy |
| `{{firmName}}` | Firm name (subject line mainly) | Jacoby & Meyers |
| `{{city}}` | Their primary metro area | Los Angeles |

---

## Notes for Sasha

- **Touches 1-5:** No links. Plain text. No 2ndchair.net URL.
- **Touch 6 (breakup):** Can include 2ndchair.net link and full signature.
- **If someone replies to ANY touch:** Sequence auto-pauses. Handle personally. See Response Handling in EMAIL_OUTREACH_PLAYBOOK.md.
- **Tier 1 whales:** Don't use this sequence as-is. Write personalized versions of each touch using these as structural guides.
- **A/B test subject lines** on Touches 1 and 3 first — they have the highest leverage.
