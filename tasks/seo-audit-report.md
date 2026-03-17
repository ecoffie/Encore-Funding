# Encore Funding SEO Audit & Strategy Report
**Date:** March 17, 2026
**Client:** Encore Funding (encore-funding.com + gov.encore-funding.com)
**Prepared by:** GovCon Giants SEO Team

---

## Executive Summary

Encore Funding operates **two separate domains**:
1. **encore-funding.com** - Main site for staffing agency payroll funding
2. **gov.encore-funding.com** - GovCon-focused subdomain for government contractor financing

The company has strong industry credentials (founded by the original Advance Partners team, $25B+ lent) but **significant SEO gaps** that limit organic visibility against well-optimized competitors.

### Key Findings at a Glance

#### Main Domain (encore-funding.com)
| Area | Score | Assessment |
|------|-------|------------|
| Technical SEO | 5/10 | Missing schema, HTTP sitemap links, thin robots.txt |
| Content Depth | 6/10 | 87 blog posts but stale dates, limited topical clusters |
| On-Page SEO | 4/10 | Weak meta descriptions, inconsistent H1 usage |
| Backlink Profile | Unknown | Needs Ahrefs/SEMrush audit |
| Competitive Position | 5/10 | Behind Advance Partners, Porter Capital, Scale Funding |
| Mobile/Speed | 7/10 | WP Rocket optimization present, lazy loading active |

#### GovCon Subdomain (gov.encore-funding.com)
| Area | Score | Assessment |
|------|-------|------------|
| Technical SEO | 4/10 | Same issues as main + subdomain dilutes authority |
| Content Depth | 4/10 | Only 18 blog posts, launched Oct 2024 |
| On-Page SEO | 5/10 | Better H1 usage, still missing schema |
| GovCon Giants Integration | 7/10 | Partnership page exists, Eric Coffie content |
| Competitive Position | 3/10 | New entrant, behind UC Funding, Parabilis, Bankers Factoring |

**Bottom Line:** Encore has content but needs **strategic restructuring, technical fixes, and aggressive content production** to compete for high-value staffing funding keywords. The GovCon subdomain is **diluting SEO authority** and should be evaluated for consolidation.

---

## Google Analytics Baseline (Mar 2025 - Mar 2026)

### Main Site Traffic (encore-funding.com)

| Channel | Sessions | % of Total |
|---------|----------|------------|
| **Total** | **28,877** | 100% |
| Organic Search | 8,172 | 28.3% |
| Paid Search | 7,028 | 24.3% |
| Direct | 6,436 | 22.3% |
| Referral | 2,053 | 7.1% |
| Paid Video | 607 | 2.1% |
| Organic Social | 560 | 1.9% |
| Email | 160 | 0.6% |

**Key Insight:** Organic Search (28.3%) and Paid Search (24.3%) are nearly equal. They're paying for traffic they could get organically with better SEO.

### Main Site Top Pages

| Page | Views | Users | Avg Time |
|------|-------|-------|----------|
| `/` (Homepage) | 18,357 | 8,777 | 41s |
| `/apply-now/` | 4,940 | 3,350 | 18s |
| `/about-us/meet-the-team/` | 3,665 | 2,338 | **1m 28s** |
| `/solutions/funding-options/` | 2,880 | 2,254 | 27s |
| `/solutions/` | 2,058 | 1,762 | 16s |
| `/about-us/` | 1,878 | 1,433 | 22s |
| `/assessment/` | 1,663 | 1,144 | 13s |
| `/contact-us/` | 1,644 | 1,214 | 23s |
| `/resources/recruitment-ebook/` | 1,520 | 1,260 | 13s |

**CRITICAL FINDING:** Zero blog posts in top 10 pages despite having 87 blog posts. Content is not driving traffic.

### GovCon Subdomain Traffic (gov.encore-funding.com)

| Metric | Value |
|--------|-------|
| Total Page Views | 13,827 |
| Total Users | 6,877 |

