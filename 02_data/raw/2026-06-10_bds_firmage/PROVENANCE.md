# PROVENANCE: Census BDS 2023, firm age by 4-digit NAICS

**Status: PENDING DOWNLOAD (SCRIPT-ONLY).** Sandbox egress to www2.census.gov is blocked; see Blockage record. Run the fetch script below from this Mac. The script appends a Landing record section to this file with hash, row count, and the firm-age buckets found.

## Dataset

- Name: Business Dynamics Statistics (BDS), 1978-2023, two-way table: 4-digit NAICS by Firm Age
- Publisher: U.S. Census Bureau
- Vintage: BDS 2023 (newest release as of 2026-06-10; the 2023 BDS release notes are at https://www.census.gov/programs-surveys/bds/news-updates/updates/2023-bds-release.html)
- Catalog page: https://www.census.gov/data/datasets/time-series/econ/bds/bds-datasets.html (listed as "4-digit NAICS by Firm Age", 20MB)
- Exact download URL: https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_vcn4_fa.csv
- Related (not pulled): 3-digit version at https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_vcn3_fa.csv
- Codebook / methodology: https://www.census.gov/programs-surveys/bds/documentation/methodology.html
- License: U.S. federal government work, public domain. Redistribution OK.

## Why this file

Complement check for the succession story: firm-age composition by 4-digit NAICS industry, to compare AI-exposed service categories against AI-insulated trades on incumbency and firm aging.

## Retrieval method

- Method: python3 03_engine/scripts/fetch_bds_firmage.py (stdlib only)
- No API key required. The script downloads the CSV exactly as published, computes sha256, counts rows, prints the header, lists the distinct firm-age (fage) buckets and the count of distinct 4-digit NAICS codes, and prints a NAICS 5412 example row for the latest year.

## Expected columns (per BDS codebook; confirm on landing, script prints actual header)

year, vcnaics4, fage, firms, estabs, emp, denom, estabs_entry, estabs_entry_rate, estabs_exit, estabs_exit_rate, job_creation, job_creation_births, job_creation_continuers, job_creation_rate_births, job_creation_rate, job_destruction, job_destruction_deaths, job_destruction_continuers, job_destruction_rate_deaths, job_destruction_rate, net_job_creation, net_job_creation_rate, reallocation_rate, firmdeath_firms, firmdeath_estabs, firmdeath_emp

## Expected firm-age buckets (per BDS codebook; confirm on landing, script prints actual)

a) 0, b) 1, c) 2, d) 3, e) 4, f) 5, g) 6 to 10, h) 11 to 15, i) 16 to 20, j) 21 to 25, k) 26+, l) Left Censored

## File hashes and row counts

Pending. Auto-appended by the fetch script as a Landing record below.

## Blockage record

- 2026-06-10T16:13Z to 16:22Z UTC: sandbox shell egress to www2.census.gov and www.census.gov refused by proxy allowlist (HTTP 403, X-Proxy-Error: blocked-by-allowlist). Per fetch discipline, no workaround attempted; catalog reconnaissance only was done via web fetch on the BDS datasets page to pin the exact URL and confirm BDS 2023 is the newest vintage.
- Collected by: DATA-2 agent (Claude), session 2026-06-10.
