# Outreach Tool Stack

> **Updated:** March 24, 2026
> **Source:** Validated against 00_Research_Findings.md

---

## Core Stack

| Tool | Purpose | Cost | Status |
|------|---------|------|--------|
| **Instantly Outreach Hypergrowth** | Cold email sending, warmup, sequences, A/B testing | $77.60/mo (annual) | Setup needed |
| **Instantly CRM Growth** | Outbound pipeline tracking, deal stages, unified inbox | $37.90/mo (annual) | Setup needed |
| **Google Workspace (2ndchair.net)** | Email inboxes — starting outreach here (already warmed) | Already have | Active |
| **Google Workspace (2ndchair.co)** | Backup/scale outreach domain (future) | $14-21/mo (2-3 users) | Needs setup |
| **SpyFu Basic** | Identify PI firms running Google Ads | $39/mo | Setup needed |
| **LinkedIn** (free accounts) | Connection requests, DMs, content | Free | Active |

## Data & Verification

| Tool | Purpose | Cost | Status |
|------|---------|------|--------|
| **MillionVerifier** | Email verification for prospect lists | $37 one-time (10K credits) | Setup needed |
| **Datablist** | List deduplication (fuzzy matching, merges records) | Free | Use as needed |
| **Apollo.io** | Contact enrichment — find managing partner emails | Free (100 credits/mo) | Setup needed |

## Scraping & Prospecting

| Tool | Purpose | Cost | Status |
|------|---------|------|--------|
| **Outscraper or Apify** | Google Maps + directory scraping | $29-39/mo | Setup needed |
| **Apify Avvo Scraper** | Avvo attorney directory scraping | Included with Apify | Setup needed |
| **Custom scrapers (Alex)** | Super Lawyers, state bars, Best Lawyers | Dev time | Build as needed |

## Monitoring & Compliance

| Tool | Purpose | Cost | Status |
|------|---------|------|--------|
| **Google Postmaster Tools** | Gmail deliverability monitoring | Free | Setup needed |
| **MXToolbox** | Blacklist monitoring, DNS verification | Free | Active |
| **Virtual office address** | CAN-SPAM physical address compliance | $30-50/mo | Setup needed |

## Existing Infrastructure

| Tool | Purpose | Location |
|------|---------|----------|
| **Lead Pipeline App** | Inbound lead tracking, firm portals, admin dashboard | `lead-gen/apps/lead-pipeline-app/` |
| **2ndchair.net** | Main website, client-facing | Live |
| **2ndchair.co** | Backup/scale outreach domain | Needs Google Workspace + warmup |

---

## Monthly Budget Summary

| Category | Monthly Cost |
|----------|-------------|
| Instantly (Outreach + CRM) | $115.50 |
| SpyFu | $39.00 |
| Scraping tools | $29-39 |
| Virtual office (CAN-SPAM) | $30-50 |
| Apollo.io (if upgraded) | $0-59 |
| **Total** | **~$215-$305/mo** |

One-time setup: MillionVerifier $37

---

## Setup Priority

1. **Virtual office address** — CAN-SPAM compliance, needed before any emails go out
2. **Instantly Outreach + CRM** — Core sending infrastructure (already connected to 2ndchair.net)
3. **MillionVerifier** — Verify prospect email lists before loading into Instantly
4. **2ndchair.co setup** — Google Workspace + SPF/DKIM/DMARC + Instantly warmup (backup/scale domain, not urgent at 20/day volume)
5. **SpyFu** — Identify hottest prospects (firms already running Google Ads)
6. **Google Postmaster Tools** — Set up monitoring before volume ramps
7. **Scraping tools** — As Alex builds scrapers for new prospect sources
8. **Apollo.io** — Enrich prospect records with decision-maker contacts

---

## Integration Map

```
Prospect Sources (SpyFu, Google Maps, Avvo, Best Lawyers)
    ↓
Alex cleans/deduplicates (Datablist + MillionVerifier)
    ↓
Load into Instantly Outreach (email sequences)
    ↓
Replies → Instantly CRM (pipeline tracking)
    ↓
Call Scheduled → Discovery call (Sasha)
    ↓
Proposal Sent → Attorney Pitch doc
    ↓
Signed → Lead Pipeline App (Alex's dashboard) for lead delivery
```
