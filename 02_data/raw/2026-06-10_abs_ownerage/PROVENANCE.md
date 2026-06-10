# PROVENANCE: Census ABS 2023, Characteristics of Business Owners, owner age by sector

**Status: PENDING DOWNLOAD (SCRIPT-ONLY).** Sandbox egress to api.census.gov is blocked, and the Census API now requires an API key on every data query (verified 2026-06-10; keyless queries return "Missing Key"). Run the fetch script below from this Mac. The script appends a Landing record section to this file with hashes, row counts, and the owner-age categories found.

## Dataset

- Name: Annual Business Survey (ABS), Characteristics of Business Owners (CBO), owner age question, U.S. level, by NAICS sector
- Publisher: U.S. Census Bureau (with NSF NCSES)
- Vintage / reference year: 2023 ABS CBO (api vintage 2023, temporal 2023/2023, endpoint metadata modified 2025-07-09). Confirmed newest: /data/2024/abscbo does not exist as of 2026-06-10; /data/2022/abscbo is the prior vintage.
- API discovery doc: https://api.census.gov/data/2023/abscbo
- Table group: AB2300CSCBO, "Annual Business Survey: Owner Characteristics of Respondent Employer Firms by Sector, Sex, Ethnicity, Race, and Veteran Status for the U.S., States, Metro Areas, and Counties: 2023"
- License: CC0 public domain (per dataset metadata: https://creativecommons.org/publicdomain/zero/1.0/). Redistribution OK.

## Granularity note (flag)

The 2023 CBO table is published by NAICS **sector** (2-digit) only; the table title says "by Sector" and NAICS2022=00 is "Total for all sectors". Owner-age by 3- or 4-digit NAICS is not published in CBO. The fetch script empirically verifies this by listing the distinct NAICS2022 codes returned.

## Retrieval method

- Method: python3 03_engine/scripts/fetch_abs_ownerage.py (stdlib only)
- Requires CENSUS_API_KEY in keys.env at project root (already present). The key is read at runtime and never written to this file; recorded query URLs show key=REDACTED.
- Query 1 (discovery, saved as raw JSON): enumerate QDESC question codes and OWNCHAR categories at US level, total sector, all-owner demographics, to locate the owner age question (QDESC label containing "AGE", historically OWNRAGE).
  https://api.census.gov/data/2023/abscbo?get=QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL&for=us:*&NAICS2022=00&OWNER_SEX=001&OWNER_ETH=001&OWNER_RACE=00&OWNER_VET=001&key=REDACTED
- Query 2 (main pull, saved as raw JSON exactly as returned): all sectors, all demographic groups, owner-age question only, employer-firm owner counts and percent shares:
  https://api.census.gov/data/2023/abscbo?get=GEO_ID,NAME,NAICS2022,NAICS2022_LABEL,OWNER_SEX,OWNER_SEX_LABEL,OWNER_ETH,OWNER_ETH_LABEL,OWNER_RACE,OWNER_RACE_LABEL,OWNER_VET,OWNER_VET_LABEL,QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL,YEAR,OWNPDEMP,OWNPDEMP_F,OWNPDEMP_S,OWNPDEMP_PCT,OWNPDEMP_PCT_S&for=us:*&QDESC=[owner-age code from Query 1]&key=REDACTED
- The script also writes a flattened CSV of Query 2 (regenerable from the raw JSON).
- Fallback if the API fights: pre-made CBO tables at https://www.census.gov/data/tables/2023/econ/abs/2023-abs-characteristics-of-business-owners.html

## Files expected in this folder after landing

- abscbo2023_qdesc_discovery_us_total.json (raw API bytes, Query 1)
- abscbo2023_ownerage_us_by_sector.json (raw API bytes, Query 2)
- abscbo2023_ownerage_us_by_sector_flat.csv (flattened from Query 2)

## Variables (confirmed from API metadata 2026-06-10T16:18Z UTC via groups/AB2300CSCBO.json)

Dimensions: NAICS2022 (+LABEL, +F), OWNER_SEX, OWNER_ETH, OWNER_RACE, OWNER_VET (+LABELs), QDESC (+LABEL), OWNCHAR (+LABEL), YEAR, GEO_ID (+F), NAME. Measures: OWNPDEMP (count of owners of respondent employer firms), OWNPDEMP_F, OWNPDEMP_S (RSE), OWNPDEMP_PCT (percent share), OWNPDEMP_PCT_S (+flags).

Expected owner-age OWNCHAR categories (verify on landing; script prints actual): Under 25; 25 to 34; 35 to 44; 45 to 54; 55 to 64; 65 or over; plus an all-owners total and item-not-reported bucket.

## File hashes and row counts

Pending. Auto-appended by the fetch script as a Landing record below.

## Blockage record

- 2026-06-10T16:13Z to 16:22Z UTC: sandbox shell egress to api.census.gov refused by proxy allowlist (X-Proxy-Error: blocked-by-allowlist). Census API additionally requires a key on every data query, so no data rows were pulled via the agent's web fetch either (key kept out of logged URLs by policy). Metadata-only reconnaissance done via web fetch on the discovery doc, groups.json, and variables endpoints; those confirmed vintage, group ID, and the variable set above. No workaround attempted for the data pull.
- Collected by: DATA-2 agent (Claude), session 2026-06-10.