### GovCon Subdomain Top Pages

| Page | Views | Users | Avg Time |
|------|-------|-------|----------|
| `/` (Homepage) | 7,057 | 3,356 | 42s |
| `/govcon-giants-partner-government-contractor-funding/` | **1,013** | **724** | 24s |
| `/solutions/` | 818 | 551 | 36s |
| `/meet-the-team/` | 727 | 480 | 49s |
| `/apply-now/` | 684 | 455 | 24s |
| `/contact-us/` | 401 | 302 | 23s |
| `/resources/what-is-the-far-beginners-guide-government-contracting/` | 258 | 261 | 22s |

**KEY WIN:** GovCon Giants partnership page is #2 most visited page (10.53% of users). Eric Coffie referrals are converting.

### Combined Totals (Both Properties)

| Metric | Main Site | GovCon Subdomain | Combined |
|--------|-----------|------------------|----------|
| Page Views | 51,384 | 13,827 | **65,211** |
| Users | 21,280 | 6,877 | **~28,000** |
| Organic Sessions | 8,172 | TBD | ~10,000+ |

**The Problem:** 28,000 users split across two domains instead of strengthening one.

---

## THE GOOD

### 1. Strong Brand Story & Credibility
- Founded by original Advance Partners team (Joel Adelman)
- $25B+ lending history provides trust signals
- Family-owned positioning differentiates from Paychex corporate (Advance Partners)
- Multiple case studies demonstrating real client success

### 2. Existing Content Foundation
- **87 blog posts** in sitemap (significant content library)
- Recent content activity (Feb 2026 posts)
- Case studies covering multiple verticals:
  - IT staffing
  - Healthcare staffing
  - Light industrial
  - Professional services
- Industry association involvement (IFA board membership)

### 3. Service Page Coverage
- Government contract financing page exists
- Full-service vs money-only factoring differentiation
- Industry vertical pages (healthcare, transportation)
- Assessment tools / interactive content

### 4. Technical Foundation
- WordPress + Beaver Builder (manageable CMS)
- WP Rocket lazy loading optimization
- Yoast SEO plugin installed (generates sitemaps)
- Mobile responsive design
- HTTPS enabled

### 5. Competitive Positioning
- Positioned as entrepreneur-focused vs corporate Advance Partners
- Flexible terms messaging
- Back-office + funding combined offering
- "Underfunded and overlooked" entrepreneur messaging resonates with target market

---

## THE BAD

### 1. Technical SEO Issues

#### Sitemap Problems
```
ISSUE: Sitemap uses HTTP instead of HTTPS
http://www.encore-funding.com/post-sitemap.xml (should be https://)
```
- All 7 sub-sitemaps reference HTTP URLs
- Can cause indexing inconsistencies
- Google may flag mixed content

#### Missing Schema Markup
- **No Organization schema** detected
- **No LocalBusiness schema** (they have physical address)
- **No FAQ schema** on FAQ pages
- **No Article/BlogPosting schema** on blog posts
- **No BreadcrumbList schema**
- Competitors (Porter Capital, Scale Funding) implement schema

#### Robots.txt Too Permissive
```
User-Agent: *
Disallow:
```
- No sitemap reference
- No crawl directives for admin areas
- Should block `/wp-admin/`, `/wp-includes/`

#### Thin Meta Descriptions
- Many pages missing explicit meta descriptions
- Truncated titles in search results
- Inconsistent keyword targeting in titles

### 2. Content Strategy Gaps

#### Stale Content
- **28 posts** dated June 2023 (bulk backdate?)
- Many "2023" posts ranking for 2026 searches = outdated
- No systematic content refresh program

#### Missing High-Value Content
| Keyword Opportunity | Status | Competitor Doing It |
|---------------------|--------|---------------------|
| "what is invoice factoring" (definition) | Have it but thin | Competitors rank higher |
| "staffing agency business plan template" | Blog post only | Scale Funding has dedicated page |
| "payroll funding calculator" | MISSING | Opportunity |
| "staffing factoring rates comparison" | MISSING | High intent keyword |
| "government contractor staffing funding" | Page exists | Needs optimization |
| "healthcare staffing payroll funding" | Blog only | Needs service page |

