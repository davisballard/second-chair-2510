# Second Chair — Platform Intelligence

**What this document is:** A reference for anyone working on Second Chair — brand, copy, website, sales materials — who needs to understand what the technology platform actually does. This is not positioning. It is a plain-English account of the product Alex is building: what it is, how it works, what it's built on, and why it matters.

**Consumer brand:** Fair Case (getafaircase.com)

---

## 1. What The Platform Is

The Second Chair platform is a two-sided lead generation and delivery system built specifically for personal injury law. It has four components:

1. **Consumer intake** — A quiz funnel under the consumer brand (Fair Case / getafaircase.com) that captures injured people, qualifies their case details, and collects TCPA-compliant consent.
2. **The pipeline** — A backend system that validates, scores, verifies, and routes every submission before it ever reaches a law firm.
3. **Premium nurturing (optional)** — AI or human qualification within 90 seconds, with live transfer capability for firms that opt in.
4. **Firm-side delivery** — A portal, email, and webhook delivery layer that puts qualified leads directly into a law firm's workflow.

Second Chair is what the law firm sees and pays for. The consumer brand is what injured people see. The pipeline and premium nurturing are invisible to both — they're the infrastructure that makes the product worth selling.

The design intent is to own the full chain: from the moment an injured person clicks an ad to the moment a qualified lead lands in a firm's intake queue (standard tier) or transfers live to a firm's phone (premium tier). Most lead gen businesses stop at form submission. This one doesn't.

---

## 2. The Consumer Intake Funnel

The consumer funnel lives at getafaircase.com and is the entry point for every lead in the system.

### How it works

A person clicks an ad, lands on a conversion-optimized landing page, and begins a guided 6-question quiz:

1. Type of accident (car, truck, motorcycle, pedestrian, rideshare, other)
2. When it happened (within 30 days / 1–6 months / 6–12 months / over a year)
3. Medical treatment status (ongoing / completed / planning / none)
4. Fault (not my fault / unsure / partially my fault)
5. Whether they already have an attorney
6. Injury severity (minor / moderate / severe / life-altering)

After the quiz, they reach the contact step where they submit name, phone, and email.

### What's collected beyond the answers

Every submission captures:

- Full quiz answers
- Contact information
- TCPA consent (with timestamp)
- TrustedForm certificate URL (consent evidence, generated client-side)
- UTM parameters and referral source
- Session metadata: device type, screen resolution, user agent, timezone
- Behavioral signals: time on page, interaction patterns, bot detection flags

### Why this matters for lead quality

Most competitor funnels are 3-field forms. This quiz collects structured case data before anyone picks up the phone. By the time a lead reaches a firm, the firm already knows the injury type, recency, treatment status, fault position, and severity. The intake work is partially done.

The funnel has been conversion-tested across multiple landing page and quiz variants simultaneously. Landing page angles tested include emotional (victim framing), value-focused (settlement range), and adversarial urgency (insurance company framing). Each variant controls headline, CTA text, trust signals, settlement estimate display, exit intent behavior, and first-contact timing.

A settlement range estimator is shown during the quiz as a conversion device — it gives injured people a reason to complete. It is calculated from injury type, severity, and treatment status, and is shown only in certain variants. It is a display tool, not a legal representation.

---

## 3. The Pipeline

Every submission runs through a sequential processing pipeline before it is stored, scored, or delivered. No lead skips any stage.

```
Submission received
       │
       ├── 1. Validation & sanitization
       ├── 2. Rate limiting & deduplication
       ├── 3. Bot challenge verification (Cloudflare Turnstile)
       ├── 4. Internal suppression check
       ├── 5. Heuristic bot detection
       ├── 6. External compliance checks (DNC, litigator, TrustedForm)
       ├── 7. Scoring (Fit Score + Quality Score → Grade)
       ├── 8. Routing (firm assignment)
       ├── 9. Premium Routing (if opted in):
       │      ├── Check SC availability (Davis/Sasha toggle)
       │      ├── If available → Trigger premium call (AI or Human)
       │      ├── If unavailable → Check firm hours
       │      │    ├── During firm hours → Deliver to firm standard
       │      │    └── After hours → AI fallback (if AI tier)
       │      └── Log call attempt, recording, transcript, outcome
       └── 10. Delivery (portal + email/webhook, or post-call notes)
```

### Dual Scoring Engine

Every lead receives two independent scores and a composite letter grade.

**Fit Score (0–100)** — Measures the economic potential of the case.

| Factor | Max Points | What it measures |
|---|---|---|
| Injury severity | 40 | Settlement size potential |
| Recency | 20 | Statute of limitations risk |
| Medical treatment | 15 | Documented damages |
| Fault position | 10 | Settlement probability |
| Case type | 15 | Average case value by accident type |

