# PROVENANCE: Anthropic Economic Index (AEI), occupation and task level files

## Status: NOT YET DOWNLOADED. Sandbox network blockage recorded below. Run the fetch script.

- Fetch script: `03_engine/scripts/fetch_anthropic_aei.py` (run on the Mac: `python3 "03_engine/scripts/fetch_anthropic_aei.py"` from the project root)
- The script downloads the exact files listed below, pinned to a specific repo revision, verifies every byte against the git object ids recorded here, writes sha256 checksums, and appends a download log to this file.

## Source
- Dataset: https://huggingface.co/datasets/Anthropic/EconomicIndex (official Anthropic release)
- Repo revision pinned: `db51ecb12920faef6df2b21dff6207ebcbc72c6f` (repo lastModified 2026-05-21T05:15:51Z)
- Reports: https://www.anthropic.com/economic-index ; labor market impacts research page: https://www.anthropic.com/research/labor-market-impacts ; v2 paper: arXiv:2503.04761 (Handa et al. 2025, "Which Economic Tasks are Performed with AI?")

## Blockage record
- Timestamp (UTC): 2026-06-10T16:17:00Z
- The sandbox routes all traffic through an allowlist proxy (127.0.0.1:3128). CONNECT to huggingface.co returns 403 Forbidden. Verified with both curl and git clone over HTTPS. raw.githubusercontent.com, codeload.github.com, arxiv.org, and science.org are blocked the same way.
- Per collection rules, no mirrors, proxies, or workarounds were used. File inventory, sizes, and git object ids below were read from the official Hugging Face API (dataset page metadata) to pin exactly what the script must land.

## License / terms
- Repo README states: "Data released under CC-BY, code released under MIT License." Hugging Face card metadata tag: license: mit.
- Redistribution: data files may be redistributed (including a public repo) under CC-BY with attribution to Anthropic; cite the relevant release (see README citations; the labor market impacts files accompany the Anthropic labor market impacts research, and the v2 release files accompany arXiv:2503.04761).

## Files to land (pinned at revision db51ecb)
Download URL pattern: `https://huggingface.co/datasets/Anthropic/EconomicIndex/resolve/db51ecb12920faef6df2b21dff6207ebcbc72c6f/<path>`

| Path in repo | Size (bytes) | git blob sha1 (verification target) | What |
|---|---|---|---|
| labor_market_impacts/job_exposure.csv | 37176 | aae568975228d5850a1913c0d09f6ce8437e7253 | Occupation-level observed exposure. Columns: occ_code (SOC 2018 6-digit), title, observed_exposure. The newest occupation-level AEI artifact. |
| labor_market_impacts/task_penetration.csv | 1889822 | 2a20bcc33ccb02ae97c9aa6b2899bfa3911fc75b | Task-level penetration underlying job_exposure |
| release_2025_03_27/task_pct_v1.csv | 461306 | fa7771817633eea639cb4a23cb5d23010eee47e5 | Claude.ai usage share by O*NET task, v1 window (Dec 2024 to Jan 2025) |
| release_2025_03_27/task_pct_v2.csv | 435372 | 9b01af042ad5d422f328eed3a9b165a3a42c6208 | Claude.ai usage share by O*NET task, v2 window (Feb to Mar 2025) |
| release_2025_03_27/automation_vs_augmentation_by_task.csv | 561368 | 844e3bf4f227e5bd8a358d6558a4e3c37ac7ea2f | Task-level interaction-mode shares. Columns: task_name, feedback_loop, directive, task_iteration, validation, learning, filtered. directive + feedback_loop lean automation; task_iteration, learning, validation lean augmentation. |
| release_2025_03_27/automation_vs_augmentation_v1.csv | 197 | 3d12303285f43eb353684bd9520d63a306ad9d4f | Aggregate mode shares, v1 |
| release_2025_03_27/automation_vs_augmentation_v2.csv | 198 | c56f5ec709d61984a59106a08be9b2d70f460ff5 | Aggregate mode shares, v2 |
| release_2025_03_27/onet_task_statements.csv | 3592256 | f156004fb29dda092b86d374cf839e901fbdffd8 | O*NET task statement to O*NET-SOC occupation mapping (the join key from task files to occupations) |
| release_2025_03_27/SOC_Structure.csv | 77176 | 07249b132a59e684f84b3ce9b012fa0107631256 | SOC hierarchy (major/minor/broad/detailed) |
| release_2025_03_27/README.md | 3205 | e9a7295d89a4646fb6453da04becb5ac7cfb2d52 | v2 release documentation |
| README.md | 4396 | c75b9b35130b3dc1e69fcc4bfbe6b6f00d3fc550 | Top-level dataset card: release index, license statement, citations |

## Selection rationale
- The brief: latest occupation-level usage plus automation/augmentation, not giant raw transcript-derived files.
- Newer releases (2025_09_15, 2026_01_15, 2026_03_24) publish only large raw facet extracts (7 MB to 103 MB aei_raw files keyed to geography x task x facet) plus reports; they contain no small occupation-level summary files. The occupation-level automation vs augmentation story lives in: (a) labor_market_impacts/job_exposure.csv, occupation-level, newest; and (b) the 2025_03_27 v2 task-level files, which aggregate to occupations through onet_task_statements.csv.
- HF_TOKEN: not required, the dataset is public and ungated (script will use one if present in keys.env).

## Structure verification
To be appended by the fetch script after download (sha256, row counts, columns per file).