#### Topical Authority Gaps
- No pillar page strategy
- Blog posts not interlinked strategically
- No content hubs around key topics:
  - Starting a staffing agency
  - Cash flow management
  - Industry-specific guides (IT, healthcare, industrial)

### 3. On-Page SEO Weaknesses

#### Title Tag Issues
- Homepage: "Payroll & Invoice Factoring | Staffing Agency Funding | Encore Funding"
  - Too many pipe separators
  - Brand at end (good)
  - Could be more compelling

#### H1 Tag Inconsistency
- Some pages have multiple H1s (Beaver Builder issue)
- H1s don't always contain target keywords

#### Internal Linking
- Weak internal link architecture
- Blog posts don't link back to service pages
- No breadcrumb navigation visible

### 4. Competitive Disadvantages

| Competitor | Advantage Over Encore |
|------------|----------------------|
| **Advance Partners** | Paychex backing, "23% annual client growth" stat, stronger brand recognition |
| **Porter Capital** | 85-95% advance rates prominently featured, $25M monthly capacity |
| **Scale Funding** | Better content structure, clear pillar pages, modern design |
| **Viva Capital** | Same-day funding emphasis, 100% advance rates, bilingual support |
| **1st Commercial Credit** | Transparent rate display (0.69-1.59%), educational content depth |

---

## THE UGLY

### 1. Critical Technical Failures

#### HTTP/HTTPS Mixed Content
- Sitemap index references HTTP URLs
- Potential duplicate content issues
- Can hurt Core Web Vitals scores

#### Jobs Sitemap Stale
```
jobs-sitemap.xml: Last Modified 2022-05-05
```
- 4+ years old
- If no jobs, should be removed
- Signals neglected technical maintenance

#### Author Sitemap Issues
- Multiple author sitemaps (authors-sitemap.xml AND author-sitemap.xml)
- Could cause crawl budget waste

### 2. Keyword Cannibalization Risk

Multiple pages targeting similar terms:
- "Starting a staffing agency" appears on:
  - `/who-we-serve/staffing-agency-start-ups/`
  - `/resources/starting-a-staffing-agency/`
  - `/resources/how-staffing-agencies-make-money-in-their-first-year/`
  - Multiple business plan posts

No clear hierarchy = Google doesn't know which to rank.

### 3. Conversion Path Issues

#### Form Placement
- CTAs scattered inconsistently
- No clear primary conversion path
- Assessment tools exist but not promoted in content

#### Trust Signals
- No visible BBB rating badge
- No Google reviews widget
- Testimonials exist but not schema-marked

### 4. Local SEO Neglected

- Address: 30100 Chagrin Blvd, Suite 350, Pepper Pike, OH 44124
- **No Google Business Profile optimization visible**
- **No LocalBusiness schema**
- Missing location-based content
- Competitors not targeting local = opportunity

### 5. Backlink Profile Concerns (Requires Tool Audit)

Without Ahrefs/SEMrush access, likely issues include:
- Limited referring domains vs competitors
- No active link building program
- No guest post strategy
- No HARO/journalist outreach
- Competitors acquiring industry publication links

---

## GovCon Subdomain Analysis (gov.encore-funding.com)

### Overview

Encore launched **gov.encore-funding.com** in October 2024 as a dedicated site for government contractor financing. This is separate from the main staffing-focused domain.

### Site Structure

| Page Type | Count | Notes |
|-----------|-------|-------|
| Core Pages | 10 | Home, Solutions, FAQs, Team, Contact, Apply |
| Blog Posts | 18 | GovCon-focused content |
| Case Studies | 2 | IT services + professional services |
| Partnership Page | 1 | GovCon Giants co-branded page |

