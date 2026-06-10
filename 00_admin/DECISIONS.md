# DECISIONS.md - Locked Decision Log

Sources: [WS] = William's intake answers (2026-06-09) · [PT] = pressure-test resolution · [CC] = Claude call on items William delegated.
Reversing a [1WD] decision requires an explicit entry here with reasoning.

## Authorship, venue, AI story

- **D-01 [WS][1WD] Sole human author.** William Sheets, sole byline. Claude gets a prominent named "How this paper was built" methods appendix and colophon. No AI co-author byline (SSRN bars it; recruiting risk).
- **D-02 [WS] "Published" = staged.** Self-published PDF on williamsheets.com + SSRN posting in launch week. A 1,500-2,500 word derivative essay pitched to outlets after launch. No peer-reviewed journal this cycle.
- **D-03 [WS] AI-production appendix is live from session 1.** Every session logged to `00_admin/SESSION_LOG/`. The appendix is built from real logs, not reconstruction. Started 2026-06-09.
- **D-04 [WS] "New style of paper" stays modest:** voice + the instrumented AI-production appendix. No interactive web-native exhibits in v1 (website hosts the PDF and Exhibit 1 image; interactive map is v2).

## Evidence and money

- **D-05 [PT] Headline evidence = asking multiples,** framed as "the seller's first claim," from BizBuySell current cross-section + Wayback historical snapshots. Corroboration spine = free quarterly broker PDFs (BizBuySell Insight sector medians + IBBA Market Pulse size bands). The frozen hypothesis is written on asking multiples so the paper cannot fail by data class.
- **D-06 [PT] DealStats $365 day pass is GATED, not default.** Decision point Jul 6 (W5). Buy only if: UVA access confirmed dead AND draft result is publishable-but-fragile such that sold-multiple corroboration upgrades its class. Personal card only, never expensed to eGateway. This exceeds William's $100 default budget and needs his explicit OK at the gate.
- **D-07 [WS→PT] Fallback order re-ranked:** (1) broker PDFs as primary series, (2) DealStats purchase at gate, (3) forward panel as garnish. (William's original order was buy-first; re-ranked because $365 > $100 budget and the freeze anchors on asking multiples.)
- **D-08 [Verified] UVA library: DealStats/BIZCOMPS/PeerComps/PrivCo NOT in catalogs.** Available to William: IBISWorld, Statista, Mergent Intellect, Business Source Complete, First Research. CapIQ/PitchBook/Preqin are Darden-gated. William runs the 10-minute NetBadge check + librarian email to confirm (see PROJECT_STATE next actions).
- **D-09 [WS] Forward panel starts W1.** Weekly snapshots of public BizBuySell category search pages. Low frequency, robots.txt respected, personal hardware and accounts only. By launch: ~7 waves = one forward-looking sentence + v2 seed, never headline evidence.
- **D-10 [PT][1WD] Four bright lines on data and the firm:** (1) No firm-licensed data touches the paper, even directionally. (2) UVA is primary affiliation; eGateway appears in a disclosure line only ("views are the author's alone; no firm data or resources used"); Chad clears the final PDF. (3) Headline result has zero live-scrape dependency (current cross-section + Wayback + PDFs). (4) Public repo ships category-week aggregates only; listing-level records and scraper code stay private permanently. Methods language: "weekly archival snapshots of publicly accessible listings."

## Method

- **D-11 [WS] Claims are descriptive only.** Strongest sentence: "prices don't yet reflect measurable AI exposure." No causal coefficients, no "difference-in-differences" headline language; "differential trend" with an event-study style plot and CIs.
- **D-12 [WS][1WD] Pre-registration freeze BEFORE any pricing data is touched** (including the toy slice). Mechanism: OSF registration WITH EMBARGO (timestamped immediately, contents private, auto-public at launch; bland working title). Resolves freeze-vs-private-repo tension. GitHub repo stays private; curated public repo at launch.
- **D-13 [PT→WS LOCKED 2026-06-09: "good call. lock it."] Travel agencies OUT of the headline exposed basket.** Promoted to its own exhibit: "the fully disrupted benchmark," the multiple path of a category the internet already killed, i.e. what the exposed basket should look like later if the thesis is right. Travel-in is pre-registered robustness #1. Rationale: 25-year OTA secular decline contaminates the treatment group; "kid stacked his AI basket with an already-dying industry" is the exact age-dismissal William fears. He gets MORE use of the vivid example, not less.
- **D-14 [PT] Headline exposed basket (5):** bookkeeping/tax prep, marketing/content agencies, call centers, transcription, paralegal services. **Insulated basket (5):** HVAC, plumbing, electrical, landscaping, auto repair. Final NAICS mapping table is Appendix A of the freeze.
- **D-15 [WS→CC] Exposure tiers = "could / is / has":** Eloundou (could, PRIMARY score), Anthropic AEI automation share (is, second scored tier), Felten AIOE (sensitivity column). "Has" = max 3 sourced vignettes on one page, narrative only. All tiers in ONE combined exhibit, never a parallel analysis.
- **D-16 [PT] Succession overlay DEMOTED to one context exhibit,** labeled "2-digit sector level, not category-resolving." Zero cross-basket succession claims (NAICS 56 contains call centers AND landscaping; 54 contains bookkeeping AND nothing insulated: any finer claim is a category error). First exhibit cut if pages run long. BDS firm-age checked as cheap complement during W1, not load-bearing.
- **D-17 [CC] Robustness floor (3):** drop-one-category jackknife, travel-in/travel-out, SDE-disclosure-rate stability by category-quarter (selection-bias check, shown as a first-class exhibit). Stretch if hours allow: deal-size mix check. Event-study style trend plot is part of the main spec, not robustness.
- **D-18 [PT] Min-cell rule:** basket-level quarterly medians are primary; category-level shown only where n≥25. Frozen in prereg.
- **D-19 [WS] MDE transparency:** compute and state the minimum detectable gap; a null prints as "no detectable discount at X sensitivity," never as proof of efficiency. All three result branches (discount / null / premium) have pre-written framings; premium = "buyers may be paying up for automatable cost bases," a publishable nuance branch.
- **D-20 [PT] Toy slice = feasibility counts only** (SDE disclosure rates, n per category, field availability). No multiples computed before the freeze is registered.

## Build and infrastructure

- **D-21 [WS] Engine is static for v1.** Live map/dashboard = v2, post-SSRN.
- **D-22 [WS] GitHub repo PRIVATE during build.** Curated public repo + aggregates at launch. Supabase project (already set up by William) mirrors the forward panel; flat files in this folder remain canonical for analysis.
- **D-23 [CC] Reproducibility bar = "regenerable by us":** deterministic scripts, dated immutable raw pulls with manifest, one command per exhibit. Not pinned-environment public one-command rebuild.
- **D-24 [WS] Engine/fast-follow infrastructure may take up to ~30% of build effort** if seriously referenceable. Fast-follows (The Audit, The Unmarked Risk) stay OUT of v1 scope.
- **D-25 [CC] Models policy:** Fable 5 for research, methodology, analysis code, and all paper prose. Cheaper models (Sonnet/Haiku) only for bulk mechanical extraction (PDF table transcription, listing parsing) with Fable 5 verification passes.

## William's non-delegable gates (the authorship contract)

- **D-26 [PT] Six gates William personally executes** (~8-10 of his ~25 total hours): (1) edit and sign the freeze doc; (2) hand-audit a random 20-listing sample against source ("I personally verified a random sample of 20 listings" goes in print); (3) write first drafts of abstract, intro, conclusion (AI edits after, never the reverse); (4) re-run the headline notebook end to end and perturb one assumption; (5) one-line takeaway on every exhibit before captions are polished; (6) 30-minute oral exam against 15 hostile interviewer questions before SSRN goes live.

## Distribution

- **D-27 [WS] eGateway:** byline affiliation acceptable for now; Chad clears the near-final PDF at W6 with a 5-business-day ask; independence fallback ready (paper stands alone without affiliation). Firm tools usable for orientation only, never for published data (D-10).
- **D-28 [WS→PT] Feed silence until SSRN is live.** Then a 3-post launch week: Day 0 announcement, Day 2 the one killer exhibit, Day 5 the "how I built this with AI" post. Transparent in artifact, silent in feed. No teaser posts (William: "keep it under wraps for now").
- **D-29 [WS] Cut order when schedule slips:** 1-pager dies first, then AEI "is" exhibit shrinks to a paragraph, then SMEs 5→2, then category-level exhibits go basket-level only. Never cut: gates, freeze, oral exam, Chad clearance.
- **D-30 [WS] Pre-readers:** one valuation professional/business broker recruited by ~W2 with a save-the-date for ~Jul 13; 3-5 SMEs after draft v1; reviews on a 7-day hard window ("proceed with whoever replies").
- **D-31 [WS] Voice:** all published prose follows 00_admin/VOICE.md. No em dashes anywhere, ever.

## Infrastructure (session 02, 2026-06-09)

- **D-32 [CC] Git:** repo root = this folder, private GitHub `fnh4mv/Repricing-Main-Street-`, branch `main`, commits authored as William (fnh4mv@virginia.edu). Gitignored forever: `.env`, raw data bulk, PDFs. Curated public repo at launch stays a separate artifact (D-22).
- **D-33 [CC, enforces D-10] Supabase separation:** the connected Supabase account only exposes firm projects (egos-dev, eGOS Backend). Both are OFF-LIMITS for this paper. The forward panel lives on a personal-org Supabase project whose URL + keys live in `.env` only. Verify the project ref in `.env` is not a firm ref before first write.
- **D-34 [WS] Panel runner = William's Mac** (launchd, Sunday evenings; "I can make it so"). n8n is the fallback if the Mac proves unreliable by W3.
