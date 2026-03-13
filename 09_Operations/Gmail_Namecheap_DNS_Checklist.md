# Gmail (Google Workspace) + 2ndchair.net — DNS Checklist

**Purpose:** Get Gmail verification and delivery working. Use this to confirm every value is correct and to fix the “Unable to verify at the moment” error.

**Domain:** `2ndchair.net`  
**Last updated:** March 2026

---

## 1. Where is DNS actually hosted? (Do this first)

Your docs say **“Nameservers pointed at Vercel”** for `2ndchair.net`.  
If that’s true, **the internet uses Vercel for DNS, not Namecheap.** Anything you add only in Namecheap won’t be seen by Google.

**Check:**
- Namecheap → Domain List → **Manage** on `2ndchair.net` → **Nameservers**.
- If it says **Custom DNS** and shows Vercel nameservers (e.g. `ns1.vercel-dns.com`, `ns2.vercel-dns.com`), then **all** records below must be added in **Vercel** (Project → Domains → `2ndchair.net` → DNS records), not in Namecheap.
- If it says **Namecheap BasicDNS** (or similar), then Namecheap is authoritative and you add/check everything in Namecheap.

**If DNS is at Vercel:** Add every record in this doc in Vercel’s DNS UI. Namecheap’s Advanced DNS / Mail Settings won’t affect Google.

---

## 2. Exact values to use (copy‑paste, no typos)

Use these exactly. Common mistakes: wrong Host (`@` vs blank vs `2ndchair.net`), missing trailing dot, O vs 0 in verification strings.

### 2.1 Domain verification (Google “Unable to verify” fix)

**Option A — TXT (what you have):**

| Field   | Value |
|--------|--------|
| Type   | TXT   |
| Host   | `@`   |
| Value  | `google-site-verification=hfc1bh0yn0O6K2N8qSbsz_wyjFpmdNgvPOdoaTQK3uU` |
| TTL    | 300 or 1 min or Automatic |

Check: the character after `hfc1bh0yn0` is the letter **O** (oh), not the number **0** (zero). Google’s screen shows which they gave you.

**Option B — CNAME (you also have this):**

| Field   | Value |
|--------|--------|
| Type   | CNAME |
| Host   | `2tk2op6lxlgx` |
| Value  | `gv-5pqbqspp76mjrh.dv.googlehosted.com.` (trailing dot) |
| TTL    | 300 or 1 min |

---

### 2.2 MX record (required for Gmail to receive mail)

Google’s current value: **one MX record**.

| Field    | Value |
|----------|--------|
| Type     | MX    |
| Host     | `@` (or leave blank if your host means “root domain”) |
| Priority | **1** (not 10) |
| Value    | `smtp.google.com` or `smtp.google.com.` (some hosts require the trailing dot; Namecheap often does) |
| TTL      | Automatic or 3600 |

**Important:** Delete any other MX records (e.g. old mail host, parking, “email by namecheap”) before or right after adding this. Multiple MX records can cause verification and delivery issues.

---

### 2.3 SPF (TXT)

| Field   | Value |
|--------|--------|
| Type   | TXT   |
| Host   | `@`   |
| Value  | `v=spf1 include:_spf.google.com ~all` |
| TTL    | Automatic |

Only one SPF record for the domain. If you have another (e.g. from an old provider), merge into one or remove the old one.

---

### 2.4 DKIM (TXT)

Google gives you a long string in Admin → Apps → Google Workspace → Gmail → Authenticate email.

| Field   | Value |
|--------|--------|
| Type   | TXT   |
| Host   | `google._domainkey` (Namecheap may show it as `google._domainkey.2ndchair.net` — use what the host expects for “root” or “@”) |
| Value  | (paste the full value from Google, e.g. `v=DKIM1; k=rsa; p=MIIBIjAN...`) |
| TTL    | Automatic |

---

### 2.5 DMARC (TXT)

| Field   | Value |
|--------|--------|
| Type   | TXT   |
| Host   | `_dmarc` |
| Value  | `v=DMARC1; p=none; rua=mailto:davis@2ndchair.net` |
| TTL    | Automatic |

In Namecheap use **Host:** `_dmarc` only — do not put `_dmarc.2ndchair.net` (they append the domain).

---

## 3. Namecheap-specific

- **Advanced DNS** is where TXT, CNAME, and often MX live. Don’t rely only on “Email” or “Mail Settings” unless that’s where your **authoritative** DNS is (see section 1).
- If you use **Mail Settings → Gmail**, it should add MX for you; then in **Advanced DNS** you still must have SPF, DKIM, DMARC, and the Google verification TXT/CNAME.
- **MX in Namecheap:** If MX is in a separate “Mail” section, use Priority **1** and server **smtp.google.com.** (with trailing dot if Namecheap asks for FQDN).

---

## 4. Verify what the internet sees

1. **Google Admin Toolbox (Dig)**  
   - Open: [https://toolbox.googleapps.com/apps/dig/#MX/](https://toolbox.googleapps.com/apps/dig/#MX/)  
   - Name: `2ndchair.net` (no www).  
   - Check MX shows `smtp.google.com` (or the legacy set if you used that).  
   - Run **TXT** for `2ndchair.net` and confirm the Google site verification and SPF strings appear.

2. **MXToolbox**  
   - [https://mxtoolbox.com/SuperTool.aspx](https://mxtoolbox.com/SuperTool.aspx)  
   - MX Lookup: `2ndchair.net`  
   - SPF Lookup: `2ndchair.net`  
   - DMARC Lookup: `2ndchair.net`

3. **Retry in Google**  
   - After saving DNS, wait 5–15 minutes (TTL 1 min) or up to 48 hours if your host uses longer TTL.  
   - In Google Workspace setup, click **Retry** / **Verify**.

---

## 5. Quick fix list if verification still fails

- [ ] DNS is really at Namecheap (not Vercel)? If at Vercel, add all records in Vercel.
- [ ] Verification TXT or CNAME matches Google exactly (O vs 0, no extra spaces).
- [ ] Only one MX record: priority 1, value `smtp.google.com` (or `smtp.google.com.`).
- [ ] No other MX records (delete old/parking mail records).
- [ ] SPF is exactly `v=spf1 include:_spf.google.com ~all` on Host `@`.
- [ ] DKIM host is exactly what Google shows (e.g. `google._domainkey`); value pasted in full.
- [ ] Waited at least a few minutes (or up to 48 hours) and clicked Retry in Google.

---

*Reference: [Google — Set up MX records](https://support.google.com/a/answer/174125); splash page / Gmail setup convo.*
