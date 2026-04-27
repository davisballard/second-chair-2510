# Compliance Pack — Final Copy + Placement Spec

**Author:** Saul (Chief Compliance Officer)
**Date:** 2026-04-27
**Reviewers:** Ed McCabe (copy), Luke Wroblewski (placement)
**Scope:** Every regulated word and every required element on the Fair Case quiz form, with WCTL Arizona overlay. Locks the language; locks the placement.

> **Saul:** Look — I'm gonna walk you through the non-negotiables. Each block has the exact text, the exact placement, and the exact font size. If your developer wants to "tighten this up" or "make it cleaner," the answer is no. Tightening this up is how class-action lawyers send their kids to college.

---

## 1. TCPA Consent Text — The One That Matters

**Effective date:** Used for every WCTL Arizona quiz submission starting at WCTL pilot launch.

**Placement:** Above the submit button on Step 7 (contact step). Visible without scrolling on mobile. **Not** in a Terms link, not in a modal, not below the button. Not collapsed into a "show consent text" expander.

**Format:** Inter Regular 13px (non-negotiable floor), color `#374151` (Body Gray, not muted gray — it must be readable). Single paragraph. No checkbox required (per FORM_DESIGN_BRIEF Section 4 — the button click constitutes consent when the language and placement are correct).

**Exact text (locked):**

> By clicking "Claim My Free Evaluation Now," I authorize Second Chair through getafaircase.com to share my request with **West Coast Trial Lawyers**, the law firm that serves my ZIP code. I authorize West Coast Trial Lawyers and its intake team to call and text me at the phone number I provided, including via automated dialing or prerecorded messages. Consent is not required to receive legal services. Message and data rates may apply. Submitting this form does not create an attorney-client relationship.

> **Saul:** See "West Coast Trial Lawyers" in there? That's the named entity. That's not a placeholder. That's not "our marketing partners." That's the actual firm. The TrustedForm video has to show those exact words on the user's screen at the moment they hit Claim. If the certificate shows "the law firm that serves my ZIP code" without naming WCTL, you just gave a class-action attorney the smoking gun.

**Code change:** `lead-gen/apps/lead-gen-frontend/src/lib/quiz-config.ts` — `buildTcpaConsentText({ advertiserName: "West Coast Trial Lawyers" })` for AZ traffic. The current default `DEFAULT_TCPA_ADVERTISER_NAME = "Second Chair through getafaircase.com"` is wrong for one-to-one consent — Second Chair is the platform/aggregator, but the consent must name the receiving firm. Two-name format above (Second Chair + WCTL named explicitly) satisfies both: the platform is identified AND the contacting entity is named.

---

## 2. Required Disclosures (Every Step)

These appear in the form **footer**, persistent across all 7 steps + the contact step. Inter Regular 12px, `#6B7280` (Form Gray Light). Visible without scrolling on mobile.

**Exact text (locked):**

> *Get A Fair Case is operated by Second Chair. The receiving law firm appears on the consent step before you submit.*

**Replace** the live "Get A Fair Case is operated by Second Chair. The receiving law firm, if one is identified, appears after ZIP review on the consent step." — current text says "if one is identified" which contradicts WCTL Arizona reality (a firm IS always identified for AZ ZIPs in this pilot). The cleaner version above tells the truth.

> **Saul:** "If one is identified" was hedge language for the period when we hadn't lined up firms in every market. WCTL Arizona is locked exclusive (Section 2.1). Every Arizona ZIP returns West Coast Trial Lawyers. The conditional language is now misleading — drop it.

---

## 3. Final-Step Disclaimer Block

This is the bordered paragraph immediately under the CTA button on Step 7.

**Format:** Inter Regular 13px, `#6B7280`, single bordered block (1px solid `#E5E7EB`, 12px padding, 8px border radius, 8px margin from CTA above).

**Exact text (locked):**

