# Partner Page Rebuild

### 🔗 Live demo: **https://partner-page-rebuild.vercel.app/**

Click through to see the rebuild in action. Resize narrower than 900px for the mobile layout (sticky bottom CTA appears).

**Target URL (production):** https://gov.encore-funding.com/govcon-giants-partner-government-contractor-funding/

**Goal:** Lift conversion rate from 3.4% → 6.0% (homepage parity)
**Estimated impact:** +11 key events / 90 days = ~18% lift on total gov subdomain conversions
**Why this page matters:** 22.8% of all gov subdomain sessions land here (406 / 1,784 over 90d). Single largest conversion lever on the property.

## Files in this folder

| File | Purpose |
|---|---|
| `README.md` | This — strategy, diagnosis, build instructions |
| `partner-page-v2.html` | Standalone preview/mockup of the new page (open in browser to review) |
| `wireframe.md` | Section-by-section layout spec |
| `copy.md` | Final copy block — drop into Beaver Builder |
| `implementation.md` | Step-by-step build instructions for the Encore web team |

---

## Diagnosis (from GA4 + live HTML audit, 2026-05-31)

### What the current page does wrong

Pulled from `gov.encore-funding.com/govcon-giants-partner-government-contractor-funding/` on 2026-05-31:

| Element | Current state | Problem |
|---|---|---|
| H1 | "GovCon Giants Fan? Meet Encore Funding." | Positions as relationship intro, not value prop. Filters out non-fans. |
| Subhead | "Achieve your vision for success with GovCon Giants and Encore Funding." | Vague. Doesn't say what the user gets. |
| Above-fold CTA | None (Apply Now is in top nav only) | Visitor has to scroll + navigate to convert |
| Body CTAs | **One** ("CONTACT THE TEAM") | Single CTA, wrong destination (contact-us, not apply-now) |
| Forms on page | **Zero** | Every conversion requires a click off |
| Mid-page content | 3 blog article promo cards with "Read More" buttons | Sends visitors *away* from the page |
| Trust signals | 5 association logos at bottom | Below the fold, post-decision |
| Primary destination | `/contact-us/` | Lower-intent than `/apply-now/` |

### Behavioral data

| Metric | Partner page | Homepage | Gap |
|---|---|---|---|
| 90d sessions | 406 (22.8%) | 762 (42.7%) | Partner gets ~half the traffic |
| Conversion rate | 3.4% | 6.0% | **43% lower** |
| Avg engagement time | 28s | 39s | 11s less |
| Key events / 90d | 14 | 46 | If it matched homepage rate: 24 |

**Missing ~10 key events / 90 days.** That's nearly 80% of the page's current key event output being left on the table.

---

## Rebuild strategy

**Core principle:** This page already does the credibility job. It does not do the conversion job. Keep the credibility, add the conversion.

### What stays
- Eric Coffie / GovCon Giants brand association (it's why people are here)
- "Why Encore?" section
- "We are entrepreneurs serving entrepreneurs" positioning
- Associations & affiliations row (national 8a, ASBCC, NVSBC, etc.)
- "Funding Questions" FAQ block
- The visual brand match with gov.encore-funding.com

### What changes
1. **H1 becomes conversion-focused** — leads with what user gets, Eric Coffie endorsement supports it
2. **Above-fold primary CTA** — visible without scrolling, points to apply-now (not contact-us)
3. **Inline lead form** — short form embedded directly on page (name, email, phone, monthly invoice volume)
4. **3 mid-page CTAs** — after credibility block, after Eric quote, after case study
5. **Sticky mobile bottom CTA** — always-visible apply button on mobile
6. **Article cards → trust block** — replace the "Read More" article promos with stat cards ($25B+ funded, 48-hour approval, etc.) so visitors aren't sent away
7. **Trust strip moved above fold** — "$25B+ funded · Eric Coffie–vetted · 48-hour approval"
8. **Exit-intent capture** — on exit, show modal with "Get the Government Contractor Funding Guide" lead magnet

### What gets added
- Schema markup: `Service` + `Review` + `Organization` + breadcrumb
- LocalBusiness schema with Pepper Pike OH NAP
- Form analytics events: `form_view`, `form_start`, `form_submit` (wires the GA4 lead funnel that currently reads 0)
- UTM-pass-through on the form (capture which Eric source the lead came from)

---

## Expected outcome

| Metric | Before | After (target) | Method |
|---|---|---|---|
| Conversion rate | 3.4% | 6.0% | Above-fold CTA + inline form + 3 mid-page CTAs |
| Key events / 90d | 14 | 24 | Conversion rate × 406 sessions |
| Avg engagement time | 28s | 40s+ | Scroll depth from clearer structure |
| Form starts / 90d | (unmeasured) | 60–80 | Visible form on page |
| Form completions / 90d | (unmeasured) | 20–25 | Form events fire to GA4 |

**Total gov subdomain key events lift:** ~22% (from 72 → 88+ over 90d) just from this single page change.
