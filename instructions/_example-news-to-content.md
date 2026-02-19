# Instruction: News to Content

## Goal
Take the latest news fetched by `scripts/fetch-news.py` and turn it into ready-to-post content: LinkedIn posts, tweets, and a newsletter snippet. One script run → a full week of content.

## Inputs
- `topic` (string, optional): Topic to fetch news on. Defaults to "artificial intelligence".
- `platforms` (list, optional): Which platforms to create for. Defaults to all: LinkedIn, Twitter/X, Newsletter.
- `angle` (string, optional): A specific perspective or brand angle to apply (e.g., "from a bootstrapped founder's perspective").

## Steps

### 1. Fetch fresh news
Run the script to pull the latest articles:
```
python3 scripts/fetch-news.py "artificial intelligence"
```
Replace the topic with whatever is relevant. The script saves results to `outputs/latest-news.md`.

### 2. Read and select stories
Open `outputs/latest-news.md` and pick the **3 best stories** based on:
- Relevance to the user's audience (check `context/business.md`)
- Potential for strong opinions or actionable insights
- Recency and newsworthiness

Skip stories that are paywalled, low-quality, or too niche.

### 3. Review context
Read `context/business.md` and `context/personal.md` for:
- Brand voice and tone
- Target audience
- Style preferences and pet peeves

All content should sound like the user wrote it, not like an AI summary.

### 4. Create LinkedIn posts (1 per story)
For each selected story, write a LinkedIn post:
- **150-250 words** (optimal LinkedIn length)
- Open with a **hook line** — a bold take, surprising angle, or contrarian opinion on the news
- Don't summarize the article. React to it. Share an insight, lesson, or prediction.
- End with a question to drive engagement
- Add 3-5 relevant hashtags
- Use line breaks liberally

Format:
```
[Hook — your take on the news, not a summary]

[2-3 short paragraphs with your insight]

[Question for engagement]

#hashtag1 #hashtag2 #hashtag3
```

### 5. Create tweets (2 per story)
For each selected story, write 2 tweets:
- Under 280 characters each
- One **hot take** (opinion or reaction)
- One **insight or tip** (what your audience can learn from this)
- No hashtags unless they add real value
- Should work standalone — no "thread" format needed

### 6. Create newsletter snippet
Write one 150-200 word section covering all 3 stories:
- Open with a 1-sentence theme ("This week in AI, three stories caught my eye...")
- Brief take on each story (2-3 sentences each)
- End with a forward-looking question or prediction
- Tone should feel personal and curated, not like a news roundup

Format:
```
### [Section Title]

[Opening theme line]

**[Story 1 headline]** — [Your take in 2-3 sentences]

**[Story 2 headline]** — [Your take in 2-3 sentences]

**[Story 3 headline]** — [Your take in 2-3 sentences]

[Closing thought or prediction]
```

### 7. Self-review checklist
Before saving, verify:
- [ ] Every piece has a strong opening — no "In this post, I'll discuss..."
- [ ] Content reacts to the news, not just summarizes it
- [ ] Brand voice matches `context/personal.md`
- [ ] All tweets are under 280 characters
- [ ] LinkedIn posts have hook lines that stop the scroll
- [ ] Newsletter snippet works as a standalone read

### 8. Save output
Write everything to `outputs/news-content-[YYYY-MM-DD].md`:
```
# Content from News — [Date]
Source: outputs/latest-news.md
Topic: [topic]

---

## LinkedIn Posts

### Post 1: [Story headline]
[content]

### Post 2: [Story headline]
[content]

### Post 3: [Story headline]
[content]

---

## Tweets

### Story 1
Tweet 1 (take): [content]
Tweet 2 (insight): [content]

### Story 2
Tweet 1 (take): [content]
Tweet 2 (insight): [content]

### Story 3
Tweet 1 (take): [content]
Tweet 2 (insight): [content]

---

## Newsletter Snippet
[content]
```

## Script
`scripts/fetch-news.py` — Fetches news from NewsAPI. Requires `NEWS_API_KEY` in `.env`.

## Output
- `outputs/latest-news.md` — Raw news articles (from script)
- `outputs/news-content-[YYYY-MM-DD].md` — Finished content package

## Requirements
- `NEWS_API_KEY` in `.env` (free at https://newsapi.org/register)
- Python 3 (no pip install needed — script uses standard library only)

## Edge Cases
- **No articles found**: Try a broader topic. "AI" works better than "transformer architecture optimizations".
- **Articles are paywalled**: Skip them. Use the description from NewsAPI and find a similar story with full access.
- **Topic is too broad**: The script returns 10 articles. If they're all over the place, narrow the search term.
- **User wants a different platform**: Adapt the format. TikTok scripts, YouTube shorts outlines, or Reddit posts all follow similar patterns — ask the user for specifics.

## Notes
- The best content reacts to news, it doesn't repeat it. "Here's what happened" is boring. "Here's what this means for you" is valuable.
- Run this weekly or daily depending on how much content the user needs.
- After each run, update this file with any lessons learned.
