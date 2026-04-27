# TCPA Arizona Overlay

> **Saul:** "TCPA 2025 is federal — same rules apply in every state. Arizona has no separate state-level TCPA equivalent that adds another layer. Good news: the federal one-to-one consent rule is the binding constraint. Get TCPA right and you've got AZ consent right. The only AZ-specific consent question is whether the engagement letter discloses the SC compensation arrangement under ER 1.5(f) — and that's a Bar rule, not a TCPA rule."

---

## 1. WHY THIS FILE EXISTS (BRIEFLY)

The federal TCPA 2025 rule is documented in detail at `Abracadabra/06_Legal/Rulebook/01_TCPA_Consent_2025.md`. This file consolidates the **Arizona-specific overlay** — what (if anything) AZ adds to the federal baseline.

**TL;DR:** Arizona does not have a state TCPA equivalent that imposes additional requirements beyond federal law. The federal rule is the binding constraint.

---

## 2. THE FEDERAL BASELINE (Recap)

FCC TCPA 2025 (effective January 27, 2025) requires for marketing calls/texts to consumer cell phones:

| Requirement | Detail |
|---|---|
| One-to-one consent | Specific named entity consent (not static hyperlink lists or "marketing partners" lists) |
| Individual unchecked checkboxes | Per buyer, per consent |
| Dynamic consent | Buyers determined BEFORE final submission |
| TrustedForm certification | Mandatory video replay of consent moment |
| Jornaya LeadiD | Mandatory audit trail + bot detection |

For Fair Case → WCTL:
- TCPA consent block names **West Coast Trial Lawyers** specifically
- One-to-one (not "marketing partners")
- TrustedForm + Jornaya integration on the form
- Consent captured before submission

---

## 3. AZ STATE LAW — WHAT'S NOT THERE

### No AZ Mini-TCPA
Arizona does not have a state-level statute equivalent to California's CIPA (state wiretapping) or Florida's FTSA (Telephone Solicitation Act amendments) imposing additional consent rules on telephonic marketing.

### No AZ-Specific Recording Consent for PI Intake
Arizona is a **one-party consent** state for call recording (A.R.S. § 13-3005 reference; one-party consent regime). Calls between AZ claimants and WCTL intake can be recorded with the consent of one party (the WCTL intake person or claimant). This is **less restrictive** than two-party-consent states like California (whose CIPA requires two-party consent).

**Caveat:** If the call originates in or is received in a two-party-consent state, that state's rule may apply. WCTL's intake practice should default to two-party consent for cross-border safety.

### Spanish-Language TCPA Disclosure
TCPA's federal rule applies regardless of language. Spanish-language Fair Case ads must include the same one-to-one consent architecture, with the consent text translated. (See [`12_Bilingual_Spanish_Language.md`](12_Bilingual_Spanish_Language.md).)

---

## 4. WHERE AZ-SPECIFIC LANGUAGE GETS LAYERED IN

The AZ-specific elements that *do* layer onto the consent flow are **Bar rules**, not TCPA rules:

| AZ Bar Rule | Consent-Adjacent Disclosure |
|---|---|
| ER 7.1 (responsible attorney) | "West Coast Trial Lawyers is responsible for this advertisement" |
| ER 7.5 (trade name) | "Fair Case is operated by Second Chair. Not a law firm." |
| ER 1.18 (prospective client) | "This form is for initial screening only. Submitting does not create an attorney-client relationship." |
| ER 1.5(f) (non-lawyer fee disclosure) | Disclosed in the engagement letter (post-form), not the consent block |

These are all stacked into the Fair Case landing page disclosure architecture — see [`09_Disclosures_and_Required_Language.md`](09_Disclosures_and_Required_Language.md).

---

## 5. STANDARD AZ-COMPLIANT TCPA CONSENT BLOCK (Reference)

Above the submit button on the Fair Case form (AZ traffic):

```
By clicking "Submit," I consent to be contacted by West Coast Trial
Lawyers via phone, text, or email at the contact information I
provided, including via automated systems and pre-recorded messages,
regarding my potential legal matter. I understand consent is not a
condition of any service. Message and data rates may apply. I have
read and agree to the Privacy Policy and Terms of Service.
```

Plus the ER 1.18 disclaimer (separate, not part of the TCPA consent itself):

```
This form is for initial screening only. Submitting this form does not
create an attorney-client relationship. Information you submit will be
used only to determine whether the firm can represent you, and
submission alone does not prevent the firm from representing other
parties — including parties whose interests may be adverse to yours —
in this or related matters.
```

Plus the ER 7.5 / ER 7.1 disclosures:

```
This is an advertisement for legal services. Fair Case is operated by
Second Chair and is not a law firm. West Coast Trial Lawyers is
responsible for the content of this advertisement.
```

---

## 6. THE PLAY (TCPA-AZ Specific)

**Do:**
- Apply the federal TCPA 2025 baseline to all AZ traffic — same as every other state
- Stack the AZ Bar disclosures (ER 7.1, 7.5, 1.18) into the disclosure architecture
- Default to two-party-consent for call recording where any party may be in a two-party-consent state
- Use TrustedForm + Jornaya integration on every Fair Case form

**Don't:**
- Don't think AZ adds a state-TCPA layer — it doesn't
- Don't assume AZ's one-party-consent recording rule covers calls received in CA/FL/NV/etc. — default to safer
- Don't conflate the TCPA consent block with the ER 1.18 disclaimer or the ER 1.5(f) engagement-letter disclosure — they're separate, served at different points

---

## References

- Federal: FCC TCPA 2025 rule (effective January 27, 2025)
- Master TCPA documentation: `Abracadabra/06_Legal/Rulebook/01_TCPA_Consent_2025.md`
- A.R.S. § 13-3005 — AZ wiretapping (one-party consent)
- See related: [`09_Disclosures_and_Required_Language.md`](09_Disclosures_and_Required_Language.md), [`02_Rules_of_Professional_Conduct/ER_1.18_Prospective_Client.md`](02_Rules_of_Professional_Conduct/ER_1.18_Prospective_Client.md), [`12_Bilingual_Spanish_Language.md`](12_Bilingual_Spanish_Language.md)
