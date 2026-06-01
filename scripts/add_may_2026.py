#!/usr/bin/env python3
"""One-off: append May 2026 items into report-data.js from Encore report.xlsx.

Surgical update — leaves existing curated items untouched, adds the new
2026-05 month, recomputes that month's aggregates, and extends the series.
"""
import datetime as dt
import json
import os

import openpyxl

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
XLSX = os.path.join(ROOT, "Encore report.xlsx")
JS = os.path.join(ROOT, "report-data.js")
PREFIX = "window.REPORT_DATA = "

TYPED = ["Sponsored Post", "Sponsored Video", "Webinar", "Custom Video",
         "Post", "Ad Spot", "Article", "Sponsored Episode"]
TARGET = "2026-05"

METRIC_KEYS = ("impressions", "views", "engagements", "clicks",
               "attendees", "chat_count", "email_sends", "article_views")


def to_int(v):
    if v is None:
        return None
    if isinstance(v, str):
        v = v.replace(",", "").strip()
        if not v:
            return None
        try:
            return int(float(v))
        except ValueError:
            return None
    try:
        return int(v)
    except (ValueError, TypeError):
        return None


def month_of(v):
    if isinstance(v, (dt.datetime, dt.date)):
        return f"{v.year:04d}-{v.month:02d}"
    return None


def iso(v):
    if isinstance(v, (dt.datetime, dt.date)):
        return f"{v.year:04d}-{v.month:02d}-{v.day:02d}"
    return ""


def is_url(v):
    return isinstance(v, str) and v.strip().lower().startswith("http")


def build_items():
    wb = openpyxl.load_workbook(XLSX, data_only=True)
    items = []
    for name in TYPED:
        ws = wb[name]
        rows = list(ws.iter_rows(values_only=True))
        for r in rows[1:]:
            if not any(x is not None for x in r):
                continue
            if month_of(r[0]) != TARGET:
                continue
            channel = (r[1] or "").strip()
            dtype = (r[2] or "").strip()
            date_val = r[3]
            title = (r[4] or "").strip()
            link = (r[9] or "").strip() if r[9] else ""
            # Quirk: podcast episode links live in the Attendees column.
            attendees = r[10]
            if not link and is_url(attendees):
                link = attendees.strip()
                attendees = None
            item = {
                "channel": channel,
                "type": dtype,
                "title": title,
                "link": link,
                "date_raw": iso(date_val),
                "date_iso": iso(date_val),
                "month": TARGET,
                "impressions": to_int(r[5]),
                "views": to_int(r[6]),
                "engagements": to_int(r[7]),
                "clicks": to_int(r[8]),
                "attendees": to_int(attendees),
                "chat_count": to_int(r[11]),
                "email_sends": to_int(r[12]),
                "article_views": to_int(r[13]),
                "interactions": to_int(r[14]),
            }
            items.append(item)
    items.sort(key=lambda it: (it["date_iso"], it["channel"], it["title"]))
    return items


def main():
    raw = open(JS, encoding="utf-8").read()
    body = raw[len(PREFIX):].rstrip().rstrip(";")
    d = json.loads(body)

    if TARGET in d["months"]:
        print(f"{TARGET} already present; aborting.")
        return 1

    new_items = build_items()
    print(f"Found {len(new_items)} items for {TARGET}")

    d["items"].extend(new_items)
    d["items"].sort(key=lambda it: (it.get("date_iso") or "9999-99-99",
                                    it.get("channel") or "",
                                    it.get("title") or ""))
    d["months"].append(TARGET)

    totals = {k: 0 for k in METRIC_KEYS}
    totals["items"] = 0
    by_channel = {}
    for it in new_items:
        totals["items"] += 1
        for k in METRIC_KEYS:
            v = it.get(k)
            if isinstance(v, int):
                totals[k] += v
        ch = it["channel"] or "Unknown"
        if ch not in by_channel:
            by_channel[ch] = {k: 0 for k in METRIC_KEYS}
            by_channel[ch]["items"] = 0
        by_channel[ch]["items"] += 1
        for k in METRIC_KEYS:
            v = it.get(k)
            if isinstance(v, int):
                by_channel[ch][k] += v
    d["aggregates"][TARGET] = {"totals": totals, "by_channel": by_channel}

    s = d["series"]
    s["months"].append(TARGET)
    s["impressions"].append(totals["impressions"])
    s["views"].append(totals["views"])
    s["engagements"].append(totals["engagements"])
    s["clicks"].append(totals["clicks"])
    s["attendees"].append(totals["attendees"])
    s["chat_count"].append(totals["chat_count"])
    s["items"].append(totals["items"])

    d["generated_at"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    with open(JS, "w", encoding="utf-8") as f:
        f.write(PREFIX + json.dumps(d, ensure_ascii=False) + ";\n")

    print(f"Updated {JS}: {len(d['items'])} items, {len(d['months'])} months.")
    print(f"{TARGET} totals: {totals}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
