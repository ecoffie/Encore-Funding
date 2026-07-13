# encoregov.com — SEO Page Expansion Plan
## Build the Content Engine to Capture GovCon Financing Buyers

**Prepared by:** GovCon Giants
**Date:** 2026-06-06
**Goal:** Grow encoregov.com from 25 pages → ~75 pages, targeting the three priority buyers (cash-strapped GovCon SMBs, staffing & construction primes, set-aside firms) where they actually search.

---

## TL;DR — The Strategy in One Paragraph

The GovCon-financing money terms ("government contract factoring," "government invoice factoring") are **low-volume but maximally commercial** — every competitor fights for them, and encoregov already has the pillar pages. The traffic-and-authority win is the **informational layer nobody owns**: how GovCon contractors get paid, the Assignment of Claims Act, WAWF, net-30/60 payment gaps. The pure GovCon *specialist* (Republic Capital Access) publishes **zero** educational content; the content leaders (altLINE, FundThrough, eCapital) aren't GovCon-pure. **encoregov's open lane = the specialist that also teaches.** Build the authority cluster first (ranks fastest, feeds the money pages), add the handful of high-intent satellites that map to real demand, and a calculator. Do **not** build more set-aside money pages — those terms have near-zero search demand.

---

## Key Research Findings (what drives this plan)

| Finding | Source | Implication |
|---|---|---|
| Money terms are low-volume / very-high-commercial-intent; SERP saturated w/ FundThrough, altLINE, 1stCC, SMB Compass | Keyword + Competitor agents | Strengthen the 3 existing pillars; don't multiply money pages |
| **Biggest open gap:** Assignment of Claims Act, "how do contractors get paid," WAWF — deep autosuggest tails, weak competitor coverage | Keyword agent (PAA harvest) | **Tier 1 priority.** Highest volume, fastest to rank, passes authority to money pages |
| "payroll funding for staffing companies" = the ONE vertical term with real demand + intent | Keyword agent (autosuggest) | Dedicated staffing-payroll page. Construction factoring second |
| Set-aside financing terms (8a/WOSB/SDVOSB/HUBZone financing) = ~zero direct demand | Keyword agent (empty autosuggest tails) | **Do not build more set-aside money pages.** Serve as FAQ sections. (12 /for/ pages already exist) |
| RCA (GovCon specialist) has no blog/glossary/tools; altLINE/FundThrough/eCapital win on content depth | Competitor agent | encoregov can own "specialist + teacher" position |
| Proven competitor page types: pillar hub, industry/vertical, comparison, glossary taxonomy, calculator, case studies, "best companies" listicle, sector FAQ | Competitor agent | These are the validated archetypes to copy |
| encoregov has 3 reusable templates (ServicePage/AudiencePage/ComparePage) + central link registry (lib/links.ts) + static sitemap | Codebase audit | New pages are cheap. A `[slug]` refactor makes 40-80 trivial + auto-sitemap |

> **Caveat (carry into the report):** Demand ratings are estimates from Google autosuggest depth + SERP density, **not** a paid keyword tool. Validate Tier-1/2 head terms in Ahrefs/SEMrush/Keyword Planner before committing major effort. GSC only shows queries encoregov *already* ranks for — it will not supply market volumes.

---

## The Build Plan — ~50 new pages, 4 tiers by ROI

### TIER 1 — Authority / Informational Cluster (BUILD FIRST)
*Highest volume, fastest to rank, feeds internal links + authority to the money pages. ~18 pages.*

**Guides (long-form, Article + FAQ schema):**
| Page (route) | Target keyword | Demand | Why |
|---|---|---|---|
| `/guides/how-government-contractors-get-paid` | how do government contractors get paid | High | #1 top-funnel hook; pivots to "…get paid faster" → money page |
| `/guides/assignment-of-claims-act` | assignment of claims act | Med-High | The legal mechanism that makes factoring possible; nobody owns it well |
| `/guides/what-is-invoice-factoring` | what is invoice factoring | High | Glossary cornerstone; broad top-funnel |
| `/guides/wawf-payment-guide` | wawf payment / wide area workflow | Med | Qualified DoD audience; thin competitor coverage |
| `/guides/government-shutdown-cash-flow` | do contractors get paid during a shutdown | High (timely) | Strong factoring angle; high autosuggest tail |
| `/guides/net-30-60-90-government-payment` | net 30 / net 60 government payment | Med | Pain-point framing → factoring CTA |
| `/guides/dcaa-compliant-invoice` | dcaa invoice / dcaa compliant invoice | Low-Med | Niche but highly qualified |
| `/guides/far-part-32-contract-financing` | contract financing FAR Part 32 | Low | Authority/topical depth |

**Glossary expansion** (individual term pages — `/glossary/[term]`, DefinedTerm schema; current glossary is one page w/ 21 terms — split highest-value terms into standalone indexable pages):
- `/glossary/assignment-of-claims` · `/glossary/notice-of-assignment` · `/glossary/progress-payments` · `/glossary/recourse-vs-non-recourse-factoring` · `/glossary/advance-rate` · `/glossary/factoring-fee` · `/glossary/wawf` · `/glossary/dcaa` · `/glossary/net-terms` · `/glossary/accounts-receivable-financing`

---

### TIER 2 — High-Intent Money Satellites
*Map to real bottom-funnel demand. ~6 pages (ServicePage template).*

