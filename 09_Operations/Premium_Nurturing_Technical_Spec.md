# Premium Lead Nurturing — Technical Specification

> **Type:** Technical Architecture & Implementation Guide
> **Status:** Implementation Ready
> **Date:** April 2026
> **Owners:** Engineering + Operations

---

## Overview

This document specifies the technical architecture, routing logic, and integration requirements for Second Chair's premium lead nurturing system. The system transforms standard web leads into AI-qualified or human-qualified live transfers through intelligent routing, real-time qualification, and multi-channel notification.

**Core Components:**
- Twilio Programmable Voice (call routing, recording, WhatsApp)
- Aircall (human agent interface, team management)
- Bland.ai or Vapi (AI voice agent)
- Supabase (lead database, routing rules)
- Next.js lead pipeline app (orchestration, billing)

---

## System Architecture

```
[Fair Case Web Form] 
        ↓
[Webhook → Lead Pipeline App]
        ↓
[Supabase: Create Lead Record]
        ↓
[Check nurturing_tier flag]
        ↓
    ┌───┴───┐
    ↓       ↓
[Standard] [Premium]
    ↓       ↓
[Deliver] [Route Premium]
```

### Premium Routing Flow

```
[Premium Lead Created]
        ↓
[Check SC Availability]
        ↓
    ┌───┴───┐
    ↓       ↓
  [OFF]   [ON]
    ↓       ↓
[Route    [Notify SC via WhatsApp]
 to Firm]     ↓
          [Wait 15s for Accept/Reject]
              ↓
          ┌───┴───┐
          ↓       ↓
      [ACCEPT] [REJECT/TIMEOUT]
          ↓       ↓
    [Twilio:  [Check Firm Availability]
     Call         ↓
     Lead]    ┌───┴───┐
          ↓   ↓       ↓
    [Qualify] [ON]  [OFF]
     Lead       ↓      ↓
          ↓  [Route  [Check AI Enabled]
    [Check   to         ↓
     Firm    Firm]  ┌───┴───┐
     Status]        ↓       ↓
          ↓      [YES]   [NO]
      ┌───┴───┐    ↓      ↓
      ↓       ↓  [Trigger [Standard
   [AVAIL] [UNAVAIL] AI]   Delivery]
      ↓       ↓      ↓
  [Transfer [Deliver [AI calls,
   Live]    w/Notes] qualifies,
      ↓       ↓     delivers]
  [Bill   [Bill      ↓
   $1200]  $1200] [Bill $200]
```

---

## Component 1: Twilio Programmable Voice

### Purpose
- Outbound calling to leads (human tier)
- Call recording and storage
- Live transfer routing (3-way bridge to firm)
- WhatsApp Business API notifications

### Setup Requirements

#### Account Configuration
```
Twilio Account SID: [From Twilio Console]
Auth Token: [From Twilio Console]
```

#### Phone Numbers
Purchase dedicated Twilio phone numbers for each major Market or use one national number.

**Recommended approach:** One national toll-free number
- **Format:** +1 (888) XXX-XXXX
- **Cost:** $2/month + $0.013/min usage
- **Benefits:** Single number for all outbound calls, professional appearance, call tracking

**Alternative:** Market-specific local numbers
- **Format:** Local area code per Market
- **Cost:** $1.15/month per number + $0.013/min
- **Benefits:** Local caller ID increases answer rate
- **Drawback:** Requires 50+ numbers for full coverage

#### TwiML Bin: Outbound Call Flow

Create TwiML Bin at `https://www.twilio.com/console/twiml-bins`

**Name:** `SC_Premium_Outbound_Call`

**TwiML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <!-- Two-party consent announcement (plays in CA, FL, IL, MD, MA, MI, MT, NH, OR, PA, WA) -->
  <Say voice="alice" language="en-US">
    This call may be recorded for quality assurance and training purposes.
  </Say>
  
  <Pause length="1"/>
  
  <!-- Connect to SC agent (Aircall or direct Twilio dial) -->
  <Dial
    timeout="30"
    record="record-from-answer"
    recordingStatusCallback="https://lead-pipeline.2ndchair.net/api/twilio/recording-status"
    recordingStatusCallbackEvent="completed"
  >
    <!-- Option A: Dial Aircall number (if using Aircall for agent interface) -->
    <Number>+1-XXX-XXX-XXXX</Number>
    
    <!-- Option B: Dial agent directly (if not using Aircall) -->
    <!-- <Number>+1-XXX-XXX-XXXX</Number> -->
  </Dial>
  
  <!-- If no answer, leave voicemail -->
  <Say voice="alice">
    We're sorry, but we're unable to connect your call at this time. 
    A representative from the law firm will call you back shortly. Thank you.
  </Say>
