# Instantly.ai Setup & Workflow Guide

> **Updated:** March 24, 2026
> **Plan needed:** Outreach Hypergrowth ($97/mo) — NOT Growth. Growth only lets you preview replies, not respond from Unibox.
> **Optional add-on:** CRM Growth ($47/mo) for pipeline/deal tracking inside Instantly.

---

## 1. Connect Your Gmail Accounts (OAuth Method)

Since you're on Google Workspace (2ndchair.net):

1. In Instantly: **Email Accounts** → **Add New** → **Google** → **Option 1: OAuth**
2. Copy the Client ID that appears
3. Go to **admin.google.com** → Security → API Controls → Manage App Access → Configure New App
4. Paste Client ID, find "Instantly OAuth Email v1," set to **Trusted** for all users, click Finish
5. Back in Instantly: click Login, pick your Google account, click Allow
6. Repeat for each account (sasha@2ndchair.net, davis@2ndchair.net)

**Tip:** Use incognito browser windows when connecting each account to avoid cached login conflicts.

---

## 2. Enable Warmup (Keep Running Forever)

Even though the domain is already warmed, Instantly's warmup maintains reputation continuously.

**How to enable:** Email Accounts → click the **flame icon** on each account.

**Settings:**

| Setting | Value |
|---------|-------|
| Daily Warmup Limit | 10 |
| Reply Rate | 30% |
| Spam Protection | ON |
| Read Emulation | ON |
| Weekdays Only | ON |
| Mark Important | ON |
| Disable Slow Warmup | Can enable (domain is pre-warmed) |

**Warmup Health Score** on the dashboard should be **90%+** before launching campaigns. Warmup emails do NOT count against your daily sending limits.

**Never turn warmup off.** Even when campaigns are running. Even months from now.

---

## 3. Create Campaigns (One Per Timezone)

**Important: Instantly does NOT auto-detect recipient timezones.** You set one timezone per campaign. Since you're targeting 10 Markets across multiple timezones, create separate campaigns:

| Campaign Name | Markets | Timezone | Send Window |
|---------------|------|----------|-------------|
| `Tier1_Eastern` | NYC, Miami, Philly, Atlanta | America/New_York | 9:00 AM - 12:00 PM ET |
| `Tier1_Central` | Chicago, Dallas, Houston | America/Chicago | 9:00 AM - 12:00 PM CT |
| `Tier1_Pacific` | LA, SF, San Diego | America/Los_Angeles | 9:00 AM - 12:00 PM PT |

You can create additional campaigns for Tier 2/3 segments following the same timezone split.

**Send days:** Tuesday, Wednesday, Thursday only.

**Sending window math:** With a 9-minute gap between emails and 20 emails/day per account, you need at least a 3-hour window. A 9:00-12:00 PM window gives plenty of room.

---

## 4. Upload Prospects (CSV)

Go to campaign → **Leads** → **Add Leads** → **CSV**

### Required CSV format:

| Column | Maps To | Required? |
|--------|---------|-----------|
| Email | email | Yes (only truly required field) |
| First Name | firstName | Yes (for personalization) |
| Last Name | lastName | Optional |
| Company Name | companyName | Optional |
| City | Custom variable → `{{City}}` | Yes (for templates) |
| Market | Custom variable → `{{Market}}` | Recommended (for tracking) |
| Tier | Custom variable → `{{Tier}}` | Recommended (for tracking) |
| Firm Name | Custom variable → `{{firmName}}` | Yes (for subject lines) |

### Upload steps:
1. Upload .csv file (must be UTF-8 encoded)
2. Instantly auto-suggests column mappings — verify each one
3. Enable **deduplication** (prevents uploading leads already in another campaign)
4. Click **Upload All**

### Rules:
- Column names should start with capital letters
- Column names max 20 characters
- Remove empty columns before uploading
- **Variables are case-sensitive.** `{{firstName}}` is NOT `{{firstname}}`. Match your CSV headers exactly to what's in your email templates.
- You cannot delete custom variables after upload — map carefully

---

## 5. Write Your Email Sequence

In the campaign editor → **Sequences** tab:

1. **Step 1:** Write subject line + email body (your Touch 1)
2. Click **Add Step** for each follow-up
3. Set delay between steps: "Send next message in X days"
4. **Leave subject line blank on follow-ups** = sends as reply in same thread. New subject = starts fresh thread.
5. Use `{{firstName}}`, `{{City}}`, `{{firmName}}` for personalization
6. Click **Preview** to see how it renders with actual lead data

### Your 6-touch sequence maps like this:

| Step | Touch | Delay Setting | Sends On ~Day |
|------|-------|--------------|---------------|
| 1 | Credentials + honestly won | — | Day 0 |
| 2 | CPSC reframe | 3 days | Day 3 |
| 3 | Show the advertising | 4 days | Day 7 |
| 4 | Compliance angle | 3 days | Day 10 |
| 5 | Intake quality | 7 days | Day 17 |
| 6 | Breakup | 5 days | Day 22 |

