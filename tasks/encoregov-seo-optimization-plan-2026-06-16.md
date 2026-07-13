# encoregov.com — SEO Optimization Plan (2026-06-16)

**Source:** live GSC (URL-prefix property `https://encoregov.com/`), last 7 days (Jun 6→13), pulled via `scripts/gsc-report.mjs`.
**Baseline (2026-06-06):** 0 clicks · 22 impr · pos 19.7.
**Now (7d):** 5 clicks · **1,257 impr** · 0.40% CTR · pos 48.3. Impressions up 57× — site moved from invisible to broadly indexed in 10 days.

The job now is **harvesting demand that already exists** — pages Google is showing but ranking too deep to earn clicks. This is on-page + internal-linking work, not new content. Ordered by impressions-at-risk (biggest wasted demand first).

---

## Priority 1 — `/financing/staffing-payroll-funding` 🔴 (566 impr · pos 59.5 · 0 clicks)

**The problem:** Highest-impression page on the whole site, stuck on page 6, earning zero clicks. Google clearly maps this URL to high-volume staffing-payroll queries ("best payroll funding for staffing companies," "back office payroll funding," "best payroll financing options for staffing agencies") — but the page is too thin/shallow to rank.

**Why it's thin:** It's a `ServicePageData` object with **3 body sections + 5 FAQs** (`src/app/financing/staffing-payroll-funding/page.tsx`). The high-intent queries it's surfacing for are *comparison/superlative* ("best…") and *specific* ("back office payroll funding for recruiters") — the current copy doesn't target those phrasings.

**Fixes (in priority order):**
1. **Title tag** — current `"Payroll Funding for Staffing Companies | Encore Funding"`. Add the modifier Google is already matching: → **`"Best Payroll Funding for Staffing Companies (GovCon & Federal) | Encore"`**. The "best" + "government" qualifiers map to the actual impression queries.
2. **Add 2–3 body sections** targeting the surfaced queries verbatim as `heading`s:
   - "Back-office payroll funding for staffing & recruiting firms" (query: *back office payroll funding* @ pos 79, *...for recruiters* @ pos 97)
   - "What to look for in a payroll funding company" (captures the "best payroll funding options" comparison intent)
   - A short comparison block: payroll funding vs. a bank line / MCA (you already have `/govcon-financing-vs-mca` to link to).
