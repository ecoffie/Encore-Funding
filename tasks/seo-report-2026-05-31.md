# Encore Funding — SEO & Conversion Audit
**Date:** 2026-05-31
**Properties:** encore-funding.com (main) + gov.encore-funding.com (subdomain)
**Compared against:** Original audit (`seo-audit-report.md`, 2026-03-17)
**Method:** Live technical crawl + Google Analytics multi-window analysis (90d / 28d / 7d) on both properties
**Data sources:** curl/HTML parsing of public surfaces; Google Analytics home + Traffic Acquisition + Source/Medium + Landing pages + Generate Leads overview screenshots
**Not included:** Google Search Console (no access this pass — see Section 9 for what GSC would add)

### 🔗 Live working demo of the recommended partner-page rebuild

# **https://partner-page-rebuild.vercel.app/**

Resize narrower than 900px for the mobile layout. See Section 7 for full conversion plan and expected impact (+22% lift on gov subdomain key events).

---

## TL;DR

- **Live working prototype of the recommended partner-page rebuild:** **https://partner-page-rebuild.vercel.app/** (see Section 7)
- **Main site is healthy** — users +16%, conversions +41% over 90 days
- **Gov subdomain is in active decline** — users ▼47%, key events ▼47% over 30d and ▼57% over 7d
- **The conversion bleed is one specific page**, not a broken referral link: `/govcon-giants-partner-government-contractor-funding/` brings 23% of gov sessions but converts at 3.4% vs the homepage's 6.0% — **43% lower**. Fixing this single page is the highest-leverage move on the property.
- **Referral is the strongest non-paid channel** for the gov subdomain (407 sessions / 47% engagement / 28% of all engaged sessions) — traffic quality is high; the conversion page is the constraint.
- **45.6% of gov traffic is "Direct" at 22.6% engagement** — that's untagged promo traffic, not brand recall. UTM tagging would reclassify most of it.
- **HubSpot email is the best channel by quality (65% engagement, 1m 07s avg time)** but only 26 sessions in 90 days. Massive underutilization.
- **Schema markup work is done** since March audit. Sitemap HTTPS issue, robots.txt, content staleness all still open. Two service URLs from the March audit now 404.
- **Proven growth engine, ready to transfer:** we ran a programmatic-SEO build on GovCon Giants (90+ pages from keyword research, 72 indexed, page-one rankings, **all free organic, no ad spend** — see Section 9A) and have turned Encore's March keyword research into a concrete page architecture for both staffing and GovCon — **40–60 pages, ~15,000+ untapped monthly searches** (Section 9B). The March report sized the market; this one shows the pages that capture it.

---

## 1. Technical Re-Crawl

### What changed since March 17

| Signal | March 17 | May 31 | Status |
|---|---|---|---|
| Main sitemap protocol | HTTP URLs in `<loc>` | **Still HTTP URLs** | Not fixed |
| Robots.txt | Permissive, no sitemap | **Unchanged** | Not fixed |
| Schema markup (homepage) | None | **Org + WebSite + Breadcrumb + WebPage** | Fixed |
| Schema markup (blog post) | None | **Article + Person + Breadcrumb + Org** | Fixed |
| Jobs sitemap (stale 2022) | Present | **Removed / 301** | Fixed |
| Main → gov subdomain links | Weak | **Zero from homepage** | Worse |
| `/solutions/government-contract-financing/` | 200 OK in audit | **404** | Broken |
| `/who-we-serve/government-contracting/` | Implied | **404** | Broken |
| Post count (main) | 87 in audit | **84 in sitemap** | Slight decline |
| Stale 2023 backdated posts | 28 posts | **Still in sitemap (earliest lastmod 2023-03-21)** | Not addressed |

### Headers & redirects

**encore-funding.com**
- `https://encore-funding.com/` → 301 → `https://www.encore-funding.com/` (200)
- Behind Sucuri Cloudproxy + Cloudflare
- `content-security-policy: upgrade-insecure-requests` masks HTTP sitemap issue in browsers — but Google reads raw HTTP `<loc>` values
- HTTP/2, HTTP/3 (alt-svc h3)

**gov.encore-funding.com**
- `https://gov.encore-funding.com/` → 200 direct (no www variant)
- Cloudflare only
- Last-modified: active (May 2026)

### Robots.txt — UNCHANGED

Both domains still return:
```
User-Agent: *
Disallow:
```