</Response>
```

#### TwiML Bin: Live Transfer (3-Way Bridge)

**Name:** `SC_Live_Transfer`

**TwiML:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <!-- SC agent already on call with lead -->
  <!-- Bridge to firm intake line -->
  <Say voice="alice">
    Please hold while I connect you with the intake team.
  </Say>
  
  <Dial
    timeout="30"
    action="https://lead-pipeline.2ndchair.net/api/twilio/transfer-status"
  >
    <!-- Firm intake line (from lead record) -->
    <Number>{{firm_intake_phone}}</Number>
  </Dial>
  
  <!-- If firm doesn't answer -->
  <Say voice="alice">
    The intake team is currently unavailable, but we've sent them your 
    information and they'll call you back within 5 minutes. Thanks for your patience.
  </Say>
</Response>
```

### API Integration (Next.js Lead Pipeline)

#### Initiate Outbound Call

**Endpoint:** `POST https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Calls.json`

**Request:**
```javascript
const twilio = require('twilio');
const client = twilio(accountSid, authToken);

async function initiateCallToLead(leadRecord) {
  const call = await client.calls.create({
    to: leadRecord.phone,  // Lead's phone number
    from: process.env.TWILIO_OUTBOUND_NUMBER,  // SC's Twilio number
    url: 'https://lead-pipeline.2ndchair.net/api/twilio/connect-agent',
    statusCallback: 'https://lead-pipeline.2ndchair.net/api/twilio/call-status',
    statusCallbackEvent: ['initiated', 'ringing', 'answered', 'completed'],
    record: true,
    recordingStatusCallback: 'https://lead-pipeline.2ndchair.net/api/twilio/recording-complete',
  });
  
  return call.sid;
}
```

#### Handle Live Transfer

**When SC agent clicks "Transfer" button in Aircall:**

```javascript
async function transferToFirm(callSid, firmIntakePhone) {
  // Update call to execute transfer TwiML
  await client.calls(callSid).update({
    url: `https://lead-pipeline.2ndchair.net/api/twilio/transfer?firm_phone=${firmIntakePhone}`,
    method: 'POST',
  });
}
```

### Call Recording Storage

**Recordings automatically saved to Twilio:**
- **Location:** `https://api.twilio.com/2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}`
- **Retention:** Set to 12 months in Twilio console
- **Cost:** $0.0025/min recording + $0.0005/min/month storage

**Webhook receives recording URL when complete:**

```javascript
// POST /api/twilio/recording-complete
export async function POST(req) {
  const { CallSid, RecordingSid, RecordingUrl, RecordingDuration } = await req.json();
  
  // Save to lead record in Supabase
  await supabase
    .from('leads')
    .update({
      call_recording_sid: RecordingSid,
      call_recording_url: RecordingUrl,
      call_duration: RecordingDuration,
    })
    .eq('twilio_call_sid', CallSid);
    
  return Response.json({ status: 'recorded' });
}
```

### WhatsApp Business API

**Purpose:** Notify Sasha/Davis of incoming premium leads in real-time

#### Setup
1. Apply for WhatsApp Business API access via Twilio
2. Register business profile: "Second Chair Lead Notifications"
3. Get WhatsApp-enabled Twilio number or use existing
4. Create message templates (WhatsApp requires pre-approved templates)

#### Message Template (Submit to WhatsApp for approval)

**Template Name:** `premium_lead_notification`

**Template Content:**
```
🚨 NEW PREMIUM LEAD

Name: {{1}}
Phone: {{2}}
City: {{3}}
Injury: {{4}}

Tap to Accept or Decline:
```

**With Interactive Buttons (Twilio ContentSID):**
```javascript
await client.messages.create({
  from: 'whatsapp:+14155238886',  // Twilio WhatsApp sender
  to: 'whatsapp:+1SASHAPHONE',    // Sasha's WhatsApp
  contentSid: 'HXXXXXXXXXXXXXX',  // Template SID from Twilio
  contentVariables: JSON.stringify({
    1: leadName,
    2: leadPhone,
    3: leadCity,
    4: leadInjuryType,
  }),
});
```

#### Alternative: Signal API (Self-Hosted)

If WhatsApp approval is slow or privacy concerns exist:

**Signal CLI via Docker:**
```bash
docker run -d \
  --name signal-cli \
  -v signal-data:/home/.local/share/signal-cli \
  bbernhard/signal-cli-rest-api:latest
```

