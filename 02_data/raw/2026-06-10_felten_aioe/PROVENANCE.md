# PROVENANCE: Felten, Raj, Seamans AI Occupational Exposure (AIOE)

## Source
- Dataset page: https://github.com/AIOE-Data/AIOE (official repository maintained by the authors)
- Paper: Felten E, Raj M, Seamans R (2021). "Occupational, industry, and geographic exposure to artificial intelligence: A novel dataset and its potential uses." Strategic Management Journal 42(12):2195-2217. DOI 10.1002/smj.3286.
- Repository commit pulled: `adca5fc2cd0e9a659ff05278b7fa7a53f4f324c1` (commit date 2024-06-03 17:11:20 -0400)

## Retrieval
- Timestamp (UTC): 2026-06-10T16:16:00Z (clone), files copied and verified 2026-06-10T16:18Z
- Method: `git clone --depth 1 https://github.com/AIOE-Data/AIOE.git`, then copied the four files below unmodified into this folder.
- Why git and not a direct file download: the sandbox network proxy returns 403 Forbidden for raw.githubusercontent.com and codeload.github.com. github.com itself is reachable, and git smart HTTP over github.com is the official endpoint for this repository. No mirrors or proxies used.
- Integrity: git blob hashes of all four copied files recomputed locally (`git hash-object`) match the blobs in the repository tree at the pulled commit. Byte-for-byte match with the official source confirmed.

## License / terms
- No LICENSE file in the repository. The README requests citation of the SMJ paper if the data are used (citation above) and gives author contacts (manavraj@wharton.upenn.edu, rseamans@stern.nyu.edu).
- Redistribution: no explicit license means no general redistribution right; under GitHub Terms of Service the public may view and fork, nothing more. For the public-repo decision: do not redistribute these xlsx files; link to the source repo and publish only derived aggregates with the requested citation. Author permission is the safe route if file redistribution is ever wanted.

## Files
| File | sha256 | Size (bytes) |
|------|--------|--------------|
| AIOE_DataAppendix.xlsx | c123b4c64840aff3568ae6c97256678719b88a74d45b6362dbefb5af34667b95 | 170359 |
| Language Modeling AIOE and AIIE.xlsx | ccdd1fb916dfa404914367eafde7c00b7148ea86f18fe616240bc85cf6131c8b | 55714 |
| Image Generation AIOE and AIIE.xlsx | 62c310544a6c1181037484b4c4017443c8d32661a0bdd482967a108aa224f5f7 | 55523 |
| README.md | 6410cb1e5f874aeebc458d2d49267db41b3c5c7ec05f3d1dc790e60d1cd18db2 | 1936 |

`README.md` is repository documentation copied for provenance; the three xlsx files are the data.

## Structure
The repository publishes xlsx only; no CSV exists at the source. Read with pandas + openpyxl.

AIOE_DataAppendix.xlsx (sheets and shapes, data rows x columns):
- `Index`: sheet descriptions
- `Appendix A`: 774 x 3, columns `SOC Code`, `Occupation Title`, `AIOE`  <- the occupation-level AIOE scores (primary)
- `Appendix B`: 250 x 3, columns `NAICS`, `Industry Title`, `AIIE` (4-digit NAICS industry exposure)
- `Appendix C`: 3271 x 3, columns `FIPS Code`, `Geographic Area`, `AIGE` (county exposure)
- `Appendix D`: 52 x 11, AI application x occupational ability relatedness matrix
- `Appendix E`: 52 x 2, columns `O*NET Abilities`, `Ability-Level AI Exposure`

Language Modeling AIOE and AIIE.xlsx: sheets `LM AIOE` (774 x 3: `SOC Code`, `Occupation Title`, `Language Modeling AIOE`) and `LM AIIE`. Image Generation AIOE and AIIE.xlsx: sheets `IG AIOE` (774 x 3) and `IG AIIE`. These are the authors' generative-AI extensions; the LM AIOE is the LLM-specific sensitivity variant.

- Appendix A has no null cells and no duplicate SOC codes.
- Taxonomy note: SOC codes are 6-digit without O*NET suffixes (for example 11-1011), 774 occupations, consistent with the SOC 2010 / O*NET-SOC vintage used in the 2021 paper. Joining to Eloundou (O*NET-SOC 2019) or OEWS (SOC 2018) requires a SOC 2010 to SOC 2018 crosswalk for the handful of changed codes.

## Flags
- The `Input/` and `Generative AI/` folders (Stata .do files and .dta inputs that construct the scores) were not pulled; out of collection scope, available at the same commit.
