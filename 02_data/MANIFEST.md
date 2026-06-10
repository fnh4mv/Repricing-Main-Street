# 02_data/MANIFEST.md - Data Manifest

Rules (CLAUDE.md hard rule 6): `raw/` is immutable. Every pull = dated subfolder `raw/YYYY-MM-DD_<source>/` + one entry here. `processed/` is regenerable from raw + scripts; anything in processed/ that can't be regenerated is a bug.

| Date | Path | Source (URL) | What | Pulled by | Notes |
|------|------|--------------|------|-----------|-------|
| 2026-06-10 | raw/2026-06-10_eloundou/ | https://github.com/openai/GPTs-are-GPTs | Eloundou et al. "GPTs are GPTs" occupation-level exposure scores (occ_level.csv, 923 occupations, GPT-4 + human alpha/beta/gamma) | Claude (DATA-1 agent) | git clone at commit 0471612, blob-verified; MIT license; O*NET-SOC 2019 codes; see PROVENANCE.md |
| 2026-06-10 | raw/2026-06-10_felten_aioe/ | https://github.com/AIOE-Data/AIOE | Felten-Raj-Seamans AIOE data appendix (Appendix A: 774 occupations, SOC 2010) plus Language Modeling and Image Generation AIOE variants | Claude (DATA-1 agent) | git clone at commit adca5fc, blob-verified; no license file, citation requested (SMJ 2021), do not redistribute files; see PROVENANCE.md |
| 2026-06-10 | raw/2026-06-10_anthropic_aei/ | https://huggingface.co/datasets/Anthropic/EconomicIndex | Anthropic Economic Index: occupation-level job_exposure.csv plus v2 task-level usage and automation/augmentation files (11 files, pinned to revision db51ecb) | Claude (DATA-1 agent) | SCRIPT PENDING: sandbox proxy blocks huggingface.co; run 03_engine/scripts/fetch_anthropic_aei.py on the Mac; data CC-BY, code MIT; see PROVENANCE.md |
| 2026-06-10 | raw/2026-06-10_oews/ | https://www.bls.gov/oes/special-requests/oesm25in4.zip | BLS OEWS May 2025 national industry-specific estimates: occupation employment by NAICS at sector/3/4/5-digit levels plus ownership, full XLSX zip + extract (engine backbone) | Claude (DATA-2 agent) | SCRIPT PENDING: sandbox proxy blocks bls.gov; run 03_engine/scripts/fetch_oews.py on the Mac; May 2025 is newest vintage (verified on tables.htm); public domain; see PROVENANCE.md |
| 2026-06-10 | raw/2026-06-10_abs_ownerage/ | https://api.census.gov/data/2023/abscbo | Census ABS 2023 Characteristics of Business Owners: owner age question by NAICS sector, US level, owner counts + percent shares, raw JSON + flattened CSV (succession context) | Claude (DATA-2 agent) | SCRIPT PENDING: sandbox proxy blocks api.census.gov and API now requires key; run 03_engine/scripts/fetch_abs_ownerage.py on the Mac; 2023 is newest vintage (no 2024 endpoint); sector level only; CC0; see PROVENANCE.md |
| 2026-06-10 | raw/2026-06-10_bds_firmage/ | https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_vcn4_fa.csv | Census BDS 2023 two-way table, firm age by 4-digit NAICS, 1978-2023 CSV (succession complement check) | Claude (DATA-2 agent) | SCRIPT PENDING: sandbox proxy blocks www2.census.gov; run 03_engine/scripts/fetch_bds_firmage.py on the Mac; BDS 2023 is newest vintage; public domain; see PROVENANCE.md |

## Planned raw/ structure

```
raw/
├── YYYY-MM-DD_oews/          (BLS industry staffing matrices)
├── YYYY-MM-DD_eloundou/      (exposure scores)
├── YYYY-MM-DD_felten_aioe/
├── YYYY-MM-DD_anthropic_aei/
├── YYYY-MM-DD_abs_ownerage/
├── YYYY-MM-DD_bds_firmage/
├── broker_pdfs/              (Insight + Market Pulse back-issues, with page-cited CSV transcriptions)
├── wayback/                  (historical BizBuySell cross-sections, dated)
├── panel/                    (weekly forward-panel waves, dated)
└── crosssection/             (current BizBuySell pulls, dated)
```
