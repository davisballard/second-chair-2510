# Fair Case — Disclosure Requirements

**Version:** 1.0 — March 2026  
**Status:** Non-negotiable. Do not launch any ad or landing page without completing this checklist.  
**Source:** `03_Voice/Disclosure_Library.md`, FCC 2025 requirements, Meta Special Ad Category rules

---

## The Three Non-Negotiable Disclosures

Every Fair Case landing page and any ad creative where applicable must include these. They are not optional.

---

### 1. Advertising Disclosure

```
This is an advertisement for legal services.
```

**Placement:** Header or above the form  
**Visibility:** Must be readable — not hidden, not in 6pt gray text

---

### 2. Lead Generation Disclosure

```
You are not contacting an attorney directly. Your information will be 
shared with a participating law firm.
```

**Placement:** Near the form, visible before submission  
**Visibility:** Readable font size, decent contrast against background

---

### 3. Outcome Disclaimer

```
Past results do not guarantee future outcomes.
```

**Placement:** Footer, or near any settlement / dollar figure mentions  
**Use when:** Any mention of settlement amounts, case results, or the $33,700 gap statistic

---

## TCPA Consent Language (2025 Compliant)

### Standard Consent (Required on all Fair Case forms)

```
By submitting this form, I provide my express written consent to receive 
calls and/or text messages from [SPECIFIC NAMED FIRM] at the phone number 
provided, including via automated telephone dialing system or prerecorded 
voice. I understand that consent is not a condition of purchase. 
Message and data rates may apply.
```

**CRITICAL:** `[SPECIFIC NAMED FIRM]` must be the actual law firm name displayed on the form. Not "marketing partners," not "participating firms," not "one of our partners." One firm. One checkbox. One consent.

### Multi-Firm Dynamic Consent (When Multiple Firms May Contact)

```
I consent to receive calls and/or text messages from the following firms 
at the phone number provided:

☐ [Firm Name 1]
☐ [Firm Name 2]
☐ [Firm Name 3]

By checking the box(es) above, I provide my express written consent to be 
contacted by the selected firm(s), including via automated telephone 
dialing system or prerecorded voice. I understand that consent is not a 
condition of purchase. Message and data rates may apply.
```

**Requirements for multi-firm consent:**
- Checkboxes must be **unchecked by default** — never pre-checked
- Each firm is a separate, individually labeled checkbox
- Firm names must be the actual bidding entities — no placeholder names
- Consent visible **above the submit button** — not below, not in a modal

---

## Placement Rules

### Required Above the Fold / Clearly Visible
- "This is an advertisement" → Header or above form
- TCPA consent checkbox → **ABOVE the submit button**
- Privacy policy link → Near form, accessible

### Acceptable in Footer
- "Past results do not guarantee future outcomes"
- Full privacy policy link
- Additional legal disclosures

### NOT Acceptable (Will Create Compliance Risk)
- Consent placed below the submit button
- Disclosures revealed only in modals or popups
- Disclosures hidden in terms pages nobody reads
- Gray text on light gray background
- Font size smaller than 8pt

---

## Consultation Language (Correct Wording)

**Free Consultation — What to Say:**
```
No upfront cost to speak with an attorney.
```

Do NOT use: "100% free" or "completely free" — these overstate what can be guaranteed.

**No Guarantee of Representation:**
```
A free consultation does not guarantee representation.
```

Use this whenever offering "free case evaluation."

---

## Technical Requirements (Non-Negotiable)

### TrustedForm

- **Mandatory on all Fair Case lead forms**
- Must capture full session replay of the consent moment
- Certificate must show the specific firm name visible at the time of consent
- Retain all certificates for minimum 5 years
- A lead without a TrustedForm certificate is a lead that cannot be defended in court. Do not deliver uncertified leads.

### Jornaya LeadiD

- **Mandatory for audit trail**
- Bot detection
- Consent verification
- Required for any court-admissible lead documentation

---

## State-Specific Requirements

Some states require additional disclosures beyond the federal/FCC baseline. Before launching in any new state, verify against the state bar advertising rules.

**High-enforcement states (additional diligence required):**
- **California** — State Bar Rules 7.1–7.5: specific requirements around advertising claims, "testimonials," and attorney identification
- **Texas** — High enforcement on advertising claims and disclaimer placement
- **Florida** — Specific requirements on "no fee unless we win" language and solicitation rules
- **New York** — Specific requirements on attorney advertising format and content

**Reference:** `05_Restrictions/` for state-by-state full rules. Before launching in any new state, read the relevant state bar advertising rules in full.

---

## Ad-Level Disclosure Requirements

### Meta Ads

Meta Special Ad Category designation requires that Fair Case:
- Does not use demographic targeting (age, gender, income)
- Does not use interest or behavioral targeting
- Uses geographic targeting only (Market / city / zip)
- Includes "This is an advertisement" language accessible via ad transparency tools

Note: Meta's ad library makes all Fair Case ads publicly visible. Write copy as if anyone — including opposing counsel, state bar investigators, and journalists — can read it. Because they can.

### Instagram / Facebook Creative

- "Sponsored" label is automatically applied by Meta to paid posts
- Additional "This is an advertisement" language should appear on the landing page, not necessarily in the ad creative itself (unless required by state bar rules for the specific state)
- Any settlement figures used in creative must be qualified as: "Settlements in similar cases have ranged from $X to $Y. Past results do not guarantee future outcomes."

---

## Pre-Launch Compliance Checklist

Complete before any Fair Case ad or landing page goes live.

### Landing Page / Quiz
- [ ] "This is an advertisement for legal services" visible above the form
- [ ] Lead gen disclosure present ("You are not contacting an attorney directly...")
- [ ] TCPA consent checkbox **above** the submit button
- [ ] Checkboxes unchecked by default
- [ ] Specific firm names shown (not "partners" or placeholder names)
- [ ] Privacy policy link visible and accessible
- [ ] TrustedForm active and capturing
- [ ] Jornaya LeadiD active
- [ ] All text readable: 8pt minimum, good contrast ratio
- [ ] "Past results" disclaimer near any settlement figure mentions
- [ ] State-specific disclosures reviewed and applied

### Ad Creative
- [ ] No "you" + injury/condition language (see `COPY_VOICE_GUIDE.md`)
- [ ] No guaranteed dollar amounts
- [ ] No manufactured urgency without a real legal basis
- [ ] No actors presenting as real clients
- [ ] No crash footage or dramatized accident imagery
- [ ] If settlement figures are used: qualified with "similar cases have ranged from..."
- [ ] State-specific SOL figure is accurate for the state where the ad runs (Tier 3 only)
- [ ] Copy reviewed against the banned phrases list

### Intake Routing
- [ ] TrustedForm certificate generation confirmed functional
- [ ] Firm names on consent form match the actual firm receiving the lead
- [ ] Lead routing tested and verified before spend goes live

---

*Source: `03_Voice/Disclosure_Library.md`, Saul (Legal Compliance agent), FCC 2025, Meta Special Ad Category requirements*  
*Review any state-specific disclosures against current state bar rules before launch — advertising regulations change.*
