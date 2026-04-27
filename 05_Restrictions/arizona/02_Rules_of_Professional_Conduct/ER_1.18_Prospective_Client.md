# ER 1.18 — Duties to Prospective Client

> **Saul:** "This is the rule that turns the Fair Case quiz into a legal-ethics question. The moment a claimant submits the form expecting an attorney to evaluate their case, ER 1.18 attaches — at WCTL, not at SC. WCTL inherits prospective-client duties on every submitted lead. The fix: build the form so it gathers identifiers and case category, not legal strategy or settlement views. Run conflict checks before substantive contact. Document everything."

---

## 1. THE RULE

**Citation:** Ariz. R. Sup. Ct. 42, ER 1.18 (tracks ABA Model Rule 1.18).

### ER 1.18(a) — Definition
A "prospective client" is a person who consults with a lawyer about the possibility of forming an attorney-client relationship.

### ER 1.18(b) — Confidentiality
Even if no engagement results, the lawyer "shall not use or reveal information learned in the consultation, except as ER 1.9 would permit with respect to information of a former client."

### ER 1.18(c) — Conflict Trigger
Lawyer cannot represent a person with materially adverse interests in the same or substantially related matter if the lawyer received information "that could be significantly harmful" to the prospective client. **Imputation extends to the lawyer's firm.**

### ER 1.18(d) — Cure
Disqualification can be avoided by:
1. **Informed-consent waiver** from both affected clients, OR
2. **Limiting** the consulting lawyer's exposure + **screening** + **apportionment of fees** + **written notice** to the prospective client.

---

## 2. WHEN ONLINE INTAKE CREATES AN ER 1.18 RELATIONSHIP

The AZ Bar's ER 1.18 best-practices guidance and Comment 2 confirm the test is the **prospective client's reasonable subjective belief** that they were communicating with a lawyer for purposes of forming a relationship.

### Triggers for ER 1.18 Attachment
- Submission invites or accepts confidential or case-specific facts
- The intake is presented as coming from "the firm" or "an attorney"
- The submitter receives any substantive legal-information response

### Specifically: Chatbots and Online Intake
The AZ Bar guidance explicitly addresses chatbots and online forms. To **avoid** unintended ER 1.18 attachment to a non-engaged claimant:
1. Clearly state the tool/form is **not a lawyer**
2. **Do not invite confidential information** until human attorney review
3. Include a clear disclaimer

---

## 3. THE FAIR CASE QUIZ — ER 1.18 ANALYSIS

### What the form does today

The Fair Case quiz collects:
- Demographic info (state, ZIP)
- Date and type of incident (filtering for SOL, jurisdiction, case type)
- Soft-tissue gate (filtering for case viability)
- Insurance status
- Contact information (phone, email)
- TCPA consent naming WCTL

**This is mostly conflict-relevant identifier info + claim category.** It does not invite case strategy, settlement views, or sensitive personal facts beyond what's needed to determine whether the case fits WCTL's intake criteria.

### Where ER 1.18 attaches

The moment the claimant submits the form expecting a WCTL attorney (the named recipient) to review their case, **ER 1.18 attaches at WCTL**. The claimant becomes a prospective client of WCTL. This means:

1. **WCTL must run a conflict check** before substantive consultation
2. **WCTL must limit further consultation** to information truly necessary to evaluate the conflict and capacity
3. **WCTL must retain the prospective-client information** in its conflicts database
4. If WCTL declines representation but later wants to represent an adverse party, **screening procedures** under ER 1.18(d)(2) must be followed

### Where Second Chair sits

Second Chair is a **lead-gen vendor**, not a law firm. Second Chair does not have ER 1.18 duties because Second Chair does not hold itself out as a lawyer. However:
- The information passing through Second Chair becomes prospective-client information once it reaches WCTL
- Second Chair's data-handling practices must support WCTL's ER 1.6 confidentiality obligations (encryption in transit, access controls, retention policies)
- Second Chair must not retain or repurpose prospective-client information for any purpose other than the WCTL handoff

---

## 4. CONFLICT-CHECK OBLIGATIONS

Once ER 1.18 attaches at WCTL:

| Step | Action |
|---|---|
| Lead arrives at WCTL | Conflict check against existing client database + adversary database |
| Match found | Decline representation; document declination; do not consult further |
| No match | Proceed to consultation (still subject to ER 1.18(b) confidentiality) |
| Decision to decline (post-consultation) | Document; retain info in conflicts DB; screening procedures if firm later represents an adverse party |
| Decision to engage | Issue ER 1.5(c) engagement letter; relationship transitions from prospective-client to client |

