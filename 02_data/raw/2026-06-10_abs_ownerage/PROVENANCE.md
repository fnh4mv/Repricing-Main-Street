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

## Landing record (auto-appended by fetch_abs_ownerage.py)

- Retrieved (UTC): 2026-06-10T19:05:42Z
- Endpoint: https://api.census.gov/data/2023/abscbo (key=REDACTED)
- Owner-age question: QDESC=O09 (OWNRAGE)
- Owner-age categories: 25 to 34; 35 to 44; 45 to 54; 55 to 64; 65 or over; Item not reported; Total reporting; Under 25
- abscbo2023_qdesc_discovery_us_total.json: 10,225 bytes, sha256 c6bc6eb415f1ed83e4e5b8776828610ac70fdbb90cc9e40855ba64839856d7f8, 114 rows
- abscbo2023_ownerage_us_by_sector.json: 29,011,263 bytes, sha256 9e2a6ebd01068d9c3c52411cbc1aa87db6577740b76081658982f24259048fa9, 103,152 rows
- abscbo2023_ownerage_us_by_sector_flat.csv: flattened from main JSON, 103,152 rows, sha256 6944d31469c67dee6192422ab506b2207e3a291be83efd58e5411aed39a472fe
- Columns: GEO_ID, NAME, NAICS2022, NAICS2022_LABEL, OWNER_SEX, OWNER_SEX_LABEL, OWNER_ETH, OWNER_ETH_LABEL, OWNER_RACE, OWNER_RACE_LABEL, OWNER_VET, OWNER_VET_LABEL, QDESC, QDESC_LABEL, OWNCHAR, OWNCHAR_LABEL, YEAR, OWNPDEMP, OWNPDEMP_F, OWNPDEMP_S, OWNPDEMP_PCT, OWNPDEMP_PCT_S, QDESC, us
- Distinct NAICS2022 codes: 00, 11, 113, 1131, 1132, 1133, 114, 1141, 1142, 115, 1151, 1152, 1153, 21, 211, 2111, 212, 2121, 2122, 2123, 213, 2131, 22, 221, 2211, 2212, 2213, 23, 236, 2361, 2362, 237, 2371, 2372, 2373, 2379, 238, 2381, 2382, 2383, 2389, 31-33, 311, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 312, 3121, 3122, 313, 3131, 3132, 3133, 314, 3141, 3149, 315, 3151, 3152, 3159, 316, 3161, 3162, 3169, 321, 3211, 3212, 3219, 322, 3221, 3222, 323, 3231, 324, 3241, 325, 3251, 3252, 3253, 3254, 3255, 3256, 3259, 326, 3261, 3262, 327, 3271, 3272, 3273, 3274, 3279, 331, 3311, 3312, 3313, 3314, 3315, 332, 3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 333, 3331, 3332, 3333, 3334, 3335, 3336, 3339, 334, 3341, 3342, 3343, 3344, 3345, 3346, 335, 3351, 3352, 3353, 3359, 336, 3361, 3362, 3363, 3364, 3365, 3366, 3369, 337, 3371, 3372, 3379, 339, 3391, 3399, 42, 423, 4231, 4232, 4233, 4234, 4235, 4236, 4237, 4238, 4239, 424, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 425, 4251, 44-45, 441, 4411, 4412, 4413, 444, 4441, 4442, 445, 4451, 4452, 4453, 449, 4491, 4492, 455, 4551, 4552, 456, 4561, 457, 4571, 4572, 458, 4581, 4582, 4583, 459, 4591, 4592, 4593, 4594, 4595, 4599, 48-49, 481, 4811, 4812, 483, 4831, 4832, 484, 4841, 4842, 485, 4851, 4852, 4853, 4854, 4855, 4859, 486, 4861, 4862, 4869, 487, 4871, 4872, 4879, 488, 4881, 4882, 4883, 4884, 4885, 4889, 492, 4921, 4922, 493, 4931, 51, 512, 5121, 5122, 513, 5131, 5132, 516, 5161, 5162, 517, 5171, 5174, 5178, 518, 5182, 519, 5192, 52, 522, 5221, 5222, 5223, 523, 5231, 5239, 524, 5241, 5242, 53, 531, 5311, 5312, 5313, 532, 5321, 5322, 5323, 5324, 533, 5331, 54, 541, 5411, 5412, 5413, 5414, 5415, 5416, 5417, 5418, 5419, 55, 551, 5511, 56, 561, 5611, 5612, 5613, 5614, 5615, 5616, 5617, 5619, 562, 5621, 5622, 5629, 61, 611, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 62, 621, 6211, 6212, 6213, 6214, 6215, 6216, 6219, 622, 6221, 6222, 6223, 623, 6231, 6232, 6233, 6239, 624, 6241, 6242, 6243, 6244, 71, 711, 7111, 7112, 7113, 7114, 7115, 712, 7121, 713, 7131, 7132, 7139, 72, 721, 7211, 7212, 7213, 722, 7223, 7224, 7225, 81, 811, 8111, 8112, 8113, 8114, 812, 8121, 8122, 8123, 8129, 99
- Granularity: WARNING deeper codes present: 113, 1131, 1132, 1133, 114, 1141, 1142, 115, 1151, 1152, 1153, 211, 2111, 212, 2121, 2122, 2123, 213, 2131, 221, 2211, 2212, 2213, 236, 2361, 2362, 237, 2371, 2372, 2373, 2379, 238, 2381, 2382, 2383, 2389, 311, 3111, 3112, 3113, 3114, 3115, 3116, 3117, 3118, 3119, 312, 3121, 3122, 313, 3131, 3132, 3133, 314, 3141, 3149, 315, 3151, 3152, 3159, 316, 3161, 3162, 3169, 321, 3211, 3212, 3219, 322, 3221, 3222, 323, 3231, 324, 3241, 325, 3251, 3252, 3253, 3254, 3255, 3256, 3259, 326, 3261, 3262, 327, 3271, 3272, 3273, 3274, 3279, 331, 3311, 3312, 3313, 3314, 3315, 332, 3321, 3322, 3323, 3324, 3325, 3326, 3327, 3328, 3329, 333, 3331, 3332, 3333, 3334, 3335, 3336, 3339, 334, 3341, 3342, 3343, 3344, 3345, 3346, 335, 3351, 3352, 3353, 3359, 336, 3361, 3362, 3363, 3364, 3365, 3366, 3369, 337, 3371, 3372, 3379, 339, 3391, 3399, 423, 4231, 4232, 4233, 4234, 4235, 4236, 4237, 4238, 4239, 424, 4241, 4242, 4243, 4244, 4245, 4246, 4247, 4248, 4249, 425, 4251, 441, 4411, 4412, 4413, 444, 4441, 4442, 445, 4451, 4452, 4453, 449, 4491, 4492, 455, 4551, 4552, 456, 4561, 457, 4571, 4572, 458, 4581, 4582, 4583, 459, 4591, 4592, 4593, 4594, 4595, 4599, 481, 4811, 4812, 483, 4831, 4832, 484, 4841, 4842, 485, 4851, 4852, 4853, 4854, 4855, 4859, 486, 4861, 4862, 4869, 487, 4871, 4872, 4879, 488, 4881, 4882, 4883, 4884, 4885, 4889, 492, 4921, 4922, 493, 4931, 512, 5121, 5122, 513, 5131, 5132, 516, 5161, 5162, 517, 5171, 5174, 5178, 518, 5182, 519, 5192, 522, 5221, 5222, 5223, 523, 5231, 5239, 524, 5241, 5242, 531, 5311, 5312, 5313, 532, 5321, 5322, 5323, 5324, 533, 5331, 541, 5411, 5412, 5413, 5414, 5415, 5416, 5417, 5418, 5419, 551, 5511, 561, 5611, 5612, 5613, 5614, 5615, 5616, 5617, 5619, 562, 5621, 5622, 5629, 611, 6111, 6112, 6113, 6114, 6115, 6116, 6117, 621, 6211, 6212, 6213, 6214, 6215, 6216, 6219, 622, 6221, 6222, 6223, 623, 6231, 6232, 6233, 6239, 624, 6241, 6242, 6243, 6244, 711, 7111, 7112, 7113, 7114, 7115, 712, 7121, 713, 7131, 7132, 7139, 721, 7211, 7212, 7213, 722, 7223, 7224, 7225, 811, 8111, 8112, 8113, 8114, 812, 8121, 8122, 8123, 8129
- Verified by: fetch_abs_ownerage.py
