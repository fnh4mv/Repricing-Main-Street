# 02_data/MANIFEST.md — Data Manifest

Rules (CLAUDE.md hard rule 6): `raw/` is immutable. Every pull = dated subfolder `raw/YYYY-MM-DD_<source>/` + one entry here. `processed/` is regenerable from raw + scripts; anything in processed/ that can't be regenerated is a bug.

| Date | Path | Source (URL) | What | Pulled by | Notes |
|------|------|--------------|------|-----------|-------|
| — | — | — | (no pulls yet; freeze precedes pricing per D-12; engine pulls land W1) | — | — |

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
