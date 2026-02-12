#!/usr/bin/env python3
"""
Builds a browser-friendly dataset for the Encore HTML reports.

Inputs:
  - Encore_Combined_Report.csv

Outputs:
  - report-data.js (window.REPORT_DATA = {...})
  - scripts/youtube_publish_dates_cache.json (cache; safe to keep local)

Notes:
  - Prefers real YouTube publish dates when Date is missing and Link is YouTube.
  - Falls back to inferred date (first day of Report Month) when needed.
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INPUT_CSV = os.path.join(ROOT, "Encore_Combined_Report.csv")
OUTPUT_JS = os.path.join(ROOT, "report-data.js")
CACHE_JSON = os.path.join(ROOT, "scripts", "youtube_publish_dates_cache.json")


MONTHS_MAP = {
    "jan": 1,
    "january": 1,
    "feb": 2,
    "february": 2,
    "mar": 3,
    "march": 3,
    "apr": 4,
    "april": 4,
    "may": 5,
    "jun": 6,
    "june": 6,
    "jul": 7,
    "july": 7,
    "aug": 8,
    "august": 8,
    "sep": 9,
    "sept": 9,
    "september": 9,
    "oct": 10,
    "october": 10,
    "nov": 11,
    "november": 11,
    "dec": 12,
    "december": 12,
}


def month_key(d: dt.date) -> str:
    return f"{d.year:04d}-{d.month:02d}"


def parse_report_month(s: str) -> Optional[dt.date]:
    # Example: "December 2025"
    if not s:
        return None
    parts = s.strip().split()
    if len(parts) != 2:
        return None
    m = MONTHS_MAP.get(parts[0].strip().lower())
    try:
        y = int(parts[1])
    except ValueError:
        return None
    if not m:
        return None
    return dt.date(y, m, 1)


def parse_human_date(s: str) -> Optional[dt.date]:
    # Examples:
    # - "9 Apr 2025"
    # - "30 Sept 2025"
    # - "9 July 2025"
    if not s:
        return None
    s = s.strip()
    if not s:
        return None
    parts = s.replace(",", "").split()
    if len(parts) != 3:
        return None
    try:
        day = int(parts[0])
    except ValueError:
        return None
    m = MONTHS_MAP.get(parts[1].strip().lower())
    if not m:
        return None
    try:
        year = int(parts[2])
    except ValueError:
        return None
    try:
        return dt.date(year, m, day)
    except ValueError:
        return None


YOUTUBE_ID_RE = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|shorts/|embed/))([A-Za-z0-9_-]{6,})"
)

STUDIO_ID_RE = re.compile(
    r"studio\.youtube\.com/video/([A-Za-z0-9_-]{6,})"
)


def normalize_youtube_url(url: str) -> Optional[str]:
    if not url:
        return None
    u = url.strip()
    if not u:
        return None

    # Extract video ID from studio links
    if "studio.youtube.com" in u:
        sm = STUDIO_ID_RE.search(u)
        if sm:
            return f"https://www.youtube.com/watch?v={sm.group(1)}"
        return None

    m = YOUTUBE_ID_RE.search(u)
    if not m:
        # Might be a watch URL with extra params
        try:
            parsed = urllib.parse.urlparse(u)
            if "youtube.com" in parsed.netloc and parsed.path == "/watch":
                qs = urllib.parse.parse_qs(parsed.query)
                vid = (qs.get("v") or [None])[0]
                if vid:
                    return f"https://www.youtube.com/watch?v={vid}"
        except Exception:
            return None
        return None
    vid = m.group(1)
    return f"https://www.youtube.com/watch?v={vid}"


PUBLISH_DATE_REGEXES = [
    re.compile(r'"publishDate"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'"uploadDate"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'itemprop="datePublished"\s+content="(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'itemprop="uploadDate"\s+content="(\d{4}-\d{2}-\d{2})"'),
]


def fetch_url_text(url: str, timeout_s: int = 20) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        # YouTube pages can be large; we only need the first chunk usually,
        # but some metadata appears later. Read up to ~2MB.
        data = resp.read(2_000_000)
    try:
        return data.decode("utf-8", errors="ignore")
    except Exception:
        return data.decode(errors="ignore")


def extract_publish_date(html: str) -> Optional[dt.date]:
    for rx in PUBLISH_DATE_REGEXES:
        m = rx.search(html)
        if m:
            try:
                return dt.date.fromisoformat(m.group(1))
            except ValueError:
                continue
    return None


def load_cache() -> Dict[str, str]:
    if not os.path.exists(CACHE_JSON):
        return {}
    try:
        with open(CACHE_JSON, "r", encoding="utf-8") as f:
            d = json.load(f)
        if isinstance(d, dict):
            return {str(k): str(v) for k, v in d.items()}
        return {}
    except Exception:
        return {}


def save_cache(cache: Dict[str, str]) -> None:
    os.makedirs(os.path.dirname(CACHE_JSON), exist_ok=True)
    with open(CACHE_JSON, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, sort_keys=True)


def youtube_publish_date(url: str, cache: Dict[str, str]) -> Optional[dt.date]:
    norm = normalize_youtube_url(url)
    if not norm:
        return None

    if norm in cache:
        try:
            return dt.date.fromisoformat(cache[norm])
        except ValueError:
            pass

    # 1) Fast path: scrape the watch HTML for common microformat fields
    try:
        html = fetch_url_text(norm)
    except Exception:
        html = ""
    d = extract_publish_date(html) if html else None
    if d:
        cache[norm] = d.isoformat()
        return d

    # 2) Fallback: yt-dlp extraction (no API key required)
    ytdlp = shutil.which("yt-dlp")
    if not ytdlp:
        for p in (
            os.path.expanduser("~/Library/Python/3.9/bin/yt-dlp"),
            os.path.expanduser("~/.local/bin/yt-dlp"),
        ):
            if os.path.exists(p):
                ytdlp = p
                break

    if ytdlp:
        try:
            cp = subprocess.run(
                [ytdlp, "--no-warnings", "--skip-download", "--print", "%(upload_date)s", norm],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                timeout=30,
                check=False,
            )
            out = (cp.stdout or "").strip()
            if re.fullmatch(r"\d{8}", out):
                d = dt.date(int(out[0:4]), int(out[4:6]), int(out[6:8]))
                cache[norm] = d.isoformat()
                return d
        except Exception:
            pass
    # Cache negative result lightly to avoid repeated fetches in one run
    cache[norm] = ""
    return None


def parse_int(s: Any) -> Optional[int]:
    if s is None:
        return None
    if isinstance(s, int):
        return s
    t = str(s).strip()
    if t == "" or t == "—":
        return None
    # remove commas
    t = t.replace(",", "")
    try:
        return int(float(t))
    except ValueError:
        return None


DATE_PRIORITY = {
    "provided": 3,
    "youtube_publish": 2,
    "inferred_report_month": 1,
    "unknown": 0,
}


def dedup_key(item: Dict[str, Any]) -> Tuple:
    channel = (item.get("channel") or "").strip()
    dtype = (item.get("type") or "").strip()
    title = (item.get("title") or "").strip()
    link = (item.get("link") or "").strip()
    date_iso = item.get("date_iso") or ""
    # Normalize YouTube URLs so youtu.be, youtube.com/watch, and studio links
    # for the same video produce the same key
    norm_link = link
    if channel.lower() == "youtube" and link:
        nl = normalize_youtube_url(link)
        if nl:
            norm_link = nl
    if not norm_link:
        if not title:
            # FHC webinars: empty title+link, use date to distinguish events
            return (channel, dtype, title, norm_link, date_iso)
        if channel.lower() in ("linkedin", "instagram"):
            # LinkedIn/Instagram: truncated titles can collide; use date
            return (channel, dtype, title, norm_link, date_iso)
    # YouTube videos with same title = same video across report months
    return (channel, dtype, title, norm_link)


def month_range(start_ym: str, end_ym: str) -> List[str]:
    sy, sm = map(int, start_ym.split("-"))
    ey, em = map(int, end_ym.split("-"))
    out = []
    y, m = sy, sm
    while (y, m) <= (ey, em):
        out.append(f"{y:04d}-{m:02d}")
        m += 1
        if m == 13:
            m = 1
            y += 1
    return out


def main() -> int:
    if not os.path.exists(INPUT_CSV):
        print(f"Missing input CSV: {INPUT_CSV}", file=sys.stderr)
        return 1

    cache = load_cache()
    items_by_key: Dict[Tuple, Dict[str, Any]] = {}

    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            channel = (row.get("Channel") or "").strip()
            dtype = (row.get("Data Type") or "").strip()
            title = (row.get("Video/Post Title") or "").strip()
            link = (row.get("Link") or "").strip()

            date_raw = (row.get("Date") or "").strip()
            report_month_raw = (row.get("Report Month") or "").strip()

            d: Optional[dt.date] = parse_human_date(date_raw)
            date_source = "unknown"

            if d:
                date_source = "provided"
            else:
                # Try YouTube publish date
                if channel.lower() == "youtube" and link:
                    try:
                        yd = youtube_publish_date(link, cache)
                    except Exception:
                        yd = None
                    if yd:
                        d = yd
                        date_source = "youtube_publish"

            if not d:
                rm = parse_report_month(report_month_raw)
                if rm:
                    d = rm
                    date_source = "inferred_report_month"

            # Still none: keep as None but mark unknown; will land in _nodate
            date_iso = d.isoformat() if d else ""
            mkey = month_key(d) if d else "_nodate"

            raw_impressions = parse_int(row.get("Impressions"))
            raw_views = parse_int(row.get("Views"))
            raw_engagements = parse_int(row.get("Engagements"))
            raw_clicks = parse_int(row.get("Clicks"))

            impressions = raw_impressions
            views = raw_views
            engagements = raw_engagements
            clicks = raw_clicks

            # The source PDFs didn't have a "views" column for LinkedIn posts, but the extraction
            # often landed "Impressions" into the CSV "Views" column and "Engagements" into the
            # CSV "Impressions" column. Fix that common case.
            if channel.lower() == "linkedin" and ("post" in dtype.lower() or dtype.lower() == "post"):
                if engagements is None and views is not None and impressions is not None and views > impressions:
                    impressions, engagements, views = views, impressions, None

            # Instagram: map interactions to engagements, Notes column to impressions
            if channel.lower() == "instagram":
                interactions_val = parse_int(row.get("Interactions"))
                notes_val = parse_int(row.get("Notes"))
                if interactions_val is not None and engagements is None:
                    engagements = interactions_val
                if notes_val is not None and impressions is None:
                    impressions = notes_val

            item = {
                "channel": channel,
                "type": dtype,
                "title": title,
                "link": link,
                "date_raw": date_raw,
                "date_iso": date_iso,
                "month": mkey,
                "date_source": date_source,
                "impressions": impressions,
                "views": views,
                "engagements": engagements,
                "clicks": clicks,
                "attendees": parse_int(row.get("Attendees")),
                "chat_count": parse_int(row.get("Chat Count")),
                "email_sends": parse_int(row.get("Email Sends")),
                "article_views": parse_int(row.get("Article Views")),
                "interactions": parse_int(row.get("Interactions")),
                "report_month": report_month_raw,
            }

            k = dedup_key(item)
            prev = items_by_key.get(k)
            if not prev:
                items_by_key[k] = item
            else:
                p1 = DATE_PRIORITY.get(prev.get("date_source", "unknown"), 0)
                p2 = DATE_PRIORITY.get(item.get("date_source", "unknown"), 0)
                prev_imp = prev.get("impressions") or 0
                new_imp = item.get("impressions") or 0

                if p2 > p1:
                    # New item has better date, but check if prev has much better metrics
                    if prev_imp > new_imp * 10 and prev_imp > 100:
                        # Adopt the better date onto the higher-metric item
                        prev["date_raw"] = item.get("date_raw") or prev.get("date_raw")
                        prev["date_iso"] = item.get("date_iso") or prev.get("date_iso")
                        prev["month"] = item.get("month") or prev.get("month")
                        prev["date_source"] = item.get("date_source")
                    else:
                        items_by_key[k] = item
                elif p2 == p1:
                    if new_imp > prev_imp:
                        items_by_key[k] = item

    # Persist cache (including successes and blanks)
    # Remove blank entries older cache? keep for now.
    save_cache(cache)

    # ── Reconcile inferred dates ──
    # Items with inferred_report_month dates are often duplicate snapshots
    # from a different report month (e.g., July 2025 report re-lists posts
    # originally from April-June). Match them to properly-dated items by
    # title prefix and merge: keep higher metrics, adopt real date, remove dup.

    def clean_title(t: str) -> str:
        """Strip trailing ellipsis/dots for prefix matching."""
        t = t.strip().lower()
        t = t.rstrip(".")
        return t

    # Index properly-dated items by (channel, clean_title_prefix)
    # Use multiple prefix lengths to handle different truncation levels
    dated_items: List[Tuple[Any, Dict[str, Any]]] = [
        (k, it) for k, it in items_by_key.items()
        if it.get("date_source") in ("provided", "youtube_publish")
    ]

    keys_to_remove: set = set()
    for k, it in list(items_by_key.items()):
        if k in keys_to_remove:
            continue
        if it.get("date_source") != "inferred_report_month":
            continue
        title = (it.get("title") or "").strip()
        if not title:
            continue

        ch = (it.get("channel") or "").strip().lower()
        ct = clean_title(title)

        # Find matches: same channel, one title starts with the other
        best_mk, best_mit = None, None
        for mk, mit in dated_items:
            if mk in keys_to_remove:
                continue
            if (mit.get("channel") or "").strip().lower() != ch:
                continue
            mt = clean_title(mit.get("title") or "")
            if not mt or len(mt) < 8:
                continue
            # Check if one is a prefix of the other (handle different truncations)
            shorter = min(len(ct), len(mt))
            if shorter < 8:
                continue
            prefix_len = min(shorter, 10)
            if ct[:prefix_len] == mt[:prefix_len]:
                # Prefer same type
                if best_mit is None:
                    best_mk, best_mit = mk, mit
                elif mit.get("type") == it.get("type") and best_mit.get("type") != it.get("type"):
                    best_mk, best_mit = mk, mit

        if best_mit is None:
            continue

        inf_imp = it.get("impressions") or 0
        dated_imp = best_mit.get("impressions") or 0

        if inf_imp >= dated_imp:
            # Inferred item has better metrics: adopt real date, remove dated dup
            it["date_iso"] = best_mit["date_iso"]
            it["date_raw"] = best_mit.get("date_raw", "")
            it["month"] = best_mit.get("month", it["month"])
            it["date_source"] = "matched_" + best_mit["date_source"]
            if best_mit.get("link") and not it.get("link"):
                it["link"] = best_mit["link"]
            keys_to_remove.add(best_mk)
        else:
            # Dated item has better metrics: remove the inferred dup
            keys_to_remove.add(k)

    for k in keys_to_remove:
        items_by_key.pop(k, None)

    items = list(items_by_key.values())

    # ── Fallback links ──
    # Items without a direct link get a platform-level URL so every row is clickable.
    PLATFORM_LINKS = {
        "linkedin": "https://www.linkedin.com/company/govcongiants",
        "instagram": "https://www.instagram.com/govcongiants/",
        "fhc": "https://federalhelpcenter.com/",
        "podcast": "https://open.spotify.com/show/1XZCaN0VDP9zQSNYS1syoC",
    }
    for it in items:
        link = (it.get("link") or "").strip()
        if link:
            it["link_type"] = "direct"
        else:
            ch = (it.get("channel") or "").strip().lower()
            fallback = PLATFORM_LINKS.get(ch, "")
            if fallback:
                it["link"] = fallback
                it["link_type"] = "platform"
            else:
                it["link_type"] = "none"

    # Sort items by date then channel
    def sort_key(it: Dict[str, Any]) -> Tuple[str, str, str]:
        return (it.get("date_iso") or "9999-99-99", it.get("channel") or "", it.get("title") or "")

    items.sort(key=sort_key)

    months = month_range("2025-03", "2026-01")

    # Aggregates
    agg: Dict[str, Any] = {}
    METRIC_KEYS = ("impressions", "views", "engagements", "clicks", "attendees", "chat_count", "email_sends", "article_views")

    for m in months:
        agg[m] = {
            "totals": {k: 0 for k in METRIC_KEYS},
            "by_channel": {},
        }
        agg[m]["totals"]["items"] = 0

    for it in items:
        m = it.get("month") or "_nodate"
        if m not in agg:
            continue  # ignore out-of-range
        agg[m]["totals"]["items"] += 1
        for k in METRIC_KEYS:
            v = it.get(k)
            if isinstance(v, int):
                agg[m]["totals"][k] += v
        ch = it.get("channel") or "Unknown"
        if ch not in agg[m]["by_channel"]:
            agg[m]["by_channel"][ch] = {k: 0 for k in METRIC_KEYS}
            agg[m]["by_channel"][ch]["items"] = 0
        agg[m]["by_channel"][ch]["items"] += 1
        for k in METRIC_KEYS:
            v = it.get(k)
            if isinstance(v, int):
                agg[m]["by_channel"][ch][k] += v

    # Flag empty months
    for m in months:
        if agg[m]["totals"]["items"] == 0:
            agg[m]["is_empty"] = True
            agg[m]["note"] = "No new content published this month"

    # Series for charts
    series = {
        "months": months,
        "impressions": [agg[m]["totals"]["impressions"] for m in months],
        "views": [agg[m]["totals"]["views"] for m in months],
        "engagements": [agg[m]["totals"]["engagements"] for m in months],
        "clicks": [agg[m]["totals"]["clicks"] for m in months],
        "attendees": [agg[m]["totals"]["attendees"] for m in months],
        "chat_count": [agg[m]["totals"]["chat_count"] for m in months],
        "items": [agg[m]["totals"]["items"] for m in months],
    }

    out = {
        "generated_at": dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
        "months": months,
        "items": items,
        "aggregates": agg,
        "series": series,
    }

    js = "window.REPORT_DATA = " + json.dumps(out, ensure_ascii=False) + ";\n"
    with open(OUTPUT_JS, "w", encoding="utf-8") as f:
        f.write(js)

    print(f"Wrote {OUTPUT_JS} with {len(items)} items.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