**Send notification:**
```javascript
await fetch('http://localhost:8080/v2/send', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: `🚨 NEW PREMIUM LEAD\n\nName: ${name}\nPhone: ${phone}\nCity: ${city}\nInjury: ${injury}\n\nReply ACCEPT or DECLINE`,
    number: process.env.SASHA_PHONE,
    recipients: [process.env.SASHA_PHONE, process.env.DAVIS_PHONE],
  }),
});
```

**Pros:** Free, private, no approval needed  
**Cons:** Self-hosted, less reliable than Twilio, no interactive buttons

---

## Component 2: Aircall (Human Agent Interface)

### Purpose
- Provide user-friendly interface for Sasha/Davis to handle calls
- Team management, call queueing, mobile apps
- Call recording with 1-year retention
- Real-time call status and availability toggle

### Setup

#### Account & Plan
- **Plan:** Essentials ($30/user/month)
- **Users:** Sasha + Davis = $60/month
- **Features needed:**
  - Unlimited inbound calls
  - Call recording (1 year retention)
  - Mobile apps (iOS/Android)
  - Call tagging and notes
  - Integrations API

#### Phone Number
**Option A:** Use Twilio number, forward to Aircall
- SC's Twilio number → Aircall SIP trunk
- **Pros:** One phone system, Twilio handles all routing
- **Cons:** Adds complexity

**Option B:** Use Aircall number directly
- Get dedicated Aircall number for SC
- **Pros:** Simple setup
- **Cons:** Separate from Twilio (harder to integrate)

**Recommended:** Option A (Twilio → Aircall integration)

#### Integration with Supabase/Next.js

**Aircall API:** `https://api.aircall.io/v1`

**Get user availability status:**
```javascript
const aircall = require('aircall-everywhere')({
  apiId: process.env.AIRCALL_API_ID,
  apiToken: process.env.AIRCALL_API_TOKEN,
});

async function checkSCAvailability() {
  const users = await aircall.users.list();
  
  // Check if Sasha or Davis are "available" status
  const available = users.users.some(user => 
    (user.name === 'Sasha' || user.name === 'Davis') && 
    user.availability_status === 'available'
  );
  
  return available;
}
```

**Create call with custom data (lead info):**
```javascript
async function notifyAircallIncomingLead(leadData) {
  // Aircall "click-to-dial" API
  await aircall.calls.dialNumber({
    number: leadData.phone,
    userId: process.env.AIRCALL_USER_ID,  // Sasha or Davis
    customAttributes: {
      lead_id: leadData.id,
      lead_name: leadData.name,
      lead_city: leadData.city,
      lead_injury: leadData.injury_type,
    },
  });
}
```

**Aircall will show lead info in agent interface during call.**

#### Mobile App Setup
1. Install Aircall app on Sasha + Davis phones (iOS/Android)
2. Enable push notifications
3. Configure availability status sync (auto-off after hours)

---

## Component 3: Bland.ai (AI Voice Agent)

### Purpose
- Automated voice intake for 24/7 coverage
- Fallback when SC unavailable
- Lower-cost tier option for clients

### Setup

#### Account
- Sign up at `https://bland.ai`
- **Pricing:** $0.09/minute all-in (voice + transcription + AI)
- **API Key:** From Bland.ai dashboard

#### AI Agent Configuration

**Create agent via Bland.ai dashboard or API:**

**Agent Name:** "Second Chair MVA Intake Agent"

**System Prompt (Base Instructions):**
```
You are an intake specialist for Second Chair, a personal injury lead generation company. 
Your job is to qualify motor vehicle accident (MVA) leads by asking 7 core questions and 
determining if they have a viable case.

You should be:
- Empathetic and professional
- Efficient (keep call under 3 minutes)
- Clear and conversational
- Able to handle interruptions and clarifications

If the lead qualifies, tell them a lawyer will call them back shortly.
If they don't qualify, politely explain why and thank them for their time.

NEVER make legal promises or give legal advice.
```

**Intake Script (Conversational Prompt):**
```
[Use exact script from Intake_Qualification_Script.md]

Start by saying:
"Hi [Name], I'm calling from Second Chair about your recent car accident inquiry. 
I'd like to ask you a few quick questions to see if we can help. This will only 
take about 2 minutes. Is now a good time?"

Then ask these 7 questions in order:
1. Were you injured in the accident?
2. Did you see a doctor or get medical care?
3. When did the crash happen?
4. Who was at fault — you, the other driver, or both?
5. Is the other driver insured?
6. Can you briefly describe what happened?
7. Do you already have an attorney?

[State-specific add-ons based on lead's state - inject dynamically]

End by saying:
- If qualified: "Great — you have a strong case. A lawyer will call you back shortly. Keep your phone handy."
- If not qualified: "Thanks for the details. Based on what you've told me, this may not meet the legal requirements, but the firm will review and follow up if they can help."
```

