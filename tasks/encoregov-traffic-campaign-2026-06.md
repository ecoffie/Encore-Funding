# Encore Funding — The 60-Day Proof Campaign

## Drive Traffic to encoregov.com, Prove the Engine Before We Pitch It

**Prepared by:** GovCon Giants
**Date:** June 1, 2026
**Companion to:** SEO & Conversion Update (May 2026)
**Decision locked:** Win condition = **qualified leads / applications**. Engine = **organic / owned channels only, $0 ad spend.**

---

## The Idea in One Sentence

Instead of *telling* Encore we can grow their GovCon channel, we **show them** — by driving traffic and leads to **encoregov.com, a property we already control**, over 60 days, and putting our results next to what their `gov.encore-funding.com` subdomain produces today.

Same audience (Eric's). Same offer (Encore funding). One side leaks; one side is engineered. The gap is the pitch.

---

## Why This Beats the Written Report

The May report makes an argument on paper. This makes it on a dashboard. When we sit down with Encore in 60 days, we don't open a PDF — we open two analytics screens:

> "Here's `gov.encore-funding.com` — the page you point Eric's audience at. **1,784 sessions, 14 applications in 90 days.**
> Here's `encoregov.com` — the page **we** built and drove traffic to. **[X] sessions, [Y] applications in 60 days, $0 in ad spend.**
> We didn't write you a strategy. We ran it."

That is unarguable. You can dismiss a slide. You can't dismiss leads in a CRM.

---

## The Baseline We're Beating (Their Property)

Pulled from the May 2026 GA4 audit of `gov.encore-funding.com`:

| Metric (90 days) | gov.encore-funding.com | Source |
|---|---|---|
| Total sessions | **1,784** | GA4 |
| Eric Coffie / Referral sessions | **407** (22.8%) | the partner-page traffic |
| Partner page sessions | **406** | the page Eric links to |
| Partner page **key events (applications)** | **14** | at 3.4% conversion |
| Organic search sessions | **152** (12.3% engagement) | SEO is not a driver |
| Content pages | **18 thin posts**, silent since Aug 2025 | crawl |
| New GovCon content in last 9 months | **0** | — |

**The number that matters:** the partner page — the single highest-traffic page Eric sends people to — produces **14 applications per 90 days.** That's the bar. We're going to clear it on our own site, from a cold start, in 60 days, for free.

---

## What We're Starting From (Our Property)

`encoregov.com` today:

| Asset | State | Implication |
|---|---|---|
| Pages | **2** (home + thank-you) | Greenfield — we build the content engine from scratch |
| Lead form | ✅ Built (`LeadForm.tsx` → HubSpot + Slack + email + Redis) | Capture path already works |
| **Analytics tag** | ❌ **Not installed** | **Phase 0 blocker — we cannot prove what we cannot measure** |
| Lead-event tracking | ❌ Not wired to GA4 | Must fire on form submit, day 1 |
| Existing traffic | Unknown (no GA) | Effectively zero baseline — every session is net-new and attributable |

The missing analytics is the most important finding here. It's also a feature: because the site starts at zero with clean instrumentation, **every single session and lead over the next 60 days is unambiguously ours** — no legacy traffic to argue about. Cleaner proof than their own property can offer.

---

## The Traffic Engine — Eric's Megaphone, Pointed at a Page We Control

We are not buying traffic. We are deploying the audience Eric already owns, across the channels GovCon Giants already operates — the same free-organic playbook that put 72 pages on Google's page one for govcongiants.org (see May report, Section 9A).

| Channel | Eric's existing reach | How we deploy it |
|---|---|---|
| **YouTube** | 1,600+ videos, **3.67M views**, 52K+ subscribers | Description links + end-screens + 1–2 dedicated/woven mentions → encoregov.com |
| **Podcast** | 688 episodes, **281K+ downloads** | Show-notes links + read placements on new episodes |
| **Email list** | GovCon Giants list (highest-engagement channel) | 2–3 sends featuring the funding offer, UTM-tagged |
| **LinkedIn** | Eric's personal + GCG company page | Organic posts driving to the new resource pages |
| **Programmatic SEO** | The govcongiants.org engine, proven | Build financing-intent pages that earn Google traffic on their own |
| **Cross-links** | tools.govcongiants.org, the partner ecosystem | Internal links from high-traffic GCG pages |

Every link is **UTM-tagged** so we can show Encore *exactly* which channel drove which lead — something their own property can't do today (45.6% of their traffic is untagged "Direct").

---

## The Build — What Goes on encoregov.com

We don't just dump traffic on a 2-page site. We build the destination that converts it, using the same architecture proposed for Encore in the May report (Section 9B) — except **we build it, on a domain we own, this month.**

### Phase 0 — Instrument (Days 1–3) — BLOCKER, do first
- Install GA4 on encoregov.com (new property, clean baseline)
- Wire **form-submit as a GA4 key event** (the thing their site fails to track)
- Connect GA4 ↔ Search Console for the domain
- Confirm HubSpot/Slack/Redis lead capture still fires end-to-end
- **Gate:** no traffic driven until a test lead shows up in GA4 *and* the CRM

### Phase 1 — Build the conversion core (Days 3–10)
- Rebuild the encoregov.com home as a true conversion page (apply form above the fold, stat block: $25B+ funded, 48-hr approval, GovCon-focused) — reuse the partner-page-rebuild prototype already live
- Add the **money pages** (financing-intent, high commercial value):
  - `/government-contractor-financing` (pillar)
  - `/govcon-invoice-factoring` / `/federal-contract-factoring`
  - `/financing/gsa-schedule`, `/financing/idiq`
- Exit-intent funding-guide capture + sticky mobile apply CTA

### Phase 2 — Build the SEO long-tail (Days 7–21)
- `/for/8a`, `/for/wosb`, `/for/sdvosb`, `/for/hubzone` — mirrors Eric's audience 1:1
- `/govcon-financing-vs-bank-loan`, `/vs-line-of-credit`, `/vs-mca` (high-intent comparison)
- 2–3 schema-marked case-study pages (repeatable template)
- Submit sitemap to GSC, request indexing in tiers (the govcongiants.org method)

### Phase 3 — Drive the traffic (Days 10–60, continuous)
- YouTube: links live in descriptions/end-screens; 1–2 woven mentions
- Podcast: show-notes + read placements on new episodes
- Email: send #1 (week 2), send #2 (week 4), send #3 (week 7)
- LinkedIn: 1 post/week to the new pages
- Weekly GSC + GA4 check; double down on whatever channel converts best

---

## The Forecast — Organic / Owned Only, $0 Spend

**Method:** conservative, mid, and aggressive scenarios. Anchored to *known* reach numbers and *observed* conversion behavior, not wishes. Every assumption is stated so Encore can check our math.

### Anchored assumptions (all from real data)

| Input | Value | Where it comes from |
|---|---|---|
| Eric's partner page already drives | 406 sessions / 90d → ~135/mo | May report, GA4 |
| That traffic converts at | 3.4% (their leaky page) | May report |
| A *well-built* page converts at | 6.0% (their own homepage rate) | May report — proves 6% is achievable with *their* audience |
| GovCon Giants SEO ramp | 19 → 96+ clicks on a single page in ~2 weeks; 72 pages indexed in 4 weeks | May report, Section 9A |
| YouTube reach available | 3.67M lifetime views, 52K subs | GCG channel |
| Podcast reach available | 281K+ downloads, 688 episodes | GCG podcast |

### Conversion rate we model

We build encoregov.com to convert at **5–6%** (we control the page, and we've already prototyped the high-converting version). We do **not** assume we beat 6% — that's just matching Encore's *own* best page. Conservative scenario uses 4%.

### 60-Day Lead Forecast (cumulative, organic only)

| Scenario | Driver logic | Sessions (60d) | Conv. rate | **Applications (60d)** |
|---|---|---|---|---|
| **Conservative** | We capture only the Eric-referral traffic that *already exists*, sent to a page that converts properly | ~270 | 4.0% | **~11** |
| **Mid** | Above + email sends + early SEO + podcast/LinkedIn picking up | ~600 | 5.0% | **~30** |
| **Aggressive** | Above + a dedicated YouTube mention converting at scale + SEO pages indexing and ranking | ~1,200 | 5.5% | **~66** |

### The Headline Comparison (the slide we present)

| | gov.encore-funding.com (theirs, **90 days**) | encoregov.com (ours, **60 days**) |
|---|---|---|
| Window | 90 days | **60 days (shorter)** |
| Ad spend | Paid search + display (~35% of traffic) | **$0** |
| Applications | **14** | **11 (conservative) → 30 (mid) → 66 (aggressive)** |
| Per-channel attribution | No (45.6% untagged) | **Yes (every link UTM-tagged)** |
| Content velocity | 0 new pages in 9 months | **8–12 new pages in 60 days** |

**Even the conservative case ties their 90-day number in 60 days with zero ad spend.** The mid case roughly **2x's** it. The aggressive case — if a single YouTube placement lands — **4–5x's** it.

### Why conservative is genuinely conservative

The conservative scenario assumes we get *none* of the SEO compounding, *no* dedicated YouTube video, and only the slice of Eric's traffic that's *already* flowing — we just send it to a page that converts at 4% instead of 3.4%. We'd have to actively underperform to miss it. The realistic outcome is the mid case: **~30 applications in 60 days vs their 14 in 90.**

---

## How We Present It (Day 60)

1. **Two tabs, side by side** — their GA4 + our GA4. Sessions, applications, conversion rate.
2. **The UTM breakdown** — "this many leads came from YouTube, this many from email, this many from organic search." Proof we know *which* lever works.
3. **The SEO indexing screen** — pages we built ranking in Google, earning traffic with no spend.
4. **The CRM** — actual applicant records. Names. "You can call these people."
5. **The ask** — "We did this on our domain in 60 days for free. Imagine it on yours, with your brand, as a paid engagement."

---

## Risks & Honest Caveats

| Risk | Mitigation |
|---|---|
| SEO won't fully mature in 60 days | Forecast leans on owned-audience channels (YT/email/podcast) for the 60-day number; SEO is upside, not the base case |
| Splitting Eric's links between two destinations | Use *new* placements (new videos/episodes/posts) for encoregov, don't cannibalize existing partner-page links — keeps the comparison clean and doesn't hurt Encore |
| "You used Eric's audience, of course it worked" | That's the point — *we* can deploy that audience and *measure* it; they currently can't even tag it. The capability is the product. |
| Lead quality, not just quantity | Track applications → qualified (HubSpot stage), report both. Quality is the funding team's call; we hand them real records |
| Attribution disputes | Clean-room baseline: encoregov starts at zero GA with day-1 lead events. Nothing to argue about. |

---

## Go / No-Go Checklist Before We Drive a Single Visitor

- [x] GA4 installed on encoregov.com — *live, property `G-VYDTBT2QV0`, tag confirmed loading on site (2026-06-06). Final step: confirm Realtime receives events (see below).*
- [x] Form-submit firing as a GA4 key event — *`generate_lead` event wired in LeadForm + /thank-you and present in deployed JS; also writes to HubSpot + Slack + Redis via /api/lead. Verify a test lead appears in GA4 Realtime **and** HubSpot.*
- [x] Search Console verified + sitemap submitted — *verified 2026-06-06; sitemap **Success**, now 57 URLs (was 25). Baseline: 0 clicks / 22 impressions / pos 19.7.*
- [x] Conversion-optimized home page live (apply form above fold) — *home + every SEO page carries the lead form; Apply Now hands off to Encore with UTMs + GA4 `apply_click`.*
- [x] Financing pillar + audience pages live — *pillar upgraded to 9-section structure; 65 pages live across 4 tiers (guides, money satellites, comparisons, calculator, case studies, glossary terms).*
- [x] UTM convention documented — *Apply Now → `?utm_source=encoregov&utm_medium=referral&utm_campaign=apply&utm_content=<source page>`. Channel campaigns should reuse utm_source=encoregov with per-channel utm_medium/utm_campaign.*
- [ ] Baseline screenshot of `gov.encore-funding.com` captured **today** (so the before/after is locked)

Six of seven gates are met. Remaining: (1) capture the `gov.encore-funding.com` baseline screenshot, and (2) the two GA4 verifications below (Realtime receiving `generate_lead` + `apply_click`). Then open the channels and start the 60-day clock.

### GA4 Realtime verification (do once)
1. GA4 property `G-VYDTBT2QV0` → Reports → Realtime.
2. Open encoregov.com in another tab; click an **Apply Now** and submit the **lead form**.
3. Confirm `apply_click` and `generate_lead` appear in Realtime within ~30s, and the test lead lands in HubSpot.

---

## Bottom Line

We can keep arguing the SEO case in documents, or we can spend the next 60 days **proving it on a property we own** — for $0 — and walk into the next meeting with a live dashboard showing **more applications in less time than their current setup produces.** The forecast says even the worst case matches them; the likely case doubles them.

Build it. Measure it. Then let the numbers do the pitching.
