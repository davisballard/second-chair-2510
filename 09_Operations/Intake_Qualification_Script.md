# Premium Lead Nurturing — MVA Intake Qualification Script

> **Type:** Operational Playbook — Human & AI Intake
> **Status:** Active
> **Date:** April 2026
> **Owner:** Sasha + Davis (Human) | AI Platform (Automated)

---

## Overview

This is the canonical qualification script for Second Chair's premium lead nurturing service. Both human agents (Sasha/Davis) and AI intake use the same 7-question framework to ensure consistency, compliance, and accurate case qualification.

**Total script time:** 90 seconds (2-3 minutes with conversation)

**Purpose:**
- Verify case viability before live transfer or detailed handoff
- Screen out non-viable leads (saves firm time)
- Gather intake data for firm's CRM
- Create conversion-optimized warm introduction

---

## The 90-Second Script

### Opening (10 seconds)

**Human version:**
> "Hi [Name], this is [Sasha/Davis] from Second Chair. You just requested information about your car accident. Do you have 2 minutes for a quick consultation to see if you have a case?"

**AI version:**
> "Hi [Name], I'm calling from Second Chair about your recent car accident inquiry. I'd like to ask you a few quick questions to see if we can help. This will only take about 2 minutes. Is now a good time?"

**Goal:** Get permission to proceed, set time expectation, warm tone

---

### Core Qualification Questions (60 seconds)

Ask these 7 questions in order. Listen for red flags. Take brief notes.

#### Q1: Injury Gate
**"Were you injured in the accident?"**

- **Y** → Continue
- **N** → Polite decline (see disqualification script)
- **Notes:** Listen for injury type (helps with no-fault threshold later)

#### Q2: Medical Treatment
**"Did you see a doctor or get medical care?"**

- **Y** → "Where did you go — hospital, ER, urgent care, or doctor's office?"
- **N** → "Are you planning to see a doctor soon?"
  - If no plans: Flag for review (may not meet threshold)
  - If yes: Note intent, proceed

**Record:** Treatment location, date (if provided)

#### Q3: Statute of Limitations Check
**"When did the crash happen?"**

- Calculate: Is it within SOL for this state?
  - Most states: 2 years
  - NY: 3 years
  - TN, LA: 1 year (urgent)
  - MN: 6 years
- If outside SOL or very close (within 30 days): Flag immediately

**Record:** Date of accident

#### Q4: Liability Screen
**"Who was at fault — you, the other driver, or both?"**

- **Other driver 100%** → Excellent
- **Shared fault** → Note percentage if they mention it
  - At-fault states: Usually OK under comparative negligence
  - Contributory negligence states (DC, MD, VA, NC, AL): Any fault = disqualify
- **Claimant at fault** → Polite decline

**Record:** Fault determination, any details about how accident happened

#### Q5: Insurance Recovery Screen
**"Is the other driver insured?"**

- **Y** → "Do you know their insurance company?"
- **N** → "Do you have uninsured motorist coverage?"
  - If no UM coverage: Flag (recovery may be difficult)
  - If yes UM: Note, proceed

**Record:** At-fault driver insurance status, company name if known

#### Q6: Narrative / Red Flag Check
**"Can you briefly describe what happened?"**

- **Goal:** Listen for:
  - Clear liability story
  - Legitimate injury mechanism
  - Red flags: fraud indicators, inconsistencies, DUI by claimant
- **Let them talk** for 30-60 seconds
- **Empathy statement:** "I'm sorry that happened to you."

**Record:** Brief summary (1-2 sentences)

#### Q7: Attorney Status (Disqualifier)
**"Do you already have an attorney?"**

- **N** → Continue to closing
- **Y** → "I see. You'll want to work with your current attorney on this. Best of luck." (End call)

---

### State-Specific Add-On Questions

**Only ask if relevant to the state. Add AFTER Q2 (medical treatment).**