> This is an attorney advertisement. Submitting this request is free and does not require you to hire a lawyer. Statutes of limitations apply to all cases. Past results do not guarantee a similar outcome. West Coast Trial Lawyers is the law firm that may contact you and is solely responsible for any legal services it provides. Second Chair operates the Get A Fair Case intake platform and is not a law firm.

**What this covers:**
- "This is an attorney advertisement." — required by every state that has a labeling rule (NY explicit, others advisory; AZ best practice)
- "Past results do not guarantee a similar outcome." — required when settlement amounts are shown elsewhere on the page (the table above the CTA shows them) — A.R.S. ER 7.1(b) substantiation
- "Statutes of limitations apply to all cases." — universal advisory, defends against claimants alleging "you didn't tell me my case was time-barred"
- "West Coast Trial Lawyers is the law firm... solely responsible for any legal services" — Section 5.1(d) qualification of provider/firm relationship; protects Second Chair from being construed as practicing law
- "Second Chair operates the Get A Fair Case intake platform and is not a law firm." — required Lead Generator vs. Lawyer Referral Service line per `04_State_Bar_Rules.md` Section 1; Texas Rule 7.01 analogue applies in spirit even though we're in Arizona

> **Saul:** The current live disclaimer says "This is an advertisement. Statutes of limitations apply. Submitting this request does not create an attorney-client relationship or guarantee representation." Two problems: (1) it doesn't name WCTL, which is the firm we're advertising for, (2) "an advertisement" is weaker than "an attorney advertisement" — the latter is the explicit phrase NY Rule 7.1 requires and AZ ER 7.1 implies. The version above passes both gates.

---

## 4. Settlement Amount Disclaimer (Step 7 only)

The Recent Settlements table shows three line items with dollar amounts. Below the table, before the CTA:

**Format:** Inter Regular 12px, `#6B7280`, italic.

**Exact text (locked):**

> *Past results do not guarantee a similar outcome. Settlement amounts shown reflect historical recoveries by the law firm and depend on case-specific facts.*

**Why:** A.R.S. ER 7.1(b) requires that if past results are presented, they include a disclaimer that prevents an unjustified expectation. The "and depend on case-specific facts" tail handles the substantiation requirement.

> **Saul:** This is the language ABA Model Rule 7.1 Comment [3] specifically calls out. It's also the language that survived 411 Pain in Florida and the various California settlement-claim cases. Don't try to be clever — use the boilerplate.

---

## 5. Phone Field Helper (TCPA Reinforcement)

Below the phone number field on Step 7. Inter Regular 13px, `#6B7280`.

**Exact text (locked):**

> *A specialist from West Coast Trial Lawyers will call within one business day. If they're not the right fit, that's the end — no follow-up calls.*

> **Saul:** This is McCabe's copy and it's actually compliant — note "A specialist from West Coast Trial Lawyers" (named entity, not "a representative" or "our team"). The "no follow-up calls" line is your shield against the TCPA "we got 17 calls in 4 days" complaint. If you say it here AND honor it on the back end, the disclosure is its own defense.

---

## 6. The "Not a Law Firm" Identification

Required by Texas Rule 7.01 spirit and best practice across all states (including AZ ER 7.5 trade name rules). Lives in the final disclaimer block (Section 3 above), the line: *"Second Chair operates the Get A Fair Case intake platform and is not a law firm."*

**Saul's Lead Generator vs. Lawyer Referral Service test:**

| Phrase | Verdict | Why |
|---|---|---|
| "Connect with a participating attorney" | ✅ Lead Generator | mechanical, non-discretionary |
| "Match you with the law firm that serves your ZIP code" | ✅ Lead Generator | ZIP-based mechanical matching |
| **"We'll match you with the best lawyer for your case"** | ❌ Lawyer Referral Service | implies discretionary selection |
| "Free case evaluation" | ✅ neutral | doesn't imply matching |
| "We review your case to find the right attorney" | ❌ Lawyer Referral Service | "review" + "find the right" = case analysis |

