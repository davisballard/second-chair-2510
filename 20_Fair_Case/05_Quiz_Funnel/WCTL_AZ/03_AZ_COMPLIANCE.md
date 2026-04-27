# WCTL Arizona — Compliance Overlay

**Author:** Saul (Chief Compliance Officer)
**Date:** 2026-04-27
**Scope:** Arizona-specific compliance requirements that overlay the universal compliance pack (`../06_COMPLIANCE_PACK.md`). Read both — this doc adds; the pack governs.

> **Note (2026-04-27):** The full multi-file Arizona compliance reference now lives at `Abracadabra/08_Brands/Second_Chair/05_Restrictions/arizona/`. This overlay file remains the form-specific application; the deeper rule-by-rule treatment (ER 7.1, ER 7.3, ER 7.5, ER 1.18, ER 5.4, statutes, case law, tribal, insurance, substantiation file spec, Practice 2.0, discipline process) is in the dedicated folder. Start with [`00_INDEX.md`](../../../05_Restrictions/arizona/00_INDEX.md).

> **Saul:** Arizona's actually one of the more permissive PI advertising states. ER 7.1 is similar to ABA Model Rule 7.1 — no false or misleading communications, basic substantiation requirements, no guarantees. The Bar enforces but isn't aggressive about lead-gen specifically (unlike Texas Rule 7.01 or California SB37). That said, AZ ER 7.5 has a trade-name rule we need to handle, and ER 7.3 governs solicitation — important for the form's status as inbound vs. outbound.

---

## 1. The Arizona Rules That Apply

| Rule | Topic | Form impact |
|---|---|---|
| ER 7.1 | False or misleading communications | All claims must be substantiated; settlement amounts need disclaimers; no "best lawyer" |
| ER 7.2 | Communications concerning a lawyer's services | Reasonable fee references; "no fee unless we win" is permissible if accurate |
| ER 7.3 | Solicitation of clients | Direct contact restricted; **inbound form is requested contact, NOT solicitation** |
| ER 7.5 | Firm names and letterheads | Trade names allowed if non-misleading; "Get A Fair Case" is a service mark, not a firm name |
| A.R.S. § 12-542 | 2-year statute of limitations on PI | Form's date question must respect this window |

---

## 2. ER 7.1 Substantiation — What Each Claim Needs

The form makes several factual claims. Each one needs substantiation in case the AZ Bar (or a court, or a TCPA defendant attorney) asks:

| Claim | Substantiation required | Where it's documented |
|---|---|---|
| "$1.7 Billion+ recovered for clients" | WCTL aggregate recovery records | Public record per `In_Depth/WCTL_Market_Intelligence_Brief.md` line 20; redacted case ledger backup desirable |
| "97% of qualifying cases reach a settlement or verdict" | WCTL case outcome data over a defined period | WCTL provides; `_Research/wctl_substantiation.md` (to be created with Sasha) |
| "4.9/5 from 254 verified reviews" | Google / Trustpilot / Yelp review aggregate | URL with review source; same file. **Note:** WCTL has 12 years of operation — the actual review count and rating may need adjustment based on current Google + other-platform aggregates |
| "Free consultation — same-day callback" | WCTL intake operations confirmation | WCTL written confirmation; same file |
| Settlement table amounts ($19.4M / $3.85M / $1.75M) | Real WCTL recoveries per `WCTL_Market_Intelligence_Brief.md` lines 27-35 (wrongful death $19.4M, truck $3.85M, pedestrian $1.75M) | Redacted case summaries to be filed at `_Research/wctl_substantiation.md` |

**Action item before launch:** Sasha to collect WCTL's substantiation data into a single internal doc Second Chair can produce on demand. The file lives at `Abracadabra/08_Brands/Second_Chair/23_Clients/West_Coast_Trial_Lawyers/_Research/wctl_substantiation.md` (to be created).

> **Saul:** The Bar doesn't ask to see this every day, but if a competitor or a disgruntled client files a complaint, you have 14 days to produce it. Better to have it in a folder you can grab than to scramble.

---

## 3. ER 7.3 — The "Inbound vs. Outbound" Distinction

