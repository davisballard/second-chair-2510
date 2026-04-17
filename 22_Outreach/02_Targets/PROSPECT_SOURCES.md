# Prospect Sources

> **Owner:** Julian Cole (strategy), Alex DuBelko (scraping/execution)
> **Source:** Validated against 00_Research_Findings.md
> **Updated:** March 24, 2026

---

## Total Addressable Market

- **US PI legal market:** $61.7B (2026)
- **~164,559 PI attorneys** across **~60,000 firms**
- **Second Chair sweet spot:** 3-50 attorney firms, $3M-$50M revenue

---

## Source Priority Matrix

Sources ranked by signal quality — how likely a prospect from this source is to buy PI leads.

### Tier 1: Hottest Signals (Build First)

**1. SpyFu — Firms Already Running Google Ads**
- **Why #1:** If they're spending on Google Ads for PI keywords, they're already buying leads. Proven ad buyers = shortest path to a deal.
- **What you get:** Domain, estimated monthly PPC spend, keywords bidding on, ad copy history
- **How:** Search "[city] personal injury lawyer" → see which domains are bidding
- **Cost:** $39/mo (Basic plan)
- **Action:** Alex exports domain lists for target metros. Sasha cross-references with firm names.
- **Accuracy caveat:** SpyFu reports only ~10% of actual ad spend. Use directionally, not as exact figures.

**2. Best Lawyers / U.S. News Rankings — Pre-Qualified, High-Budget Firms**
- **URL:** https://www.bestlawfirms.com/united-states/personal-injury-litigation-plaintiffs
- **What you get:** 3,187 PI firms ranked nationally. Tier 1/2/3 by metro. Firm name, location, total awards, number of attorneys, client endorsements.
- **Why valuable:** These firms have prestige, budget, and ambition. Tier 1 firms in major metros are ideal prospects.
- **Scraping:** No Cloudflare. Predictable URL patterns. Medium feasibility — Alex can build scraper.
- **Cost:** Free (manual) or scraping setup time

### Tier 2: Strong Coverage (Build Second)

**4. Google Maps — Complete Market Coverage**
- **What you get:** Every PI firm with a Google Business Profile in target metros. Firm name, address, phone, website, Google rating, review count.
- **How:** Search "personal injury lawyer [city]" → scrape all results
- **Tools:** Outscraper ($3/1,000 records after 500 free) or Apify Google Maps Scraper ($29-39/mo)
- **Signal:** Review count and rating = proxy for firm activity and size. 100+ reviews = established firm.
- **Limitation:** Gets firm's general contact info, not managing partner direct email. Needs enrichment via Apollo.

**5. Avvo — 97% of All US Attorneys**
- **URL:** https://www.avvo.com
- **What you get:** Name, practice areas, location, phone, website, Avvo rating (1-10), client reviews, peer endorsements, years of experience
- **Tools:** Apify "Avvo Attorney Scraper" (parseforge) — turnkey, API access
- **Signal:** Filter by Avvo rating 8+ and 10+ reviews for active, reputable PI firms
- **Cost:** $29-39/mo via Apify
- **Note:** Has Cloudflare but existing scrapers handle it with proxy rotation

**6. Apollo.io — Decision-Maker Enrichment**
- **URL:** https://www.apollo.io
- **What you get:** Managing partner and marketing director names, direct emails, LinkedIn profiles
- **How:** Input firm domains from Google Maps/Avvo → Apollo returns individual contacts by title
- **Cost:** Free (100 credits/mo) or $59/mo (Basic, 5,000 credits)
- **Key for:** Turning firm-level data into person-level outreach targets

### Tier 3: Supplementary Sources (Build As Needed)

**7. AAJ (American Association for Justice) Member Directory**
- **URL:** directory.justice.org
- **What you get:** Plaintiff trial attorneys searchable by practice area, state, city
- **Why valuable:** Self-selected plaintiff attorneys — nearly perfect overlap with PI lead buyers
- **Cost:** Free to search