Hard adjustments: −40 points if already represented by an attorney. Stale cases with no treatment are penalized further.

**Quality Score (0–100)** — Measures submission legitimacy.

| Factor | Max Points | What it measures |
|---|---|---|
| Time on page | 25 | Bots submit fast; humans take time |
| Behavioral integrity | 25 | Bot detection signal result |
| Attribution clarity | 20 | Known traffic source = real channel |
| Session metadata completeness | 15 | Missing fields suggest automation |
| TCPA consent quality | 15 | Consent with timestamp = compliance |

Hard adjustments: −25 points for missing TCPA consent. Individual bot signals (honeypot triggered, missing sec-fetch headers, etc.) each carry their own point deductions.

**Lead Grade (A / B / C / D)**

```
Composite = (Fit Score × 60%) + (Quality Score × 40%)
```

| Grade | Composite required | Quality floor | What it means |
|---|---|---|---|
| A | ≥ 85 | ≥ 70 | High-value, high-confidence — work immediately |
| B | ≥ 65 | ≥ 50 | Good case, trustworthy submission — same day |
| C | ≥ 45 | ≥ 30 | Marginal case or some quality flags — normal queue |
| D | Below thresholds | — | Low value or suspicious — human review before contact |

Hard blocks: a lead with an already-represented claimant, a confirmed bot signal, or missing consent cannot grade above C, regardless of fit score.

The grade travels with the lead into the firm portal. Firms see it immediately.

---

## 4. Compliance and Verification Infrastructure

This is the part of the platform that has no direct consumer-facing expression — it runs server-side on every lead — but it is one of Second Chair's strongest differentiators relative to shared lead marketplaces and conventional lead gen vendors.

### TrustedForm (ActiveProspect)

TrustedForm generates a tamper-proof certificate for every submission. The certificate is a cryptographically signed record of: the exact consent language shown, when it was shown, the form interaction, and the IP address of the submitter.

- **Certify**: runs on every lead, free. The certificate URL is captured in the form payload.
- **Verify**: called server-side on leads that will be routed — confirms the certificate matches the expected consent language.
- **Retain**: called after a lead is accepted for delivery — preserves the certificate in ActiveProspect's archive for long-term legal defense.

In the event of a TCPA dispute, the firm (and Second Chair) has a timestamped, court-admissible consent record. Most lead vendors cannot provide this. Most shared marketplaces do not generate certificates at the lead level at all.

### TCPA Consent Capture

Every lead captures:
- `tcpa_consent: true/false`
- `consent_timestamp`: exact UTC time consent was given
- The specific consent language presented (controlled by compliance rules, not by A/B variants)

TCPA consent fields are excluded from A/B testing — they are invariant across all variants. No test can remove or alter the consent step.

### DNC and Litigator Screening (dnc.com)

Before delivery, phone numbers are screened against:
- **Federal and state DNC registries** — numbers registered on do-not-call lists
- **Litigator Scrub** — known TCPA plaintiff phone numbers who have a documented history of filing TCPA lawsuits

Litigator hits suppress delivery entirely. DNC hits are handled with a fail-closed policy in the initial build — these leads are suppressed from routing until a restricted-contact workflow is available.

### Cloudflare Turnstile

A low-friction bot challenge runs at the contact step (where name/phone/email are submitted). Turnstile tokens are verified server-side — client-side completion alone is not trusted. Invalid tokens block the submission.

### Suppression Lists

An internal suppression table stores flagged IPs, phone numbers, emails, session fingerprints, and TrustedForm certificate IDs. Admin staff can add, review, and expire suppression rules. External suppression via ActiveProspect SuppressionList is configurable as a feed layer on top of internal tables.

### Twilio Lookup

Phone number intelligence runs on every accepted lead:
- **Line type**: distinguishes mobile, landline, and VoIP — landlines are flagged because they cannot receive texts
- **Reassigned number risk**: checks whether the number has recently been transferred to a new owner (TCPA compliance risk if the prior owner had a relationship with the firm)

### Verification Audit Trail

Every lead carries a `verification_status` field (`clear`, `review`, `blocked`, `error`) plus a full `lead_verifications` log table recording every provider call, its result, latency, reason code, and timestamp. The admin dashboard exposes this timeline per lead. Nothing is a black box.

---

## 5. Routing and Delivery

### Assignment

Once a lead clears verification and receives a grade, it is assigned to exactly one firm. The routing system checks:

- Whether the firm has available capacity (daily and weekly caps, configurable per firm)
- Whether the firm covers the lead's geography

Each firm's territory is configured by the admin team. A lead that cannot be routed (no firm available, caps reached) is held for admin review rather than discarded.

### Delivery Channels

Firms receive leads through whichever channels their setup specifies:

