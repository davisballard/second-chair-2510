# Premium Lead Nurturing Service Agreement — Contract Addendum

> **Type:** Legal Contract Template
> **Status:** Active Template
> **Date:** April 2026
> **Use:** Attach to base Second Chair Lead Generation Agreement

---

## Premium Lead Nurturing Service Agreement

**This Addendum** modifies and supplements the Second Chair Lead Generation Agreement dated [BASE AGREEMENT DATE] between Second Chair ("Vendor") and [FIRM NAME] ("Client").

---

### Section 1: Service Tiers

Client has enrolled in Second Chair's Premium Lead Nurturing service, which offers three tiers of lead delivery:

#### Tier 1: Standard Web Lead (Base Service)
- Pre-qualified web form submission from Fair Case consumer funnel
- Dual scoring (conversion likelihood + case value)
- Real-time delivery via portal, email, and webhook
- TrustedForm certificate, DNC/litigator screening, Twilio Lookup
- **Pricing:** Base MOI price per Market (as specified in base agreement)

#### Tier 2: AI-Qualified Lead (Premium Service)
- All Standard Lead features PLUS:
- AI voice agent calls lead within 90 seconds of form submission
- Completes 7-question intake qualification script
- Verifies case criteria (injury, treatment, liability, insurance, SOL)
- Delivers lead with full call transcript, structured intake notes, and qualification status
- **Pricing:** Base MOI price + $200 premium
- **Availability:** 24/7/365

#### Tier 3: Human Live Transfer (Premium Service)
- All Standard Lead features PLUS:
- Second Chair agent (Sasha or Davis) calls lead within 90 seconds of form submission
- Completes 7-question intake qualification script
- Verifies case criteria per state-specific requirements
- Attempts live warm transfer to Client's intake line during business hours
- **Pricing:** Base MOI price + $1,200 premium
- **Availability:** M-F 9am-6pm PT (or as specified in Schedule A)
- **Billing Model:** Pay-per-transfer — flat rate charged regardless of whether live transfer succeeds or firm is unavailable

---

### Section 2: Pricing Examples

**Market:** [City/State]
**Base MOI Price:** $[X]/lead

| Service Tier | Total Price | Premium Surcharge |
|---|---|---|
| Standard Web Lead | $[X] | — |
| AI-Qualified Lead | $[X + 200] | +$200 |
| Human Live Transfer | $[X + 1,200] | +$1,200 |

**Example (Denver, CO — Base $315):**
- Standard web lead: $315
- AI-qualified lead: $515 ($315 + $200)
- Human live transfer: $1,515 ($315 + $1,200)

**Example (New York City — Base $460):**
- Standard web lead: $460
- AI-qualified lead: $660 ($460 + $200)
- Human live transfer: $1,660 ($460 + $1,200)

---

### Section 3: Service Enrollment

**Client has selected the following premium tier:**

☐ AI-Qualified Leads (24/7 availability)  
☐ Human Live Transfer Leads (business hours availability)  
☐ Hybrid: AI fallback when humans unavailable

**Monthly lead package:** [X] leads/month at base pricing

---

### Section 4: Billing & Payment Terms

#### Base Package Billing
- Base lead package billed upfront on 1st of month
- Example: 100 leads × $315 = $31,500 (due March 1)

#### Premium Surcharge Billing
- Premium surcharges billed weekly based on actual premium lead delivery
- Invoice issued every Monday for previous week's premium leads
- Payment due net-7 (7 days from invoice date)
- Premium leads count toward monthly package total

**Example Weekly Invoice:**
```
Week of March 31, 2026
Base Package: 100 leads/month at $315/lead = $31,500 (billed March 1)

Premium Surcharges This Week:
- 5x AI-Qualified leads: 5 × $200 = $1,000
- 8x Human Live Transfer leads: 8 × $1,200 = $9,600

Total Premium Charges: $10,600
Due: April 7, 2026 (net-7)

Lead delivery this week: 13 leads (counts toward 100-lead package)
Remaining in package: 87 leads
```

#### Pay-Per-Transfer Model (Human Tier Only)
- Client is billed flat rate ($1,200 premium) per qualified call
- Billing applies regardless of live transfer outcome:
  - **Transfer succeeded:** Firm connected live with lead
  - **Firm unavailable:** SC agent qualified lead, delivered detailed notes for warm callback
