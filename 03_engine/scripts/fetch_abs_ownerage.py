#!/usr/bin/env python3
"""Fetch Census ABS 2023 Characteristics of Business Owners: owner age by sector, US level.

Repricing Main Street, dataset 2 of 3 (succession context).
Target dir: 02_data/raw/2026-06-10_abs_ownerage/
Run from anywhere: python3 03_engine/scripts/fetch_abs_ownerage.py [--force]

Stdlib only. Requires CENSUS_API_KEY in keys.env at project root.
Saves raw API JSON bytes exactly as returned, plus a flattened CSV.
Prints the owner-age categories found and the NAICS granularity check.

On success, appends a Landing record to the folder's PROVENANCE.md.
Written by DATA-2 agent, 2026-06-10. Sandbox egress to api.census.gov was
blocked and the API requires a key, so this script is the official landing
path (run on William's Mac).
"""

import csv
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

VINTAGE = 2023
BASE = f"https://api.census.gov/data/{VINTAGE}/abscbo"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = PROJECT_ROOT / "02_data" / "raw" / "2026-06-10_abs_ownerage"
PROVENANCE = OUT_DIR / "PROVENANCE.md"
DISCOVERY_JSON = OUT_DIR / f"abscbo{VINTAGE}_qdesc_discovery_us_total.json"
MAIN_JSON = OUT_DIR / f"abscbo{VINTAGE}_ownerage_us_by_sector.json"
FLAT_CSV = OUT_DIR / f"abscbo{VINTAGE}_ownerage_us_by_sector_flat.csv"

MAIN_GET = (
    "GEO_ID,NAME,NAICS2022,NAICS2022_LABEL,"
    "OWNER_SEX,OWNER_SEX_LABEL,OWNER_ETH,OWNER_ETH_LABEL,"
    "OWNER_RACE,OWNER_RACE_LABEL,OWNER_VET,OWNER_VET_LABEL,"
    "QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL,YEAR,"
    "OWNPDEMP,OWNPDEMP_F,OWNPDEMP_S,OWNPDEMP_PCT,OWNPDEMP_PCT_S"
)


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def read_key() -> str:
    keys = PROJECT_ROOT / "keys.env"
    for line in keys.read_text().splitlines():
        if line.startswith("CENSUS_API_KEY="):
            val = line.split("=", 1)[1].strip().strip('"').strip("'")
            if val:
                return val
    print(f"CENSUS_API_KEY not found or empty in {keys}")
    sys.exit(1)


