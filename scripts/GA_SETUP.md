# Permanent Google Analytics (GA4) Connection

This connects the dashboard to **live GA4 data** via the Google Analytics Data API.
A scheduled GitHub Action runs `scripts/fetch_ga.py`, regenerates `ga-data.js`
(now with **month-by-month** channels, pages, and conversions), commits it, and
Vercel auto-deploys. No servers, no cost.

```
GitHub Action (weekly) → fetch_ga.py → GA4 Data API → ga-data.js → commit → Vercel deploy
```

---

## One-time setup (~10 minutes)

### 1. Enable the API
- Go to [Google Cloud Console](https://console.cloud.google.com/) → create or select a project.
- **APIs & Services → Library** → search **"Google Analytics Data API"** → **Enable**.

### 2. Create a service account + key
- **APIs & Services → Credentials → Create Credentials → Service account**.
- Name it (e.g. `encore-ga-reader`), create. No roles needed at the project level.
- Open the service account → **Keys → Add key → Create new key → JSON** → download.
- Keep this JSON file private (it is a password).

### 3. Grant the service account access to the GA4 property
- In [Google Analytics](https://analytics.google.com/) → **Admin** (gear, bottom-left).
- Under the **Property** column → **Property Access Management** → **+** → **Add users**.
- Paste the service account email (looks like
  `encore-ga-reader@your-project.iam.gserviceaccount.com`).
- Role: **Viewer**. Uncheck "Notify by email". Add.

### 4. Find the GA4 Property ID (numeric)
- **Admin → Property Settings** → copy the **PROPERTY ID** at the top
  (a number like `493820114`). *Not* the "G-XXXX" measurement ID.

### 5. Add the GitHub secrets
- In the repo (`github.com/ecoffie/Encore-Funding`) → **Settings → Secrets and
  variables → Actions → New repository secret**. Add two:
  | Name | Value |
  |------|-------|
  | `GA4_PROPERTY_ID` | the numeric property id from step 4 |
  | `GA4_SA_KEY` | paste the **entire contents** of the JSON key file from step 2 |

That's it. The workflow is already in `.github/workflows/refresh-ga.yml`.

---

## Run it

- **Automatic:** every Monday (see the `cron` in the workflow). Change the schedule
  by editing the `cron` line.
- **Manual:** repo → **Actions** tab → **Refresh GA4 data** → **Run workflow**.

---

## Run locally (optional, to test before pushing)

```bash
pip install -r scripts/requirements.txt

# point at the downloaded key file
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
export GA4_PROPERTY_ID="493820114"

python3 scripts/fetch_ga.py
```

This rewrites `ga-data.js`. Commit + push to deploy.

---

## What gets pulled

| Section | Dimensions | Metrics |
|---------|-----------|---------|
| Period totals | — | active users, new users, sessions, key events, engagement time |
| Monthly trend | `yearMonth` | active/new users, sessions, key events, avg engagement |
| Channels | `sessionDefaultChannelGroup` (+ monthly) | sessions, new users |
| Top pages | `pageTitle` (+ monthly) | screen page views |
| Conversions | `eventName` (+ monthly) | key events |

The `monthly_channels`, `monthly_pages`, and `monthly_key_events` fields are the
upgrade over the CSV snapshot — they let the monthly reports show per-month
sources, top pages, and conversions (not just users).

---

## Migration note

`scripts/ingest_ga_csv.py` (manual CSV → `ga-data.js`) still works as a fallback.
Once the API is live, `fetch_ga.py` replaces it and outputs a superset of the
same shape, so the dashboard keeps working unchanged.