### Content Inventory (gov.encore-funding.com)

**Blog Posts (18 total):**
| Title | Last Modified |
|-------|---------------|
| Alternative Government Contractor Financing | Nov 2024 |
| Encore Funding Expands Commitment to Government Contractors | Nov 2024 |
| Government Contractor Funding to Enhance Credibility | Nov 2024 |
| Debriefings: A Guide for Government Contractors | May 2025 |
| How to Use Government Contracts to Make Your First 100k | May 2025 |
| How to Start Earning from Government Contracts | May 2025 |
| What is the FAR: Beginners Guide | May 2025 |
| Top Three Common Mistakes New Contractors Make | May 2025 |
| Top Three Government Contracting Trends | May 2025 |
| Networking Strategies for Government Contractors | May 2025 |
| The Role of Technology in Government Contracting | May 2025 |
| Building Trust with Government Agencies | May 2025 |
| Emerging Trends in Federal Contracting | May 2025 |
| 5 Reasons to Get Your Woman-Owned Business Certification | May 2025 |
| 5 Mistakes to Avoid in Government Contracting | Jun 2025 |
| How to Find the Right Agencies for Your Business | Jul 2025 |
| Case Study: Fueling Rapid Growth with GovCon Financing | Aug 2025 |
| Case Study: How GovCon Financing Ramped Up IT Services Growth | Aug 2025 |

### GovCon Subdomain: THE GOOD

1. **Dedicated GovCon Focus** - Clear targeting of government contractor financing
2. **GovCon Giants Partnership** - Co-branded page with Eric Coffie content
3. **Relevant Content Topics** - FAR guide, WOSB certification, agency finding
4. **Association Affiliations** - NVSBC, OMSDC, ASBCC, TempNet logos displayed
5. **Case Studies** - Two real client success stories
6. **Clear Value Props** - 90% advance, same-day funding, financial support letters
7. **GA + GTM Tracking** - Analytics properly implemented

### GovCon Subdomain: THE BAD

1. **Subdomain vs Subfolder Architecture**
   - **CRITICAL:** Using subdomain (gov.encore-funding.com) instead of subfolder (encore-funding.com/govcon/)
   - Subdomains are treated as separate sites by Google
   - **Splits domain authority** between two sites
   - Main site's 87 blog posts don't benefit GovCon subdomain

2. **Thin Content Volume**
   - Only 18 blog posts (vs 87 on main site)
   - Launched Oct 2024 = still young domain
   - Competitors have more content depth

3. **Same Technical Issues as Main Site**
   - Thin robots.txt (no sitemap reference)
   - No schema markup detected
   - Missing meta descriptions on many pages

4. **Duplicate Author Issues**
   - Both authors-sitemap.xml AND author-sitemap.xml exist
   - our-team-sitemap.xml AND department-sitemap.xml separate

5. **Content Publish Gaps**
   - May 2025: 10 posts published (bulk upload)
   - Then silence until Aug 2025
   - No consistent publishing cadence

### GovCon Subdomain: THE UGLY

1. **SEO Authority Dilution**
   ```
   PROBLEM: Two separate domains = two separate SEO profiles

   Main site DA: ~XX (estimated)
   GovCon subdomain DA: Lower (newer, fewer links)

   If consolidated: Combined authority would rank better
   ```

2. **Keyword Cannibalization Risk**
   - Main site has `/solutions/funding-options/government-contract-financing/`
   - GovCon subdomain has entire site for same topic
   - Google may not know which to rank

3. **Link Equity Split**
   - Any backlinks to gov.encore-funding.com don't help main domain
   - GovCon Giants partnership links go to subdomain, not main site
   - Eric Coffie content exists on subdomain only

4. **No Cross-Linking Strategy**
   - Main site doesn't prominently link to GovCon subdomain
   - GovCon subdomain doesn't link back to main site resources
   - Two siloed properties

### GovCon Competitor Landscape

