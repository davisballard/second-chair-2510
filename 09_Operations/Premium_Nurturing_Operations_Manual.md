# Premium Lead Nurturing — Operations Manual

> **Type:** Day-to-Day Operations Playbook
> **Status:** Active
> **Date:** April 2026
> **For:** Sasha + Davis (Human Agents)

---

## Overview

This is the operational playbook for running Second Chair's premium lead nurturing service day-to-day. It covers:
- How to manage your availability
- What happens when a premium lead comes in
- How to handle calls and transfers
- Billing and record-keeping
- Troubleshooting common issues

**Read this before handling your first premium call.**

---

## Daily Operations Checklist

### Morning (Start of Business Day)

**9:00am PT (or whenever you start):**

☐ **Turn on availability toggle** 
  - Go to: `admin.2ndchair.net/availability`
  - Click toggle to "Available for Premium Nurturing"
  - Verify WhatsApp is connected and notifications are on

☐ **Check phone readiness**
  - Phone charged >50%
  - Aircall app open and logged in
  - Ringer on (not silent/DND)
  - Test call to verify audio quality

☐ **Review overnight leads**
  - Check dashboard for any AI-qualified leads that came in after hours
  - Review intake notes for follow-up needs
  - Check if any firms need callbacks

☐ **Check availability hours**
  - Verify today's hours are correct in dashboard
  - Update if you need different hours today (e.g., leaving early for appointment)

---

### During the Day (Active Hours)

**When you're available:**

☐ **Keep phone accessible**
  - WhatsApp notifications on
  - Aircall app open or available to open quickly
  - Not in meetings unless availability is OFF

☐ **Respond to premium lead notifications within 15 seconds**
  - WhatsApp will alert you: "🚨 NEW PREMIUM LEAD"
  - Open notification, read lead details
  - Tap "Accept" link or decline

☐ **Handle calls per script**
  - Use the 7-question qualification script
  - Take brief notes during call
  - Attempt live transfer if qualified

☐ **Update lead records after each call**
  - Mark qualification decision
  - Add intake notes
  - Update status

---

### End of Day

**6:00pm PT (or whenever you finish):**

☐ **Turn OFF availability toggle**
  - Admin dashboard → Toggle to OFF
  - This routes new leads to AI or standard delivery

☐ **Review day's premium leads**
  - Check all calls have recordings saved
  - Verify all intake notes are complete
  - Flag any "needs review" leads for tomorrow

☐ **Check billing**
  - Verify premium surcharges were created for all qualified calls
  - Flag any discrepancies for review

---

## Availability Management

### How to Update Your Availability

**Dashboard location:** `admin.2ndchair.net/availability`

**Toggle options:**
- **Available (ON):** You'll receive WhatsApp notifications for premium leads
- **Unavailable (OFF):** Premium leads route to AI fallback or standard delivery

**Business hours setting:**
- Default: M-F 9am-6pm PT
- Can customize per day
- Auto-off after hours (if enabled)

### When to Turn Availability OFF

Turn availability OFF when:
- ✓ End of work day
- ✓ Lunch break (30+ minutes away from phone)
- ✓ In important meeting
- ✓ Sick or taking time off
- ✓ Traveling (unless you can handle calls)
- ✓ Phone low battery and no charger nearby

**Don't worry:** Leads will still be handled by AI or delivered to firm standard. You're not "losing" leads — just routing them differently.

### WhatsApp Notification Format

**What you'll see:**

```
🚨 NEW PREMIUM LEAD

Name: John Smith
Phone: +1 (720) 555-1234
City: Denver, CO
Injury: Back pain, neck pain

Accept or decline within 15 seconds:
https://admin.2ndchair.net/leads/abc123/accept
```

**What to do:**
1. **Read quickly** (name, city, injury)
2. **Tap "Accept" link** if you can take the call right now
3. **Don't tap** if you're busy (it will timeout after 15 seconds and route elsewhere)

### 15-Second Response Window

