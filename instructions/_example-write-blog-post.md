# Instruction: Write Blog Post

## Goal
Research a topic, create an outline, and write a complete ~1,500-word SEO-optimized blog post ready for editing and publishing.

## Inputs
- `topic` (string): The subject of the blog post (e.g., "how to build a SaaS content calendar")
- `target_keyword` (string): The primary SEO keyword to target (e.g., "SaaS content calendar")
- `audience` (string, optional): Who this post is for. Defaults to the audience in `context/business.md`.
- `tone` (string, optional): Writing tone. Defaults to the brand voice in `context/business.md`.
- `word_count` (number, optional): Target word count. Defaults to 1,500.

## Steps

1. **Review context** — Read `context/business.md` for brand voice and audience. Read `context/personal.md` for style preferences (especially the pet peeves section).

2. **Research the topic** — Search the web for:
   - Top 5 ranking articles for the target keyword
   - Key subtopics and questions people ask about this topic
   - Recent statistics, data points, or expert quotes to reference
   - Content gaps in existing articles (what are they all missing?)

3. **Create an outline** — Structure the post as:
   - **Title**: Include the target keyword. Make it specific and compelling (not clickbait).
   - **Introduction** (100-150 words): Open with a specific insight, stat, or bold claim. No generic "In today's world" openers. State what the reader will learn and why it matters.
   - **3-5 main sections** with H2 headings: Each section covers one key idea. Use H3 subheadings if a section has multiple parts.
   - **Conclusion** (100-150 words): Summarize the key takeaway and include a clear call to action.

4. **Present the outline for approval** — Show the outline to the user before writing the full draft. Wait for feedback. If the user says "looks good" or similar, proceed. If they request changes, revise the outline first.

5. **Write the full draft** — Follow the approved outline. For each section:
   - Start with the key point (don't bury the lead)
   - Include specific examples, data, or actionable tips
   - Use short paragraphs (2-4 sentences max)
   - Use bullet points or numbered lists for scannable content
   - Include transition sentences between sections

6. **Add SEO elements**:
   - Use the target keyword in the title, first paragraph, at least 2 H2 headings, and the conclusion
   - Include 2-3 related keywords naturally throughout the post
   - Write a meta description (155 characters max)
   - Suggest 3-5 internal link opportunities (if applicable)

7. **Self-review checklist** — Before saving, verify:
   - [ ] Word count is within 10% of the target
   - [ ] No filler phrases (check personal.md pet peeves)
   - [ ] Every paragraph adds value — cut anything that's just padding
   - [ ] The intro hooks the reader in the first sentence
   - [ ] At least 2 specific examples, stats, or data points
   - [ ] All claims are accurate and sourced where possible
   - [ ] The CTA in the conclusion is clear and relevant

8. **Save the output** — Write the finished post to `outputs/blog-[slugified-title].md` with front matter:
   ```
   ---
   title: "Post Title Here"
   target_keyword: "keyword here"
   meta_description: "155-char description here"
   word_count: 1523
   date_drafted: 2025-01-15
   status: draft
   ---
   ```

## Script
No script required — this is a writing task handled directly by the AI.

## Output
- A complete blog post saved to `outputs/blog-[slugified-title].md`
- Front matter with SEO metadata
- Ready for human review and editing

## Requirements
- Web search access (for research in Step 2)
- The `context/business.md` and `context/personal.md` files must be filled in

## Edge Cases
- **Topic is too broad**: Ask the user to narrow it down. Suggest 2-3 more specific angles. Example: "SaaS marketing" is too broad — suggest "SaaS content marketing for early-stage startups" instead.
- **No good data or stats available**: Use concrete examples and case studies instead. Flag to the user that stats were hard to find.
- **User skips the outline approval**: Write the draft anyway, but note that it wasn't pre-approved and may need more revision.
- **Word count runs long**: Prioritize cutting fluff over cutting substance. If the post naturally needs more words (e.g., a comprehensive guide), let the user know and suggest splitting into a series.

## Notes
- The biggest quality differentiator is the intro. Spend extra effort making the first 2-3 sentences compelling.
- SaaS audiences respond well to specific numbers ("increased conversions by 34%") over vague claims ("significantly improved results").
- If the topic has been covered extensively, focus on a unique angle or contrarian take rather than repeating what everyone else says.