**8. State Bar Directories**
- **Best for PI filtering:** Florida (floridabar.org) and Texas (texasbar.com) — both allow practice area search
- **Limitation:** California and New York do NOT filter by practice area
- **Best use:** Verification and enrichment, not primary prospecting
- **Scraping:** Apify has California State Bar scraper. Florida/Texas need custom builds.

**9. Super Lawyers — Top 5% of Attorneys**
- **URL:** https://attorneys.superlawyers.com/personal-injury-plaintiff/
- **What you get:** Pre-qualified, top-tier PI attorneys. 1,559 in LA alone.
- **Limitation:** Cloudflare bot protection. No existing scrapers. Manual compilation or headless browser needed.
- **Best use:** Manually identify whales in priority metros

**10. Martindale-Hubbell — AV-Rated Firms**
- **URL:** https://www.martindale.com
- **What you get:** 1M+ lawyers. AV Preeminent rating = top 10% peer-reviewed attorneys.
- **Scraping:** No Cloudflare detected. Medium feasibility.
- **Signal:** AV-rated PI firms are established, successful, and have marketing budgets

**11. Pre-Built Attorney Email Lists**
- **BookYourData:** 373,000+ verified attorney emails. ~$0.40/contact. Claims 97% accuracy.
- **UpLead:** $99-199/mo. 95% accuracy guarantee.
- **Best use:** Fast bootstrap if scraping/enrichment pipeline isn't ready yet

**12. Other Directories**
- **Justia** (justia.com/lawyers) — Free profiles, Apify scrapers available
- **FindLaw** (lawyers.findlaw.com) — Apify scraper available
- **Expertise.com** — "Best PI lawyers" by city rankings
- **Lawyer Legion** — Aggregates bar association data

---

## Scraping Feasibility Summary

| Source | Cloudflare? | Existing Scrapers? | Feasibility | Alex Priority |
|--------|------------|-------------------|-------------|--------------|
| Google Maps | N/A | Yes (multiple) | HIGH | Week 1 |
| Avvo | Yes | Yes (Apify) | MEDIUM-HIGH | Week 1 |
| Best Lawyers | No | No | MEDIUM | Week 1-2 |
| Justia | Unknown | Yes (Apify) | HIGH | Week 2 |
| FindLaw | Unknown | Yes (Apify) | HIGH | Week 2 |
| Martindale | No | No | MEDIUM | Week 3 |
| Super Lawyers | Yes | No | LOW | Manual only |
| State Bars (FL/TX) | No | Partial | MEDIUM | Week 3 |

---

## Legality

Scraping publicly visible attorney directory data for B2B outreach is **legal** per hiQ Labs v. LinkedIn (9th Circuit, affirmed multiple times). Key rules:

- Factual data (names, addresses, phone numbers) is not copyrightable
- Don't scrape behind login walls
- Use rate limiting — don't overload servers
- Respect robots.txt where practical
- Provide opt-out mechanism in all outreach emails
- Main risk is a cease-and-desist from a directory site (civil, not criminal)

---

## Build Order for Alex

**Week 1:**
1. Set up SpyFu — export PI firms running Google Ads in NYC and LA
3. Set up Outscraper/Apify — scrape Google Maps for "personal injury lawyer" in top 10 metros
4. Set up Avvo scraper via Apify — filter PI attorneys in target markets

**Week 2:**
5. Scrape Best Lawyers PI firm rankings by metro
6. Enrich firm domains with Apollo.io (managing partner/marketing director contacts)
7. Run Justia and FindLaw scrapers for additional coverage

**Week 3+:**
8. Martindale-Hubbell AV-rated firms
9. Florida and Texas state bar directories
10. Super Lawyers — manual compilation for whale targets

**Ongoing:**
- New data batches → Datablist (dedup) → MillionVerifier (verify) → Instantly (load)
- Re-verify lists monthly — email addresses decay ~2-3% per month
