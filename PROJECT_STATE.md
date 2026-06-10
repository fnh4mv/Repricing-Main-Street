# PROJECT_STATE.md - Living State

**Last updated:** 2026-06-10 (Session 03, W1 collection + audit)
**Phase:** W1 in progress. Gate 0 due Jun 14.
**Launch target:** SSRN + site + LinkedIn live by Aug 2, 2026. Hard floor: before August apps.

## Status snapshot

- **GitHub live and synced:** private repo `fnh4mv/Repricing-Main-Street`, push working, all project docs committed. Provenance records tracked in git; raw data and env files excluded by design.
- **All keys in env (verified):** GitHub PAT, Supabase (personal project `piou...`, confirmed NOT a firm project per D-33), Anthropic, Census, BLS, OSF, HuggingFace, Zenodo.
- **Data: 2 of 6 landed, 4 await one command on William's Mac** (sandbox blocks .gov and huggingface.co; no workarounds used, per rules). Landed and blob-verified against official repos: **Eloundou** (923 occupations, MIT license) and **Felten AIOE** (774 occupations, no license: cite-only, never redistribute files). Script-pending with pinned integrity checks baked in: **OEWS May 2025** (newest vintage), **ABS 2023 owner-age** (sector-only, confirmed), **BDS 2023 firm-age** (4-digit NAICS exists), **Anthropic AEI** (pinned revision db51ecb, CC-BY).
- **Audit (2026-06-10, William-ordered) PASSED:** recomputed checksums match PROVENANCE exactly; row counts and columns verified; no hardcoded secrets in tracked files; official URLs only; MANIFEST accurate (6 rows). Fixed during audit: em dashes purged from 11 internal files (all in titles, all mine), gitignore now tracks PROVENANCE.md while excluding data, missing folders created (04_analysis, 05_paper, 06_distribution, 07_freeze, 02_data/processed), root README rewritten.
- **Methods fact for the freeze doc:** the three exposure measures use three SOC vintages (Eloundou O*NET-SOC 2019 with 149 specialty codes; Felten SOC 2010; AEI and OEWS SOC 2018). Harmonization rule must be specified in the freeze.
- **BVR/BIZCOMPS academic-access email drafted** (William's idea): `01_sources/OUTREACH_data_vendors.md`. Send from UVA address.
- UVA librarian inquiry out; Darden library reportedly pulling some data for William (details pending).
- Plan locked (MASTER_PLAN v1.0), decisions D-01..D-34, travel-agency call LOCKED (D-13).

## Gate status

| Gate | What | Status |
|------|------|--------|
| 0 | Freeze registered (OSF embargo) + panel wave 1 + Wayback yield known | OPEN, due Jun 14 |
| 1 | Engine sanity ranking (bookkeeping >> plumbing) | pending, due Jun 21 |
| 2 | Pricing n-table (n per category-quarter, SDE disclosure rates) | pending, due Jun 28 |
| 3 | Result class declared (discount / null-at-MDE / premium) | pending, due Jul 5 |
| DealStats | $365 buy decision (D-06; librarian/BVR replies may moot it) | pending, Jul 6 |

## WILLIAM'S QUEUE (in order)

1. **Run the four fetch scripts** (~2 min, ~60MB, stock python3). From the project folder in Terminal:
   `python3 03_engine/scripts/fetch_oews.py && python3 03_engine/scripts/fetch_abs_ownerage.py && python3 03_engine/scripts/fetch_bds_firmage.py && python3 03_engine/scripts/fetch_anthropic_aei.py`
   Each verifies its own checksums and updates its PROVENANCE.md. Tell me when done; I flip MANIFEST rows to LANDED and start the engine build.
2. **Send the BVR/BIZCOMPS email** from fnh4mv@virginia.edu: ready in `01_sources/OUTREACH_data_vendors.md`.
3. **Forward the librarian verdict** when it lands; paste any Darden data details into chat.
4. **Valuation pre-reader:** one name by ~Jun 21, Jul 13 save-the-date (D-30).
5. (Standing) Chad heads-up before W6; W5 writing block calendared Jul 6-12.

## NEXT ACTIONS (machine queue, in order)

1. **Freeze doc draft** → `07_freeze/FREEZE_v1_DRAFT.md`: basket NAICS mapping (Appendix A), SOC harmonization rule, primary measure spec, min-cell rule, robustness set, MDE method, three result framings. For William's gate-1 signature.
2. OSF registration walk-through (account exists, token in env; embargo settings, bland title).
3. Wayback CDX audit script (his Mac; archive.org blocked in sandbox).
4. Weekly panel snapshot script + launchd plist + Supabase DDL + SETUP_MAC.md. First wave must run by Jun 14.
5. After his data lands: engine v1 build (staffing-mix join, exposure scores), Gate 1 sanity check.
6. Toy slice AFTER freeze registered: feasibility counts only (D-20).

## Open questions

- UVA librarian / Darden data verdict (may moot the $365 DealStats gate).
- BVR reply (1-2 weeks; lands near the Jul 6 gate).
- Valuation pre-reader name.

## Parking lot (v2, not now)

Interactive web map · live engine/dashboard · The Audit · The Unmarked Risk · quarterly forward-panel data note · X account build-out.

## Session log index

- [2026-06-09 · Session 01](00_admin/SESSION_LOG/2026-06-09_session-01.md): intake, lenses, pressure test, plan locked, folder built.
- [2026-06-09 · Session 02](00_admin/SESSION_LOG/2026-06-09_session-02.md): answers locked, git wired, env scaffold, Supabase separation flag.
- [2026-06-10 · Session 03](00_admin/SESSION_LOG/2026-06-10_session-03.md): GitHub synced, keys verified, 2 datasets landed + 4 scripted, full audit passed with fixes.