**Why 15 seconds?**
- Leads expect immediate contact (speed to lead)
- If you don't respond, system automatically routes to next option
- Not a test — it's fine to let it timeout if you're busy

**If you miss it:**
- Lead automatically routes to AI or firm
- No penalty — system is designed for this
- Check dashboard later to see what happened

---

## Handling Premium Calls

### Step-by-Step: From Notification to Transfer

#### Step 1: Notification Arrives (15-second window)

WhatsApp alert: "🚨 NEW PREMIUM LEAD"

**Do:** Read name, city, injury type  
**Then:** Tap "Accept" link if available

---

#### Step 2: Accept the Call

Aircall app opens automatically and dials the lead.

**What happens:**
- Twilio calls the lead's phone
- Recording announcement plays (in two-party states)
- Lead answers (hopefully)
- You're connected

**If lead doesn't answer:**
- Voicemail triggers automatically
- Lead marked as "no answer"
- No billing (no call completion)
- Move to next lead

---

#### Step 3: Run the Qualification Script

**Use the 7-question script** (see `Intake_Qualification_Script.md`):

1. "Were you injured in the accident?"
2. "Did you see a doctor or get medical care?"
3. "When did the crash happen?"
4. "Who was at fault — you, the other driver, or both?"
5. "Is the other driver insured?"
6. "Can you briefly describe what happened?"
7. "Do you already have an attorney?"

**Plus state-specific add-ons** (if applicable):
- FL/NY: "Were you hospitalized, break any bones, or have permanent injuries?"
- PA/NJ: "Do you have full tort or limited tort coverage?"
- DC/MD/VA: "Was the other driver completely at fault, or were you partially responsible in any way?"

**Take brief notes** during the call in Aircall notes field.

**Typical call time:** 2-3 minutes

---

#### Step 4: Make Qualification Decision

Based on answers, decide:

**QUALIFIED** = Strong case, proceed to transfer
- Injury occurred
- Medical treatment (or intent to get treatment)
- Within statute of limitations
- Other driver at fault (or shared in comparative negligence state)
- Other driver insured (or claimant has UM coverage)
- No existing attorney
- Meets state-specific threshold (no-fault, contributory negligence)

**NEEDS REVIEW** = Marginal case, flag for firm review
- Very recent accident (same day, no treatment yet)
- Soft-tissue injury in no-fault state (might not meet threshold)
- Shared fault in contributory negligence state
- Uninsured at-fault driver but claimant might have UM coverage

