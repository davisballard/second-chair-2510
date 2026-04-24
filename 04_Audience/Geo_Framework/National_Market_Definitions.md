# National Market Definitions

**Status:** v1.0 (2026-04-23)
**Coverage:** All 50 states + DC
**Total Markets:** ~110 (national)
**Methodology:** see `Methodology.md`

This document applies the 6 construction rules to every state. County-level only — full ZIP-level builds happen on-demand per state (see `States/{XX}/`).

---

## Headline numbers

| Tier | State pop | # of states | Market count |
|---|---|---|---|
| Mega (>20M) | CA, TX, FL | 3 | 20 |
| Large (10-20M) | NY, PA, IL, OH, GA, NC | 6 | 21 |
| Medium (5-10M) | MI, NJ, VA, WA, AZ, TN, MA, IN, MO, MD, WI, CO, MN | 13 | 26 |
| Small-Med (2-5M) | SC, AL, LA, KY, OR, OK, CT, UT, IA, NV, AR, MS, KS, NM | 14 | 24 |
| Small (1-2M) | NE, ID, WV, HI, NH, ME, MT, RI | 8 | 12 |
| Tiny (<1M, exception) | DE, SD, ND, AK, DC, VT, WY | 7 | 7 |
| **Total** | | **51** | **110** |

110 Markets vs. Nielsen's 210 — bigger pieces, all state-pure. (v1.1: split CA-01 Greater LA into CA-01 LA Core + CA-04 Inland Empire + Coachella, bringing CA from 6→7 Markets and national total from 109→110.)

---

## Mega States (>20M)

### CA — California (39.1M, 7 Markets) ✅ BUILT (v1.1)
See `States/CA/CA_Markets.md`. CA-01 Greater LA Core (13.7M, $425) + CA-02 Bay Area (7.7M, $375) + CA-03 Sacramento + Far North (5.0M, $305) + CA-04 Inland Empire + Coachella (4.7M, $340) + CA-05 San Diego + Imperial (3.5M, $335) + CA-06 Central Valley (3.0M, $275, Tofer locked $265) + CA-07 Central Coast (1.5M, $285).

### TX — Texas (30.5M, 7 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs | Key counties |
|---|---|---:|---|---|
| TX-01 | Dallas-Fort Worth Metroplex | 8.1M | Dallas-Ft. Worth (TX portion) | Dallas, Tarrant, Collin, Denton, Ellis, Kaufman, Rockwall, Johnson, Parker, Wise, Hunt |
| TX-02 | Greater Houston | 7.5M | Houston | Harris, Fort Bend, Montgomery, Brazoria, Galveston, Liberty, Waller, Chambers, Austin |
| TX-03 | Austin + Hill Country | 2.5M | Austin | Travis, Williamson, Hays, Bastrop, Caldwell, Burnet, Blanco |
| TX-04 | San Antonio + South-Central | 2.6M | San Antonio | Bexar, Comal, Guadalupe, Wilson, Kendall, Atascosa, Medina, Bandera |
| TX-05 | Rio Grande Valley + Laredo + Corpus | 2.5M | Harlingen-Weslaco-Brownsville-McAllen + Laredo + Corpus Christi | Hidalgo, Cameron, Starr, Willacy, Webb, Nueces, San Patricio, Kleberg, Refugio |
| TX-06 | El Paso + West Texas | 1.3M | El Paso (TX portion) + Odessa-Midland + San Angelo + Abilene-Sweetwater (combined per Rule 3) | El Paso, Hudspeth, Midland, Ector, Tom Green, Taylor |
| TX-07 | East TX + Panhandle (rest of state) | 6.0M | Tyler-Longview + Waco-Temple-Bryan + Beaumont-Port Arthur (TX portion) + Amarillo (TX portion) + Lubbock + Wichita Falls (TX portion) + Sherman-Ada (TX portion) | Smith, McLennan, Bell, Brazos, Jefferson, Orange, Potter, Randall, Lubbock, Wichita |

**Cross-state Markets split:** Sherman-Ada, Wichita Falls-Lawton, Texarkana, Beaumont-Port Arthur, Shreveport, El Paso, Amarillo. TX portions assigned per Rule 2.

