# PROVENANCE: Eloundou et al., "GPTs are GPTs" occupation-level exposure scores

## Source
- Dataset page: https://github.com/openai/GPTs-are-GPTs (official OpenAI repository)
- File of record: `data/occ_level.csv` in that repository
- Paper: Eloundou, Manning, Mishkin, Rock. "GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models." arXiv:2303.10130. Journal version: "GPTs are GPTs: Labor market impact potential of LLMs," Science 384(6702), 2024, DOI 10.1126/science.adj0998.
- Repository commit pulled: `0471612fef3cc22b74fb884d27bff9dbd3770582` (commit date 2025-10-03 17:18:48 -0700, sole committer Pamela Mishkin / manlikemishap)

## Retrieval
- Timestamp (UTC): 2026-06-10T16:15:00Z (clone), files copied and verified 2026-06-10T16:18Z
- Method: `git clone --depth 1 https://github.com/openai/GPTs-are-GPTs.git`, then copied `data/occ_level.csv`, `LICENSE`, and `README.md` unmodified into this folder.
- Why git and not a direct file download: the sandbox network proxy returns 403 Forbidden for raw.githubusercontent.com and codeload.github.com. github.com itself is reachable, and git smart HTTP over github.com is the official endpoint for this repository. No mirrors or proxies used.
- Integrity: git blob hash of the copied `occ_level.csv` recomputed locally (`git hash-object`) = `faf734ccef32b373b16899d40636a9ff8de52a40`, identical to the blob recorded in the repository tree at the pulled commit. Byte-for-byte match with the official source confirmed.

## License / terms
- MIT License, Copyright (c) 2024 OpenAI. Full text in `LICENSE` in this folder.
- Redistribution: permitted, including in a public repo, provided the copyright and permission notice are retained. Cite the paper (arXiv:2303.10130 / Science 2024).

## Files
| File | sha256 | Size (bytes) |
|------|--------|--------------|
| occ_level.csv | 40c74f53de40aec91c0017d80690cbba915f83a8bb414bcf2f884692f1749acb | 126022 |
| LICENSE | d831db55645e47ca8e491c5a0e37f1ee744d7b10bf5aa8d50146c795ac0176c0 | 1063 |
| README.md | fb8ae66d02142a9b7178d8cbd59b90a6c5bd80bf088107cae126f4276c8d68c6 | 172 |

`LICENSE` and `README.md` are repository documentation copied for provenance; `occ_level.csv` is the data file.

## Structure: occ_level.csv
- Rows: 923 data rows + 1 header row
- Columns (8): `O*NET-SOC Code`, `Title`, `dv_rating_alpha`, `dv_rating_beta`, `dv_rating_gamma`, `human_rating_alpha`, `human_rating_beta`, `human_rating_gamma`
- Per repo README: `dv_rating` = GPT-4 annotations, `human` = human annotators; `_alpha` = E1 (direct exposure), `_beta` = E1 + 0.5 x E2, `_gamma` = E1 + E2. Values are 0 to 1 shares of occupation task exposure.
- No null cells. No duplicate occupation codes.
- Taxonomy note: codes are O*NET-SOC 2019. 774 rows are base codes ending in `.00`; 149 rows are detailed specialty codes (suffix other than `.00`, for example 11-1011.03). Joining to BLS 6-digit SOC 2018 requires collapsing specialty codes to their parent SOC.

## Flags
- The repo holds task-level labels too (`full_labelset.tsv`); not pulled, out of this collection's scope. Re-pull from the same commit if needed.
- arXiv and science.org were unreachable from the sandbox (proxy 403), so the journal supplementary materials were not compared. The GitHub repo is the authors' canonical machine-readable release.
