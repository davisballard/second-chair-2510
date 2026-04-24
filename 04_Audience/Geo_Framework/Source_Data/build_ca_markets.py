#!/usr/bin/env python3
"""
Build CA Markets master file from Census ZCTA-County data.

Input:  ca_zcta_primary_county.csv (built by previous step)
Output: ../States/CA/CA_Markets.csv  + per_market_zips/CA-NN_*.txt

Methodology: see ../Methodology.md
"""
import csv
from pathlib import Path
from collections import defaultdict

HERE = Path(__file__).parent
CA_DIR = HERE.parent / "States" / "CA"
CA_DIR.mkdir(parents=True, exist_ok=True)
(CA_DIR / "per_market_zips").mkdir(exist_ok=True)

# County FIPS -> (market_id, market_name, nielsen_dma_origin)
# Market mapping per approved framework v1.1 (2026-04-23)
# v1.1: Split former CA-01 (Greater LA + Coachella) into CA-01 LA Core + CA-04 Inland Empire + Coachella.
#       Renumbered CA-03/04/05/06 by population. See changelog.
# nielsen_dma_origin tracks which Nielsen DMA each county came from (reference column)
COUNTY_MAP = {
    # CA-01 Greater LA Core (13.7M) — coastal/urban LA only, IE+Coachella split off
    "06037": ("CA-01", "Greater LA Core", "Los Angeles"),  # Los Angeles
    "06059": ("CA-01", "Greater LA Core", "Los Angeles"),  # Orange
    "06111": ("CA-01", "Greater LA Core", "Los Angeles"),  # Ventura
    "06027": ("CA-01", "Greater LA Core", "Los Angeles"),  # Inyo

    # CA-02 Bay Area (7.7M)
    "06075": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # San Francisco
    "06001": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Alameda
    "06013": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Contra Costa
    "06081": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # San Mateo
    "06085": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Santa Clara
    "06041": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Marin
    "06097": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Sonoma
    "06055": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Napa
    "06095": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Solano
    "06033": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Lake
    "06045": ("CA-02", "Bay Area", "San Francisco-Oakland-San Jose"),  # Mendocino

    # CA-03 Sacramento + Far North (5.0M) — was CA-04 in v1.0
    "06067": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Sacramento
    "06113": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Yolo
    "06101": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Sutter
    "06115": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Yuba
    "06061": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Placer
    "06017": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # El Dorado
    "06077": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # San Joaquin
    "06099": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Stanislaus
    "06005": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Amador
    "06009": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Calaveras
    "06109": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Tuolumne
    "06003": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Alpine
    "06057": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Nevada
    "06091": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Sierra
    "06063": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Plumas
    "06011": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Colusa
    "06021": ("CA-03", "Sacramento + Far North", "Sacramento-Stockton-Modesto"),  # Glenn
    "06007": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Butte
    "06089": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Shasta
    "06103": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Tehama
    "06105": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Trinity
    "06093": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Siskiyou
    "06049": ("CA-03", "Sacramento + Far North", "Chico-Redding"),                # Modoc
    "06023": ("CA-03", "Sacramento + Far North", "Eureka"),                       # Humboldt
    "06015": ("CA-03", "Sacramento + Far North", "Eureka"),                       # Del Norte
    "06035": ("CA-03", "Sacramento + Far North", "Reno (CA portion)"),            # Lassen
    "06051": ("CA-03", "Sacramento + Far North", "Reno (CA portion)"),            # Mono

    # CA-04 Inland Empire + Coachella (4.7M) — NEW in v1.1, split from former CA-01
    "06071": ("CA-04", "Inland Empire + Coachella", "Los Angeles (Inland Empire)"),  # San Bernardino
    "06065": ("CA-04", "Inland Empire + Coachella", "Los Angeles + Palm Springs"),   # Riverside (whole county per Rule 5)

    # CA-05 San Diego + Imperial (3.5M) — was CA-03 in v1.0
    "06073": ("CA-05", "San Diego + Imperial", "San Diego"),                       # San Diego
    "06025": ("CA-05", "San Diego + Imperial", "Yuma-El Centro (CA portion)"),     # Imperial

    # CA-06 Central Valley (3.0M) — was CA-05 in v1.0 (Tofer's market)
    "06019": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Fresno
    "06107": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Tulare
    "06031": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Kings
    "06039": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Madera
    "06043": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Mariposa
    "06047": ("CA-06", "Central Valley", "Fresno-Visalia"),  # Merced
    "06029": ("CA-06", "Central Valley", "Bakersfield"),     # Kern

    # CA-07 Central Coast (1.5M) — was CA-06 in v1.0
    "06053": ("CA-07", "Central Coast", "Monterey-Salinas"),                              # Monterey
    "06069": ("CA-07", "Central Coast", "Monterey-Salinas"),                              # San Benito
    "06087": ("CA-07", "Central Coast", "Monterey-Salinas"),                              # Santa Cruz
    "06083": ("CA-07", "Central Coast", "Santa Barbara-Santa Maria-San Luis Obispo"),     # Santa Barbara
    "06079": ("CA-07", "Central Coast", "Santa Barbara-Santa Maria-San Luis Obispo"),     # San Luis Obispo
}

