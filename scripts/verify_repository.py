"""Read-only inventory and validation of available evidence; optional report output.

Run from any directory: python /path/to/repo/scripts/verify_repository.py
Missing archived research is reported as blocked, never as reproduced.
"""

import argparse
import csv
from datetime import datetime
import hashlib
import io
import json
import math
from pathlib import Path
import subprocess
import sys
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from src.analysis.metrics import gini, hhi
from src.clean_attractions import FIELDS


def csv_rows(path):
    raw = path.read_bytes()
    for encoding in ("utf-8-sig", "cp949"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError(f"Unsupported CSV encoding: {path}")
    reader = csv.DictReader(io.StringIO(text))
    rows = list(reader)
    return encoding, reader.fieldnames or [], rows


def inventory():
    paths = subprocess.check_output(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"], cwd=ROOT
    ).decode().split("\0")
    records = []
    for name in sorted(set(filter(None, paths))):
        path = ROOT / name
        if not path.is_file():
            continue
        record = dict(path=name, bytes=path.stat().st_size,
                      sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        if path.suffix == ".csv":
            encoding, columns, rows = csv_rows(path)
            record.update(encoding=encoding, rows=len(rows), columns=columns,
                          duplicate_rows=len(rows) - len({json.dumps(r, sort_keys=True) for r in rows}),
                          missing={k: sum(not (r.get(k) or "").strip() for r in rows) for k in columns},
                          ragged_rows=sum(None in r or any(v is None for v in r.values()) for r in rows))
            for key in ("기준년월일", "month"):
                if key in columns and rows:
                    dates = sorted(r[key] for r in rows if r.get(key))
                    record["date_range"] = [dates[0], dates[-1]] if dates else []
        elif path.suffix == ".json":
            obj = json.loads(path.read_text(encoding="utf-8-sig"))
            record["root_type"] = type(obj).__name__
            if isinstance(obj, dict) and "getAttractionEn" in obj:
                body = obj["getAttractionEn"]
                items = body["item"]
                record.update(rows=len(items), columns=sorted({k for r in items for k in r}),
                              duplicate_rows=len(items)-len({json.dumps(r, sort_keys=True) for r in items}),
                              declared_total=body.get("totalCount"))
        records.append(record)
    return records


def validate_attractions():
    _, columns, rows = csv_rows(ROOT / "data/processed/busan_attractions.csv")
    raw = json.loads((ROOT / "data/raw/busan_attractions_raw_full.json").read_text(encoding="utf-8-sig"))["getAttractionEn"]["item"]
    seen = set()
    expected = []
    for item in raw:
        key = json.dumps(item, sort_keys=True, ensure_ascii=False)
        if key not in seen:
            expected.append({target: str(item.get(source, "")) for source, target in FIELDS.items()})
            seen.add(key)
    errors = []
    if columns != list(FIELDS.values()) or rows != expected:
        errors.append("CSV does not exactly match the cleaner's JSON field projection")
    if len(rows) != 207 or len({r["uc_seq"] for r in rows}) != 207:
        errors.append("Expected 207 unique attraction IDs")
    counts = Counter(r["district"] for r in rows)
    if len(counts) != 16:
        errors.append("Expected 16 districts")
    for r in rows:
        try:
            lat, lon = float(r["latitude"]), float(r["longitude"])
            if not (34 <= lat <= 36 and 128 <= lon <= 130):
                errors.append(f"Coordinates outside broad Busan region: {r['uc_seq']}")
        except ValueError:
            errors.append(f"Invalid coordinates: {r['uc_seq']}")
    return dict(status="pass" if not errors else "fail", rows=len(rows),
                district_counts=dict(sorted(counts.items())), errors=errors,
                csv_json_consistency="exact field projection including row order")


def check_saved_summaries():
    _, _, policies = csv_rows(ROOT / "experiments/equity/results/rq3_policy_summary.csv")
    base = next(r for r in policies if float(r["lambda"]) == 0)
    checks = []
    for row in policies:
        gain = 100 * (float(row["undercapture_exposure"]) - float(base["undercapture_exposure"]))
        retention = float(row["mean_relevance"]) / float(base["mean_relevance"])
        checks.append(dict(policy_lambda=float(row["lambda"]),
                           gain_arithmetic_matches=abs(gain-float(row["undercapture_gain_pp"])) < 1e-10,
                           retention_arithmetic_matches=abs(retention-float(row["relevance_retained"])) < 1e-10))
    _, _, exposure = csv_rows(ROOT / "results/tables/figure4_district_exposure_comparison.csv")
    derived = {}
    for name in ("Baseline", "Equity"):
        shares = [float(r[name]) for r in exposure]
        derived[name] = dict(share_sum=sum(shares), gini=gini(shares), hhi=hhi(shares),
                             district_coverage=sum(x > 0 for x in shares))
    equity_policy = next(r for r in policies if float(r["lambda"]) == .8)
    matches = abs(derived["Equity"]["gini"]-float(equity_policy["exposure_gini"])) < 1e-10
    _, _, access = csv_rows(ROOT / "experiments/accessibility/results/accessibility_15km_summary.csv")
    origins = sorted({r["origin"] for r in access})
    access_checks = []
    for origin in origins:
        b = next(r for r in access if r["origin"] == origin and r["policy"] == "baseline")
        e = next(r for r in access if r["origin"] == origin and r["policy"] == "equity")
        access_checks.append(dict(origin=origin,
                                  same_query_count=b["eligible_query_count"] == e["eligible_query_count"],
                                  gain_pp=100*(float(e["undercapture_exposure"])-float(b["undercapture_exposure"]))))
    return dict(status="summary_arithmetic_only_not_experiment_reproduction", policy_checks=checks,
                exposure_table_metrics=derived, exposure_table_matches_lambda_0_8_gini=matches,
                accessibility_checks=access_checks)


def validate_historical_exports():
    """Structural checks cannot establish the original download selections."""
    reports = []
    paths = sorted((ROOT / "data/raw/tourism_spending/haeundae").glob("*.csv"))
    paths += [ROOT / "data/raw/foreign_visitors_raw.csv", ROOT / "data/raw/foreign_spending_raw.csv"]
    for path in paths:
        _, columns, rows = csv_rows(path)
        numeric = [key for key in columns if "소비" in key or key == "방문자 수"]
        errors = []
        for number, row in enumerate(rows, 2):
            for key in numeric:
                try:
                    value = float(row[key].replace(",", "").rstrip("%"))
                    if not math.isfinite(value) or value < 0:
                        raise ValueError
                except (ValueError, TypeError, AttributeError):
                    errors.append(f"Invalid nonnegative numeric value at row {number}: {key}")
            if "기준년월일" in columns:
                text = row["기준년월일"]
                try:
                    if len(text) != 6:
                        raise ValueError
                    datetime.strptime(text, "%Y%m")
                except (ValueError, TypeError):
                    errors.append(f"Invalid YYYYMM at row {number}")
        key_columns = [key for key in columns if key not in numeric]
        keys = [tuple(row[k] for k in key_columns) for row in rows]
        duplicate_keys = len(keys) - len(set(keys))
        if duplicate_keys:
            errors.append("Duplicate categorical/date keys")
        if "total_foreign_spending" in path.name:
            year = path.stem.rsplit("_", 1)[1]
            if {r["기준년월일"] for r in rows} != {f"{year}{month:02}" for month in range(1, 13)}:
                errors.append("District-year total is missing expected months")
        reports.append(dict(path=path.relative_to(ROOT).as_posix(), rows=len(rows),
                            unique_regions=sorted({r["지역"] for r in rows}) if "지역" in columns else [],
                            checked_numeric_fields=numeric, duplicate_keys=duplicate_keys, errors=errors,
                            provenance_status="unverified_export_filters_and_redistribution_terms"))
    return reports


def audit():
    records = inventory()
    by_hash = defaultdict(list)
    for r in records:
        if r["bytes"]:
            by_hash[r["sha256"]].append(r["path"])
    visitor = ROOT / "data/raw/foreign_visitors_raw.csv"
    spending = ROOT / "data/raw/foreign_spending_raw.csv"
    return dict(schema_version=1, inventory=records,
                duplicate_file_groups=[v for v in by_hash.values() if len(v) > 1],
                attractions=validate_attractions(),
                historical_exports=validate_historical_exports(),
                mislabeled_spending_equals_visitors=visitor.read_bytes() == spending.read_bytes(),
                research_reproduction=dict(status="blocked_missing_inputs",
                    missing=["768-row district-month panel", "combined research JSON", "48 benchmark queries and categories",
                             "archived economic and accessibility scripts", "station coordinates and detailed policies", "manuscript and figures"]),
                saved_summaries=check_saved_summaries())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional local JSON report (do not publish source inventories blindly)")
    parser.add_argument("--summary-output", type=Path, help="Optional small derived summary, omitting file contents/inventory")
    parser.add_argument("--manifest-ref", help="Git revision for an immutable baseline manifest")
    parser.add_argument("--manifest-output", type=Path)
    args = parser.parse_args()
    report = audit()
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    if args.summary_output:
        summary = {k: v for k, v in report.items() if k != "inventory"}
        args.summary_output.parent.mkdir(parents=True, exist_ok=True)
        args.summary_output.write_text(json.dumps(summary, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    if args.manifest_ref or args.manifest_output:
        if not (args.manifest_ref and args.manifest_output):
            parser.error("Use --manifest-ref and --manifest-output together")
        revision = subprocess.check_output(["git", "rev-parse", "--verify", args.manifest_ref], cwd=ROOT).decode().strip()
        names = subprocess.check_output(["git", "ls-tree", "-rz", "--name-only", revision], cwd=ROOT).decode().split("\0")
        args.manifest_output.parent.mkdir(parents=True, exist_ok=True)
        with args.manifest_output.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["revision", "path", "bytes", "sha256"])
            writer.writeheader()
            for name in filter(None, names):
                content = subprocess.check_output(["git", "show", f"{revision}:{name}"], cwd=ROOT)
                writer.writerow(dict(revision=revision, path=name, bytes=len(content), sha256=hashlib.sha256(content).hexdigest()))
    print(json.dumps({k: v for k, v in report.items() if k != "inventory"}, ensure_ascii=False, indent=2))
    return 1 if report["attractions"]["errors"] or any(
        row["errors"] for row in report["historical_exports"]
    ) else 0


if __name__ == "__main__":
    raise SystemExit(main())
