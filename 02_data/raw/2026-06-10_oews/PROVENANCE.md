# PROVENANCE: BLS OEWS May 2025, national industry-specific estimates

**Status: PENDING DOWNLOAD (SCRIPT-ONLY).** Sandbox egress to bls.gov is blocked; see Blockage record. Run the fetch script below from this Mac to land the files. The script appends a Landing record section to this file with hashes and verification output.

## Dataset

- Name: Occupational Employment and Wage Statistics (OEWS), May 2025, national industry-specific and by ownership estimates
- Publisher: U.S. Bureau of Labor Statistics
- Vintage / reference period: May 2025 (newest published release as of 2026-06-10; OEWS publishes each May reference period the following spring; tables page last modified 2026-05-15)
- Catalog page: https://www.bls.gov/oes/tables.htm (section "May 2025" > "National industry-specific and by ownership")
- Exact download URL: https://www.bls.gov/oes/special-requests/oesm25in4.zip
- Fallback (prior vintage, only if 2025 file is ever pulled by BLS): https://www.bls.gov/oes/special-requests/oesm24in4.zip
- License: U.S. federal government work, public domain. Redistribution OK.

## Why this file

Engine backbone: occupation employment by NAICS industry at the national level. The in4 zip carries the industry-specific XLSX files at sector, 3-digit, 4-digit, and 5-digit (where available) NAICS levels, plus ownership breakouts and a field-descriptions file.

## Retrieval method

- Method: python3 03_engine/scripts/fetch_oews.py (stdlib only; openpyxl optional for the XLSX row verification step)
- The script downloads the zip exactly as published, computes sha256, extracts to oesm25in4/ inside this folder, verifies that 4-digit industry files exist in the archive, and (if openpyxl is installed) prints a NAICS 5412 example row from the 4-digit file.
- No API key required.

## Expected contents (confirm on landing; script prints actual member list)

- oesm25in4.zip containing XLSX files named like natsector_M2025_dl.xlsx, nat3d_M2025_dl.xlsx, nat4d_M2025_dl.xlsx, nat5d_M2025_dl.xlsx, ownership files, and a field descriptions file.

## Expected columns (per OEWS field descriptions; confirm on landing)

AREA, AREA_TITLE, AREA_TYPE, PRIM_STATE, NAICS, NAICS_TITLE, I_GROUP, OWN_CODE, OCC_CODE, OCC_TITLE, O_GROUP, TOT_EMP, EMP_PRSE, PCT_TOTAL, PCT_RPT, H_MEAN, A_MEAN, MEAN_PRSE, H_PCT10, H_PCT25, H_MEDIAN, H_PCT75, H_PCT90, A_PCT10, A_PCT25, A_MEDIAN, A_PCT75, A_PCT90, ANNUAL, HOURLY

## File hashes and row counts

Pending. Auto-appended by the fetch script as a Landing record below.

## Blockage record

- 2026-06-10T16:13Z to 16:22Z UTC: sandbox shell egress to www.bls.gov and download.bls.gov refused by proxy allowlist (HTTP 403, X-Proxy-Error: blocked-by-allowlist). Per fetch discipline, no workaround attempted; catalog reconnaissance only was done via web fetch on https://www.bls.gov/oes/tables.htm to pin the exact URL and confirm May 2025 is the newest published vintage.
- Collected by: DATA-2 agent (Claude), session 2026-06-10.
