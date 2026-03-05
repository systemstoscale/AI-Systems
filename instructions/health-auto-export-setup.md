# SOP: Health Auto Export → Supabase

## Goal
Automatically sync Apple Health data (workouts, weight, body fat, water intake, heart rate, sleep) to your Supabase database using the Health Auto Export iOS app.

## Architecture

```
Apple Watch → Apple Health → Health Auto Export app → Your Webhook → Supabase
                                    (POST JSON)        (Railway)    (personal.health_metrics)
```

## Prerequisites

- iPhone with Apple Health data (Apple Watch recommended but not required)
- **Health Auto Export** app ($2.99 on App Store)
- A running webhook server (Railway, Vercel, or any server that accepts POST)
- Supabase project with `personal.health_metrics` table

---

## Step 1: Install Health Auto Export

1. Download [Health Auto Export](https://apps.apple.com/app/health-auto-export/id1115567069) from the App Store
2. Open the app and grant Apple Health permissions
3. Select all categories you want to track:
   - **Body:** Weight, Body Fat Percentage, Body Mass Index
   - **Heart:** Heart Rate, Resting Heart Rate, Heart Rate Variability
   - **Activity:** Steps, Active Energy, Exercise Minutes
   - **Nutrition:** Dietary Water
   - **Sleep:** Sleep Analysis
   - **Vitals:** Blood Oxygen, Respiratory Rate, Body Temperature

## Step 2: Deploy Your Webhook

Your webhook is a small server that receives health data and writes it to Supabase.

**Option A: Railway (Recommended)**
1. Create a new Railway project
2. Deploy `apple_health_webhook.py` (from `_shared/scripts/ai-systems/`)
3. Set environment variables:
   - `NEXT_PUBLIC_SUPABASE_URL` — Your Supabase URL
   - `SUPABASE_SERVICE_ROLE_KEY` — Your Supabase service role key
   - `AI_EMPLOYEE_USER_ID` — Your user ID
   - `HEALTH_WEBHOOK_SECRET` — A random secret string (you choose)
   - `PORT` — `8080` (Railway default)
4. Note your Railway public URL (e.g., `https://your-app.up.railway.app`)

**Option B: Any Server**
- The webhook is a simple Python HTTP server
- It accepts `POST /health` with JSON body
- Requires `Authorization: Bearer <your-secret>` header
- Returns `{"ok": true}` on success

## Step 3: Configure Health Auto Export Automation

1. Open Health Auto Export
2. Tap **Automations** (bottom nav)
3. Tap **+ New Automation**
4. Configure:

| Setting | Value |
|---------|-------|
| **Type** | REST API |
| **URL** | `https://your-railway-url.up.railway.app/health` |
| **Method** | POST |
| **Format** | JSON |
| **Batch Requests** | OFF (send all at once) |

5. Add header:
   - Key: `Authorization`
   - Value: `Bearer your-secret-here` (match your `HEALTH_WEBHOOK_SECRET`)

6. **Select Metrics** — tap each one you want to export:
   - Weight
   - Body Fat Percentage
   - Heart Rate
   - Resting Heart Rate
   - Heart Rate Variability (HRV)
   - Steps
   - Active Energy Burned
   - Sleep Analysis
   - Dietary Water
   - Blood Oxygen Saturation
   - Respiratory Rate

7. **Select Workouts** — enable All Workouts

8. **Schedule**:
   - **Manual**: Tap to sync anytime
   - **Automatic**: Every 1 hour (recommended) or Every 6 hours
   - **On Change**: Syncs when new data appears (uses more battery)

9. Tap **Save**

## Step 4: Test the Connection

1. In Health Auto Export, go to your automation
2. Tap **Run Now**
3. You should see a green checkmark
4. Check Supabase → `personal.health_metrics` table for new rows with `source = 'apple_health'`

## Step 5: Verify Data Flow

After a day of use, check your data:
```sql
SELECT date, source,
  raw_data->>'weight_kg' as weight,
  raw_data->>'body_fat_pct' as body_fat,
  raw_data->>'water_ml' as water,
  steps, resting_hr, hrv
FROM personal.health_metrics
WHERE source = 'apple_health'
ORDER BY date DESC
LIMIT 7;
```

---

## What Gets Tracked

| Data Type | Source | Column | Notes |
|-----------|--------|--------|-------|
| Weight | Scale / manual entry | `raw_data.weight_kg` | Auto-converts lbs → kg |
| Body Fat % | Scale / manual entry | `raw_data.body_fat_pct` | |
| Water Intake | Manual entry | `raw_data.water_ml` | Log water in Apple Health |
| Resting HR | Apple Watch (passive) | `resting_hr` | Updated daily |
| HRV | Apple Watch (sleep) | `hrv` | Measured during sleep |
| Steps | iPhone / Apple Watch | `steps` | All-day count |
| Active Calories | Apple Watch | `active_calories` | |
| Sleep | Apple Watch | `sleep_hours`, `deep_hours`, `rem_hours` | Requires wearing Watch to sleep |
| SpO2 | Apple Watch (sleep) | `raw_data.spo2` | Blood oxygen |
| Workouts | Apple Watch | `personal.workouts` table | Type, duration, HR, calories |

## Workout Types That Get Tracked

Any Apple Watch workout type is captured, including:
- Strength Training
- HIIT / Functional Training
- Running / Walking
- Cycling
- Swimming
- Sauna (log as "Mind and Body" or custom)
- Ice Bath / Cold Plunge (log as "Other")

**Pro tip:** For sauna and ice baths, start a workout on your Apple Watch:
- **Sauna**: Use "Mind and Body" or "Other" workout type
- **Ice Bath**: Use "Other" workout type, or create a custom workout type

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| No data appears | Check Authorization header matches your secret |
| Missing metrics | Make sure each metric is selected in the automation |
| Workouts missing | Enable "All Workouts" in the automation |
| Delayed data | Apple Health updates in background — may take up to 1 hour |
| 401 error | Your Bearer token doesn't match `HEALTH_WEBHOOK_SECRET` |
| 400 error | Check webhook server logs for column type mismatches |

## Cost

- **Health Auto Export app**: $2.99 one-time (no subscription)
- **Railway webhook**: Free tier covers this easily (minimal compute)
- **Battery impact**: Minimal with hourly schedule, ~5% more with "on change"
