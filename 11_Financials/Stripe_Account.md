# Stripe Account — Second Chair LLC

Living reference for the Second Chair Stripe account: configuration decisions, support history, and operational notes.

---

## Account snapshot

| Field | Value |
|---|---|
| Legal entity | Second Chair LLC |
| EIN | 41-516-6795 |
| State of formation | California |
| Formation date | March 19, 2026 |
| Principal address | 522 Marine Street, La Jolla, CA 92037 |
| Business type | Multi-member LLC (3 members @ 33.3% each) |
| Members | William Davis Ballard · [Member 2] · Alexander Zinshtein |
| MCC / Category | Professional services → Other marketing services |
| Payout bank | Bank of America business checking (ACH 121000358 / Acct ...8622) |
| Payout schedule | Manual |
| 2FA | Passkey + Authenticator app (backup codes saved in 1Password) |

## Payment configuration

- **Enabled methods (account-wide):** Card, ACH Direct Debit
- **Disabled:** all foreign payment methods, all consumer wallets (Cash App / Apple Pay / Google Pay / Link / Amazon Pay), all BNPL (Affirm / Klarna / Afterpay / Sunbit / Zip), Stripe Tax
- **Per-invoice override:** ACH can be removed for clients who agreed to pay by card (e.g., Tofer)

## Pricing & fee policy

- **Standard policy:** ACH preferred (no fee); credit card payments incur a full **3% processing fee** passed through to the client
- **Tofer & Associates exception:** 50/50 split — Tofer pays 1.5%, Second Chair absorbs 1.5% (one-off courtesy, not standing policy)
- Stripe ACH fee: 0.8% capped at $5
- Stripe card fee: 2.9% + $0.30

## Standard invoice memo (template)

> Payment terms: Net 10 from invoice date.
>
> ACH bank transfer is preferred — no fees for either party. Use the secure payment link at the top of this invoice and select "Bank account."
>
> Wire transfer available on request — reply to this invoice and we'll send instructions.
>
> Credit card payments incur a 3% processing fee. Reply if you'd prefer this option and we'll send an updated invoice.
>
> Billing questions: sasha@2ndchair.net

## Standard invoice footer

> Second Chair LLC · EIN 41-516-6795 · 522 Marine Street, La Jolla, CA 92037 · W-9 available on request.

---

## Support case history

### 2026-04-30 · Account onboarding heads-up

- **Case ID:** `sco_UR2OcM0ImE2Ukd`
- **Channel:** Stripe live chat
- **Subject:** Proactive notification of incoming high-value B2B invoice on a new account
- **What was communicated:**
  - Business model (B2B marketing services for US PI law firms)
  - Typical invoice range $40k–$110k, up to $200k
  - Primarily ACH, card secondary
  - First incoming invoice ~$53,795 from Tofer & Associates, paid by credit card
- **Stripe response:** Specialized team informed; note placed on account.
- **Purpose:** Avoid first-transaction hold (typical for new accounts on 5-figure incoming payments).

---

## Useful Stripe links

- Dashboard: https://dashboard.stripe.com/
- Support phone: +1 (888) 926-2289
- Account settings → Business: https://dashboard.stripe.com/settings/business
- Payouts: https://dashboard.stripe.com/settings/payouts
- Invoices: https://dashboard.stripe.com/invoices

---

*Update this file whenever account config changes, a new support case opens, or fee/payment policy shifts.*
