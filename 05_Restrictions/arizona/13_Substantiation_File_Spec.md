# Substantiation File Spec (Arizona)

> **Saul:** "When the AZ Bar comes asking, you've got 14 days. Not 14 weeks, not a 'we'll get back to you' — 14 days to produce the binder. The substantiation file is the binder. Build it once, maintain it monthly, and it sits ready. The headline number is **$1.7 billion settled** — that's the canonical aggregate. Every other claim has its own backing record."

---

## 1. WHY THIS FILE EXISTS

ER 7.1 requires that all factual claims in WCTL/Second Chair advertising be **substantiable** — meaning the firm must be able to produce records demonstrating the claim's truth. The AZ Bar's standard practice is to demand response within 14 days when a complaint is opened.

The substantiation file is the operational binder that answers that demand.

It also defends against:
- AZ Consumer Fraud Act (§ 44-1521) private actions or AG enforcement
- Reciprocal discipline against CA-licensed WCTL attorneys
- Civil discovery in any case where WCTL's marketing claims are at issue

---

## 2. CANONICAL SUBSTANTIATION FIGURE — $1.7 BILLION

**Per Davis confirmation 2026-04-27:** WCTL's aggregate settlement total is **$1.7 billion**. This is the canonical number for the substantiation file.

**Note:** Some older Second Chair files (and possibly some current Fair Case ad creative or landing page copy) reference "$150M+" — that figure is stale or scoped to a specific case-table subset, not the lifetime aggregate. When standardizing the substantiation file:
- The topline aggregate claim is **$1.7 billion**
- If "$150M+" appears anywhere, it should be flagged for reconciliation — likely scope-specific (e.g., a specific case-result table) where the smaller figure may be intentional

This standardization sweep should be done across:
- Fair Case landing pages
- Quiz funnel copy
- Ad creative (static + video)
- Email/SMS follow-up sequences
- WCTL's own webpage copy (where SC has visibility)

---

## 3. THE SUBSTANTIATION FILE STRUCTURE

### Suggested file location
`Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/_Research/wctl_substantiation.md`

### Required sections

#### Section 1: Aggregate Recovery — $1.7B
**The claim:** "$1.7B+ recovered for clients"

**Backing records required:**
- Internal closed-case records spanning from firm founding to present
- Sum of all settlement amounts and verdict amounts (gross recovery, before fees/expenses)
- Methodology disclosure (e.g., includes verdict + settlement + structured-settlement total face value)
- Period covered (firm-life total)
- Update cadence (monthly recalculation, dated)

**Format:** Spreadsheet with date, case ID (or anonymized identifier), case type, recovery amount; summary tab with rolling total. Source records (settlement agreements, court records) retained in WCTL's case management system.

#### Section 2: Case-Outcome Rate — 97%
**The claim:** "97% of qualifying cases reach a settlement or verdict"

**Backing records required:**
- Closed-case data with definition of "qualifying" (cases that pass intake + retainer)
- Definition of "favorable resolution" (settlement, verdict, or other affirmative outcome)
- Period covered
- Methodology disclosure (denominator = qualifying cases closed in period; numerator = those with favorable resolution)

**Format:** Spreadsheet with period, qualifying-case count, favorable-resolution count, percentage.

#### Section 3: Specific Case Results
**The claim:** "$8.4M settlement — Truck crash, 2024" / "$4.1M settlement — Pedestrian motor vehicle, 2023" / "$2.3M settlement — Multi-vehicle crash, 2024"

**Backing records required (per case):**
- Court filing (case caption, court, case number)
- Settlement agreement or verdict document (redacted if needed)
- Date of resolution
- Brief case summary (factual basis, anonymized as appropriate)
- Recovery amount documented

**Format:** Per-case PDF with court filing + settlement doc + summary; index spreadsheet listing all advertised case results.

#### Section 4: Review Aggregates
**The claim:** "4.9/5 from 254 reviews" (or whatever current figure is)

**Backing records required:**
- Source platform (Google, Yelp, Avvo, Lawyers.com)
- Screenshot dated
- Review count and average at time of advertising
- Update cadence (monthly screenshots; advertised number must be no older than X days)

**Format:** Per-platform screenshot folder with dated images.

#### Section 5: Years of Experience / Practice History
**The claim:** "Trusted by Arizona families for [X] years"

**Backing records required:**
- Bar admission dates for senior attorneys
- Firm founding date
- AZ office founding date

**Format:** Roster document with attorney names, bar admissions, firm tenure.

#### Section 6: AZ-Admitted Attorney Documentation
**The claim:** "Licensed to practice in Arizona"

