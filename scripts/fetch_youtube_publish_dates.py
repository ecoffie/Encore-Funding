#!/usr/bin/env python3
"""
Pre-populates the YouTube publish dates cache for Encore report data.

Finds rows in Encore_Combined_Report.csv where:
  - Channel = Youtube
  - Date is missing
  - Link looks like a YouTube watch URL

Fetches each watch page, extracts publish date from embedded microformat JSON,
and caches results in youtube_publish_dates_cache.json.

Run this before build_report_data.py to avoid refetching. Uses Python stdlib only.
"""

from __future__ import annotations

import csv
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from typing import Dict, Optional


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
INPUT_CSV = os.path.join(ROOT, "Encore_Combined_Report.csv")
CACHE_JSON = os.path.join(os.path.dirname(__file__), "youtube_publish_dates_cache.json")

YOUTUBE_ID_RE = re.compile(
    r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|shorts/|embed/))([A-Za-z0-9_-]{6,})"
)

PUBLISH_DATE_REGEXES = [
    re.compile(r'"publishDate"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'"uploadDate"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'itemprop="datePublished"\s+content="(\d{4}-\d{2}-\d{2})"'),
    re.compile(r'itemprop="uploadDate"\s+content="(\d{4}-\d{2}-\d{2})"'),
]


def normalize_youtube_url(url: str) -> Optional[str]:
    if not url or not url.strip():
        return None
    u = url.strip()
    if "studio.youtube.com" in u:
        return None
    m = YOUTUBE_ID_RE.search(u)
    if not m:
        try:
            parsed = urllib.parse.urlparse(u)
            if "youtube.com" in parsed.netloc and parsed.path == "/watch":
                qs = urllib.parse.parse_qs(parsed.query)
                vid = (qs.get("v") or [None])[0]
                if vid:
                    return f"https://www.youtube.com/watch?v={vid}"
        except Exception:
            pass
        return None
    return f"https://www.youtube.com/watch?v={m.group(1)}"


def fetch_url_text(url: str, timeout_s: int = 20) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = resp.read(2_000_000)
    return data.decode("utf-8", errors="ignore")


def extract_publish_date(html: str) -> Optional[str]:
    for rx in PUBLISH_DATE_REGEXES:
        m = rx.search(html)
        if m:
            return m.group(1)
    return None


def load_cache() -> Dict[str, str]:
    if not os.path.exists(CACHE_JSON):
        return {}
    try:
        with open(CACHE_JSON, "r", encoding="utf-8") as f:
            d = json.load(f)
        if isinstance(d, dict):
            return {str(k): str(v) for k, v in d.items() if v}
        return {}
    except Exception:
        return {}


def save_cache(cache: Dict[str, str]) -> None:
    with open(CACHE_JSON, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, sort_keys=True)


def main() -> int:
    if not os.path.exists(INPUT_CSV):
        print(f"Missing input CSV: {INPUT_CSV}", file=sys.stderr)
        return 1

    cache = load_cache()
    to_fetch = []

    with open(INPUT_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            channel = (row.get("Channel") or "").strip()
            date_raw = (row.get("Date") or "").strip()
            link = (row.get("Link") or "").strip()
            if channel.lower() != "youtube" or date_raw or not link:
                continue
            norm = normalize_youtube_url(link)
            if not norm:
                continue
            if norm not in cache:
                to_fetch.append(norm)

    if not to_fetch:
        print("No new YouTube URLs to fetch. Cache is up to date.")
        return 0

    print(f"Fetching publish dates for {len(to_fetch)} YouTube URLs...")
    updated = 0
    for url in to_fetch:
        try:
            html = fetch_url_text(url)
            date_str = extract_publish_date(html)
            if date_str:
                cache[url] = date_str
                updated += 1
                print(f"  {url} -> {date_str}")
        except Exception as e:
            print(f"  {url} -> FAILED: {e}", file=sys.stderr)

    save_cache(cache)
    print(f"Cached {updated} new publish dates. Total entries: {len(cache)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