#### No-Fault States (FL, NY, MI, MA, MN, HI, UT)

**Florida & New York (Highest Threshold):**
> "Were you hospitalized, did you break any bones, or do you have permanent injuries from the accident?"

- **Y** → Note injury type (fracture, hospitalization, permanent = likely clears threshold)
- **N** → "How long were you in pain or unable to work?"
  - FL/NY: Need 90+ days disability OR permanent injury
  - If soft tissue only with quick recovery: Flag as marginal

**Michigan:**
> "Would you say your injuries have seriously affected your ability to live your normal life?"

- Looking for: "Serious impairment of body function"
- Soft tissue with full recovery: Marginal
- Ongoing pain, limited mobility, missed work: Strong

**Massachusetts:**
> "About how much were your medical bills?"

- **$2,000+** → Clears threshold automatically
- **Under $2,000** → Ask about serious injury (fracture, permanent damage)

**Minnesota, Utah, Hawaii:**
> "Were your medical bills over $3,000-4,000?"

- MN: $4,000 threshold OR 60-day disability
- UT: $3,000 threshold
- HI: $5,000 threshold OR serious injury

#### Choice No-Fault States (PA, NJ, KY)

**Pennsylvania, New Jersey, Kentucky:**
> "Do you know if you have full tort or limited tort coverage on your insurance?"

- **Full tort** → Excellent, no threshold
- **Limited tort** → Similar threshold to no-fault (permanent/serious injury required)
- **Don't know** → Note for firm to verify (most drivers have limited tort)

---

### Closing (20 seconds)

#### If Qualified → Live Transfer Attempt

**"Great — based on what you've told me, you have a strong case. I'm going to connect you with [Firm Name] right now so you can speak with their intake team. Hold on one moment while I get them on the line."**

**Actions:**
1. Hit transfer button (Twilio dial to firm intake line)
2. Brief intro to firm: *"Hi, this is [Name] from Second Chair. I have [Lead Name] on the line. They were in an accident on [Date] in [City], [Injury Type], other driver at fault and insured. Transferring now."*
3. Connect call
4. Stay on until firm confirms connection, then drop

#### If Qualified BUT Firm Unavailable → Warm Handoff

**"Perfect — you have a strong case. [Firm Name] is currently with another client, but I'm sending them your information right now with a note that this is urgent. They'll call you back within 5 minutes. Keep your phone handy. Is [Phone Number] the best number to reach you?"**

**Actions:**
1. Note "URGENT - LIVE QUALIFIED" in lead record
2. Send detailed intake notes to firm immediately
3. Text/email lead: *"Thanks for speaking with me. [Firm Name] will call you at [Phone] within 5 minutes."*

#### If NOT Qualified → Polite Decline

**Choose appropriate script:**

**No injury:**
> "Based on what you've told me, it sounds like you weren't injured in the accident. Without an injury, there typically isn't a personal injury case here. But I'd recommend following up with your insurance company about any property damage. Thanks for your time."

**Outside statute of limitations:**
> "I appreciate you reaching out. Unfortunately, the accident was outside the time limit for filing a claim in your state. I wish we could help, but the deadline has passed. Thanks for contacting us."

**Claimant at fault (contributory negligence state):**
> "Thanks for the details. In [State], if you were partially at fault, it affects your ability to recover compensation. The attorney would need to review this carefully. I'm passing your information along, but I want to set your expectations that this may be difficult. They'll follow up if they can help."

**Uninsured at-fault party + no UM coverage:**
> "I see. The challenge here is that the other driver doesn't have insurance, and you don't have uninsured motorist coverage. That makes recovery difficult because there's no insurance company to pay a settlement. The firm will review your case, but I want to set your expectations that this may not be viable. They'll be in touch if they can help."

**Minor soft-tissue injury in no-fault state:**
> "Thanks for sharing that. In [State], there's a threshold for pursuing a case — you typically need a fracture, permanent injury, or significant medical treatment. Based on what you've described, this may not meet that threshold. I'm passing your information to the firm, and they'll review it, but I want to set your expectations. They'll follow up if they can help."