| Competitor | Strength |
|------------|----------|
| **UC Funding (ucfunding.com/govcon)** | Dedicated GovCon page on main domain |
| **Parabilis** | Pure GovCon focus, transparent pricing |
| **Bankers Factoring** | 25+ years experience, strong content |
| **Business Factors** | Federal/state/local coverage |
| **Capital Source Group** | Inc. 5000 ranked |
| **SMB Compass** | Prime + subcontractor coverage |

### GovCon Subdomain Recommendations

**Option A: Consolidate (Recommended)**
1. Migrate gov.encore-funding.com content to encore-funding.com/govcon/
2. 301 redirect all subdomain URLs to new subfolder paths
3. Combine domain authority into single property
4. Cross-link GovCon content with staffing content
5. Keep GovCon Giants partnership prominent

**Option B: Keep Subdomain (If business reasons require)**
1. Treat as separate SEO project with own strategy
2. Build dedicated backlinks to subdomain
3. Increase content velocity (weekly posts)
4. Implement full technical SEO fixes
5. Accept it will rank slower than consolidated approach

**Estimated Impact of Consolidation:**
- +20-30% faster ranking potential
- Combined backlink profile benefits all content
- Single Google Search Console property
- Unified content strategy
- Better internal linking opportunities

---

## Competitive Landscape Analysis

### Direct Competitors - SEO Maturity Assessment

| Company | Est. DA* | Content Volume | Schema | Blog Frequency | Threat Level |
|---------|----------|----------------|--------|----------------|--------------|
| advancepartners.com | 45-55 | High | Yes | Monthly | HIGH |
| portercap.com | 40-50 | Medium | Yes | Bi-weekly | MEDIUM |
| getscalefunding.com | 35-45 | High | Yes | Weekly | HIGH |
| vivacf.net | 30-40 | Medium | Partial | Monthly | MEDIUM |
| payrollfunding.com | 35-45 | High | Yes | Weekly | HIGH |
| 1stcommercialcredit.com | 40-50 | Very High | Yes | Daily | HIGH |

*Estimated Domain Authority - requires tool verification

### Keyword Opportunity Matrix - Staffing (Main Site)

| Keyword | Est. Monthly Volume | Difficulty | Encore Current Rank | Opportunity |
|---------|---------------------|------------|---------------------|-------------|
| payroll funding | 1,000-2,000 | Medium | Not ranking | HIGH |
| invoice factoring | 5,000-8,000 | High | Not top 20 | MEDIUM |
| staffing agency funding | 500-800 | Medium | Unknown | HIGH |
| payroll factoring | 500-1,000 | Medium | Unknown | HIGH |
| how to start a staffing agency | 2,000-4,000 | Medium | Have content | OPTIMIZE |
| staffing agency business plan | 1,000-2,000 | Medium | Have content | OPTIMIZE |
| healthcare staffing funding | 200-400 | Low | Blog only | HIGH |
| IT staffing funding | 100-200 | Low | Blog only | HIGH |
| temporary staffing payroll | 200-400 | Low | Content exists | OPTIMIZE |

### Keyword Opportunity Matrix - GovCon (Subdomain)

| Keyword | Est. Monthly Volume | Difficulty | Current Status | Opportunity |
|---------|---------------------|------------|----------------|-------------|
| government contract financing | 300-500 | Low | Have content | QUICK WIN |
| government contractor funding | 200-400 | Low | Have content | OPTIMIZE |
| government invoice factoring | 100-200 | Low | Mentioned | HIGH |
| federal contractor financing | 100-200 | Low | Partial | HIGH |
| government contract factoring | 100-200 | Low | Have content | OPTIMIZE |
| 8a contractor funding | 50-100 | Very Low | Mentioned | QUICK WIN |
| small business government funding | 500-800 | Medium | Not targeting | HIGH |
| how to start government contracting | 1,000-2,000 | Medium | Have content | OPTIMIZE |
| government contract cash flow | 50-100 | Very Low | Have content | QUICK WIN |
| assignment of claims | 100-200 | Low | Not covered | HIGH |
| WOSB certification | 500-1,000 | Medium | Have content | OPTIMIZE |
| FAR guide | 200-400 | Low | Have content | OPTIMIZE |

