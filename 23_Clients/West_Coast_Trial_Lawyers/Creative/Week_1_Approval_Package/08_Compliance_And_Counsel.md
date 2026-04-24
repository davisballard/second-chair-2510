# 08 — Compliance & Counsel

**Scope:** AZ Bar ER 7.1 / 7.2 / 7.3 position, Meta Special Ad Category policy citations, and the specific counsel-review routing for M2-V3 dramatization.

**Audience:** WCTL's Arizona-licensed counsel (for §7.1 approval window) + Robert for situational awareness.

---

## 1. Arizona Rules of Professional Conduct (ER 7.1, 7.2, 7.3)

**ER 7.1 — Communications Concerning a Lawyer's Services**

Operative rule: a lawyer shall not make a *false or misleading communication* about the lawyer or the lawyer's services. "False or misleading" means:
- Contains a material misrepresentation of fact or law
- Omits a fact necessary to make the statement not materially misleading
- Creates unjustified expectations about results the lawyer can achieve
- States or implies the lawyer can achieve results by means violating the Rules

**Position across all 24 variants in this package:**
- Zero guaranteed-results language
- Zero specific case-outcome claims ("We won $X" / "Average settlement $Y")
- All numeric props (e.g., "$18,000 offer" in Diana S5-V3, "$35,000" in Sarah S1 agitation beat, "$47,000 ER" in Ty M1-V2) are framed as *illustrative of insurance-company lowball dynamics*, not WCTL results
- All creative directs viewers to a "free case review" or similar evaluative framing — it offers consultation, not outcome
- Every hook and body copy element has been filtered for truthfulness before inclusion

**ER 7.2 — Permitted Media**

Arizona permits advertising through any public media. No restriction on Meta/Facebook/Instagram placement for lawyer advertising. Disclosure requirements (name of firm, location of office) met via WCTL branding + landing-page disclosures.

**ER 7.3 — Solicitation of Clients**

Prohibition is on live, in-person, or real-time electronic contact with a specific prospect. Advertising that *invites a prospect to initiate contact* (fill out a quiz, click Learn More, visit a website) is not solicitation and is permitted. **Every variant in this package uses third-person framing in the ad itself** — the ad describes a situation ("Hit while crossing the street?" "Riders don't ask for sympathy") without asserting personal attributes about the viewer. Viewer initiates by clicking CTA.

### AZ-specific notes on reenactments

Arizona is classified as **"Cautious (not banned)"** on reenactments and crash-adjacent imagery. Permitted with disclosure. "Dramatization" overlay is the accepted disclosure format. See M2-V3 section below for the specific application.

---

## 2. Meta Special Ad Category — Policy Position

**Campaign setup (already confirmed in Doc 6):** Special Ad Category set to "Social Issues, Elections or Politics." This categorization is required for legal-services advertising on Meta. It restricts detailed interest/behavior/audience-based targeting (no "people interested in personal injury law," no lookalike audiences based on past customers). Geographic targeting by state/zip is permitted.

**Personal Attributes Policy:**

Meta prohibits ads that assert or imply personal attributes of the viewer. Examples of forbidden phrasing:
- "Are YOU injured?" — asserts injury attribute
- "Were YOU in a crash?" — asserts event attribute about viewer
- "If YOU were hit by a truck..." — asserts attribute

Examples of **permitted** phrasing (used throughout this package):
- "Hit by a semi on I-10?" — question form, third-person framing, no attribute assertion
- "Riders don't ask for sympathy" — community observation, not viewer attribute
- "A driver didn't see the rider" — third-person causal statement

Every hook in this package is written to comply. Body copy in each variant uses "if you were seriously injured" only in conditional phrasing that describes a category, not a viewer assertion.

**Violent and Graphic Content Policy (Transparency Center 2026):**

**Prohibited:**
- Visible innards (exposed organs, bones, muscle tissue) — even in health contexts
- Shocking, sensational, or excessively violent content
- Crash footage with graphic injury detail or victim distress (screaming, panic, suffering)

**Permitted:**
- Reenactments and dramatizations if labeled ("This is a dramatization")
- Impact/collision moments if contextualized (no gore, no victim focus)
- Recovery imagery (casts, crutches, slings, mobility aids) without graphic content
- Third-person educational framing

**Position across all 24 variants in this package:**
- 23 of 24 variants use pure absence/aftermath doctrine — no crash imagery whatsoever
- 1 variant (M2-V3) uses a compliant moment-before + cut-to-black construction with "Dramatization" overlay; see §4 below
- Recovery props (arm brace on Sarah, sling on Diana, cane on Laura, leg brace/crutch on Ty, cracked helmet on Ty M3-V3) are compliant visible severity indicators without graphic content

**Sponsored-post disclosure:** All ads run under Meta's standard "Sponsored" label via the ad placement system. UGC-Native creatives (Diana ×4, M2-V1 UGC, S1-V3 UGC) still surface the Sponsored label — we do not suppress it and do not disguise sponsored content as organic.

---

## 3. TCPA & Landing-Page Disclosures

Per signed Service Agreement §7.1-§7.2 and Doc 6 §9 funnel spec:

- **"Not a law firm" disclosure:** Landing page header or footer states Second Chair is a lead-generation platform and not a law firm. WCTL appears as the attorney relationship.
- **TCPA 1-to-1 consent:** Step 6 of the quiz funnel (contact-info step) includes an explicit consent line naming West Coast Trial Lawyers as the party authorized to contact the lead via call, text, or email.
- **"This is an advertisement" disclosure:** Present in the landing page footer.

