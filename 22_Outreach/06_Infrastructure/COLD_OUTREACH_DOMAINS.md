# Cold Outreach Domain Strategy

**Primary domain (never use for cold sends):** `2ndchair.net`
**Outreach domain (active):** `2ndchair.co`
**Backup domain (buy when scaling):** `secondchair.co`

**Last updated:** March 2026

---

## Why Separate Domains

Cold email has low engagement by nature (70-80% ignore rate). ISPs track engagement ratios per domain. If `2ndchair.net` sends cold emails that get ignored or spam-reported, it tanks deliverability for everything — client emails, proposals, invoices.

`2ndchair.co` is the outreach domain. If it gets burned, replace it for $12/year. `2ndchair.net` stays clean.

---

## Domain Roles

| Domain | Use For | Never Use For |
|--------|---------|---------------|
| `2ndchair.net` | Client communication, proposals, invoices, marketing emails to opted-in contacts | Cold outreach, mass sends to people who didn't opt in |
| `2ndchair.co` | All cold email outreach — attorney prospecting, venue outreach, brand partnerships | Client-facing communication after they become a client |

---

## Setup Checklist for `2ndchair.co`

### 1. Email Hosting
- [ ] Add `2ndchair.co` to Google Workspace (or set up Zoho free tier)
- [ ] Create outreach email addresses (e.g. `davis@2ndchair.co`, `sasha@2ndchair.co`)

### 2. DNS Authentication (All three required)
Follow the same structure as `Gmail_Namecheap_DNS_Checklist.md` but for `2ndchair.co`:

**SPF (TXT record):**
| Field | Value |
|-------|-------|
| Type | TXT |
| Host | `@` |
| Value | `v=spf1 include:_spf.google.com ~all` |

**DKIM (TXT record):**
| Field | Value |
|-------|-------|
| Type | TXT |
| Host | `google._domainkey` |
| Value | (get from Google Workspace Admin > Apps > Gmail > Authenticate email) |

**DMARC (TXT record):**
| Field | Value |
|-------|-------|
| Type | TXT |
| Host | `_dmarc` |
| Value | `v=DMARC1; p=none; rua=mailto:davis@2ndchair.co` |

### 3. Landing Page
- [ ] Set up a simple one-page site on `2ndchair.co`
- Content: Logo, one-line description ("Second Chair — Music-First Marketing for Attorneys"), link to `2ndchair.net`
- Purpose: Trust signal only — if a prospect checks the domain, it looks legit and routes to the main site
- Can be a simple Carrd page, static HTML on Vercel, or a Namecheap redirect with a parking page

### 4. Verify Setup
- [ ] MXToolbox: MX, SPF, DMARC lookups for `2ndchair.co`
- [ ] Google Admin Toolbox: Confirm DNS propagation
- [ ] Send test email to a Gmail and Outlook account — confirm it lands in inbox, not spam

---

## Warmup Protocol

Do NOT send cold outreach from `2ndchair.co` on Day 1. New domains have no reputation — ISPs treat unknown senders as suspicious.

**Week 1:**
- Send 10-20 emails/day to people you know (friends, existing contacts, team)
- Have them open, reply, and click links in your emails
- This builds positive engagement signals

**Week 2:**
- Increase to 20-40 emails/day
- Mix in a few cold sends (5-10) alongside warm sends
- Monitor: Are emails landing in inbox? Check spam folders

**Week 3:**
- Increase to 40-60 emails/day
- Shift ratio toward cold sends
- Monitor bounce rate (<2%) and spam complaints

**Week 4:**
- Full cold outreach volume (up to 50-80/day)
- Domain is warmed — maintain consistent daily volume
- Don't spike from 50/day to 200/day overnight — gradual increases only

**Warmup tools (optional):** Instantly.ai, Warmbox, Lemwarm — these automate the warm send/reply cycle. Worth it if you want to speed up the process.

---

## Cold Email Rules

### First Email to Any New Prospect
- **Plain text only** — no HTML templates, no images, no logos
- **No links** in the body (URLs trigger spam filters on fresh domains)
- **No email signature** with images/logos (HTML sig = spam signal)
- **Simple text signature:** Name, title, Second Chair, phone number
- **Short:** 75-125 words max

### Why Plain Text
ISPs process plain text emails differently than HTML. Plain text reads as personal correspondence, not marketing. On a fresh outreach domain, this is critical for inbox placement.

### After First Reply
Once a prospect responds, subsequent emails can include:
- Links to your site (`2ndchair.net`)
- A simple text signature
- Still avoid heavy HTML, images, and embedded logos

---

## Volume Guidelines

| Phase | Daily Volume | Split Across Domains |
|-------|-------------|---------------------|
| Starting out | 10-30/day | 1 domain (`2ndchair.co`) is enough |
| Active pipeline | 30-60/day | 1 domain still fine |
| Scaling campaigns | 60-100+/day | Add second domain (`secondchair.co`), split volume |

**Per-domain safe ceiling:** ~50-80 cold sends/day. Beyond that, add another domain rather than pushing one domain harder.

---

## If a Domain Gets Burned

Signs: Open rates drop below 10%, emails landing in spam, Google Postmaster shows reputation decline.

**Recovery:**
1. Stop all cold sends from that domain immediately
2. Send only to engaged/warm contacts for 2-3 weeks
3. Clean any bad addresses from your lists
4. Gradually reintroduce cold sends

**If recovery doesn't work:**
- Retire the domain for cold outreach
- Buy a replacement ($12/year)
- Warm it up (4 weeks)
- Keep the burned domain for its landing page redirect only

---

## Monitoring

**Weekly:**
- [ ] Check bounce rate per domain (<2%)
- [ ] Check open rates (should be 20-30% for well-targeted cold sends)
- [ ] Check spam complaint rate (<0.1%)

**Monthly:**
- [ ] Google Postmaster Tools — sender reputation for `2ndchair.co`
- [ ] SenderScore.org — overall domain score
- [ ] Review and remove inactive/bounced addresses

---

## Quick Reference

| Question | Answer |
|----------|--------|
| Can we send cold email from `2ndchair.net`? | No. Never. |
| How long to warm up `2ndchair.co`? | 2-4 weeks |
| How many cold emails/day? | Start at 10-20, scale to 50-80 per domain |
| Plain text or HTML for first email? | Plain text only, no images/links/sig |
| When to buy a second outreach domain? | When you're consistently sending 50+/day |
| What if `2ndchair.co` gets burned? | Rotate to backup domain, recover or replace |
