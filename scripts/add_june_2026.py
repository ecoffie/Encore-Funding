#!/usr/bin/env python3
"""Add June 2026 Sponsored Video data from the CSV export to report-data.js."""
import csv, json, re, datetime as dt, os, sys

ROOT    = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_IN  = "/Users/kkii/Downloads/Encore report - Sponsored Video.csv"
JS_OUT  = os.path.join(ROOT, "report-data.js")
TARGET  = "2026-06"

MONTHS_MAP = {
    "january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
    "july":7,"august":8,"september":9,"october":10,"november":11,"december":12,
}

def month_of(s):
    s = (s or "").strip().lower()
    for name, num in MONTHS_MAP.items():
        if s.startswith(name):
            # Extract year: last 4-digit sequence
            m = re.search(r'(\d{4})', s)
            if m:
                return f"{m.group(1)}-{num:02d}"
    return None

def parse_date(s):
    s = (s or "").strip()
    for fmt in ("%d %b %Y", "%d %B %Y", "%Y-%m-%d"):
        try:
            return dt.datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None

def to_int(v):
    try:
        return int(str(v).strip().replace(",", "").split(".")[0])
    except (ValueError, TypeError):
        return None

def is_url(s):
    return (s or "").strip().startswith("http")

def build_items():
    items = []
    seen = set()  # dedup by (title, date)
    with open(CSV_IN, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mk = month_of(row.get("Report Month", ""))
            if mk != TARGET:
                continue

            title  = (row.get("Video/Post Title") or "").strip()
            date_s = parse_date(row.get("Date") or "")
            key    = (title, date_s)
            if key in seen:
                continue
            seen.add(key)

            link = (row.get("Link") or "").strip()
            if not is_url(link):
                link = None

            item = {
                "month":       TARGET,
                "channel":     (row.get("Channel") or "").strip(),
                "type":        (row.get("Data Type") or "").strip(),
                "title":       title,
                "date":        date_s,
                "link":        link,
                "impressions": to_int(row.get("Impressions")),
                "views":       to_int(row.get("Views")),
                "engagements": to_int(row.get("Engagements")),
                "clicks":      to_int(row.get("Clicks")),
                "attendees":   to_int(row.get("Attendees")),
                "email_sends": to_int(row.get("Email Sends")),
                "article_views": to_int(row.get("Article Views")),
                "interactions":  to_int(row.get("Interactions")),
            }
            items.append(item)
    return sorted(items, key=lambda x: x.get("date") or "")

def main():
    new_items = build_items()
    if not new_items:
        print(f"No items found for {TARGET} in {CSV_IN}")
        sys.exit(1)
    print(f"Found {len(new_items)} new items for {TARGET}:")
    for it in new_items:
        print(f"  [{it['channel']:8}] imp={it['impressions']} views={it['views']} :: {it['title'][:60]}")

    # Load existing data
    with open(JS_OUT, encoding="utf-8") as f:
        raw = f.read().split("=", 1)[1].strip().rstrip(";")
    d = json.loads(raw)

    # Guard: don't double-add
    existing_months = set(it.get("month") for it in d["items"])
    if TARGET in existing_months:
        print(f"\n{TARGET} items already exist in report-data.js. Remove them first if you want to re-add.")
        sys.exit(1)

    d["items"].extend(new_items)
    d["items"].sort(key=lambda x: (x.get("month") or "", x.get("date") or ""))

    if TARGET not in d["months"]:
        d["months"].append(TARGET)
        d["months"].sort()

    # Compute aggregates for June 2026
    def s(key):
        return sum(it.get(key) or 0 for it in new_items)

    totals = {
        "impressions":   s("impressions"),
        "views":         s("views"),
        "engagements":   s("engagements"),
        "clicks":        s("clicks"),
        "attendees":     s("attendees"),
        "chat_count":    0,
        "email_sends":   s("email_sends"),
        "article_views": s("article_views"),
        "items":         len(new_items),
    }
    by_channel = {}
    for it in new_items:
        ch = (it.get("channel") or "").strip()
        if ch not in by_channel:
            by_channel[ch] = {k: 0 for k in totals}
            by_channel[ch]["items"] = 0
        for k in totals:
            by_channel[ch][k] = by_channel[ch].get(k, 0) + (it.get(k) or 0)

    d["aggregates"][TARGET] = {"totals": totals, "by_channel": by_channel}

    # Extend series arrays
    if "series" in d:
        ser = d["series"]
        for key in ("impressions", "views", "engagements", "clicks", "items",
                    "attendees", "email_sends", "article_views"):
            if key in ser:
                ser[key].append(totals.get(key, 0))

    d["generated_at"] = dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    js = "window.REPORT_DATA = " + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + ";"
    with open(JS_OUT, "w", encoding="utf-8") as f:
        f.write(js + "\n")

    print(f"\n✓ report-data.js updated — {len(d['items'])} total items, {len(d['months'])} months")
    print(f"  June 2026 totals: impressions={totals['impressions']:,}  views={totals['views']:,}  items={totals['items']}")

if __name__ == "__main__":
    main()
