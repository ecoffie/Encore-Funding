# Partner Page — Implementation Guide

For the Encore web team / WordPress admin.

URL: `https://gov.encore-funding.com/govcon-giants-partner-government-contractor-funding/`
CMS: WordPress + Beaver Builder
Theme: `bb-theme-child`

---

## Pre-build checklist

- [ ] Take a backup of the current page (export Beaver Builder layout to JSON)
- [ ] Note the current page ID — needed for redirect / republish if URL changes (it shouldn't)
- [ ] Confirm Yoast SEO is active (it is — schema is firing)
- [ ] Confirm Gravity Forms or whatever form plugin Encore uses (look at `/apply-now/` to copy the existing form structure)
- [ ] Verify HubSpot is integrated for form submissions
- [ ] Confirm GA4 is firing (already confirmed — measurement ID is active)

---

## Beaver Builder build steps

Open the page in Beaver Builder. Delete every existing row except the header/footer (those are theme-controlled).

### Row 1 — Hero

Two columns, equal width. Set row background to gradient (existing brand gradient — pull from Solutions page row 1).

**Left column:**
1. Add **Heading** module → H1 → paste from `copy.md` Section 1
2. Add **Text Editor** module → small caps trust strip → above the heading
3. Add **Subheading** module → paste subhead from copy
4. Add **Button** module → "APPLY NOW →" → link `/apply-now/?utm_source=partner&utm_medium=hero` → primary button style
5. Add **Button** module → "See if you qualify" → link `#apply-form` → ghost/secondary style

**Right column:**
1. Add **Photo** module → Eric Coffie photo (use the existing high-res one from `/wp-content/uploads/`)
2. Add **Quote** module (or Text Editor with quote styling) → paste Eric quote from copy

**Mobile:** Set right column to stack below left.

### Row 2 — Stat block

Four columns, equal width. Background: light gray or white.

In each column:
1. Add **Heading** module → big number (e.g., "$25B+") → H3, bold, brand green
2. Add **Text Editor** → small caption ("Funded since 2014")

**Mobile:** 2×2 grid.

### Row 3 — Why Encore?

Three columns. Section H2 in a full-width row above.

Each column:
1. **Icon** module (use existing icon library — chair/heart/shield style)
2. **Heading** module → H3 → card title
3. **Text Editor** → card body

Below row: single-column row with centered button:
- **Button** module → "READY TO APPLY? START HERE →" → link `#apply-form` → primary style

### Row 4 — Eric Coffie story

Two-column row. Left column ~40% width, right ~60%.

**Left:** Larger Eric Coffie photo
**Right:** Heading H2 + Text Editor with the story copy + quote attribution

Below row: single-column with button:
- **Button** module → "SEE IF YOU QUALIFY — APPLY IN 5 MIN →" → link `#apply-form` → primary style

### Row 5 — Inline lead form (THE conversion moment)

Set row ID to `apply-form` (this is what the anchor links jump to).

Single column, max-width 720px, centered.

1. **Heading** module → H2 → "Apply for government contractor funding"
2. **Text Editor** → subhead
3. **HTML/Form** module → embed the form (see "Form spec" below)
4. **Text Editor** → trust line ("🔒 Your information is secure...")

### Row 6 — Use cases

Three columns. Section H2 above. Each column: heading + text.

### Row 7 — FAQ

Section H2. Use **Accordion** module (Beaver Builder native).

Each Q&A as a collapsible item. Include the existing FAQs plus the 3 new ones from copy.md.

Below: button → "STILL HAVE QUESTIONS? TALK TO OUR GOVCON TEAM →" → link `/contact-us/?utm_source=partner&utm_medium=faq-cta`

### Row 8 — Associations strip

Keep the existing Beaver Builder row from the current page — it already has the logo grid. Just verify GovCon Giants logo is in the row.

### Row 9 — Final CTA

Full-width row with dark background.
1. Heading H2 (white text)
2. Subhead
3. Button "APPLY NOW →" → link `/apply-now/?utm_source=partner&utm_medium=final` → large size

---

## Form spec

### Fields

```
First name      [text, required, name="first_name"]
Last name       [text, required, name="last_name"]
Business email  [email, required, name="email"]
Phone           [tel, required, name="phone"]
Company name    [text, required, name="company"]
Monthly invoice volume [select, required, name="invoice_volume"]
  options: under_50k | 50k_250k | 250k_1m | over_1m
Contract type   [select, optional, name="contract_type"]
  options: prime | sub | both | not_yet
```

### Hidden fields (auto-populate)

```
utm_source       [hidden, value from URL]
utm_medium       [hidden, value from URL]
utm_campaign     [hidden, value from URL]
gclid            [hidden, value from URL]
referrer         [hidden, value=document.referrer]
landing_page     [hidden, value=window.location.pathname]
form_location    [hidden, value="partner-page-inline"]
```

### Submission flow

1. Client-side validation (HTML5 + jQuery)
2. POST to existing HubSpot form endpoint (use same endpoint as `/apply-now/` form — coordinate with Encore web admin to confirm)
3. HubSpot creates/updates contact, fires workflow (drop into existing nurture sequence)
4. GA4 event fires: `form_submit` with `form_location: partner-page-inline`
5. Mark as **qualified lead** key event in GA4
6. Redirect to thank-you page or show inline success message

### Existing form to clone

Check `/apply-now/` page in Beaver Builder. Copy the form module configuration so HubSpot mapping is identical (just fewer fields here — the short partner-page form is intentionally lighter to maximize completion).

---

## GA4 event wiring

Add to page via Google Tag Manager or directly in theme.

```javascript
// Fire when the form scrolls into view
const form = document.getElementById('apply-form');
if (form && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        gtag('event', 'form_view', {
          form_location: 'partner-page-inline',
          page_path: location.pathname
        });
        observer.disconnect();
      }
    });
  }, { threshold: 0.5 });
  observer.observe(form);
}

// Fire on first field focus
document.querySelectorAll('#apply-form input, #apply-form select').forEach(field => {
  field.addEventListener('focus', () => {
    if (!window._formStarted) {
      window._formStarted = true;
      gtag('event', 'form_start', {
        form_location: 'partner-page-inline'
      });
    }
  }, { once: true });
});

// Fire on successful submission (in the HubSpot success callback)
window.addEventListener('message', (e) => {
  if (e.data.type === 'hsFormCallback' && e.data.eventName === 'onFormSubmitted') {
    gtag('event', 'form_submit', {
      form_location: 'partner-page-inline',
      page_path: location.pathname
    });
    // Mark as key event in GA4 admin (one-time setup)
  }
});
```

### GA4 admin setup (one-time)

1. GA4 → Admin → Events → Mark `form_submit` as a key event when `form_location = partner-page-inline`
2. Optionally: create a second key event `apply_complete` that fires only when HubSpot returns "qualified" status — but `form_submit` is the minimum

This fills the current zero: GA4 reads 0 qualified leads / 0 converted leads. After this wire-up, every submission shows up.

---

## Schema markup additions

Yoast handles WebPage + BreadcrumbList automatically. Add these manually via Yoast → Schema tab or a JSON-LD code block:

### Service schema

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Government Contractor Financing",
  "provider": {
    "@type": "Organization",
    "name": "Encore Funding",
    "url": "https://www.encore-funding.com"
  },
  "areaServed": "United States",
  "description": "Working capital financing for government contractors against federal receivables. Same-day approval, no equity required, no personal guarantees.",
  "offers": {
    "@type": "Offer",
    "description": "Same-day funding assessment for government contractors with federal receivables."
  }
}
```

### LocalBusiness schema (also needed sitewide)

```json
{
  "@context": "https://schema.org",
  "@type": "FinancialService",
  "name": "Encore Funding",
  "image": "https://www.encore-funding.com/wp-content/uploads/2022/09/Encore-funding.jpg",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "30100 Chagrin Blvd, Suite 350",
    "addressLocality": "Pepper Pike",
    "addressRegion": "OH",
    "postalCode": "44124",
    "addressCountry": "US"
  },
  "telephone": "[Encore phone number]",
  "url": "https://www.encore-funding.com"
}
```

### FAQ schema (auto-generated from Accordion module if Yoast FAQ block is used)

If Beaver Builder Accordion doesn't auto-emit FAQ schema, use the Yoast FAQ block inside the accordion section instead, or add manual JSON-LD.

---

## Sticky mobile bottom CTA

Add to theme footer (or via Beaver Builder global module):

```html
<div class="mobile-sticky-cta" id="mobileStickyCta">
  <a href="/apply-now/?utm_source=partner&utm_medium=mobile-sticky"
     class="btn btn-primary btn-full">
    APPLY NOW — GET FUNDED IN 48 HOURS →
  </a>
