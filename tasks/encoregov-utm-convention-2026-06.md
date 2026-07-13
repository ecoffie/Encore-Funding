# encoregov.com — UTM Tagging Convention
## So Every Traffic Source Is Attributable in the 60-Day Lead-Gen Experiment

**Prepared by:** GovCon Giants
**Date:** 2026-06-06
**Why this exists:** The experiment's whole deliverable is proving *which* channels drive leads/applications to encoregov.com. UTMs are how GA4 (both `G-VYDTBT2QV0` Encore-reporting and `G-DMG27PEE17` ours) and HubSpot can tell organic from YouTube from podcast from email. **If a link isn't tagged, the visit lands in "direct/none" and the attribution is lost.** Tag every link from every channel, every time.

---

## The 3 rules

1. **Tag every external link to encoregov.com** (YouTube description, podcast show notes, email, social bio/post, etc.). Untagged = unattributable.
2. **Use lowercase, no spaces** (use hyphens). UTMs are case-sensitive — `YouTube` ≠ `youtube` and will split into two rows in reports.
3. **Keep `utm_source=` consistent per channel** (always `youtube`, never sometimes `yt`). Consistency is what makes the report readable.

---

## The parameters

| Param | What it means | Our convention |
|---|---|---|
| `utm_source` | **Where** the click came from (the platform) | `youtube`, `podcast`, `email`, `linkedin`, `instagram`, `fhc` (Federal Help Center), `recompete-tracker` |
| `utm_medium` | **Type** of traffic | `video`, `audio`, `email`, `social`, `referral`, `cpc` (if ever paid) |
| `utm_campaign` | **Which** push/initiative | `encore-experiment` for everything in this 60-day test (so it all rolls up under one campaign), or a more specific name like `encore-launch-jun26` |
| `utm_content` | **Which specific** placement/asset (optional but recommended) | the video slug, episode number, email name, or post — e.g. `ep-201`, `staffing-payroll-video`, `welcome-email-1` |

> **Landing page first, then `?`.** Drive traffic to the most relevant page, not always the homepage. A staffing-payroll YouTube video should link to `/financing/staffing-payroll-funding`, not `/`.

---

## Copy-paste templates per channel

Replace `<page>` with the target path (e.g. `/financing/staffing-payroll-funding`) and `<asset>` with the specific video/episode/email.

**YouTube** (description links, pinned comment, end-screen)
```
https://encoregov.com<page>?utm_source=youtube&utm_medium=video&utm_campaign=encore-experiment&utm_content=<asset>
```

**Podcast** (show notes, episode description)
```
https://encoregov.com<page>?utm_source=podcast&utm_medium=audio&utm_campaign=encore-experiment&utm_content=ep-<number>
```

**Email** (GovCon Giants list sends)
```
https://encoregov.com<page>?utm_source=email&utm_medium=email&utm_campaign=encore-experiment&utm_content=<email-name>
```

**LinkedIn** (posts, profile/company link)
```
https://encoregov.com<page>?utm_source=linkedin&utm_medium=social&utm_campaign=encore-experiment&utm_content=<post>
```

**Instagram** (bio link, story link sticker)
```
https://encoregov.com<page>?utm_source=instagram&utm_medium=social&utm_campaign=encore-experiment&utm_content=<post>
```

**Federal Help Center / webinar / Recompete Tracker** (referral placements)
```
https://encoregov.com<page>?utm_source=fhc&utm_medium=referral&utm_campaign=encore-experiment&utm_content=<placement>
```

---

## Already-built internal tracking (don't tag these — they're handled in code)

These fire automatically; UTMs above are only for **inbound** links from channels.

- **On-site Apply Now → Encore application:** `ApplyButton.tsx` already appends `utm_source=encoregov&utm_medium=referral&utm_campaign=apply&utm_content=<source page>` to the `gov.encore-funding.com/apply-now/` link, and fires a GA4 `apply_click` event. So Encore's analytics see which encoregov page sent each applicant.
- **On-site lead form:** POSTs to `/api/lead` → HubSpot + Slack + Redis + email, and fires GA4 `generate_lead`. The inbound `utm_*` on the landing URL is captured by GA4 for the session, so a form lead is attributable to the channel that drove it.

---

## How to read the results

In GA4 (either property) → **Reports → Acquisition → Traffic acquisition**, or build an exploration grouped by **Session source / medium**, with **`generate_lead`** and **`apply_click`** as the metrics. That table answers the experiment's core question: *which channel drove how many leads/applications.*

In HubSpot, the captured UTMs (if mapped to contact properties) let you attribute *closed* applications, not just clicks — the strongest version of the proof.

---

## Quick checklist before posting any link to encoregov.com
- [ ] Points to the most relevant landing page (not just `/`)
- [ ] Has all four `utm_*` params, lowercase, hyphenated
- [ ] `utm_source` matches the channel's standard value above
- [ ] `utm_campaign=encore-experiment` (so it rolls up with the rest of the test)
- [ ] `utm_content` identifies the specific asset (so you can compare videos/episodes/emails)
