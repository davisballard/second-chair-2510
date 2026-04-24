# Appendix: Tool Stack & Engine Questionnaire

Fill this out together on the call. This unblocks the Founders Engine section and strengthens the Compliance + Intelligence sections.

---

## Alex — Product, Compliance & Technology

### Compliance Engine

**Consent Architecture:**
- **TrustedForm (ActiveProspect)** — captures and stores consent certificates on every lead; API v4 verify + match_lead validation; cert URLs stored for full audit trail
- **LeadConduit (ActiveProspect)** — hybrid intake orchestrator; runs TrustedForm verification and litigator scrub as blocking steps before lead acceptance
- **SuppressionList (ActiveProspect / DNC.com)** — checks phone, email, IP, and cert against suppression lists

**DNC/Litigator Screening:**
- **DNC.com — Contact Center Compliance (CCC)** — litigator scrub (live in production); identifies known litigators and serial filers. DNC Scrub, TCPA Reassigned Authority, and Disconnect Scrub available but not yet activated

**Fail-Closed Architecture:**
- TrustedForm verification failure → lead blocked
- Litigator Scrub non-success outcome → lead blocked
- Missing consent metadata (cert URL, TCPA consent, consent text, timestamp) → rejected with 400 error
- Suppression list matches → held for review before routing
- All verification results logged to `lead_verifications` table with provider, status, decision, reason code, and response excerpt

**What makes this compliant where competitors aren't:**
TrustedForm consent is a hard requirement — not optional, not bolted on. Every lead must pass consent verification before it enters the system. Known litigator screening runs as a blocking step. Two additional APIs validate phone numbers and email for quality.

> *Note: Alex flagged that DNC lists need a deeper conversation — many people on DNC lists have given explicit consent to be called. The nuance matters for how we position this.*

### Lead Scoring & Routing

**Dual Scoring Engine** (custom-built, `rules-v2.1`):

1. **Fit Score (0–100)** — case economic value
   - Injury severity (0–40 pts), recency (0–20 pts), medical treatment (0–15 pts), liability/fault (0–10 pts), injury type (0–15 pts)
   - Adjustments: -40 if has attorney, -8 if unsure; stale case penalty halves recency

2. **Quality Score (0–100)** — lead legitimacy
   - Engagement time (0–25 pts), behavioral integrity (0–25 pts), attribution clarity (0–20 pts), session metadata (0–15 pts), consent quality (0–15 pts)
   - Penalties: missing TCPA consent (-25), ultra-fast submissions, bot signals (-8 to -40 per signal)

**Lead Grade:** Composite = (Fit x 0.60) + (Quality x 0.40)
- **A:** composite ≥85, quality ≥70, no hard risks
- **B:** composite ≥65, quality ≥50, no hard risks
- **C:** composite ≥45, quality ≥30
- **D:** below thresholds or hard risk flags (already represented, bot suspect, missing TCPA)

**Scoring logic lives:** 100% custom-built in-app; all weights configurable in admin settings with backtest endpoint

**Routing — Exclusive Territory Model:**
1. **ZIP Code Overrides** (highest priority) — direct ZIP-to-firm mapping
2. **Market Territory** — geographic zones defined as ZIP code arrays, one firm per Market
3. **No match** → lead marked unroutable, status set to failed
- **Capacity management:** per-firm daily/weekly caps with atomic check-and-reserve (no race conditions); exclusive routing means no fallback when cap reached

### Performance Dashboard

**Built on:** Next.js 15, React 19, Recharts; hosted on Vercel (`app.2ndchair.net`)

**Metrics visible in admin dashboard:**
- Live lead counts, grade distribution, variant performance
- 5-stage pipeline funnel view (Preflight → Qualified → Verification → Routing → Delivery)
- Per-lead trace timeline with module-level execution details
- Source performance by UTM parameters
- Delivery latency tracking
- Upstream provider telemetry (LeadConduit callback outcomes)

**CPSC tracking:**
- Buyer-reported outcome fields: reviewed, contacted, qualified by firm, signed
- Outcome audit trail (who updated, when)
- Lead events timeline: created → scored → routed → delivered → outcome updated

**Firm portal view (what the attorney sees):**
- Firm-scoped lead queue (only their assigned leads, enforced by row-level security)
- Lead details, status tracking, outcome reporting
- Firm-level statistics and performance
- **CPSC not shown in portal** — Second Chair only has data up to the point the lead is delivered to the firm. Signed-case outcomes are not tracked in the product currently. CPSC is a modeled metric for internal/sales use, not a live dashboard number.
> *Resolved 2026-03-18: Alex confirmed CPSC can't be shown because we don't have post-delivery outcome data.*

### Product Infrastructure

**Frameworks & Hosting:**
- **SvelteKit 2 + Svelte 5** — consumer quiz funnel + buyer marketing site
- **Next.js 15 + React 19** — backend pipeline app, admin CRM, firm portal
- **Turborepo** — monorepo workspace orchestration
- **Vercel** — hosting and deployment for all three apps
- **Tailwind CSS 4** — styling across all frontends