def api_get(params: dict, key: str) -> bytes:
    q = urllib.parse.urlencode(params, safe=":*,()")
    url = f"{BASE}?{q}&key={key}"
    redacted = f"{BASE}?{q}&key=REDACTED"
    print(f"  GET {redacted}")
    req = urllib.request.Request(url, headers={"User-Agent": "RepricingMainStreet-research/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:500]
        print(f"  HTTP {e.code}: {body}")
        raise
    except Exception as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            print("TLS certs missing. Run: /Applications/Python*/Install Certificates.command")
        raise


def find_age_qdesc(rows, header):
    qi = header.index("QDESC")
    qli = header.index("QDESC_LABEL")
    cands = {}
    for r in rows:
        if "AGE" in (r[qli] or "").upper():
            cands[r[qi]] = r[qli]
    return cands


def main() -> int:
    force = "--force" in sys.argv
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if MAIN_JSON.exists() and not force:
        print(f"REFUSING to overwrite existing {MAIN_JSON} (raw/ is immutable). Use --force only if the prior pull was bad.")
        return 1
    key = read_key()
    t0 = utc_now()

    # Query 1: discover the owner-age QDESC code and its OWNCHAR categories.
    print(f"[{t0}] Query 1: QDESC discovery at US level, total sector, all-owner demographics")
    disc_params = {
        "get": "QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL",
        "for": "us:*",
        "NAICS2022": "00",
        "OWNER_SEX": "001",
        "OWNER_ETH": "001",
        "OWNER_RACE": "00",
        "OWNER_VET": "001",
    }
    try:
        disc_raw = api_get(disc_params, key)
    except urllib.error.HTTPError:
        print("  Filtered discovery failed; retrying without demographic filters (larger pull).")
        disc_params = {"get": "QDESC,QDESC_LABEL,OWNCHAR,OWNCHAR_LABEL", "for": "us:*", "NAICS2022": "00"}
        disc_raw = api_get(disc_params, key)
    DISCOVERY_JSON.write_bytes(disc_raw)
    disc = json.loads(disc_raw)
    header, rows = disc[0], disc[1:]
    questions = sorted({(r[header.index("QDESC")], r[header.index("QDESC_LABEL")]) for r in rows})
    print(f"  questions found: {questions}")
    cands = find_age_qdesc(rows, header)
    if len(cands) != 1:
        own = {c: l for c, l in cands.items() if "OWN" in (l or "").upper()}
        if len(own) == 1:
            cands = own
    if len(cands) != 1:
        print(f"Could not isolate a single owner-age QDESC. Candidates: {cands}")
        print("Inspect the discovery JSON and set the QDESC filter manually.")
        return 3
    age_code, age_label = next(iter(cands.items()))
    print(f"  owner-age question: QDESC={age_code} ({age_label})")
    qli, oli = header.index("QDESC_LABEL"), header.index("OWNCHAR_LABEL")
    age_cats = sorted({r[oli] for r in rows if r[header.index("QDESC")] == age_code})
    print("  owner-age categories (US total, all owners):")
    for c in age_cats:
        print(f"    {c}")

    # Query 2: the main pull. All sectors, all demographic groups, owner age only.
    print("Query 2: owner age x NAICS sector x demographics, US level")
    main_raw = api_get({"get": MAIN_GET, "for": "us:*", "QDESC": age_code}, key)
    MAIN_JSON.write_bytes(main_raw)
    data = json.loads(main_raw)
    mh, mrows = data[0], data[1:]
    print(f"  rows (excl. header): {len(mrows):,}")

    with open(FLAT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(mh)
        w.writerows(mrows)

    ni, nli = mh.index("NAICS2022"), mh.index("NAICS2022_LABEL")
    naics_codes = sorted({r[ni] for r in mrows})
    deeper = [c for c in naics_codes if c.isdigit() and len(c) > 2]
    print(f"  distinct NAICS2022 codes ({len(naics_codes)}): {naics_codes}")
    print("  granularity verdict: " + ("SECTOR LEVEL ONLY (2-digit and ranges), as expected" if not deeper else f"DEEPER THAN SECTOR FOUND: {deeper}"))

    rec = (
        "\n## Landing record (auto-appended by fetch_abs_ownerage.py)\n\n"
        f"- Retrieved (UTC): {t0}\n"
        f"- Endpoint: {BASE} (key=REDACTED)\n"
        f"- Owner-age question: QDESC={age_code} ({age_label})\n"
        f"- Owner-age categories: {'; '.join(age_cats)}\n"
        f"- {DISCOVERY_JSON.name}: {len(disc_raw):,} bytes, sha256 {sha256_bytes(disc_raw)}, {len(rows):,} rows\n"
        f"- {MAIN_JSON.name}: {len(main_raw):,} bytes, sha256 {sha256_bytes(main_raw)}, {len(mrows):,} rows\n"
        f"- {FLAT_CSV.name}: flattened from main JSON, {len(mrows):,} rows, sha256 {sha256_bytes(FLAT_CSV.read_bytes())}\n"
        f"- Columns: {', '.join(mh)}\n"
        f"- Distinct NAICS2022 codes: {', '.join(naics_codes)}\n"
        f"- Granularity: {'sector (2-digit) only' if not deeper else 'WARNING deeper codes present: ' + ', '.join(deeper)}\n"
        f"- Verified by: fetch_abs_ownerage.py\n"
    )
    with open(PROVENANCE, "a", encoding="utf-8") as f:
        f.write(rec)
    print(f"Landing record appended to {PROVENANCE}")
    print("NEXT: flip this dataset's row in 02_data/MANIFEST.md from SCRIPT-ONLY to LANDED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
