# MASTER PLAN - Repricing Main Street

**Paper:** Repricing Main Street: AI Exposure, the Succession Wave, and What Buyers Aren't Pricing
**Author:** William Sheets (University of Virginia), built with Claude (disclosed, instrumented)
**Target:** SSRN live + website + LinkedIn launch by Aug 2, 2026 (hard stop: before IB apps open in August)
**Status home:** PROJECT_STATE.md · Decisions: DECISIONS.md · Voice: VOICE.md
**Plan version:** 1.0, locked 2026-06-09

---

## 0. One screen

The bet: buyers in the ~$5T boomer succession wave are paying the same multiples for businesses that sell typing (bookkeeping, agencies, call centers) as for businesses that sell hands (HVAC, plumbing), and nobody has checked. We check.

Two layers of evidence. Layer 1, the engine: score every Main Street category for AI exposure (BLS staffing mix × occupational exposure scores) and overlay succession pressure. Layer 2, pricing: asking multiples from BizBuySell (current + Wayback history) corroborated by free quarterly broker series, exposed basket vs. insulated basket, trends since Nov 2022.

The claim is descriptive: "prices don't yet reflect measurable AI exposure." All three results publish: discount found (first quantified AI discount on Main Street), no discount (documented market blind spot, MDE-framed), premium (buyers paying up for automatable cost bases, the nuance branch).

William's ~25 total hours go to six authorship gates (D-26). The machine does everything else. Every session ships something and logs itself for the AI-production appendix.

---

## 1. Workstreams

- **WS-A Engine** (exposure scores × succession overlay → Exhibit 1)
- **WS-B Pricing evidence** (cross-section, Wayback, broker PDFs, forward panel)
- **WS-C Analysis** (frozen spec → exhibits → robustness)
- **WS-D Paper** (outline → drafts → review → final PDF)
- **WS-E Production system** (repo, logging, agents, n8n/Supabase, provenance appendix)
- **WS-F Distribution** (SSRN, website, LinkedIn sequence, derivative pitches, Chad clearance)

Dependencies: A and B run parallel from W1. C needs the freeze (end W1) + B yield (end W3). D outline starts W1, drafting starts W3 alongside data. E starts now. F mechanics start W5.

---

## 2. Week-by-week (June 9 → August 2, buffer to Aug 7)

