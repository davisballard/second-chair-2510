# Second Chair Geo-Targeting Framework — Methodology

**Owner:** Second Chair (Abracadabra brand)
**Location:** `Abracadabra/08_Brands/Second_Chair/04_Audience/Geo_Framework/`
**Status:** Active
**Version:** 1.1 (2026-04-23)
**Applies to:** All Second Chair legal-vertical clients.
**Vocabulary:** Our unit is the **Market** (capital M). When this doc references "DMA" it always means Nielsen's product, never ours.

---

## Why this exists

The legal advertising vertical has a hard constraint that most commercial geo-targeting systems don't respect: **every campaign must live within a single state.** State bar rules (led by Florida Rule 4-7) govern advertising based on where the audience receives the ad, not where the firm is located, and penalties for out-of-state leakage are real.

Nielsen DMAs are the standard unit in TV/CTV/digital media buying. But ~half of the 210 Nielsen DMAs cross state lines — NYC DMA = NY/NJ/CT, DC DMA = DC/MD/VA/WV, Memphis DMA = TN/MS/AR, LA DMA is mostly CA but skims into NV. Buying a Nielsen DMA wholesale means buying multi-state exposure that legal clients cannot use.

We audited the alternatives:

| Scheme | # of areas | State-pure? | Verdict |
|---|---|---|---|
| Counties (3,143) | Too granular | ✅ | Building block only |
| ZIPs (~33,000) | Too granular | ✅ ~99% | Building block only |
| Census MSAs (393) | Right-size | ❌ Many cross states | Same problem as Nielsen DMAs |
| Census CBSAs (935) | Too granular | ❌ | — |
| Census CSAs (181) | Right-size | ❌ **Worst** — designed for 3–5 state spans | — |
| BEA Economic Areas (179) | Right-size | ❌ Multi-state by design | — |
| Nielsen DMAs (210) | Right-size | ❌ ~50% cross states | Starting skeleton |

Every off-the-shelf metro scheme intentionally crosses state lines because they're built around economic/commuting linkage, not political/legal boundaries. **We must build our own.**

## The Framework

Our unit of geography is the **Market**. Each Market:
- Contains exactly one state's territory (state-pure)
- Has at least 1,000,000 people (with documented tiny-state exceptions)
- Is composed of one or more whole counties
- Has a unique ID like `CA-01`, `NY-03`, `FL-02`

Markets replace Nielsen DMAs as Second Chair's commercial unit (pricing, exclusivity, contracts) and execution unit (zip lists for ad platforms). National total: **109 Markets** vs. Nielsen's 210 DMAs.

## The Six Construction Rules

### Rule 1 — Start from Nielsen DMA composition

Nielsen's county-level DMA composition is public (via TVB, Wikipedia, `github.com/simzou/nielsen-dma`). We use it as the structural skeleton because every media buyer already understands it and because Nielsen's county boundaries reflect real viewing/media consumption patterns. The Markets we derive from this skeleton are *ours*, not Nielsen's.

### Rule 2 — State-purify cross-state Nielsen DMAs

Any Nielsen DMA that spans multiple states is split at state borders. Each state-portion becomes its own candidate Market.

Example: Yuma-El Centro Nielsen DMA → `AZ-Yuma-portion` candidate + `CA-Imperial-portion` candidate.

### Rule 3 — Merge sub-1M candidates into adjacent same-state candidates

Any candidate Market with fewer than 1,000,000 people is merged into the nearest same-state candidate. "Nearest" is determined by geographic adjacency and cultural/economic affinity.

Example (CA): Palm Springs Nielsen DMA alone ≈ 600K → merges into Greater LA Market (which is contiguous and shares Riverside County).

When multiple sub-1M candidates are adjacent only to each other, merge them all together and reassess (Chico-Redding + Eureka + Reno-CA-slice + Medford-CA-slice collectively become "Far North," which then merges into Sacramento Market).

### Rule 4 — Mega Markets stay whole

Any source Nielsen DMA with 5M+ population (LA, NYC, Chicago, Dallas-Ft. Worth, Houston, SF Bay Area, Atlanta, Philadelphia, DC, Boston, Phoenix) becomes a single Market and is **not sub-split** in V1. "Bigger is better for targeting" — agency principle confirmed 2026-04-23.

If a specific client use case later requires sub-LA or sub-NYC Markets, we can add a tier below `XX-NN` (e.g., `CA-01a`, `CA-01b`) without breaking the framework.

### Rule 5 — Border-county handling

Approximately 12 of the 3,143 US counties are split between Nielsen DMAs (Riverside CA, San Bernardino CA, Westchester NY, parts of Memphis-area counties, etc.). Our convention:

