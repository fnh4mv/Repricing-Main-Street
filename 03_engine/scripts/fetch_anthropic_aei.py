#!/usr/bin/env python3
"""Fetch the Anthropic Economic Index occupation/task-level files.

Written 2026-06-10 by the DATA-1 collection agent because the Claude sandbox
proxy blocks huggingface.co (403 at CONNECT). Run this on the Mac from
anywhere; it locates the project root from its own path.

    python3 "03_engine/scripts/fetch_anthropic_aei.py"

What it does:
1. Downloads 11 files from the official Hugging Face repo
   Anthropic/EconomicIndex, pinned to revision db51ecb1 (state enumerated
   2026-06-10), into 02_data/raw/2026-06-10_anthropic_aei/ preserving
   repo-relative paths.
2. Verifies every file byte-for-byte against the git blob sha1 recorded at
   enumeration time. A mismatch deletes the file and reports failure.
3. Prints sha256, row count, and columns per file, and appends the same as a
   download log to the folder's PROVENANCE.md.

Stdlib only. Uses HF_TOKEN from the environment or keys.env if present
(not required; the dataset is public and ungated).
"""

import csv
import hashlib
import io
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = "Anthropic/EconomicIndex"
REVISION = "db51ecb12920faef6df2b21dff6207ebcbc72c6f"
BASE = f"https://huggingface.co/datasets/{REPO}/resolve/{REVISION}/"

# (repo path, expected size in bytes, expected git blob sha1)
FILES = [
    ("labor_market_impacts/job_exposure.csv", 37176, "aae568975228d5850a1913c0d09f6ce8437e7253"),
    ("labor_market_impacts/task_penetration.csv", 1889822, "2a20bcc33ccb02ae97c9aa6b2899bfa3911fc75b"),
    ("release_2025_03_27/task_pct_v1.csv", 461306, "fa7771817633eea639cb4a23cb5d23010eee47e5"),
    ("release_2025_03_27/task_pct_v2.csv", 435372, "9b01af042ad5d422f328eed3a9b165a3a42c6208"),
    ("release_2025_03_27/automation_vs_augmentation_by_task.csv", 561368, "844e3bf4f227e5bd8a358d6558a4e3c37ac7ea2f"),
    ("release_2025_03_27/automation_vs_augmentation_v1.csv", 197, "3d12303285f43eb353684bd9520d63a306ad9d4f"),
    ("release_2025_03_27/automation_vs_augmentation_v2.csv", 198, "c56f5ec709d61984a59106a08be9b2d70f460ff5"),
    ("release_2025_03_27/onet_task_statements.csv", 3592256, "f156004fb29dda092b86d374cf839e901fbdffd8"),
    ("release_2025_03_27/SOC_Structure.csv", 77176, "07249b132a59e684f84b3ce9b012fa0107631256"),
    ("release_2025_03_27/README.md", 3205, "e9a7295d89a4646fb6453da04becb5ac7cfb2d52"),
    ("README.md", 4396, "c75b9b35130b3dc1e69fcc4bfbe6b6f00d3fc550"),
]

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEST = PROJECT_ROOT / "02_data" / "raw" / "2026-06-10_anthropic_aei"
PROVENANCE = DEST / "PROVENANCE.md"


def hf_token():
    tok = os.environ.get("HF_TOKEN")
    if tok:
        return tok.strip()
    keys = PROJECT_ROOT / "keys.env"
    if keys.exists():
        for line in keys.read_text().splitlines():
            if line.startswith("HF_TOKEN="):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    return None


def git_blob_sha1(data: bytes) -> str:
    h = hashlib.sha1()
    h.update(b"blob %d\x00" % len(data))
    h.update(data)
    return h.hexdigest()


def fetch(path: str, token) -> bytes:
    req = urllib.request.Request(BASE + path)
    req.add_header("User-Agent", "repricing-main-street-data-collection/1.0")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def csv_profile(data: bytes, name: str):
    """Return (n_data_rows, columns) for csv files, (None, None) otherwise."""
    if not name.endswith(".csv"):
        return None, None
    text = data.decode("utf-8", errors="replace")
    reader = csv.reader(io.StringIO(text))
    try:
        header = next(reader)
    except StopIteration:
        return 0, []
    n = sum(1 for _ in reader)
    return n, header


def main():
    token = hf_token()
    DEST.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = [
        "",
        "## Download log (appended by fetch_anthropic_aei.py)",
        f"- Run timestamp (UTC): {stamp}",
        f"- Revision: {REVISION}",
        "",
        "| File | sha256 | Verified vs pinned git sha1 | Data rows | Columns |",
        "|---|---|---|---|---|",
    ]
    failures = 0
    for path, exp_size, exp_sha1 in FILES:
        out = DEST / path
        out.parent.mkdir(parents=True, exist_ok=True)
        print(f"-> {path} ...", end=" ", flush=True)
        try:
            data = fetch(path, token)
        except Exception as e:
            print(f"FAILED: {e}")
            failures += 1
            log.append(f"| {path} | DOWNLOAD FAILED: {e} | no | | |")
            continue
        got_sha1 = git_blob_sha1(data)
        ok = got_sha1 == exp_sha1 and len(data) == exp_size
        if not ok:
            print(f"INTEGRITY MISMATCH (size {len(data)} vs {exp_size}, sha1 {got_sha1} vs {exp_sha1}). Not saved.")
            failures += 1
            log.append(f"| {path} | INTEGRITY MISMATCH, not saved | no | | |")
            continue
        out.write_bytes(data)
        sha256 = hashlib.sha256(data).hexdigest()
        nrows, cols = csv_profile(data, path)
        rows_s = "" if nrows is None else str(nrows)
        cols_s = "" if cols is None else "; ".join(cols[:8]) + (" ..." if cols and len(cols) > 8 else "")
        print(f"ok ({len(data)} bytes, {rows_s or 'n/a'} rows)")
        if cols:
            print(f"   columns: {cols_s}")
        log.append(f"| {path} | {sha256} | yes | {rows_s} | {cols_s} |")
    with open(PROVENANCE, "a", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")
    print()
    if failures:
        print(f"DONE WITH {failures} FAILURE(S). See {PROVENANCE}")
        sys.exit(1)
    print(f"All {len(FILES)} files landed and verified. Log appended to {PROVENANCE}")
    print("Remember: update the Notes cell for the AEI row in 02_data/MANIFEST.md from 'script pending' to 'landed'.")


if __name__ == "__main__":
    main()
