# Encore Funding SEO Testing & Evaluation Criteria
**Version:** 1.0
**Last Updated:** March 17, 2026

---

## Purpose

This document establishes testing criteria for evaluating Encore Funding SEO work before marking any task complete. Use this checklist after EVERY change.

---

## Technical SEO Verification

### Before ANY Deploy

- [ ] **Sitemap Valid**: Run `curl https://www.encore-funding.com/sitemap.xml` - returns 200
- [ ] **Sitemap HTTPS**: All URLs in sitemap use HTTPS (not HTTP)
- [ ] **Robots.txt Accessible**: `curl https://www.encore-funding.com/robots.txt` - valid directives
- [ ] **Schema Validates**: Test at https://validator.schema.org/
- [ ] **Mobile Friendly**: Test at https://search.google.com/test/mobile-friendly
- [ ] **Core Web Vitals**: Test at https://pagespeed.web.dev/

### After Page Changes

- [ ] Page returns HTTP 200
- [ ] Canonical URL is correct
- [ ] Meta title under 60 characters
- [ ] Meta description under 160 characters
- [ ] Exactly one H1 tag present
- [ ] H1 contains target keyword
- [ ] Images have alt text
- [ ] Internal links work (no 404s)
- [ ] Schema present and valid
- [ ] Page loads under 3 seconds

---

## Content Quality Checks

### Every Blog Post Must Have

- [ ] Unique meta title (not duplicated elsewhere)
- [ ] Unique meta description (not duplicated elsewhere)
- [ ] H1 matches title intent
- [ ] Minimum 1,000 words for pillar content
- [ ] Minimum 500 words for regular posts
- [ ] At least 2-3 internal links to related content
- [ ] At least 1 link to service page
- [ ] Target keyword in first 100 words
- [ ] Target keyword in at least one H2
- [ ] At least one image with descriptive alt text
- [ ] Clear CTA (call to action)
- [ ] Author attribution
- [ ] Publish date accurate
- [ ] Article schema implemented

### Content Freshness

- [ ] No dates older than 18 months (update if so)
- [ ] Statistics cited are from last 2 years
- [ ] External links still work
- [ ] Information is current and accurate

---

## On-Page SEO Verification

### Title Tag Checklist
```
✓ Under 60 characters (or 600 pixels)
✓ Contains primary keyword
✓ Brand name present (at end preferred)
✓ Compelling - would you click it?
✓ No duplicate titles on site
```

### Meta Description Checklist
```
✓ Under 160 characters
✓ Contains primary keyword
✓ Includes call to action
✓ Describes page accurately
✓ No duplicate descriptions on site
```

### URL Structure Checklist
```
✓ Contains keyword (hyphens, not underscores)
✓ Under 75 characters
✓ No special characters
✓ Lowercase
✓ No dates in URL (unless news)
```

### Header Hierarchy
```
✓ Single H1 per page
✓ H2s break up main sections
✓ H3s subdivide H2 sections
✓ Headers contain keywords naturally
✓ Logical hierarchy (no H3 before H2)
```

---

## Schema Markup Validation

### Site-Wide Schema
- [ ] **Organization Schema**: Name, URL, logo, contact info
- [ ] **LocalBusiness Schema**: Address, phone, hours
- [ ] **WebSite Schema**: SearchAction enabled

### Page-Type Schema
| Page Type | Required Schema |
|-----------|-----------------|
| Homepage | Organization + WebSite |
| Service Pages | Service + BreadcrumbList |
| Blog Posts | Article/BlogPosting + BreadcrumbList |
| FAQ Page | FAQPage |
| Contact Page | LocalBusiness |
| Team Page | Person (for each team member) |
| Case Studies | Article + Review (if testimonial) |

### Schema Testing Process
1. Copy page URL
2. Go to https://search.google.com/test/rich-results
3. Enter URL
4. Confirm "Eligible for rich results"
5. Check for errors/warnings
6. Screenshot result for records

---

## Competitive Position Tracking

### Weekly Keyword Checks

Track these keywords in Ahrefs/SEMrush:

| Keyword | Target Position | Check Date | Current Rank |
|---------|-----------------|------------|--------------|
| payroll funding | Top 10 | Weekly | ___ |
| invoice factoring | Top 20 | Weekly | ___ |
| staffing agency funding | Top 10 | Weekly | ___ |
| payroll factoring | Top 10 | Weekly | ___ |
| staffing invoice factoring | Top 10 | Weekly | ___ |
| how to start a staffing agency | Top 5 | Weekly | ___ |
| government contract financing | Top 5 | Weekly | ___ |
| healthcare staffing funding | Top 5 | Weekly | ___ |

### Monthly Competitor Audit

For each competitor, record:
- [ ] New content published (topic, URL)
- [ ] New backlinks acquired (source, type)
- [ ] Ranking changes for target keywords
- [ ] New features/tools launched
- [ ] Design or UX changes