- **Default to whole-county assignment** to the dominant Nielsen DMA (the one with the majority of the county's population/area). The whole county then flows to whichever Market that Nielsen DMA collapses into under Rules 3–4.
- **Where the split is culturally dramatic** (Riverside: Inland Empire vs. Coachella Valley), document the judgment call but still use whole-county assignment — because after Rule 3 merges, both sides usually end up in the same Market anyway.
- **We do not split counties at the ZIP level** except where a specific campaign requires it (a client opt-in workflow, handled per-engagement).

### Rule 6 — Tiny states (<1M total population)

States whose entire population is under 1M (WY, VT, AK, ND, SD, DE, and DC as a jurisdiction) each become one whole-state Market as a documented exception to Rule 3. SC may choose to not actively sell these markets, but the Markets exist so campaigns remain coverable.

## Naming convention

- Market ID: `{STATE}-{NN}` where NN is a two-digit sequence number, ordered by population descending within the state (CA-01 = Greater LA, CA-02 = Bay Area, …).
- Market name: short, human-readable, descriptive of the combined region (`Greater LA + Coachella`, `Central Valley`, `Sacramento + Far North`).
- Sub-Markets (future, if added): `{STATE}-{NN}{letter}` (e.g., `CA-01a`, `CA-01b`).

## What this replaces

This framework **replaces** Second Chair's prior use of Nielsen DMAs as the commercial unit. Affected artifacts (re-paper required):

- `08_Brands/Second_Chair/04_Audience/Market_Ranked_List.md` — migrate 121 Nielsen DMA tier ranking → 109 Market tier ranking (file rename: `Market_Ranked_List.md`)
- `08_Brands/Second_Chair/07_Research/02_Sales_Intelligence/Market_Analysis/Market_Baseline_Pricing_Framework.md` — recalibrate MOI formula for Market boundaries (file rename: `Market_Baseline_Pricing_Framework.md`)
- `08_Brands/Second_Chair/07_Research/02_Sales_Intelligence/Market_Analysis/Geo_Exclusivity/Geo_Exclusivity_Territory_Model.md` — "DMA" → "Market" language; "Territory" stays as the exclusivity wrapper concept
- **Jacoby contract** (formerly "all 7 CA DMAs @ 15%") → "all 6 CA Markets @ 15%" — same coverage, new naming (deferred per Davis 2026-04-23)
- **Tofer pitch** (formerly "LA + Bakersfield + Fresno DMAs") → "Greater LA Core + Central Valley" (CA-01 + CA-06; renumbered in v1.1 from CA-01 + CA-05)

## Source data

Build dependencies, all public and free:

- **Nielsen DMA-County map:** `github.com/simzou/nielsen-dma` + Wikipedia DMA pages as cross-check
- **ZIP–County relationship:** Census 2020 ZCTA-to-County relationship file (`www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/`)
- **County populations:** Census ACS 2023 5-year estimates (`data.census.gov`)
- **Nielsen DMA TV household counts (for MOI recalibration):** `ustvdb.com`

All snapshots saved dated under `Source_Data/`.

## Data structure — the Market file

Each state gets a `XX_Markets.csv` with one row per ZIP:

| column | description |
|---|---|
| `zip` | 5-digit ZIP (ZCTA) |
| `county` | County name |
| `county_fips` | 5-digit county FIPS code |
| `market_id` | e.g., `CA-01` |
| `market_name` | e.g., `Greater LA + Coachella` |
| `state` | 2-letter state code |
| `nielsen_dma_origin` | The Nielsen DMA this ZIP originally mapped to, for reference |
| `population_estimate` | 2023 ACS county population (attributed to county, not pro-rated by ZIP) |

Plus per-Market `.txt` files under `per_market_zips/` with just the ZIPs, one per line — for direct paste into Meta, Google Ads, TTD.

## Verification checklist

Before shipping any state's build:
1. **Coverage** — All counties in the state assigned to exactly one Market. Sum of Market populations ≈ state total.
2. **State-purity** — Every ZIP in every Market has the correct state prefix. No leakage.
3. **Min-floor** — Every Market ≥ 1M (or flagged tiny-state exception).
4. **Spot-check ZIP counts** — Plausible distribution (mega-Markets 400–700 ZIPs, small 100–200).
5. **Platform sanity** — Upload to one sandbox campaign, check reach estimate.
6. **Known client cross-reference** — Confirm existing client footprints map cleanly.

## Change log

| date | version | change |
|---|---|---|
| 2026-04-23 | 1.0 | Initial methodology. CA = 6 Markets (then called "Buckets"). National framework rules locked. |
| 2026-04-23 | 1.1 | Terminology lock: unit is **Market** (Abracadabra agency consult). "Bucket" usage removed. File names migrated: `National_Bucket_Definitions.md` → `National_Market_Definitions.md`, `CA_Buckets.csv` → `CA_Markets.csv`, etc. CSV columns: `bucket_id` → `market_id`, `bucket_name` → `market_name`, `dma_origin` → `nielsen_dma_origin`. |
| 2026-04-23 | 1.1 | CA framework expanded from 6→7 Markets: split former CA-01 Greater LA + Coachella into **CA-01 Greater LA Core** (LA, Orange, Ventura, Inyo — 13.7M, $425 anchor-preserved) and **CA-04 Inland Empire + Coachella** (San Bernardino, Riverside whole — 4.7M, $340). Renumbered CA-03 through CA-07 by population descending. National total: 109→110. Rationale: split unlocks parallel exclusivity sales (two whales possible in LA-area instead of one), and reflects how PI firms actually segment LA-area opportunity (coastal vs. IE compete in different sub-markets). |
