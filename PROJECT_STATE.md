# PROJECT_STATE.md — Living State

**Last updated:** 2026-06-09 (Session 02, pre-flight quick session)
**Phase:** W0 complete. W1 runs when William lands.
**Launch target:** SSRN + site + LinkedIn live by Aug 2, 2026. Hard floor: before August apps.

## Status snapshot

- Plan locked (MASTER_PLAN v1.0), decisions D-01..D-34. Travel-agency call **LOCKED** by William (D-13).
- **Git is live:** repo initialized at folder root, first commit done (10 files, 634 lines), remote wired to `github.com/fnh4mv/Repricing-Main-Street-` (private). Push pending one thing: William's PAT in `.env`.
- `.env` scaffold created at folder root (gitignored): GITHUB_PAT, SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY, ANTHROPIC_API_KEY, OSF_TOKEN. William fills when he lands. Note: the env file he created earlier is NOT in this folder (probably parent "Sheets Paper" folder, which is outside my view); values go into this `.env`.
- **Supabase separation flag (D-33):** connected MCP sees only firm projects (egos-dev, eGOS Backend). Off-limits per D-10. Paper's Supabase = personal-org project, creds in `.env`.
- William done: SSRN account created · UVA librarian email sent (no DealStats/BIZCOMPS visible in catalog, matching our research) · runner = Mac (D-34) · Chad heads-up planned · W5 block acknowledged.
- No data pulled yet (freeze first, D-12).

## Gate status

| Gate | What | Status |
|------|------|--------|
| 0 | Freeze registered (OSF embargo) + panel wave 1 + Wayback yield known | OPEN, due Jun 14 |
| 1 | Engine sanity ranking (bookkeeping ≫ plumbing) | pending, due Jun 21 |
| 2 | Pricing n-table (n per category-quarter, SDE disclosure rates) | pending, due Jun 28 |
| 3 | Result class declared (discount / null-at-MDE / premium) | pending, due Jul 5 |
| DealStats | $365 buy decision (D-06; librarian reply may moot it) | pending, Jul 6 |

## WILLIAM'S QUEUE

1. **Fill `.env` when you land** (file is at the folder root; in Finder press Cmd+Shift+. to see dotfiles): GitHub fine-grained PAT (repo-scoped, Contents: read/write), your PERSONAL Supabase project URL + keys (not egos-dev / eGOS Backend, D-33), Anthropic API key. Say "env ready" and I push the repo + wire the panel.
2. **Librarian reply:** forward the verdict on DealStats/BIZCOMPS when it arrives.
3. **Chad heads-up** when natural (before W6).
4. **Valuation pre-reader:** start thinking of one name; recruit by ~Jun 21 with a Jul 13 save-the-date (D-30).

## NEXT ACTIONS (machine queue, W1, in order)

0. Push initial commit to GitHub the moment PAT lands; verify with `git ls-remote`.
1. Pull OEWS staffing matrices, Eloundou, Felten AIOE, Anthropic AEI, ABS owner-age, BDS firm-age → `02_data/raw/` + MANIFEST entries.
2. Draft freeze doc (basket NAICS mapping, spec, min-cell, robustness, MDE method, three framings) → `07_freeze/` for William's gate-1 sign-off.
3. OSF registration walk-through for William (account, embargo, bland title).
4. Wayback CDX audit script (his machine or Claude-in-Chrome; archive.org blocked in sandbox).
5. Weekly panel snapshot script for Mac launchd + Supabase DDL (personal project) + dated CSV fallback.
6. Toy slice AFTER freeze: feasibility counts only (D-20).

## Open questions

- UVA librarian verdict (may kill or confirm the $365 DealStats gate).
- Valuation pre-reader name.
- Whether William's personal Supabase project exists yet or needs creating (his org, his account; 2 minutes).

## Parking lot (v2, not now)

Interactive web map · live engine/dashboard · The Audit · The Unmarked Risk · quarterly forward-panel data note · X account build-out.

## Session log index

- [2026-06-09 · Session 01](00_admin/SESSION_LOG/2026-06-09_session-01.md): intake, lenses, pressure test, plan locked, folder built.
- [2026-06-09 · Session 02](00_admin/SESSION_LOG/2026-06-09_session-02.md): William's answers locked, git live + remote wired, .env scaffold, Supabase separation flag.
