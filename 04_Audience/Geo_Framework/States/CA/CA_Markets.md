# California Markets — Reference & Upload Guide

**State:** California
**Markets:** 7
**Total ZIPs:** 1,802
**Coverage:** All 58 California counties, all state-pure
**Built:** 2026-04-23 (v1.1 — split former CA-01 into CA-01 LA Core + CA-04 IE+Coachella, renumbered by population)
**Source:** Census 2020 ZCTA-County relationship file + Nielsen DMA composition

See `../../Methodology.md` for the construction rules.

---

## The 7 California Markets

| Market | Name | Pop (2023) | Counties | ZIPs | Underlying Nielsen DMAs |
|---|---|---:|---:|---:|---|
| **CA-01** | Greater LA Core | 13.74M | 4 | 421 | Los Angeles DMA (coastal/urban core) |
| **CA-02** | Bay Area | 7.71M | 11 | 340 | San Francisco-Oakland-San Jose |
| **CA-03** | Sacramento + Far North | 5.01M | 27 | 460 | Sacramento + Chico-Redding + Eureka + Reno (CA portion) |
| **CA-04** | Inland Empire + Coachella | 4.69M | 2 | 162 | Los Angeles DMA (Inland Empire) + Palm Springs |
| **CA-05** | San Diego + Imperial | 3.47M | 2 | 130 | San Diego + Yuma-El Centro (CA portion) |
| **CA-06** | Central Valley | 3.03M | 7 | 190 | Fresno-Visalia + Bakersfield |
| **CA-07** | Central Coast | 1.49M | 5 | 99 | Monterey-Salinas + Santa Barbara-Santa Maria-SLO |
| **Total** | | **39.14M** | **58** | **1,802** | |

---

## Market-by-Market Detail

### CA-01 — Greater LA Core (13.74M)
**Counties:** Los Angeles, Orange, Ventura, Inyo
**Notable markets:** Los Angeles, Long Beach, Anaheim, Santa Ana, Oxnard, Beverly Hills, Hollywood, Long Beach, Irvine
**File:** `per_market_zips/CA-01_GreaterLA_Core.txt`
**Note:** The coastal/urban core LA Market. Split out from former Greater LA + Coachella in v1.1 — Inland Empire and Coachella moved to CA-04. Anchor-priced at $425 (preserves Tofer pitch deck legacy LA pricing).

### CA-02 — Bay Area (7.71M)
**Counties:** San Francisco, Alameda, Contra Costa, San Mateo, Santa Clara, Marin, Sonoma, Napa, Solano, Lake, Mendocino
**Notable markets:** San Francisco, San Jose, Oakland, Fremont, Santa Rosa, Vallejo, Concord, Berkeley
**File:** `per_market_zips/CA-02_BayArea.txt`

### CA-03 — Sacramento + Far North (5.01M)
**Counties (27):** Sacramento, San Joaquin, Stanislaus, Yolo, Placer, El Dorado, Sutter, Yuba, Amador, Calaveras, Tuolumne, Alpine, Nevada, Sierra, Plumas, Colusa, Glenn, Butte, Shasta, Tehama, Trinity, Siskiyou, Modoc, Humboldt, Del Norte, Lassen, Mono
**Notable markets:** Sacramento, Stockton, Modesto, Roseville, Chico, Redding, Eureka
**File:** `per_market_zips/CA-03_Sacramento_FarNorth.txt`
**Note:** Largest county count by far — collapses 5 sub-1M Nielsen DMAs (Sac, Chico-Redding, Eureka, Reno-CA-slice, Medford-CA-slice) into one Market per Rule 3 merge. *Was CA-04 in v1.0; renumbered by population in v1.1.*

### CA-04 — Inland Empire + Coachella (4.69M) ⭐ NEW in v1.1
**Counties:** San Bernardino, Riverside (whole county, includes Coachella Valley)
**Notable markets:** Riverside, San Bernardino, Ontario, Rancho Cucamonga, Fontana, Moreno Valley, Corona, Palm Springs, Coachella, Indio, Palm Desert, La Quinta
**File:** `per_market_zips/CA-04_InlandEmpire_Coachella.txt`
**Note:** Split out from former Greater LA + Coachella in v1.1. Reflects how PI firms actually segment LA-area opportunity: LA-coastal firms vs IE firms operate as different competitor sets. **Sells as separate exclusivity from CA-01** — two whales possible in the LA-area geography instead of one.

### CA-05 — San Diego + Imperial (3.47M)
**Counties:** San Diego, Imperial
**Notable markets:** San Diego, Chula Vista, Oceanside, Escondido, El Centro, Calexico
**File:** `per_market_zips/CA-05_SanDiego_Imperial.txt`
**Note:** *Was CA-03 in v1.0; renumbered by population in v1.1.*