# County FIPS -> 2023 ACS population estimate (rounded to nearest 1000)
COUNTY_POP = {
    "06001": 1650000, "06003": 1200, "06005": 41000, "06007": 211000, "06009": 46000,
    "06011": 22000, "06013": 1160000, "06015": 27000, "06017": 192000, "06019": 1010000,
    "06021": 28000, "06023": 132000, "06025": 180000, "06027": 19000, "06029": 920000,
    "06031": 153000, "06033": 67000, "06035": 28000, "06037": 9720000, "06039": 162000,
    "06041": 256000, "06043": 17000, "06045": 90000, "06047": 290000, "06049": 8500,
    "06051": 13500, "06053": 432000, "06055": 134000, "06057": 102000, "06059": 3170000,
    "06061": 421000, "06063": 19000, "06065": 2494000, "06067": 1599000, "06069": 67000,
    "06071": 2194000, "06073": 3290000, "06075": 808000, "06077": 803000, "06079": 282000,
    "06081": 738000, "06083": 444000, "06085": 1872000, "06087": 263000, "06089": 181000,
    "06091": 3200, "06093": 43000, "06095": 449000, "06097": 488000, "06099": 552000,
    "06101": 100000, "06103": 65000, "06105": 16000, "06107": 478000, "06109": 53000,
    "06111": 832000, "06113": 220000, "06115": 86000,
}

assert len(COUNTY_MAP) == 58, f"Expected 58 counties, got {len(COUNTY_MAP)}"
assert len(COUNTY_POP) == 58, f"Expected 58 county pops, got {len(COUNTY_POP)}"
assert set(COUNTY_MAP) == set(COUNTY_POP), "County FIPS mismatch between MAP and POP"

# Read the primary-county file produced earlier
rows = []
with open(HERE / "ca_zcta_primary_county.csv") as f:
    next(f)  # skip header
    for line in f:
        zip_, cfips, cname = line.rstrip("\n").split(",")
        if cfips not in COUNTY_MAP:
            print(f"WARN: ZIP {zip_} county {cfips} ({cname}) not in COUNTY_MAP")
            continue
        market_id, market_name, nielsen_dma_origin = COUNTY_MAP[cfips]
        pop = COUNTY_POP[cfips]
        rows.append({
            "zip": zip_,
            "county": cname,
            "county_fips": cfips,
            "market_id": market_id,
            "market_name": market_name,
            "state": "CA",
            "nielsen_dma_origin": nielsen_dma_origin,
            "county_population_2023": pop,
        })

# Sort by market_id then zip
rows.sort(key=lambda r: (r["market_id"], r["zip"]))

# Write master CSV
master = CA_DIR / "CA_Markets.csv"
with open(master, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=[
        "zip", "county", "county_fips", "market_id", "market_name",
        "state", "nielsen_dma_origin", "county_population_2023"
    ])
    w.writeheader()
    w.writerows(rows)
print(f"Wrote {master} ({len(rows)} rows)")

# Per-market TXT files (just ZIPs)
by_market = defaultdict(list)
for r in rows:
    by_market[r["market_id"]].append((r["market_name"], r["zip"]))

market_short_names = {
    "CA-01": "GreaterLA_Core",
    "CA-02": "BayArea",
    "CA-03": "Sacramento_FarNorth",
    "CA-04": "InlandEmpire_Coachella",
    "CA-05": "SanDiego_Imperial",
    "CA-06": "CentralValley",
    "CA-07": "CentralCoast",
}

for mid, zips in sorted(by_market.items()):
    short = market_short_names[mid]
    fname = CA_DIR / "per_market_zips" / f"{mid}_{short}.txt"
    with open(fname, "w") as f:
        for _, z in sorted(zips, key=lambda x: x[1]):
            f.write(z + "\n")
    print(f"  {fname.name}: {len(zips)} zips")

# Verification summary
print("\n--- VERIFICATION ---")
state_pop_total = sum(COUNTY_POP.values())
print(f"Total CA county pop: {state_pop_total:,} (~39.0M expected)")
print()
print(f"{'Market':<8} {'Pop':>12}  {'Counties':>9}  {'ZIPs':>5}  Name")
market_pop = defaultdict(int)
market_counties = defaultdict(set)
market_zips = defaultdict(int)
for r in rows:
    market_zips[r["market_id"]] += 1
    market_counties[r["market_id"]].add(r["county_fips"])
for cfips, (mid, _, _) in COUNTY_MAP.items():
    market_pop[mid] += COUNTY_POP[cfips]
for mid in sorted(market_pop):
    name = next(n for c, (m, n, d) in COUNTY_MAP.items() if m == mid)
    floor_ok = "PASS" if market_pop[mid] >= 1_000_000 else "FAIL"
    print(f"{mid:<8} {market_pop[mid]:>12,}  {len(market_counties[mid]):>9}  {market_zips[mid]:>5}  {name} [{floor_ok}]")

# State-purity check (all zips should be 90000-96199)
out_of_range = [r["zip"] for r in rows if not ("90000" <= r["zip"] <= "96199")]
print(f"\nZIPs outside 90000-96199 range: {len(out_of_range)}")
if out_of_range:
    print(f"  {out_of_range[:10]}")

# Coverage check
covered_counties = set(r["county_fips"] for r in rows)
missing = set(COUNTY_MAP) - covered_counties
print(f"\nCounties without any ZIPs: {len(missing)}")
if missing:
    print(f"  {missing}")
