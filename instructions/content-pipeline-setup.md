---
module_id: content
module_name: Content Pipeline
module_number: 10
category: business
description: Research topics, generate scripts, repurpose across platforms
env_keys:
  required: []
  optional:
    - key: NEWS_API_KEY
      label: NewsAPI Key
      get_url: https://newsapi.org/register
      hint: "Free tier, 100 requests/day"
    - key: LATE_API_KEY
      label: Late.dev API Key
      get_url: https://late.com
      hint: "For multi-platform publishing"
    - key: ANTHROPIC_API_KEY
      label: Anthropic API Key
      get_url: https://console.anthropic.com/settings/keys
      hint: "For content generation"
pip_packages: [python-dotenv, requests]
test_command: "python scripts/fetch-news.py"
estimated_time: "20 minutes"
interactive_steps: true
---

# Instruction: Content Pipeline Setup

## Goal
Build a content creation pipeline: research trending topics, generate scripts and social copy, and publish across platforms. End state: the user has a repeatable system that turns one idea into content for YouTube, LinkedIn, Twitter/X, and newsletters.

## Inputs
- `platforms` (list): Which platforms the user publishes on (YouTube, LinkedIn, Twitter/X, TikTok, Newsletter, Blog)
- `niche` (string): The user's content niche (e.g., "AI automation for agencies")
- `content_frequency` (string): How often they publish (daily, 2-3x/week, weekly)
- `existing_content` (list, optional): Links to past content for voice/style extraction

## Steps

### 1. Define the content strategy

Read `context/business.md` and `context/personal.md` to understand:
- Who their audience is
- What problems they solve
- Their brand voice and tone
- Content preferences and pet peeves

Ask the user:
1. What's your primary platform? (Where does your audience live?)
2. What content has performed best for you?
3. Do you prefer talking head, screen share, or mixed format?
4. Any competitors or creators whose style you admire?

Document answers in `instructions/content-strategy.md`.

### 2. Set up topic research

Create `scripts/research-topics.py` that:
1. Searches YouTube for top-performing videos in the user's niche
2. Pulls title, view count, publish date, channel size
3. Calculates an "outlier score" (views relative to channel average)
4. Saves top 20 ideas to `outputs/topic-ideas-[YYYY-MM-DD].md`

**Sources to check:**
- YouTube search + competitor channels (outlier analysis)
- Reddit/forums (what questions do people ask?)
- News via `scripts/fetch-news.py` (timely angles)
- Google Trends (rising search terms)

**Outlier formula:**
```
outlier_score = video_views / channel_average_views
```
Videos with outlier score > 3x are proven topics worth covering.

### 3. Build the title generator

Create a title generation workflow that produces 10+ title options per topic using proven frameworks:

**Curiosity framework:**
- "I Found the [Unexpected Thing] That [Desirable Outcome]"
- "Why [Common Belief] Is Completely Wrong"
- "[Number] [Things] I Wish I Knew Before [Activity]"

**Desire framework:**
- "How to [Achieve Goal] in [Timeframe] (Step-by-Step)"
- "The [Adjective] Way to [Outcome] Without [Pain Point]"
- "How I [Achievement] and How You Can Too"

**Fear framework:**
- "Stop [Common Mistake] Before It [Consequence]"
- "[Number] Signs Your [Thing] Is [Failing/Broken]"
- "The [Thing] Nobody Tells You About [Topic]"

Save the workflow as `instructions/generate-titles.md`.

### 4. Build the script generator

Create `instructions/generate-script.md` with three output modes:

**Outline mode** (for experienced speakers):
- Hook (2 sentences)
- 3-5 key points with supporting examples
- CTA

**Hybrid mode** (recommended):
- Full hook written out
- Bullet points for main content
- Transitions written out
- Full CTA written out

**Teleprompter mode** (for beginners):
- Every word written out
- Natural speech patterns (contractions, filler acknowledgments)
- Paragraph breaks every 2-3 sentences

**Script structure:**
```
HOOK (0:00-0:30)
[Problem or provocative statement that stops the scroll]

SETUP (0:30-2:00)
[Context — why this matters, what's at stake]

BODY (2:00-8:00)
[3-5 main points with examples/proof]

CTA (8:00-end)
[What to do next — subscribe, comment, link in bio]
```