**Structured Output Schema:**
```json
{
  "qualification_decision": "qualified | needs_review | disqualified",
  "questions": {
    "injury": "yes | no",
    "injury_type": "string",
    "treatment": "yes | no",
    "treatment_location": "hospital | er | urgent_care | doctor | none",
    "accident_date": "YYYY-MM-DD",
    "sol_status": "within | close | expired",
    "fault": "other_driver | shared | claimant | unclear",
    "insurance": "yes | no",
    "insurance_company": "string",
    "narrative_summary": "string (1-2 sentences)",
    "has_attorney": "yes | no"
  },
  "state_specific": {
    "threshold_met": "yes | no | unclear",
    "threshold_details": "string"
  },
  "next_action": "firm_callback | disqualified",
  "call_duration": "integer (seconds)",
  "red_flags": "array of strings"
}
```

### API Integration

**Initiate AI call:**

```javascript
const BLAND_API_KEY = process.env.BLAND_API_KEY;

async function triggerAIIntake(leadRecord) {
  const response = await fetch('https://api.bland.ai/v1/calls', {
    method: 'POST',
    headers: {
      'Authorization': BLAND_API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      phone_number: leadRecord.phone,
      task: `Qualify MVA lead for ${leadRecord.state}`,
      voice: 'maya',  // Professional female voice
      model: 'enhanced',
      max_duration: 5,  // 5 minutes max
      record: true,
      wait_for_greeting: true,
      language: 'en-US',
      
      // Inject lead-specific data
      variables: {
        lead_name: leadRecord.first_name,
        lead_state: leadRecord.state,
        state_specific_questions: getStateQuestions(leadRecord.state),
      },
      
      // Webhook for completion
      webhook: 'https://lead-pipeline.2ndchair.net/api/bland/call-complete',
    }),
  });
  
  const { call_id } = await response.json();
  
  // Save call_id to lead record
  await supabase
    .from('leads')
    .update({ ai_call_id: call_id })
    .eq('id', leadRecord.id);
    
  return call_id;
}
```

**Handle webhook when call completes:**

```javascript
// POST /api/bland/call-complete
export async function POST(req) {
  const {
    call_id,
    call_length,
    transcripts,
    variables,
    completed,
  } = await req.json();
  
  // Parse structured output from AI
  const qualification = variables.qualification_decision;
  const questions = variables.questions;
  
  // Update lead record with AI results
  await supabase
    .from('leads')
    .update({
      nurturing_status: 'ai_qualified',
      qualification_decision: qualification,
      intake_data: questions,
      call_transcript: transcripts,
      call_duration: call_length,
      ai_qualification_timestamp: new Date().toISOString(),
    })
    .eq('ai_call_id', call_id);
    
  // Deliver lead to firm with AI results
  await deliverLeadToFirm(call_id, 'ai_qualified');
  
  // Bill AI premium ($200)
  await createPremiumSurcharge(call_id, 'ai_qualified', 200);
  
  return Response.json({ status: 'processed' });
}
```

---

## Component 4: Supabase (Lead Database & Routing Rules)

### Database Schema Updates

**Add columns to `leads` table:**

```sql
ALTER TABLE leads ADD COLUMN IF NOT EXISTS nurturing_tier TEXT 
  CHECK (nurturing_tier IN ('standard', 'ai_qualified', 'human_live_transfer'));

ALTER TABLE leads ADD COLUMN IF NOT EXISTS nurturing_status TEXT
  CHECK (nurturing_status IN ('pending', 'sc_notified', 'calling', 'qualified', 'disqualified', 'transferred'));

ALTER TABLE leads ADD COLUMN IF NOT EXISTS qualification_decision TEXT
  CHECK (qualification_decision IN ('qualified', 'needs_review', 'disqualified'));

ALTER TABLE leads ADD COLUMN IF NOT EXISTS intake_data JSONB;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS twilio_call_sid TEXT;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS ai_call_id TEXT;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS call_recording_sid TEXT;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS call_recording_url TEXT;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS call_transcript TEXT;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS call_duration INTEGER;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS transfer_attempted BOOLEAN DEFAULT FALSE;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS transfer_succeeded BOOLEAN DEFAULT FALSE;
ALTER TABLE leads ADD COLUMN IF NOT EXISTS firm_connected_timestamp TIMESTAMPTZ;

ALTER TABLE leads ADD COLUMN IF NOT EXISTS premium_surcharge NUMERIC(10,2);
ALTER TABLE leads ADD COLUMN IF NOT EXISTS premium_billed BOOLEAN DEFAULT FALSE;
```