---

## Immediate Action Items (Next 30 Days)

### Priority 1: Technical Fixes (Week 1)

- [ ] Fix sitemap HTTPS issue (update Yoast settings)
- [ ] Add sitemap reference to robots.txt
- [ ] Block `/wp-admin/` and `/wp-includes/` in robots.txt
- [ ] Remove or update stale jobs-sitemap.xml
- [ ] Consolidate author sitemaps
- [ ] Implement Organization schema site-wide
- [ ] Add LocalBusiness schema with NAP data
- [ ] Add FAQ schema to FAQ page
- [ ] Add Article schema to blog posts

### Priority 2: On-Page Quick Wins (Week 2)

- [ ] Rewrite homepage title tag (more compelling)
- [ ] Add meta descriptions to top 20 pages
- [ ] Fix H1 tag issues (one H1 per page)
- [ ] Add breadcrumb navigation
- [ ] Implement internal linking strategy
- [ ] Add schema to case study pages

### Priority 3: Content Optimization (Weeks 3-4)

- [ ] Update all 2023-dated posts with fresh content
- [ ] Create "Ultimate Guide to Payroll Funding" pillar page
- [ ] Optimize government contract financing page
- [ ] Build healthcare staffing dedicated service page
- [ ] Build IT staffing dedicated service page
- [ ] Create payroll funding calculator tool

### Priority 4: GovCon Subdomain Decision (Week 2)

**CRITICAL DECISION REQUIRED:**

- [ ] **Decide: Consolidate subdomain or keep separate?**
  - If consolidate: Plan migration to encore-funding.com/govcon/
  - If keep separate: Treat as second SEO project

**If Consolidating (Recommended):**
- [ ] Map all gov.encore-funding.com URLs to new subfolder paths
- [ ] Create 301 redirects for every page
- [ ] Migrate GovCon Giants partnership page
- [ ] Update Google Search Console
- [ ] Notify GovCon Giants of URL changes
- [ ] Update all external links (Eric Coffie content, etc.)

**If Keeping Subdomain:**
- [ ] Fix robots.txt on subdomain (add sitemap reference)
- [ ] Implement schema markup on subdomain
- [ ] Build dedicated backlink strategy for subdomain
- [ ] Increase publishing cadence to weekly
- [ ] Create GovCon-specific pillar pages:
  - "Government Contract Financing: Complete Guide"
  - "How to Start Government Contracting"
  - "8(a) Contractor Funding Guide"
- [ ] Target featured snippets for "what is" GovCon questions

---

## 12-Month SEO & Content Strategy

### Phase 1: Foundation (Months 1-3)

**Focus:** Technical fixes, content audit, competitive gap closure

#### Month 1
- Complete all technical SEO fixes
- Audit and update top 30 blog posts
- Implement schema across all templates
- Set up Google Search Console monitoring
- Baseline current rankings with SEMrush/Ahrefs

#### Month 2
- Create 3 pillar pages:
  1. "Payroll Funding: Complete Guide for Staffing Agencies"
  2. "Invoice Factoring Explained: How It Works"
  3. "Starting a Staffing Agency: Step-by-Step Guide"
- Publish 4 new blog posts (weekly cadence)
- Build internal linking structure around pillars
- Submit updated sitemaps to Google

#### Month 3
- Create industry vertical pages:
  - Healthcare staffing funding
  - IT staffing funding
  - Light industrial staffing funding
- Launch payroll funding calculator
- Publish 4 new blog posts
- Begin guest post outreach

### Phase 2: Growth (Months 4-6)

**Focus:** Keyword expansion, link building, content velocity

#### Month 4
- Target "comparison" keywords:
  - "payroll funding vs bank loan"
  - "factoring vs line of credit"
  - "Encore Funding vs Advance Partners"