Read `context/personal.md` for voice preferences. The script should sound like the user talks, not like AI wrote it.

### 5. Set up social content repurposing

One long-form piece should generate multiple short-form pieces. Create `instructions/repurpose-content.md`:

**From one YouTube video, generate:**
- 3 LinkedIn posts (different angles from the video)
- 5 tweets (key insights, hot takes, one-liners)
- 1 newsletter section (summary + personal commentary)
- 2-3 short-form clips (identify timestamp ranges for TikTok/Reels/Shorts)
- 1 blog post (SEO-optimized written version)

**Repurposing workflow:**
1. Read/watch the source content
2. Extract the 5 strongest standalone insights
3. Rewrite each for the target platform's format and constraints
4. Match the user's voice from `context/personal.md`
5. Save to `outputs/social-content-[YYYY-MM-DD].md`

### 6. Set up publishing (optional)

**Option A: Late.dev (multi-platform scheduling)**
1. Get API key at late.com
2. Add `LATE_API_KEY` to `.env`
3. Create `scripts/publish-content.py` that:
   - Takes content from `outputs/`
   - Schedules to connected platforms
   - Tracks post performance

**Option B: Manual publishing**
- Save all content to `outputs/` in ready-to-paste format
- User copies to each platform manually

**Option C: Platform-specific APIs**
- YouTube: Google OAuth + upload API
- LinkedIn: LinkedIn API (limited)
- Twitter/X: Twitter API v2

Start with Option B (manual). Graduate to A or C once the content pipeline is proven.

### 7. Create the content calendar

Build a weekly content workflow:

```
Monday: Research + pick 2-3 topics for the week
Tuesday: Write scripts / outlines
Wednesday: Record (if video) or finalize written content
Thursday: Edit + create social repurposing package
Friday: Schedule everything for next week
```

Save as `instructions/content-calendar.md`.

### 8. Test the pipeline

Run through one full cycle:
1. [ ] Research script finds relevant topics with good outlier scores
2. [ ] Title generator produces 10+ compelling options
3. [ ] Script generator creates content in the user's voice
4. [ ] Repurposing produces platform-specific content
5. [ ] Content saved to `outputs/` in correct format
6. [ ] User approves the voice and quality

## Script
- `scripts/research-topics.py` — Topic research and outlier analysis
- `scripts/fetch-news.py` — News-based content ideas (existing)
- `scripts/publish-content.py` — Publishing automation (optional)

## Output
- `outputs/topic-ideas-[YYYY-MM-DD].md` — Researched topic ideas
- `outputs/script-[title]-[YYYY-MM-DD].md` — Generated scripts
- `outputs/social-content-[YYYY-MM-DD].md` — Repurposed social content
- `instructions/content-strategy.md` — Documented content strategy
- `instructions/generate-titles.md` — Title generation workflow
- `instructions/generate-script.md` — Script generation workflow
- `instructions/repurpose-content.md` — Repurposing workflow
- `instructions/content-calendar.md` — Weekly schedule

## Requirements
- `NEWS_API_KEY` in `.env` (for news-based content)
- `LATE_API_KEY` in `.env` (optional, for publishing automation)
- `ANTHROPIC_API_KEY` in `.env` (for content generation)
- Python 3, `requests` library
- YouTube Data API key (optional, for outlier research)

## Edge Cases
- **User has no existing content**: Skip voice extraction. Build voice profile from their answers in `context/personal.md` and refine after first batch.
- **Niche is too narrow for outlier research**: Broaden search terms. "AI for agencies" is narrow — also search "AI automation", "agency growth", "business AI".
- **User wants daily content**: Focus on repurposing, not creating from scratch daily. One deep piece per week → 5+ daily social posts.
- **Multiple team members creating content**: Create separate voice profiles in `context/` for each creator.
- **Content doesn't sound like the user**: This is the #1 complaint. Fix by reading their past content, noting speech patterns, favorite phrases, and updating the prompt.

## Notes
- Quality > quantity. One great video per week beats daily mediocre posts.
- The best content frameworks are proven by data (outlier analysis), not guesswork.
- Scripts should be 80% the user's words, 20% structure. Never over-polish.
- After each content cycle, update this file with performance data and lessons.
