# SOP: Health Data Integration

## Goal
Connect your wearables and health devices to your AI Systems so it can track sleep, recovery, HRV, workouts, weight, and body composition — all flowing into your Daily Brief.

## Supported Sources

| Source | Data | Auth Method | Cost |
|--------|------|-------------|------|
| **OURA Ring** | Sleep, readiness, HRV, RHR, activity, steps | OAuth2 | Ring purchase ($299+) |
| **WHOOP** | Recovery, strain, sleep, HRV, RHR, workouts, SpO2 | OAuth2 | Membership ($30/mo) |
| **Apple Watch** | Workouts, weight, body fat, water, HR, sleep, SpO2 | Health Auto Export app | Watch + $2.99 app |

You don't need all three — pick the ones you use. Data merges into one `personal.health_metrics` table with a `source` field so you can compare.

---

## Option 1: OURA Ring

### Setup
1. Go to [developer.ouraring.com](https://developer.ouraring.com)
2. Sign in with your OURA account
3. Create an app (or find your existing one)
4. Add redirect URI: `http://localhost:8099/callback`
5. Copy **Client ID** and **Client Secret** to your `.env.shared`:
   ```
   OURA_CLIENT_ID=your-client-id
   OURA_CLIENT_SECRET=your-client-secret
   ```
6. Run the authorization:
   ```bash
   python _shared/scripts/integrations/oura_client.py --authorize
   ```
7. Approve in browser → token saved automatically

### Test
```bash
python _shared/scripts/integrations/oura_client.py --summary
```

### Sync to Supabase
```bash
python _shared/scripts/ai-systems/health_sync.py --source oura --days 7
```

### What You Get
- Sleep score, readiness score (daily)
- HRV, resting heart rate (nightly)
- Steps, active calories (daily)
- Body temperature deviation
- Deep/REM/light sleep hours

---

## Option 2: WHOOP

### Setup
1. Go to [developer-dashboard.whoop.com](https://developer-dashboard.whoop.com)
2. Create a team, then create an app
3. Add scopes: `read:recovery`, `read:cycles`, `read:sleep`, `read:workout`, `read:profile`, `read:body_measurement`, `offline`
4. Set redirect URI: `http://localhost:8098/callback`
5. Copy **Client ID** and **Client Secret** to your `.env.shared`:
   ```
   WHOOP_CLIENT_ID=your-client-id
   WHOOP_CLIENT_SECRET=your-client-secret
   ```
6. Run the authorization:
   ```bash
   python _shared/scripts/integrations/whoop_client.py --authorize
   ```
7. Approve in browser → token saved automatically

### Test
```bash
python _shared/scripts/integrations/whoop_client.py --summary
```

### Sync to Supabase
```bash
python _shared/scripts/ai-systems/health_sync.py --source whoop --days 7
```

### What You Get
- Recovery score (daily, like OURA readiness)
- Strain score (daily activity load)
- HRV, resting heart rate (nightly)
- Sleep hours (deep/REM/light breakdown)
- SpO2, skin temperature
- Workout details (sport type, strain, HR zones)

---

## Option 3: Apple Watch (via Health Auto Export)

See the dedicated SOP: **[health-auto-export-setup.md](health-auto-export-setup.md)**

### Summary
1. Install [Health Auto Export](https://apps.apple.com/app/health-auto-export/id1115567069) ($2.99)
2. Deploy the webhook server (`apple_health_webhook.py`) to Railway
3. Create a REST API automation in the app pointing to your webhook
4. Data syncs automatically every hour

### What You Get
- Workouts (strength, cardio, sauna, ice bath — any Apple Watch workout)
- Weight, body fat % (from smart scale or manual entry)
- Water intake (manual logging)
- Heart rate, resting HR, HRV
- Sleep analysis (deep/REM/core)
- Steps, active calories
- Blood oxygen (SpO2)

---

## Automated Sync (Railway Cron)

Once set up, add health sync to your Railway cron job:

```python
# In railway_daily_brief.py or a separate service
from health_sync import sync_all
results = sync_all(days=1)  # Syncs OURA + WHOOP
```

Schedule: Run at midnight daily, before the 7 AM Daily Brief.

Apple Health syncs separately via the webhook (real-time or hourly).

---

## Data in Your Daily Brief

Once health data flows into Supabase, your Daily Brief automatically includes:

```
HEALTH
  Readiness: 84 (OURA) | Recovery: 34% (WHOOP)
  HRV: 57 ms | RHR: 46 bpm
  Sleep: 6.0h (74 score) — deep 1.5h, REM 1.7h
  Steps: 8,234 | Calories: 2,100
  Weight: 73.0 kg | Body Fat: 14.2%
  Water: 2.8L
```

The Daily Brief pulls from whatever sources you have configured. Missing a source? That section just gets skipped.

---

## Comparing OURA vs WHOOP

If you wear both, you'll see interesting differences:

| Metric | OURA | WHOOP | Notes |
|--------|------|-------|-------|
| HRV | Measured once (during sleep) | Measured continuously | WHOOP trends higher |
| RHR | Lowest overnight | Average overnight | OURA reads lower |
| Sleep | Duration + quality score | Duration + stages + recovery | Both are good |
| Recovery | "Readiness" (0-100) | "Recovery" (0-100%) | Different algorithms |
| Activity | Steps + calories | Strain (0-21 scale) | WHOOP = intensity focused |

Both devices can co-exist in Supabase with `source = 'oura'` vs `source = 'whoop'`.