- Calls where lead does not answer or hangs up immediately are NOT billed
- Calls where lead is disqualified (no case) are NOT billed

#### Payment Methods
- ACH (preferred)
- Wire transfer
- Credit card (3% processing fee applies to premium surcharges)

---

### Section 5: Availability & Routing Logic

#### Second Chair Availability (Human Tier)
**Business Hours:** [M-F 9am-6pm PT] (or as specified in Schedule A)

SC agents (Sasha/Davis) available to field premium calls during specified hours. Availability status managed via admin dashboard toggle.

#### Client/Firm Availability
**Intake Hours:** [Specify hours, e.g., M-F 8am-7pm MT, 24/7, etc.]

Client specifies hours when intake team is available to receive live transfers. SC verifies firm status before attempting transfer.

#### Routing Priority
1. **If Human tier selected AND SC available:** SC agent calls lead, qualifies, attempts live transfer
2. **If SC unavailable:** Lead routes to Firm during Firm availability hours (standard delivery, no premium)
3. **If both unavailable AND AI enabled:** AI intake triggers (AI premium billed)
4. **If both unavailable AND AI not enabled:** Standard lead delivery (no premium)

**Client acknowledges:** Standard web leads may still be delivered when premium service is unavailable. Premium surcharges apply only when premium services are actually rendered.

---

### Section 6: Service Level Agreements (SLAs)

#### Speed to Contact
- **AI tier:** Call attempt within 90 seconds of form submission
- **Human tier:** Call attempt within 90 seconds of form submission (when SC available)
- **Standard delivery:** Immediate delivery via portal/email/webhook

#### Qualification Standards
- All leads qualified using Second Chair's 7-question intake script
- State-specific criteria applied (no-fault thresholds, contributory negligence, SOL)
- Structured intake notes provided with every premium lead
- Call recordings provided with every premium lead

#### Quality Metrics
- **Qualification accuracy target:** >85% (qualified leads accepted by firm as viable cases)
- **Call completion target (human):** >90% (lead answers phone)
- **Call completion target (AI):** >85%

