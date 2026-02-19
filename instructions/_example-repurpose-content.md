# Instruction: Repurpose Content

## Goal
Take a single blog post and transform it into a multi-platform content package: LinkedIn posts, tweets/X posts, a newsletter snippet, and a thread. Maximize the reach of every piece of content we publish.

## Inputs
- `source_file` (string): Path to the blog post to repurpose (e.g., `outputs/blog-saas-content-calendar.md`)
- `platforms` (list, optional): Which platforms to create for. Defaults to all: LinkedIn, Twitter/X, Newsletter.
- `thread_platform` (string, optional): Where the thread should be optimized for. Defaults to "LinkedIn".

## Steps

1. **Read the source post** — Open the blog post file and identify:
   - The core argument or thesis
   - 3-5 key insights or takeaways
   - Any specific data points, stats, or quotes
   - The target audience and tone

2. **Review context** — Read `context/business.md` for brand voice and `context/personal.md` for style preferences. Social content should match the blog tone but be more conversational and punchy.

3. **Create 3 LinkedIn posts** — Each post should:
   - Be 150-300 words (optimal LinkedIn length)
   - Open with a strong hook line that stops the scroll (first line is everything on LinkedIn)
   - Focus on ONE key insight from the blog post (don't try to summarize the whole thing)
   - End with a question or call to action to drive engagement
   - Include 3-5 relevant hashtags at the bottom
   - Use line breaks liberally — dense paragraphs don't work on LinkedIn
   - Format:
     ```
     [Hook line — bold claim, surprising stat, or contrarian take]

     [2-3 short paragraphs expanding on the idea]

     [Question or CTA]

     #hashtag1 #hashtag2 #hashtag3
     ```

4. **Create 5 tweets/X posts** — Each tweet should:
   - Be under 280 characters
   - Be standalone — it should make sense without reading the blog post
   - Cover a different insight, tip, or angle from the source
   - Include a mix of formats: hot take, quick tip, stat callout, question, and one linking back to the full post
   - No hashtags unless they add real value (X has moved away from hashtag culture)
   - Format:
     ```
     Tweet 1 (hot take): [Bold opinion from the post]
     Tweet 2 (quick tip): [One actionable takeaway]
     Tweet 3 (stat): [Specific number or data point]
     Tweet 4 (question): [Thought-provoking question for engagement]
     Tweet 5 (link): [Teaser + link to full post]
     ```

5. **Create 1 newsletter snippet** — A 150-200 word section that:
   - Summarizes the blog post for newsletter readers
   - Opens with why this topic matters right now
   - Includes 2-3 bullet points of key takeaways
   - Ends with a "Read the full post" link placeholder
   - Tone should feel like a personal recommendation from the user, not a corporate summary
   - Format:
     ```
     ### [Section Title]

     [Why this matters — 2-3 sentences]

     Key takeaways:
     - [Takeaway 1]
     - [Takeaway 2]
     - [Takeaway 3]

     [Read the full post →](LINK)
     ```

6. **Create 1 thread (5-7 posts)** — A longer-form breakdown:
   - Post 1: Hook — grab attention with the core insight or a bold claim
   - Posts 2-5: Walk through the key points, one per post. Include examples or data.
   - Post 6: Summary or "TL;DR" with bullet points
   - Post 7 (optional): CTA — link to the full post, ask for follows, or pose a question
   - Each post should be under 280 characters if for Twitter/X, or under 300 words if for LinkedIn
   - Use "1/" numbering format

7. **Self-review checklist** — Before saving, verify:
   - [ ] No content is copy-pasted directly from the blog — everything is rewritten for the platform
   - [ ] Each LinkedIn post has a strong opening hook
   - [ ] All tweets are under 280 characters
   - [ ] The newsletter snippet works as a standalone read
   - [ ] Thread posts flow logically and each stands on its own
   - [ ] Brand voice is consistent across all pieces
   - [ ] No filler phrases (check personal.md pet peeves)

8. **Save all output** — Write everything to a single file:
   `outputs/repurposed-[source-post-slug].md`

   Structure the file with clear section headers:
   ```
   # Repurposed Content: [Blog Post Title]
   Source: [path to original blog post]
   Date: [today's date]

   ---

   ## LinkedIn Posts

   ### LinkedIn Post 1
   [content]

   ### LinkedIn Post 2
   [content]

   ### LinkedIn Post 3
   [content]

   ---

   ## Tweets / X Posts

   ### Tweet 1 (hot take)
   [content]

   ### Tweet 2 (quick tip)
   [content]

   [... etc]

   ---

   ## Newsletter Snippet
   [content]

   ---

   ## Thread
   [content]
   ```

## Script
No script required — this is a writing task handled directly by the AI.

## Output
- A single file saved to `outputs/repurposed-[source-post-slug].md` containing:
  - 3 LinkedIn posts
  - 5 tweets/X posts
  - 1 newsletter snippet
  - 1 thread (5-7 posts)

## Requirements
- The source blog post must exist at the specified path
- The `context/business.md` and `context/personal.md` files must be filled in

## Edge Cases
- **Source post is very short (under 500 words)**: Still create all pieces, but note that some may overlap in content. Suggest to the user that a longer source post yields more diverse repurposed content.
- **Source post is very technical**: Simplify language for social media. Technical depth is fine for the thread but LinkedIn posts and tweets should be accessible.
- **Source post has no data or stats**: Focus on insights, opinions, and actionable tips instead. Flag to the user that adding data points would strengthen the social content.
- **User only wants certain platforms**: Only generate the requested platforms. Still save to the same file format, just skip the sections that weren't requested.

## Notes
- The hook line on LinkedIn posts is the single most important element. Test different styles: contrarian takes, surprising stats, "most people think X but actually Y" framing.
- Tweets perform better when they're opinionated. Don't be afraid to take a stance.
- The newsletter snippet should feel personal and curated — like the user is saying "hey, I wrote this and here's why you should care."
- Threads that teach something step-by-step tend to outperform threads that just summarize.
- Repurposing is not reformatting. Each platform has different norms. A LinkedIn post is NOT just a longer tweet.