### CA-06 — Central Valley (3.03M)
**Counties:** Fresno, Tulare, Kings, Madera, Mariposa, Merced, Kern
**Notable markets:** Fresno, Bakersfield, Visalia, Hanford, Madera, Merced
**File:** `per_market_zips/CA-06_CentralValley.txt`
**Note:** Tofer's Central Valley target. *Was CA-05 in v1.0; renumbered to CA-06 in v1.1.* Tofer locked at $265/lead through current renewal window per signed Service Agreement.

### CA-07 — Central Coast (1.49M)
**Counties:** Monterey, San Benito, Santa Cruz, Santa Barbara, San Luis Obispo
**Notable markets:** Salinas, Santa Cruz, Santa Maria, Santa Barbara, San Luis Obispo, Hollister
**File:** `per_market_zips/CA-07_CentralCoast.txt`
**Note:** Smallest Market. Just clears the 1M floor (1.49M). *Was CA-06 in v1.0; renumbered to CA-07 in v1.1.*

---

## How to upload to ad platforms

### Meta (Facebook / Instagram)
1. Ads Manager → Audiences → Create Audience → Saved Audience
2. Location → "Add locations in bulk" → paste contents of the Market's `.txt` file (or upload the `.txt` directly)
3. Name it: `WCTL_CA-01_GreaterLA` (or client-specific naming)
4. Save. Reuse on every campaign for that client + Market.

**Note:** Meta caps at 2,500 ZIPs per location set. Largest CA Market (CA-03 Sacramento + Far North) is 460 — well under cap.

### Google Ads / YouTube
1. Campaign → Settings → Locations → Enter another location
2. "Advanced search" → Bulk locations → paste contents of the Market's `.txt` file
3. Save as Location Group with the Market name for re-use.

### The Trade Desk (Kokai)
1. Use the "Geography Lists" feature
2. Upload the `.txt` as a ZIP-list geography
3. Create one campaign shell per Market per client (TTD's recommended workflow for Market-bucketed buys)

### Other DSPs (DV360, Amazon DSP, StackAdapt, Basis, etc.)
All accept ZIP lists via paste or CSV upload. Same pattern.

---

## Tofer-specific mapping

**Tofer's confirmed footprint (per Call 2, 2026-04-20):** Greater LA + Central Valley combined
- Buy `CA-01` (Greater LA Core) + `CA-06` (Central Valley)
- Total: 16.77M people, 11 counties, 611 ZIPs
- *In v1.0 this was CA-01 + CA-05; renumbered in v1.1.*

**If Tofer wants Inland Empire too** (mentioned in call notes), that's now its own Market — `CA-04` Inland Empire + Coachella. Tofer would buy `CA-01` + `CA-04` + `CA-06` (3 line items: Greater LA Core $425 + IE+Coachella $340 + Central Valley $265-$275). Total ~21.46M people.

---

## Verification (results from build, 2026-04-23 v1.1)

- ✅ **Coverage:** All 58 CA counties present in exactly one Market. No double-counting.
- ✅ **State-purity:** All 1,802 ZIPs in 90000-96199 range. No leakage to AZ (85xxx), NV (89xxx), OR (97xxx).
- ✅ **Min-floor:** Every Market ≥ 1M. Smallest is CA-07 at 1.49M.
- ✅ **Population sum:** 39.14M (matches CA total).
- ✅ **Tofer cross-reference:** LA Core + Central Valley target maps cleanly to CA-01 + CA-06 with no leakage. IE optional add as CA-04.
- ⏳ **Platform sanity test:** Pending — needs sandbox upload to Meta/Google to confirm reach estimates are plausible. Recommend doing this with the first real campaign launch.

---

## Files

```
States/CA/
├── CA_Markets.csv                                 # Master file (zip, county, market_id, market_name, nielsen_dma_origin, pop)
├── CA_Markets.md                                  # This file
└── per_market_zips/
    ├── CA-01_GreaterLA_Core.txt                  # 421 zips
    ├── CA-02_BayArea.txt                         # 340 zips
    ├── CA-03_Sacramento_FarNorth.txt             # 460 zips
    ├── CA-04_InlandEmpire_Coachella.txt          # 162 zips  ⭐ NEW
    ├── CA-05_SanDiego_Imperial.txt               # 130 zips
    ├── CA-06_CentralValley.txt                   # 190 zips
    └── CA-07_CentralCoast.txt                    #  99 zips
```

## Rebuild

If source data updates (Census refresh, Nielsen DMA boundary changes), rerun:
```
cd Source_Data/
python3 build_ca_markets.py
```
This regenerates `CA_Markets.csv` and all per-Market TXT files in place.

## Changelog

| Date | Version | Change |
|---|---|---|
| 2026-04-23 | 1.0 | Initial CA build. 6 Markets. CA-01 = Greater LA + Coachella (single 18.4M Market). |
| 2026-04-23 | 1.1 | Split CA-01 into CA-01 Greater LA Core (13.7M) + CA-04 Inland Empire + Coachella (4.7M). Renumbered CA-03 through CA-07 by population descending. CA-06 = Central Valley (was CA-05, Tofer's market). |