### FL — Florida (22.6M, 6 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs | Notes |
|---|---|---:|---|---|
| FL-01 | South Florida | 6.2M | Miami-Ft. Lauderdale | Miami-Dade, Broward, Palm Beach, Monroe |
| FL-02 | Tampa Bay | 5.0M | Tampa-St. Petersburg-Sarasota | Hillsborough, Pinellas, Pasco, Manatee, Sarasota, Polk, Hernando, Citrus |
| FL-03 | Central FL / Orlando | 4.4M | Orlando-Daytona Beach-Melbourne | Orange, Seminole, Osceola, Lake, Volusia, Brevard, Marion, Sumter, Flagler |
| FL-04 | North FL / Jacksonville | 2.0M | Jacksonville (FL portion) | Duval, St. Johns, Clay, Nassau, Putnam, Baker |
| FL-05 | Panhandle | 2.2M | Pensacola-Mobile (FL portion) + Panama City + Tallahassee (FL portion) | Escambia, Santa Rosa, Okaloosa, Walton, Bay, Leon, Gadsden, Wakulla |
| FL-06 | SW Florida + Treasure Coast | 2.8M | Ft. Myers-Naples + W. Palm Beach (sliver) + Gainesville | Lee, Collier, Charlotte, Sarasota (overflow), Indian River, St. Lucie, Martin, Alachua |

**Note:** Mobile-Pensacola and Tallahassee-Thomasville are cross-state (AL/MS/GA) — FL portions only assigned here.

---

## Large States (10-20M)

### NY — New York (19.5M, 4 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| NY-01 | NYC Metro (NY-only) | 12.0M | NYC DMA (NY counties only — NJ/CT split off to those states) |
| NY-02 | Capital Region + North Country | 1.8M | Albany-Schenectady-Troy (NY portion) + Burlington-Plattsburgh (NY portion) + Watertown |
| NY-03 | Western NY | 2.5M | Buffalo + Rochester + Erie (PA-portion split off) |
| NY-04 | Central + Southern Tier | 1.5M | Syracuse + Binghamton (NY portion) + Elmira (NY portion) + Utica |

**Note:** NYC's NJ portion (~7M) lives in NJ-01; CT portion (~1M) lives in CT-01.

### PA — Pennsylvania (13.0M, 4 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| PA-01 | Greater Philadelphia (PA portion) | 4.0M | Philadelphia (PA counties only) |
| PA-02 | Pittsburgh + Western PA | 2.4M | Pittsburgh (PA portion) + Johnstown-Altoona |
| PA-03 | Central PA | 2.6M | Harrisburg-Lancaster-Lebanon-York + Wilkes-Barre-Scranton |
| PA-04 | Northern + Northwest PA | 1.6M | Erie + Elmira (PA portion) + Binghamton (PA portion) |

### IL — Illinois (12.5M, 3 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| IL-01 | Chicago Metro | 8.5M | Chicago (IL counties only) |
| IL-02 | Central IL | 2.0M | Peoria-Bloomington + Champaign-Springfield-Decatur |
| IL-03 | Downstate + Quad Cities (IL) + Metro East | 2.0M | St. Louis (IL portion) + Quad Cities (IL portion) + Paducah (IL portion) + Rockford |

### OH — Ohio (11.8M, 4 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| OH-01 | Cleveland + NE Ohio | 3.6M | Cleveland-Akron + Youngstown |
| OH-02 | Columbus + Central | 2.7M | Columbus + Zanesville |
| OH-03 | Cincinnati + Dayton (OH portion) | 3.3M | Cincinnati (OH portion) + Dayton |
| OH-04 | Toledo + Lima + Wheeling-Steubenville (OH portion) | 2.2M | Toledo (OH portion) + Lima + Wheeling (OH portion) + Parkersburg (OH portion) |

### GA — Georgia (11.0M, 3 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| GA-01 | Atlanta Metro | 6.5M | Atlanta DMA (GA portion) |
| GA-02 | Savannah + Coastal | 1.5M | Savannah (GA portion) + Macon (eastern) + Brunswick area |
| GA-03 | Augusta + Columbus + Albany + Macon-W | 3.0M | Augusta (GA portion) + Columbus GA (GA portion) + Albany + Macon (W) + Tallahassee (GA portion) |

### NC — North Carolina (10.7M, 4 Markets)