**Create `availability_status` table:**

```sql
CREATE TABLE availability_status (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id TEXT NOT NULL,  -- 'sasha' | 'davis' | 'team'
  is_available BOOLEAN DEFAULT FALSE,
  availability_hours JSONB,  -- { "monday": ["09:00", "18:00"], ... }
  auto_off_after_hours BOOLEAN DEFAULT TRUE,
  last_updated TIMESTAMPTZ DEFAULT NOW()
);

-- Insert default availability
INSERT INTO availability_status (user_id, is_available, availability_hours) VALUES
('team', FALSE, '{"monday": ["09:00", "18:00"], "tuesday": ["09:00", "18:00"], "wednesday": ["09:00", "18:00"], "thursday": ["09:00", "18:00"], "friday": ["09:00", "18:00"]}');
```

**Create `premium_surcharges` table (for billing):**

```sql
CREATE TABLE premium_surcharges (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  lead_id UUID REFERENCES leads(id),
  client_id UUID REFERENCES clients(id),
  surcharge_type TEXT NOT NULL,  -- 'ai_qualified' | 'human_live_transfer'
  amount NUMERIC(10,2) NOT NULL,
  billed BOOLEAN DEFAULT FALSE,
  invoice_id UUID,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Routing Logic Functions

**Check if premium routing should trigger:**

```javascript
async function shouldTriggerPremiumRouting(leadId) {
  // Get lead + client settings
  const { data: lead } = await supabase
    .from('leads')
    .select('*, client:clients(*)')
    .eq('id', leadId)
    .single();
    
  // Check if client has premium tier enabled
  if (!lead.client.premium_nurturing_enabled) {
    return { trigger: false, reason: 'client_not_enrolled' };
  }
  
  // Check tier
  const tier = lead.client.premium_tier;  // 'ai' | 'human' | 'hybrid'
  
  if (tier === 'standard') {
    return { trigger: false, reason: 'standard_tier' };
  }
  
  // Check SC availability (for human tier)
  if (tier === 'human' || tier === 'hybrid') {
    const scAvailable = await checkSCAvailability();
    
    if (!scAvailable && tier === 'hybrid') {
      // Fall back to AI
      return { trigger: true, route: 'ai' };
    }
    
    if (!scAvailable && tier === 'human') {
      // Route to firm (standard delivery)
      return { trigger: false, reason: 'sc_unavailable' };
    }
    
    if (scAvailable) {
      return { trigger: true, route: 'human' };
    }
  }
  
  if (tier === 'ai') {
    return { trigger: true, route: 'ai' };
  }
  
  return { trigger: false, reason: 'unknown' };
}

async function checkSCAvailability() {
  // Check Supabase availability_status table
  const { data } = await supabase
    .from('availability_status')
    .select('is_available, availability_hours')
    .eq('user_id', 'team')
    .single();
    
  if (!data.is_available) return false;
  
  // Check if within business hours
  const now = new Date();
  const day = now.toLocaleLowerCase('en-US', { weekday: 'long' });
  const hours = data.availability_hours[day];
  
  if (!hours) return false;
  
  const [start, end] = hours;
  const currentTime = now.toTimeString().slice(0, 5);  // "HH:MM"
  
  return currentTime >= start && currentTime <= end;
}
```

---

## Routing Logic Implementation (Lead Pipeline App)

### Webhook Entry Point

**Endpoint:** `POST /api/leads/ingest`

**Triggered by:** Fair Case form submission

```javascript
// app/api/leads/ingest/route.js
export async function POST(req) {
  const formData = await req.json();
  
  // 1. Create lead record in Supabase
  const { data: lead } = await supabase
    .from('leads')
    .insert({
      ...formData,
      nurturing_tier: formData.client_premium_tier || 'standard',
      nurturing_status: 'pending',
    })
    .select()
    .single();
    
  // 2. Check if premium routing should trigger
  const routing = await shouldTriggerPremiumRouting(lead.id);
  
  if (!routing.trigger) {
    // Standard delivery
    await deliverLeadStandard(lead);
    return Response.json({ status: 'delivered_standard' });
  }
  
  // 3. Route to premium tier
  if (routing.route === 'human') {
    await routeToHumanQualification(lead);
  } else if (routing.route === 'ai') {
    await routeToAIQualification(lead);
  }
  
  return Response.json({ 
    status: 'routed_premium',
    route: routing.route,
  });
}
```

### Human Tier Routing

```javascript
async function routeToHumanQualification(lead) {
  // 1. Update lead status
  await supabase
    .from('leads')
    .update({ nurturing_status: 'sc_notified' })
    .eq('id', lead.id);
    
  // 2. Send WhatsApp notification to Sasha + Davis
  await notifyAgentsViaWhatsApp(lead);
  
  // 3. Wait for accept/reject (15 seconds timeout)
  const accepted = await waitForAgentResponse(lead.id, 15000);
  
  if (!accepted) {
    // Timeout or reject → check firm availability
    const firmAvailable = await checkFirmAvailability(lead.client_id);
    
    if (firmAvailable) {
      // Route to firm (standard delivery)
      await deliverLeadStandard(lead);
      return;
    }
    
    // Firm also unavailable → AI fallback (if enabled)
    if (lead.client.ai_fallback_enabled) {
      await routeToAIQualification(lead);
    } else {
      // Standard delivery
      await deliverLeadStandard(lead);
    }
    
    return;
  }
  
  // 4. Agent accepted → initiate Twilio call
  await supabase
    .from('leads')
    .update({ nurturing_status: 'calling' })
    .eq('id', lead.id);
    
  const callSid = await initiateCallToLead(lead);
  
  await supabase
    .from('leads')
    .update({ twilio_call_sid: callSid })
    .eq('id', lead.id);
    
  // Call handling continues via Twilio webhooks...
}

