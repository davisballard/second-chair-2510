# Email Outreach Playbook

> **Lead:** Richard Roma (VP of Sales) + Ed McCabe (copy)
> **Source:** Validated against 00_Research_Findings.md
> **Updated:** March 24, 2026
> **Voice guide:** All copy must align with `13_Brand_Strategy/05_Execution_Briefs/B2B_Sales_Language_Guide.md`

---

## The Rules

These are non-negotiable. Every email Sasha or Davis sends must follow these.

### Format
- **Plain text only.** No HTML, no images, no logos, no formatting. Plain text has 652% lower bounce rate than HTML.
- **No tracking pixels.** Disable open tracking or use a custom tracking domain. Tracking pixels are a major spam trigger.
- **0-1 links maximum.** One link (calendar or website) OR zero links. Never two.
- **50-125 words.** Emails under 80 words get 50% higher reply rates than longer formats.
- **Physical mailing address in every email.** CAN-SPAM requires it. $51,744 penalty per violation. Use virtual office address.
- **Unsubscribe mechanism.** "Reply STOP to opt out" or equivalent. Required by law.

### Sending
- **Max 20 emails per account per day.** This volume looks like normal business email — no reputation risk even on the main domain.
- **Starting from 2ndchair.net** (already warmed). Transition to 2ndchair.co once it's set up and warmed as a backup/scale domain.
- **Send days:** Tuesday, Wednesday, Thursday only.
- **Send time:** 9:00-10:30 AM in recipient's timezone. Instantly handles timezone detection.

### Compliance
- **CAN-SPAM applies to B2B.** There is no business exemption.
- **Honor unsubscribes within 10 business days.** Instantly handles this automatically.
- **Honest subject lines.** Must reflect email content. No bait-and-switch.
- **Real names and real company information.** No spoofed domains or fake names.

### Tracking
- **Turn off open tracking in Instantly.** Open tracking embeds a hidden pixel that converts your plain text email to HTML behind the scenes. Spam filters detect this. At 20 emails/day you need maximum deliverability, not vanity metrics.
- **Turn off click tracking.** Click tracking rewrites your links through a redirect domain that spam filters flag. Since you're not including links in first touches anyway, there's nothing to track.
- **Reply rate is your primary metric.** Replies = conversations = calls = revenue. If you're not getting replies after 2-3 weeks, the problem is targeting, copy, or deliverability — diagnose by testing new subject lines and angles, not by staring at open rates.
- **What you CAN still track without pixels:** Replies, bounces, unsubscribes. These are the metrics that matter.
- **If you ever want open/click tracking later:** Set up a custom tracking domain (e.g., track.2ndchair.net) in Instantly first. Custom domains are less likely to get flagged than Instantly's shared default. But at your current volume, skip it.

