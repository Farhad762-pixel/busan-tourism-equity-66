#!/usr/bin/env python3
"""Check frozen 2026-11-13 repository blobs and append-only Git changes.

This is a research-integrity guard for accidental overwrites/deletions.
It does not prevent a repository administrator from rewriting history,
disabling the workflow, or deleting the repository.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / (
    "research_journal/2026-11-13_1658_KST/"
    "BASELINE_TRACKED_FILES_2026-11-13_1658_KST.csv"
)
SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


def git(*args: str) -> str:
    run = subprocess.run(
        ["git", *args], cwd=ROOT, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        check=False,
    )
    if run.returncode:
        raise RuntimeError(
            "git " + " ".join(args) + " failed: " + run.stderr.strip()
        )
    return run.stdout


def check_snapshot() -> list[str]:
    problems: list[str] = []
    with MANIFEST.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 89:
        problems.append(f"Original manifest should list 89 blobs; found {len(rows)}")
    tracked = {}
    for line in git("ls-tree", "-r", "--full-tree", "HEAD").splitlines():
        info, separator, path = line.partition("\t")
        chunks = info.split()
        if separator and len(chunks) == 3 and chunks[1] == "blob":
            tracked[path] = chunks[2]
    paths_seen: set[str] = set()
    for row in rows:
        path, blob = row["path"], row["git_blob_sha_at_freeze"]
        if path in paths_seen:
            problems.append(f"Duplicate manifest entry: {path}")
        paths_seen.add(path)
        if not SHA_PATTERN.fullmatch(blob):
            problems.append(f"Invalid frozen Git blob ID: {path}")
        actual = tracked.get(path)
        if actual != blob:
            problems.append(
                f"ORIGINAL FILE CHANGED OR DELETED: {path}; "
                f"frozen={blob}, HEAD={actual or 'MISSING'}"
            )
    return problems


def check_append_only(base_sha: str) -> list[str]:
    if not base_sha or not SHA_PATTERN.fullmatch(base_sha):
        return []
    if set(base_sha) == {"0"}:
        return []
    problems: list[str] = []
    changes = git("diff", "--name-status", "--no-renames", base_sha, "HEAD")
    for row in changes.splitlines():
        state, _, path = row.partition("\t")
        if state != "A":
            problems.append(
                f"APPEND-ONLY VIOLATION: {state} {path} "
                "(create a newly dated file instead of modifying or deleting)"
            )
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="", help="Base SHA of PR or previous main commit")
    args = parser.parse_args()
    if not MANIFEST.is_file():
        print("FAIL: frozen baseline manifest missing", file=sys.stderr)
        return 1
    problems = check_snapshot() + check_append_only(args.base)
    if problems:
        for issue in problems:
            print("FAIL:", issue, file=sys.stderr)
        return 1
    print("PASS: all 89 original research files match their frozen Git blobs")
    if args.base and SHA_PATTERN.fullmatch(args.base):
        print("PASS: new changes are additions only; no tracked file was overwritten/deleted")
    return 0


if __name__ == "__main__":
    sys.exit(main())