- Publish 6 blog posts
- Secure 3-5 industry publication backlinks
- Optimize for Google Business Profile

#### Month 5
- Create "Staffing Success" video series
- Launch podcast or webinar content
- Build state-specific landing pages (Texas, California, Ohio)
- Publish 6 blog posts
- Continue link building

#### Month 6
- Create downloadable resources:
  - Staffing agency business plan template
  - Cash flow calculator spreadsheet
  - Compliance checklist
- Publish 6 blog posts
- Mid-point audit and strategy adjustment

### Phase 3: Authority (Months 7-9)

**Focus:** Thought leadership, brand building, competitive positioning

#### Month 7
- Launch "Founder Stories" interview series
- Create industry trend reports
- Target featured snippets for key questions
- Publish 6 blog posts
- Guest post on staffing industry publications

#### Month 8
- Build scholarship or industry award program
- Create annual "State of Staffing Funding" report
- Partner with staffing associations for content
- Publish 6 blog posts

#### Month 9
- Optimize for AI/voice search queries
- Create FAQ expansion content
- Target "People Also Ask" opportunities
- Publish 6 blog posts

### Phase 4: Domination (Months 10-12)

**Focus:** Market leadership, aggressive keyword capture

#### Month 10
- Target competitor branded keywords strategically
- Create comparison pages
- Expand to adjacent keywords (business funding, SBA alternatives)
- Publish 8 blog posts

#### Month 11
- Launch user-generated content program
- Feature client success stories prominently
- Build review acquisition strategy
- Publish 8 blog posts

#### Month 12
- Comprehensive annual audit
- Plan Year 2 strategy
- Document wins and learnings
- Publish 8 blog posts
- Celebrate ranking improvements!

---

## KPIs & Measurement

### Monthly Tracking Metrics (BASELINES SET FROM GA4)

| Metric | Baseline (12mo) | Month 6 Target | Month 12 Target |
|--------|-----------------|----------------|-----------------|
| **Main Site Organic Sessions** | 8,172 | 12,258 (+50%) | 20,430 (+150%) |
| **Main Site Total Sessions** | 28,877 | 36,000 (+25%) | 50,000 (+73%) |
| **GovCon Subdomain Users** | 6,877 | 10,315 (+50%) | 17,192 (+150%) |
| **GovCon Giants Page Views** | 1,013 | 2,000 (+100%) | 4,000 (+300%) |
| **Blog Posts in Top 10 Pages** | 0 | 3 posts | 10 posts |
| **FAR Guide Page Views** | 258 | 1,000 (+287%) | 3,000 (+1,063%) |
| Keyword Rankings (Top 10) | ~0 | 15 keywords | 50 keywords |
| Keyword Rankings (Top 3) | ~0 | 5 keywords | 20 keywords |
| Domain Authority | TBD (need Ahrefs) | +5 points | +12 points |
| Referring Domains | TBD (need Ahrefs) | +30 | +100 |
| Blog Posts Published | 87 existing | +24 new | +72 total new |

### Traffic Quality Targets

| Metric | Current | Target |
|--------|---------|--------|
| Organic % of Total Traffic | 28.3% | 45%+ |
| Paid Search Dependency | 24.3% | 15% (reduce spend) |
| Meet the Team Avg Time | 1m 28s | Maintain (trust signal) |
| Apply Now Conversions | TBD | +50% |

### GovCon Giants Partnership KPIs

| Metric | Current (12mo) | 6-Month Target | 12-Month Target |
|--------|----------------|----------------|-----------------|
| Partnership Page Views | 1,013 | 2,000 | 4,000 |
| Partnership Page Users | 724 | 1,500 | 3,000 |
| Eric Coffie Content Views | 258 (FAR guide) | 1,500 | 5,000 |
| GovCon Blog Traffic | Minimal | 2,000 sessions | 8,000 sessions |

### Reporting Cadence