**Live form check:** The current consent text says "may review my request for a free case evaluation and match me with the law firm that serves my ZIP code after a quick review." That "match me with the law firm that serves my ZIP code" is a mechanical, non-discretionary connection — passes the test. The "after a quick review" is the gray-zone phrase. Keep this language as ZIP-based mechanical matching only; never expand into "review your case."

---

## 7. AZ ER 7.1 Specific (See Also `WCTL_AZ/03_AZ_COMPLIANCE.md`)

Arizona Rules of Professional Conduct ER 7.1, 7.3, 7.5 govern this. Headlines that apply to the form:

- **ER 7.1 (false or misleading communication):** No "best lawyer," no guarantees, no unsubstantiated comparisons. The form complies.
- **ER 7.3 (solicitation):** Direct solicitation of a known accident victim is restricted. Inbound quiz fills are *requested* contact, not solicitation — the form is initiated by the claimant. Compliant.
- **ER 7.5 (firm names and letterheads):** Trade names are restricted to non-misleading uses. "Get A Fair Case" is a service name, not a firm name. Disclosure that Second Chair operates the platform and is not a law firm satisfies this.

The previously-untouched `04_State_Bar_Rules.md` rulebook gets a new Arizona section added — see that file's update.

---

## 8. Visible-Disclosure Checklist (Saul's Audit)

Before the form ships, this checklist must show all green:

- [ ] TCPA consent text contains "West Coast Trial Lawyers" exactly, above submit button, ≥13px, non-collapsed, non-modal
- [ ] TrustedForm script is active and capturing the rendered consent text including the firm name
- [ ] Jornaya LeadiD script is active
- [ ] Footer disclosure on every step: "Get A Fair Case is operated by Second Chair. The receiving law firm appears on the consent step before you submit."
- [ ] Final-step disclaimer block (Section 3 above) renders below CTA, bordered, ≥13px
- [ ] Settlement table disclaimer (Section 4 above) renders below the table, italic
- [ ] Phone field helper (Section 5 above) renders below the phone input, ≥13px
- [ ] "This is an attorney advertisement" appears verbatim somewhere on the form (currently in the final disclaimer block — confirm)
- [ ] No checkbox for TCPA (button click constitutes consent — verify Saul's traffic-light, not all attorneys agree on this)
- [ ] No "marketing partners" link anywhere on any step
- [ ] No pre-checked consent boxes anywhere
- [ ] Past-results disclaimer (Section 4) is not below 12px and not lighter than `#6B7280`

> **Saul:** Run that checklist before EVERY launch. Not just WCTL. If you ship a Fair Case form for a different client and any of those rows is red, you're betting the account.

---

## 9. What stays compliant after the WCTL pilot ends

This pack is WCTL-Arizona-specific only on the *named entity* (WCTL) and *jurisdiction* (Arizona) lines. When the pilot ends or the program expands:

- The named entity in the TCPA consent must update to whichever firm is contacting the claimant in that ZIP.
- The footer disclosure stays as written.
- The settlement disclaimer stays as written.
- The "not a law firm" identification stays as written.
- AZ-specific ER 7.1 references stay as written for AZ traffic; new state coverage requires consulting `04_State_Bar_Rules.md` and adding state-specific overlays per `Saul.md` State Routing Protocol.

---

## 10. The traffic light: GREEN

> **Saul:** Look, with everything in this doc shipped exactly as written, you're at GREEN. TCPA: green. State bar: green. Platform: green (the form doesn't run as an ad on Meta, so Personal Attributes don't apply here — but the ads driving traffic to the form must still pass that check separately, which is McCabe + my call on the ad creative side, not this doc). The form is bulletproof. Run it.

---

*Compliance pack locked. Any deviation requires Saul's named approval and a comment in this doc explaining why.*
