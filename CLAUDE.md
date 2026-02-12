# Encore Funding 2026 Proposal - Change Log

## Project Overview
HTML proposal document for Encore Funding x GovCon Giants 2026 Strategic Partnership.

**Main File:** `/Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My Drive/GOVCON EDU/ENCORE FUNDING/Encore_Funding_2026_Sponsorship_Proposal.html`

**PDF Output:** `/Users/ericcoffie/Downloads/Encore_Funding_2026_Proposal_PRINT_READY.pdf`

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
| `preferred-partner.png` | FHC Preferred Partners page |
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

---

## PDF Generation Command
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="/Users/ericcoffie/Downloads/Encore_Funding_2026_Proposal_PRINT_READY.pdf" "file:///Users/ericcoffie/Library/CloudStorage/GoogleDrive-evankoffdev@gmail.com/My%20Drive/GOVCON%20EDU/ENCORE%20FUNDING/Encore_Funding_2026_Sponsorship_Proposal.html"
```

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
- **Future task:** Build a separate storytelling presentation for the actual talk

---

## Pending Tasks (Encore Funding Proposal)
- [x] ~~Capture and add screenshots to `images/` folder for Rights & Benefits section~~
- [ ] Add extra images to sections (fhc linkedin stats, total impressions linkedin, Post 9)

## Pending Tasks (TempNet Handout)
- [ ] Build storytelling presentation for TempNet conference talk
