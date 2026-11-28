#!/usr/bin/env python3
"""Resumable 2022-2025 KTO collection and validated CSV export.

Run from repository root:
  python3 scripts/collect_kto_full_panel.py --max-new 0
Existing raw JSON is never overwritten. Service keys are read by the existing
collector from a local environment variable and NEVER recorded here.
These are tourism-demand INDICES, not amounts in KRW or causal effects.
"""
import argparse
import csv
import json
import math
import re
import sys
import time
from collections import Counter
from pathlib import Path

from collect_kto_external_metrics import SERVICES, run

DISTRICTS = {
    "26110": "Jung-gu", "26140": "Seo-gu", "26170": "Dong-gu",
    "26200": "Yeongdo-gu", "26230": "Busanjin-gu", "26260": "Dongnae-gu",
    "26290": "Nam-gu", "26320": "Buk-gu", "26350": "Haeundae-gu",
    "26380": "Saha-gu", "26410": "Geumjeong-gu", "26440": "Gangseo-gu",
    "26470": "Yeonje-gu", "26500": "Suyeong-gu", "26530": "Sasang-gu",
    "26710": "Gijang-gun",
}
OUTPUT = Path.home() / "busan_research_private" / "kto_api"
COLUMNS = ["month", "district_code", "district", "indicator", "metric_code",
           "indicator_label_ko", "index_value", "unit", "source_file"]


def month_range(first, last):
    if not re.fullmatch(r"20\d{4}", first) or not re.fullmatch(r"20\d{4}", last):
        raise ValueError("Dates must be YYYYMM")
    year, month = int(first[:4]), int(first[4:])
    end_year, end_month = int(last[:4]), int(last[4:])
    if month not in range(1, 13) or end_month not in range(1, 13) or (year, month) > (end_year, end_month):
        raise ValueError("Invalid date range")
    while (year, month) <= (end_year, end_month):
        yield f"{year:04d}{month:02d}"
        year, month = (year + 1, 1) if month == 12 else (year, month + 1)


def check_json(path, month, district, indicator):
    """Validate provider record; return status, normalized row, reason."""
    try:
        obj = json.loads(path.read_text(encoding="utf-8"))
        response = obj["api_response"]["response"]
        header = response["header"]
        body = response["body"]
        if str(header.get("resultCode")) not in ("00", "0000", "0", "OK"):
            return "invalid", None, "provider resultCode not successful"
        items = body.get("items", {})
        if isinstance(items, dict):
            items = items.get("item", [])
        if isinstance(items, dict):
            items = [items]
        if not isinstance(items, list):
            return "invalid", None, "unknown items structure"
        total = int(body.get("totalCount", 0) or 0)
        if total == 0 and not items:
            return "empty", None, "no data for this request"
        if total > 0 and not items:
            return "invalid", None, "nonzero totalCount but missing items"
        if len(items) != 1:
            return "invalid", None, "expected exactly one indicator record"
        item = items[0]
        param, code = SERVICES[indicator][1:3]
        if str(item.get("baseYm")) != month or str(item.get("signguCd")) != district:
            return "invalid", None, "returned month/district does not match request"
        if str(item.get(param)) != code:
            return "invalid", None, "returned indicator code does not match request"
        value_key = "tarSvcDemIxVal" if param == "tarSvcDemIxCd" else "tarExpDsIxVal"
        label_key = "tarSvcDemIxNm" if param == "tarSvcDemIxCd" else "tarExpDsIxNm"
        value = float(str(item.get(value_key, "")).replace(",", ""))
        if not math.isfinite(value):
            return "invalid", None, "nonfinite value"
        return "valid", {
            "month": month, "district_code": district, "district": DISTRICTS[district],
            "indicator": indicator, "metric_code": code,
            "indicator_label_ko": str(item.get(label_key, "")),
            "index_value": format(value, ".12g"), "unit": "KTO index (NOT KRW)",
            "source_file": path.name,
        }, ""
    except (OSError, KeyError, ValueError, TypeError, AttributeError):
        return "invalid", None, "cannot parse provider response"


def make_audit(folder, start, end):
    records = []
    counts = Counter()
    problems = []
    for month in month_range(start, end):
        for district in DISTRICTS:
            for indicator in SERVICES:
                path = folder / f"{month}_{district}_{indicator}.json"
                if not path.exists():
                    counts["missing"] += 1
                    continue
                status, row, reason = check_json(path, month, district, indicator)
                counts[status] += 1
                if row:
                    records.append(row)
                if status == "invalid":
                    problems.append({"file": path.name, "issue": reason})
    csv_path = folder / f"kto_busan_indices_{start}_{end}.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(records)
    summary = {"period": [start, end], "expected": sum(1 for _ in month_range(start, end))*64,
               "status_counts": dict(counts), "validated_rows": len(records),
               "csv_file": str(csv_path), "first_100_invalid": problems[:100],
               "warning": "Values are indices, NOT KRW; not proof of changes caused by the recommender."}
    (folder / f"kto_audit_{start}_{end}.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def main():
    p = argparse.ArgumentParser(description="Collect all available 2022-2025 KTO monthly indices")
    p.add_argument("--start", default="202201")
    p.add_argument("--end", default="202512")
    p.add_argument("--max-new", type=int, default=200,
                   help="Cap new API calls in this run (0 means no cap, subject to service quota)")
    p.add_argument("--delay", type=float, default=1.2)
    p.add_argument("--audit-only", action="store_true")
    args = p.parse_args()
    if args.max_new < 0 or args.delay < 0.2:
        p.error("max-new must be nonnegative; delay must be >= 0.2 seconds")
    try:
        months = list(month_range(args.start, args.end))
    except ValueError as err:
        p.error(str(err))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    print(f"Expected: {len(months) * 64} records; existing JSON files are skipped.", flush=True)
    new = 0
    stop = ""
    if not args.audit_only:
        for month in months:
            for district in DISTRICTS:
                for indicator in SERVICES:
                    path = OUTPUT / f"{month}_{district}_{indicator}.json"
                    if path.exists():
                        continue
                    if args.max_new and new >= args.max_new:
                        stop = "Reached max-new; rerun the same command to continue."
                        break
                    try:
                        result = run(month, district, indicator, OUTPUT)
                        if result.get("status") != "DOWNLOADED_UNAUDITED":
                            raise RuntimeError("no successful download")
                        new += 1
                        state, _, reason = check_json(path, month, district, indicator)
                        if state == "invalid":
                            stop = f"Invalid response in {path.name}: {reason}; stopped for inspection."
                            break
                        if new % 20 == 0:
                            print(f"New: {new} | last: {month}, {district}, {indicator} ({state})", flush=True)
                        time.sleep(args.delay)
                    except (OSError, RuntimeError, FileExistsError):
                        # Never print raw exceptions; some URL errors include an API key.
                        stop = f"API error, quota or connectivity at {month}/{district}/{indicator}; resume later."
                        break
                if stop:
                    break
            if stop:
                break
    summary = make_audit(OUTPUT, args.start, args.end)
    print(json.dumps({"new_downloads_this_run": new, **summary,
                      "stop_reason": stop or "completed all requests"},
                     ensure_ascii=False, indent=2), flush=True)
    if summary["status_counts"].get("invalid", 0) or ("API error" in stop) or ("Invalid response" in stop):
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