#### Performance Reporting
Client receives weekly email report including:
- Premium lead volume by tier
- Qualification accuracy (% of qualified leads firm accepts)
- Conversion rates by tier (based on firm's signed case reporting)
- Average time to contact (form submission to call)
- Cost per signed case by tier

---

### Section 7: Call Recording & Compliance

#### Recording Policy
- All premium calls (AI and Human) are recorded for quality assurance, compliance, and client verification
- Recordings retained for 12 months minimum
- Client has full portal access to all call recordings

#### Two-Party Consent Compliance
**States requiring pre-call announcement:** CA, FL, IL, MD, MA, MI, MT, NH, OR, PA, WA

For leads in two-party consent states, automated announcement plays before call connects:
> "This call may be recorded for quality assurance and training purposes."

Client acknowledges that SC's call recording practices comply with federal and state law.

#### Data Security
- Call recordings stored encrypted in Twilio Cloud or Aircall
- Access restricted to authorized SC staff and Client portal users
- Recordings tied to lead records in Second Chair database (Supabase)
- No recordings shared with third parties without Client consent

---

### Section 8: Intake Data & Lead Ownership

#### Data Provided
For every premium lead, Client receives:
- All standard lead data (contact info, accident details, form responses)
- Full call recording (audio file)
- Call transcript (AI-generated)
- Structured intake notes (7-question framework)
- Qualification decision (qualified / needs review / disqualified)
- State-specific threshold analysis
- Recommended next action

#### Lead Ownership
- Client owns all lead data immediately upon delivery
- Premium leads are exclusive to Client (never resold or shared)
- Market exclusivity applies (as specified in base agreement)

---

### Section 9: Client Responsibilities

#### For Human Live Transfer Tier
Client agrees to:
1. **Maintain intake availability** during specified Firm availability hours
2. **Answer live transfers promptly** (within 30 seconds when available)
3. **Provide performance feedback** within 48 hours if qualified lead is rejected
4. **Report signed cases** within 7 days of retainer execution (for conversion tracking)

#### Unavailability Protocol
If Client is unavailable during specified hours:
- Client updates availability status via portal OR
- SC delivers detailed intake notes for warm callback
- Human premium is still billed (pay-per-transfer model)

#### Performance Data Sharing
To enable accurate conversion tracking and optimization:
- Client reports signed case status (signed Y/N, not case details)
- Client provides reason code for rejected leads (e.g., "outside SOL," "pre-existing attorney," "insufficient injury")
- Data used solely for SC service improvement, never shared externally

---

### Section 10: Disqualification & Replacement Policy

#### Disqualified Leads (Not Billed)
SC does NOT bill premium surcharge for:
- Lead does not answer phone (no call completion)
- Lead hangs up immediately (<15 seconds)
- Lead determined to have no case (no injury, outside SOL, has attorney, claimant at fault)

#### Qualified Leads (Billed at Premium Rate)
SC bills premium surcharge for:
- Lead qualifies per 7-question script
- Meets state-specific case criteria
- Call recording + intake notes delivered
- Live transfer attempted (Human tier) OR AI qualification completed

#### Quality Disputes
If Client believes a qualified lead should not have been qualified:
1. Client submits dispute within 48 hours with reason code
2. SC reviews call recording + intake notes
3. If SC error confirmed: Premium surcharge credited
4. If qualification was accurate per script: Charge stands

**Dispute resolution standard:** Did lead meet published case criteria at time of call? (Not: Did firm ultimately sign the case?)

---

### Section 11: Service Modifications & Termination

#### Changing Tiers
Client may change premium tier with 7 days written notice:
- Upgrade: Takes effect immediately
- Downgrade: Takes effect at start of next billing period

#### Adding/Removing AI Fallback
Client may enable or disable AI fallback tier at any time via portal toggle (takes effect immediately)

#### Termination of Premium Service
Either party may discontinue premium nurturing service with 7 days written notice:
- Standard lead delivery continues per base agreement
- Premium surcharges stop accruing immediately
- Final premium invoice due upon termination

#### Termination of Base Agreement
If base lead generation agreement terminates, premium service terminates automatically.

---

### Section 12: Limitations & Disclaimers

#### No Conversion Guarantee
SC provides qualified leads based on intake criteria. SC does NOT guarantee:
- Firm will sign retainer with lead
- Lead will hire any attorney
- Case will settle or reach verdict
- Specific conversion rates or ROI

**Performance targets** (40-60% conversion for live transfers, 15-25% for AI) are industry benchmarks, not contractual guarantees.

#### Firm's Sole Discretion
Client retains sole discretion to:
- Accept or reject any lead
- Determine which cases to pursue
- Set own case acceptance criteria beyond SC qualification

#### Technical Limitations
SC makes reasonable efforts to ensure service availability but is NOT liable for:
- Phone system outages (Twilio, Aircall, carrier issues)
- AI service interruptions (Bland.ai, Vapi downtime)
- Lead's phone unreachable (disconnected, voicemail full, carrier blocks)
- Internet connectivity issues

#### Limitation of Liability
SC's total liability for any claim related to premium nurturing service is limited to premium surcharges paid in the 30 days prior to claim.

---

### Section 13: Pilot Program Terms (Optional)

**If applicable:** Client has enrolled in a pilot program with modified terms:

☐ **Pilot Term:** [30/60/90 days]  
☐ **Pilot Pricing:** [Discounted rate or standard rate]  
☐ **Pilot Volume:** First [X] premium leads  
☐ **Performance Review:** Scheduled for [Date]  

**Pilot conversion to standard terms:** If Client does not cancel in writing 7 days before pilot end date, service automatically converts to standard premium pricing.

---

### Section 14: Schedule A — Client-Specific Terms

**Client:** [FIRM NAME]  
**Market(s):** [City, State]  
**Base MOI Price:** $[X]/lead  
**Monthly Package:** [X] leads/month  

**Premium Tier Selected:**  
☐ AI-Qualified ($[X + 200]/lead)  
☐ Human Live Transfer ($[X + 1,200]/lead)  

**SC Availability (Human Tier):**  
[Days/Hours, e.g., M-F 9am-6pm PT]  

**Firm Availability (for live transfers):**  
[Days/Hours, e.g., M-F 8am-7pm MT, 24/7]  

**Billing Contact:**  
[Name, Email, Phone]  

**Intake Contact (for live transfers):**  
[Name, Phone, Email]  
**Backup Contact:**  
[Name, Phone, Email]  

**Special Terms (if any):**  
[E.g., Spanish-language priority, custom availability hours, pilot pricing, etc.]

---

### Section 15: Signatures

By signing below, both parties agree to the terms of this Premium Lead Nurturing Service Agreement Addendum, which supplements and modifies the base Second Chair Lead Generation Agreement dated [DATE].

**SECOND CHAIR (VENDOR)**

Signature: ___________________________  
Name: [Sasha/Davis]  
Title: [Founder / Operations Director]  
Date: ___________________________  

**[FIRM NAME] (CLIENT)**

Signature: ___________________________  
Name: [Attorney Name]  
Title: [Managing Partner / Attorney]  
Date: ___________________________  

---

## Appendix A: Qualification Script Summary

For Client reference, Second Chair's qualification script includes:

**7 Core Questions:**
1. Were you injured in the accident?
2. Did you see a doctor or get medical care?
3. When did the crash happen? (SOL check)
4. Who was at fault — you, the other driver, or both?
5. Is the other driver insured?
6. Can you briefly describe what happened?
7. Do you already have an attorney?

**State-Specific Add-Ons:**
- **No-fault states (FL, NY, MI, MA, MN, HI, UT):** Threshold questions (hospitalization, fracture, permanent injury, medical bill amount)
- **Choice no-fault states (PA, NJ, KY):** Tort election status (full tort vs. limited tort)
- **Contributory negligence states (DC, MD, VA, NC, AL):** Zero-fault verification (claimant cannot be at fault at all)

Full script available at: `Second_Chair/09_Operations/Intake_Qualification_Script.md`

---

## Appendix B: Sample Intake Notes

**Format provided with every premium lead:**

```
PREMIUM QUALIFICATION CALL — [Date/Time]
Agent: [Sasha/Davis/AI]
Duration: [MM:SS]

QUALIFICATION DECISION: [QUALIFIED / NEEDS REVIEW / DISQUALIFIED]

1. INJURY: [Yes/No] — [Type]
2. TREATMENT: [Yes/No] — [Location] — [Date]
3. ACCIDENT DATE: [MM/DD/YYYY] — SOL: [Within/Close/Expired]
4. LIABILITY: [Other driver 100% / Shared / Unclear] — [Description]
5. INSURANCE: [Other driver insured: Y/N] — [Company] — [UM coverage: Y/N]
6. NARRATIVE: [1-2 sentence summary]
7. ATTORNEY STATUS: [None / Already has one]

STATE-SPECIFIC:
[Threshold met: Y/N] — [Details]

TRANSFER STATUS: [Successful / Firm unavailable / Did not attempt]

NOTES: [Any red flags or special circumstances]

NEXT ACTION: [Live transfer completed / Firm to call back / Disqualified]
```

---

## Appendix C: Weekly Performance Report Sample

**Format delivered every Monday:**

```
[FIRM NAME] — Week of [Date]

LEADS DELIVERED: [X] total
- [X] AI-qualified leads ($[Y] each)
- [X] Human live transfer leads ($[Z] each)
  - [X] connected live
  - [X] firm unavailable (notes provided)

CONVERSION RATES (based on your intake reporting):
- AI-qualified: [X]% (industry avg: 15-25%)
- Human live transfer: [X]% (industry avg: 40-60%)

COST PER SIGNED CASE:
- AI-qualified: $[Price] / [Conversion %] = $[Cost per case]
- Human live transfer: $[Price] / [Conversion %] = $[Cost per case]

BENCHMARK: Industry standard CPSC is $2,500-$3,000

ROI ANALYSIS (assuming $35,000 avg settlement, 33% contingency):
- Attorney fee per case: $11,550
- Acquisition cost: $[Cost per case]
- Net profit per case: $[Fee - Cost]
- ROI: [Multiplier]x

📊 Full dashboard: [portal link]
```

---

*Second Chair — Premium Lead Nurturing — April 2026*