- **Weekly:** Rankings tracker, content published
- **Monthly:** Full traffic report, conversion analysis, competitor comparison
- **Quarterly:** Strategy review, pivot recommendations

---

## Tools Recommended

### Essential (Must Have)
1. **Ahrefs or SEMrush** - Keyword tracking, backlink analysis, competitor research
2. **Google Search Console** - Indexing, search performance, technical issues
3. **Google Analytics 4** - Traffic, conversions, user behavior
4. **Screaming Frog** - Technical SEO audits
5. **Surfer SEO** - Content optimization

### Nice to Have
6. **Clearscope** - Content optimization
7. **Schema Pro** - WordPress schema management
8. **Rank Math or Yoast Premium** - On-page SEO
9. **BrightLocal** - Local SEO tracking
10. **HARO** - Journalist outreach for backlinks

---

## Investment Estimate

### One-Time Setup (Month 1)
- Technical SEO fixes: 20-30 hours
- Content audit and optimization: 40-50 hours
- Schema implementation: 10-15 hours
- Tool setup and baseline: 10-15 hours

### Ongoing Monthly
- Content creation (6-8 posts): 24-32 hours
- Link building: 15-20 hours
- Technical maintenance: 5-10 hours
- Reporting and analysis: 5-8 hours

---

## Next Steps

1. **Schedule GA4 access** - Review current traffic, top pages, conversion data
2. **Run Ahrefs/SEMrush audit** - Get exact domain authority, backlink profile
3. **Prioritize fixes** - Use this report to create sprint tickets
4. **Assign content calendar** - Lock in first 90 days of publishing
5. **Weekly check-ins** - Review progress against KPIs

---

## Appendix

### A. Competitor URLs for Reference

**Staffing Funding Competitors:**
- https://www.advancepartners.com/
- https://portercap.com/payroll-funding-for-staffing-companies/
- https://getscalefunding.com/industries/staffing-factoring/
- https://vivacf.net/staffing/
- https://payrollfunding.com/
- https://www.1stcommercialcredit.com/factoring-staffing-recruitment-lending

**GovCon Funding Competitors:**
- https://ucfunding.com/govcon/
- https://parabilis.com/
- https://www.bankersfactoring.com/government-factoring/
- https://businessfactors.com/industries/government-contract-financing/
- https://capitalsourcegroup.com/
- https://www.smbcompass.com/government-contract-financing/
- https://www.comcapfactoring.com/blog/financing-invoices-government-contracts/
- https://newfrontierfunding.com/financing-for-government-contracts-guide/

### B. High-Value Keyword Targets

**Staffing Keywords (Main Site)**
1. payroll funding
2. invoice factoring
3. staffing agency funding
4. payroll factoring
5. staffing invoice factoring
6. how to start a staffing agency
7. staffing agency business plan
8. healthcare staffing funding
9. IT staffing funding
10. payroll funding for staffing companies
11. factoring for staffing agencies
12. staffing cash flow solutions
13. back office for staffing
14. temporary staffing funding
15. light industrial staffing funding

**GovCon Keywords (Subdomain or Consolidated)**
16. government contract financing
17. government contractor funding
18. government invoice factoring
19. federal contractor financing
20. 8a contractor funding
21. government contract factoring
22. assignment of claims act
23. small business government contract funding
24. WOSB certification benefits
25. FAR compliance guide
26. government contract cash flow
27. federal receivables factoring
28. government subcontractor funding
29. how to start government contracting
30. government contract working capital

### C. Content Gap Analysis - Missing Topics
- [ ] Payroll funding calculator
- [ ] State-by-state staffing guides
- [ ] Staffing industry statistics/reports
- [ ] Video tutorials
- [ ] Podcast content
- [ ] Interactive assessment tools (more)
- [ ] Comparison guides
- [ ] ROI calculators
- [ ] Compliance resources by state
- [ ] Staffing software integrations guide

---

*Report prepared for Encore Funding SEO engagement. Data accurate as of March 17, 2026.*
