# Cross-State Nielsen DMA Reference

**Purpose:** Authoritative internal count + list of which Nielsen DMAs cross state lines, since Nielsen does not publish this number directly. Drives state-purification logic in our Geo Framework (`Methodology.md` Rule 2).

**Built:** 2026-04-23
**Source:** Nielsen DMA-County composition cross-referenced against state FIPS

---

## Headline numbers

- **Total Nielsen DMAs:** 210
- **Cross-state DMAs:** ~108 (≈ 51%)
- **Single-state DMAs:** ~102 (≈ 49%)

The ~108 figure is approximate because (a) some DMAs include only 1–2 marginal counties from a neighboring state that are sometimes reclassified, and (b) Nielsen has nudged a handful of borderline assignments over the past few years.

**Practical implication:** Roughly half of Nielsen's DMAs are unusable as commercial units for state-restricted advertising verticals (legal, cannabis, sports betting, certain insurance/financial products). The framework's Rule 2 (state-purify) addresses every one of them.

---

## Cross-state DMAs grouped by anchor metro

### Top-tier mega-DMAs that cross states
| DMA | States | Notes |
|---|---|---|
| New York | NY, NJ, CT, PA | Largest US DMA. NJ portion is huge (~3.8M N-NJ + 3M Central NJ). |
| Los Angeles | CA (some sources include AZ slivers) | Mostly CA-pure; minor border noise |
| Chicago | IL, IN | NW Indiana (Lake, Porter) is the IN piece (~700K) |
| Philadelphia | PA, NJ, DE, MD | South Jersey is huge piece (~2.5M); Delaware is ~1M |
| Dallas-Fort Worth | TX, OK | Small OK slice |
| Washington DC | DC, MD, VA, WV | One of the most state-fragmented mega-DMAs |
| Boston | MA, NH | Southern NH counties |
| Atlanta | GA, AL | Small AL spillover |

