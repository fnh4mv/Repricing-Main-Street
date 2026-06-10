# Pre-Registration: Service Category Asking-Price Multiples, 2019-2026

**Working title (bland, for embargo):** Small business asking-price multiples by service category, 2019-2026: a descriptive study
**Author:** William Sheets, University of Virginia
**Status:** DRAFT v1 for author signature. Becomes FROZEN on OSF registration (embargoed until publication).
**Rule:** This document is written before any business-listing pricing data is collected or viewed, including feasibility samples. After registration, the specification does not move. Any unavoidable deviation will be disclosed in the paper with a dated amendment note.

---

## 1. Research question and prior

**RQ1 (engine):** Which small-business service categories carry the highest measurable AI exposure, given their occupational staffing mix?

**RQ2 (pricing, the core test):** Have asking-price multiples for AI-exposed service categories diverged from AI-insulated skilled-trade categories since November 2022 (the release of ChatGPT)?

**Stated prior:** No. I expect no detectable divergence. The market is not yet pricing AI exposure on Main Street.

**Claim discipline:** All claims are descriptive. The strongest sentence this study will defend is: "prices don't yet reflect measurable AI exposure." No causal language. No difference-in-differences identification claims; the design is a descriptive differential trend with uncertainty bands.

**Three pre-committed result framings (one will be used, decided by the data):**
1. **Discount found:** exposed-basket multiples have declined relative to insulated; reported as the first quantified AI repricing on Main Street, with magnitude and uncertainty.
2. **No detectable divergence:** reported as "no detectable discount at a sensitivity of X turns of SDE" where X is the computed minimum detectable effect (Section 7). Never reported as proof the market is efficient.
3. **Premium found:** exposed-basket multiples have risen relative to insulated; reported as buyers potentially paying up for automatable cost bases, a distinct and publishable finding.

## 2. Data sources (pinned)

| Source | Vintage / pin | Role |
|---|---|---|
| BLS OEWS national industry staffing | May 2025 release (oesm25in4.zip, sha256 3ef0e42f...) | Occupation employment shares by NAICS |
| Eloundou et al., GPTs are GPTs (occ_level.csv) | repo commit 0471612 | PRIMARY exposure score ("could") |
| Anthropic Economic Index job_exposure.csv + automation/augmentation | revision db51ecb | Second tier ("is": observed usage) |
| Felten AIOE Appendix A | repo commit adca5fc | Sensitivity measure |
| Census ABS 2023 CBO owner age (O09/OWNRAGE) | 2023, NAICS2022 sectors | Succession CONTEXT ONLY (Section 8) |
| Census BDS firm age | 2023, 4-digit NAICS | Succession context complement |
| BizBuySell public listing pages | current cross-section + Wayback Machine historical snapshots, 2019-2026 | Asking prices and seller-reported cash flow (PRIMARY pricing) |
| BizBuySell Insight Reports | quarterly back-issues | Corroboration (coarse sector sold medians) |
| IBBA Market Pulse | quarterly back-issues | Corroboration (size-band sold multiples; size-mix context) |

Closed-transaction data (DealStats, BIZCOMPS, or equivalent), if access is granted or purchased later, will be used as CORROBORATION of the frozen asking-multiple analysis, not as a replacement specification.

## 3. Appendix A: category definitions (frozen)

A listing is assigned to a category if its BizBuySell category label matches, or failing a usable category label, its title or description matches the inclusion keywords. Exclusion: franchises-resale aggregator pages, real-estate-only sales, and asset-only auctions.

**EXPOSED basket (5):**

| Category | Listing keywords (include) | Engine NAICS | Scorable level |
|---|---|---|---|
| Bookkeeping and tax practices | bookkeeping, tax practice, tax preparation, accounting practice, payroll service | 541200 | 4-digit |
| Marketing and advertising agencies | marketing agency, advertising agency, digital marketing, PR firm, content agency, SEO | 541800 | 4-digit |
| Call centers and answering services | call center, answering service, telemarketing | 561400 | 4-digit (pooled, see note) |
| Transcription and document preparation | transcription, medical transcription, court reporting, document preparation | 561400 | 4-digit (pooled, see note) |
| Legal support services | paralegal, legal document, title abstract, process serving, legal services (non-attorney where identifiable) | 541100 | 4-digit (caveat: industry mix includes attorneys; disclosed) |

**INSULATED basket (5):**

| Category | Listing keywords (include) | Engine NAICS | Scorable level |
|---|---|---|---|
| HVAC | HVAC, heating and air, air conditioning | 238220 | 5-digit (shared with plumbing, see note) |
| Plumbing | plumbing, plumber | 238220 | 5-digit (shared with HVAC) |
| Electrical contractors | electrical contractor, electrician | 238210 | 5-digit |
| Landscaping | landscaping, lawn care, landscape maintenance | 561730 | 6-digit |
| Auto repair | auto repair, automotive repair, transmission, brake, collision | 811100 | 4-digit |

**BENCHMARK (excluded from the exposed basket, own exhibit):** Travel agencies (travel agency, tour operator; NAICS 561500). Pre-AI secular decline makes it a contaminated treatment member; it is presented as "the fully disrupted benchmark," the path a category takes after technological disintermediation. Robustness #1 re-runs the headline with travel agencies included.

**Pooling notes (disclosed in the paper):** OEWS May 2025 publishes no 5-digit detail for 5614 or 5615 and no sub-4-digit detail for 5412, 5418, 5411. Consequences: call centers and transcription share one engine exposure score (561400); HVAC and plumbing share one (238220). Pricing categories remain separate throughout. The shared scores bias AGAINST finding within-pair exposure differences and do not affect the basket-level contrast.