---

## Link Building Quality Criteria

### Acceptable Backlinks
- [ ] Domain Authority 25+
- [ ] Relevant to staffing/finance industry
- [ ] Editorial link (not paid/sponsored)
- [ ] Followed link (not nofollow only)
- [ ] From real website (not PBN)
- [ ] Contextual placement in content
- [ ] Anchor text varies naturally

### Red Flags (Avoid)
- Sites with DA under 15
- Obvious link farms
- Irrelevant industries
- Excessive reciprocal links
- Sites primarily in other languages
- Thin/duplicate content sites

---

## Conversion Tracking Setup

### Required GA4 Events

- [ ] `form_submit` - Contact form submissions
- [ ] `application_start` - Funding application started
- [ ] `application_complete` - Funding application finished
- [ ] `phone_click` - Click-to-call
- [ ] `email_click` - Email link clicks
- [ ] `chat_open` - Live chat initiated
- [ ] `resource_download` - PDF/guide downloads
- [ ] `video_play` - Video engagement

### Conversion Goals (Monthly)

| Goal | Baseline | Target |
|------|----------|--------|
| Form submissions | TBD | +20% MoM |
| Applications started | TBD | +15% MoM |
| Phone calls | TBD | Track |
| Resource downloads | TBD | +25% MoM |

---

## Google Search Console Monitoring

### Daily Checks
- [ ] No manual actions
- [ ] No security issues
- [ ] Index coverage stable

### Weekly Checks
- [ ] New indexed pages appear
- [ ] No crawl errors increasing
- [ ] Core Web Vitals passing
- [ ] Mobile usability OK

### Monthly Analysis
- [ ] Top queries trending up
- [ ] Click-through rate improving
- [ ] Average position improving
- [ ] New backlinks appearing
- [ ] International targeting correct

---

## Content Calendar Compliance

### Weekly Requirements
- [ ] 1-2 blog posts published
- [ ] Posts optimized before publish
- [ ] Posts interlinked to existing content
- [ ] Social shares scheduled
- [ ] Email newsletter inclusion

### Monthly Requirements
- [ ] 6-8 total new content pieces
- [ ] 1 pillar content update
- [ ] 1 new backlink acquired
- [ ] 5 old posts refreshed
- [ ] Competitor content gap analyzed

### Quarterly Requirements
- [ ] Full technical audit
- [ ] Content performance review
- [ ] Strategy adjustment meeting
- [ ] ROI calculation
- [ ] Next quarter planning

---

## Reporting Requirements

### Weekly Report (Internal)
- Pages indexed count
- Keyword ranking changes
- Content published
- Technical issues found
- Backlinks acquired

### Monthly Report (Client)
1. **Executive Summary**: 3-5 bullet wins
2. **Traffic Overview**: Organic sessions, users, pageviews
3. **Ranking Progress**: Target keyword positions
4. **Content Performance**: Top pages, new content metrics
5. **Technical Health**: Errors, warnings, fixes
6. **Competitive Analysis**: Position vs competitors
7. **Conversions**: Leads, applications, downloads
8. **Next Month Plan**: Priorities and goals

### Quarterly Business Review
- ROI analysis
- Strategy effectiveness
- Market position change
- Recommendations for next quarter
- Budget review

---

## Emergency Protocols

### If Traffic Drops >20% Suddenly
1. Check Google Search Console for manual actions
2. Check for algorithm update (Google Search Status)
3. Review recent site changes
4. Check competitor rankings (did they surge?)
5. Audit technical issues (site down, robots.txt blocked)
6. Document findings
7. Create recovery plan

### If Ranking Drops Significantly
1. Identify affected pages/keywords
2. Check for content changes
3. Review backlink profile (lost links?)
4. Check competitor changes
5. Evaluate SERP changes (new features?)
6. Plan recovery action

---

## Tool Access Requirements

### Must Have Access To:
- [ ] Google Analytics 4 (Admin)
- [ ] Google Search Console (Owner)
- [ ] WordPress Admin (Editor+)
- [ ] Ahrefs OR SEMrush (Full access)
- [ ] Screaming Frog (Licensed)
- [ ] Google Looker Studio (for reporting)

### Nice to Have:
- [ ] Surfer SEO
- [ ] Clearscope
- [ ] BrightLocal
- [ ] Rank Math Pro

---

## Approval Workflow

### Before Publishing Content
1. Writer completes draft
2. SEO review (checklist above)
3. Editorial review (quality/accuracy)
4. Client approval (if required)
5. Schedule publish
6. Post-publish verification

### Before Technical Changes
1. Document current state
2. Create backup
3. Implement in staging (if possible)
4. Test thoroughly
5. Implement in production
6. Verify no regressions
7. Document change

---

*Use this document for every SEO task. No exceptions.*
