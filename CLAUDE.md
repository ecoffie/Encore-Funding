# Encore Funding 2026 Proposal - Change Log

## Project Overview
HTML proposal document for Encore Funding x GovCon Giants 2026 Strategic Partnership.

**Original File (browser-first):** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/Encore_Funding_2026_Sponsorship_Proposal.html`

**Print-First PDF File:** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/Encore_Funding_2026_Proposal_PDF.html`

**PDF Output:** `/Users/ericcoffie/Downloads/Encore_Funding_2026_Proposal_PRINT_READY.pdf`

**2026 Letter Contract (.docx):** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/GCG Encore Funding Letter Contract 2026.docx`

**2026 Letter Contract (HTML draft):** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/Encore_Funding_2026_Letter_Contract.html`

**Previous Letter Contracts:** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/GCG Encore Funding Letter Contract.pdf` (2024), `GCG Encore Funding Letter Contract rev1.pdf` (2025)

**Git Remotes:**
- `origin` → https://github.com/ecoffie/Encore-Funding (dashboard/Vercel)
- `encoregov` → https://github.com/ecoffie/encoregov

---

## Changes Made (February 2026)

### Rights & Benefits Section - Screenshots
- Updated all 10 Rights & Benefits pages with actual screenshots
- Changed from `[ Screenshot ]` text placeholders to actual `<img>` tags
- All images placed in `images/` folder (Google Drive location)
- LinkedIn Management section expanded to show 2 stacked images

**Image files (all populated):**
| Filename | Description |
|----------|-------------|
| `fhc.png` | Federal Help Center platform with Encore branding |
| `youtube.png` | YouTube video with Encore logo bug in corner |
| `podcast.png` | Podcast episode with Encore sponsorship |
| `webinar.png` | Webinar registration page with co-branding |
| `email.png` | Newsletter with Encore logo |
| `preferred-partner.png` | FHC Preferred Partners page (replaced on page 15) |
| `website-encore.png` | Encore Funding website screenshot (now used on page 15) |
| `social-media.png` | Instagram/LinkedIn post featuring Encore |
| `brand-ambassador.png` | Eric Coffie at GovCon conference |
| `linkedin-management.png` | Encore GovCon LinkedIn page |
| `linkedin-management-2.png` | Encore LinkedIn post example |
| `recompete-tracker.png` | Recompete Tracker platform screenshot |

### Podcast Numbers
- Corrected podcast download numbers throughout document
- Changed from 195K/195,543 to **9,292 downloads**
- Updated in: Rights & Benefits section, Appendix branding section, Performance Scorecard

### Brand Ambassador Events
- Changed from "3-5 events" to **"3 events"** throughout document
- Updated in all locations: 2026 Proposed Contract, Rights & Benefits, Deliverables table, Brand Ambassador Program, Strategic Partnership Summary, Value Breakdown table

### 2025 Performance Review Section
- Removed screenshot placeholders from "2025 Encore Branding In Action" sections
- Converted to clean card-based layout showing only results/stats
- Removed the "Note: Replace [ Screenshot ]..." alert

### Removed Sections
- **Partnership Terms** - Removed (payment terms, contract term, reporting, exclusivity)
- **Agreement Acceptance** - Removed (signature lines for both parties)
- Rationale: This is a proposal, not a contract

### Recompete Tracker License (NEW Benefit #10)
- Added as new Rights & Benefits section (#10) after LinkedIn Management
- Standalone GovCon Giants tool that tracks expiring federal contracts up for rebid
- Encore uses it for both content creation and direct lead generation
- License value: **$12,000/year ($1,000/month)**
- Added to all 6 locations: NEW for 2026 list, R&B title page, benefit section, deliverables table, Strategic Partnership Summary (#09), Value Breakdown table

### Updated Financials (with Recompete Tracker)
- Total package value: **$189,400** (was $177,400)
- Investment: **$63,200/year** (was $59,200) — calculated as value / 3
- Monthly: **$5,267/month** (was $4,933)
- Savings: **$126,200** (was $118,200)
- Discount: **69%** (was 67%)
- Value ratio: **3:1** (maintained)

### Appendix Index
- Added "What's Included" index to the Appendix cover page
- Lists all 5 sections:
  1. Executive Summary
  2. 2025 Encore Branding In Action
  3. 2025 Performance Scorecard
  4. Platform Performance Deep Dive
  5. Lead Generation Performance

### Print-First PDF Rebuild (February 2026)
- Created new `Encore_Funding_2026_Proposal_PDF.html` — designed exclusively for PDF output
- Every page is a fixed `<div class="page">` at 8.5in x 11in with 0.5in padding
- CSS: `@page { size: letter; margin: 0; }` — margins baked into each page div
- Images use absolute `file:///` paths for Playwright compatibility
- PDF generated with Playwright (zero margins, `print_background=True`)
- 37 pages total (Lead Generation page removed)
- Page numbers via CSS counters (`counter-reset`, `counter-increment`, `::after`)