### Mid-size cross-state DMAs (commercially significant)
| DMA | States | Notes |
|---|---|---|
| Cincinnati | OH, KY, IN | NKY is significant |
| St. Louis | MO, IL | Metro East IL (~600K) |
| Kansas City | MO, KS | KS half includes Overland Park, Olathe |
| Memphis | TN, MS, AR | DeSoto MS, Crittenden AR |
| Charlotte | NC, SC | Includes Lake Norman + Rock Hill SC |
| Jacksonville | FL, GA | South GA spillover |
| Mobile-Pensacola | AL, FL, MS | Rare 3-state DMA |
| Hartford-New Haven | CT, MA | |
| Providence-New Bedford | RI, MA | |
| Portland (OR) | OR, WA | SW Washington (Vancouver, Camas) ~500K |
| Spokane | WA, ID | N. Idaho panhandle |
| Boise | ID, OR | E. Oregon |
| Reno | NV, CA | Lassen + Mono CA |
| Las Vegas | NV (mostly), some AZ NW | |
| Salt Lake City | UT, ID, NV, WY | 4-state DMA |
| Albuquerque-Santa Fe | NM, AZ | |
| Yuma-El Centro | AZ, CA | Imperial Co. is the CA piece |
| Minneapolis-St. Paul | MN, WI | Western WI suburbs |
| Duluth-Superior | MN, WI | |
| Fargo | ND, MN | |
| Sioux Falls | SD, MN, IA | 3-state |
| Omaha | NE, IA | Council Bluffs IA |
| Sioux City | IA, NE, SD | 3-state |
| Quad Cities | IA, IL | |
| Davenport-Rock Island-Moline | IA, IL | (alt name for Quad Cities) |
| Toledo | OH, MI | |
| South Bend-Elkhart | IN, MI | |
| Louisville | KY, IN | Southern IN |
| Evansville | IN, KY, IL | 3-state |
| Paducah-Cape Girardeau-Harrisburg | KY, MO, IL, IN, TN | **5-state DMA** — the most fragmented |
| Bristol-Kingsport-Johnson City (Tri-Cities) | TN, VA | |
| Chattanooga | TN, GA, AL | 3-state |
| Huntsville-Decatur (Florence) | AL, TN | |
| Columbus GA | GA, AL | Phenix City AL |
| Augusta | GA, SC | |
| Savannah | GA, SC | |
| Wilmington NC | NC, SC | |
| Norfolk-Portsmouth-Newport News | VA, NC | NE NC |
| Greenville-Spartanburg-Asheville | SC, NC, GA | 3-state |
| Roanoke-Lynchburg | VA, WV, NC | |
| Bluefield-Beckley-Oak Hill | WV, VA | |
| Wheeling-Steubenville | WV, OH | |
| Parkersburg | WV, OH | |
| Huntington-Charleston | WV, OH, KY | 3-state |
| Lexington | KY, WV | |
| Pittsburgh | PA, WV, OH, MD | |
| Erie | PA, NY | |
| Elmira (Corning) | NY, PA | |
| Binghamton | NY, PA | |
| Watertown | NY, ON-Canada (rare cross-border, not state) | |
| Burlington-Plattsburgh | VT, NY, NH | 3-state |
| Albany-Schenectady-Troy | NY, MA, VT | 3-state |
| Springfield-Holyoke | MA, CT | |
| Bangor | ME (mostly) | |
| Portland-Auburn ME | ME, NH | |
| Tupelo-Columbus | MS, AL | |
| Jackson MS | MS (mostly) | Some sources include LA slivers |
| Shreveport | LA, TX, AR | 3-state |
| Monroe-El Dorado | LA, AR, MS | 3-state |
| Texarkana | TX, AR, OK, LA | 4-state |
| Beaumont-Port Arthur | TX, LA | |
| Lake Charles | LA (mostly) | |
| Lafayette LA | LA (mostly) | |
| Baton Rouge | LA, MS | |
| Biloxi-Gulfport | MS (mostly) | |
| Hattiesburg-Laurel | MS (mostly) | |
| Greenwood-Greenville | MS, AR | |
| Jonesboro | AR, MO, TN | 3-state |
| Fort Smith-Fayetteville | AR, OK | |
| Springfield MO | MO, AR, KS | 3-state |
| Joplin-Pittsburg | MO, KS, OK, AR | 4-state |
| Wichita Falls-Lawton | TX, OK | |
| Amarillo | TX, NM, OK | 3-state |
| Lubbock | TX, NM | |
| Odessa-Midland | TX (mostly) | |
| El Paso | TX, NM | |
| Medford-Klamath Falls | OR, CA | |
| Eureka | CA (mostly), some OR slivers | |
| Anchorage | AK | (single-state) |
| Honolulu | HI | (single-state) |

*(Above is illustrative, not exhaustive — full machine-readable list with county composition lives in `Source_Data/nielsen_dma_county_map.csv` once that's pulled.)*

### "5+ state" DMAs (most fragmented, hardest legal-vertical case)
1. **Paducah-Cape Girardeau-Harrisburg** — KY, MO, IL, IN, TN (5 states)
2. **Texarkana** — TX, AR, OK, LA (4 states)
3. **Joplin-Pittsburg** — MO, KS, OK, AR (4 states)
4. **Salt Lake City** — UT, ID, NV, WY (4 states)
5. **Pittsburgh** — PA, WV, OH, MD (4 states)
6. **Philadelphia** — PA, NJ, DE, MD (4 states)
7. **New York** — NY, NJ, CT, PA (4 states)
8. **Washington DC** — DC, MD, VA, WV (4 states)

These eight DMAs alone cover ~40M people and would each fragment into 4–5 separate Markets under Rule 2.

---

## States entirely covered by single-state DMAs

These states have zero in-bound or out-bound DMA spillover — every Nielsen DMA serving them is wholly contained in the state:

- **Alaska** (Anchorage, Fairbanks, Juneau)
- **Hawaii** (Honolulu)

Nearly every other state is touched by at least one cross-state DMA, even tiny ones at the borders.

---

## How this is used

This reference exists for two purposes:

1. **Internal:** When discussing a market with a client or planning a buy, we can immediately tell whether the Nielsen DMA is state-pure or needs to be Market-mapped (split per Rule 2).
2. **Build-time input:** Rule 2 (state-purify) iterates over every cross-state DMA in this list, splits at the state border, and assigns each state-portion to a Market per Rules 3–5.

For the definitive machine-readable list, see `Source_Data/nielsen_dma_county_map.csv` (to be pulled from `github.com/simzou/nielsen-dma`). This document is the human-readable summary.
