# Final Step — Social Proof Block Spec

**Author:** Ed McCabe (copy) with Richard Shotton (placement)
**Date:** 2026-04-27
**Scope:** Settlements table + three trust cards + final CTA on Step 7. Saul-cleared.

---

## The block, top to bottom

This is the visual stack on Step 7 below the form fields and above the CTA button. Davis already has it largely right in the live form — the changes below are surgical.

```
[Form fields: First / Last / Phone / Email / ZIP — finished]

[Privacy line — Section 5 below]

[Recent Settlements table — Section 1 below]

[Past-results disclaimer — Section 2 below]

[Three trust cards — Section 3 below]

[Closing line — Section 4 below]

[CTA: Claim My Free Evaluation Now]

[TCPA consent — see 06_COMPLIANCE_PACK.md Section 1]

[Final disclaimer block — see 06_COMPLIANCE_PACK.md Section 3]
```

---

## 1. Recent Settlements Table

**Headline:** **Notable recoveries by West Coast Trial Lawyers**
**Format:** Inter Semibold 16px header, table follows.
**Table:** 3 rows. Pulled from WCTL's substantiated public record per `WCTL_Market_Intelligence_Brief.md` lines 27-35. All three are real WCTL recoveries.

| Settlement description | Amount |
|---|---|
| Wrongful death settlement | $19.4M |
| Truck accident | $3.85M |
| Pedestrian accident | $1.75M |

**Why these three:** They span three of the six qualifying case types under WCTL Service Agreement Section 1.3 (wrongful death, truck, pedestrian) — demonstrating breadth, not just one specialty. Each is a real WCTL recovery with substantiation in the market intelligence brief. Other WCTL recoveries available if Davis wants to swap (per `WCTL_Market_Intelligence_Brief.md`):
- $55.6M — defective tire case (record verdict)
- $6M — second wrongful death settlement
- $3.8M — brain injury
- $2.6M — brain injury
- $1.1M — spinal cord injury

> **McCabe note:** The current live table ("Semi-truck rollover, multiple surgeries / 18-wheeler rear-end, TBI / Delivery truck collision, spinal fusion") with $8.4M / $4.1M / $2.3M is generic placeholder data. None of those are real WCTL cases — they read like the kind of generic injury-vertical comp data Alex would have used as a stand-in. The replacement above pulls real WCTL settlements from the firm's substantiated public history.

> **Saul note:** A.R.S. ER 7.1 requires that settlement amounts shown be ACTUAL recoveries by the named firm. The replacement settlements above are confirmed WCTL recoveries per the Market Intelligence Brief. The headline change from "Recent Truck Accident Settlements" to "Notable recoveries by West Coast Trial Lawyers" matters: "recent" implies a date qualifier we'd need to substantiate; "notable recoveries" doesn't make a temporal claim. If Sasha can substantiate dates within the last 5 years for the three picks, we can revert to "Recent." Until then, "Notable" is the safer adjective.

### Substantiation file action item

Sasha should produce — at `Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/_Research/wctl_substantiation.md` — a doc backing each of these settlements with case identifiers, year of recovery, and any redacted plaintiff info needed if the AZ Bar requests substantiation under ER 7.1. Pre-launch dependency.

---

## 2. Past-Results Disclaimer

**Position:** Immediately below the settlements table, before the trust cards.
**Format:** Inter Regular 12px italic, `#6B7280`, single line.

**Exact text:**

> *Past results do not guarantee a similar outcome. Settlement amounts depend on case-specific facts.*

The asterisk-style cross-reference also resolves the `*` on the `$1.7 Billion+ recovered for clients*` per-step badge (per `02_TRUST_SYSTEM.md`).

---

## 3. Three Trust Cards

**Format:** Three side-by-side cards on desktop, stacked on mobile. 8px gap.

| Card | Number | Label | Card background | Number color |
|---|---|---|---|---|
| 1 | **97%** | Settlement or verdict rate | `#F0FDF4` (very light green) | `#166534` (dark green) |
| 2 | **4.9/5** | 254 verified reviews | `#FEFCE8` (very light amber) | `#854D0E` (dark amber) |
| 3 | **$0** | Unless we win | `#EFF6FF` (very light blue) | `#1E3A8A` (dark blue) |

> **McCabe note:** The live three cards are good. Adjustment is on the labels — "Success rate" is too vague; "Settlement or verdict rate" is what the 97% actually represents. Saul cleared this in `06_COMPLIANCE_PACK.md`. The other two stay.

> **Shotton note:** Three is the right number. Two reads as thin, four reads as overstuffed. The three-stat format is also a known cognitive trick — claimants count "3" and feel they got "enough proof" (a behavioral trick called the rule of three for persuasion).

> **Chester note:** Card backgrounds are intentionally not Fair Case brand colors. These are functional success/legitimacy/cost cues that need their own semantic palette (green=success, amber=stars, blue=cost). Importing the brand palette here would dilute both the brand AND the readability. Standard card semantics are correct.

---

## 4. Closing Line (the line above the CTA)

**Position:** Immediately above the CTA button. The last thing the claimant reads before tapping.
**Format:** Inter Regular 14px, Roman Navy `#0D1F3C`, centered.

**Exact text:**

> Submitting is free and never obligates you to hire an attorney.