| Market | Name | Pop (~) | Underlying Nielsen DMAs |
|---|---|---:|---|
| NC-01 | Charlotte Metro (NC portion) | 2.6M | Charlotte (NC counties only) |
| NC-02 | Triangle (Raleigh-Durham) | 2.4M | Raleigh-Durham-Fayetteville |
| NC-03 | Triad + Western NC | 2.7M | Greensboro-High Point-Winston Salem + Greenville-Spartanburg-Asheville (NC portion) |
| NC-04 | Eastern NC + Coast | 3.0M | Greenville-New Bern-Washington + Wilmington (NC portion) + Norfolk (NC portion) |

---

## Medium States (5-10M) — 13 states, 26 Markets total

### MI — Michigan (10.0M, 3 Markets)
- **MI-01 Detroit Metro** (4.3M): Detroit DMA (MI portion only — Toledo/South Bend slivers split off)
- **MI-02 West Michigan** (3.0M): Grand Rapids-Kalamazoo-Battle Creek + Lansing
- **MI-03 Northern + UP** (2.7M): Flint-Saginaw-Bay City + Traverse City-Cadillac + Marquette + Alpena

### NJ — New Jersey (9.3M, 2 Markets)
- **NJ-01 North NJ + NYC-NJ portion** (6.8M): NYC DMA (NJ counties: Bergen, Hudson, Essex, Morris, Passaic, Sussex, Union, Middlesex, Somerset, Hunterdon, Warren, Monmouth, Ocean)
- **NJ-02 South NJ + Philly-NJ portion** (2.5M): Philadelphia DMA (NJ counties: Camden, Burlington, Gloucester, Atlantic, Cape May, Cumberland, Salem, Mercer)

### VA — Virginia (8.7M, 3 Markets)
- **VA-01 Northern VA / DC-VA portion** (3.0M): DC DMA (VA counties: Fairfax, Loudoun, Prince William, Arlington, Stafford, Spotsylvania, Fauquier, Culpeper, Clarke, Warren, Frederick, Fredericksburg city, etc.)
- **VA-02 Hampton Roads + Richmond** (3.5M): Norfolk-Portsmouth-Newport News (VA portion) + Richmond-Petersburg
- **VA-03 SW VA + Roanoke + Charlottesville** (2.2M): Roanoke-Lynchburg (VA portion) + Tri-Cities (VA portion) + Bluefield-Beckley (VA portion) + Charlottesville + Harrisonburg

### WA — Washington (7.8M, 2 Markets)
- **WA-01 Greater Seattle + Western WA** (5.5M): Seattle-Tacoma + Portland-OR (WA portion = Vancouver/SW WA) + Yakima
- **WA-02 Eastern WA** (2.3M): Spokane (WA portion) + Tri-Cities WA + Wenatchee

### AZ — Arizona (7.4M, 2 Markets)
- **AZ-01 Phoenix + Northern AZ** (5.5M): Phoenix DMA + Flagstaff-Prescott + Yuma-El Centro (AZ portion)
- **AZ-02 Tucson + SE AZ** (1.9M): Tucson (Sierra Vista-Nogales)

### TN — Tennessee (7.1M, 3 Markets)
- **TN-01 Nashville Metro + Mid-TN** (2.7M): Nashville
- **TN-02 Memphis (TN portion) + W. TN** (1.5M): Memphis (TN portion) + Jackson TN
- **TN-03 Knoxville + Tri-Cities (TN portion) + Chattanooga (TN portion)** (2.9M): Knoxville + Tri-Cities + Chattanooga (TN portion)

### MA — Massachusetts (7.0M, 2 Markets)
- **MA-01 Greater Boston + East MA** (5.5M): Boston DMA (MA counties only — NH split off) + Providence (MA portion: Bristol)
- **MA-02 Western MA** (1.5M): Springfield-Holyoke (MA portion) + Albany (MA portion: Berkshire)

### IN — Indiana (6.8M, 3 Markets)
- **IN-01 Indianapolis Metro** (2.5M): Indianapolis
- **IN-02 NW Indiana + South Bend** (1.7M): Chicago (IN portion: Lake, Porter, LaPorte, Newton, Jasper) + South Bend-Elkhart (IN portion)
- **IN-03 Rest of IN** (2.6M): Fort Wayne + Evansville (IN portion) + Louisville (IN portion) + Lafayette IN + Terre Haute + Cincinnati (IN portion)

### MO — Missouri (6.2M, 2 Markets)
- **MO-01 St. Louis Metro (MO portion)** (2.5M): St. Louis (MO counties only)
- **MO-02 Kansas City (MO portion) + Springfield + Rest** (3.7M): Kansas City (MO portion) + Springfield MO + Columbia-Jefferson City + Joplin (MO portion) + Paducah (MO portion) + St. Joseph