---

## 5. INFORMATION-FIREWALL (Screening) UNDER ER 1.18(d)(2)

If WCTL declines representation but later wants to represent an adverse party:

- **Disqualified lawyer must be timely screened** from any participation in the matter
- Disqualified lawyer apportioned **no part of the fee** from the matter
- **Written notice** promptly given to the prospective client
- Information from the prospective-client consultation must have been "limited to that reasonably necessary" to determine whether to represent

The "reasonably necessary" gate is why the Fair Case quiz architecture matters — by collecting only conflict-relevant info + claim category (not legal strategy, settlement views, or sensitive personal info), the form keeps WCTL's screening optionality intact.

---

## 6. INTERSECTION WITH ER 1.6 (CONFIDENTIALITY)

ER 1.6 confidentiality "duty survives the representation." It expressly extends to former clients (via ER 1.9(c)) and prospective clients (via ER 1.18(b)).

ER 1.6 covers **"all information relating to the representation"** from any source — not just client-disclosed facts. AZ adds an **express ER 1.6(e) duty of competent technology**:

> "Reasonable efforts to prevent unauthorized access or disclosure"

Comment 22 directs lawyers to consult with a competent tech expert when needed.

For online intake/lead-gen, the storage of the prospective-client data attaches ER 1.6(e) safeguarding duties from the moment of submission. This is why:
- Second Chair must use encryption in transit and at rest
- Access to lead data must be controlled (role-based; auditable)
- Retention policies must align with WCTL's ER 1.6 / 1.18 obligations
- Vendor security review of any third-party tools handling prospective-client data

(See [`ER_1.6_Confidentiality.md`](ER_1.6_Confidentiality.md) for the full ER 1.6 treatment.)

---

## 7. BEST-PRACTICE DISCLAIMER PATTERN (Fair Case Form)

To minimize unintended ER 1.18 attachment in the Fair Case funnel and keep WCTL's optionality intact, the form should include — visibly, before submission:

```
This form is for initial screening only. Submitting this form does not
create an attorney-client relationship. Information you submit will be
used only to determine whether the firm can represent you, and
submission alone does not prevent the firm from representing other
parties — including parties whose interests may be adverse to yours —
in this or related matters.
```

Combined with:
- Clear "Fair Case is not a law firm" disclosure (ER 7.5 satisfaction)
- TCPA consent block naming WCTL
- Substantive intake (case strategy discussion, settlement views) deferred to **post-conflict-check, post-engagement-letter** attorney consultation

This pattern satisfies the AZ Bar's chatbot/intake guidance and preserves WCTL's screening optionality under ER 1.18(d)(2).

---

## 8. WHAT NOT TO DO

| Form behavior | Problem |
|---|---|
| Asking "What do you think your case is worth?" at intake | Invites settlement-view info; creates reasonably-necessary problem under ER 1.18(d)(2) |
| Asking "Have you talked to other lawyers?" | Could elicit privileged info; problematic |
| AI-driven case-strength scoring shown to claimant | Implies legal evaluation by SC; ER 1.18 attachment risk + LRS classification risk |
| Live chat asking "Tell me about your accident in detail" pre-engagement | Substantive intake before conflict check |
| Auto-emailing the claimant a "case strategy" summary | Substantive legal advice without engagement |

---

## 9. THE PLAY (ER 1.18 Specific)

**Do:**
- Keep the Fair Case quiz scoped to identifiers + claim category, not legal strategy
- Include the ER 1.18 disclaimer above the submit button
- Run WCTL conflict checks **before** substantive consultation
- Document declination decisions and retain in conflicts DB
- Use ER 1.18(d)(2) screening procedures if WCTL later faces adverse representation

**Don't:**
- Don't add settlement-view, case-strategy, or detailed-fact questions to the form
- Don't have an AI tool give substantive legal feedback to claimants
- Don't transition from "form submission" to "case evaluation" without an attorney conflict check first
- Don't share prospective-client info beyond the WCTL handoff

---

## References

- **Ariz. R. Sup. Ct. 42, ER 1.18** (current text)
- AZ State Bar, ER 1.18 Best Practices — [azbar.org](https://www.azbar.org/for-legal-professionals/ethics/best-practices/er-1-18-duties-to-prospective-clients/)
- ABA Model Rule 1.18 Comments
- See related: [`ER_1.6_Confidentiality.md`](ER_1.6_Confidentiality.md), [`ER_7.3_Solicitation.md`](ER_7.3_Solicitation.md), [`ER_7.1_Communications.md`](ER_7.1_Communications.md)