**Backing records required:**
- AZ Bar admission certificates for AZ-admitted attorneys at WCTL
- Current good-standing certificates (annual update)
- Office address documentation

**Format:** Per-attorney folder with admission cert + good-standing cert + address proof.

#### Section 7: Specific Practice-Area Claims
**The claim:** "Focuses on personal injury and motor vehicle crashes"

**Backing records required:**
- Practice composition data (% of cases by type)
- Period covered

**Format:** Spreadsheet with case-type breakdown.

---

## 4. UPDATE CADENCE

| Section | Update frequency |
|---|---|
| Aggregate $1.7B | Quarterly |
| Case outcome 97% | Quarterly |
| Specific case results | As advertised; refresh whenever ad creative cites new figures |
| Review aggregates | Monthly (screenshots) |
| Years of experience | Annually |
| AZ admission docs | Annually + on attorney roster changes |
| Practice-area claims | Annually |

---

## 5. THE 14-DAY RESPONSE WORKFLOW

When an AZ Bar complaint or AG inquiry lands:

1. **Day 0** — Notify WCTL compliance lawyer immediately
2. **Day 0-1** — Acknowledge receipt; identify the specific claim or ad at issue
3. **Day 1-3** — Pull the relevant section of the substantiation file
4. **Day 3-5** — Coordinate with defense counsel (reciprocal discipline risk for CA-licensed attorneys)
5. **Day 5-12** — Draft response letter with substantiation attached
6. **Day 12-14** — Final review; submit response to LRO before 14-day deadline

**Documentation throughout:** Every step logged. Even if the complaint is dismissed at intake, the documentation is mitigating evidence for any future inquiry.

---

## 6. WHO MAINTAINS THE SUBSTANTIATION FILE

- **Owner:** WCTL Compliance Lawyer (the AZ-admitted attorney designated for this function)
- **Operational support:** Second Chair Operations (data pulls, screenshot updates, file index maintenance)
- **Quarterly review:** WCTL Compliance Lawyer + Second Chair compliance lead jointly review for currency and consistency

---

## 7. SECURITY AND ACCESS CONTROLS (ER 1.6 Overlap)

The substantiation file may contain:
- Anonymized case data
- Specific settlement amounts
- Court filings (public, but consolidated)
- Attorney admission records

ER 1.6(e) "reasonable efforts" applies. Best practice:
- Encrypted storage
- Role-based access (compliance lawyer + designated SC compliance lead only)
- Audit log of access
- Periodic review of access list

---

## 8. RECONCILIATION SWEEP — ACTION ITEM

A follow-up pass should sweep existing SC files (quiz funnel, ad creative, landing-page copy) for "$150M+" references and either:
1. Update to "$1.7B+" (most cases — aggregate claim)
2. Confirm scope-specific reference is accurate (e.g., "$150M+ recovered in 2023" might be true and intentional)
3. Flag any conflicts to Davis before silently overwriting

This is documented in the project memory file `project_wctl_substantiation.md`.

---

## 9. THE PLAY (Substantiation Specific)

**Do:**
- Build the substantiation file once and maintain it on the cadence above
- Use $1.7B as the canonical aggregate substantiation figure
- Document every advertised claim with traceable backing
- Coordinate with defense counsel on any AZ Bar inquiry
- Sweep existing SC files for "$150M+" references and reconcile

**Don't:**
- Don't advertise a number you can't substantiate within 14 days
- Don't let case-result claims age past their record-update cadence
- Don't omit the $1.7B reconciliation sweep — old files create discrepancy risk
- Don't let access controls slip on the substantiation file

---

## References

- AZ Rules of Professional Conduct ER 7.1 (substantiation requirement)
- A.R.S. § 44-1521 — AZ Consumer Fraud Act
- AZ Bar disciplinary process — see [`15_Disciplinary_Process_and_Sanctions.md`](15_Disciplinary_Process_and_Sanctions.md)
- WCTL substantiation file location: `Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/_Research/wctl_substantiation.md` (TO BE CREATED — this spec describes its required structure)
- See related: [`02_Rules_of_Professional_Conduct/ER_7.1_Communications.md`](02_Rules_of_Professional_Conduct/ER_7.1_Communications.md), [`02_Rules_of_Professional_Conduct/ER_1.6_Confidentiality.md`](02_Rules_of_Professional_Conduct/ER_1.6_Confidentiality.md), [`14_Voluntary_Review_Practice_2.0.md`](14_Voluntary_Review_Practice_2.0.md)