3. **Internal links IN** — this is the biggest structural lever (see Cross-Cutting #1). Link to this page from: the homepage, `/government-contractor-financing`, the `how-government-contractors-get-paid` guide, and `net-30-60-90` guide. Currently service pages have almost no inbound internal links, which is why a 566-impr page sits at pos 59.
4. **FAQ expansion** — add "Is payroll funding the same as factoring?" and "How fast can I get funded for my first payroll?" (FAQs emit FAQPage schema → rich-result eligibility).

**Target:** pos 59 → high-20s within 4–6 weeks; first clicks within 2 weeks of the title change.

---

## Priority 2 — `/guides/assignment-of-claims-act` 🟢 (103 impr · **pos 14** · 3 clicks — best page on site)

**The opportunity:** Already your strongest performer and **one position off page 1**. Small push = outsized click gain (CTR jumps hard from pos 14 → pos 8–9). It ranks for "assignment of claims act" (pos 9), "31 usc 3727" (pos 10), "federal assignment of claims act" (pos 12), "assignment funding," "assignment of receivables."

**Fixes:**
1. **Build topical authority around it** — it's surfacing for `31 usc 3727`, `assignment of receivables`, `assignment funding`. Add an H2 section explicitly covering "31 U.S.C. § 3727 and § 3728" by name (you rank pos 10 for the bare statute — own it) and a short "Assignment of receivables vs. assignment of claims" clarifier.
2. **Internal links IN from money pages** — link to this guide from `/govcon-invoice-factoring` and `/federal-contract-factoring` with anchor text "Assignment of Claims Act." It's the *legal mechanism* that makes GovCon factoring possible, so the link is natural and passes authority to a near-page-1 winner.
3. **Internal links OUT (conversion)** — make sure this guide links forward to `/govcon-invoice-factoring` (it gets the traffic; that's where the money is). Use the guides `related-links` model already in `src/content/guides.ts`.
4. Confirm Article/FAQ schema is firing (GuidePage should already emit it — verify in Rich Results Test).

**Target:** pos 14 → pos 8–10 = page 1 → 3 clicks/wk could become 10–15/wk.

---

## Priority 3 — `/govcon-invoice-factoring` 💰 (126 impr · pos 57.7 · 1 click)

**Why it matters:** This is the **primary money page** — and it's buried at pos 58 despite real impressions. It ranks for "best factoring company for government contracts" (pos 11.7) and "best construction factoring companies." This is the conversion destination; getting it to page 1 is worth more than any guide.

**Fixes:**
1. Pull internal-link equity toward it from every guide (assignment-of-claims, what-is-invoice-factoring @ 116 impr, how-contractors-get-paid). Guides should funnel to this page.
2. Title/H1 should include "best…government contract" modifier it's already ranking for at pos 11.7.
3. Strengthen with the comparison pages you already own (`/govcon-financing-vs-mca`, `/govcon-financing-vs-sba-loan`, `/govcon-financing-vs-traditional-factoring`) — interlink them as a cluster pointing at the money page.

---

## Priority 4 — Striking-distance quick wins (small tweaks, near page 1)

| Page | Impr | Pos | Move |
|------|------|-----|------|
| `/guides/net-30-60-90-government-payment` | 9 | 19.8 | Add internal links in; expand FAQ. ~1 pos from page 2 top |
| `/guides/how-government-contractors-get-paid` | 27 | 24.8 | Hub page — link OUT to all money pages; it's a natural top-of-funnel |
| `/guides/what-is-invoice-factoring` | 116 | 71.3 | High impr, deep — title needs "government contract" qualifier + link to `/govcon-invoice-factoring` |
| `/government-contractor-financing` | 55 | 39.4 | Link in from homepage hero + footer; broad-term page |

---

## Cross-Cutting Fixes (do these once, lift everything)

1. **🔧 Add a `relatedLinks` field to `ServicePageData`** (`src/components/ServicePage.tsx` + interface). Guides already have related-links (`src/content/guides.ts` line 26) — **service pages do NOT**, which is the #1 reason money pages sit at pos 55–60. This is the single highest-leverage code change. Render a "Related" grid + inline contextual links.
2. **Internal-linking map** — guides (traffic) → service pages (money). Every guide should link to ≥2 service pages with descriptive anchor text; every service page should link to ≥2 supporting guides. Currently near-zero cross-linking between the two route types.
3. **Title-tag pass** — several pages rank for "best …" / "government …" modifiers they don't have in their titles. Match the title to the query GSC shows you're already surfacing for.
4. **Re-pull GSC weekly** to track movement: `export $(grep '^GCP_SA_JSON=' "/Users/ericcoffie/govcon-funnels/.env.local") && node scripts/gsc-report.mjs --site "https://encoregov.com/" --days 7`

---

## Sequencing (recommended)

**Week 1 (highest ROI, lowest effort):**
- [ ] Add `relatedLinks` to `ServicePage` (Cross-Cutting #1) — unblocks everything
- [ ] Title-tag fixes on staffing-payroll, invoice-factoring, what-is-invoice-factoring (P1, P3, P4)
- [ ] Wire internal links into the 3 money pages from guides

**Week 2:**
- [ ] Expand `/financing/staffing-payroll-funding` body sections (P1)
- [ ] Add 31 U.S.C. § 3727 section to assignment-of-claims guide (P2)

**Week 3–4:**
- [ ] Build the guides→money interlink cluster fully (P3, Cross-Cutting #2)
- [ ] Re-pull GSC, measure pos movement, double down on whatever moved

---

## What this plan does NOT do (honest scope)
- **No new pages** — this is harvesting demand on the 25+ URLs already indexed. New content is a separate Tier-3 effort.
- **GSC ≠ market volume.** These are queries encoregov.com *already* ranks for. Whole-market keyword volumes (total staffing/GovCon search demand) still need Ahrefs/SEMrush — don't size the opportunity from GSC alone. See `tasks/encoregov-seo-findings-2026-06.md`.
- Position estimates are directional, not guaranteed; re-measure weekly via the script.
