# Second Chair — Website Tech Stack & Deployment
## `02_Tech_Stack_And_Deployment.md`

> **Document Purpose:** Authoritative reference for how the Second Chair website is coded, updated, and deployed. Covers the full pipeline from local editing in Cursor through GitHub to live production on Vercel. Includes framework migration roadmap. Read this first before touching any website code.
>
> **Last Updated:** March 2026

---

## TECH PHILOSOPHY

Build in stages. Don't carry framework weight before the design is locked.

**Phase 1 — Vanilla HTML/CSS/JS**
Start here. No build tools, no dependencies, no compile step. Open `index.html` in a browser and the site is running. Every design decision can be made and reversed instantly. Cursor edits, browser refreshes, ship. The goal at this stage is getting the design right — not optimizing infrastructure that doesn't exist yet.

**Phase 2 — Framework Migration (Next.js / Svelte)**
Once the design is signed off and content is finalized, rebase into the appropriate framework. The vanilla build is the blueprint — components map 1:1 to the existing HTML sections, CSS carries over. No redesign, no scope creep. This is a technical lift, not a creative one.

- **Main website** → Next.js (React 19), App Router, native Vercel support
- **Funnels** → Svelte (separate codebase and repo)

**Phase 3 — Edge Performance**
After the framework is in place: image optimization (`next/image`), font subsetting, lazy loading, caching headers. Vercel's Edge Network handles CDN distribution automatically. Target: Core Web Vitals green across all pages.

**Rationale:** Design decisions made in vanilla are faster and cheaper to change. Framework overhead during discovery creates friction without benefit. Build correct first, then build fast.

---

## LOCAL DEVELOPMENT

| Item | Detail |
|------|--------|
| **Website source** | `18_Website/` inside this brand files repo |
| **Editor** | Cursor |
| **Preview (Phase 1)** | Open `index.html` directly in browser, or run a local server (`npx serve .`) for anything requiring relative paths |
| **Build step (Phase 1)** | None — static HTML, no compilation required |
| **Build step (Phase 2)** | `next dev` for local Next.js development |

### File Structure (Phase 1)

```
18_Website/
├── index.html
├── css/
│   └── styles.css
├── js/
│   └── main.js
├── images/
└── fonts/
```

### Editing Workflow

1. Open the `18_Website/` folder in Cursor
2. Edit `index.html`, `css/styles.css`, or `js/main.js`
3. Refresh browser to preview
4. When happy with a change, commit and push to the website repo (see below)

---

## GITHUB WORKFLOW

The website has its **own dedicated GitHub repo**, separate from the brand files repo.

| Item | Detail |
|------|--------|
| **Website repo** | `https://github.com/davisballard/second-chair-website-5220` |
| **Brand files repo** | `https://github.com/davisballard/second-chair-2510` (this repo — brand docs only, not deployed) |
| **Branch** | `main` |
| **Deploy trigger** | Every push to `main` auto-deploys to Vercel |

### Push Workflow

```bash
# Navigate to the website repo (cloned separately)
cd ~/second-chair-website-5220

# Stage and commit changes
git add -A
git commit -m "describe what changed"

# Push — Vercel deploys automatically
git push origin main
```

> The `18_Website/` folder inside this brand files repo is the working copy. Keep the website GitHub repo (`second-chair-website-5220`) in sync with it. The brand files repo (`second-chair-2510`) is for brand documentation only and is not connected to Vercel.

---

## VERCEL DEPLOYMENT

| Item | Detail |
|------|--------|
| **Connected repo** | `second-chair-website-5220` |
| **Root directory** | `/` |
| **Build command (Phase 1)** | None — Vercel serves static HTML directly |
| **Build command (Phase 2)** | `next build` |
| **Output directory (Phase 2)** | `.next` |
| **Deploy time** | ~30 seconds from push to live |
| **Preview deployments** | Every branch push gets a unique preview URL from Vercel |

Every push to `main` triggers an automatic production deployment. Non-`main` branch pushes create preview URLs — useful for reviewing changes before merging.

---

## DOMAIN

| Item | Detail |
|------|--------|
| **Domain** | `2ndchair.net` |
| **DNS** | Nameservers pointed at Vercel |
| **SSL** | Handled automatically by Vercel |
| **Production URL** | `https://2ndchair.net` |

Vercel manages SSL certificate issuance and renewal. No manual certificate management required. The domain resolves through Vercel's global edge network.

---

## PHASE 2 — FRAMEWORK MIGRATION (MAIN WEBSITE)

**Trigger:** Design is signed off. Content is final. No more layout or copy changes expected.

**Target framework:** Next.js (React 19), App Router

**Why Next.js:**
- First-party Vercel support — zero configuration for deployment
- App Router enables server components, streaming, and edge rendering
- React 19 server actions simplify form handling (apply/contact forms)
- `next/image` handles image optimization natively
- ISR (Incremental Static Regeneration) available if content becomes dynamic

**Migration steps:**
1. Initialize Next.js project in a fresh branch of `second-chair-website-5220`
2. Map each HTML section → a React component (`Hero`, `CreativeWork`, `Moat`, `Founders`, `Proof`, `HowWeWork`, `CTA`, `Footer`)
3. Port CSS to CSS Modules or Tailwind (decision to be made at migration time)
4. Update Vercel build config: build command → `next build`, output → `.next`
5. QA on preview URL before merging to `main`

---

## PHASE 2 — FUNNELS (SVELTE)

Funnels are a **separate codebase** from the main website.

| Item | Detail |
|------|--------|
| **Framework** | Svelte (SvelteKit recommended) |
| **Repo** | Separate GitHub repo (TBD — create when funnel build begins) |
| **Deployment** | Vercel (separate project) or alternative TBD |
| **Relationship to main site** | Funnels link to/from the main site but are independent codebases |

**Why Svelte for funnels:**
- Minimal bundle size — critical for paid traffic landing pages where every millisecond of load time affects conversion
- No virtual DOM overhead
- Reactive state management is built in — ideal for multi-step form flows
- SvelteKit handles routing, SSR, and form actions cleanly

---

## PHASE 3 — EDGE PERFORMANCE

Begins after Phase 2 framework migration is complete and stable.

| Optimization | Tool / Approach |
|---|---|
| Image optimization | `next/image` (automatic format conversion, lazy loading, sizing) |
| Font loading | Self-hosted with `font-display: swap`, subset to used characters |
| JS bundle size | Next.js code splitting by default; audit with `@next/bundle-analyzer` |
| Caching | Vercel Edge caching headers; static assets cached at edge nodes |
| Core Web Vitals | Target: LCP < 2.5s, CLS < 0.1, INP < 200ms |
| Analytics | Vercel Analytics for real-user performance data |

---

## QUICK REFERENCE

```
Edit locally in Cursor (18_Website/)
    ↓
Commit + push to second-chair-website-5220 (main)
    ↓
Vercel auto-deploys
    ↓
Live at https://2ndchair.net (~30 seconds)
```

**Website repo:** `https://github.com/davisballard/second-chair-website-5220`
**Production URL:** `https://2ndchair.net`
**Deployment platform:** Vercel
**Phase 1 stack:** Vanilla HTML / CSS / JS
**Phase 2 stack (website):** Next.js (React 19)
**Phase 2 stack (funnels):** Svelte (SvelteKit)