### MD — Maryland (6.2M, 2 Markets)
- **MD-01 Baltimore + Maryland-DC suburbs** (5.5M): Baltimore + DC DMA (MD counties: Montgomery, Prince George's, Charles, etc.)
- **MD-02 Eastern Shore + Western MD** (700K, exception — under 1M but distinct region): Salisbury (MD portion) + Pittsburgh (MD portion: Garrett) + Hagerstown area
  - **Alternative:** merge into MD-01 (single MD Market of 6.2M). Recommend keeping split for cultural distinctness; revisit if ARPU disappoints.

### WI — Wisconsin (5.9M, 3 Markets)
- **WI-01 Milwaukee Metro + SE WI** (2.5M): Milwaukee + Madison (eastern overflow)
- **WI-02 Madison + South-Central WI** (1.5M): Madison + La Crosse-Eau Claire (eastern)
- **WI-03 Green Bay + Northern WI** (1.9M): Green Bay-Appleton + Wausau-Rhinelander + Duluth (WI portion: Superior)

### CO — Colorado (5.8M, 2 Markets)
- **CO-01 Denver Metro + Front Range** (4.5M): Denver
- **CO-02 Western Slope + Springs + South** (1.3M): Colorado Springs-Pueblo + Grand Junction-Montrose

### MN — Minnesota (5.7M, 2 Markets)
- **MN-01 Twin Cities Metro + Southern MN** (4.0M): Minneapolis-St. Paul (MN portion) + Rochester-Mason City (MN portion)
- **MN-02 Northern MN** (1.7M): Duluth-Superior (MN portion) + Mankato + Fargo (MN portion)

---

## Small-Medium States (2-5M) — 14 states, ~24 Markets

### SC — South Carolina (5.3M, 2 Markets)
- **SC-01 Charleston + Coast + Columbia** (3.0M): Charleston SC + Myrtle Beach-Florence + Columbia + Savannah (SC portion)
- **SC-02 Upstate SC + Charlotte (SC portion)** (2.3M): Greenville-Spartanburg-Asheville (SC portion) + Charlotte (SC portion: York, Lancaster, Chester, Cherokee) + Augusta (SC portion: Aiken, Edgefield)

### AL — Alabama (5.1M, 2 Markets)
- **AL-01 Birmingham + Central AL** (3.0M): Birmingham + Tuscaloosa + Anniston + Montgomery + Selma
- **AL-02 Mobile + Huntsville + Dothan + AL slivers** (2.1M): Mobile-Pensacola (AL portion) + Huntsville-Decatur + Dothan + Columbus GA (AL portion: Russell)

### LA — Louisiana (4.6M, 2 Markets)
- **LA-01 New Orleans + Baton Rouge** (2.3M): New Orleans + Baton Rouge (LA portion)
- **LA-02 Shreveport + Lafayette + Lake Charles + Monroe** (2.3M): Shreveport (LA portion) + Lafayette LA + Lake Charles + Monroe-El Dorado (LA portion) + Alexandria

### KY — Kentucky (4.5M, 2 Markets)
- **KY-01 Louisville (KY portion) + Lexington + Central KY** (2.7M): Louisville (KY portion) + Lexington (KY portion)
- **KY-02 Eastern + Western KY** (1.8M): Cincinnati (KY portion) + Huntington-Charleston (KY portion) + Bowling Green + Paducah (KY portion) + Evansville (KY portion)

### OR — Oregon (4.3M, 2 Markets)
- **OR-01 Portland Metro + Willamette Valley** (3.2M): Portland OR (OR portion only) + Eugene + Salem (incl. in Portland)
- **OR-02 Eastern + Southern OR** (1.1M): Medford-Klamath Falls (OR portion) + Bend + Boise (OR portion: Malheur)

### OK — Oklahoma (4.0M, 2 Markets)
- **OK-01 OKC Metro + Central** (2.4M): Oklahoma City + Tulsa (eastern overflow handled in OK-02)
- **OK-02 Tulsa + NE/SE OK** (1.6M): Tulsa + Joplin (OK portion) + Ft. Smith (OK portion) + Sherman-Ada (OK portion) + Wichita Falls (OK portion)

### CT — Connecticut (3.6M, 2 Markets)
- **CT-01 Hartford-New Haven + NYC-CT portion** (3.0M): Hartford-New Haven (CT portion) + NYC DMA (CT portion: Fairfield)
- **CT-02 Eastern CT** (~600K, **exception** — under 1M, kept for cultural distinctness): Providence-New Bedford (CT portion: New London)
  - **Alternative:** merge into CT-01 (single CT Market of 3.6M). **Recommend single Market** unless client demands; CT is small enough that one Market suffices.
  - **Final:** **1 Market** — `CT-01 All Connecticut` (3.6M)

### UT — Utah (3.4M, 1 Market)
- **UT-01 All Utah** (3.4M): Salt Lake City (UT counties only) + St. George (UT)

### IA — Iowa (3.2M, 2 Markets)
- **IA-01 Des Moines + Eastern IA** (2.0M): Des Moines-Ames + Cedar Rapids-Waterloo + Quad Cities (IA portion) + Davenport
- **IA-02 Western + Southern IA** (1.2M): Sioux City (IA portion) + Omaha (IA portion: Pottawattamie etc.) + Ottumwa-Kirksville

### NV — Nevada (3.2M, 2 Markets)
- **NV-01 Las Vegas Metro** (2.4M): Las Vegas
- **NV-02 Reno + Northern NV** (~800K, **exception** — kept distinct because LV vs Reno are entirely different markets): Reno (NV portion) + Salt Lake City (NV portion: Elko)
  - **Final:** **2 Markets**, NV-02 documented as sub-1M exception

### AR — Arkansas (3.0M, 2 Markets)
- **AR-01 Little Rock + Central + NW AR** (2.0M): Little Rock-Pine Bluff + Fayetteville-Springdale-Rogers (AR portion of Ft. Smith)
- **AR-02 Rest of AR** (1.0M): Memphis (AR portion) + Texarkana (AR portion) + Jonesboro (AR portion) + Monroe-El Dorado (AR portion)

### MS — Mississippi (2.9M, 2 Markets)
- **MS-01 Jackson + Central + N. MS** (1.8M): Jackson MS + Memphis (MS portion: DeSoto etc.) + Greenwood-Greenville (MS portion) + Columbus-Tupelo (MS portion)
- **MS-02 Gulf Coast + S. MS** (1.1M): Biloxi-Gulfport + Hattiesburg-Laurel + Mobile-Pensacola (MS portion: Jackson, George)

### KS — Kansas (2.9M, 2 Markets)
- **KS-01 Wichita + Topeka + Central** (1.7M): Wichita-Hutchinson + Topeka
- **KS-02 KC-KS portion + Western KS** (1.2M): Kansas City (KS portion: Johnson, Wyandotte, etc.) + Joplin (KS portion) + Sherman-Ada (KS sliver)

### NM — New Mexico (2.1M, 1 Market)
- **NM-01 All New Mexico** (2.1M): Albuquerque-Santa Fe (NM portion) + El Paso (NM portion) + Amarillo (NM portion: Quay) + Lubbock (NM portion: Lea)

---

## Small States (1-2M) — 8 states, 12 Markets

### NE — Nebraska (2.0M, 2 Markets)
- **NE-01 Omaha + Lincoln + East NE** (1.5M): Omaha (NE portion) + Lincoln-Hastings-Kearney
- **NE-02 Western NE** (~500K, **exception**): North Platte + Cheyenne-Scottsbluff (NE portion) + Sioux City (NE portion)
  - **Recommend:** merge to single Market NE-01 (2.0M)
  - **Final:** **1 Market**

### ID — Idaho (1.9M, 1 Market)
- **ID-01 All Idaho** (1.9M): Boise (ID portion) + Idaho Falls-Pocatello + Spokane (ID portion: panhandle) + Salt Lake City (ID portion)

### WV — West Virginia (1.8M, 1 Market)
- **WV-01 All West Virginia** (1.8M): Charleston-Huntington (WV portion) + Pittsburgh (WV portion) + DC DMA (WV portion: Berkeley, Jefferson) + Wheeling (WV portion) + Parkersburg (WV portion) + Bluefield-Beckley (WV portion) + Roanoke-Lynchburg (WV portion: Mercer)

### HI — Hawaii (1.4M, 1 Market)
- **HI-01 All Hawaii** (1.4M): Honolulu DMA (covers all islands)

### NH — New Hampshire (1.4M, 1 Market)
- **NH-01 All New Hampshire** (1.4M): Boston (NH portion: Hillsborough, Rockingham, Strafford) + Burlington-Plattsburgh (NH portion) + Portland-Auburn ME (NH portion: Carroll)

### ME — Maine (1.4M, 1 Market)
- **ME-01 All Maine** (1.4M): Portland-Auburn ME + Bangor + Presque Isle

### MT — Montana (1.1M, 1 Market)
- **MT-01 All Montana** (1.1M): Billings + Missoula + Great Falls + Butte-Bozeman + Glendive + Helena

### RI — Rhode Island (1.1M, 1 Market)
- **RI-01 All Rhode Island** (1.1M): Providence-New Bedford (RI counties only)

---

## Tiny States (<1M, documented exceptions) — 7 jurisdictions, 7 Markets

| Market | Jurisdiction | Pop | Underlying Nielsen DMAs |
|---|---|---:|---|
| DE-01 | All Delaware | 1.0M | Philadelphia (DE counties: New Castle, Kent, Sussex) |
| SD-01 | All South Dakota | 895K | Sioux Falls (SD portion) + Rapid City + Minot-Bismarck (SD portion: NW) |
| ND-01 | All North Dakota | 770K | Fargo (ND portion) + Minot-Bismarck-Dickinson |
| AK-01 | All Alaska | 735K | Anchorage + Fairbanks + Juneau |
| DC-01 | District of Columbia | 700K | DC DMA (DC only — see DMA Note above) |
| VT-01 | All Vermont | 647K | Burlington-Plattsburgh (VT portion) + Albany (VT portion) |
| WY-01 | All Wyoming | 580K | Cheyenne-Scottsbluff (WY portion) + Casper-Riverton + Salt Lake City (WY portion) + Denver (WY portion: Laramie) + Billings (WY portion: NW) |

**Strategic note:** SC may choose not to actively prospect tiny states (low PI lead volume, low ARPU potential). Markets exist so coverage is possible if a client requests.

---

## Notable cross-state Nielsen DMAs and how they were split

| Market | States touched | Resulting Markets |
|---|---|---|
| New York | NY, NJ, CT, PA | NY-01 + NJ-01 + CT-01 (PA portion negligible, in PA-04) |
| Philadelphia | PA, NJ, DE, MD | PA-01 + NJ-02 + DE-01 + MD-01 (Cecil) |
| Washington DC | DC, MD, VA, WV | DC-01 + MD-01 + VA-01 + WV-01 (panhandle) |
| Chicago | IL, IN | IL-01 + IN-02 |
| Cincinnati | OH, KY, IN | OH-03 + KY-02 + IN-03 |
| St. Louis | MO, IL | MO-01 + IL-03 |
| Kansas City | MO, KS | MO-02 + KS-02 |
| Memphis | TN, MS, AR | TN-02 + MS-01 + AR-02 |
| Charlotte | NC, SC | NC-01 + SC-02 |
| Boston | MA, NH | MA-01 + NH-01 |
| Salt Lake City | UT, ID, NV, WY | UT-01 + ID-01 + NV-02 + WY-01 |
| Yuma-El Centro | AZ, CA | AZ-01 + CA-05 |
| Reno | NV, CA | NV-02 + CA-03 |
| Paducah | KY, MO, IL, IN, TN | KY-02 + MO-02 + IL-03 + IN-03 + TN-02 |

---

## Build status

| Phase | State(s) | Status |
|---|---|---|
| Phase 1 | National framework + this doc | ✅ Complete (2026-04-23) |
| Phase 2 | CA full ZIP-level build | ✅ Complete |
| Phase 3 | Other states on demand | ⏳ As clients request |

**Next likely build:** TX (Tofer expansion candidate?) or NY (high-volume PI market). Each state takes 2–4 hours given methodology is locked.

---

## Decisions deferred

- **Tiny-state economics** — actively prospect or skip? Affects total addressable market calculation.
- **MD Market split** — kept single (MD-01 = 6.2M). Revisit if Eastern Shore or Western MD demand emerges.
- **NV-02 (Reno)** — sub-1M exception. Northern NV is genuinely different market from Vegas; kept split.
- **CT split** — collapsed to single Market (CT-01 = 3.6M, all CT). Eastern CT culturally distinct but volume too small for separate exclusivity.
- **MO Market count** — currently 2 (St. Louis MO + KC MO + rest). Could go to 3 if Springfield/Joplin warrants split. Defer until client data supports.