### W1 · Jun 9-14 - Freeze + first collection
- Pull OEWS national industry staffing (3/4-digit NAICS), Eloundou scores, Felten AIOE, Anthropic AEI, ABS owner-age (2-digit), BDS firm-age (complement check). All into `02_data/raw/` with manifest entries.
- Draft freeze doc: basket NAICS mapping table (Appendix A), primary measure, main spec, min-cell rule, robustness set, MDE method, three result framings. **William gate 1: edit + sign.**
- Register on OSF with embargo, bland working title. THEN toy slice (counts only, D-20).
- **Forward panel wave 1 collected this week** (calendar-bound; lost weeks are unrecoverable). Runner decision with William: launchd on his Mac (preferred, residential IP, Sunday 9pm) or n8n instance. Script provided to him to run.
- Wayback CDX audit of BizBuySell coverage (script for William's machine or Claude-in-Chrome; archive.org is blocked from the sandbox).
- William: UVA 10-minute library check + librarian email; SSRN account created NOW (new unaffiliated accounts screen slower); Chad heads-up conversation (not clearance, just awareness).
- **GATE 0 (end W1): freeze registered, panel running, Wayback yield known.**

### W2 · Jun 15-21 - Engine v1
- Build per-NAICS exposure scores: Σ(occupation share × exposure). Eloundou primary, AEI second tier, Felten sensitivity column. Swappable weights file.
- **GATE 1: sanity ranking.** Bookkeeping/tax prep must outscore plumbing/HVAC by a wide margin; if the ranking looks wrong, stop and fix the crosswalk before anything else. This is the derisk moment for the whole engine.
- Exhibit 1 draft (exposure × succession context map, "death in escrow" quadrant).
- Recruit the valuation-professional pre-reader with a save-the-date for ~Jul 13 (their latency is slip source #2).
- Paper outline v1 + intro first draft (William writes, machine edits after, per gate 3).

### W3 · Jun 22-28 - Pricing assembly (THE LONG POLE)
- Current BizBuySell cross-section across the 10 basket categories + Wayback historical cross-sections + transcribe all broker PDF back-issues (BizBuySell Insight quarterly sector tables, IBBA Market Pulse) to CSV with page cites.
- **GATE 2: the n table.** Listings per category per period, SDE disclosure rates. If Wayback is thin: broker PDFs become the primary time series, pre-decided, no deliberation (D-07).
- Exhibit skeletons for whatever the data supports (basket medians by period, disclosure-rate exhibit).

### W4 · Jun 29-Jul 5 - Analysis per freeze
- Run the frozen spec. Compute MDE. Build exhibits v1: trend plot with CIs, basket gap, travel benchmark exhibit, robustness set.
- **GATE 3: result class declared** (discount / null-at-MDE / premium). Drop in the pre-written framing. **William gate 5: one-line takeaway per exhibit.**

### W5 · Jul 6-12 - William's writing block
- **DealStats gate:** buy the $365 day pass only if UVA is dead AND the result is publishable-but-fragile (D-06). His call, his card.
- **William gates 2, 3, 4:** 20-listing hand audit; abstract/intro/conclusion first drafts; re-run headline notebook + perturb one assumption. This is his unmovable 8-10 hour block. Protect it.
- Machine drafts all middle sections around his drafts, in VOICE.md voice.

### W6 · Jul 13-19 - Review round
- Draft v1 to valuation pre-reader + SMEs, 7-day hard window, proceed with whoever replies.
- **Chad gets the near-final NOW** with a 5-business-day ask (not W7; his latency is slip source #1).
- Provenance appendix assembled from session logs.

### W7 · Jul 20-26 - Final + submit
- Revisions from reviews. Final PDF (typeset clean, exhibits final).
- **William gate 6: oral exam.** 15 hostile interviewer questions, answered cold; misses studied before going live.
- **SSRN submission Jul 24-27** (screening 2-5 business days, longer possible for new accounts; submit early in the week).
- Stage website page + LinkedIn posts + curated public repo.

### W8 · Jul 27-Aug 2 - Launch
- SSRN live → 3-post launch week (D-28): Day 0 announce, Day 2 killer exhibit, Day 5 "how I built this with AI."
- Curated public repo + aggregates live. OSF embargo lifts.
- Buffer to Aug 7. Then W9+: derivative essay pitched to 2-3 outlets (The Diff / Net Interest tier, Axial Middle Market Review).

**Slip rule:** cut order is D-29 (1-pager already dead). Gates, freeze, oral exam, and Chad clearance never get cut. If two full weeks slip, launch moves into the Aug 3-7 buffer and the derivative essay moves to September. Hard floor: live before apps open.

---

## 3. Evidence architecture

### 3.1 The engine (WS-A)
- **Inputs:** OEWS national industry×occupation staffing matrices (3/4-digit NAICS); Eloundou et al. task-exposure scores (could); Anthropic Economic Index automation/augmentation shares by SOC (is); Felten AIOE (sensitivity); ABS owner-age by 2-digit sector (context only, D-16); BDS firm-age (complement check).
- **Computation:** per-NAICS exposure = Σ(occupation employment share × occupation exposure). One swappable weights file per measure. Crosswalk SOC↔NAICS via OEWS directly; crosswalk NAICS↔BizBuySell listing categories is hand-built, frozen as Appendix A, and William-audited.
- **Outputs:** category scorecard (all scored NAICS), Exhibit 1 map, basket scores. Reusable for fast-follows (engine code stays paper-agnostic: score any NAICS list against any occupation-level measure).

### 3.2 Pricing (WS-B)
- **Primary:** asking multiples (asking price ÷ seller-reported SDE/cash flow), BizBuySell current cross-section + Wayback historical snapshots. Framed as "the seller's first claim."
- **Corroboration spine ($0):** BizBuySell Insight quarterly sector medians + IBBA Market Pulse size-band sold multiples, hand-transcribed once with page cites.
- **Gated upgrade:** DealStats day pass (D-06), decision Jul 6.
- **Forward panel:** weekly public-page snapshots → Supabase + dated CSVs. Garnish and v2 seed only.
- **Collection rules (D-10):** personal hardware/accounts, low frequency, robots.txt respected, no firm IPs, aggregates only in anything public, scraper code private forever. Methods language: "weekly archival snapshots of publicly accessible listings."

### 3.3 Analysis (WS-C)
Frozen before any pricing pull (D-12). Basket-level quarterly medians primary; category-level only at n≥25 (D-18). Trend plot with CIs pre/post Nov 2022 ("differential trend," not DiD). MDE computed and printed (D-19). Robustness: drop-one jackknife, travel-in/out, disclosure-rate stability (D-17). Three result framings pre-written (Gate 3 just picks one).

---

## 4. Production system (WS-E)

### 4.1 Where things live
- **This folder = the brain.** Canonical for all data, code, drafts, state. Map in CLAUDE.md.
- **GitHub (private):** mirrors `03_engine/` + `04_analysis/`. Curated public repo at launch only.
- **Supabase (William's project instance):** forward-panel tables + a mirror of session logs if useful. Never canonical; flat files win conflicts.
- **n8n (William's instance, in progress):** only genuinely recurring jobs. Candidates: weekly panel snapshot (if Mac launchd loses), quarterly report watcher (v2). Nothing else; one-shot scripts beat workflows for one-shot work.
- **OSF:** embargoed pre-registration. **Zenodo at launch:** DOI for the public dataset.

### 4.2 Model and agent policy
- **Fable 5 (this model): default for everything that thinks.** Research, methodology, crosswalk design, analysis code, all paper prose, all verification passes.
- **Sonnet/Haiku subagents:** bulk mechanical work only (PDF table transcription, listing-page parsing, citation formatting), always followed by a Fable 5 verification pass on a sample.
- **Fan-out pattern:** independent research/collection tasks run as parallel subagents (as done for the lens round). Serial judgment (basket calls, claims language, exhibit takeaways) never fans out.
- **Verification discipline:** every number that reaches a draft carries a source path (raw file + script + line). Every exhibit regenerable by one command. A wrong number in print is the project's only unrecoverable failure mode.

### 4.3 Provenance instrumentation (D-03)
Every working session appends `00_admin/SESSION_LOG/YYYY-MM-DD_session-NN.md`: date, what shipped, agents/models used, key decisions, William-hours vs machine-work. The "How this paper was built" appendix compiles from these logs. Honest accounting: it states what AI did (collection, drafting, code) and what William did (gates 1-6, judgment calls, final words).

---

## 5. Writing plan (WS-D)

Outline locked W2, drafted alongside data W3-W5, reviewed W6, final W7. Target 15-25 pages + appendices. Voice: VOICE.md, calibrated to "Building the Car." William first-drafts abstract/intro/conclusion (gate 3); machine drafts middle sections; William's one-liners drive every exhibit caption.

Working outline:
1. **The garage sale** (hook: succession wave meets AI, the Blockbuster-and-plumber framing, ELI15 kept)
2. **What buyers are buying** (Main Street market structure, SDE multiples explained plainly, who the buyers are)
3. **Scoring the typing** (the engine: method, Exhibit 1 map, death-in-escrow quadrant, tiers could/is/has)
4. **The benchmark that already died** (travel agencies exhibit: what full disruption looks like in multiples)
5. **What prices say** (the test: baskets, trends, the gap or its absence, MDE stated plainly)
6. **What would have to be true** (interpretation branches, what buyers may know that the scores don't, premium nuance if found)
7. **What I can't claim** (limitations in William's honest-gap voice: asking vs sold, selection, small n, category noise)
8. **What happens next** (succession math forward, what a repricing would look like, one forward-panel sentence)
9. **Appendices:** A method/crosswalk + freeze record · B robustness · C data dictionary + aggregates pointer · D how this paper was built (the AI appendix)

---

## 6. Distribution (WS-F)

- **Launch stack:** SSRN (DOI, UVA affiliation) + williamsheets.com paper page + LinkedIn sequence + curated public repo. Resume line and interview talk-track written in W8.
- **Feed silence until live** (D-28), then Day 0 / Day 2 / Day 5 posts. X account optional at launch for finance-twitter amplification; LinkedIn is primary.
- **Derivative essay** (1,500-2,500 words) pitched W9+ to 2-3 outlets. Exclusive on the finding tradeable for placement.
- **eGateway:** disclosure-line affiliation, Chad clearance W6, independence fallback ready (D-27).
- **Reviewers as first distribution wave:** valuation pro + SMEs get named thanks (with permission).

---

## 7. Budget

- Committed now: **$0.** (OSF, SSRN, GitHub, Wayback, all government data: free. Supabase/n8n: existing.)
- Possible: scraping-assist credits if collection needs them (~$30, inside the $100 default) · DealStats day pass **$365, gated, William's explicit OK at Jul 6** (D-06).
- Never: firm-expensed anything (D-10).

---

## 8. Risk register

| # | Risk | Trigger | Response |
|---|------|---------|----------|
| 1 | Wayback coverage thin | W1 CDX audit | Pre-decided: broker PDFs become primary series (D-07) |
| 2 | Exposed-category listings too sparse (n<25/quarter) | W3 n-table | Basket-level only (D-18); transcription/call-center cells merged or footnoted |
| 3 | Collection blocked (anti-bot) | W1-W3 | Browser-assisted manual pulls at low volume; scope shrinks before methods compromise |
| 4 | Chad requests changes/kill | W6 | Affiliation drops to none; paper ships independent (D-27). Heads-up in W1 prevents surprise |
| 5 | SSRN screening slow/rejected (new account) | W7-W8 | Account created W1; UVA affiliation; fallback: website + Zenodo DOI on time, SSRN follows |
| 6 | Scooped (someone ships the pricing test first) | any week | Differentiation = engine + freeze + forward panel; cite them, ship anyway; speed is the main defense |
| 7 | Reviewer latency | W6 | 7-day hard window, proceed with whoever replies (D-30) |
| 8 | William's W5 block collides with life | W5 | The block is the schedule's only immovable human dependency; if it slips, everything slips week-for-week. Calendar it now |
| 9 | A wrong number in print | always | Verification discipline (4.2); 20-listing audit; oral exam catches understanding gaps |
| 10 | Scope creep (interactive map, fast-follows, 50-agent theater) | any session | This file is the scope. New ideas go to PROJECT_STATE "parking lot" for v2 |

---

## 9. Fast-follow hooks (v2, NOT NOW)

Engine code stays category-agnostic and measure-agnostic so that: **The Audit** (AI roll-up margin claims vs hiring data) reuses the SOC-level exposure layer; **The Unmarked Risk** (LMM PE portfolio scoring) reuses the NAICS scorecard. The forward panel becomes a quarterly data note. The interactive map becomes the website artifact. None of this gets a minute before SSRN is live.

---

## 10. Session protocol (every future chat)

1. **Boot:** read CLAUDE.md, then PROJECT_STATE.md. (60 seconds of context, no re-asking.)
2. **Pick:** top item in NEXT ACTIONS queue unless William redirects.
3. **Ship:** end with working code, a completed pull, a validated join, or a drafted section. Never discussion alone.
4. **Log:** append session log entry; update PROJECT_STATE (status, queue, gates, parking lot).
5. **Flag:** anything needing William (a purchase, an account, a judgment call) goes in PROJECT_STATE under "WILLIAM'S QUEUE" with exactly what to do and why.

William's cadence: 2-4 hrs/week. Machine sessions can run long; his time is spent only on gates and queue items marked his.