**Already has attorney:**
> "Got it. Since you're already working with an attorney, you'll want to continue with them. Best of luck with your case."

---

## State-Specific Case Criteria Quick Reference

### At-Fault States (Standard Comparative Negligence)

**States:** TX, IL, GA, CA, AZ, WA, CO, OR, WI, MO, OH, IN, TN, LA, OK, MS

**Viability Requirements:**
- ✓ Injury occurred
- ✓ Medical treatment (ER/urgent care/doctor minimum)
- ✓ Accident within SOL (typically 2 years; TN/LA = 1 year)
- ✓ Other driver at fault (or shared fault under comparative negligence rules)
  - **Modified 51% bar (TX, IL, GA, WI, OH, IN, TN, OK, OR):** Claimant must be <51% at fault
  - **Modified 50% bar (CO):** Claimant must be <50% at fault
  - **Pure comparative (CA, AZ, WA, MO, LA, MS):** Any fault % recovers proportionally
- ✓ Other driver has insurance OR significant assets
- ✓ No existing attorney

**Red Flags:**
- Claimant admits majority fault (>50%)
- No medical treatment and no intent to seek treatment
- DUI by claimant
- Accident over 1 year old in TN/LA (SOL risk)

---

### No-Fault States

#### Florida

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Tort threshold:** Permanent injury, significant scarring, hospitalization, fracture, or death
  - Permanent injury: Ongoing pain, limited mobility, chronic condition
  - Significant scarring: Visible permanent scarring (face, exposed areas)
  - Fracture: Any broken bone confirmed by X-ray/medical records
  - Hospitalization: Admitted to hospital (not just ER visit)
  - 90/180 rule: 90 days of total disability OR 180 days of partial disability

**Red Flags:**
- Soft-tissue only (whiplash, muscle strain) with full recovery in <90 days
- Minor ER visit, no follow-up treatment, no fracture
- "Feeling fine now" within weeks of accident

#### New York

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Serious injury threshold (Insurance Law §5102(d)):** Must meet ONE of 9 categories:
  1. Death
  2. Dismemberment
  3. Significant disfigurement
  4. Fracture
  5. Loss of fetus
  6. Permanent loss of use of body organ, member, function, or system
  7. Permanent consequential limitation of use of body organ or member
  8. Significant limitation of use of body function or system
  9. Medically determined injury preventing normal activities for 90 of 180 days

**Red Flags:**
- Soft-tissue injury with no fracture, no permanent limitation
- Quick recovery (<90 days)
- No ongoing medical treatment

#### Michigan

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Serious impairment threshold:** Objectively manifested impairment of important body function that affects general ability to lead normal life
  - "Important body function" = mobility, sight, cognition, etc.
  - "Affects normal life" = can't work, can't do daily activities, ongoing limitations

**Red Flags:**
- Minor injury with no impact on daily life
- Full return to work and normal activities within weeks

#### Massachusetts

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Threshold:** $2,000 in medical expenses OR serious injury
  - Serious injury: Death, dismemberment, significant disfigurement, fracture, loss of sight/hearing

**Note:** MA has the LOWEST no-fault threshold — easiest to clear. $2K in medical bills = automatic qualification.

#### Minnesota, Hawaii, Utah

**Minnesota:**
- $4,000 in medical expenses OR 60+ days disability OR permanent injury

**Hawaii:**
- $5,000 in medical expenses OR serious injury

**Utah:**
- $3,000 in medical expenses OR serious injury

---

### Choice No-Fault States

#### Pennsylvania

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Tort election check:** Must have "full tort" OR meet serious injury threshold if "limited tort"
  - ~75% of PA drivers have limited tort (lower premiums)
  - Limited tort threshold: Similar to NY serious injury standard

