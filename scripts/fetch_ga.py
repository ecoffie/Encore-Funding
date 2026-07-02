#!/usr/bin/env python3
"""Fetch live data from the GA4 Data API and write ga-data.js for the dashboard.

This is the automated replacement for ingest_ga_csv.py. It produces the same
ga-data.js shape the dashboard already consumes, PLUS month-by-month breakdowns
for channels, top pages, and key events (which the CSV snapshot could not give).

Auth (service account):
  - Set GA4_PROPERTY_ID   -> the numeric GA4 property id (e.g. 493820114)
  - Provide credentials one of two ways:
      * GA4_SA_KEY                  -> the full JSON of the service-account key
      * GOOGLE_APPLICATION_CREDENTIALS -> path to the key file on disk
  - Optional: GA4_START_DATE (YYYY-MM-DD, default 2025-03-01)

Run:
  pip install -r scripts/requirements.txt
  GA4_PROPERTY_ID=XX: python3 scripts/fetch_ga.py

Docs: see scripts/GA_SETUP.md
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys
import tempfile
from collections import OrderedDict
from typing import Dict, List, Optional

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUT_JS = os.path.join(ROOT, "ga-data.js")

PROPERTY_ID = os.environ.get("GA4_PROPERTY_ID", "").strip()
START_DATE = os.environ.get("GA4_START_DATE", "2025-03-01").strip()
PROPERTY_LABEL = os.environ.get(
    "GA4_PROPERTY_LABEL", "Encore Funding - GA4 (gov.encore-funding.com)"
)

# Pages whose titles are noise rather than real destinations.
SKIP_PAGES = {"Page not found", "trafficheap.com", "(not set)"}


def _import_client():
    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import (
            DateRange,
            Dimension,
            Metric,
            RunReportRequest,
        )
        from google.oauth2 import service_account
    except ImportError:
        print(
            "Missing deps. Run: pip install -r scripts/requirements.txt",
            file=sys.stderr,
        )
        raise
    return (
        BetaAnalyticsDataClient,
        DateRange,
        Dimension,
        Metric,
        RunReportRequest,
        service_account,
    )


def _credentials(service_account):
    """Build credentials from GA4_SA_KEY (inline JSON) or the default env var."""
    scopes = ["https://www.googleapis.com/auth/analytics.readonly"]
    raw = os.environ.get("GA4_SA_KEY", "").strip()
    if raw:
        info = json.loads(raw)
        return service_account.Credentials.from_service_account_info(info, scopes=scopes)
    keyfile = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
    if keyfile and os.path.exists(keyfile):
        return service_account.Credentials.from_service_account_file(keyfile, scopes=scopes)
    raise SystemExit(
        "No credentials. Set GA4_SA_KEY (inline JSON) or GOOGLE_APPLICATION_CREDENTIALS."
    )


def ym_to_key(ym: str) -> str:
    """GA4 'yearMonth' is 'YYYYMM' -> normalize to 'YYYY-MM'."""
    ym = (ym or "").strip()
    if len(ym) == 6 and ym.isdigit():
        return f"{ym[:4]}-{ym[4:]}"
    return ym


def to_num(v):
    try:
        f = float(v)
        return int(f) if f.is_integer() else f
    except (TypeError, ValueError):
        return 0


def clean_page_title(raw: str) -> str:
    name = (raw or "").split("|")[0].strip()
    return name or (raw or "").strip()


def main() -> int:
    if not PROPERTY_ID:
        print("GA4_PROPERTY_ID is required.", file=sys.stderr)
        return 1

    (
        BetaAnalyticsDataClient,
        DateRange,
        Dimension,
        Metric,
        RunReportRequest,
        service_account,
    ) = _import_client()

    creds = _credentials(service_account)
    client = BetaAnalyticsDataClient(credentials=creds)
    prop = f"properties/{PROPERTY_ID}"
    today = dt.date.today().isoformat()
    date_range = DateRange(start_date=START_DATE, end_date="today")

    def run(dimensions: List[str], metrics: List[str], limit: int = 100000):
        req = RunReportRequest(
            property=prop,
            date_ranges=[date_range],
            dimensions=[Dimension(name=d) for d in dimensions],
            metrics=[Metric(name=m) for m in metrics],
            limit=limit,
        )
        resp = client.run_report(req)
        out = []
        for row in resp.rows:
            dims = [d.value for d in row.dimension_values]
            mets = [to_num(m.value) for m in row.metric_values]
            out.append((dims, mets))
        return out

    # ── 1) Period totals ──
    tot = run([], ["activeUsers", "newUsers", "sessions", "keyEvents", "userEngagementDuration"])
    if tot:
        _, m = tot[0]
        total_active, total_new, total_sessions, total_key_events, eng_dur = m
    else:
        total_active = total_new = total_sessions = total_key_events = eng_dur = 0
    avg_engagement = round(eng_dur / total_active, 1) if total_active else None

    # ── 2) Monthly users / sessions / engagement ──
    rows = run(["yearMonth"], ["activeUsers", "newUsers", "sessions", "keyEvents", "userEngagementDuration"])
    monthly_map: "OrderedDict[str,Dict]" = OrderedDict()
    for dims, mets in sorted(rows, key=lambda r: r[0][0]):
        mk = ym_to_key(dims[0])
        a, nu, s, ke, ed = mets
        monthly_map[mk] = {
            "active_users": int(a),
            "new_users": int(nu),
            "sessions": int(s),
            "key_events": int(ke),
            "avg_engagement_seconds": round(ed / a, 1) if a else None,
        }
    months = list(monthly_map.keys())
    monthly = {
        "months": months,
        "new_users": [monthly_map[m]["new_users"] for m in months],
        "active_users": [monthly_map[m]["active_users"] for m in months],
        "sessions": [monthly_map[m]["sessions"] for m in months],
        "key_events": [monthly_map[m]["key_events"] for m in months],
    }

    # ── 3) Channels (period) + monthly channels ──
    ch_rows = run(["sessionDefaultChannelGroup"], ["sessions", "newUsers"])
    channels = sorted(
        ({"name": d[0], "sessions": int(mv[0]), "new_users": int(mv[1])} for d, mv in ch_rows),
        key=lambda c: c["sessions"],
        reverse=True,
    )
    mc_rows = run(["yearMonth", "sessionDefaultChannelGroup"], ["sessions", "newUsers"])
    monthly_channels: Dict[str, List[Dict]] = {}
    for d, mv in mc_rows:
        mk = ym_to_key(d[0])
        monthly_channels.setdefault(mk, []).append(
            {"name": d[1], "sessions": int(mv[0]), "new_users": int(mv[1])}
        )
    for mk in monthly_channels:
        monthly_channels[mk].sort(key=lambda c: c["sessions"], reverse=True)

    # ── 4) Top pages (period) + monthly pages ──
    pg_rows = run(["pageTitle"], ["screenPageViews"])
    page_totals: "OrderedDict[str,int]" = OrderedDict()
    for d, mv in pg_rows:
        name = clean_page_title(d[0])
        if name in SKIP_PAGES:
            continue
        page_totals[name] = page_totals.get(name, 0) + int(mv[0])
    top_pages = [
        {"title": k, "views": v}
        for k, v in sorted(page_totals.items(), key=lambda kv: kv[1], reverse=True)
    ][:12]

    mp_rows = run(["yearMonth", "pageTitle"], ["screenPageViews"])
    monthly_pages_acc: Dict[str, "OrderedDict[str,int]"] = {}
    for d, mv in mp_rows:
        mk = ym_to_key(d[0])
        name = clean_page_title(d[1])
        if name in SKIP_PAGES:
            continue
        monthly_pages_acc.setdefault(mk, OrderedDict())
        monthly_pages_acc[mk][name] = monthly_pages_acc[mk].get(name, 0) + int(mv[0])
    monthly_pages: Dict[str, List[Dict]] = {}
    for mk, acc in monthly_pages_acc.items():
        monthly_pages[mk] = [
            {"title": k, "views": v}
            for k, v in sorted(acc.items(), key=lambda kv: kv[1], reverse=True)
        ][:8]

    # ── 5) Key events (period) + monthly key events ──
    ke_rows = run(["eventName"], ["keyEvents"])
    key_events = sorted(
        ({"name": d[0], "count": int(mv[0])} for d, mv in ke_rows if int(mv[0]) > 0),
        key=lambda e: e["count"],
        reverse=True,
    )
    mke_rows = run(["yearMonth", "eventName"], ["keyEvents"])
    monthly_key_events: Dict[str, List[Dict]] = {}
    for d, mv in mke_rows:
        if int(mv[0]) <= 0:
            continue
        mk = ym_to_key(d[0])
        monthly_key_events.setdefault(mk, []).append({"name": d[1], "count": int(mv[0])})
    for mk in monthly_key_events:
        monthly_key_events[mk].sort(key=lambda e: e["count"], reverse=True)

    out = {
        "generated_at": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "property": PROPERTY_LABEL,
        "source": "ga4_data_api",
        "date_range": {"start": START_DATE, "end": today},
        "totals": {
            "active_users": int(total_active),
            "new_users": int(total_new),
            "sessions": int(total_sessions),
            "key_events": int(total_key_events),
            "avg_engagement_seconds": avg_engagement,
        },
        "monthly": monthly,
        "channels": channels,
        "top_pages": top_pages,
        "key_events": key_events,
        "monthly_channels": monthly_channels,
        "monthly_pages": monthly_pages,
        "monthly_key_events": monthly_key_events,
    }

    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write("window.GA_DATA = " + json.dumps(out, ensure_ascii=False) + ";\n")

    print(f"Wrote {OUTPUT_JS}")
    print(f"  range: {START_DATE} -> {today}  ({len(months)} months)")
    print(
        f"  totals: active={int(total_active):,} new={int(total_new):,} "
        f"sessions={int(total_sessions):,} key_events={int(total_key_events):,} "
        f"avg_eng={avg_engagement}s"
    )
    print(
        f"  channels={len(channels)} top_pages={len(top_pages)} "
        f"key_events={len(key_events)} monthly_breakdowns=yes"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