async function notifyAgentsViaWhatsApp(lead) {
  const message = `
🚨 NEW PREMIUM LEAD

Name: ${lead.first_name} ${lead.last_name}
Phone: ${lead.phone}
City: ${lead.city}, ${lead.state}
Injury: ${lead.injury_type || 'Not specified'}

Accept or decline within 15 seconds:
${process.env.ADMIN_URL}/leads/${lead.id}/accept
  `.trim();
  
  // Send to Sasha
  await twilioClient.messages.create({
    from: `whatsapp:${process.env.TWILIO_WHATSAPP_NUMBER}`,
    to: `whatsapp:${process.env.SASHA_PHONE}`,
    body: message,
  });
  
  // Send to Davis
  await twilioClient.messages.create({
    from: `whatsapp:${process.env.TWILIO_WHATSAPP_NUMBER}`,
    to: `whatsapp:${process.env.DAVIS_PHONE}`,
    body: message,
  });
}

async function waitForAgentResponse(leadId, timeoutMs) {
  return new Promise((resolve) => {
    const startTime = Date.now();
    
    const checkInterval = setInterval(async () => {
      const { data } = await supabase
        .from('leads')
        .select('agent_response')
        .eq('id', leadId)
        .single();
        
      if (data.agent_response === 'accept') {
        clearInterval(checkInterval);
        resolve(true);
      }
      
      if (data.agent_response === 'reject' || Date.now() - startTime >= timeoutMs) {
        clearInterval(checkInterval);
        resolve(false);
      }
    }, 1000);  // Check every second
  });
}
```

### AI Tier Routing

```javascript
async function routeToAIQualification(lead) {
  // 1. Update lead status
  await supabase
    .from('leads')
    .update({ nurturing_status: 'ai_calling' })
    .eq('id', lead.id);
    
  // 2. Trigger Bland.ai call
  const callId = await triggerAIIntake(lead);
  
  // 3. AI completes via webhook (see Bland.ai section above)
  // Results processed in /api/bland/call-complete
}
```

### Live Transfer Logic

**Triggered when agent clicks "Transfer" in Aircall:**

```javascript
// POST /api/twilio/initiate-transfer
export async function POST(req) {
  const { lead_id, call_sid } = await req.json();
  
  // 1. Get firm intake phone from lead/client record
  const { data: lead } = await supabase
    .from('leads')
    .select('*, client:clients(*)')
    .eq('id', lead_id)
    .single();
    
  const firmPhone = lead.client.intake_phone;
  
  // 2. Update call to bridge to firm
  await transferToFirm(call_sid, firmPhone);
  
  // 3. Update lead record
  await supabase
    .from('leads')
    .update({
      transfer_attempted: true,
      nurturing_status: 'transferring',
    })
    .eq('id', lead_id);
    
  return Response.json({ status: 'transferring' });
}