**Script:** "Do you know if you have full tort or limited tort coverage?"
- Full tort: No additional threshold
- Limited tort: Need serious injury (fracture, permanent, significant disfigurement)
- Unknown: Flag for firm to verify via insurance card

#### New Jersey

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Threshold:** Must have "zero threshold" OR meet verbal threshold if standard policy
  - Verbal threshold = permanent injury (similar to PA limited tort)
  - Most NJ drivers have verbal threshold

#### Kentucky

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **Threshold:** Must have "tort" OR meet threshold if "basic reparations" (no-fault option)
  - Basic reparations threshold = permanent injury, death, or serious disfigurement

---

### Contributory Negligence States (Harshest Standard)

**States:** DC, MD, VA, NC, AL

**Viability Requirements:**
- All standard criteria PLUS:
- ✓ **ZERO fault by claimant** — plaintiff cannot be at fault AT ALL
  - Even 1% fault = complete bar to recovery
  - Must have CLEAR other-driver liability

**Script Adjustment:**
- Q4 becomes: "Was the other driver completely at fault, or were you partially responsible for the accident in any way?"
- If claimant mentions ANY contributory fault: Polite decline or "flag for review"

**Red Flags:**
- Claimant admits any fault ("I might have been going a little fast too")
- Unclear liability (intersection accident, both rolling through stop)
- Any suggestion of shared responsibility

---

## Call Recording Compliance

### Two-Party Consent States (Must Announce)

**States requiring announcement:** CA, FL, IL, MD, MA, MI, MT, NH, OR, PA, WA

**Script (pre-call automated message via Twilio):**
> "This call may be recorded for quality assurance and training purposes."

**Technical implementation:**
- Twilio `<Say>` tag plays before connecting to lead
- 3-second announcement
- Recording starts after announcement completes

### One-Party Consent States (No Announcement Required)

All other states — recording can occur without notification.

**SC policy:** Announce in ALL states for consistency and transparency.

---

## Quality Assurance

### Post-Call Checklist (Human)

After every call, verify you captured:
- [ ] All 7 core questions answered
- [ ] State-specific question asked (if applicable)
- [ ] Qualification decision (qualified / needs review / disqualified)
- [ ] Call recording saved to lead record
- [ ] Intake notes written in structured format
- [ ] Lead status updated in Supabase
- [ ] Billing tier updated (Human Live Transfer premium)

### AI Output Validation (Human Review)

Sasha/Davis review all AI calls flagged as "needs review":
- AI uncertain about qualification
- Conflicting answers
- Unusual injury or liability circumstances
- High-value case indicators (trucking, severe injury)

**Review within:** 2 hours during business hours, next morning if after hours

---

## Intake Notes Template (Structured Format)

Copy this into lead record after call:

```
PREMIUM QUALIFICATION CALL — [Date/Time]
Agent: [Sasha/Davis/AI]
Duration: [MM:SS]

QUALIFICATION DECISION: [QUALIFIED / NEEDS REVIEW / DISQUALIFIED]

1. INJURY: [Yes/No] — [Type: e.g., back pain, broken arm, whiplash]
2. TREATMENT: [Yes/No] — [Location: ER/Hospital/Doctor/Urgent Care] — [Date if provided]
3. ACCIDENT DATE: [MM/DD/YYYY] — SOL: [Within/Close/Expired]
4. LIABILITY: [Other driver 100% / Shared / Unclear] — [Brief description]
5. INSURANCE: [Other driver insured: Y/N] — [Company if known] — [UM coverage: Y/N/Unknown]
6. NARRATIVE: [1-2 sentence summary of accident]
7. ATTORNEY STATUS: [None / Already has one]

STATE-SPECIFIC:
[FL/NY threshold met: Y/N] — [Details: fracture/hospitalization/permanent injury]
[PA/NJ tort status: Full/Limited/Unknown]

TRANSFER STATUS: [Successful / Firm unavailable / Did not attempt]

NOTES: [Any red flags, special circumstances, or urgency factors]

NEXT ACTION: [Live transfer completed / Firm to call back within 5 min / Disqualified - no follow-up]
```