- **Firm portal** — the primary interface, with lead grade, full case details, and response-speed UI
- **Email** — sent via Resend from the platform domain, with structured lead data
- **Webhook** — a JSON payload compatible with Zapier, Make, Clio Grow, Salesforce, HubSpot, and Slack

Delivery uses an async queue (Upstash QStash) with automatic retry on failure — up to 5 retry attempts. Every delivery attempt is logged in `lead_deliveries` regardless of outcome.

### Volume Caps

Firms set daily and weekly lead caps. When a cap is reached, new matching leads are queued for admin review rather than auto-delivered. This prevents firms from being overwhelmed and gives Second Chair a mechanism to manage supply-demand balance without turning off delivery entirely.

---

## 6. Premium Nurturing (Optional Tier)

Firms can opt into premium qualification services that convert cold web leads into warm qualified leads or live transfers.

### Three Service Tiers

**Standard** — Web lead delivered to firm portal/email/webhook. Firm calls lead. Base price.

**AI-Qualified** (+$200) — AI voice agent calls lead within 90 seconds of form submission, completes 7-question intake script, delivers full transcript and structured notes. Available 24/7.

**Human Live Transfer** (+$1,200) — Davis or Sasha calls lead within 90 seconds, qualifies using same script with state-specific criteria (no-fault thresholds, contributory negligence, SOL), attempts live warm transfer to firm's intake line. If firm unavailable, delivers detailed qualification notes.

### Premium Routing Logic

```
Lead submitted → passes validation/scoring
       │
       ├── Is firm opted into premium tier?
       │     │
       │     NO → Standard delivery (portal/email/webhook)
       │     │
       │     YES → Check premium tier selected
       │          │
       │          ├── AI-Qualified Tier:
       │          │    ├── Trigger Bland.ai call within 90s
       │          │    ├── Execute 7-question script
       │          │    ├── Record call (two-party consent where required)
       │          │    ├── Generate structured notes + transcript
       │          │    └── Deliver to firm with AI qualification data
       │          │
       │          └── Human Live Transfer Tier:
       │               ├── Check SC availability (Davis/Sasha toggle at admin.2ndchair.net/availability)
       │               │    │
       │               │    AVAILABLE → Notify via WhatsApp
       │               │    │            ↓
       │               │    │        Human calls lead within 90s
       │               │    │            ↓
       │               │    │        Qualify using 7-question script + state criteria
       │               │    │            ↓
       │               │    │        Lead qualified? 
       │               │    │            │
       │               │    │            YES → Attempt live transfer to firm
       │               │    │            │      │
       │               │    │            │      SUCCESS → Log successful transfer
       │               │    │            │      FAIL → Deliver detailed notes for warm callback
       │               │    │            │
       │               │    │            NO → Log disqualified, do not bill
       │               │    │
       │               │    UNAVAILABLE → Check firm hours
       │               │                   │
       │               │                   DURING HOURS → Route to firm standard
       │               │                   AFTER HOURS → AI fallback (if available)
       │               │
       │               └── Log: call attempt, recording URL (Twilio), transcript, outcome, billing status
```

### Technical Stack (Premium Tier)

| Component | Technology | Purpose |
|---|---|---|
| **Availability Toggle** | Next.js admin panel + Supabase | Davis/Sasha set availability status |
| **WhatsApp Notifications** | WhatsApp Business API | Instant lead notification with contact info |
| **AI Voice** | Bland.ai | 24/7 AI voice agent, 7-question script execution |
| **Phone System** | Twilio Programmable Voice | Call routing, recording, transfer |
| **Call Interface** | Aircall | Human agent interface for Davis/Sasha calls |
| **Call Recording** | Twilio Recording API | Two-party consent compliance (stored 7 years) |
| **Transcript** | Bland.ai transcription | AI-generated from call audio |
| **Call Logs** | Supabase | Call attempts, outcomes, recordings, billing |

### Qualification Script (7 Questions)

Standard across AI and Human tiers:

1. **Injury Gate:** "Were you injured in the accident?" (Y/N — if No, politely end call)
2. **Injury Type:** "What type of injuries did you sustain?" (Whiplash, broken bones, head injury, etc.)
3. **Medical Treatment:** "Have you received medical treatment?" / "Are you still receiving treatment?"
4. **Fault:** "Was the accident your fault, the other party's fault, or are you unsure?"
5. **Attorney Status:** "Do you already have an attorney representing you for this accident?" (If Yes, politely end call)
6. **Accident Date:** "When did the accident happen?" (Verify within SOL for state)
7. **Contact Preference:** "What's the best way for the law firm to reach you — phone call, text, or email?"

**State-specific add-ons** (Human tier only):
- **No-fault states** (FL, MI, NJ, etc.): Verify injury threshold ($X+ medical costs)
- **Contributory negligence states** (NC, VA, MD, DC, AL): Confirm 0% fault
- **Pure comparative** (CA, NY, etc.): Note fault percentage for settlement impact

