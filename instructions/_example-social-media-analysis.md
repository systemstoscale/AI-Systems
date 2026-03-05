# Social Media Analysis

## Goal
Analyze my social media presence across platforms and create an actionable growth report.

## Inputs
- Social media handle (same across platforms, or specify per platform)
- Platforms to analyze (YouTube, Instagram, TikTok)

## Steps

1. Run the social profile fetcher:
   ```bash
   python3 scripts/fetch-social.py [handle]
   ```

2. Read the output file: `outputs/social-profile-[handle].md`

3. Analyze the data:
   - **Reach:** followers/subscribers across platforms
   - **Content:** posting frequency, content types, top performing posts
   - **Engagement:** likes, comments, shares relative to audience size
   - **Growth:** trends over time (if available)

4. Compare against benchmarks:
   - What's the engagement rate? (good = 3-6%, great = 6%+)
   - What content format performs best?
   - Which platform has the most growth potential?

5. Generate recommendations:
   - Top 3 quick wins (things to do this week)
   - Content gaps (topics or formats not being used)
   - Platform-specific tips
   - Posting schedule recommendation

## Output
Save to `outputs/social-analysis-[handle]-[date].md` with:
- Executive summary (3 bullets)
- Platform-by-platform breakdown
- Recommendations table
- 30-day action plan