// POST /api/twilio/transfer-status (webhook from Twilio)
export async function POST(req) {
  const { CallSid, DialCallStatus } = await req.json();
  
  const { data: lead } = await supabase
    .from('leads')
    .select('*')
    .eq('twilio_call_sid', CallSid)
    .single();
    
  if (DialCallStatus === 'completed') {
    // Firm answered, transfer succeeded
    await supabase
      .from('leads')
      .update({
        transfer_succeeded: true,
        firm_connected_timestamp: new Date().toISOString(),
        nurturing_status: 'transferred',
      })
      .eq('id', lead.id);
      
    // Bill human live transfer premium ($1,200)
    await createPremiumSurcharge(lead.id, 'human_live_transfer', 1200);
    
  } else {
    // Firm didn't answer
    await supabase
      .from('leads')
      .update({
        transfer_succeeded: false,
        nurturing_status: 'qualified_no_transfer',
      })
      .eq('id', lead.id);
      
    // Still bill premium (pay-per-transfer model)
    await createPremiumSurcharge(lead.id, 'human_live_transfer', 1200);
    
    // Deliver with detailed notes for callback
    await deliverLeadWithNotes(lead);
  }
  
  return Response.json({ status: 'processed' });
}
```

---

## Billing Integration

### Create Premium Surcharge

```javascript
async function createPremiumSurcharge(leadId, type, amount) {
  const { data: lead } = await supabase
    .from('leads')
    .select('client_id')
    .eq('id', leadId)
    .single();
    
  await supabase
    .from('premium_surcharges')
    .insert({
      lead_id: leadId,
      client_id: lead.client_id,
      surcharge_type: type,
      amount: amount,
      billed: false,
    });
    
  // Update lead record
  await supabase
    .from('leads')
    .update({
      premium_surcharge: amount,
      premium_billed: false,
    })
    .eq('id', leadId);
}
```

### Weekly Invoice Generation

**Cron job (runs every Monday at 9am):**

```javascript
// app/api/cron/generate-invoices/route.js
export async function GET(req) {
  // Verify cron secret
  if (req.headers.get('Authorization') !== `Bearer ${process.env.CRON_SECRET}`) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 });
  }
  
  // Get all unbilled premium surcharges from last week
  const oneWeekAgo = new Date(Date.now() - 7 * 24 * 60 * 60 * 1000);
  
  const { data: surcharges } = await supabase
    .from('premium_surcharges')
    .select('*, client:clients(*), lead:leads(*)')
    .eq('billed', false)
    .gte('created_at', oneWeekAgo.toISOString());
    
  // Group by client
  const byClient = surcharges.reduce((acc, s) => {
    if (!acc[s.client_id]) acc[s.client_id] = [];
    acc[s.client_id].push(s);
    return acc;
  }, {});
  
  // Generate invoice for each client
  for (const [clientId, clientSurcharges] of Object.entries(byClient)) {
    const invoice = await generateWeeklyInvoice(clientId, clientSurcharges);
    
    // Mark surcharges as billed
    const surchargeIds = clientSurcharges.map(s => s.id);
    await supabase
      .from('premium_surcharges')
      .update({ billed: true, invoice_id: invoice.id })
      .in('id', surchargeIds);
      
    // Send invoice email
    await sendInvoiceEmail(invoice);
  }
  
  return Response.json({ status: 'invoices_generated' });
}
```

---

## Admin Dashboard Features

### Availability Toggle

**UI Component:** `/dashboard/availability`

```tsx
// components/AvailabilityToggle.tsx
'use client';

export function AvailabilityToggle() {
  const [available, setAvailable] = useState(false);
  
  async function toggleAvailability() {
    const newStatus = !available;
    
    await fetch('/api/availability/toggle', {
      method: 'POST',
      body: JSON.stringify({ available: newStatus }),
    });
    
    setAvailable(newStatus);
  }
  
  return (
    <div className="availability-toggle">
      <label>
        <input 
          type="checkbox" 
          checked={available} 
          onChange={toggleAvailability}
        />
        Available for Premium Nurturing
      </label>
      
      {available && (
        <p className="status-active">
          ✅ You'll receive WhatsApp notifications for new premium leads
        </p>
      )}
    </div>
  );
}
```

**API Endpoint:**

```javascript
// app/api/availability/toggle/route.js
export async function POST(req) {
  const { available } = await req.json();
  
  await supabase
    .from('availability_status')
    .update({
      is_available: available,
      last_updated: new Date().toISOString(),
    })
    .eq('user_id', 'team');
    
  return Response.json({ status: 'updated' });
}
```

### Lead Detail View

**Show premium qualification data:**

```tsx
// app/dashboard/leads/[id]/page.tsx
export default async function LeadDetailPage({ params }) {
  const { data: lead } = await supabase
    .from('leads')
    .select('*')
    .eq('id', params.id)
    .single();
    
  return (
    <div>
      <h1>Lead: {lead.first_name} {lead.last_name}</h1>
      
      {lead.nurturing_tier !== 'standard' && (
        <section className="premium-details">
          <h2>Premium Qualification</h2>
          
          <p><strong>Tier:</strong> {lead.nurturing_tier}</p>
          <p><strong>Status:</strong> {lead.nurturing_status}</p>
          <p><strong>Decision:</strong> {lead.qualification_decision}</p>
          
          {lead.call_recording_url && (
            <audio controls src={lead.call_recording_url}>
              Your browser does not support audio playback.
            </audio>
          )}
          
          {lead.call_transcript && (
            <details>
              <summary>View Transcript</summary>
              <pre>{lead.call_transcript}</pre>
            </details>
          )}
          
          {lead.intake_data && (
            <details>
              <summary>View Intake Data</summary>
              <pre>{JSON.stringify(lead.intake_data, null, 2)}</pre>
            </details>
          )}
          
          {lead.premium_surcharge && (
            <p><strong>Premium Surcharge:</strong> ${lead.premium_surcharge}</p>
          )}
        </section>
      )}
    </div>
  );
}
```

---

## Environment Variables

**Required environment variables in `.env`:**

```bash
# Twilio
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxx
TWILIO_OUTBOUND_NUMBER=+18885551234
TWILIO_WHATSAPP_NUMBER=+14155238886