**Database & Auth:**
- **Supabase (PostgreSQL)** — primary database, auth, row-level security
- 27 migrations, 15+ core tables

**Third-Party Services:**
- **LeadConduit (ActiveProspect)** — hybrid intake orchestration
- **TrustedForm (ActiveProspect)** — consent verification
- **DNC.com / CCC** — litigator scrub, phone compliance
- **SuppressionList** — multi-field suppression checks
- **Resend** — email delivery (buyer notifications)
- **QStash (Upstash)** — async delivery queue

**UI Libraries:**
- **Shadcn/UI + Radix UI** — admin/portal component system
- **Recharts** — dashboard charting
- **Lucide React** — iconography

**Layered Protection Stack (custom-built):**
- Server-side validation → bot detection (honeypot, time gates, UA analysis) → rate limiting → deduplication → suppression rules

### Recognizable Logos
TBD — pending roundtable decision on which logos to feature
> *Candidates with strong logos: Supabase, Vercel, SvelteKit, Next.js, TrustedForm/ActiveProspect, Tailwind*

### AI-Native Development

**Development tools:**
- **Claude Code** — primary development AI
- **Cursor** — AI-assisted coding

**AI agents:** 4–6 total (4 core agents, sometimes 1–2 additional per app)

**AI embedded in the product:**
- None currently embedded in the live product. Not necessary at this stage.
> *Resolved 2026-03-18: Alex confirmed — no AI in the product, not planned near-term.*

### One-liner for the website
> *Still pending from Alex — no one-liner provided yet.*
> *Suggested draft based on codebase: "A compliance-first lead platform with fail-closed consent verification, dual scoring, and exclusive territory routing — custom-built so every lead is verified before it reaches your desk."*

---

## Davis — Creative, Strategy & Systems

### Creative & Strategy Stack

**AI & Development:**
- **Claude Code (Anthropic)** — primary AI, runs everything
- **Superset** — application/system hub
- **OpenAI** — supplemental AI tasks
- **Gemini** — supplemental AI tasks

**Image Generation:**
- **Nano Banana Pro 2**
- **FLUX 1.1 Pro**

**Video Generation:**
- **Kling 2.5**
- **Higgsfield** — 360° views, cinema studio simulation

**Audio/Voice:**
- **ElevenLabs** — voice generation
- **Stable Audio 2.5** — music/background audio

**Post-Production:**
- **FFmpeg** — audio/video processing
- **Whisper** — speech-to-text/subtitles

**Infrastructure & Ops:**
- **FAL.ai** — API infrastructure layer
- **Airtable** — asset management & tracking
- **Supabase** — database/backend
- **Figma** — design
- **n8n** — workflow automation (planned)

### Recognizable Logos
TBD — pending Alex's tools + roundtable decision on which logos to feature

### AI Tools
- **Claude (Anthropic)** — primary LLM
- **Claude Code** — development & agent orchestration
- **OpenAI** — supplemental
- **Gemini** — supplemental

### AI Agents/Automations Running
23 specialized AI agents across 6 departments:
- **Strategy (6):** behavioral science, brand growth, narrative strategy, effectiveness research
- **Creative (5):** creative direction, art direction, copywriting, brand identity, UX design
- **Media (6):** media buying, Google/Meta platform specialists, CRM lifecycle, performance creative, account management
- **Production (4):** AI creative direction, UI/UX, web design, integrated production
- **Accounts (1):** sales
- **Legal/Compliance (1):** Saul — ad compliance review through entire creative process

Additional: n8n workflows (planned)

### Research System
- **What powers it:** 4Cs Deep Dive Methodology (Consumer, Category, Culture, Company) executed by AI agent team; behavioral science library (14 frameworks including Cialdini, loss aversion, cognitive ease); multi-agent synthesis round tables; claimant timing tier analysis; zip code demographics; competitor activity mapping; consumer persona development from behavioral research
- **How automated:** AI-powered research directed by human strategic judgment — agents do the research gathering, framework application, and synthesis; Davis directs what to research, validates findings, and makes all strategic/creative decisions

### One-liner for the website
"A 23-agent AI system that delivers full-agency creative — from behavioral research to finished ads — directed by 18 years of brand strategy experience."

---

## Sasha — Sales & Media

### Media Buying Stack
- **Meta Ads Manager**
- **Google Ads**
- **Google Tag Manager** — conversion tracking/pixel implementation
- **Google Ad Manager** — ad serving
- **StackAdapt** — programmatic DSP

### Reporting/Analytics
- ___

### One-liner for the website
- Sasha's system in one sentence for an attorney: ___

---

## Shared / Company-Wide

- **Combined AI agent count:** ~29 (Davis 23 + Alex 4–6)
  - *Note: Previous estimate of 55 (Davis 23 + Alex 32) was incorrect. Alex confirmed 4–6 agents on 2026-03-18.*
- **Combined tool count:** ___
- **Tools with recognizable logos** (for Engine diagram): ___
- **Output multiplier** — how many people-equivalent does the system produce?
  - Current prototype says "25" — is this right, or higher/lower? ___
- **The "only us" claim** — what combination of capabilities does Second Chair have that no competitor can replicate? ___
