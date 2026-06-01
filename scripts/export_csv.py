#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import os
import re
from typing import Any, Dict, List


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IN_JS = os.path.join(ROOT, "report-data.js")
OUT_CSV = os.path.join(ROOT, "Encore_Report_Normalized.csv")


def load_report_data(js_path: str) -> Dict[str, Any]:
    with open(js_path, "r", encoding="utf-8") as f:
        s = f.read()
    m = re.search(r"window\.REPORT_DATA\s*=\s*(\{[\s\S]*\})\s*;\s*$", s)
    if not m:
        raise ValueError("Could not find window.REPORT_DATA JSON in report-data.js")
    return json.loads(m.group(1))


def main() -> int:
    if not os.path.exists(IN_JS):
        raise SystemExit(f"Missing: {IN_JS}. Run scripts/build_report_data.py first.")

    data = load_report_data(IN_JS)
    items: List[Dict[str, Any]] = data.get("items") or []

    cols = [
        "month",
        "date_iso",
        "date_source",
        "channel",
        "type",
        "title",
        "impressions",
        "views",
        "engagements",
        "clicks",
        "attendees",
        "chat_count",
        "email_sends",
        "article_views",
        "interactions",
        "link",
        "link_type",
        "report_month",
        "date_raw",
    ]

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for it in items:
            row = {k: it.get(k, "") for k in cols}
            w.writerow(row)

    print(f"Wrote {OUT_CSV} ({len(items)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