## 4. Exposure engine (frozen)

For industry i with occupations o:
**E_i = Σ_o w_(o,i) × x_o**, where w_(o,i) = occupation o's share of industry i employment among scored occupations (OEWS May 2025, TOT_EMP, national), and x_o = the occupation exposure score.

- **Primary x_o: Eloundou human_rating_beta** (human annotations, beta = E1 + 0.5 × E2). Chosen over the GPT-4-rated variant to avoid any "the model scored itself" critique in an AI-assisted paper; the GPT-4 variant (dv_rating_beta) is reported as an agreement check.
- **Tier 2 ("is"): AEI observed exposure** (job_exposure.csv, observed_exposure by SOC 2018) and the automation versus augmentation split, presented alongside the primary in one combined exhibit.
- **Sensitivity: Felten AIOE** (Appendix A scores).
- **SOC harmonization:** Eloundou O*NET-SOC 2019 specialty codes (suffix other than .00) collapse to their 6-digit SOC parent by unweighted mean. OEWS May 2025 and AEI use SOC 2018 6-digit natively. Felten SOC 2010 maps via the BLS 2010-to-2018 crosswalk (sensitivity only).
- **Coverage rule:** occupations lacking a score are excluded and weights renormalized; each reported industry must have scored occupations covering ≥80% of its employment, else it is flagged in the exhibit.
- **"Has" tier:** maximum three sourced narrative vignettes in the paper; never scored, never plotted as data.

**Gate-1 sanity prediction (falsifiable now):** E(541200 bookkeeping) and E(541800 marketing) each exceed E(238220 plumbing/HVAC) and E(561730 landscaping) under the primary measure. If not, the engine has a construction error; fix before anything else proceeds, and disclose the fix.

## 5. Pricing data and multiple construction (frozen)

- **Unit:** a listing observation = (category, snapshot date, asking price, seller-reported cash flow/SDE where disclosed, gross revenue where disclosed, location, listing id where extractable).
- **Asking multiple = asking price ÷ seller-reported cash flow (SDE).**
- **Inclusion:** asking price ≥ $20,000; SDE ≥ $10,000; multiple within [0.25, 15]. Listings flagged as including real estate are excluded from multiple computation when the flag is detectable.
- **Missing SDE:** listing is excluded from multiples but counted in the disclosure-rate exhibit (Section 6 robustness c).
- **Aggregation:** median multiple per basket per period is primary. Category-level medians shown only where cell n ≥ 25.
- **Period rule:** quarterly if the median basket-quarter cell has n ≥ 40 across the historical series; otherwise semiannual. This feasibility parameter is set by counting observations BEFORE any multiples are computed, and the chosen periodization is reported.
- **Historical source:** Wayback Machine snapshots of BizBuySell public category pages, 2019 to present, plus one current-day cross-section. If Wayback yield is insufficient for a pre-2022 baseline (fewer than 2 usable cross-sections per year in 2019-2021), the quarterly broker PDF series (BizBuySell Insight, IBBA Market Pulse) becomes the primary time dimension and the listing data becomes the 2026 cross-sectional anchor; this fallback is pre-committed here.

## 6. The test and robustness (frozen)

- **Headline statistic:** gap_t = median exposed-basket multiple minus median insulated-basket multiple, per period.
- **Comparison:** mean gap in the pre period (2019Q1 through 2022Q4) versus the post-period trajectory (2023Q1 onward), shown as a differential-trend plot with bootstrap confidence bands (resampling listings within category-period, 1,000 replications).
- **Descriptive support:** a permutation check shuffling category-to-basket assignment; reported as descriptive support, not causal inference.
- **Robustness floor (all pre-committed):** (a) drop-one-category jackknife on both baskets; (b) travel agencies in versus out; (c) SDE-disclosure-rate stability by category-period, presented as a first-class exhibit (selection check); (d) agreement table across exposure measures (primary, GPT-4 variant, Felten, AEI).

## 7. Minimum detectable effect (frozen method)

Before interpreting any null, simulate: at the achieved cell sizes and observed within-cell dispersion, the smallest post-period gap change detectable at 80% power with two-sided alpha 0.05. The MDE in turns of SDE is printed in the limitations section, and framing 2 (Section 1) is stated relative to it.

## 8. Succession overlay (frozen demotion)

ABS 2023 owner-age data exist only at 2-digit NAICS sector level. Both baskets draw from sectors 54, 56, 23, 81, so sector-level owner age CANNOT resolve category-level contrasts. Commitment: succession data appear in ONE context exhibit motivating the succession wave, labeled "sector level, not category-resolving." Zero cross-basket succession claims. BDS firm age (4-digit) may appear as a context complement, clearly labeled firm age, not owner age.

## 9. Collection ethics and publication boundaries

Listing data are collected from publicly accessible pages at low frequency on personal hardware, respecting robots.txt, described in the methods as archival snapshots of publicly accessible listings. Published outputs contain ONLY aggregated category-period statistics, code for the engine, and government data. No listing-level records, no scraper code, no firm (eGateway) data or tools-derived numbers anywhere in the paper.

## 10. Not frozen

Prose, exhibit design and styling, the order of sections, the title of the published paper, vignette selection for the "has" tier, and any post-hoc EXPLORATORY analyses, which will be labeled exploratory if shown.

---

**Signature (Gate 1 of the authorship contract):**

I have read this specification, edited what needed editing, and I sign it as the frozen design of the study.

Signed: __William Sheets_________  Date: ___06/10/2026
William Sheets
