---
module_id: ads
module_name: Paid Ads Monitoring
module_number: 11
category: business
description: Monitor ad performance, alerts, optimization recommendations
env_keys:
  required: []
  optional:
    - key: META_ACCESS_TOKEN
      label: Meta Ads Access Token
      get_url: https://developers.facebook.com
      hint: "Long-lived token, expires in 60 days"
    - key: META_AD_ACCOUNT_ID
      label: Meta Ad Account ID
      get_url: null
      hint: "Starts with act_"
    - key: GOOGLE_ADS_DEVELOPER_TOKEN
      label: Google Ads Developer Token
      get_url: https://ads.google.com/home/tools/manager-accounts/
      hint: "Requires API Center approval (3-5 days)"
    - key: ANTHROPIC_API_KEY
      label: Anthropic API Key
      get_url: https://console.anthropic.com/settings/keys
      hint: "For generating recommendations"
pip_packages: [python-dotenv, requests]
test_command: null
estimated_time: "20 minutes"
interactive_steps: true
---

# Instruction: Paid Ads Monitoring Setup

## Goal
Build a system to monitor paid ad performance across platforms, track spend, alert on anomalies, and generate optimization recommendations. End state: the user gets daily performance summaries and instant alerts when something needs attention.

## Inputs
- `platforms` (list): Which ad platforms the user runs on — "meta" (Facebook/Instagram), "google", "tiktok", "linkedin"
- `monthly_budget` (number): Total monthly ad budget across platforms
- `kpis` (dict): Key metrics and targets (e.g., `{"cpa": 50, "roas": 3.0, "ctr": 2.0}`)
- `alert_thresholds` (dict, optional): When to trigger alerts (e.g., `{"spend_over_daily": 500, "cpa_over": 75}`)

## Steps

### 1. Connect ad platforms

**Meta (Facebook/Instagram) Ads:**
1. Create a Meta app at developers.facebook.com (or use existing)
2. Get a long-lived access token (exchange short-lived via `grant_type=fb_exchange_token`)
3. Add to `.env`:
   ```
   META_ACCESS_TOKEN=your_long_lived_token
   META_AD_ACCOUNT_ID=act_123456789
   ```
4. Token expires in 60 days — set a reminder to refresh

**Google Ads:**
1. Create OAuth credentials in Google Cloud Console
2. Get developer token from Google Ads API Center
3. Add to `.env`:
   ```
   GOOGLE_ADS_DEVELOPER_TOKEN=your_token
   GOOGLE_ADS_CLIENT_ID=your_client_id
   GOOGLE_ADS_CLIENT_SECRET=your_secret
   GOOGLE_ADS_REFRESH_TOKEN=your_refresh_token
   GOOGLE_ADS_CUSTOMER_ID=1234567890
   ```

**TikTok Ads:**
1. Create app at ads.tiktok.com/marketing_api
2. Add to `.env`:
   ```
   TIKTOK_ACCESS_TOKEN=your_token
   TIKTOK_ADVERTISER_ID=your_id
   ```

Start with whichever platform the user spends the most on.

### 2. Build the metrics fetcher

Create `scripts/fetch-ad-metrics.py` that:
1. Pulls last 24h and last 7d metrics from each connected platform
2. Extracts per-campaign: spend, impressions, clicks, CTR, conversions, CPA, ROAS
3. Calculates trends (7d vs previous 7d)
4. Saves to `outputs/ad-metrics-[YYYY-MM-DD].json`

**Key metrics to track:**

| Metric | What It Tells You | Red Flag |
|--------|-------------------|----------|
| CTR | Ad creative relevance | Below 1% (Meta), below 2% (Google Search) |
| CPA | Cost per acquisition | Above target by 50%+ |
| ROAS | Return on ad spend | Below 2x (most businesses need 3x+) |
| CPM | Cost per 1000 impressions | Sudden spike = audience fatigue |
| Frequency | How often same person sees ad | Above 3 = creative fatigue |
| Spend | Budget consumption | Above daily budget = pacing issue |

### 3. Set up alerts

Create `scripts/ad-alerts.py` that runs on a schedule and alerts when:

| Alert | Trigger | Notification |
|-------|---------|--------------|
| Overspend | Daily spend > 120% of budget | Immediate |
| CPA spike | CPA > 150% of target | Immediate |
| Creative fatigue | Frequency > 3 or CTR drops 30% | Daily summary |
| Campaign paused | Active campaign stops spending | Within 1 hour |
| ROAS drop | ROAS falls below target | Daily summary |
| Budget exhausted | Campaign hits lifetime budget | Immediate |