| Page (route) | Target keyword | Demand | Notes |
|---|---|---|---|
| `/financing/mobilization-funding` | mobilization loan / mobilization funding | Med | Pre-invoice / startup capital; RCA & TFN touch it thinly |
| `/financing/line-of-credit` | government contract line of credit | Low-Med | Satellite to pillar |
| `/financing/purchase-order-financing` | purchase order financing government contracts | Low-Med | Distinct product intent |
| `/for/staffing-payroll-funding` | payroll funding for staffing companies | **Med (best vertical term)** | The standout segment term — real demand + intent |
| `/financing/construction-contract-factoring` | construction contract factoring | Low | Classic high-AR factoring vertical |
| `/government-contract-factoring` (pillar upgrade) | government contract factoring | Med/V.High intent | Rework existing pillar to full altLINE H2 set (What/Benefits/How/Uses/Who/vs/Rates/Requirements/FAQ) |

---

### TIER 3 — Comparison / Consideration
*Evaluation-stage buyers. ~5 pages (ComparePage template).*

| Page (route) | Target keyword | Demand | Notes |
|---|---|---|---|
| `/govcon-financing-vs-sba-loan` | factoring vs SBA loan / CAPLines | Low-Med | Live Oak owns SBA side; GovCon-specific comparison is open |
| `/govcon-financing-vs-traditional-factoring` | government vs commercial factoring | Low | "GovCon factoring is cheaper" angle (1-3% vs 2-5%) |
| `/best-government-contract-factoring-companies` | best government contract factoring companies | Med | Buyer's-guide/listicle where Encore appears favorably (competitors farm this) |
| `/factoring-vs-line-of-credit-government` | invoice factoring vs line of credit | Med | GovCon-specific cut (distinct from existing generic /vs-line-of-credit) |
| `/[competitor]-alternative` (1-2) | e.g. "republic capital access alternative" | Low | Capture competitor-brand intent |

---

### TIER 4 — Conversion Assets
*~4 pages.*

- `/tools/factoring-rate-calculator` — interactive advance-rate/fee calculator (proven link magnet per altLINE; high intent capture)
- `/case-studies/[3 new]` — anonymized deal stories by vertical (staffing, construction, IT) w/ Article schema; mirror eCapital/1stCC "transactions" pattern
- Sector FAQ block reused across pages (set-asides served HERE, not as standalone pages)

---

## Set-Asides — How We Handle Them (per the data)

**We do NOT build new 8a/WOSB/SDVOSB/HUBZone *financing* money pages** (near-zero search demand; 12 `/for/` pages already exist). Instead:
1. Add a reusable **"Financing for set-aside firms" FAQ section** to the pillar + audience pages (captures self-identifying buyers on-page).
2. Keep existing `/for/*` pages; cross-link them from the new authority cluster.

---

## Implementation Approach

**Recommended: refactor to data-driven `[slug]` routes before batch-building** (codebase audit Option B). Today each page is a hand-built file + manual entries in BOTH `lib/links.ts` and `sitemap.ts` (two sources of truth to keep in sync). For 50 pages:
1. Move page data → `src/data/pages/{guides,glossary,services,compare}/*.json` (or `.ts`)
2. Create `[slug]/page.tsx` dynamic routes per type using existing `ServicePage`/`AudiencePage`/`ComparePage` components + `generateStaticParams`/`generateMetadata`
3. **Auto-generate `sitemap.ts` and the `lib/links.ts` PAGES registry from the data files** (kills the dual-source-of-truth problem)
4. Batch-author content per tier

Effort estimate (from playbook teardown): ~50-80 hrs for 50 pages with this approach vs. 200+ hand-built.

---

## Build Order & QA Gate (per CLAUDE.md Build→Test→Ship)

**Order:** Tier 1 (authority) → Tier 2 (money satellites) → Tier 3 (comparison) → Tier 4 (assets).
**Rationale:** authority pages rank fastest and pass link equity *into* the money pages, so they should exist before/with the satellites.

**QA criteria before deploy (each batch):**
- [ ] Every new route returns HTTP 200
- [ ] Each page has unique title, meta description, canonical, JSON-LD (correct schema type)
- [ ] New routes appear in `/sitemap.xml`
- [ ] RelatedLinks renders (internal links wired both directions)
- [ ] Mobile viewport verified
- [ ] No keyword cannibalization (new GovCon-specific /vs/ pages don't duplicate existing generic ones — set distinct canonicals/angles)
- [ ] After deploy: submit updated sitemap in GSC; Request Indexing on Tier-1 + pillar pages

---

## Open Decisions for Eric
1. **Validate volumes** — pull Ahrefs/SEMrush MSV on Tier 1/2 head terms before full build? (Or build on autosuggest signal and let GSC confirm.)
2. **Refactor first vs. hand-build?** — `[slug]` refactor is the right long-term call for 50 pages; hand-building Tier 1 now is faster to first results.
3. **"Best factoring companies" page** — comfortable publishing a buyer's-guide that names competitors (with Encore positioned favorably)?
4. **Calculator scope** — simple fee/advance estimator, or fuller working-capital model?

---

## Sources
Competitor teardown: republiccapitalaccess.com, altline.sobanco.com, fundthrough.com, ecapital.com, 1stcommercialcredit.com, tabbank.com, portercap.com, smbcompass.com, crestmontcapital.com, tfnlending.com, liveoak.bank, advancepartners.com, acquisition.gov (FAR 32.8).
Keyword/SERP: Google autosuggest + live SERPs across seed terms; SBA, SMB Compass, REV Capital, Crestmont guides.
Playbook: govcon-funnels codebase (93 pages, data-driven `[slug]` architecture).
Codebase: encoregov (25 pages, 3 templates, lib/links.ts + sitemap.ts).
