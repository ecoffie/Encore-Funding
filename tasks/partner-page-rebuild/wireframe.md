# Partner Page Wireframe — Section by Section

URL: `/govcon-giants-partner-government-contractor-funding/`

Each section listed in scroll order. Mobile-first; desktop variations noted where relevant.

---

## Section 1 — Hero (above the fold)

**Goal:** Communicate value + drive click in <3 seconds.

```
┌──────────────────────────────────────────────────────┐
│ [trust strip — small text, top of hero]              │
│ $25B+ FUNDED · ERIC COFFIE–VETTED · 48-HOUR APPROVAL │
│                                                       │
│ ┌─────────────────────────┐  ┌────────────────────┐  │
│ │ H1:                     │  │                    │  │
│ │ Government Contractor   │  │  [Eric Coffie      │  │
│ │ Financing —             │  │   photo or video   │  │
│ │ Endorsed by Eric Coffie │  │   thumbnail]       │  │
│ │                         │  │                    │  │
│ │ Subhead:                │  │  "I trust Encore   │  │
│ │ Fast working capital    │  │   with my own      │  │
│ │ for government          │  │   audience because │  │
│ │ contractors. Same-day   │  │   they fund the    │  │
│ │ approval. No equity,    │  │   contractor I'd   │  │
│ │ no personal guarantees. │  │   want to fund."   │  │
│ │                         │  │   — Eric Coffie    │  │
│ │ [APPLY NOW →]           │  │                    │  │
│ │ [SEE IF YOU QUALIFY]    │  │                    │  │
│ └─────────────────────────┘  └────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

**Mobile:** Eric quote stacks below the H1+CTA block. Primary CTA full-width.

**Primary CTA:** `APPLY NOW →` → `/apply-now/?utm_source=partner-page&utm_medium=hero-cta`
**Secondary CTA:** `SEE IF YOU QUALIFY` → opens inline form (jumps to Section 5)

---

## Section 2 — Stat block (replaces blog cards)

**Goal:** Quick credibility + answer "are you legit?" without sending the user away.

```
┌─────────────┬─────────────┬─────────────┬─────────────┐
│   $25B+     │  48 hour    │   100%      │   2014      │
│   funded    │  approval   │  GovCon-    │   founded   │
│   since     │  process    │  focused    │   by ex-    │
│   2014      │             │  team       │   Advance   │
│             │             │             │   Partners  │
└─────────────┴─────────────┴─────────────┴─────────────┘
```

**Mobile:** 2x2 grid.

No links, no buttons — passive trust delivery.

---

## Section 3 — "Why Encore?" credibility block

**Goal:** Differentiate from competitors (Advance Partners, Porter Capital, Scale Funding).

Three-column layout:

| Entrepreneurs serving entrepreneurs | Full back-office support | Built for GovCon specifically |
|---|---|---|
| Founded by the team behind Advance Partners. Family-owned, not corporate. | Funding + invoicing + collections, not just cash. | Schedule 21A timelines, DCAA compliance, NET-30 cash flow. |

**CTA after block:** `READY TO APPLY? START HERE →` (mid-page CTA #1)

---

## Section 4 — Eric Coffie partnership story

**Goal:** Deliver the credibility that Eric's audience came for.

```
┌──────────────────────────────────────────────────────┐
│  [Eric photo, larger]    "Why I partnered with       │
│                           Encore Funding"            │
│                                                       │
│                          1-2 paragraphs in Eric's    │
│                          voice. Why he vetted them.  │
│                          What makes them different.  │
│                          What his audience gets.     │
│                                                       │
│                          — Eric Coffie               │
│                            GovCon Giants             │
└──────────────────────────────────────────────────────┘
```

**CTA after block:** `SEE IF YOU QUALIFY — APPLY IN 5 MIN →` (mid-page CTA #2)

---

## Section 5 — Inline lead form (THE conversion moment)

**Goal:** Make conversion possible without leaving the page.

```
┌──────────────────────────────────────────────────────┐
│  H2: Apply now for government contractor funding     │
│                                                       │
│  Get a same-day response. No equity required.        │
│                                                       │
│  ┌─────────────────────┐ ┌─────────────────────┐    │
│  │ First name *        │ │ Last name *         │    │
│  └─────────────────────┘ └─────────────────────┘    │
│  ┌─────────────────────┐ ┌─────────────────────┐    │
│  │ Business email *    │ │ Phone *             │    │
│  └─────────────────────┘ └─────────────────────┘    │
│  ┌─────────────────────────────────────────────┐    │
│  │ Company name *                              │    │
│  └─────────────────────────────────────────────┘    │
│  ┌─────────────────────────────────────────────┐    │
│  │ Monthly invoice volume (dropdown) *         │    │
│  │  · Under $50K                               │    │
│  │  · $50K–$250K                               │    │
│  │  · $250K–$1M                                │    │
│  │  · Over $1M                                 │    │
│  └─────────────────────────────────────────────┘    │
│                                                       │
│  [    GET MY FUNDING ASSESSMENT  →    ]              │
│                                                       │
│  🔒 Your information is secure. No credit pull       │
│     required for initial review.                     │
└──────────────────────────────────────────────────────┘
```

**Hidden fields capture:**
- `utm_source`, `utm_medium`, `utm_campaign` from URL
- `referrer` (document.referrer)
- `gclid` if present
- `landing_page` = partner page URL

**Form events to GA4:**
- `form_view` fires when form enters viewport
- `form_start` fires on first field focus
- `form_submit` fires on successful submission → mark as **qualified lead** key event
- HubSpot webhook fires on submit to drop into existing nurture sequence

---

## Section 6 — Funding scenarios / use cases

**Goal:** Help the visitor self-identify ("yes this is for me").

Three cards:

| Schedule 21A Holder | Newly Awarded Contract | NET-30/60 Squeeze |
|---|---|---|
| Need working capital between agency payments? We fund against your federal receivables. | Won a contract but can't fund the ramp? We fund against the contract value. | Government pays slow, payroll runs weekly. We bridge the gap. |

---

## Section 7 — Funding Questions FAQ

**Goal:** Handle objections inline.

Keep the existing "Funding Questions? We Have Answers" block. Wrap in `FAQPage` schema for SERP rich results.

Add 2-3 GovCon-specific Q&As if missing:
- "Do you fund prime contractors only or subs too?"
- "How fast can I get my first advance?"
- "What contract types qualify?" (Firm-Fixed-Price, T&M, Cost-Plus, etc.)

**CTA after block:** `STILL HAVE QUESTIONS? TALK TO OUR GOVCON TEAM →` (mid-page CTA #3) — this is the only place `/contact-us/` link goes.

---

## Section 8 — Associations & affiliations strip

**Goal:** Final trust signal before page end.

Keep existing logos (national 8a, ASBCC, NVSBC, etc.). Add Eric Coffie / GovCon Giants logo alongside.

---

## Section 9 — Final CTA block

**Goal:** Last-chance conversion for visitors who scroll past the form.

```
┌──────────────────────────────────────────────────────┐
│   Ready to fund your next government contract?       │
│                                                       │
│   Get a same-day funding assessment.                 │
│                                                       │
│           [   APPLY NOW   →   ]                      │
└──────────────────────────────────────────────────────┘
```

---

## Persistent elements

### Mobile sticky bottom CTA
Always visible on mobile scroll:
```
[ APPLY NOW — GET FUNDED IN 48 HOURS → ]
```

### Exit-intent modal (desktop only)
Triggers on mouse-out toward browser chrome:
```
┌──────────────────────────────────┐
│   Before you go —                │
│                                   │
│   Get the Government Contractor   │
│   Funding Guide (free)            │
│                                   │
│   [ email field ]                 │
│   [ DOWNLOAD GUIDE → ]            │
└──────────────────────────────────┘
```

Drops captured email into HubSpot nurture sequence.

---

## Sections REMOVED from current page

| Current section | Why removed |
|---|---|
| "GovCon Insights & Resources" (3 blog card promos) | Sends visitors away from conversion path. Replaced with stat block (Section 2). |
| `CONTACT THE TEAM` as primary CTA | Wrong intent. Replaced with `APPLY NOW` throughout, contact link kept in FAQ section only. |

---

## CTA destination map (UTM-tagged)

| CTA position | Destination | Tag |
|---|---|---|
| Hero primary | `/apply-now/` | `?utm_source=partner&utm_medium=hero` |
| Hero secondary | `#apply-form` (jump) | (no UTM, internal) |
| Mid-page CTA #1 (after Why Encore) | `#apply-form` (jump) | (no UTM, internal) |
| Eric quote CTA | `#apply-form` (jump) | (no UTM, internal) |
| Form submit | `/thank-you-partner/` | (carries UTMs forward) |
| FAQ CTA | `/contact-us/` | `?utm_source=partner&utm_medium=faq-cta` |
| Final CTA | `/apply-now/` | `?utm_source=partner&utm_medium=final` |
| Exit modal | HubSpot form embed | (HubSpot tracks separately) |