**Notification options:**
- Telegram (via Command Center if installed)
- Email (via `scripts/email-capture.py` adapter)
- Slack (via Slack integration)

### 4. Build the performance dashboard

Create `instructions/ad-performance-review.md` — a workflow the AI runs daily or on-demand:

**Daily Ad Report (auto-generated):**
```
# Ad Performance — [Date]

## Spend Summary
Total: $X,XXX | Budget remaining: $X,XXX (XX% of monthly)
Meta: $XXX | Google: $XXX | TikTok: $XXX

## Top Performers
1. [Campaign name] — $XX CPA, X.Xx ROAS (↑15% vs last week)
2. [Campaign name] — $XX CPA, X.Xx ROAS

## Needs Attention
1. [Campaign name] — CPA spiked 45%, consider pausing
2. [Campaign name] — Frequency at 4.2, creative refresh needed

## Recommendations
- Increase budget on [Campaign] (strong ROAS, room to scale)
- Test new creatives for [Campaign] (fatigue signals)
- Pause [Campaign] (CPA above threshold for 3 consecutive days)
```

Save to `outputs/ad-report-[YYYY-MM-DD].md`.

### 5. Create optimization workflows

Document repeatable optimization actions in `instructions/`:

**Creative refresh workflow:**
1. Identify fatigued campaigns (frequency > 3, CTR declining)
2. Pull top-performing ad copy and hooks
3. Generate 3 new variations with different angles
4. Use image generation module (if active) for new visuals
5. Launch as A/B test against current best performer

**Scaling workflow:**
1. Identify campaigns with CPA < target and ROAS > target
2. Increase daily budget by 20% (not more — avoid learning phase reset)
3. Monitor for 48 hours
4. If CPA holds, increase again
5. If CPA spikes, revert and wait 3 days

**Kill workflow:**
1. Campaign CPA > 200% of target for 3+ days
2. Pause campaign
3. Analyze: audience wrong? Creative weak? Offer mismatch?
4. Fix root cause before restarting

### 6. Integrate with Daily Brief (optional)

If the Daily Brief module is active, add ad metrics to the morning briefing:
- Update `scripts/daily-brief.py` to call `scripts/fetch-ad-metrics.py`
- Add a "Paid Ads" section to the brief template
- Include: yesterday's spend, top campaign, any alerts

### 7. Test the system

1. [ ] Metrics fetcher pulls real data from at least one platform
2. [ ] Daily report generates with correct numbers
3. [ ] Alerts trigger on test thresholds (temporarily lower them)
4. [ ] Recommendations are actionable and make sense
5. [ ] Token/API keys are stored securely in `.env`

## Script
- `scripts/fetch-ad-metrics.py` — Pulls metrics from ad platforms
- `scripts/ad-alerts.py` — Monitors for anomalies and sends alerts

## Output
- `outputs/ad-metrics-[YYYY-MM-DD].json` — Raw metrics data
- `outputs/ad-report-[YYYY-MM-DD].md` — Daily performance report
- `instructions/ad-performance-review.md` — Review workflow
- `instructions/ad-optimization.md` — Scaling and optimization playbooks

## Requirements
- Ad platform API credentials in `.env` (at least one platform)
- `ANTHROPIC_API_KEY` in `.env` (for generating recommendations)
- Python 3, `requests` library
- Active ad campaigns with sufficient data (at least 7 days of spend)

## Edge Cases
- **Meta token expires**: Long-lived tokens last 60 days. Set a calendar reminder. Re-exchange before expiry.
- **Google Ads API approval**: Developer tokens require basic access approval. Apply early — takes 3-5 business days.
- **Low spend campaigns**: Metrics are unreliable with <$50/day spend. Flag as "insufficient data" rather than making optimization calls.
- **Multiple ad accounts**: Aggregate across accounts but report per-account. Some clients have separate accounts for different offers.
- **Attribution delays**: Conversions can take 1-7 days to report (especially Meta). Don't make optimization decisions on same-day data.
- **Currency differences**: Normalize everything to the user's primary currency.

## Notes
- Don't optimize daily. Most ad platforms need 3-7 days of data after changes to exit learning phase.
- The biggest wins come from creative, not targeting. Focus optimization time on new creative angles.
- Budget pacing: Meta spends aggressively early. Set campaign-level daily budgets, not ad-set level.
- After each review cycle, update this file with platform-specific lessons.