### Call Recording Compliance

**Two-party consent states:** CA, CT, FL, IL, MA, MD, MT, NH, PA, WA
- Automated announcement at call start: "This call may be recorded for quality assurance and training purposes."
- If lead objects, recording stops and call continues unrecorded (notes only)

**One-party consent states:** All others
- Recording starts immediately (SC is consenting party)

Recordings stored 7 years (TCPA compliance requirement). Accessible via admin panel per lead.

### Billing Logic

- **AI-Qualified:** Bill base + $200 if call completes (lead answers and script executes). No bill if lead doesn't answer or hangs up immediately.
- **Human Live Transfer:** Bill base + $1,200 if lead qualifies and transfer is attempted. No bill if lead doesn't answer, hangs up immediately, or disqualifies (no injury, already represented, etc.).

---

## 7. The Firm Portal

The firm portal is the law firm team's primary interface for working their assigned leads.

### What firms see

- All leads assigned to their account (and only their leads — other firms' data is never visible)
- Lead grade (A/B/C/D) at a glance
- Full case summary: injury type, accident recency, treatment status, fault position, severity
- Contact information
- Lead age counter — a live timer showing how long the lead has been waiting. Displays in green (recent), yellow (aging), and red (overdue). Speed-to-contact is the single largest predictor of conversion in PI intake; the UI makes the urgency visible.
- One-click status updates: contacted, not reached, signed, rejected, etc.
- Browser push notifications for new leads

### What the admin sees

The admin dashboard (internal-only) provides:

- Full lead volume and status breakdown
- Firm management: territory settings, delivery configuration, cap management
- Scoring weight configuration (adjustable without code deploys)
- Protection and verification settings
- A/B variant performance tracking
- Live pipeline view: every lead's current stage in real time
- Per-lead timelines: full audit from submission to delivery to firm outcome

---

## 7. Tech Stack

| Layer | Technology |
|---|---|
| Consumer funnel | SvelteKit (Svelte 5) |
| Pipeline backend, admin dashboard, firm portal | Next.js 14 (App Router), TypeScript |
| Database | Supabase (PostgreSQL with Row-Level Security) |
| Async queue | Upstash QStash |
| Email delivery | Resend |
| Hosting and deployment | Vercel + GitHub |
| Bot challenge | Cloudflare Turnstile |
| Consent verification | ActiveProspect TrustedForm |
| Phone intelligence | Twilio Lookup |
| Premium call routing | Twilio Programmable Voice |
| Premium call interface | Aircall |
| Premium AI voice | Bland.ai |
| Premium notifications | WhatsApp Business API |
| IP/fraud enrichment | MaxMind minFraud (Phase 2) |
| Second Chair website | Next.js, React — Vercel + GitHub |

The database uses Row-Level Security at the Supabase layer — firms can only query their own records, not other firms'. Admin access requires a separate authenticated role. There is no scenario where a firm portal user can access another firm's data.

The scoring engine weights and grade thresholds are stored in the database (not hardcoded), so they can be adjusted via admin UI and take effect within 30 seconds without a code deployment.

---

## 8. What This Means for Second Chair

The platform's technical infrastructure is not just an operational detail — it is a direct source of competitive differentiation in the pitch to law firms.

**Most shared lead marketplaces:**
- Sell the same lead to multiple firms simultaneously
- Capture a basic 3-field form with no case qualification
- Have no scoring — firms cannot know if a lead is worth calling before they call
- Have no compliance audit trail — if a TCPA claim arises, there is no documentation
- Deliver via email to whoever paid most for the territory, with no exclusivity guarantee

**What Second Chair delivers:**
- One firm receives each lead. No auction. No sharing.
- Every lead arrives pre-qualified: the firm knows injury type, recency, treatment status, fault position, and severity before first contact
- Every lead carries a letter grade (A/B/C/D) derived from a structured scoring model
- Every lead has a TrustedForm certificate — tamper-proof, timestamped consent evidence
- Every lead has passed DNC and litigator screening before delivery
- The firm portal shows lead age in real time, because the first 5 minutes after an injury inquiry are the highest-conversion window
- Delivery is configurable: portal, email, webhook, or all three — leads flow into whatever system the firm already uses
- Full audit trail: the firm can see exactly when a lead was submitted, verified, scored, routed, and delivered

The platform was built to make compliance a feature, not a checkbox. The firms Second Chair targets — PI firms spending $30K–$200K/month on lead acquisition — have been burned by unverifiable, unqualified, shared leads. The infrastructure above is the evidence that Second Chair is structurally different.

---

*Last updated: March 2026. Source: lead-gen/ monorepo (Alex DuBelko). Consumer brand: Fair Case (getafaircase.com) — confirmed March 12, 2026.*
