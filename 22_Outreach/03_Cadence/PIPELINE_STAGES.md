# Pipeline Stages

> **Purpose:** Standard stage definitions for tracking every prospect. Configure CRM to match these exactly.
> **Updated:** March 24, 2026

---

## Stages

| Stage | Definition | Owner | Max Time Before Action |
|-------|-----------|-------|----------------------|
| **Cold** | Identified but not yet contacted | Sasha | Move to Contacted within 1 week of adding |
| **Contacted** | First email or LinkedIn request sent | Sasha | Auto-advances based on sequence |
| **Opened** | Email opened (if tracked), no reply | Sasha | Sequence continues automatically |
| **Responded** | Any reply received (positive, negative, neutral) | Sasha | Respond within 2 hours (business hours) |
| **Call Scheduled** | Discovery call booked | Sasha | Prep 24 hours before call |
| **Call Completed** | Discovery call done, awaiting follow-up | Sasha | Send Attorney Pitch within 1 hour |
| **Proposal Sent** | Attorney Pitch doc sent | Sasha | Follow up within 3 business days |
| **Negotiating** | Active discussion on pilot terms | Sasha + Davis | Close within 2 weeks or re-qualify |
| **Signed** | Client signed, pilot begins | All | Hand off to onboarding |
| **Lost** | Declined or went cold after engagement | Sasha | Log reason, move to Nurture if appropriate |
| **Nurture** | Said "not now" — re-engage later | Sasha | Re-engage in 60-90 days with new angle |

---

## Stage Transition Rules

**Cold → Contacted:** First email sent or LinkedIn connection request sent.

**Contacted → Responded:** Any reply received. Negative replies ("not interested") also count — log the reason before moving to Lost.

**Responded → Call Scheduled:** Prospect agrees to a call. Must have specific date/time confirmed.

**Call Completed → Proposal Sent:** Only after discovery call is done AND Sasha determines the prospect is qualified. If not qualified, move directly to Lost with notes.

**Proposal Sent → Negotiating:** Prospect engages with the pitch doc — asks questions, requests changes, discusses terms.

**Negotiating → Signed:** Contract/agreement executed. Pilot terms confirmed.

**Any Stage → Lost:** Prospect explicitly declines, goes unresponsive after 3+ touches post-engagement, or is disqualified.

**Lost → Nurture:** Only if the prospect said "not now" or "bad timing" (not "not interested"). Re-engage in 60-90 days with a new angle or trigger event.

---

## CRM Configuration Notes

- Every prospect must have: firm name, contact name, title, email, tier (1/2/3), persona, DMA, current stage
- Log every touch: date, channel (email/LinkedIn/phone), type (outreach/follow-up/call), notes
- Tag prospects by source: SpyFu, Best Lawyers, Google Maps, Avvo, referral, inbound
- Weekly pipeline report: count by stage, conversion rates stage-to-stage, average time in stage
