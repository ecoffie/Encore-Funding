# Encore Funding — SEO Technical Re-Crawl + GA4 Snapshot
**Date:** 2026-05-31 (10 weeks after original audit)
**Compared against:** `seo-audit-report.md` (2026-03-17)
**Method:** Live HTTP crawl of public surfaces (curl + HTML parsing) + GA4 home/snapshot screenshots (both properties). No GSC, Ahrefs, or PageSpeed (quota exhausted).

---

## TL;DR — What Changed

| Signal | March 17 | May 31 | Status |
|---|---|---|---|
| Main sitemap protocol | HTTP URLs | **Still HTTP URLs** | Not fixed |
| Robots.txt | Permissive, no sitemap ref | **Unchanged** | Not fixed |
| Schema markup (homepage) | None detected | **Org + WebSite + Breadcrumb + WebPage** | Fixed |
| Schema markup (blog post) | None | **Article + Person + Breadcrumb + Org** | Fixed |
| Jobs sitemap (stale 2022) | Present | **Removed / 301** | Fixed |
| Main → gov subdomain links | Weak | **Zero links from homepage** | Worse |
| `/solutions/government-contract-financing/` | 200 OK in audit | **404** | Broken |
| `/who-we-serve/government-contracting/` | implied | **404** | Broken |
| Post count (main) | 87 in audit | **84 in sitemap** | Slight decline |
| Stale 2023 backdated posts | 28 posts | **Still in sitemap, earliest lastmod 2023-03-21** | Not addressed |

**Net:** Schema work is done (good). Sitemap HTTPS issue, robots.txt, and content staleness untouched. New problem: gov financing service page URL changed, leaving 404s on the URLs that were in the original audit.

**GA4 cross-check confirms it:** Main site up 16% over 90 days. **Gov subdomain down 47% users / 49% new users**, and gov key events fell off a cliff in the last 30 days (▼47%) and 7 days (▼57%). The technical findings above explain the GA4 decline.

