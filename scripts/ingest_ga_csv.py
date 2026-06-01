#!/usr/bin/env python3
"""Parse a GA4 "Reports snapshot" CSV export into ga-data.js for the dashboard.

The snapshot export is a single CSV containing several stacked tables, each
preceded by `#` comment lines and a header row, separated by blank lines.
We extract:
  - Daily Active users      (Nth day, Active users)        -> monthly trend
  - Daily New users         (Nth day, New users)           -> monthly trend
  - Avg engagement / user   (Nth day, Average engagement..)-> weighted KPI
  - Sessions by channel     (Session primary channel ...)  -> traffic sources
  - New users by channel    (First user primary channel..) -> traffic sources
  - Top pages               (Page title and screen class)  -> top pages
  - Key events              (Event name, Key events)       -> conversions
  - Country (Country ID)                                   -> total active users

Output: ga-data.js  (window.GA_DATA = {...})

Usage: python3 scripts/ingest_ga_csv.py [path-to-snapshot.csv]
"""
from __future__ import annotations

import csv
import datetime as dt
import io
import json
import os
import sys
from collections import OrderedDict
from typing import Dict, List, Optional, Tuple

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DEFAULT_INPUT = os.path.join(ROOT, "Reports_snapshot.csv")
OUTPUT_JS = os.path.join(ROOT, "ga-data.js")


def to_num(s: str):
    s = (s or "").strip().replace(",", "")
    if s == "":
        return None
    try:
        v = float(s)
        return int(v) if v.is_integer() else v
    except ValueError:
        return None


def parse_blocks(text: str) -> List[Dict]:
    """Split the export into blocks. Each block keeps its `#` meta comments,
    a header row, and the list of data rows (parsed via csv to handle quotes)."""
    blocks: List[Dict] = []
    cur_meta: List[str] = []
    cur_lines: List[str] = []
    header: Optional[str] = None

    def flush():
        nonlocal header, cur_lines, cur_meta
        if header is not None:
            rows = list(csv.reader(io.StringIO("\n".join(cur_lines)))) if cur_lines else []
            cols = next(csv.reader(io.StringIO(header)))
            blocks.append({"meta": cur_meta, "header": cols, "rows": rows})
        header = None
        cur_lines = []
        cur_meta = []

    for raw in text.splitlines():
        line = raw.rstrip("\n")
        if line.strip() == "":
            flush()
            continue
        if line.lstrip().startswith("#"):
            if header is not None:
                # A new section starting; flush the previous one first.
                flush()
            cur_meta.append(line.strip().lstrip("#").strip())
            continue
        if header is None:
            header = line
        else:
            cur_lines.append(line)
    flush()
    return blocks


def block_start_date(meta: List[str]) -> Optional[dt.date]:
    for m in meta:
        if m.lower().startswith("start date:"):
            d = m.split(":", 1)[1].strip()
            try:
                return dt.date(int(d[0:4]), int(d[4:6]), int(d[6:8]))
            except (ValueError, IndexError):
                return None
    return None


def find_block(blocks, col0, col1=None):
    for b in blocks:
        h = [c.strip().lower() for c in b["header"]]
        if not h:
            continue
        if h[0].startswith(col0.lower()) and (col1 is None or (len(h) > 1 and h[1].startswith(col1.lower()))):
            return b
    return None


def daily_series(block) -> List[Tuple[int, Optional[float]]]:
    out = []
    for r in block["rows"]:
        if len(r) < 2:
            continue
        idx = to_num(r[0])
        val = to_num(r[1])
        if idx is None:
            continue
        out.append((int(idx), val))
    return out


CHANNEL_ORDER_FALLBACK = 999