### Authentication (Pre-Send Checklist)
Every sending domain must have:
- [ ] SPF record configured
- [ ] DKIM record configured
- [ ] DMARC record configured
- [ ] Custom tracking domain (not Instantly's default)
- [ ] Warmup running for 2+ weeks minimum
- [ ] Test email sent to Gmail and Outlook — confirmed inbox, not spam

---

## The 7-Touch Sequence

See `04_Templates/Follow_Up_Sequence_7_Touch.md` for full copy of each email.

| Touch | Day | Type | Goal |
|-------|-----|------|------|
| 1 | Day 0 | Credentials + honestly won pitch | Earn a response |
| 2 | Day 3 | Value-add — CPSC reframe | Teach a new metric |
| 3 | Day 7 | Social proof / case study | Build credibility |
| 4 | Day 10 | "Show you the advertising" offer | Second Chair's proof move |
| 5 | Day 17 | Pain point specific to persona | Hit where it hurts |
| 6 | Day 22 | Breakup email | Trigger loss aversion |

**Note:** 6 touches, not 7. Research shows diminishing returns after 6 for our audience. The 3-7-7 cadence captures 93% of replies by Day 10.

### Reply Behavior
- Touch 1 captures 58% of all replies
- Follow-ups capture the remaining 42%
- Breakup email is often the highest-performing individual email (10-33% response rate)
- **Auto-pause entire sequence on any reply**

---

## Personalization by Tier

### Tier 1 (Whales) — Fully Personalized

**Investment:** 30-60 minutes per prospect

Pre-outreach research:
- Firm website (practice areas, attorney count, case results, "About Us")
- Google Ads activity (SpyFu — are they spending? How much? What keywords?)
- Best Lawyers / Super Lawyers ranking
- Recent news (verdicts, settlements, awards, hires)
- LinkedIn (managing partner's posts, activity, connections)

Personalization in email:
- Reference something specific about their firm (recent verdict, market position, growth)
- Reference their Google Ads activity if applicable ("I noticed your firm is actively advertising in [market]")
- Custom CTA based on their likely pain point

**Sent by:** Sasha, hand-written. Not through Instantly sequences.

### Tier 2 (Growth Firms) — Semi-Personalized

**Investment:** 5-10 minutes per prospect

Merge fields in Instantly:
- `{{firstName}}` — managing partner's first name
- `{{firmName}}` — firm name (subject line only)
- `{{city}}` — their primary metro
- `{{practiceArea}}` — their main PI focus (MVA, med mal, workers comp)

Body stays template but opening line is customized per segment (firm size, market, practice area).

**Sent by:** Instantly sequences, reviewed by Sasha before launch.

### Tier 3 (Mass) — Template-Based

**Investment:** <1 minute per prospect (batch load)

Merge fields: `{{firstName}}`, `{{city}}` only.

Generic template from `04_Templates/Cold_Email_Generic.md`.

**Sent by:** Instantly sequences, fully automated. Sasha loads batches weekly.

---

## A/B Testing

### What to Test (Priority Order)
1. **Subject line** — highest leverage, affects everything downstream
2. **Opening line / hook type** — timeline hook vs. pain point vs. question
3. **CTA** — specific ask vs. open-ended question
4. **Email length** — under 80 words vs. 80-125 words

### How to Test
- **One variable at a time.** Testing two makes results unreadable.
- **Minimum 250 contacts per variant** (500 total for A vs B). If list is smaller, accept directional results.
- **Wait 48 hours** for open data to stabilize.
- **Wait 5-7 days** for reply data before declaring winner.
- **Winning metric: positive reply rate** — not just opens.

### Subject Line Testing
- Run 2 variants per campaign minimum
- Review weekly at Friday retrospective
- Kill underperformers, iterate on winners
- Best performing format: 2-4 word, question-based, lowercase, personalized

---

## Response Handling

### Rules
- **All replies handled personally.** Never automated responses.
- **2-hour SLA** during business hours (9 AM - 5 PM ET).
- **Same-day response** for after-hours replies (by next morning at latest).

### By Response Type

**Positive ("Sure, let's talk"):**
1. Respond within 2 hours
2. Provide 2-3 specific time options + calendar link
3. Move to "Call Scheduled" in pipeline
4. Pre-call: prep per Discovery Call Script

**Negative ("Not interested"):**
1. Acknowledge gracefully: "Appreciate you letting me know."
2. Ask one clarifying question: "Out of curiosity — is it timing, or not a fit?"
3. Log reason in CRM
4. Move to Lost (or Nurture if "bad timing")

**"Not now" / "Check back later":**
1. Acknowledge: "Totally understand. When would be a better time to reconnect?"
2. Get a specific timeframe if possible
3. Move to Nurture with re-engage date
4. Set reminder in CRM

**Question ("How does this work?" / "What's the pricing?"):**
1. Answer briefly in the reply — don't dump everything
2. Pivot to call: "Easier to show you than explain over email. Worth 30 minutes?"
3. Stay in Responded stage until call is booked

**Unsubscribe / hostile:**
1. Honor immediately. Remove from all sequences.
2. Respond: "Done — you won't hear from me again. Appreciate your time."
3. Move to Lost. Never re-contact.

---

## Benchmarks & Targets

| Metric | Industry Avg | Our Target | Action If Below |
|--------|-------------|------------|-----------------|
| **Reply rate** | 3.4-5.1% | 5-8% | Test copy, tighten targeting |
| **Positive reply rate** | 50% of replies | 50%+ | Improve qualification |
| **Meeting booked rate** | 0.5-1% | 1.5-2% | Improve CTA, speed up response time |
| Bounce rate | — | Below 2% | Re-verify list |
| Spam complaint rate | — | Below 0.1% | Check copy, reduce volume, verify targeting |

**Open rate is not tracked.** Open tracking is disabled to protect deliverability. Reply rate is the primary metric.

---

## Email Signature Template

```
Sasha Zinshtein
Co-Founder, Second Chair
[phone]

Second Chair | [Address]
Reply STOP to opt out.
```

**No links in first email.** After first reply, can add 2ndchair.net.
**No images.** No logos. No HTML signature. Plain text only.

**[Address] = your virtual mailbox address.** Get one from iPostal1, Anytime Mailbox, or UPS Store ($15-40/mo). Pick a New York address for credibility. Replace `[Address]` in all templates once you have it.

---

## Why No Links in the First Email

This comes up a lot. The instinct is to put at least a website link in the signature. Here's why we don't.

**1. Spam filters treat links as marketing signals.** Google's RETVec ML system distinguishes personal emails from marketing/bulk. A plain text email with zero links looks like a one-to-one personal message. Add a link — even one — and it shifts the signal toward marketing. On a fresh outreach domain with no reputation, that shift can be the difference between inbox and spam.

**2. Tracking domains are the real killer.** Instantly (and most email tools) wrap links in tracking domains to measure clicks. These tracking domains are shared across thousands of cold emailers and get flagged constantly. Even custom tracking domains hurt deliverability on fresh domains.

**3. Fresh domain = no benefit of the doubt.** 2ndchair.co has no sending history. Google and Microsoft scrutinize every element — links, images, HTML — 10x more aggressively on new domains than on established ones. Once the domain is aged with good engagement metrics (3-6 months), links in first emails become safer.

**4. The data backs it up.** HTML emails (which include formatted links, images, signatures) have a 652% higher bounce rate than plain text. Links also enable spam filter "sandbox testing" where the filter follows the link to evaluate the destination — if it looks like a lead gen site, that's another negative signal.

**5. Prospects Google you anyway.** People see "Second Chair" in the signature and look it up themselves. This is actually better because it shows higher intent (they chose to look you up), doesn't trigger any spam signals, and means they're already interested before they land on the site.

**The rule by domain:**
- **2ndchair.net (main domain, starting here):** At 20 emails/day this looks like normal business email. 0-1 links is fine. Still recommend zero links in first touch for maximum deliverability.
- **2ndchair.co (outreach domain, future):** Once set up and warmed, zero links in Touches 1-5. Link OK in breakup email (Touch 6).
- **After someone replies:** Links, website, calendar — whatever you need. The reply established the relationship.
