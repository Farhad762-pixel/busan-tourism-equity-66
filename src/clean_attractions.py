"""Export attraction fields to UTF-8 CSV without changing the raw JSON."""

import csv
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


def main():
    records = json.loads(SOURCE.read_text(encoding="utf-8-sig"))["getAttractionEn"]["item"]
    seen = set()
    rows = []
    for record in records:
        # Compare the complete raw record, including fields omitted from the CSV.
        key = json.dumps(record, sort_keys=True, ensure_ascii=False)
        if key in seen:
            continue
        seen.add(key)
        rows.append({target: record.get(source, "") for source, target in FIELDS.items()})

    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    with DESTINATION.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(FIELDS.values()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows and {len(FIELDS)} columns to {DESTINATION}")
    print(f"Removed {len(records) - len(rows)} exact duplicate records")


if __name__ == "__main__":
    main()
