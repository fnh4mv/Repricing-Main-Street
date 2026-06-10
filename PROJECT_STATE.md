# PROJECT_STATE.md - Living State

**Last updated:** 2026-06-10 (Session 03, W1 collection + audit)
**Phase:** W1 in progress. Gate 0 due Jun 14.
**Launch target:** SSRN + site + LinkedIn live by Aug 2, 2026. Hard floor: before August apps.

## Status snapshot

- **GitHub live and synced:** private repo `fnh4mv/Repricing-Main-Street`, push working, all project docs committed. Provenance records tracked in git; raw data and env files excluded by design.
- **All keys in env (verified):** GitHub PAT, Supabase (personal project `piou...`, confirmed NOT a firm project per D-33), Anthropic, Census, BLS, OSF, HuggingFace, Zenodo.
- **Data: ALL 6 ENGINE DATASETS LANDED AND VERIFIED** (Eloundou 923 occs, Felten 774, AEI 756 + task files, OEWS May 2025, ABS 2023 owner-age, BDS 2023 firm-age). Every pull pinned, checksummed, provenance-logged.
- **FREEZE_v1_DRAFT.md is written and awaiting William's signature** (`07_freeze/`), with the OSF walk-through beside it. OEWS granularity probe locked the mapping: HVAC+plumbing share engine score 238220, call centers+transcription share 561400, both disclosed. Primary measure = Eloundou human_rating_beta (human annotations, so no "the model scored itself" attack surface).
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

1. **GATE 1 OF THE AUTHORSHIP CONTRACT: read, edit, and sign `07_freeze/FREEZE_v1_DRAFT.md`** (~30 min). This is the document a referee will judge you by. Push back on anything. Then register it on OSF per `07_freeze/OSF_REGISTRATION_GUIDE.md` (10 min, embargo to 2026-08-05) and paste the registration URL + DOI into chat. NOTHING pricing-side runs until this is done, and the panel clock is ticking toward Jun 14.
2. **Darden professor:** when they reply, share what they're offering (data access? feedback?). A faculty reader is the D-30 credibility slot.
3. **Forward librarian/BVR replies** as they land.
4. **Valuation pre-reader:** one name by ~Jun 21, Jul 13 save-the-date (D-30).
5. (Standing) Chad heads-up before W6; W5 writing block calendared Jul 6-12.

## NEXT ACTIONS (machine queue, in order)

1. **Panel snapshot script + launchd plist + Supabase DDL + SETUP_MAC.md** (runs only after OSF registration; first wave by Jun 14).
2. **Wayback CDX audit script** (his Mac; archive.org blocked in sandbox). Gate 0 needs the yield number.
3. **Engine v1 build** (SOC harmonization + staffing-mix join + scores per freeze Section 4) and the Gate 1 sanity ranking. Data is all here; can start immediately, engine side is not pricing data.
4. Toy slice AFTER freeze registered: feasibility counts only (D-20).
5. Exhibit 1 draft (exposure map) once Gate 1 passes.

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
