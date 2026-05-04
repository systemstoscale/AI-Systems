# Social Media Analysis

Analyze a social media profile across platforms and create an actionable growth report.

## Inputs
- Social media handle (same across platforms, or specify per platform)
- Platforms to analyze: YouTube, Instagram, TikTok

## Steps

1. Use the ScrapeCreators API to fetch the profile. The API key is in `.env` as `SCRAPECREATORS_API_KEY`. Write a script to call the API and save the raw data to `outputs/social-raw-[handle].json`.

2. Read the output and analyze:
   - **Reach:** followers/subscribers across platforms
   - **Content:** posting frequency, content types, top performing posts
   - **Engagement:** likes, comments, shares relative to audience size
   - **Growth:** trends (if available)

3. Compare against benchmarks:
   - Engagement rate: good = 3–6%, great = 6%+
   - Best-performing content format
   - Platform with the most growth potential

4. Generate recommendations:
   - Top 3 quick wins (actions this week)
   - Content gaps (formats or topics not being used)
   - Posting schedule recommendation

## Output

Save to `outputs/social-analysis-[handle]-[date].md` with:
- Executive summary (3 bullets)
- Platform-by-platform breakdown
- Recommendations table
- 30-day action plan
