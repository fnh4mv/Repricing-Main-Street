# CLAUDE.md - Boot File for Repricing Main Street

Read this first, every session. Then read PROJECT_STATE.md. That's the whole boot.

## What this is

Personal research project of William Sheets (UVA second-year, eGateway intern, sole author). Paper: "Repricing Main Street: AI Exposure, the Succession Wave, and What Buyers Aren't Pricing." Tests whether Main Street sale multiples in AI-exposed service categories have diverged from AI-insulated trades since late 2022. Launch target: SSRN + LinkedIn + williamsheets.com by Aug 2, 2026. Fully separate from eGateway work.

## Read order

1. This file
2. `PROJECT_STATE.md` (status, queues, gates)
3. As needed: `00_admin/MASTER_PLAN.md` (full plan) · `00_admin/DECISIONS.md` (locked decisions, numbered D-XX) · `00_admin/VOICE.md` (writing voice)

## Hard rules (never break, never relitigate silently)

1. **No em dashes in anything William publishes or signs.** See VOICE.md. Apply everywhere by habit.
2. **No firm data, tools-derived numbers, accounts, or hardware in the paper** (D-10). eGateway tools for orientation only.
3. **Freeze before pricing:** no pricing data touched before the OSF-embargoed pre-registration is filed; after the freeze, the spec doesn't move (D-12).
4. **Descriptive claims only.** "Prices don't yet reflect measurable AI exposure." Never causal language (D-11).
5. **Public outputs = aggregates + code + government data only.** Listing-level records and scraper code stay private permanently (D-10).
6. **`02_data/raw/` is immutable.** Dated subfolders, never edited, every pull gets a MANIFEST.md entry with source URL and date.
7. **Every number in a draft carries a source path.** Raw file + script. A wrong number in print is the one unrecoverable failure.
8. **Log every session** to `00_admin/SESSION_LOG/` (feeds the published "How this paper was built" appendix, D-03).
9. **Ship every session.** Code, data, a validated join, or drafted prose. Never discussion alone.
10. **Scope is MASTER_PLAN.md.** New ideas go to the PROJECT_STATE parking lot, not into the build.

## Folder map

```
SHEETS MAINSTREET PAPER/
├── CLAUDE.md              ← this file
├── PROJECT_STATE.md       ← living state, queues, gates
├── 00_admin/              ← plan, decisions, voice, intake, session logs
│   └── SESSION_LOG/
├── 01_sources/            ← source registry + collected PDFs
├── 02_data/
│   ├── raw/               ← immutable dated pulls + MANIFEST.md
│   └── processed/         ← cleaned/joined outputs (regenerable)
├── 03_engine/             ← exposure-scoring code (mirrors private GitHub)
├── 04_analysis/           ← notebooks, exhibit generation
├── 05_paper/              ← outline, drafts, exhibits
├── 06_distribution/       ← SSRN package, posts, website assets
└── 07_freeze/             ← pre-registration record (OSF mirror)
```

## Operating policies

- **Models:** Fable 5 default for research, methodology, code, prose, verification. Sonnet/Haiku subagents for bulk mechanical extraction only, with Fable 5 sample-verification after (D-25).
- **Agents:** fan out for independent collection/research; never fan out judgment (baskets, claims, captions).
- **Infra:** flat files canonical; Supabase = forward-panel mirror; n8n = recurring jobs only; GitHub private until launch (D-22).
- **William's time:** 2-4 hrs/wk, spent only on his six gates (D-26) and items in WILLIAM'S QUEUE. Put asks in front of him with exactly what to do and why.
- **Voice:** all published prose per VOICE.md. Short sentences, concrete, plain words, honest limits, no em dashes, one earned closing line max.

## Session protocol

Boot → pick top of NEXT ACTIONS (unless redirected) → ship → append session log → update PROJECT_STATE.md → flag William items. End of every session: PROJECT_STATE.md must be accurate enough that a brand-new chat resumes instantly.