**Note:** Delays count all calendar days including weekends. If the calculated send day falls on a non-active day (e.g., Sunday), Instantly sends on the next active day (Tuesday).

### A/B Testing:
Click **Add Variant** on any step to create alternative versions. Instantly rotates between them. Test subject lines on Steps 1 and 3 first — highest leverage.

---

## 6. Campaign Settings

In campaign **Options**, configure these before launching:

| Setting | Set To | Why |
|---------|--------|-----|
| **Stop Sending on Reply** | ON | Auto-pauses sequence when someone replies |
| **Stop Campaign for Company on Reply** | ON | Stops emails to all contacts at same firm when one replies |
| **Open Tracking** | **OFF** | Tracking pixel converts plain text to HTML, triggers spam filters |
| **Link Tracking** | **OFF** | Link rewrites get flagged by spam filters |
| **Send as Text-Only** | ON | Maximum deliverability |
| **Insert Unsubscribe Header** | ON | CAN-SPAM compliance |
| **Min Time Gap** | 9 minutes (default) | Natural sending pattern |
| **Random Additional Delay** | 5 minutes (default) | Avoids robotic timing |
| **Daily Limit Per Account** | 20 | Your target volume |
| **Max New Leads Per Day** | Set a cap | Prevents blasting full list on day 1 |

---

## 7. Launch and Monitor

### Before launching — checklist:
- [ ] Leads uploaded and variables mapped correctly
- [ ] Sequence written with personalization rendering properly (check Preview)
- [ ] Test email sent to yourself — confirm it looks right
- [ ] Sending accounts assigned to campaign
- [ ] Schedule set (correct timezone, Tue-Thu, 9-12 window)
- [ ] Open tracking OFF, link tracking OFF
- [ ] Warmup health score 90%+

### Launch:
Click **Launch.** Instantly drips emails during your sending windows automatically.

### Campaign Slow Ramp:
Enabled by default — starts at 2 emails on day 1, increases by 2/day until reaching your max (20). So it takes ~10 days to reach full volume on a new campaign. Since your domain is already warmed, you can disable this in Email Accounts → Settings → Campaign Slow Ramp. But monitor bounces closely if you do.

---

## 8. Handling Replies (Unibox)

**Unibox** is Instantly's unified inbox — pulls replies from all connected accounts into one view.

### How it works:
- All replies appear in Unibox automatically
- AI labels sentiment: positive, negative, neutral, interested, not interested
- You reply directly from Unibox (Hypergrowth plan required)
- No need to switch to Gmail

### What you see:
- Filter by: campaign, sending account, unread, positive/negative
- Search by email or domain
- Full conversation thread for each lead
- Quick actions: move to another campaign, add notes, set reminders

### When someone replies:
- Their sequence auto-pauses immediately (no more follow-ups sent)
- The reply appears in Unibox
- You respond personally within 2 hours (business hours)
- If it's a positive reply, mark as **Opportunity** → flows into CRM pipeline if you have the CRM add-on

---

## 9. Your Daily Workflow

**Afternoon/Evening — Write & Queue:**
1. Research prospects, build CSV with proper columns
2. Upload to the correct timezone campaign (Eastern, Central, or Pacific)
3. Write/review sequence steps
4. Everything queues automatically — Instantly sends during tomorrow's window

**Next Morning — Reply & Engage:**
1. Open Unibox → handle all replies (2-hour SLA)
2. Positive replies → schedule calls, mark as Opportunities
3. Negative replies → log reason, move to appropriate stage
4. Check for bounces → if any campaign exceeds 2% bounce rate, pause and re-verify list

---

## 10. Key Numbers

| Metric | Limit |
|--------|-------|
| Campaign emails per account per day | 30 max (you're setting to 20) |
| Warmup emails per day | 10 (don't count against the 30) |
| Total emails per account per day | ~30 campaign + 10 warmup = 40 |
| Sending window needed for 20 emails | ~3 hours minimum (9-min gaps) |
| Warmup health score target | 90%+ |
| Bounce rate ceiling | Below 2% |
| Spam complaint ceiling | Below 0.3% |

---

## 11. Common Mistakes to Avoid

1. **Sending before warmup is ready** — Wait for 90%+ health score
2. **Turning off warmup** — Keep it running forever, even during active campaigns
3. **Open/click tracking on cold email** — Disable both for best deliverability
4. **Variables don't match CSV headers** — Case-sensitive. `{{firstName}}` ≠ `{{firstname}}`
5. **Sending window too narrow** — 90 minutes only fits ~10 emails. Use 3-hour windows.
6. **One campaign for all timezones** — Create separate campaigns per timezone so emails land at 9-10 AM local time
7. **No deduplication on upload** — Always enable to prevent double-emailing leads in other campaigns
8. **Blasting full list day 1** — Set Max New Leads Per Day to ramp gradually
9. **Replying from Gmail instead of Unibox** — Use Unibox to keep everything tracked in one place
10. **Forgetting the address + opt-out** — CAN-SPAM requires physical address and unsubscribe in every email. It's in your templates — don't remove it.