</div>
```

```css
.mobile-sticky-cta {
  display: none;
}
@media (max-width: 767px) {
  .mobile-sticky-cta {
    display: block;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 999;
    padding: 12px 16px;
    background: white;
    box-shadow: 0 -4px 12px rgba(0,0,0,0.08);
  }
  .mobile-sticky-cta .btn {
    width: 100%;
    padding: 14px;
    font-weight: 700;
  }
  /* Add bottom padding to body so content isn't hidden behind sticky */
  body { padding-bottom: 72px; }
}
```

Add page-level class so this only appears on the partner page (or pages where it's wanted) — set via Beaver Builder page settings.

---

## Exit-intent modal (desktop only)

Use the OptinMonster plugin (if installed) or a simple custom solution:

```javascript
let exitShown = false;
document.addEventListener('mouseleave', (e) => {
  if (e.clientY < 0 && !exitShown && window.innerWidth >= 768) {
    exitShown = true;
    document.getElementById('exitModal').classList.add('show');
  }
});
```

Modal contains HubSpot embedded form for the funding guide PDF. Same nurture-sequence drop as the inline form, but flagged `source=exit-intent`.

---

## QA checklist before go-live

- [ ] Page loads under 3 seconds on mobile 4G (test with PageSpeed)
- [ ] All CTAs scroll/link to correct destination with correct UTM
- [ ] Form submits successfully and creates HubSpot contact
- [ ] GA4 `form_view`, `form_start`, `form_submit` events fire (check GA4 DebugView)
- [ ] Schema validates: paste page HTML into https://search.google.com/test/rich-results
- [ ] Mobile sticky CTA appears below 768px, disappears above
- [ ] Exit-intent modal triggers on desktop only, fires only once per session
- [ ] No console errors
- [ ] All images have alt text
- [ ] Page is indexable (no `noindex` meta)
- [ ] Canonical URL is the page itself (Yoast)

---

## Post-launch tracking

**Week 1:** Verify `form_submit` events appearing in GA4 (currently zero). Should see 5-10/week.

**Week 4:** Compare conversion rate:
- Pre-launch baseline: 3.4%
- Target: 6.0%
- Method: GA4 → Reports → Engagement → Landing pages → filter to partner page → divide key events by sessions

**Week 8:** A/B test the H1 (current target vs. "Get Funded in 48 Hours — Government Contractor Financing" variant). Use Google Optimize or Beaver Builder split-test plugin.

**Week 12:** Full re-audit. Compare against 90d baseline of 14 key events. Target: 24+.

---

## Rollback plan

If conversion rate **drops** after 4 weeks (it shouldn't, but defensive):
1. Restore Beaver Builder JSON backup from pre-build
2. Document what specific element caused the drop (analyze GA4 funnel)
3. Re-deploy a partial change (e.g., just the new H1 + form, skip use cases section)

If form submissions break:
1. Verify HubSpot endpoint is reachable
2. Check browser console for JS errors
3. Fall back to linking the hero CTA to `/apply-now/` until form is fixed