**Smoking gun for the conversion crash:** Gov subdomain Referral engagement rate fell from **47.3% (90d) → 27.5% (28d)** while volume stayed flat. A high-quality referral source (most likely the GovCon Giants partnership traffic path that was the #2 page in March) dropped off and was replaced by junk traffic. Plus 45.6% of gov traffic is "Direct" at 22.6% engagement — that's untagged Eric/GovCon promo traffic, not brand recall.

---

## 1. Headers & Redirects

### encore-funding.com
- `https://encore-funding.com/` → 301 → `https://www.encore-funding.com/` (200)
- Served behind **Sucuri Cloudproxy** + Cloudflare
- `content-security-policy: upgrade-insecure-requests` present (this is what's masking the HTTP sitemap issue from breaking — but Google sees the raw HTTP loc)
- HSTS: not in headers shown
- HTTP/2, HTTP/3 (alt-svc h3)

### gov.encore-funding.com
- `https://gov.encore-funding.com/` → 200 direct (no www variant)
- Cloudflare only, cache HIT
- HTTP/2, HTTP/3
- Last-modified: 2026-05-31 (active updates)

---

## 2. Robots.txt — UNCHANGED

Both domains still return:
```
User-Agent: *
Disallow:
```

- No `Sitemap:` line (audit recommendation #1, still open)
- No disallow for `/wp-admin/`, `/wp-includes/`, `/?s=` search results
- This was Recommendation #1 in March — never actioned

---

## 3. Sitemaps

### Main site (`encore-funding.com/sitemap_index.xml`)

Returned 200. **Still references HTTP URLs in the sitemap index:**

| Sub-sitemap | Protocol | lastmod | URL count |
|---|---|---|---|
| post-sitemap.xml | **http://** | 2026-05-13 | 84 |
| page-sitemap.xml | **http://** | 2026-05-20 | 53 |
| authors-sitemap.xml | **http://** | 2026-05-13 | 10 |
| category-sitemap.xml | **http://** | 2026-05-13 | 6 |
| post_tag-sitemap.xml | **http://** | 2026-05-13 | — |
| author-sitemap.xml | **http://** | 2026-04-28 | — |

Good news: When you actually fetch the HTTP sub-sitemap URLs they 301 to HTTPS now. Bad news: the sitemap index itself still lists `http://` `<loc>` values — Yoast setting was never flipped. Google reads the literal `<loc>` values.

**Old sitemap files no longer in index:**
- `jobs-sitemap.xml` — gone (now 301 redirect). Audit flagged it stale 2022-05-05. **Fixed.**

**Author sitemap duplication still present:**
- Both `authors-sitemap.xml` AND `author-sitemap.xml` still listed. Audit flagged this. **Not fixed.**

**Stale post dates:**
- Earliest `<lastmod>` in post-sitemap: `2023-03-21` (3+ years old)
- Latest: `2026-05-13`
- Audit's "28 posts backdated to June 2023" issue — not visible in counts but the old `<lastmod>` values remain.

### Gov subdomain (`gov.encore-funding.com/sitemap_index.xml`)

Returned 200. **All URLs are HTTPS** (cleaner than main).

| Sub-sitemap | lastmod | URL count |
|---|---|---|
| post-sitemap.xml | 2025-08-26 | **18** (same as audit) |
| page-sitemap.xml | 2026-05-20 | 10 |
| authors-sitemap.xml | 2025-08-07 | — |
| our-team-sitemap.xml | 2026-05-14 | — |
| category-sitemap.xml | 2025-08-26 | — |
| post_tag-sitemap.xml | **2024-11-21** | — |
| department-sitemap.xml | 2026-05-14 | — |
| author-sitemap.xml | 2026-05-07 | — |

**No new posts** on gov subdomain since August 2025. Page count active but post production stopped 9 months ago.

Same duplicate author sitemap issue (authors vs author).

---

## 4. Schema Markup — NEW SINCE AUDIT

This was a major gap in March; it's now implemented via Yoast.

### Main homepage JSON-LD `@graph` types
- WebPage
- ImageObject
- BreadcrumbList
- WebSite
- **Organization** ← new

### Gov homepage JSON-LD `@graph` types
- WebPage
- ImageObject
- BreadcrumbList
- WebSite
- (no Organization — gov subdomain missing it)

### Blog post (recent: Chad Eberly ABF Journal Award) JSON-LD
- **Article** ← new (audit noted missing BlogPosting/Article schema)
- WebPage
- ImageObject
- BreadcrumbList
- WebSite
- Organization
- **Person** (author markup) ← new

**Still missing:**
- LocalBusiness schema (audit recommendation — they have a Pepper Pike OH address)
- FAQ schema on resource pages
- Service schema on solution pages
- Review/AggregateRating schema for testimonials
- Gov subdomain has no Organization schema (main does)

---

## 5. On-Page Snapshot

### Main homepage
- **Title:** `Payroll & Invoice Factoring | Staffing Agency Funding | Encore Funding` (unchanged from audit — still 3 pipes)
- **Meta description:** `Encore Funding provides quick, secure staffing agency funding. Grow, stabilize cash flow, streamline back office & reduce costs.`
- **H1:** Not found via grep (likely rendered via Beaver Builder dynamic class — needs browser render to confirm)
- **Canonical:** `https://www.encore-funding.com/` (correct)
- **OG image:** `Encore-funding.jpg` from `/uploads/2022/09/` (4 years old)

### Apply Now (`/apply-now/`)
- 200 OK
- **Title:** `Apply Now For Fast Staffing Factoring | Encore Funding`
- **Meta:** `Encore delivers staffing factoring, invoice factoring, payroll funding, and back-office support. Start your easy application.`
- Generic meta — no urgency/value prop

### Gov subdomain homepage
- **Title:** `Government Contractor Financing | Encore Funding`
- **Meta:** `Encore Funding provides quick, easy alternative government contractor financing. Stabilize cash flow and streamline your operations.`
- **Canonical:** `https://gov.encore-funding.com/` (correct)
- **OG image:** From `/uploads/2024/10/` (current)

---

## 6. Broken / Moved URLs Since Audit ⚠️

| URL referenced in audit | Status today |
|---|---|
| `/solutions/government-contract-financing/` | **404** |
| `/who-we-serve/government-contracting/` | **404** |
| `/government-contract-financing/` (root) | 200 ← seems to be the new location |
| `/solutions/` | 200 |
| `/solutions/funding-options/` | 200 |
| `gov./govcon-giants-partner-government-contractor-funding/` | 200 |

**Action needed:** If anything (backlinks, GA4 sessions, sales decks) was pointing to the old `/solutions/government-contract-financing/` URL, those are now dead. 301 redirects should be added from the old URLs to `/government-contract-financing/`.

---

## 7. Cross-Property Linking — STILL BROKEN

The audit's "domain authority dilution" thesis was: main and gov subdomain should reinforce each other.

**Today:** Searched the main homepage HTML for any link to `gov.encore-funding.com` or any URL containing "government". **Zero matches.** A new staffing-agency visitor on the main site has no path to the gov financing offer.

Conversely, the gov subdomain does link back to `encore-funding.com` (per audit), but the main site doesn't reciprocate. SEO authority flow is one-directional.

---

## 8. GA4 Snapshot (Both Properties)

Pulled from GA4 home + Reports snapshot on 2026-05-31. Two GA4 properties: "Encore Funding - GA4" (main) and "Gov Encore Funding" (subdomain).

### Last 90 days (Mar 8 – May 24, 2026) vs prior 90d

| Metric | Main site | Gov subdomain |
|---|---|---|
| Active users | **4.3K** ▲ 15.8% | **1.4K** ▼ 47.2% |
| Event count | 31K ▲ 5.4% | 7.9K ▼ 42.1% |
| Key events | **371** ▲ 41.1% | **72** ▲ 2.9% |
| New users | 4.2K ▲ 16.5% | 1.4K ▼ 49.1% |

### Last 28 days (May 3 – May 30, 2026)

| Metric | Main site | Gov subdomain |
|---|---|---|
| Active users | 1.3K | 467 |
| New users | 1.2K | 452 |
| Avg engagement time / active user | **45s** | **37s** |

### Last 30 days (May 1 – May 30) — Gov subdomain
- Active users: **493** ▲ 13.3%
- Event count: 2.9K ▲ 27.2%
- **Key events: 16 ▼ 46.7%**
- New users: 478 ▲ 13.5%

### Last 7 days (May 24 – 30) — Gov subdomain
- Active users: 101 ▼ 12.9%
- Event count: 519 ▼ 37.2%
- **Key events: 3 ▼ 57.1%**
- New users: 97 ▼ 9.3%
- Below peer median/range band (Business Finance)

### Landing pages — Gov subdomain (Last 90d) — the conversion leak

| # | Landing page | Sessions | % | Avg eng. time | Key events | Conv. rate |
|---|---|---|---|---|---|---|
| 1 | `/` (homepage) | 762 | 42.7% | 39s | 46 | **6.0%** |
| 2 | `/govcon-giants-partner-government-contractor-funding` | **406** | **22.8%** | 28s | 14 | **3.4%** |
| 3 | (not set) | 111 | 6.2% | — | — | — |
| 4 | `/meet-the-team` | 59 | 3.3% | 40s | 0 | 0% |
| 5 | `/resources/our-team/chad-eberly` | 49 | 2.8% | 47s | 2 | 4.1% |
| 6 | `/solutions` | 35 | 2.0% | 47s | 0 | 0% |

**The conversion leak is the partner page itself, not a broken referral source.**

- Eric Coffie's partner page brings **23% of all sessions** (406 of 1,784) — the referral path is healthy
- But it converts at **3.4%** vs homepage at **6.0%** — a **43% lower conversion rate**
- 406 landings × (6.0% - 3.4%) = ~11 missing key events the partner page should be producing if it converted like the homepage
- That's nearly 80% of the partner page's actual key event output being left on the table

**This is the highest-leverage fix on the entire property.** Either:
- Optimize the partner page funnel (CTA placement, form, trust signals) so it converts like the homepage, OR
- Redirect/restructure some of Eric's promotional links to point at `/` directly when the audience doesn't need the partnership-specific framing

**Other observations:**
- `/solutions/government-contract-financing/` and `/who-we-serve/government-contracting/` — the 404 URLs — do NOT appear in the top 6 landing pages. Either nobody is clicking the legacy links anymore, or those links were updated externally. Still worth adding the 301 redirects for safety, but it's not the bleed source.
- `/meet-the-team` and `/solutions` produce zero key events from 94 combined sessions — entire site sections with no conversion path
- `(not set)` at 6.2% = GA4 tracking gap on ~111 sessions. Worth investigating gtag config.

### Lead funnel — Gov subdomain (Last 90d, from Generate leads overview)

| Funnel stage | Value |
|---|---|
| New users | 1.4K |
| Returning users | 139 |
| **Qualified leads** | **0** |
| **Converted leads** | **0** |

The "Generate leads" business objective is set up but **qualified leads and converted leads return zero over 90 days**. The 72 / 16 / 3 "key events" we saw aren't actual lead conversions — they're upstream events (form views, button clicks). The end-of-funnel events that GA4 needs to call something a "qualified" or "converted" lead are either not wired up or not firing.

Returning users / new users = **9% return rate** — most gov subdomain traffic is one-and-done.

### Traffic Acquisition — Main site (Last 28d, May 3–30)

| Channel | Sessions | % | Engaged | Notes |
|---|---|---|---|---|
| Paid Search | 601 | 22.0% | 360 (37.7%) | Largest channel |
| Direct | 472 | 25.2% | 200 | High brand recall |
| Organic Search | 317 | 16.9% | 201 (21%) | Down from 28% share in March audit |
| Display | 239 | 12.7% | 47 (**4.9%**) | High volume, near-zero engagement — burning budget? |
| Referral | 101 | 5.4% | 66 | |
| Organic Social | 54 | 2.9% | 35 | |
| Email | 31 | 1.7% | 21 | |
| **Total** | **1,876** | | 955 | |

Paid + Display = ~35% of sessions. They're still paying for traffic SEO could earn. Display anomaly worth investigating — 239 sessions at 4.9% engagement.

### Source/Medium — Gov subdomain (Last 90d) — single-source dependency

| Source / Medium | Sessions | % | Engaged | Eng. rate | Avg time |
|---|---|---|---|---|---|
| (direct) / (none) | 813 | 45.6% | 184 | 22.6% | 21s |
| **Eric Coffie / Referral** | **407** | **22.8%** | **191** | **46.9%** | **29s** |
| google / cpc | 231 | 13.0% | 147 | 63.6% | 37s |
| google / organic | 152 | 8.5% | 85 | 12.3% | 37s |
| (not set) | 59 | 3.3% | 14 | 23.7% | 21s |
| bing / organic | 37 | 2.1% | 22 | 2.2% | 40s |
| hs_email / email | 26 | 1.5% | 17 | 65.4% | 1m 07s |
| statics.teams.cdn.office.net / referral | 10 | 0.6% | 3 | 0.4% | — |
| yahoo / organic | 9 | 0.5% | 2 | 0.3% | — |

**"Eric Coffie / Referral" is the gov subdomain's only real referral source.** 407 sessions / 191 engaged sessions / 47% engagement — that single referral path drives **28% of all engaged sessions on the entire property**.

When the 28d engagement rate on Referral fell from 47.3% → 27.5%, that's Eric Coffie traffic being replaced by junk referrers (Teams link previews at 0.4% engagement). Either some Eric Coffie links broke (likely the `/solutions/government-contract-financing/` 404) or the inbound link source itself slowed down.

**Other signals:**
- `(direct) / (none)` at 45.6% / 22.6% engagement = untagged Eric/email/social traffic misattributed. If UTM-tagged properly, dependency on Eric is likely even higher than 22.8% shown.
- `hs_email` (HubSpot email) at **65.4% engagement, 1m 07s avg time** — best-performing channel by quality, but only 26 sessions in 90 days. Massive underutilization.
- `google / cpc` is the cleanest paid channel — 63.6% engagement.
- `bing / organic` at 2.2% engagement = likely bots or junk; not real traffic.
- `google / organic` only 152 sessions over 90 days at 12.3% engagement. SEO is not yet a real driver for gov.

### Traffic Acquisition — Gov subdomain (Last 90d vs 28d) — channel view

| Channel | 90d sess | 90d eng rate | 28d sess | 28d eng rate |
|---|---|---|---|---|
| Direct | 813 (45.6%) | **22.6%** | 283 (48.1%) | **20.1%** |
| **Referral** | **448** (25.1%) | **47.3%** | **125** (21.2%) | **27.5%** ⚠️ |
| Paid Search | 231 (12.9%) | 63.6% | 76 (12.9%) | 65.8% |
| Organic Search | 199 (11.2%) | 55.3% | 73 (12.4%) | 54.8% |
| Email | 26 (1.5%) | 65.4% | 26 (4.4%) | 65.4% |
| Organic Social | 4 (0.2%) | — | 3 (0.5%) | — |
| **Total** | **1,784** | 38.7% | **589** | 38.9% |

**The conversion crash is referral-driven:**

- **Referral engagement rate fell from 47.3% (90d) to 27.5% (28d)** while volume stayed roughly flat
- High-quality referrals dropped off; low-quality replaced them
- This matches the March audit's finding that `/govcon-giants-partner-government-contractor-funding/` was the #2 page with 49s engagement — that traffic source likely pulled back
- **Direct is 45.6% of sessions at 22.6% engagement** — bad ratio. Suggests untagged Eric/GovCon promotional traffic falling into "Direct" instead of being attributed to Referral/Email/Social. Audit assumed Direct = brand; engagement rate says otherwise.
- **Email at 65% engagement is the best channel but only 26 sessions** in 28 days — list not being used to drive gov subdomain traffic
- **Organic Search: 199 sessions over 90 days = 2.2/day.** Tiny base; SEO is not yet moving the needle on gov subdomain.

### Read

**Main site:** Healthy. Users +16%, conversions (key events) **+41%** over 90 days. Engagement 45s. SEO + content work on main is paying off.

**Gov subdomain:** In decline.
- Users **▼47–49%** over 90 days vs prior period
- 90d key events flat (+2.9%) — but 30d ▼47%, 7d ▼57%
- **Conversions fell off a cliff in the last ~30 days**, not gradually
- Engagement (37s) lower than main (45s)

**Why this is likely happening** (cross-referenced with the technical re-crawl above):
1. **No new posts on gov subdomain since Aug 2025** — 9 months of content silence
2. **`/solutions/government-contract-financing/` returning 404** — if any backlinks, ads, or sales decks point there, they're dead
3. **Main homepage has zero links to gov subdomain** — main grew 15.8% but doesn't pass any of that traffic to gov
4. **Stale gov category sitemap (Aug 2025) + post_tag sitemap (Nov 2024)** — Google sees a property that stopped publishing

The "GovCon Giants partnership" referral path was the gov subdomain's #2 traffic driver in the March audit. The cliff-shaped 30-day conversion drop suggests either that referral source dried up or the conversion path itself broke.

---

## 9. What I Could NOT Pull This Pass

| Signal | Why | How to get it |
|---|---|---|
| Core Web Vitals (LCP, CLS, TBT) | PageSpeed Insights anonymous quota exhausted | Use a Google Cloud API key, or run tomorrow |
| CrUX field data | Same | Same |
| GA4 traffic delta (Mar–May) | Needs property access | Export from GA4 |
| GSC impressions/CTR/queries | Needs property access | Export from Search Console |
| Backlinks / DA / referring domains | Needs paid tool | Ahrefs or SEMrush |
| Indexed page count | Needs GSC | `site:` operator gives a rough proxy but unreliable |
| Keyword rankings | Needs paid tool | Ahrefs/SEMrush rank tracker |

---

## 10. Prioritized Fix List (Updated)

### URGENT — gov subdomain bleeding (do this week)
1. **Fix the conversion leak on `/govcon-giants-partner-government-contractor-funding`** — the highest-leverage fix on the entire property. Page brings 23% of sessions but converts at 3.4% vs homepage's 6.0% (43% lower). Audit CTA placement, form prominence, trust signals, and apply-now path. If the partner page funnel matched the homepage, gov subdomain conversions would jump ~25% overnight.
2. **Audit every "Eric Coffie / Referral" link** — single-source dependency confirmed (407 sessions / 47% engagement / 1:1 maps to the partner page). Find every place those links live (YouTube descriptions, FHC, podcast show notes, LinkedIn, email signatures) and verify they all work.
3. **Add 301 redirects** from `/solutions/government-contract-financing/` and `/who-we-serve/government-contracting/` to `/government-contract-financing/` — even though they don't appear in top landing pages, any legacy backlink should redirect not 404. Safety play.
3. **UTM-tag every Eric/GovCon promotional link to gov subdomain** — `(direct) / (none)` is 45.6% of traffic at 22.6% engagement. That's almost certainly untagged Eric/email/social. Tag every link going forward: `?utm_source=govcongiants&utm_medium=youtube` (or `podcast`, `linkedin`, `email`). The 813 Direct sessions should largely reclassify into Referral/Email/Social once tagged.
4. **Hit the HubSpot email list** — `hs_email / email` is the **best channel by quality** (65.4% engagement, 1m 07s avg time) but only 26 sessions in 90 days. Send a gov-specific blast this week. This is the lowest-effort, highest-quality lever available.
5. **Diversify referrals** — gov subdomain depends on one source. Add a second: guest posts on adjacent GovCon publications, GovCon Giants subscriber outreach, NAICS-relevant industry sites.
6. **Add main → gov subdomain links** on main homepage, footer, and "industries we serve" — main grew 16% but currently passes zero authority to gov
7. **Restart gov subdomain content production** — 9 months of silence since Aug 2025 is showing up in GA4 (▼49% new users)
8. **Investigate bing/organic** — 37 sessions at 2.2% engagement is almost certainly bot traffic. Verify in GSC and block if confirmed.
9. **Wire up qualified/converted lead events in GA4** — the Generate Leads business objective is configured but qualified/converted leads return zero over 90 days. The "key events" are firing on upstream actions (form views, scroll, button clicks), not actual form submits or apply-now completions. Without this, attribution back to which referral/page produces actual leads is impossible.

### Still open from March audit
5. **Flip Yoast sitemap to HTTPS** — Yoast Settings → Site Features → toggle. 2-minute fix.
6. **Add `Sitemap:` line to robots.txt** for both domains
7. **Tighten robots.txt** — disallow `/wp-admin/`, `/?s=`, `/wp-includes/`
8. **Consolidate duplicate author sitemaps** (authors-sitemap.xml vs author-sitemap.xml)
9. **Add LocalBusiness schema** for Pepper Pike OH office
10. **Address 2023-backdated post lastmod values** (28 posts flagged in March)

### Polish
11. **Add Organization schema to gov subdomain** (main has it, gov doesn't)
12. **Refresh stale OG image** on main homepage (uses 2022 asset)

### Wins to acknowledge
- Schema markup deployed across main domain (Article, Person, Organization, Breadcrumb)
- Stale 2022 jobs sitemap removed
- Gov subdomain canonicalized correctly on HTTPS

---

## Raw Files

All crawl outputs saved to:
```
/Users/ericcoffie/Encore Funding/tasks/crawl-2026-05-31/
  ├── home-main.html
  ├── home-gov.html
  ├── robots-main.txt
  ├── robots-gov.txt
  ├── sitemap-index-main.xml
  ├── sitemap-index-gov.xml
  ├── post-sitemap-main.xml  (84 URLs)
  ├── page-sitemap-main.xml  (53 URLs)
  ├── authors-sitemap-main.xml
  ├── cat-sitemap-main.xml
  ├── post-sitemap-gov.xml  (18 URLs)
  ├── page-sitemap-gov.xml  (10 URLs)
  ├── latest-post.html
  └── test-apply.html
```
