# ER 7.5 — Firm Names and Letterheads
## Arizona Rules of Professional Conduct

> **Saul:** "ER 7.5 is the rule that decides whether 'Fair Case' is a problem. The trade name itself isn't — it's a service mark, like a brand. The thing the rule cares about is whether a reasonable claimant could conclude that 'Fair Case' is a law firm. Answer that with disclosure: 'Fair Case is operated by Second Chair. The receiving law firm appears on the consent step.' Done. Reasonable claimant can no longer be confused."

---

## 1. THE RULE

A lawyer shall not use a firm name, letterhead, or other professional designation that violates ER 7.1 (false or misleading communications).

**Trade names** are permitted if they:
- Do not imply a connection with a government agency
- Do not imply a connection with a public legal services organization or any charitable legal services organization
- Do not imply the trade name belongs to "any other type of legal services organization or entity that the lawyer or law firm is not"

**Firm name restrictions:**
- Cannot include the name of a lawyer holding public office during the period of public service
- Cannot use "and Associates" without actually having multiple attorney associates
- Multi-jurisdictional firms must identify the jurisdictions of each lawyer

---

## 2. WHY THIS MATTERS FOR SECOND CHAIR

Second Chair operates **Fair Case** as a B2C trade name (`getafaircase.com`) — the consumer-facing brand. The architecture is:

```
Claimant sees ad → "Fair Case" brand
        ↓
Claimant fills quiz on getafaircase.com
        ↓
Form discloses: receiving law firm (West Coast Trial Lawyers)
        ↓
Lead routed to WCTL with claimant consent
```

The ER 7.5 question: does "Fair Case" — sitting at the top of that funnel — mislead a reasonable claimant into thinking they're contacting a law firm?

**Answer: not if the disclosure is conspicuous.** Specifically:
- "Fair Case" is consistently presented as a service mark (claim-evaluation tool), not a firm name
- The site discloses that **Fair Case is operated by Second Chair**, a non-law-firm entity
- The actual law firm (WCTL) is **named separately** before the claimant submits
- Footer disclosures on every page: "Fair Case is not a law firm"
- The TCPA consent block names WCTL as the receiving entity (one-to-one consent, FCC 2025-compliant)

The combination satisfies ER 7.5(a) — a reasonable claimant cannot conclude the trade name is itself a law firm, because the disclosure architecture surfaces the actual firm before any commitment is made.

---

## 3. WHAT ER 7.5 PROHIBITS (Specifically for Lead-Gen Trade Names)

| Conduct | Status |
|---|---|
| Using "Fair Case" as a service mark for the quiz/evaluation tool | :white_check_mark: Permitted |
| Footer "Fair Case is operated by Second Chair. Not a law firm." | :white_check_mark: Required for compliance |
| Naming WCTL on the form before claimant submits | :white_check_mark: Required (also TCPA-required) |
| "Fair Case lawyers will review your case" | :x: Implies "Fair Case" is itself a law firm |
| "Fair Case attorneys are standing by" | :x: Same problem |
| Signature line on legal communications using "Fair Case" trade name | :x: Suggests trade name is the legal entity |
| "America's Injury Law Firm" as a tagline for Fair Case | :x: Affirmatively misrepresents Fair Case as a law firm |
| "1-800-FAIR-CASE" as a phone number | :warning: Could be problematic if the number routes to non-attorneys answering as if they are attorneys |
| Trade name implying government affiliation ("Arizona Crash Authority") | :x: Implies governmental connection |
| Trade name implying charitable service ("Free Legal Aid for Crash Victims") | :x: Implies charity legal services org |

---

## 4. THE TEXAS COMPARISON (Why AZ Is Easier)

Texas Rule 7.01 has a specific "presumed law firm" rule that requires lead-gen entities to affirmatively disclose "not a law firm" with very specific format requirements. Florida's Rule 4-7.22 ("Qualifying Provider" rule) is even more aggressive.

Arizona has **no equivalent specific lead-gen disclosure mandate**, but ER 7.5(a)'s "not misleading trade name" standard accomplishes effectively the same thing, by requiring the disclosure architecture above.

> **Saul:** "Arizona doesn't have a Texas-style 'NOT A LAW FIRM' label rule, so we get to design the disclosure into the user experience instead of bolting on a banner. Cleaner. The standard is 'reasonable claimant can't be confused' — and we satisfy that with the 'Fair Case is operated by Second Chair' footer + WCTL named on the form. Don't strip those. Both are load-bearing."

---

## 5. MULTI-JURISDICTIONAL FIRM DISCLOSURE

WCTL is a California-headquartered firm with offices in multiple states (including Arizona). When WCTL is named in Fair Case advertising:

- The fact that WCTL has multi-state operations is permissible
- ER 7.5(b)-equivalent requires the jurisdictions of each lawyer to be identifiable if implied
- Best practice: landing page/form discloses "West Coast Trial Lawyers — licensed to practice in [list of states]"
- For AZ-targeted ads, ensure at least one AZ-licensed attorney at WCTL is identifiable

(See [`ER_5.5_Multijurisdictional_Practice.md`](ER_5.5_Multijurisdictional_Practice.md) for the deeper multijurisdictional analysis.)

---

## 6. AZ vs. OTHER STATES — TRADE NAME RULE COMPARISON

| State | Trade name rule | Required label |
|---|---|---|
| Arizona | ER 7.5: must not imply firm/govt/charity | None mandated; disclosure architecture satisfies |
| California | RPC 7.5: similar, plus BPC § 6155 LRS rules | "Not a law firm" recommended |
| Texas | Rule 7.01: presumed-firm rule | "Not a law firm" disclaimer with specific format |
| Florida | Rule 4-7.22: Qualifying Provider | Spoken "Spokesperson is not an attorney" + label |
| New York | RPC 7.5: stricter; "Attorney Advertising" label | "Attorney Advertising" required |

---

## 7. THE PLAY (ER 7.5 Specific)

**Do:**
- Keep "Fair Case" branded as a claim-evaluation service mark
- Maintain the "Fair Case is operated by Second Chair. Not a law firm." footer on every Fair Case page
- Name WCTL conspicuously before claimant submits the form
- List WCTL's licensed jurisdictions on the landing page
- Match disclosure size/contrast to the primary brand text — "clear and conspicuous" is enforced

**Don't:**
- Don't use Fair Case as if it were a firm name ("Fair Case lawyers," "Fair Case attorneys")
- Don't sign legal communications as "Fair Case" — those signatures come from WCTL
- Don't pick a trade name that implies government connection ("AZ Crash Authority," "State Injury Bureau")
- Don't pick a trade name that implies charity ("Free Help for Crash Victims," "Crash Victim Legal Aid")
- Don't bury the "not a law firm" disclosure in fine print at 4pt — clear-and-conspicuous is the standard

---

## References

- AZ Rules of Professional Conduct ER 7.5 (current text)
- AZ Bar Best Practices: Information About Legal Services
- See related: [`ER_7.1_Communications.md`](ER_7.1_Communications.md), [`ER_5.5_Multijurisdictional_Practice.md`](ER_5.5_Multijurisdictional_Practice.md)
- See related: [`../11_Lead_Generator_vs_LRS_Arizona.md`](../11_Lead_Generator_vs_LRS_Arizona.md), [`../09_Disclosures_and_Required_Language.md`](../09_Disclosures_and_Required_Language.md)