---

## Training & Onboarding

### For Human Agents (Sasha/Davis)

**Before first call:**
1. Read this script 3x
2. Practice with role-play (5 mock calls minimum)
3. Memorize 7 core questions
4. Review state-specific criteria for top 5 states (CA, FL, TX, NY, IL)
5. Shadow 3 live calls (listen only)
6. Supervised calls: First 10 calls with review/feedback

**Ongoing:**
- Weekly script review (5 minutes)
- Monthly conversion rate analysis by agent
- Quarterly re-training on state-specific updates

### For AI Configuration (Bland.ai / Vapi)

**Prompt engineering:**
- Load this script as base prompt
- Add conversational flexibility ("I didn't catch that, can you repeat?")
- Empathy statements at injury/narrative
- Clear end-of-call summary

**Testing:**
- 50 test calls across common scenarios
- Validate structured output matches template
- Confirm state-specific logic triggers correctly
- Test disqualification paths (no injury, outside SOL, has attorney)

---

## Common Objections & Responses

### "I'm not sure if I want to pursue this."
**Response:** "I understand. There's no commitment right now — we just want to see if you have a case. If you do, [Firm Name] can explain your options and you can decide from there. Fair enough?"

### "How much is my case worth?"
**Response:** "That's a great question. The attorney will need to review all the details — your medical records, the police report, and the insurance information — before giving you an estimate. But based on what you've told me, you have a viable case. Let's get you connected with them so they can walk you through it."

### "Do I have to pay anything upfront?"
**Response:** "No, [Firm Name] works on contingency, which means they only get paid if you win. There are no upfront costs. They'll explain the details when you speak with them."

### "I already talked to another lawyer."
**Response:** "Got it. Are you working with them, or are you still exploring options?"
- If working with them: "You'll want to continue with your current attorney. Best of luck."
- If exploring: "No problem. [Firm Name] can give you a second opinion. Let me connect you."

### "I don't have time right now."
**Response:** "I totally understand. When would be a better time for [Firm Name] to call you back?" [Get specific time, note in record]

---

## Red Flags — Do Not Qualify

Immediate disqualification if:
- No injury whatsoever
- Already represented by attorney (and not shopping)
- Claimant was 100% at fault
- Accident outside statute of limitations
- Claimant admits DUI at time of accident
- Fraud indicators (story doesn't add up, asks about payout first, coached answers)
- Hostile or abusive toward agent

**Flag for review** (don't auto-disqualify, let firm decide):
- Marginal no-fault threshold (soft tissue, minimal treatment)
- Shared fault in contributory negligence state
- Uninsured at-fault driver with no UM coverage
- Very recent accident (same day — may not have treatment yet)
- Minor injury with high damages potential (e.g., commercial vehicle, multiple defendants)

---

## Performance Metrics

**Target KPIs (Human Agents):**
- Call completion rate: >90% (lead answers)
- Qualification accuracy: >85% (firm accepts qualified leads)
- Average call time: 2-3 minutes
- Transfer success rate: >80% (when firm is available)
- Conversion rate (qualified leads): 40-60%

**Target KPIs (AI):**
- Call completion rate: >85%
- Qualification accuracy: >75%
- Average call time: 3-4 minutes
- Escalation rate to human review: <20%
- Conversion rate (qualified leads): 15-25%

---

## Script Updates & Version Control

**Current Version:** 1.0 (April 2026)

**Update triggers:**
- State law changes (SOL, no-fault threshold, tort reforms)
- Firm feedback on qualification accuracy
- Conversion rate drops below targets
- New case types added (beyond MVA)

**Change log:**
- v1.0 (April 2026): Initial script for MVA cases

---

*Second Chair — Premium Lead Nurturing — April 2026*
