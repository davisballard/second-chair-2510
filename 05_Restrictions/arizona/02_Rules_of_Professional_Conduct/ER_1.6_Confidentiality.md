# ER 1.6 — Confidentiality of Information

> **Saul:** "ER 1.6 doesn't just protect the case file. It protects the data trail. Every byte of prospective-client info that flows through the SC → WCTL handoff is covered. Encryption in transit, access controls, retention policies — these aren't IT-department questions, they're ER 1.6(e) compliance questions. Get it wrong and the technical breach becomes an ethics violation."

---

## 1. THE RULE

**Citation:** Ariz. R. Sup. Ct. 42, ER 1.6.

### ER 1.6(a) — General Confidentiality
A lawyer shall not reveal information relating to the representation of a client unless:
- The client gives informed consent
- Disclosure is impliedly authorized to carry out the representation
- One of the specific exceptions in ER 1.6(b) or (d) applies

### ER 1.6(b) — Permissive Disclosures (selected)
A lawyer **may** reveal confidential information to the extent reasonably necessary to:
- Prevent reasonably certain death or substantial bodily harm
- Prevent client from committing a crime or fraud reasonably certain to result in substantial financial harm to another (where lawyer's services were used)
- Establish a claim or defense in a controversy with the client
- Comply with court order or other law

### ER 1.6(e) — Duty of Competent Technology (Arizona-Specific)

> "A lawyer shall make reasonable efforts to prevent the inadvertent or unauthorized disclosure of, or unauthorized access to, information relating to the representation of a client."

**Comment 22** directs lawyers to consult with a competent tech expert when needed. AZ has gone further than many ABA Model Rule jurisdictions in formalizing the technology-competence obligation.

---

## 2. SCOPE — "ALL INFORMATION RELATING TO THE REPRESENTATION"

ER 1.6 covers more than just client-disclosed facts. It covers **all information relating to the representation**, from any source:
- Information learned from the client
- Information learned from third parties about the client
- Information learned from public records once it's part of the representation
- Strategy, work product, mental impressions
- The fact that the firm represents the client (sometimes)
- Settlement positions, communications with adversaries

**For SC/WCTL:** the lead-form data, the date of the incident, the type of injury, the contact information — all of it becomes ER 1.6-covered information once the prospective-client relationship attaches under ER 1.18(b).

---

## 3. ER 1.6 + ER 1.18 — THE PROSPECTIVE-CLIENT EXTENSION

ER 1.18(b) extends ER 1.6 confidentiality to **prospective clients**:

> "Even when no client-lawyer relationship ensues, a lawyer who has had discussions with a prospective client shall not use or reveal information learned in the consultation, except as ER 1.9 would permit with respect to information of a former client."

This means: from the moment a claimant submits the Fair Case quiz with the expectation that WCTL will evaluate their case, ER 1.6 (via ER 1.18(b)) covers the data they submitted.

---

## 4. ER 1.6(e) IN PRACTICE — DATA-HANDLING REQUIREMENTS

The "reasonable efforts" standard under ER 1.6(e) is fact-specific. Factors:
- **Sensitivity** of the information
- **Likelihood** of disclosure if safeguards aren't taken
- **Cost** of additional safeguards
- **Difficulty** of implementing safeguards
- **Extent to which safeguards adversely affect** the lawyer's ability to represent clients

For the SC/WCTL data flow, "reasonable efforts" means at minimum:

| Layer | Requirement |
|---|---|
| Encryption in transit | TLS 1.2+ on all SC↔WCTL handoff endpoints |
| Encryption at rest | At-rest encryption on lead databases |
| Access control | Role-based access; audit logs; principle of least privilege |
| Vendor security review | Third-party tools (Higgsfield, ChatGPT Image, CapCut, ad platforms) reviewed for data handling — though these don't typically touch lead data |
| Retention policy | Lead data retained only as long as needed for WCTL conflict checks + standard discovery preservation |
| Breach response plan | Documented procedure for incident response; client notification under ER 1.6 if breach occurs |
| Vendor agreements | SC↔WCTL data-handling terms documented; data-processor language; subprocessor list |

---

## 5. SC-SPECIFIC OBLIGATIONS

Second Chair is **not** an AZ-licensed law firm and is therefore not directly bound by ER 1.6. However, SC's data handling **must support WCTL's ER 1.6 obligations**, because:

1. WCTL is responsible for ensuring its agents (including SC as a lead-gen vendor) handle prospective-client data consistent with ER 1.6
2. A breach at the SC side that exposes prospective-client info reflects on WCTL's ER 1.6(e) "reasonable efforts" obligation
3. AZ Consumer Fraud Act (A.R.S. § 44-1521) liability could attach to SC directly if data handling is deceptive (e.g., promised privacy not delivered)

**Operational implication:** SC's data-handling practices should be documented in the SC↔WCTL service agreement, and WCTL's compliance lawyer should periodically review SC's tech stack to confirm "reasonable efforts" are in place.

---

## 6. WHEN TO REVEAL — SPECIFIC SCENARIOS

### Permitted disclosures relevant to lead-gen operations
- **WCTL → its insurance carrier** for malpractice coverage purposes (impliedly authorized)
- **WCTL → opposing counsel** in the course of representation (impliedly authorized)
- **WCTL → court** under court order (ER 1.6(b))
- **WCTL → AZ Bar** in response to a disciplinary inquiry (often a contested area; consult counsel)
- **WCTL → SC** for routine handoff and conflict check (impliedly authorized within the lead-gen architecture, with informed-consent disclosure in TCPA block)

### Prohibited disclosures
- **WCTL → other firms** about a declined prospective client (without ER 1.18(d)(2) screening procedures)
- **WCTL → marketing analytics** revealing identifiable claimant info
- **SC → other clients/firms** of any prospective-client info
- **Either → media or public** without client consent

---

## 7. AI / CHATGPT / CLOUD-AI CAUTIONS

If WCTL or SC uses AI tools (ChatGPT, Claude, etc.) to process prospective-client info:
- Default-mode use of public AI services may transmit data to providers and **violate ER 1.6(e)** if the provider stores or trains on the data
- **Best practice:** Use enterprise/zero-retention AI configurations only for any data that touches prospective-client info
- AZ Bar Practice 2.0 has issued guidance on AI use; consult before deploying AI to client-facing or intake-data flows

For Fair Case ad creative (image generation, video generation): the assets themselves don't contain prospective-client info, so ER 1.6(e) doesn't bite the creative pipeline. The bite is on **lead data** — and that data should not be passed through public AI services.

---

## 8. THE PLAY (ER 1.6 Specific)

**Do:**
- Encrypt prospective-client data in transit and at rest
- Document SC↔WCTL data-handling architecture in the service agreement
- Limit access to lead data to those who need it (role-based)
- Use enterprise/zero-retention AI configurations if AI touches lead data
- Document breach response plan
- Periodic security review of the SC tech stack by WCTL's compliance lawyer

**Don't:**
- Don't send prospective-client info through public ChatGPT or similar default-mode AI tools
- Don't retain lead data longer than needed for conflict-check + reasonable preservation
- Don't share prospective-client info with vendors who haven't been vetted
- Don't treat ER 1.6 as an IT problem — it's a Bar-rule problem with IT consequences

---

## References

- **Ariz. R. Sup. Ct. 42, ER 1.6** (current text)
- AZ State Bar, ER 1.6 Best Practices — [azbar.org](https://www.azbar.org/for-legal-professionals/ethics/best-practices/er-1-6-confidentiality-of-information/)
- AZ Courts AEA Committee ER 1.6 rule text
- See related: [`ER_1.18_Prospective_Client.md`](ER_1.18_Prospective_Client.md), [`ER_7.1_Communications.md`](ER_7.1_Communications.md), [`../03_Statutes/44-1521_Consumer_Fraud_Act.md`](../03_Statutes/44-1521_Consumer_Fraud_Act.md)
