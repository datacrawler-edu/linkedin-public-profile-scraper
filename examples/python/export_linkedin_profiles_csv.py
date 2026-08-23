"""Flatten saved Actor JSON output into a useful CSV view.

Usage:
    python export_linkedin_profiles_csv.py data/sample-output.json > profiles.csv
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any


FIELDS = [
    "success",
    "status",
    "inputUrl",
    "profileUrl",
    "publicIdentifier",
    "fullName",
    "headline",
    "location",
    "followers",
    "connections",
    "dataQuality",
    "error",
]


def row_from_item(item: dict[str, Any]) -> dict[str, Any]:
    profile = item.get("profile") or {}
    quality = item.get("dataQuality") or {}
    return {
        "success": item.get("success"),
        "status": item.get("status"),
        "inputUrl": item.get("inputUrl"),
        "profileUrl": item.get("profileUrl"),
        "publicIdentifier": item.get("publicIdentifier"),
        "fullName": profile.get("fullName"),
        "headline": profile.get("headline"),
        "location": profile.get("location"),
        "followers": profile.get("followers"),
        "connections": profile.get("connections"),
        "dataQuality": quality.get("level"),
        "error": item.get("error"),
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python export_linkedin_profiles_csv.py OUTPUT.json")

    items = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(items, list):
        raise SystemExit("The input JSON must contain a list of Dataset items.")

    writer = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for item in items:
        writer.writerow(row_from_item(item))


if __name__ == "__main__":
    main()