- No `Sitemap:` line (audit recommendation #1 — still open after 10 weeks)
- No disallow for `/wp-admin/`, `/wp-includes/`, `/?s=` search results

### Sitemaps

**Main site** — sitemap index still lists `http://` URLs (Yoast setting never toggled):

| Sub-sitemap | Protocol | lastmod | URLs |
|---|---|---|---|
| post-sitemap.xml | **http://** | 2026-05-13 | 84 |
| page-sitemap.xml | **http://** | 2026-05-20 | 53 |
| authors-sitemap.xml | **http://** | 2026-05-13 | 10 |
| category-sitemap.xml | **http://** | 2026-05-13 | 6 |
| post_tag-sitemap.xml | **http://** | 2026-05-13 | — |
| author-sitemap.xml | **http://** | 2026-04-28 | — |

Note: Duplicate `authors-sitemap.xml` AND `author-sitemap.xml` still present (audit flagged this).

**Gov subdomain** — all HTTPS (cleaner):

| Sub-sitemap | lastmod | URLs |
|---|---|---|
| post-sitemap.xml | **2025-08-26** | 18 (unchanged) |
| page-sitemap.xml | 2026-05-20 | 10 |
| category-sitemap.xml | 2025-08-26 | — |
| post_tag-sitemap.xml | **2024-11-21** | — |

**No new posts on gov subdomain since August 2025** — 9 months of content silence. Same author-sitemap duplication.

### Schema markup — NEW SINCE AUDIT

Major gap closed. Yoast deployed structured data across the main domain.

**Main homepage `@graph`:**
- WebPage, ImageObject, BreadcrumbList, WebSite, **Organization** ← new

**Gov homepage `@graph`:**
- WebPage, ImageObject, BreadcrumbList, WebSite (**no Organization**)

**Blog post `@graph`:**
- **Article**, WebPage, ImageObject, BreadcrumbList, WebSite, Organization, **Person** ← new

**Still missing:** LocalBusiness (Pepper Pike OH office), FAQ, Service schema on solution pages, Review/AggregateRating for testimonials, and Organization on gov subdomain.

### On-page

| Page | Title | Meta | H1 | Schema |
|---|---|---|---|---|
| Main `/` | "Payroll & Invoice Factoring \| Staffing Agency Funding \| Encore Funding" (unchanged from March, still 3 pipes) | Present | Not in raw HTML (Beaver Builder dynamic) | Yes |
| Main `/apply-now/` | "Apply Now For Fast Staffing Factoring \| Encore Funding" | Generic | — | — |
| Main `/government-contract-financing/` | 200 OK (this is the new location) | — | — | — |
| Main `/solutions/government-contract-financing/` | **404** | — | — | — |
| Main `/who-we-serve/government-contracting/` | **404** | — | — | — |
| Gov `/` | "Government Contractor Financing \| Encore Funding" | Present | — | Yes (no Org) |
| Gov `/govcon-giants-partner-government-contractor-funding/` | 200 OK | — | — | — |

### Cross-property linking — STILL BROKEN

Main homepage HTML contains **zero** links to gov.encore-funding.com or any URL with "government" in it. Main grew 16% in users; passes none of it to gov. Authority flow is one-directional.

---

## 2. Google Analytics Performance Snapshot

### Main site vs Gov subdomain — Last 90 days (Mar 8 – May 24, 2026)

| Metric | Main | Gov |
|---|---|---|
| Active users | **4.3K** ▲ 15.8% | **1.4K** ▼ 47.2% |
| Event count | 31K ▲ 5.4% | 7.9K ▼ 42.1% |
| Key events | **371 ▲ 41.1%** | **72 ▲ 2.9%** |
| New users | 4.2K ▲ 16.5% | 1.4K ▼ 49.1% |

### Last 28 days (May 3 – May 30, 2026)

| Metric | Main | Gov |
|---|---|---|
| Active users | 1.3K | 467 |
| New users | 1.2K | 452 |
| Avg engagement time / user | **45s** | **37s** |

### Gov subdomain — recent decay

| Window | Active users | Event count | **Key events** | New users |
|---|---|---|---|---|
| 90d | 1.4K ▼ 47.2% | 7.9K ▼ 42.1% | **72 ▲ 2.9%** | 1.4K ▼ 49.1% |
| 30d | 493 ▲ 13.3% | 2.9K ▲ 27.2% | **16 ▼ 46.7%** | 478 ▲ 13.5% |
| 7d | 101 ▼ 12.9% | 519 ▼ 37.2% | **3 ▼ 57.1%** | 97 ▼ 9.3% |

Volume came back in May (30d users +13%) but **conversions fell off a cliff in the same window** — 90d key events were +3%, then 30d ▼47%, then 7d ▼57%. This is the smoking gun.

7-day chart below the peer median/range band for Business Finance.

---

## 3. Traffic Acquisition

### Main site — Last 28d (May 3–30)

| Channel | Sessions | % | Engaged | Notes |
|---|---|---|---|---|
| Paid Search | **601** | 22.0% | 360 (37.7%) | Largest channel |
| Direct | 472 | 25.2% | 200 | Brand recall |
| Organic Search | 317 | 16.9% | 201 (21%) | Down from 28% share in March |
| Display | **239** | 12.7% | 47 (**4.9%**) | High volume, near-zero engagement — burning budget? |
| Referral | 101 | 5.4% | 66 | |
| Organic Social | 54 | 2.9% | 35 | |
| Email | 31 | 1.7% | 21 | |
| **Total** | **1,876** | | 955 | |

Paid + Display ≈ 35% of sessions. Still paying for traffic SEO should be earning. Display anomaly worth investigating — 239 sessions at 4.9% engagement is retargeting or low-quality network burn.

### Gov subdomain — Channel view (90d vs 28d)

| Channel | 90d sess | 90d eng rate | 28d sess | 28d eng rate |
|---|---|---|---|---|
| Direct | 813 (45.6%) | **22.6%** | 283 (48.1%) | **20.1%** |
| **Referral** | **448** (25.1%) | **47.3%** | **125** (21.2%) | **27.5%** ⚠️ |
| Paid Search | 231 (12.9%) | 63.6% | 76 (12.9%) | 65.8% |
| Organic Search | 199 (11.2%) | 55.3% | 73 (12.4%) | 54.8% |
| Email | 26 (1.5%) | 65.4% | 26 (4.4%) | 65.4% |
| Organic Social | 4 (0.2%) | — | 3 (0.5%) | — |
| **Total** | **1,784** | 38.7% | **589** | 38.9% |

**Referral engagement rate fell 47.3% → 27.5% in the last 28 days** while volume stayed roughly flat. High-quality referrals partially replaced by junk.

### Gov subdomain — Source/Medium (Last 90d)

| Source / Medium | Sessions | % | Engaged | Eng. rate | Avg time |
|---|---|---|---|---|---|
| (direct) / (none) | 813 | 45.6% | 184 | 22.6% | 21s |
| **Eric Coffie / Referral** | **407** | **22.8%** | **191** | **46.9%** | **29s** |
| google / cpc | 231 | 13.0% | 147 | 63.6% | 37s |
| google / organic | 152 | 8.5% | 85 | 12.3% | 37s |
| (not set) | 59 | 3.3% | 14 | 23.7% | 21s |
| bing / organic | 37 | 2.1% | 22 | 2.2% | 40s |
| **hs_email / email** | **26** | 1.5% | 17 | **65.4%** | **1m 07s** |
| statics.teams.cdn.office.net / referral | 10 | 0.6% | 3 | 0.4% | — |
| yahoo / organic | 9 | 0.5% | 2 | 0.3% | — |

**Referral is the gov subdomain's strongest non-paid channel.** 407 sessions / 191 engaged sessions = 28% of all engaged sessions on the property, at a high 47% engagement rate.

**Other signals:**
- `(direct) / (none)` at 45.6% / 22.6% engagement is untagged email/social/referral misattributed. UTM tagging would reclassify most of it into its real sources.
- `hs_email`: **best channel by quality** (65.4% engagement, 1m 07s avg) — only 26 sessions in 90 days. Massive underuse.
- `google/cpc`: cleanest paid channel at 63.6% engagement.
- `bing/organic` at 2.2% engagement: almost certainly bots. Investigate.
- `google/organic`: 152 sessions / 90d at 12.3% engagement. SEO is not yet a real driver for gov.

---

## 4. Landing Pages — Gov subdomain (Last 90d)

| # | Landing page | Sessions | % | Avg eng. time | Key events | Conv. rate |
|---|---|---|---|---|---|---|
| 1 | `/` (homepage) | 762 | 42.7% | 39s | 46 | **6.0%** |
| 2 | **`/govcon-giants-partner-government-contractor-funding`** | **406** | **22.8%** | 28s | 14 | **3.4%** |
| 3 | (not set) | 111 | 6.2% | — | — | — |
| 4 | `/meet-the-team` | 59 | 3.3% | 40s | 0 | 0% |
| 5 | `/resources/our-team/chad-eberly` | 49 | 2.8% | 47s | 2 | 4.1% |
| 6 | `/solutions` | 35 | 2.0% | 47s | 0 | 0% |

(96 total landing pages)

**The conversion leak is the partner page itself, not a broken referral.**

- Eric Coffie's partner page brings **23% of all gov sessions** (406 of 1,784) — referral path is healthy
- But converts at **3.4%** vs homepage at **6.0%** — a **43% lower conversion rate**
- 406 sessions × (6.0% − 3.4%) = **~11 missing key events per 90 days** the partner page should be producing if it converted like the homepage
- That's nearly **80% of the page's actual key event output being left on the table**

**This is the highest-leverage fix on the entire engagement.**

**Other findings:**
- `/solutions/government-contract-financing/` and `/who-we-serve/government-contracting/` (the 404 URLs) do NOT appear in top landing pages — either nobody clicks legacy links anymore or those got updated externally. 301s are still a safety play.
- `/meet-the-team` and `/solutions` produce zero key events from 94 combined sessions — entire sections with no conversion path
- `(not set)` at 6.2% (~111 sessions) = Google Analytics tracking gap. Worth investigating gtag config.

---

## 5. Lead Funnel — Gov subdomain (90d, from Generate Leads overview)

| Funnel stage | Value |
|---|---|
| New users | 1.4K |
| Returning users | 139 |
| **Qualified leads** | **0** |
| **Converted leads** | **0** |

The "Generate leads" business objective is configured but qualified leads and converted leads return **zero over 90 days**. The 72 / 16 / 3 "key events" we saw are firing on upstream actions (form views, button clicks, scroll) — not actual form submits or apply-now completions.

**Without lead-event wiring, attribution back to which referral source or landing page produces actual revenue is impossible.** Eric's traffic may be converting offline but Google Analytics can't see it.

Returning users / new users = 9% — most gov subdomain traffic is one-and-done.

---

## 6. The Conversion Diagnosis (Synthesis)

The 30-day conversion crash on the gov subdomain is the result of **three compounding factors**, in order of impact:

### Factor 1: Eric's partner page leaks 43% of its conversion potential
The single biggest issue. 406 sessions × 2.6 percentage points of missed conversion = the property's largest performance gap.

**Likely cause:** The page is optimized for *trust-building* and *credibility* (Eric Coffie partnership story) but not for *direct response*. Visitors read the story, get the credibility hit, leave. Homepage is the opposite: clear apply CTA above fold → 6.0% conversion.

### Factor 2: Channel concentration
Eric Coffie referrals = 28% of engaged sessions. When Eric's volume dipped slightly (or his page traffic mix shifted toward lower-intent visitors), the property's overall conversion rate dropped because his page converts at half the rate of the homepage.

### Factor 3: 45.6% untagged "Direct" traffic
Untagged Eric/email/social falls into Direct. This means:
- Once UTM-tagged, referral's true share likely resolves to ~35–40% of traffic
- Email channel performance looks 4x worse than reality (since email blasts without UTMs become Direct)
- Can't optimize what can't be measured

**What's NOT the cause:**
- The 404 URLs (not in top landing pages)
- A specific referrer disappearing (Eric Coffie source is intact)
- SEO collapse (organic was never large enough to crash the property)

---

## 7. Recommended Fixes — Partner Page Conversion Plan

### 🔗 Live working prototype: **https://partner-page-rebuild.vercel.app/**

Click through to see the rebuild in action. Resize the window narrower than 900px to see the mobile layout including the sticky bottom CTA. All CTAs are wired to scroll to the embedded form. Full source + build spec in `partner-page-rebuild/`.

**Full rebuild spec lives in `partner-page-rebuild/`** — wireframe, copy, implementation guide, and HTML preview. Summary below.

The single most valuable change to make this week. Target: lift `/govcon-giants-partner-government-contractor-funding/` from 3.4% to 6.0% conversion = +11 key events / 90d = ~18% lift on total property conversions.

**What the current page is missing (confirmed by HTML audit on 2026-05-31):**
- Zero forms on the page (every conversion requires a click off)
- Only one body CTA, and it points to `/contact-us/` (not `/apply-now/`)
- H1 is "GovCon Giants Fan? Meet Encore Funding." — filters out non-fans, doesn't sell anything
- 3 blog article promos in the middle send visitors **away** from the conversion path
- No above-fold CTA in the page body (Apply Now exists only in the header nav)

### Above-the-fold (first 600px)

**Current likely state:** Header → "Eric Coffie + Encore Funding" hero → long credibility story
**Change to:**
- **Headline:** Conversion-focused, not partnership-focused
  - *Bad:* "Eric Coffie Partners With Encore Funding"
  - *Good:* "Government Contractor Financing — Endorsed by Eric Coffie"
- **Subhead:** What it does + who it's for in one line
  - *"Fast working capital for government contractors. Same-day approval, no equity, no personal guarantees."*
- **Primary CTA button:** Above the fold, contrasting color, action verb
  - *"Apply Now — Get Funded in 48 Hours"* (not "Learn More")
- **Trust strip:** Below CTA: "$25B+ funded · Founded by Advance Partners team · Eric Coffie–vetted"
- **Eric quote/photo:** Right-side or below — supports the headline, doesn't lead it

### Mid-page (the credibility block)

Keep the partnership story — it's why people are there — but **break it up with mid-content CTAs**:
- After Eric's quote → "Ready to apply? Start here" button
- After case study → "See if you qualify" button (links to assessment tool)
- After "About Encore" → repeat primary CTA

The current page likely has one CTA at the bottom. Visitors land, read, leave before reaching it.

### Form placement

- **Embed the apply-now form directly on the page** — don't make people click through to `/apply-now/`. Every click loses 20–30% of intent.
- Short form: name, email, phone, monthly invoice volume. Long-form fields can come on the next step.
- Right rail sticky form on desktop, sticky bottom bar on mobile

### Exit-intent capture

- Modal on exit: "Before you go — get our Government Contractor Funding Guide" with email capture
- Routes captured leads into HubSpot for the email nurture sequence (which has the 65% engagement rate already)

### Trust signals

- Add LocalBusiness schema (Pepper Pike OH address)
- Add Review/AggregateRating schema for any existing testimonials
- BBB badge, Inc. 5000 mentions if applicable
- "As featured by Eric Coffie" video embed (high-engagement)

### Page speed / UX

- Confirm mobile experience — most Eric Coffie referrals likely come from YouTube/podcast on mobile
- Check that form fields work cleanly on mobile keyboards (autofocus, autocomplete attributes)

---

## 8. Recommended Fixes — Full Prioritized List

### URGENT — do this week
1. **Fix partner page conversion** (see Section 7) — highest leverage on the property. 3.4% → 6.0% conversion = ~18% total property lift.
2. **Audit every Eric Coffie referral link** — YouTube descriptions, Federal Help Center, podcast show notes, LinkedIn, email signatures. Verify destinations are live.
3. **Wire qualified/converted lead events to Google Analytics** — the funnel currently reads 0 qualified / 0 converted leads over 90 days. Until form submits fire as key events, no real attribution is possible.
4. **Send HubSpot email blast this week** — 65.4% engagement, 1m 07s avg time, currently 26 sessions in 90d. Cheapest highest-quality lever available. Topic: drive traffic to the (newly fixed) partner page or directly to homepage.
5. **UTM tagging spec (deploy today, retrofit going forward):**
   - YouTube descriptions: `?utm_source=youtube&utm_medium=video&utm_campaign=[video-slug]`
   - Podcast show notes: `?utm_source=podcast&utm_medium=show-notes&utm_campaign=[episode]`
   - LinkedIn posts: `?utm_source=linkedin&utm_medium=social&utm_campaign=[topic]`
   - Email blasts: `?utm_source=encore&utm_medium=email&utm_campaign=[date-topic]`
   - Federal Help Center: `?utm_source=fhc&utm_medium=referral&utm_campaign=[placement]`
   - Sales decks/PDFs: `?utm_source=sales&utm_medium=deck&utm_campaign=[deck-name]`

### HIGH — do this month
6. **Add 301 redirects** from `/solutions/government-contract-financing/` and `/who-we-serve/government-contracting/` → `/government-contract-financing/`
7. **Add main → gov subdomain links** on main homepage, footer, and "industries we serve" section
8. **Restart gov subdomain content production** — 9 months silent since Aug 2025. Target: 2 posts/month minimum.
9. **Diversify gov subdomain referrals** — second source besides Eric Coffie. Guest posts on adjacent GovCon publications, NAICS-relevant industry sites, GovCon Giants subscriber outreach.
10. **Add lead-stage events on gov subdomain forms:**
    - `form_view` → `form_start` → `form_submit` → `apply_complete`
    - Mark `form_submit` as qualified lead, `apply_complete` as converted lead

### MEDIUM — open since March audit
11. **Flip Yoast sitemap to HTTPS** — 2-minute fix in Yoast settings. Still not done.
12. **Add `Sitemap:` line to robots.txt** for both domains
13. **Tighten robots.txt** — disallow `/wp-admin/`, `/?s=`, `/wp-includes/`
14. **Consolidate duplicate author sitemaps** (`authors-sitemap.xml` vs `author-sitemap.xml`) on both domains
15. **Add LocalBusiness schema** with Pepper Pike OH NAP data
16. **Address 2023-backdated post `<lastmod>` values** (28 posts flagged in March audit)
17. **Add Organization schema to gov subdomain** (main has it, gov doesn't)
18. **Refresh stale OG image** on main homepage (uses 2022 asset)

### LOW — polish
19. **Investigate Display anomaly on main site** — 239 sessions at 4.9% engagement. Likely retargeting burn.
20. **Investigate bing/organic on gov** — 2.2% engagement = likely bots. Verify in GSC and block if confirmed.
21. **Investigate `(not set)` landing pages** — 6.2% of gov sessions have no captured landing page. gtag/Google Analytics config issue.

---

## 9. Google Search Console — Data Needed

Google Analytics tells us what happens **after** users land on the site. GSC tells us what happens **before** — in the Google search results themselves. The current report is blind on the second half.

### How GSC differs from Google Analytics

| Question | Google Analytics | GSC |
|---|---|---|
| How many people visit | ✅ | ❌ |
| What they did once they arrived | ✅ | ❌ |
| Which channel they came from | ✅ | ❌ |
| **Which Google searches showed our page** | ❌ | ✅ |
| **CTR by query and by page** | ❌ | ✅ |
| **What position we rank at for each query** | ❌ | ✅ |
| Whether Google is indexing our pages | ❌ | ✅ |
| Whether Google accepted our sitemap | ❌ | ✅ |
| Manual actions / penalties / security issues | ❌ | ✅ |
| Core Web Vitals from real users | Partial | ✅ |
| Mobile usability errors | ❌ | ✅ |
| Schema validation (rich results) | ❌ | ✅ |

One-line summary: **Google Analytics = what happens after the click. GSC = what happens before the click.**

### Why this matters for the current findings

Several conclusions in this report would sharpen significantly with GSC data:

1. **Why organic search is so small on gov subdomain** (152 sessions / 90d at 12.3% engagement). GSC would tell us if the cause is:
   - Not indexed for the right queries → coverage problem
   - Indexed but ranking poorly → ranking problem
   - Ranking well but bad title/meta causing low CTR → snippet problem
   - Currently we can only guess
2. **Real keyword rankings** — the March audit's keyword list is aspirational. GSC shows the queries the sites *actually* rank for, at what position, with what CTR. This is the foundation for any real SEO strategy.
3. **The 404 URLs** (`/solutions/government-contract-financing/`) — GSC's coverage report shows how many impressions Google still shows for those dead URLs, which sizes the 301 redirect priority. If Google still serves 50 impressions/month for them, those clicks are landing on a 404 page.
4. **HTTP/HTTPS sitemap rejection** — GSC explicitly flags whether Google accepted the main site's sitemap with HTTP `<loc>` values or excluded URLs. Currently I'm inferring impact.
5. **Schema validation** — confirmed structurally present (Article, Person, Org, Breadcrumb) but GSC's Rich Results report tells us if Google is **accepting** the markup and serving rich snippets in SERPs.
6. **Core Web Vitals (real users)** — PageSpeed anonymous quota was exhausted; GSC has CrUX field data permanently available, segmented mobile vs desktop.
7. **Indexed page count** — are all 84 main posts + 18 gov posts actually indexed? GSC answers in one screen.

### Specific GSC reports to pull

**For both properties (main + gov subdomain):**

| Report | Why | Output to capture |
|---|---|---|
| Performance → Queries (last 3 months) | Real keyword rankings + impressions + CTR | Top 30 queries by clicks, top 30 by impressions, average position |
| Performance → Pages (last 3 months) | Which URLs Google sends traffic to | Top 20 pages by clicks |
| Performance → Devices | Mobile vs desktop split | Click split |
| Performance → Countries | Geographic distribution | Top 10 countries |
| Pages (Indexing) → Why pages aren't indexed | Coverage problems | "Not indexed" reasons + counts |
| Pages (Indexing) → Indexed pages | Confirms full sitemap is in index | Total indexed count vs sitemap count |
| Sitemaps | Did Google accept the sitemap | Status + last read + URLs submitted vs indexed |
| Page experience → Core Web Vitals | LCP, CLS, INP from real users | Mobile + desktop URL counts in Good/Needs Improvement/Poor |
| Page experience → Mobile usability | Mobile errors | Error count and affected pages |
| Enhancements → Each schema type | Rich result validation | Valid / Warning / Error counts |
| Links → External | Backlink count + top linking sites + top linked pages | Top 20 referring sites |
| Links → Internal | Internal link distribution | Top linked internal pages |
| Manual actions | Penalty check | Should be empty |
| Security issues | Hacked/malware check | Should be empty |

### Cross-references against this report

Once GSC data is available, these specific cells in the current report can be filled or corrected:

| Currently in report | GSC will resolve |
|---|---|
| "Organic Search: 199 sessions / 90d at 12.3% engagement" | Which queries drove those 199 — and whether the engagement issue is wrong queries or weak landing pages |
| "Main → gov subdomain: zero links from homepage" | Whether Google sees the gov subdomain as related to main (via internal/external links graph) |
| "404 URLs: not in top landing pages" | Whether Google still shows them in SERPs and how many impressions/month |
| "google/organic at 152 sessions" on gov | Which queries — likely brand ("encore funding") vs non-brand ("government contractor financing") |
| "Schema deployed (Article, Person, Org)" | Whether Google validated it and how many rich result eligible URLs exist |
| "84 posts in main sitemap" | How many are actually indexed |
| "No new gov posts since Aug 2025" | Whether those 18 posts still rank — and for what |
| "google/cpc converts at 63.6% engagement" | Paid CTR/position vs organic — should the gov subdomain bid less and rank more? |
| "bing/organic at 2.2% engagement = likely bots" | Confirm by checking if those queries exist in Bing Webmaster Tools (GSC's bing equivalent) |

### Access path

If GSC isn't accessible:
- **Easiest:** Eric or the Encore web admin grants access at search.google.com/search-console — both `encore-funding.com` and `gov.encore-funding.com` properties (separate properties; subdomain needs its own verification)
- **Google Analytics integration:** the Google Analytics left nav already shows a "Search Console" section in the screenshots, so the properties may already be linked — you can pull most query data inside Google Analytics once linked
- **Minimum useful screenshots:** Performance → Queries (last 3 months, both properties) + Indexing → Pages (both) + Page experience → Core Web Vitals (both)

---

## 9A. Proof of Method — The GovCon Giants Programmatic-SEO Build

The recommendations in this report (especially Section 8's "restart content" and the page-architecture in 9B below) are not theoretical. We ran the identical playbook on **GovCon Giants (govcongiants.org)** over Mar–May 2026, with **zero ad spend**, and have the GSC data to prove the outcome. This is the engine we'd bring to Encore.

### Method: research first, pages second

Every page was justified by a search-volume + difficulty pull for the government-contracting niche before it was built. The result is a set of programmatic clusters, each rendered from a template with per-page schema (Article + FAQPage on guides, DefinedTermSet on glossary, Service on service pages, VideoObject on video pages):

| Cluster | Route pattern | Targets | Pages |
|---|---|---|---|
| Guides | `/guides/[slug]` | "cage code" (9,900/mo), "8(a) certification," "GSA schedule," "SAM.gov registration" (5,400/mo) | 16 |
| Glossary | `/glossary` (DefinedTermSet) | "what is a [term]" long-tail — DCAA, BPA, PWS, SOW, FFP, CPFF… | 63 terms |
| Competitor comparisons | `/compare/[competitor]` | "GovWin alternative" (1,300/mo), Deltek/GovTribe/HigherGov/Bloomberg/Sweetspot… | 11 |
| Audience landing | `/for/[audience]` | "for 8(a) contractors," "for staffing agencies," "for HUBZone," "for SDVOSB"… | 12 |
| Jobs | `/jobs/[role]` | "capture manager jobs," "proposal manager salary," "/jobs/defense," "/jobs/remote" | 9+ |
| Video SEO | `/videos/[slug]` | video-intent searches mapped to the YouTube library (~10,600/mo combined) | 16 |

**90+ indexable routes, one keyword-research pass, one developer.** Sitemap grew from ~37 → ~82 URLs over the period.

### Measured GSC results (all organic, no ad spend)

| Metric | Mar 17 (Wk 2) | Mar 29 (Wk 4) | Note |
|---|---|---|---|
| Total clicks (new pages) | 19 | — | from a cold start |
| Total impressions | 360 | — | |
| Average CTR | **5.3%** | 9.2% (homepage) | vs ~3% benchmark — exceeding |
| Average position | **8.9** | top-10 holding | page 1 |
| Homepage | — | **96 clicks / 1,047 impr / 9.2% CTR** | top performer |
| CAGE-code cluster (guide + tool + blog redirect) | — | **46 clicks / 11,828 impressions** | one topic, one month |
| Pages indexed | — | **72** | confirmed in GSC Coverage |

Indexing health managed in GSC throughout: 200+ legacy WordPress 404s fixed with 301/308 redirects (Mar 29), priority pages submitted for indexing in tiers, JSON-LD validated via Rich Results Test.

### Why this transfers to Encore

- Encore's gov subdomain has **published nothing since Aug 2025** and carries only 18 thin posts — the same cold-start GovCon Giants began from.
- The `/for/[audience]` and `/compare/[competitor]` patterns map **directly** onto Encore's set-aside audiences and financing-competitor set (Section 9B).
- It adds a **compounding organic channel** that earns its own traffic from Google — broadening the channel mix noted in Section 3.

---

## 9B. The Encore Page Architecture — Turning March's Market Size Into Pages

The March audit established the **market size** and surfaced the keyword matrices for both staffing and GovCon financing. This section converts that research into a concrete, buildable page set. Two engines.

### Engine 1 — Staffing (encore-funding.com)

Most of these queries currently resolve to a blog post or nothing. Each should be a dedicated service/resource page with schema, internal links, and a clear apply/contact CTA.

| Page to build | Target query | Est. vol/mo | Current state | Priority |
|---|---|---|---|---|
| `/payroll-funding` (pillar) | payroll funding / payroll factoring | 500–800 | Thin | HIGH |
| `/staffing-factoring-rates` | staffing factoring rates comparison | high-intent | **Missing** | HIGH |
| `/healthcare-staffing-funding` | healthcare staffing funding | 200–400 | Blog only | HIGH |
| `/it-staffing-funding` | IT staffing funding | 100–200 | Blog only | HIGH |
| `/how-to-start-a-staffing-agency` (pillar) | how to start a staffing agency | 2,000–4,000 | Optimize existing | MED |
| `/staffing-agency-business-plan` + template | staffing agency business plan template | 1,000–2,000 | Competitor (Scale) owns it | MED |
| `/staffing-agency-startup-costs` | how much to start a staffing agency | ~1,400 | Missing | MED |
| `/staffing-agency-license/[state]` | staffing agency license [state] | ~2,000 | **Missing — 50-state programmatic set** | HIGH (long-tail) |
| `/payroll-funding-vs-bank-loan` | payroll funding vs bank loans | comparison | Missing | MED |

The state-licensing template alone yields **~50 low-competition long-tail pages** from one build — the highest-leverage programmatic play on the staffing side.

### Engine 2 — GovCon Financing (gov.encore-funding.com)

The clearest greenfield Encore owns. Financing-intent + certification-adjacent queries mirror the GovCon Giants `/for/` and `/compare/` patterns and align with the audience Eric already drives.

| Page cluster | Route | Target query | Conversion logic |
|---|---|---|---|
| Pillar | `/government-contractor-financing` | government contractor financing | core money term, high commercial intent; consolidate, don't cannibalize |
| Bottom-funnel | `/govcon-invoice-factoring`, `/federal-contract-factoring` | govcon invoice factoring | buyers ready to apply |
| Set-aside audience | `/for/8a`, `/for/wosb`, `/for/sdvosb`, `/for/hubzone` | "financing for 8(a) contractors," etc. | mirrors GCG `/for/`; matches Eric's audience 1:1 |
| Contract-type | `/financing/idiq`, `/financing/gsa-schedule`, `/financing/prime-sub` | "funding a GSA schedule contract" | captures contractors at award moment |
| Comparison | `/govcon-financing-vs-bank-loan`, `/vs-line-of-credit`, `/vs-mca` | comparison queries | high-intent buyers weighing options |
| Case studies | `/case-studies/[slug]` (schema-marked) | "[industry] govcon financing case study" | 2 already exist → repeatable template |

**Note on architecture:** the March audit recommended consolidating the subdomain to a subfolder (`encore-funding.com/govcon/`) to stop authority dilution. Whichever architecture Encore chooses, this page set is the content layer that goes on top of it. Build the pages on a subfolder and they inherit the main domain's authority from day one.

### Sizing the opportunity

- **40–60 new programmatic pages** across both engines (staffing verticals + 50-state set + GovCon audience/contract-type/comparison clusters).
- **~15,000+ combined monthly searches** the two properties do not currently capture in any meaningful position.
- Benchmark from the GovCon Giants build (9A): page-one rankings on validated terms within weeks, 72 pages indexed in ~4 weeks.
- Strategic payoff: a **second compounding traffic source independent of Eric Coffie** — directly mitigating the single-source dependency in Section 3 and the publishing silence in Section 8.

The March report sold the *why* (market size). This is the *what* and *how* (the pages, the routes, the templates). The only missing input is a go-ahead to start producing them.

---

## 10. What Could NOT Be Pulled (Other)

| Signal | Why | How to get it |
|---|---|---|
| Backlinks / DA / referring domains (full graph) | Needs paid tool | Ahrefs or SEMrush (GSC shows top 1000 but not the full graph) |
| Keyword rankings outside top 1000 impressions | GSC truncates long-tail | Ahrefs/SEMrush rank tracker |
| Referral source for the 30d quality drop | Need 28d vs prior 28d source/medium comparison | One more Google Analytics screenshot |
| Core Web Vitals from synthetic test (PageSpeed) | Anonymous quota exhausted today | Google Cloud API key, or run tomorrow (GSC has the real-user CrUX data; PageSpeed is the synthetic complement) |

---

## 10. Expected Impact (If Top 5 URGENT Items Shipped)

| Fix | Estimated 90d impact on gov subdomain key events |
|---|---|
| Partner page conversion 3.4% → 6.0% | +11 key events |
| HubSpot email blast (1 send to gov segment) | +5–8 key events (est. 200–300 quality sessions) |
| UTM tagging (no direct lift, enables optimization) | Indirect — unlocks ability to measure |
| Lead-event wiring (no direct lift, enables attribution) | Indirect — unlocks ROI reporting |
| Eric Coffie link audit (defensive — prevents loss) | Maintains current 14 key events from partner page |

**Total estimated lift over 90d: +16–19 key events (~22–26% lift on the 72-event 90d baseline)**

**See the proposed partner-page rebuild live:** **https://partner-page-rebuild.vercel.app/**

---

## Raw Crawl Files

All HTTP crawl outputs saved to:
```
/Users/ericcoffie/Encore Funding/tasks/crawl-2026-05-31/
  ├── home-main.html, home-gov.html
  ├── robots-main.txt, robots-gov.txt
  ├── sitemap-index-main.xml, sitemap-index-gov.xml
  ├── post-sitemap-main.xml (84 URLs), page-sitemap-main.xml (53 URLs)
  ├── authors-sitemap-main.xml, cat-sitemap-main.xml
  ├── post-sitemap-gov.xml (18 URLs), page-sitemap-gov.xml (10 URLs)
  ├── latest-post.html (Chad Eberly ABF Journal post — schema reference)
  └── test-apply.html
```

Google Analytics screenshots referenced for this audit:
- Both properties: Home, Reports snapshot
- Main: Traffic Acquisition (28d)
- Gov: Traffic Acquisition (28d, 90d), Source/Medium (90d), Landing pages (90d), Generate Leads overview (90d)