### Print-First PDF Changes
- **Cover page**: "GovCon Giants & Encore Funding" on 3 separate lines
- **Page 6**: Redesigned 2026 Partnership Structure with 4 numbered priority cards (added #04 Google Analytics)
- **Page 8**: Added "Google Analytics Reporting & Insights" to NEW for 2026 list
- **Page 15**: Replaced `preferred-partner.png` with `website-encore.png`
- **Page 24**: Added item #05 "Access to Google Analytics" to Encore To Provide
- **Page 24**: Fixed typo "personnel" → "personal" referral
- **Page 25-26**: Strategic Partnership Summary expanded with larger fonts and proper bullet lists
- **Page 26**: Added #12 "Google Analytics Reporting & Insights", changed "FREE for Clients" → "FREE for Encore Clients"
- **Page 27**: Investment & Value Summary — larger fonts, more breathing room
- **Page 29**: Timeline starts March 2026 (was January), quarters shifted accordingly
- **Page 32**: 2025 Branding cards — increased padding and font sizes
- **Page 35-36**: Platform Deep Dive split across two pages for breathing room
- **Page 37**: Areas for Improvement redesigned from table to 3 visual cards
- **Page 38 (Lead Generation)**: Removed from proposal

### Updated Financials (Print-First PDF)
- Total package value: **$207,400**
- Investment: **$69,200/year** ($5,767/month)
- Savings: **$138,200** (67% discount)
- Value ratio: **3:1**

---

## PDF Generation (Playwright — preferred method)
```python
from playwright.sync_api import sync_playwright
import urllib.parse
html_path = '/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/Encore_Funding_2026_Proposal_PDF.html'
pdf_path = '/Users/ericcoffie/Downloads/Encore_Funding_2026_Proposal_PRINT_READY.pdf'
file_url = 'file://' + urllib.parse.quote(html_path)
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(file_url, wait_until='networkidle')
    page.pdf(path=pdf_path, format='Letter', margin={'top':'0','right':'0','bottom':'0','left':'0'}, print_background=True)
    browser.close()
```

---

## 2026 Letter Contract (March 2026)

**File:** `GCG Encore Funding Letter Contract 2026.docx` (Google Drive ENCORE FUNDING folder)

### Overview
- Created .docx letter contract matching the format of the 2024/2025 letter contracts
- Same letter-style layout: GovCon Giants logo top-right, date, Encore address, subject line, numbered sections, bullet lists, single Encore signature block
- Generated with python-docx

### Content
- **Investment:** $69,200/year ($5,767/month)
- **12 deliverables** listed under Section 2 with dollar values:
  - YouTube (24 videos) — $36,000
  - Custom Encore YouTube (4 videos) — $12,000
  - Podcast (12 episodes) — $12,000
  - Federal Help Center — $18,000
  - Email Marketing — $22,400
  - Social Media — $24,000
  - Brand Ambassador (3 events) — $24,000 (NEW)
  - LinkedIn Management — $35,000 (NEW)
  - Scaling Webinars (2/yr) — $6,000 (NEW)
  - Recompete Tracker — $12,000 (NEW)
  - Help Desk Support — $6,000 (NEW)
  - Google Analytics — Included (NEW)
- **Total package value:** $207,400 (67% discount)
- **Sections 3-8:** Investment Summary, Term (1 year, 6-month cancel for non-performance), Payment, Broker Agreement, Confidentiality, Governing Law (Florida)
- Also created HTML draft version (`Encore_Funding_2026_Letter_Contract.html`) and an earlier styled version (`Encore_Funding_2026_Contract_Agreement.html`)

---

## TempNet Staffing Handout (February 2026)

**Main File:** `/Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-handout.html`

**PDF Output:** `/Users/ericcoffie/Downloads/TempNet_Staffing_Handout.pdf`

**Images Folder:** `/Users/ericcoffie/Projects/Bootcamp/presentations/images/`

**Source Images:** `/Users/ericcoffie/Downloads/encore/tempnet/`

### Overview
- Converted from slide presentation (v1) into a print-ready letter-size handout
- Target audience: older American baby boomers at TempNet conference
- 16 numbered sections + cover page, TOC, and back cover
- Partner logos: GovCon Giants (black), Encore Funding, TempNet

### Sections (16 total)
01. The Staffing Market & Getting Started
02. Am I a "Small Business" for Staffing?
03. Your NAICS Strategy
04. The GSA Schedule Path
05. Quick Glossary & How Buys Work
06. Getting on GSA MAS & eBuy
07. Compliance & What Agencies Care About
08. Three Free Websites You Must Know
09. SAM.gov Notice Types
10. Who Buys Staffing
11. How to Find the Right Opportunities
12. AI Prompts for GovCon Staffing
13. Capability Statements & DSBS
14. Pricing, Teaming & Common Mistakes
15. First 30 Days & Resources
16. Beginner Foundation Checklist

### Image Files
| Filename | Used In |
|----------|---------|
| `am-i-small-business.png` | Section 02 |
| `your-naics-strategy.png` | Section 03 |
| `filter-naics.png` | Section 03 |
| `gsa-mas.png` | Section 04 |
| `gsa-mas-contractor-listing.png` | Section 06 |
| `gsa-ebuy.png` | Section 08 |
| `usaspending.png` | Section 08 |
| `early-stage-notice.png` | Section 09 |
| `bid-stage-notice.png` | Section 09 |
| `post-award-notice.png` | Section 09 |
| `sam-notice-types.png` | Section 09 |
| `usaspending-filter-naics.png` | Section 11 |
| `sam-gov.png` | Section 11 |
| `sources-sought-rfi.png` | Section 11 |

### Key Technical Notes
- Chrome headless PDF: use `--allow-file-access-from-files` flag for local images
- All image `src` attributes use absolute `file:///` paths (relative paths fail in headless PDF)
- Page breaks use explicit `<div class="pb"></div>` dividers (CSS-only page-break was unreliable)
- Combined sections use `<hr class="sub-divider">` (green accent line) between subsections

### PDF Generation Command
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --allow-file-access-from-files --print-to-pdf="/Users/ericcoffie/Downloads/TempNet_Staffing_Handout.pdf" "file:///Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-handout.html"
```

### Related Files
- **Slide presentation (v1):** `/Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-presentation-v1.html`

---

## TempNet Keynote Presentation v1 (March 2026)

**File:** `/Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-presentation-v1.html`

### Overview
- Full restructure from 25-slide tactical training deck into 20-slide keynote
- 10-minute keynote setup → fireside chat with two Tracys → free guide handoff
- Target: punchy, visual, story-driven — not a training manual
- All existing CSS, nav bar (arrow keys + buttons), and JS preserved
- JS auto-numbers slides and adds footers

### Slide Structure (20 slides)
01. **Title** — "You're Already a Government Contractor" (black bg, 3 logos: GCG, Encore, TempNet)
02. **Your Host** — Eric Coffie headshot + Founder, GovCon Giants
03. **Evankoff** — 10 years federal construction, $20M+ contracts (with construction photo)
04. **YouTube** — 1,600+ videos, 3.67M views, 52K+ subscribers (with channel screenshot)
05. **Podcast** — 688 episodes, 281K+ downloads (with Apple Podcasts screenshot)
06. **Myth #1** — "You need government experience" → commercial work counts (with stock image)
07. **Myth #2** — "It's all on SAM.gov" → only 5% publicly posted (with stock image)
08. **Myth #3** — "It takes years to win" → subcontracting starts in weeks (with stock image)
09. **The Market** — $775B, 23% small biz, $86B subcontracts (stats row)
10. **Evergreen Customer** — "What if one customer paid you for 10, 20, 30 years?"
11. **Success Story: Mama U** — Corliss Udoema, CSI, 20 years GovCon (with headshot)
12. **Define Your Core Capability** — focused vs. broad (red/green two-column)
13. **Your Experience Is Enough** — commercial → federal past performance translations
14. **Who's Actually Buying?** — agency table (VA, DoD, DHS, HHS, GSA)
15. **The Benefits Nobody Talks About** — long-term contracts, net-30, set-asides, vehicles
16. **The Brutal Challenges** — compliance, cash flow, proposal fatigue, losing bids
17. **Real Stories From the Trenches** — teaser for fireside chat
18. **Fireside Chat Intro** — Tracy Balazs + Tracy Marcinowski headshots (black bg)
19. **Free Guide** — handout cover image + bullet list of what's inside
20. **Closing** — "Now go make it official" (black bg, 3 logos)

### Image Files (presentations/images/)
| Filename | Used On |
|----------|---------|
| `eric-coffie-headshot.jpeg` | Slide 02 |
| `eric-construction.jpg` | Slide 03 |
| `youtube-videos.png` | Slide 04 |
| `podcast-apple.png` | Slide 05 |
| `myth-experience.png` | Slide 06 |
| `myth-samgov.png` | Slide 07 |
| `myth-speed-new.jpg` | Slide 08 |
| `mama-u-headshot.jpeg` | Slide 11 |
| `tracy-balazs-headshot.jpeg` | Slide 18 |
| `tracy-marcinowski-headshot.jpeg` | Slide 18 |
| `handout-cover.png` | Slide 19 (auto-generated from handout HTML via Playwright) |

### Logo Usage on Dark Slides
- GovCon Giants: `GovconGiants-logo-new.png` with `filter: brightness(0) invert(1)` for white on black
- Encore Funding: `EncoreLogo_Primary_Reversed.png` (white version, 55px height)
- TempNet: `TempNet_Logo_Web.png`

---

## TempNet Presentation v3 — "Fact vs. Fiction" (March 2026)

**File (Bootcamp):** `/Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-presentation-v3.html`
**File (Encore):** `/Users/ericcoffie/Projects/Encore-Funding/tempnet-staffing-presentation-v3.html`
**Vercel:** https://encore-funding.vercel.app/tempnet-staffing-presentation-v3.html

### Overview
- Modified copy of v1 keynote — rebranded as "Encore Funding Presents: Fact vs. Fiction in Government Contracting"
- Green color scheme
- Removed v1 slides 2-5 (Your Host, Evankoff, YouTube, Podcast)
- Added: Encore Funding intro slide, myths section title, "How to Get Started" transition, QR codes (encoregov.com), Encore contact closing slides with speakers

### Slide Order (21 slides)
01. Encore Funding Presents (white bg, GCG + Encore logos)
02. Title — "You're Already a Government Contractor" (black bg)
03. Free Guide (title at top, larger 260px cover, bullets, QR code)
04. The Market ($775B stats)
05. Myths section title ("Myths That Keep You Out")
06. Myth #1 — "You need government experience"
07. Myth #2 — "It's all on SAM.gov"
08. Myth #3 — "It takes years to win"
09. Evergreen Customer
10. Mama U Success Story
11. "How to Get Started" transition
12. Define Your Core Capability
13. Your Experience Is Enough
14. Who's Actually Buying
15. Benefits Nobody Talks About
16. Brutal Challenges
17. Real Stories From the Trenches
18. Fireside Chat (Tracy Balazs + Tracy Marcinowski)
19. Free Guide (side-by-side layout, QR code)
20. Speakers + Encore Contact (orange, 3-column)
21. Encore Contact solo (orange)

---

## TempNet Presentation v4 — Orange Scheme (March 2026)

**File (Bootcamp):** `/Users/ericcoffie/Projects/Bootcamp/presentations/tempnet-staffing-presentation-v4.html`
**File (Encore):** `/Users/ericcoffie/Projects/Encore-Funding/tempnet-staffing-presentation-v4.html`
**Vercel:** https://encore-funding.vercel.app/tempnet-staffing-presentation-v4.html

### Overview
- Identical to v3 but with orange color scheme (`--green: #F57C00`, `--green-dark: #E65100`)
- All accent colors (checkmarks, borders, stats, nav buttons, boxes) are orange instead of green

---

## Encore Marketing Report Dashboard

**Live URL:** https://encore-funding.vercel.app/

**Deployment:** Vercel via GitHub integration (auto-deploys on push to `main`)

**Repo:** https://github.com/ecoffie/Encore-Funding

### Files
| File | Purpose |
|------|---------|
| `index.html` | Root redirect → `Encore_Report.html` |
| `Encore_Report.html` | Executive dashboard (KPIs, sparkline, channel bars, top content, month cards, deliverable tracker) |
| `monthly-report.html` | Individual month drill-down (trend chart, channel mix, filterable activity table, CSV export) |
| `report-data.js` | Data layer — all content items, monthly aggregates, time series |
| `scripts/build_report_data.py` | Python script to rebuild `report-data.js` from source data |

### Data Coverage
- **Period:** March 2025 – January 2026 (11 months)
- **Channels:** YouTube, LinkedIn, FHC (Webinars), Instagram, Podcast
- **Content items:** 85 total
- **Key metrics:** Impressions, views, engagements, clicks, attendees, email sends, podcast downloads

### Architecture
- Pure static site — HTML + JS, no build step
- `report-data.js` sets `window.REPORT_DATA` consumed by both HTML files
- Dashboard has 3 tab views: Overview, Monthly Reports, Deliverables
- Monthly report uses `?month=YYYY-MM` query param for navigation
- All charts rendered as inline SVG (no external charting library)

---

## EncoreGov.com Landing Page (March 2026)

**Project:** `/Users/ericcoffie/Projects/encoregov/`

**Live URL:** https://encoregov.com/

**Repo:** https://github.com/ecoffie/encoregov

**Deployment:** Vercel (auto-deploys on push to `main`)

### Tech Stack
- **Framework:** Next.js 15 (TypeScript, React 19)
- **Styling:** Tailwind CSS 4
- **Email:** Nodemailer (Gmail SMTP)
- **CRM:** HubSpot API v3
- **Notifications:** Slack webhooks + email
- **Lead Storage:** Upstash Redis KV

### Key Files
| File | Purpose |
|------|---------|
| `src/app/page.tsx` | Main landing page (hero, form, services, how it works) |
| `src/app/thank-you/page.tsx` | Thank you page after form submission |
| `src/components/LeadForm.tsx` | Reusable lead capture form component |
| `src/app/api/lead/route.ts` | POST — form submission (CRM + Slack + emails + Redis) |
| `src/app/api/leads/route.ts` | GET — retrieve all stored leads from Redis |
| `src/lib/crm.ts` | HubSpot contact creation + Slack notifications |
| `src/lib/email.ts` | Guide email to lead + admin notification emails |
| `src/lib/leads.ts` | Redis KV store for lead persistence |
| `public/TempNet-Staffing-Handout.pdf` | Free guide PDF (8.4 MB) |

### Form Submission Flow
1. User submits LeadForm (name, email, phone, company)
2. POST to `/api/lead` — runs in parallel:
   - HubSpot contact creation (handles 409 duplicates)
   - Slack notification with lead details
   - HTML email to lead with guide download link
   - **Admin notification email** to `evankoffdev@gmail.com` and `ssweedler@encore-funding.com`
   - Store in Upstash Redis KV
3. Redirect to `/thank-you` page

### Environment Variables (`.env.local`)
```
HUBSPOT_ACCESS_TOKEN
SLACK_LEAD_WEBHOOK_URL
SMTP_USER              # Gmail address
SMTP_PASSWORD           # Gmail app password
KV_REST_API_URL         # Upstash Redis
KV_REST_API_TOKEN
```

### Session Changes (2026-03-13)
- Added lead notification emails — both `evankoffdev@gmail.com` and `ssweedler@encore-funding.com` receive an email with lead details (name, email, phone, company, timestamp) on every form submission

---

## Pending Tasks (Encore Funding Proposal)
- [x] ~~Capture and add screenshots to `images/` folder for Rights & Benefits section~~
- [ ] Add extra images to sections (fhc linkedin stats, total impressions linkedin, Post 9)

## Pending Tasks (TempNet)
- [x] ~~Build storytelling presentation for TempNet conference talk~~
- [ ] Add Evankoff image to slide 03 placeholder
- [ ] Source/finalize stock images for myth slides if needed

---

## TempNet Presentation v4 (March 2026)

**Main File:** `/Users/ericcoffie/Encore Funding/tempnet-staffing-presentation-v4.html`

**Live URL:** https://encore-funding.vercel.app/tempnet-staffing-presentation-v4.html

**PowerPoint Export:** `/Users/ericcoffie/Downloads/TempNet_Presentation_v4.pptx`

**Export Script:** `/Users/ericcoffie/Encore Funding/export_to_pptx.py`

### Overview
- 20 slides, 16:9 aspect ratio (960x540)
- Topic: "Fact vs. Fiction in Government Contracting" for staffing companies
- Fireside chat with Tracy Balazs, RN and Tracy Marcinowski

### Changes Made (March 2026)
- Page 17: Changed to "built a government contracting firm from the ground up"
- Page 18: Tracy Balazs, RN — "RN turned Government Contractor"
- Page 20: Redesigned closing slide — Encore logo at top, two photos centered, encoregov.com at bottom
- Removed standalone Encore contact slide (was page 21)
- Hidden nav bar and slide footers for cleaner presentation

### PowerPoint Export
```bash
cd "/Users/ericcoffie/Encore Funding" && python3 export_to_pptx.py
```
Uses Playwright to screenshot each slide, then python-pptx to assemble into PPTX.

---

## HUBZone Webinar Landing Page (June 2026)

**Project:** `/Users/ericcoffie/govcon-funnels/` (NOT in Encore Funding repo)

**Live URL:** https://govcongiants.com/hubzone

**Repo:** https://github.com/ecoffie/govcon-funnels

### Webinar Details
- **Title:** From Interested To Procurement Ready — HUBZone Webinar
- **Date:** Wednesday, June 17, 2026
- **Time:** 6:00 – 8:00 PM EST (includes ½-hour Q&A)
- **Hosts:** Eric Coffie + Tim Hagerty (TeamingPro), Chad Eberly (Encore Funding), Todd Rogers (LTR)

### Key Files (govcon-funnels)
| File | Purpose |
|------|---------|
| `src/app/hubzone/page.tsx` | Landing page (schema.org Event, hero, CTAs) |
| `src/app/hubzone/thank-you/page.tsx` | Post-registration confirmation page |
| `src/lib/email.ts` | `sendHubzoneWebinarEmail()` — confirmation email with Google Calendar link |

### Session Changes (2026-05-26)
- Corrected webinar date from June 15 → June 17 across all surfaces:
  - Landing page (title, meta, hero, schema.org Event start/end, CTAs)
  - Thank-you page (also fixed wrong time window "8 AM – 6 PM" → "6 – 8 PM EST")
  - Confirmation email (subject, headline, date block, weekday Mon→Wed, Google Calendar `dates=20260617T220000Z/20260618T000000Z`)
- Commit: `3b59f29`

### Gotcha
- **Always update weekday when changing date.** June 15 = Monday, June 17 = Wednesday. Easy to miss in the email's "Save the Date" block.
- **Google Calendar `dates=` param uses UTC.** 6 PM EDT = 22:00 UTC, so June 17 6–8 PM EDT = `20260617T220000Z/20260618T000000Z` (crosses midnight UTC).

### Registration Command Center (June 9–10, 2026) — in govcon-funnels
- **`/hubzone/registrations`** (password `***REMOVED-SENSITIVE-CREDENTIAL***`, or admin pw) — live ops dashboard reading GHL by tags `hubzone-webinar` + `hubzone-webinar-bottom`. Pace vs. **200 goal**, projection, velocity, source attribution, follow-up worklist (name/company/email/phone) + CSV. PII-redacted endpoint retired in favor of full detail behind the password.
- **Company Name field** added to both `/hubzone` forms → GHL `companyName` + Slack + worklist/CSV.
- **Scarcity banner** "first 100 get Zoom access" (public count-only `/api/hubzone/spots`, no PII).
- **Spin-the-wheel PROTOTYPE** on `/hubzone/thank-you` (`HubzoneSpinWheel.tsx`) — canvas, weighted prizes, one-spin-per-attendee. Client-side draw; move server-side before real prizes.
- Webinar pivoted to a **roundtable with Chad Eberly** (Encore storytelling). Action items: `govcon-funnels/tasks/hubzone-webinar-todo.md`.

---

## Encore Competitive Market Briefing (June 9, 2026)

**File (HTML source):** `/Users/ericcoffie/Encore Funding/encore-competitive-briefing.html`
**PDF:** `/Users/ericcoffie/Downloads/Encore_GovCon_Competitive_Briefing.pdf`

- 5-page branded (GovCon Giants × Encore) PDF for **Shelly Sweedler** — neutral market-intel briefing on the GovCon financing competitive landscape.
- **Tier One (direct):** RCA (Republic Capital Access), United Capital Funding, Parabilis, Porter Capital, REV Capital, 1st Commercial Credit, White Oak, Action Capital, Eagle, Raistone.
- **Tier Two (adjacent):** altLINE, eCapital, Republic Business Credit, Scale Funding, Riviera, Prestige, FundThrough, Bay View, Charter.
- **Tier Three (alternatives):** SBA 7(a) CAPLines, SBA WCP, Lendistry, Mobilization Funding, Live Oak, FAR Part 32.
- Closest threats: **RCA, UC Funding, Parabilis** — RCA matches Encore's unbilled-financing + bid-letter pitch; UC Funding/Parabilis lead with bank backing. Encore's edges: unbilled invoices, RFP support letters, no transactional fees, back-office + consulting wraparound.
- **Every claim fact-checked via web search** before delivery (UC Funding/Gulf Coast Bank, Parabilis, altLINE/Southern Bank, Republic/Renasant, RCA/DoD Trusted Capital, Lendistry SBLC, Triumph=trucking excluded).
- PDF via Playwright (same method as the proposal PDFs). Logos embedded `file://`. Re-export: open HTML, `page.pdf(format='Letter', margin=0, print_background=True)`.

---

## HUBZone Conference Panel — "Building for Scale" Run of Show (July 2026)

**File (HTML):** `/Users/ericcoffie/Encore Funding/hubzone-conference-run-of-show.html`
**PDF:** `/Users/ericcoffie/Downloads/HUBZone_Building_for_Scale_Run_of_Show.pdf`

- Panelist prep sheet (doubles as the day-of run of show, used to align panelists on the prep call) for the **2026 National HUBZone Conference** session **"Building for Scale: Innovative Growth & Funding Strategies."**
- **Tue, July 21, 2026 · 10:30 AM–12:00 PM · Westfields Marriott, Chantilly, VA.** Moderator: Eric Coffie. (Organizer: Michelle Burnett, HUBZone Contractors National Council. NOTE: Michelle's email said 7/22 but the correct date is 7/21.)
- **Panelists (3):** Teresa McBride (Chairman, MCPM Inc. — scaled a tech consulting firm to $197M/800+ by 1999, SBA Entrepreneur of the Year; now leads $1B–$5B project finance) → pillar *Scaling & Capital*; Calvin J. Mitchell Jr. (Sr. Director, GDIT; former SES procurement exec; NCMA Board Advisor) → *Buyer & Prime Side*; Joel Adelman (CEO, Encore Funding / AdCap Growth Partners / Transcap) → *Funding / Access to Capital*. **Joel is the Encore panelist.** Intro order Teresa → Calvin → Joel (builds scale → get selected → fund it, ending on Encore).
- Panelist titles/bios sourced from their LinkedIn profiles (Calvin: linkedin.com/in/calvin-j-mitchell-jr-a705348; Joel: linkedin.com/in/joel-adelman-cleveland).
- **Layout:** GCG × Encore branded, 2 pages. P1 = frame + prep-call note + Run of Show timeline + Cross-Panel & Q&A Backup box. P2 = three panelist cards (pillar + bio + 5 tailored questions, orange = opener). Built from the June 17 webinar template (`hubzone-run-of-show.html`).
- **PDF via Playwright** (Letter, margin 0, print_background=True). Fit was tuned by headless render measuring content-bottom vs. footer-top per page — both pages CLEAR.