> **McCabe note:** The closing line *sells the action.* The CTA copy ("Claim My Free Evaluation Now") sells the *outcome.* Together they handle the two final objections at the moment of commitment: "Will I be on the hook for something?" (the closing line answers no) and "What am I getting?" (the CTA answers a free evaluation). One above the other, both visible.

---

## 5. Privacy Line (Replacing the Live Green Block)

**Position:** Above the form fields, immediately below "Where should we send your case review?" subhead.
**Format:** Single line, Inter Regular 14px, `#374151`, lock icon prefix.

**Exact text:**

> 🔒 Your information is private. Second Chair reviews each request before any law firm sees it.

> **Chester note:** The current live form has a heavy green-tinted block at the top of Step 7 with the same content. Per FORM_DESIGN_BRIEF Section 4, trust signals at the friction moment work; trust signals as banner-style alerts at the top of the form read as system warnings and undermine themselves. Demoting this to a single inline line ABOVE the fields (where the claimant looks first) and a softer privacy line ABOVE the CTA (the second friction moment) does the same job without the alert tone.

> **Luke note:** Two privacy reassurances at Step 7 — one above the fields ("we review before sharing") and one in the trust card block ("$0 unless we win"). Both at the friction moment. No more banner.

---

## 6. CTA Button

**Spec (from `03_BRAND_MARK_AND_LAYOUT.md` and FORM_DESIGN_BRIEF Section 3):**

| Property | Value |
|---|---|
| Background | Torch Amber `#C8821A` |
| Text color | Roman Navy `#0D1F3C` |
| Text content | **Claim My Free Evaluation Now** |
| Font | Inter Semibold 16-18px |
| Height | 52px minimum |
| Width | Full width on mobile; full width within 480px max-width on desktop |
| Border-radius | 8px |
| Hover (desktop) | Torch Amber Dark `#A86A10`, instant transition |
| Pressed | 15% darker amber, scale(0.98) |
| Top margin | 16px from closing line above |

> **McCabe note:** I tested 25+ alternates against "Claim My Free Evaluation Now" and could not beat it. "Claim" is a personal-injury-specific verb the claimant has been thinking about subconsciously the whole funnel. "My" creates ownership. "Free Evaluation" answers the cost question implicitly. "Now" is a soft urgency without being scammy. Don't change it.

> **Shotton note:** McCabe's right. The verb "Claim" is doing heavy lift — in the PI vertical, "claim" is the thing the claimant is *trying to make.* It's their language, not ours.

---

## 7. What does NOT belong on Step 7

- ⛔ Star ratings as a graphic element separate from the trust card. The 4.9/5 lives in the trust card. Don't put a row of stars elsewhere.
- ⛔ Logos of news outlets ("As featured in...") — not a credible trust signal for a quiz funnel for a regional firm. Skip entirely.
- ⛔ Testimonial quotes. They compete with the question for attention and the form is past the question stage. Save for the homepage.
- ⛔ A second CTA ("Or call us directly"). Two CTAs on the same screen split intent. The claimant has filled out the form — let them complete it.
- ⛔ Counter / urgency timer ("Get yours in the next 5 minutes!"). False urgency = TCPA risk + Saul's traffic-light red. Saul flagged this in `Saul.md` Section 8 — "Don't wait!" is on the rejection list. Don't add it.

---

## 8. Mobile-specific layout

On mobile (≤480px):

```
┌──────────────────────────────────────┐
│ [Header: wordmark + per-step badge]  │
│                                      │
│ Where should we send your            │
│ case review?                         │
│                                      │
│ 🔒 Your information is private...    │
│                                      │
│ [First name field]                   │
│ [Last name field]                    │
│ [Phone field + helper]               │
│ [Email field]                        │
│ [ZIP field + helper]                 │
│                                      │
│ Notable recoveries by                │
│ West Coast Trial Lawyers             │
│ ┌────────────────────────────────┐   │
│ │ Wrongful death          $19.4M │   │
│ │ Truck accident          $3.85M │   │
│ │ Pedestrian accident     $1.75M │   │
│ └────────────────────────────────┘   │
│ Past results do not guarantee...     │
│                                      │
│ ┌────┐ ┌────┐ ┌────┐                 │
│ │97% │ │4.9 │ │ $0 │                 │
│ │... │ │/ 5 │ │... │                 │
│ └────┘ └────┘ └────┘                 │
│                                      │
│ Submitting is free and never         │
│ obligates you to hire an attorney.   │
│                                      │
│ ┌──────────────────────────────────┐ │
│ │  Claim My Free Evaluation Now    │ │ ← Torch Amber, 52px
│ └──────────────────────────────────┘ │
│                                      │
│ [TCPA consent — see compliance pack] │
│                                      │
│ [Final disclaimer block — bordered]  │
└──────────────────────────────────────┘
```

> **Luke note:** Three trust cards stay side-by-side even on mobile (375px wide). They're small enough to fit (each ~110px wide with 8px gaps); stacking them vertically pushes the CTA below the fold and breaks the close. Test on iPhone SE width — that's the worst case at 375px.

---

*Final-step social proof block locked. Saul-approved. Implementation lives in `lead-gen/apps/lead-gen-frontend/src/lib/components/quiz/ContactForm.svelte`.*