def main() -> int:
    inp = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_INPUT
    if not os.path.exists(inp):
        print(f"Missing input CSV: {inp}", file=sys.stderr)
        return 1

    with open(inp, "r", encoding="utf-8-sig") as f:
        text = f.read()

    blocks = parse_blocks(text)

    # ── Daily series → monthly trend ──
    active_block = find_block(blocks, "Nth day", "Active users")
    new_block = find_block(blocks, "Nth day", "New users")
    eng_block = find_block(blocks, "Nth day", "Average engagement")

    start = block_start_date(active_block["meta"]) if active_block else None
    if start is None:
        start = dt.date(2025, 1, 1)

    monthly_new: "OrderedDict[str,int]" = OrderedDict()
    monthly_active: "OrderedDict[str,int]" = OrderedDict()

    def add_monthly(series, target):
        for idx, val in series:
            if val is None:
                continue
            d = start + dt.timedelta(days=idx)
            mk = f"{d.year:04d}-{d.month:02d}"
            target[mk] = target.get(mk, 0) + int(round(val))

    if new_block:
        add_monthly(daily_series(new_block), monthly_new)
    if active_block:
        add_monthly(daily_series(active_block), monthly_active)

    months = sorted(set(list(monthly_new.keys()) + list(monthly_active.keys())))
    monthly = {
        "months": months,
        "new_users": [monthly_new.get(m, 0) for m in months],
        "active_users": [monthly_active.get(m, 0) for m in months],
    }

    # Weighted average engagement time (seconds) per active user
    avg_engagement = None
    if eng_block and active_block:
        eng = dict(daily_series(eng_block))
        act = dict(daily_series(active_block))
        num = 0.0
        den = 0.0
        for idx, a in act.items():
            e = eng.get(idx)
            if e is None or a is None:
                continue
            num += e * a
            den += a
        if den:
            avg_engagement = round(num / den, 1)

    # ── Channels: merge sessions + new users ──
    sess_block = find_block(blocks, "Session primary channel")
    nu_block = find_block(blocks, "First user primary channel")
    channels: "OrderedDict[str,Dict]" = OrderedDict()
    if sess_block:
        for r in sess_block["rows"]:
            if len(r) < 2:
                continue
            channels.setdefault(r[0].strip(), {"name": r[0].strip(), "sessions": 0, "new_users": 0})
            channels[r[0].strip()]["sessions"] = to_num(r[1]) or 0
    if nu_block:
        for r in nu_block["rows"]:
            if len(r) < 2:
                continue
            channels.setdefault(r[0].strip(), {"name": r[0].strip(), "sessions": 0, "new_users": 0})
            channels[r[0].strip()]["new_users"] = to_num(r[1]) or 0
    channel_list = sorted(channels.values(), key=lambda c: c["sessions"], reverse=True)
    total_sessions = sum(c["sessions"] for c in channel_list)
    total_new_users = sum(c["new_users"] for c in channel_list)

    # ── Total active users from country breakdown ──
    country_block = find_block(blocks, "Country ID", "Active users")
    total_active = 0
    if country_block:
        for r in country_block["rows"]:
            if len(r) >= 2:
                total_active += to_num(r[1]) or 0

    # ── Top pages (dedup by leading title segment) ──
    pages_block = find_block(blocks, "Page title and screen class", "Views")
    page_totals: "OrderedDict[str,int]" = OrderedDict()
    if pages_block:
        for r in pages_block["rows"]:
            if len(r) < 2:
                continue
            raw_title = r[0].strip()
            views = to_num(r[1]) or 0
            # Use the distinctive leading segment before the first pipe.
            name = raw_title.split("|")[0].strip() or raw_title
            page_totals[name] = page_totals.get(name, 0) + views
    # Drop obvious non-pages
    SKIP = {"Page not found", "trafficheap.com"}
    top_pages = [
        {"title": k, "views": v}
        for k, v in sorted(page_totals.items(), key=lambda kv: kv[1], reverse=True)
        if k not in SKIP
    ][:12]

    # ── Key events (conversions) ──
    # Prefer the "top performing key events" block (header: Event name, Key events)
    ke_block = find_block(blocks, "Event name", "Key events")
    key_events = []
    if ke_block:
        for r in ke_block["rows"]:
            if len(r) < 2:
                continue
            c = to_num(r[1])
            if c is None:
                continue
            key_events.append({"name": r[0].strip(), "count": c})
    key_events.sort(key=lambda e: e["count"], reverse=True)
    total_key_events = sum(e["count"] for e in key_events)

    start_iso = start.isoformat()
    end_block = active_block or new_block
    end_iso = None
    if end_block:
        for m in end_block["meta"]:
            if m.lower().startswith("end date:"):
                d = m.split(":", 1)[1].strip()
                try:
                    end_iso = dt.date(int(d[0:4]), int(d[4:6]), int(d[6:8])).isoformat()
                except (ValueError, IndexError):
                    pass

    out = {
        "generated_at": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "property": "Encore Funding - GA4 (gov.encore-funding.com)",
        "date_range": {"start": start_iso, "end": end_iso},
        "totals": {
            "active_users": total_active,
            "new_users": total_new_users,
            "sessions": total_sessions,
            "key_events": total_key_events,
            "avg_engagement_seconds": avg_engagement,
        },
        "monthly": monthly,
        "channels": channel_list,
        "top_pages": top_pages,
        "key_events": key_events,
    }

    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write("window.GA_DATA = " + json.dumps(out, ensure_ascii=False) + ";\n")

    print(f"Wrote {OUTPUT_JS}")
    print(f"  range: {start_iso} -> {end_iso}")
    print(f"  totals: active={total_active:,} new={total_new_users:,} "
          f"sessions={total_sessions:,} key_events={total_key_events:,} "
          f"avg_eng={avg_engagement}s")
    print(f"  months: {len(months)}  channels: {len(channel_list)}  "
          f"top_pages: {len(top_pages)}  key_events: {len(key_events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