# Aircall
AIRCALL_API_ID=xxxxxxxxxx
AIRCALL_API_TOKEN=xxxxxxxxxxxxxxxxxxxx
AIRCALL_USER_ID_SASHA=123456
AIRCALL_USER_ID_DAVIS=123457

# Bland.ai
BLAND_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJxxx...
SUPABASE_SERVICE_KEY=eyJxxx...

# Notifications
SASHA_PHONE=+15551234567
DAVIS_PHONE=+15559876543

# Admin
ADMIN_URL=https://admin.2ndchair.net
CRON_SECRET=xxxxxxxxxxxxx

# Pricing
AI_PREMIUM_AMOUNT=200
HUMAN_PREMIUM_AMOUNT=1200
```

---

## Testing & QA

### Test Scenarios

#### Test 1: Human Tier - Successful Transfer
1. Submit test lead via Fair Case form
2. SC availability = ON, Firm availability = ON
3. WhatsApp notification sent to Sasha/Davis
4. Agent accepts within 15 seconds
5. Twilio calls lead
6. Agent qualifies lead (qualified)
7. Agent clicks "Transfer"
8. Firm answers, transfer succeeds
9. **Verify:**
   - Lead status = "transferred"
   - transfer_succeeded = TRUE
   - Premium surcharge created ($1,200)
   - Call recording saved
   - Intake notes populated

#### Test 2: Human Tier - Firm Unavailable
1. Submit test lead
2. SC availability = ON, Firm availability = OFF
3. WhatsApp notification sent
4. Agent accepts, calls lead, qualifies
5. Agent clicks "Transfer"
6. Firm does not answer
7. **Verify:**
   - Lead status = "qualified_no_transfer"
   - transfer_succeeded = FALSE
   - Premium surcharge still created ($1,200) — pay-per-transfer
   - Detailed notes delivered to firm for callback

#### Test 3: AI Tier - Qualified
1. Submit test lead
2. SC availability = OFF, AI enabled = TRUE
3. Bland.ai calls lead within 90 seconds
4. AI completes 7-question script
5. Lead qualifies
6. **Verify:**
   - Lead status = "ai_qualified"
   - AI transcript saved
   - Intake data structured JSON populated
   - Premium surcharge created ($200)

#### Test 4: Disqualified Lead - No Billing
1. Submit test lead with "no injury"
2. Either human or AI calls
3. Lead disqualified (no case)
4. **Verify:**
   - Lead status = "disqualified"
   - qualification_decision = "disqualified"
   - Premium surcharge NOT created
   - No billing

#### Test 5: Call Recording Compliance (Two-Party State)
1. Submit test lead from California
2. Human tier calls lead
3. **Verify:**
   - Automated announcement plays: "This call may be recorded..."
   - Recording starts after announcement
   - Recording URL saved to lead record

---

## Monitoring & Alerts

### Key Metrics to Track

**Operational:**
- Call completion rate (lead answers)
- Qualification rate (qualified / total calls)
- Transfer success rate (firm answers / transfer attempts)
- Average call duration
- SC availability uptime

**Financial:**
- Premium tier adoption rate (% of clients)
- Premium leads per week (by tier)
- Premium revenue per week
- Gross margin by tier

**Quality:**
- Qualification accuracy (firm accepts / SC qualifies)
- Conversion rate by tier
- Client satisfaction (NPS)

### Alerting (Supabase Edge Functions + Slack/Email)

**Alert Conditions:**
- SC availability OFF for >4 hours during business hours
- Call failure rate >20%
- Premium surcharge not created for qualified lead
- Twilio API error
- Bland.ai API error

---

*Second Chair — Premium Lead Nurturing — Technical Specification — April 2026*
