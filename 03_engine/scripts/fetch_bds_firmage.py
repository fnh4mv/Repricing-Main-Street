#!/usr/bin/env python3
"""Fetch Census BDS 2023 two-way table: 4-digit NAICS by Firm Age (1978-2023).

Repricing Main Street, dataset 3 of 3 (succession complement check).
Target dir: 02_data/raw/2026-06-10_bds_firmage/
Run from anywhere: python3 03_engine/scripts/fetch_bds_firmage.py [--force]

Stdlib only. No API key needed. Downloads the CSV exactly as published,
hashes it, counts rows, prints the firm-age buckets and a NAICS 5412 sample.

On success, appends a Landing record to the folder's PROVENANCE.md.
Written by DATA-2 agent, 2026-06-10. Sandbox egress to www2.census.gov was
blocked, so this script is the official landing path (run on William's Mac).
"""

import csv
import hashlib
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

URL = "https://www2.census.gov/programs-surveys/bds/tables/time-series/2023/bds2023_vcn4_fa.csv"
PROJECT_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = PROJECT_ROOT / "02_data" / "raw" / "2026-06-10_bds_firmage"
CSV_PATH = OUT_DIR / "bds2023_vcn4_fa.csv"
PROVENANCE = OUT_DIR / "PROVENANCE.md"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def download(url: str, dest: Path) -> int:
    req = urllib.request.Request(url, headers={"User-Agent": "RepricingMainStreet-research/1.0 (contact: sheets@egatewaycapital.com)"})
    done = 0
    try:
        with urllib.request.urlopen(req, timeout=180) as resp, open(dest, "wb") as out:
            status = getattr(resp, "status", 200)
            if status != 200:
                raise RuntimeError(f"HTTP {status} for {url}")
            while True:
                chunk = resp.read(1 << 20)
                if not chunk:
                    break
                out.write(chunk)
                done += len(chunk)
                if done % (5 << 20) < (1 << 20):
                    print(f"  ... {done / 1e6:.1f} MB")
    except Exception as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            print("TLS certs missing. Run: /Applications/Python*/Install Certificates.command")
        raise
    return done


def main() -> int:
    force = "--force" in sys.argv
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if CSV_PATH.exists() and not force:
        print(f"REFUSING to overwrite existing {CSV_PATH} (raw/ is immutable). Use --force only if the prior pull was bad.")
        return 1

    t0 = utc_now()
    print(f"[{t0}] downloading {URL}")
    nbytes = download(URL, CSV_PATH)
    digest = sha256_file(CSV_PATH)
    print(f"  saved {CSV_PATH.name}: {nbytes:,} bytes  sha256={digest}")

    with open(CSV_PATH, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        print(f"  columns ({len(header)}): {', '.join(header)}")
        fage_i = next((i for i, c in enumerate(header) if c.lower() == "fage"), None)
        naics_i = next((i for i, c in enumerate(header) if "naics" in c.lower()), None)
        year_i = next((i for i, c in enumerate(header) if c.lower() == "year"), None)
        if fage_i is None or naics_i is None or year_i is None:
            print("VERIFICATION FAILED: expected columns year, fage, and a naics column.")
            return 2
        n = 0
        fages = set()
        naics_codes = set()
        max_year = ""
        sample_5412 = {}
        for row in reader:
            n += 1
            fages.add(row[fage_i])
            naics_codes.add(row[naics_i])
            y = row[year_i]
            if y > max_year:
                max_year = y
            if row[naics_i].startswith("5412"):
                k = (y, row[fage_i])
                sample_5412[k] = row

    print(f"  data rows: {n:,}")
    print(f"  distinct firm-age buckets ({len(fages)}):")
    for b in sorted(fages):
        print(f"    {b}")
    four_digit = [c for c in naics_codes if c.isdigit() and len(c) == 4]
    print(f"  distinct industry codes: {len(naics_codes)} total, {len(four_digit)} are 4-digit numeric")
    if not four_digit:
        print("VERIFICATION FAILED: no 4-digit NAICS codes found.")
        return 2
    latest_5412 = [v for (y, fa), v in sorted(sample_5412.items()) if y == max_year]
    if latest_5412:
        print(f"  NAICS 5412 sample row (year {max_year}):")
        for name, val in list(zip(header, latest_5412[0]))[:12]:
            print(f"    {name}: {val}")
    else:
        print("VERIFICATION WARNING: no NAICS 5412 rows found. Investigate before use.")

    rec = (
        "\n## Landing record (auto-appended by fetch_bds_firmage.py)\n\n"
        f"- Retrieved (UTC): {t0}\n"
        f"- Source URL: {URL}\n"
        f"- File: {CSV_PATH.name}, {nbytes:,} bytes\n"
        f"- sha256: {digest}\n"
        f"- Data rows (excl. header): {n:,}\n"
        f"- Columns: {', '.join(header)}\n"
        f"- Years: through {max_year}\n"
        f"- Firm-age buckets: {'; '.join(sorted(fages))}\n"
        f"- Distinct 4-digit NAICS codes: {len(four_digit)}\n"
        f"- NAICS 5412 present: {'yes' if latest_5412 else 'NO (flag)'}\n"
        f"- Verified by: fetch_bds_firmage.py\n"
    )
    with open(PROVENANCE, "a", encoding="utf-8") as f:
        f.write(rec)
    print(f"Landing record appended to {PROVENANCE}")
    print("NEXT: flip this dataset's row in 02_data/MANIFEST.md from SCRIPT-ONLY to LANDED.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