Full disclosure language lives in `lead-gen/apps/second-chair-website/` (SC website repo) under the AZ-specific landing page. Counsel can review the live landing page via staging URL on request.

---

## 4. M2-V3 Dramatization — Heightened Review Section

**This section is the specific material WCTL counsel should review before launching M2-V3.** Separate email inbound with storyboard frames and this section in isolation.

### 4a. The creative

**Hook:** *"Southern and Dobson. 4:45 PM. Full sun. She never looked right."*
**Full 15-second breakdown:** See `05_M2_Ty_Loss.md` §Variant M2-V3.
**Format:** 15-second vertical video (9:16 Reels / 4:5 feed / 1:1 square), dashcam-POV simulation approaching a suburban AZ intersection, generic silver/white SUV enters frame from opposite direction, driver's head visible turning left (not right), cut to black at 7-8s before any impact, cut to Ty composed at home for remainder.

### 4b. Compliance position

**AZ Bar:** Reenactments-with-disclosure are expressly permitted. "Dramatization" overlay (white sans-serif, 40% opacity black card, bottom-right corner, 11pt minimum, visible frames 1 to 15) is the disclosure. No identifiable person (driver face obscured/turned), no identifiable vehicle (generic SUV, no plate visible). No specific case-outcome claim. **Position: GREEN under ER 7.1 with counsel sign-off.**

**Meta Special Ad Category:** Implied-impact-without-gore-or-victim is permitted. The cut-to-black is the industry-standard compliant treatment for this kind of implication. **Position: GREEN at human review, AMBER on algorithmic reach** — Meta's algorithm may deprioritize (rate-limit) even after human review approval if it perceives sensational content. Budget accordingly; M1 and M3 absorb impressions if M2-V3 throttles.

**Second Chair brand doctrine:** SC's prior "no crash footage" position was a brand-discipline choice modeled on California's stricter SB-37 standard. Davis has explicitly re-evaluated: for the AZ market specifically, a tactfully-executed Moment-Before Dramatization is consistent with "honest persuasion over shock factor" — it makes the factual argument for Ty's innocence visible rather than asking viewers to take it on faith. The treatment does not rely on shock value; it relies on the *specificity* of the intersection and the *factual* structure of the events (full sun, driver turned left-not-right, no impact shown).

### 4c. What counsel is being asked to approve

1. The creative as specified above, including the dashcam-POV simulation, generic SUV rendering, cut-to-black timing, and "Dramatization" overlay specification.
2. Storyboard frames (5-6 key frames — to be sent with this document in the heightened-review email). These frames show structure without committing to final generation; Davis will re-render to counsel-specified edits if requested.
3. The associated hook copy and body text as written in `05_M2_Ty_Loss.md`.

### 4d. What counsel is NOT being asked

- Counsel is not reviewing the 23 other variants in this package via the heightened-review email — those go through standard Service Agreement §7.1 approval with the main package email.
- Counsel is not reviewing the campaign architecture, media plan, or funnel spec — those were settled in the April call and signed.

### 4e. Fallback if counsel declines

If counsel finds M2-V3 non-compliant or wants substantive edits that can't be produced within the Fri 2026-05-01 response window:
- **M2-V3 is held for Phase 2.** Not included in 2026-05-05 launch.
- M2 launches with primary + V1 + V2 only (three units instead of four).
- Package is unchanged otherwise.

---

## 5. Compliance sign-off checklist (for counsel)

Before WCTL counsel signs off on the package, please confirm:

- [ ] All 24 hooks use third-person framing per Meta Personal Attributes policy (§2 above)
- [ ] All body copy is free of guaranteed-results language per AZ ER 7.1 (§1 above)
- [ ] Numeric props ($18K offer, $35K offer, $47K ER, etc.) are framed as illustrative, not as WCTL case results
- [ ] Recovery props (arm brace, sling, cane, leg brace, cracked helmet) are not paired with graphic injury content
- [ ] "Free case review" CTA does not cross into solicitation under ER 7.3 — ad invites contact, does not initiate it
- [ ] M2-V3 dramatization (separate review) — if approved, "Dramatization" overlay visible frames 1–15s, generic SUV rendering, no identifiable driver, cut-to-black timing at 7-8s

Any flag → edit required before Meta submission (Sun 2026-05-03 EOD).

---

## 6. Sources

**Internal (reference only, not re-attached):**
- `Abracadabra/08_Brands/Second_Chair/05_Restrictions/arizona/State_Rules.md` — full AZ ER 7.1 / 7.2 / 7.3 text + Saul's annotations
- `Abracadabra/08_Brands/Second_Chair/05_Restrictions/Platform_Rules.md` — Meta Special Ad Category, Personal Attributes, Violent-Graphic-Content policies

**External (public policy documents):**
- Arizona Rules of Professional Conduct, ER 7.1-7.5 (Supreme Court of Arizona)
- Meta Transparency Center — Advertising Standards: Violent and Graphic Content (transparency.meta.com)
- Meta Special Ad Category policy (Meta Ad Standards)
- TCPA (Telephone Consumer Protection Act), 47 U.S.C. § 227, and FCC 1-to-1 consent rule (effective 2024-01-27)

Happy to share the external policy language verbatim in a separate document on request.
