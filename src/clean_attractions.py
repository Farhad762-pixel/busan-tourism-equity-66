"""Export attraction fields to UTF-8 CSV without changing the raw JSON."""

import csv
import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/raw/busan_attractions_raw_full.json"
DESTINATION = ROOT / "data/processed/busan_attractions.csv"
FIELDS = {
    "UC_SEQ": "uc_seq",
    "MAIN_TITLE": "main_title",
    "SUBTITLE": "subtitle",
    "GUGUN_NM": "district",
    "LAT": "latitude",
    "LNG": "longitude",
    "ADDR1": "address",
    "PLACE": "place",
    "TRFC_INFO": "transport_info",
    "HOMEPAGE_URL": "homepage_url",
    "USAGE_DAY_WEEK_AND_TIME": "opening_info",
    "USAGE_AMOUNT": "usage_amount",
    "MAIN_IMG_NORMAL": "image_url",
    "MAIN_IMG_THUMB": "thumbnail_url",
}


def export_attractions(source: Path, destination: Path):
    """Write a new file only; callers must explicitly choose a fresh destination."""
    records = json.loads(source.read_text(encoding="utf-8-sig"))["getAttractionEn"]["item"]
    seen = set()
    rows = []
    for record in records:
        # Compare the complete raw record, including fields omitted from the CSV.
        key = json.dumps(record, sort_keys=True, ensure_ascii=False)
        if key in seen:
            continue
        seen.add(key)
        rows.append({target: record.get(source, "") for source, target in FIELDS.items()})

    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(FIELDS.values()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows and {len(FIELDS)} columns to {destination}")
    print(f"Removed {len(records) - len(rows)} exact duplicate records")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=DESTINATION,
                        help="A new file; existing datasets are never overwritten")
    args = parser.parse_args()
    try:
        export_attractions(args.source, args.output)
    except (FileExistsError, FileNotFoundError, KeyError, json.JSONDecodeError) as error:
        parser.exit(1, f"Export failed: {error}. Choose an existing source and a fresh --output path.\n")


if __name__ == "__main__":
    main()