ER 7.3 prohibits direct, in-person, live telephone, or real-time electronic contact with a known accident victim ("ambulance chasing"). The Fair Case quiz form is **inbound**: the claimant initiates contact by clicking a Meta ad and filling out the form. They are not being solicited — they are *requesting* a case evaluation.

This distinction is critical. Three things keep the form on the right side of ER 7.3:

1. **The ad creative leads with information, not solicitation.** "Truck accident in Arizona? Here's what your case may be worth" is informational; "Were YOU hit by a truck? Call now!" is solicitation. (And also Meta-bannable per personal attribute rule — not just an AZ Bar problem.)
2. **The form is initiated by the claimant.** They tap; they choose to engage; they fill out their information.
3. **The follow-up call is from the law firm whose name is on the consent.** Per TCPA 2025 one-to-one consent, the call comes from West Coast Trial Lawyers (or its authorized intake — Second Chair acting on WCTL's behalf), and the consent specifically authorizes that call.

What would break ER 7.3:
- ⛔ The ad targeting Arizona claimants directly identified by name or accident location (e.g., scraping police reports and sending personalized ads — this is a real practice and absolutely banned in AZ)
- ⛔ A live-chat feature on the quiz that proactively pings the claimant ("Hi, I see you're filling out a form — can I help?") — that's real-time electronic contact; restricted under ER 7.3(a)(3)
- ⛔ An automated text or call to the claimant that goes BEYOND the consent they gave (e.g., upsell, additional case types, follow-up after they declined)

---

## 4. ER 7.5 — Trade Names

"Get A Fair Case" is a service mark for the intake platform Second Chair operates. It is NOT a law firm name. ER 7.5(a) restricts use of trade names that imply a connection with a government agency, public services organization, or "any other type of legal services organization or entity that the lawyer or law firm is not."

Current handling — compliant:
- The footer disclosure on every step says: *"Get A Fair Case is operated by Second Chair. The receiving law firm appears on the consent step before you submit."*
- The final disclaimer block says: *"Second Chair operates the Get A Fair Case intake platform and is not a law firm."*

These statements together satisfy ER 7.5(a) — a reasonable claimant cannot conclude that "Get A Fair Case" is a law firm.

What would break ER 7.5:
- ⛔ Marketing copy that says "Get A Fair Case lawyers" or "Get A Fair Case attorneys"
- ⛔ A Get A Fair Case signature line on a legal communication (no GAF Case communication is legal advice — they're all marketing or intake)
- ⛔ Implying that "Get A Fair Case" can take a case or represent a claimant — only the named law firm (WCTL for Arizona) can

---

## 5. AZ-Specific Disclosure Requirements (vs. Other States)

Arizona does NOT require the explicit "Attorney Advertising" label that NY Rule 7.1 requires. Including it is fine (and we do, in the final disclaimer block per `06_COMPLIANCE_PACK.md` Section 3) — but it's a best practice, not an AZ-specific mandate.

Arizona does NOT require a spoken "Spokesperson is not an attorney" disclosure (unlike Florida Rule 4-7.22). Not relevant for the form context anyway since there's no spokesperson.

Arizona does NOT have a state law analogous to California's SB37 (which restricts crash footage and certain settlement claims). WCTL's permitted creative latitude in AZ ad campaigns (see `Saul.md` State Routing Protocol — though Saul's file currently calls AZ a "paused state," the WCTL pilot is reactivating it) is closer to Nevada's than California's. **For form copy, this means we can be specific about settlement amounts as long as substantiation exists** (Section 2 above).

---

## 5A. Geographic Specificity of Settlement Amounts (Davis's question)

**The question:** Do the settlement amounts shown in the form have to be from Arizona cases specifically, or can they be from West Coast Trial Lawyers' general recovery history (which is heavily California-weighted — 7 of WCTL's 11 markets are CA)?

**The answer (Saul-ruled):** They can be from WCTL's general history. AZ ER 7.1 and the analogous ABA Model Rule 7.1 do **not** require state-specific settlement examples. What they require:

1. **The settlements must be actual WCTL recoveries.** ✅ — the table now shows real WCTL settlements per `WCTL_Market_Intelligence_Brief.md`.
2. **Past-results disclaimer.** ✅ — *"Past results do not guarantee a similar outcome. Settlement amounts depend on case-specific facts."* per `../06_COMPLIANCE_PACK.md` Section 4.
3. **The case facts shown must be reasonably comparable to the prospective claimant's situation.** ✅ — the three picks (wrongful death, truck, pedestrian) match qualifying case types under WCTL Service Agreement Section 1.3.
4. **The firm must be authorized to practice in the jurisdiction of the audience.** ✅ — WCTL has a Phoenix, AZ office, and Section 11.2 of the WCTL Service Agreement warrants WCTL is licensed to practice law in Arizona.

**What would NOT be compliant:**
- ❌ Showing settlements from a firm not licensed in AZ
- ❌ Showing settlements that aren't actual recoveries by the named firm (e.g., industry averages, comp data, "similar cases settle for X")
- ❌ Implying the AZ claimant will receive a similar outcome ("Get $19.4M for your case")
- ❌ Showing settlements without the past-results disclaimer

**Strategic recommendation (not a compliance requirement):** If WCTL has any AZ-specific recoveries, including at least one in the table is *more persuasive* — the claimant pattern-matches "this firm recovers in MY state." It's not required, but it's stronger. Action item for Sasha: ask WCTL/Robert if any Phoenix-office recoveries can be added to the substantiation file, even smaller-dollar ones, for future creative variants. The current three picks are compliant either way.

> **Saul:** Geo-specificity is a strategy lever, not a compliance lever. The Bar doesn't say "you can only show CA cases in CA ads." But if a competitor or a disgruntled claimant ever files a complaint, the closer the case facts shown are to actual AZ outcomes, the harder it is to argue the ads were misleading. Mix in an AZ case if WCTL has one. Otherwise, the firm-general settlements with proper disclaimers are GREEN.

---

## 5B. Settlement Numbers in Fair Case Ads (Davis's follow-up question)

**The question:** Can we use WCTL's social proof numbers ($1.7B+ recovered, specific settlements like $19.4M wrongful death, $3.85M truck) in the Fair Case **ads** themselves, not just on the form?

**The answer (Saul + Hegarty pulled in for the brand-fit read):** Layered. State bar says yes; brand and platform say be careful.

| Layer | Verdict | Reason |
|---|---|---|
| **AZ ER 7.1 (state bar)** | ✅ Compliant | Actual WCTL recoveries + past-results disclaimer + WCTL is AZ-licensed (Section 11.2 of WCTL Service Agreement). Same logic as form-side ruling in 5A above. |
| **Meta platform policy** | ⚠️ Yellow zone | Meta's sensational/exploitative content rules flag settlement-amount creative even when state bar approves. Specific dollar mentions sit at YELLOW per `Saul.md` Section 5 Quick Reference. Runnable but elevates account risk. Watch CPMs — if they spike, kill the creative. |
| **WCTL brand fit** | ❌ Probable Neama veto | Per `WCTL_Market_Intelligence_Brief.md` line 53: Neama "would be personally furious if he saw what the current vendors' ads actually look like running under his name — especially anything with crash footage, **settlement promises**, or prohibited content." The Second Chair pitch was that we *don't* run those ads. Putting $19.4M in a Meta ad would be the exact creative register Neama is trying to escape from. |
| **SC creative register** | ❌ Wrong register | The locked Elevated Documentary direction for WCTL ads is empathy-driven and restrained. Specific settlement numbers prime greed/scare register, which is the opposite of where the brand lives. |

**Recommendation (locked):**
- ❌ **Do NOT use specific settlement amounts** ($19.4M / $3.85M / $1.75M / etc.) in ad creative for Fair Case → WCTL Arizona.
- 🟡 **The aggregate `$1.7 Billion+ recovered` is defensible in ads** with the past-results disclaimer, but: use sparingly, never as the hook line, only as a closing card stat under the Elevated Documentary register. Run past Neama before lighting it up.
- ✅ **"97% of qualifying cases reach a settlement or verdict"** is the strongest authority signal for ads — cleaner than dollar numbers, doesn't trigger the exploit/greed register, no ER 7.1 substantiation issues if WCTL's actual data backs it.
- ✅ **Specific settlement amounts belong ON THE FORM, not in ads.** The form's closing-step social proof block (`../05_FINAL_STEP_SOCIAL_PROOF.md`) is where they earn their place — by then the claimant has invested ~90 seconds and is in evaluation mode, not scroll mode. Ad context = scroll. Form context = decision.

**If Davis wants to test settlement numbers in ads anyway:**
1. Run past Neama via Robert FIRST. Get explicit greenlight, not silence.
2. Use only the aggregate `$1.7B+`, never specific case verdicts.
3. Disclaimer on every frame: *Past results do not guarantee a similar outcome.*
4. Pair with the elevated documentary register (restraint, not numbers theater).
5. Watch CPMs daily for the first week. If Meta starts pushing them up, that's the algorithm's reaction — kill it.
6. Document the test: copy variant, dates, performance, Neama's reaction.

> **Saul:** State bar is the easy gate here. The hard gates are Meta's algorithm and your client's brand sensibility. Both have higher costs of failure than an ER 7.1 complaint. ER 7.1 is a 14-day-response process; Meta restriction is the account dies same-day; Neama's reaction is the relationship dies. Order your concerns by which one ends the program fastest — specific settlement numbers in ads aren't worth it for an extra few percent in click-through.

> **Hegarty (pulled in for the brand-fit read):** Settlement numbers in creative are the language of the firms WCTL is trying not to be. If we put $19.4M on a Fair Case ad serving Phoenix, we just made WCTL look like every other lead-vendor ad Neama wishes he could un-buy. The win is in the empathy-driven register, not the numbers register. Keep the numbers on the form, where they're earned.

---

## 6. Comparative-Fault Disclosure

Arizona is a pure comparative-fault state under A.R.S. § 12-2505. A claimant who is partially at fault can still recover, reduced by their fault percentage. This is relevant to:

- **Step 4 question copy** — McCabe's reassurance ("Even partial fault doesn't stop most cases") is factually accurate under AZ law.
- **Step 4 expansion copy** — The "Why we're asking" expansion (`04_OBJECTION_COPY_FRAMEWORK.md`) explicitly mentions Arizona as a comparative-fault state. That fact is correct.

> **Saul:** This is not a compliance requirement per se — it's a factual accuracy requirement. ER 7.1 prohibits misleading communications, and saying "any fault kills your case" would be misleading in AZ. We don't say that; we say the opposite, accurately. Good.

---

## 7. Saul's AZ Traffic-Light Audit

The form, with everything in `06_COMPLIANCE_PACK.md` and this overlay shipped:

| Layer | Status |
|---|---|
| ER 7.1 (substantiation) | 🟢 **Green** — pending Sasha's substantiation file |
| ER 7.2 (fee references) | 🟢 **Green** |
| ER 7.3 (solicitation) | 🟢 **Green** — inbound only |
| ER 7.5 (trade names) | 🟢 **Green** — "not a law firm" disclosed |
| TCPA 2025 (one-to-one consent) | 🟢 **Green** — WCTL named explicitly |
| Meta platform (Personal Attributes) | not applicable to form (the *ads driving traffic* must pass separately) |
| A.R.S. § 12-542 (SOL) | 🟢 **Green** — form filters out >2-year cases |

**Overall: 🟢 GREEN** for AZ + WCTL launch, contingent on:
- Sasha producing the substantiation file (Section 2 action item)
- Engineering implementing the form changes in `01_QUESTION_COPY.md`, `02_SOFT_TISSUE_GATE.md`, `06_COMPLIANCE_PACK.md`, `03_BRAND_MARK_AND_LAYOUT.md`
- TrustedForm + Jornaya certificates capturing the rendered "West Coast Trial Lawyers" consent text

---

## 8. References

- Arizona Rules of Professional Conduct (ER 7.1, 7.2, 7.3, 7.5) — `https://www.azcourts.gov/rules/`
- A.R.S. § 12-542 (statute of limitations on PI)
- A.R.S. § 12-2505 (comparative fault)
- ABA Model Rules of Professional Conduct (parallel reference)
- Section 5.1 + Section 8.1 of WCTL Service Agreement (TCPA + AZ ER compliance obligations)
- `../../../06_Legal/Rulebook/04_State_Bar_Rules.md` (extended with new Arizona section per this brief)
- `../../../06_Legal/Rulebook/01_TCPA_Consent_2025.md`

---

*AZ overlay locked. Pending substantiation file from Sasha. Saul on call for any pre-launch question.*