**DISQUALIFIED** = No case
- No injury
- Outside statute of limitations
- Claimant 100% at fault
- Already has attorney
- Fraud indicators (story doesn't add up, coached answers)

---

#### Step 5A: If QUALIFIED → Transfer to Firm

**Script:**  
> "Great — based on what you've told me, you have a strong case. I'm going to connect you with [Firm Name] right now. Hold on one moment."

**In Aircall:**
- Click "Transfer" button
- Select firm from dropdown (or dial intake number)
- Aircall bridges the call (3-way)

**When firm answers:**
- Brief intro: *"Hi, this is [Sasha/Davis] from Second Chair. I have [Lead Name] on the line. They were in an accident on [Date] in [City], [Injury Type], other driver at fault and insured. Transferring now."*
- Click "Complete Transfer" (drops you off call)

**If firm answers:**
- ✓ Transfer succeeded
- ✓ Bill $1,200 premium (automatically)
- ✓ Lead marked "transferred"

**If firm doesn't answer:**
- ✗ Transfer failed (firm unavailable)
- ✓ Still bill $1,200 premium (pay-per-transfer model)
- → Go to Step 5B

---

#### Step 5B: If QUALIFIED but Firm Unavailable

**Script:**  
> "Perfect — you have a strong case. [Firm Name] is currently with another client, but I'm sending them your information right now with a note that this is urgent. They'll call you back within 5 minutes. Keep your phone handy. Is [Phone Number] the best number to reach you?"

**After call:**
- Write detailed intake notes in lead record (see template below)
- Mark lead "URGENT - LIVE QUALIFIED" 
- Send immediate notification to firm
- Text lead: *"Thanks for speaking with me. [Firm Name] will call you at [Phone] within 5 minutes."*

**Billing:** Still $1,200 premium (you qualified the lead, firm just needs to call back)

---

#### Step 6: If DISQUALIFIED → Polite Decline

**Use appropriate script** (see `Intake_Qualification_Script.md` for full list):

**No injury:**  
> "Based on what you've told me, it sounds like you weren't injured in the accident. Without an injury, there typically isn't a personal injury case here. But I'd recommend following up with your insurance company about any property damage. Thanks for your time."

**Outside statute of limitations:**  
> "I appreciate you reaching out. Unfortunately, the accident was outside the time limit for filing a claim in your state. I wish we could help, but the deadline has passed."

**Already has attorney:**  
> "Got it. Since you're already working with an attorney, you'll want to continue with them. Best of luck with your case."

**After call:**
- Mark lead "disqualified"
- Add brief reason in notes
- No billing (disqualified leads are NOT billed)

---

### Intake Notes Template (Copy After Every Call)

**Paste this into lead record after call:**

```
PREMIUM QUALIFICATION CALL — [Date/Time]
Agent: [Sasha/Davis]
Duration: [MM:SS]

QUALIFICATION DECISION: [QUALIFIED / NEEDS REVIEW / DISQUALIFIED]

1. INJURY: [Yes/No] — [Type: back pain, broken arm, whiplash, etc.]
2. TREATMENT: [Yes/No] — [Location: ER/Hospital/Doctor/UC] — [Date if provided]
3. ACCIDENT DATE: [MM/DD/YYYY] — SOL: [Within/Close/Expired]
4. LIABILITY: [Other driver 100% / Shared / Unclear] — [Brief description]
5. INSURANCE: [Other driver insured: Y/N] — [Company] — [UM coverage: Y/N]
6. NARRATIVE: [1-2 sentence summary of what happened]
7. ATTORNEY STATUS: [None / Already has one]

STATE-SPECIFIC:
[FL/NY threshold met: Y/N] — [Details: fracture/hospitalization/permanent]
[PA/NJ tort status: Full/Limited/Unknown]
[DC/MD/VA fault: Other driver 100%? Y/N]

TRANSFER STATUS: [Successful / Firm unavailable / Did not attempt / Disqualified]

NOTES: [Any red flags, special circumstances, urgency factors]

NEXT ACTION: [Live transfer completed / Firm to call back within 5 min / Disqualified - no follow-up]
```

**Time required:** ~2 minutes to complete  
**When to do it:** Immediately after call, while fresh in memory

---

## Common Call Scenarios

### Scenario 1: Lead is Perfect Case → Transfer Succeeds

1. Lead answers, qualifies perfectly (clear injury, treatment, other driver 100% at fault, insured)
2. You: "Great — I'm connecting you with [Firm] right now."
3. Transfer to firm, firm answers
4. You give 10-second intro, drop off call
5. **Result:** Lead marked "transferred," $1,200 billed, done.

**Time:** 3-4 minutes total

---

### Scenario 2: Lead Qualifies but Firm is Unavailable

1. Lead answers, qualifies
2. You attempt transfer
3. Firm doesn't answer (phone rings, no pickup)
4. You: "Firm is with another client, they'll call you back in 5 minutes."
5. **After call:** Write detailed notes, mark "URGENT," notify firm
6. **Result:** $1,200 still billed (pay-per-transfer), firm calls back

**Time:** 4-5 minutes (longer notes)

---

### Scenario 3: Lead Disqualified (No Case)

1. Lead answers
2. Q1: "Were you injured?" → "No, just my car was damaged."
3. You: "Without an injury, there's no personal injury case. Contact your insurance for property damage."
4. End call politely
5. **Result:** Mark "disqualified," no billing, done.

**Time:** 1-2 minutes

---

### Scenario 4: Marginal Case (Needs Review)

1. Lead answers, describes soft-tissue injury in Florida (no-fault state)
2. No fracture, no hospitalization, ER visit only
3. Might not meet "permanent injury" threshold
4. You're unsure → Mark "NEEDS REVIEW"
5. **Result:** Deliver lead to firm with notes: "Marginal FL threshold, firm to review"
6. **Billing:** If you attempted qualification call: $1,200 (qualified with flag). If you think it's disqualified: No billing.

**Rule of thumb:** When in doubt, mark "qualified with review needed" and let firm decide. Don't over-disqualify.

---

### Scenario 5: Lead Doesn't Answer

1. Twilio dials lead
2. Rings, no answer or voicemail
3. Automated message plays
4. **Result:** Mark "no answer," no billing (no call completion)
5. Lead routes to standard delivery for firm to try

**Time:** 30 seconds

---

### Scenario 6: Lead is Rude or Hostile

1. Lead answers, immediately hostile: "Why are you calling me? I didn't ask for this!"
2. You: "I'm sorry for the confusion. You filled out a form on our website requesting information about your accident. If now's not a good time, no problem. Have a great day." (End call politely)
3. **Result:** Mark "declined contact," no billing

**Never argue or engage.** Just end the call professionally.

---

## Troubleshooting

### Problem: WhatsApp notification didn't arrive

**Check:**
- WhatsApp app open and connected to internet?
- Notifications enabled in phone settings?
- Availability toggle is ON in dashboard?

**Solution:**
- Restart WhatsApp app
- Check dashboard for missed leads (backup notification in admin)
- Verify phone number in settings

---

### Problem: Aircall isn't dialing the lead

**Check:**
- Aircall app logged in?
- Internet connection stable?
- Lead's phone number is valid (not missing digits)?

**Solution:**
- Restart Aircall app
- Try manual dial from Aircall using lead's phone number
- Check Twilio status page (status.twilio.com) for outages
- Contact Sasha/Davis (whichever one isn't you) to try

---

### Problem: Call recording didn't save

**Check:**
- Twilio recording enabled in call settings?
- Recording usually appears 1-2 minutes after call ends (not instant)

**Solution:**
- Wait 2-3 minutes, refresh lead page
- Check Twilio console directly (twilio.com/console)
- If still missing after 5 minutes, note in lead record: "Recording failed - technical issue"
- Contact engineering

---

### Problem: Transfer failed — firm's line was busy

**What happened:** Firm's phone system couldn't accept the transfer (line busy, voicemail, etc.)

**What to do:**
1. Tell lead: "The intake team is currently on another call. I'm marking this as urgent and they'll call you back within 5 minutes."
2. Write detailed intake notes
3. Send urgent notification to firm
4. **Billing:** Still $1,200 (you qualified the lead, firm's phone system issue isn't on you)

---

### Problem: Lead's story doesn't add up (fraud indicators)

**Red flags:**
- Story changes between answers
- Lead asks about "payout" or "settlement" before injury questions
- Coached answers (sounds like reading a script)
- Accident details are vague or inconsistent
- Lead admits they're calling multiple firms

**What to do:**
- Complete the call professionally
- Mark "disqualified" with note: "Possible fraud - [specific red flag]"
- No billing
- Notify firm in case they want to investigate

---

### Problem: I'm not sure if they meet the state threshold (no-fault)

**When in doubt:**
- Mark "qualified with review needed"
- Add detailed notes about the threshold question
- Let firm make final decision
- **Billing:** Yes, bill $1,200 (you did the qualification work)

**Examples:**
- FL: "Soft-tissue only, no fracture, ER visit only — may not meet permanent injury threshold. Firm to review."
- NY: "Neck pain, physical therapy for 8 weeks, no fracture — may not meet 90/180 rule. Firm to review."

**Rule:** We're not making legal determinations — we're qualifying leads per script. Marginal cases go to the firm with flags.

---

## Billing & Invoicing

### How Premium Surcharges Work

**Automatic billing:**
- When you complete a qualification call, system automatically creates a premium surcharge
- Human live transfer: $1,200 (over base lead price)
- No action needed from you — it's automatic

**Pay-per-transfer model:**
- You're billed for the qualified call whether transfer succeeds or not
- If you qualify a lead and firm is unavailable: Still $1,200
- If you qualify a lead and firm answers transfer: $1,200
- If lead doesn't answer your call: NOT billed (no call completion)
- If you disqualify the lead: NOT billed

**Weekly invoices:**
- Generated every Monday for previous week
- Sent to client automatically
- You don't need to do anything

---

### What Gets Billed vs. Not Billed

**BILLED ($1,200 premium):**
- ✓ Qualified call, transfer succeeded
- ✓ Qualified call, firm unavailable (warm handoff with notes)
- ✓ Qualified call, lead flagged "needs review"

**NOT BILLED:**
- ✗ Lead didn't answer
- ✗ Lead disqualified (no case)
- ✗ Lead declined contact (hung up immediately, hostile)
- ✗ Technical failure (your phone died, Twilio outage)

**If you're unsure:** Check with Sasha/Davis or mark lead for billing review.

---

### Checking Billing in Dashboard

**Go to:** `admin.2ndchair.net/billing/premium`

**You'll see:**
- This week's premium calls
- Qualification decision for each
- Billing status (billed / not billed / pending review)
- Premium amount ($1,200 per qualified call)

**If something looks wrong:**
- Flag for review
- Add note explaining the issue
- We review every Monday before invoices go out

---

## Performance Metrics (Your KPIs)

### What We're Tracking

**Call completion rate (target: >90%):**
- % of calls where lead answers
- If <90%: Might be phone number quality issue, not your fault

**Qualification accuracy (target: >85%):**
- % of qualified leads that firm accepts as viable cases
- If <85%: Review script adherence, might need re-training

**Average call time (target: 2-3 minutes):**
- Faster = good (efficient script)
- Slower = might be over-explaining or off-script

**Transfer success rate (target: >80% when firm available):**
- % of transfer attempts that connect to firm
- If <80%: Firm phone system issue, not your fault

**Conversion rate (target: 40-60% for live transfers):**
- % of qualified leads that sign retainer with firm
- Based on firm's reporting (not something you control directly)
- Used to validate that qualification is working

---

### Weekly Performance Email

**Every Monday you'll receive:**

```
Premium Nurturing Performance — Week of [Date]

YOUR STATS:
- Calls handled: 15
- Call completion rate: 93% (14 of 15 answered)
- Qualified: 12
- Disqualified: 2
- Average call time: 2:45
- Transfers attempted: 12
- Transfers succeeded: 10 (83%)

QUALIFICATION ACCURACY:
- Firm accepted: 11 of 12 qualified leads (92%)
- Firm feedback: "Excellent qualification, keep it up"

BILLING:
- Premium surcharges created: 12 × $1,200 = $14,400
- Total billed to clients this week: $14,400

GREAT WORK! 🎉
```

**Don't stress the numbers** — they're for optimization, not punishment. If something looks off, we'll work together to fix it.

---

## When to Escalate / Ask for Help

### Technical Issues

**Escalate if:**
- Twilio outage (calls won't go through)
- Aircall outage (can't dial)
- WhatsApp not delivering notifications consistently
- Recording system not working for multiple calls
- Admin dashboard is down

**Who to contact:** Engineering (via Slack #tech-support)

---

### Legal/Qualification Questions

**Escalate if:**
- You're unsure about state-specific threshold (no-fault, contributory negligence)
- Lead's case involves unusual circumstance (e.g., rideshare, commercial vehicle, DUI)
- Fraud indicators but not obvious
- Lead threatens legal action or demands to speak to "a lawyer"

**Who to contact:** Sasha + Davis (whoever isn't you), or legal review (for complex cases)

---

### Client/Firm Issues

**Escalate if:**
- Firm is consistently unavailable during stated hours
- Firm is rejecting qualified leads at >20% rate
- Firm complains about qualification quality
- Firm's intake line is disconnected or wrong number

**Who to contact:** Client success / account management

---

## Tips for Success

### Do's

✓ **Stick to the script** — it's tested and works  
✓ **Be empathetic** — these are real people in stressful situations  
✓ **Ask clarifying questions** — "Can you tell me more about that?"  
✓ **Take brief notes during call** — don't rely on memory  
✓ **Transfer confidently** — "I'm connecting you right now"  
✓ **Write detailed notes after marginal cases** — help the firm decide  
✓ **Turn availability OFF when truly unavailable** — don't miss calls  

---

### Don'ts

✗ **Don't give legal advice** — "You should sue them" → NO  
✗ **Don't promise outcomes** — "You'll get $50,000" → NO  
✗ **Don't over-disqualify** — When in doubt, let firm review  
✗ **Don't skip state-specific questions** — they're critical for no-fault states  
✗ **Don't argue with hostile leads** — just end the call politely  
✗ **Don't forget to write intake notes** — critical for firm follow-up  
✗ **Don't leave availability ON when you're not available** — leads will be lost  

---

## Quick Reference Card (Print & Keep at Desk)

```
╔══════════════════════════════════════════════════════╗
║   SECOND CHAIR PREMIUM NURTURING QUICK REFERENCE     ║
╚══════════════════════════════════════════════════════╝

7 CORE QUESTIONS:
1. Were you injured?
2. Did you see a doctor?
3. When did the crash happen?
4. Who was at fault?
5. Is the other driver insured?
6. Can you describe what happened?
7. Do you have an attorney already?

STATE-SPECIFIC ADD-ONS:
• FL/NY: Hospitalized? Broken bones? Permanent injury?
• PA/NJ: Full tort or limited tort?
• DC/MD/VA: Other driver 100% at fault?

QUALIFIED = Transfer or warm handoff → Bill $1,200
DISQUALIFIED = Polite decline → NO billing
NEEDS REVIEW = Flag for firm → Bill $1,200 with notes

TRANSFER SCRIPT:
"Great — I'm connecting you with [Firm] right now."

DECLINE SCRIPT (No injury):
"Without an injury, there's no PI case. Contact your 
insurance for property damage."

AVAILABILITY TOGGLE:
admin.2ndchair.net/availability

HELP/ESCALATION:
Tech: Slack #tech-support
Legal: Sasha/Davis
Client: Account management
```

---

## Training & Onboarding (New Agent Checklist)

If you're new to premium nurturing:

☐ **Read this manual cover to cover** (30 minutes)  
☐ **Read the qualification script** (`Intake_Qualification_Script.md`) (20 minutes)  
☐ **Watch 3 recorded sample calls** (good/bad examples) (30 minutes)  
☐ **Practice with role-play** — 5 mock calls with feedback (1 hour)  
☐ **Review state-specific criteria** for top 5 states (CA, FL, TX, NY, IL) (30 minutes)  
☐ **Shadow 3 live calls** (listen-only) (30 minutes)  
☐ **Supervised call #1-5** — Sasha/Davis listens in, provides feedback (1 hour)  
☐ **Solo call #6-10** — You're on your own, but reviewed afterward (1 hour)  
☐ **Certification** — You're cleared for unsupervised premium calls  

**Total training time:** ~6 hours spread over 2-3 days

---

## Updates & Version Control

**Current Version:** 1.0 (April 2026)

**This manual is a living document.** Updates will be made when:
- New states added to coverage
- Script changes (rare)
- New tools/systems implemented
- Client feedback requires process changes

**Check for updates:** First Monday of every month

---

*Second Chair — Premium Lead Nurturing — Operations Manual — April 2026*
