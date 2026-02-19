# Instruction: Competitor Analysis

## Goal
Research a competitor consulting firm and produce a structured profile covering their services, market positioning, pricing, strengths, and weaknesses. Used for strategic planning and proposal differentiation.

## Inputs
- `competitor_name` (string, required): The name of the competitor firm to research.
- `focus_area` (string, optional): A specific angle to emphasize — e.g., "pricing", "digital transformation services", "healthcare clients". If not provided, do a general-purpose analysis.

## Steps
1. **Confirm the competitor** — Verify the company name with the user. Ask: "I will research [competitor_name]. Is this the right company? Any specific website or details to make sure I find the right one?"
2. **Gather information** — Research the competitor using available sources. Look for:
   - Company overview (size, founding year, locations)
   - Services offered and how they describe them
   - Target market and ideal client profile
   - Publicly available pricing or engagement models (hourly, project-based, retainer)
   - Key differentiators — what they emphasize in their marketing
   - Client testimonials or case studies (if public)
   - Leadership team and notable hires
   - Recent news, awards, or partnerships
3. **Analyze relative to your company** — Read `context/business.md` to understand our own positioning. Compare:
   - Where do our services overlap?
   - Where do they offer something we do not?
   - Where are we stronger?
   - What can we learn from their approach?
4. **Assess strengths and weaknesses** — Based on the research, list:
   - 3-5 strengths (things they do well or advantages they have)
   - 3-5 weaknesses (gaps, complaints, or areas where we have an edge)
5. **Compile the profile** using this structure:
   ```
   # Competitor Profile: [Competitor Name]
   *Generated: [date]*

   ## Overview
   - **Company**: [name]
   - **Founded**: [year]
   - **Size**: [employee count or range]
   - **Headquarters**: [location]
   - **Website**: [URL]

   ## Services
   - [Service 1]: [brief description]
   - [Service 2]: [brief description]
   - [Service 3]: [brief description]

   ## Target Market
   [Who they serve — industries, company sizes, geographies]

   ## Pricing / Engagement Model
   [What is publicly known — hourly rates, project fees, retainer structures, or "not publicly available"]

   ## Positioning
   [How they describe themselves. What is their core message or value proposition?]

   ## Key Differentiators
   - [What makes them stand out]

   ## Strengths
   1. [Strength with brief explanation]
   2. [Strength with brief explanation]
   3. [Strength with brief explanation]

   ## Weaknesses
   1. [Weakness with brief explanation]
   2. [Weakness with brief explanation]
   3. [Weakness with brief explanation]

   ## How They Compare to your company
   | Dimension | [Competitor] | your company |
   |-----------|-------------|----------|
   | Core Focus | [their focus] | [our focus] |
   | Target Market | [their market] | [our market] |
   | Pricing | [their model] | [our model] |
   | Strengths | [summary] | [summary] |

   ## Opportunities for your company
   - [What we can learn or how we can differentiate against this competitor]

   ## Sources
   - [List URLs and sources used]
   ```
6. **Save the profile** to `outputs/competitor-[competitor-name-slug].md` using a lowercase, hyphenated version of the competitor name.
7. **Summarize for the user** — After saving, show the Overview, Strengths, Weaknesses, and Opportunities for your company sections as a quick briefing.

## Script
No script required. This is a research and writing task handled by the AI. If web search is available, use it. If not, work with what the user provides and clearly label anything that could not be verified.

## Output
- Markdown file saved to `outputs/competitor-[competitor-name-slug].md`

## Requirements
- `context/business.md` must be filled in so the comparison section is accurate.
- If web search is not available, the user may need to paste in information from the competitor's website or other sources.

## Edge Cases
- **Competitor has very little public information**: Fill in what is available, mark unknown sections as "Not publicly available", and suggest specific things the user could look into manually.
- **Competitor name is ambiguous**: Ask the user to confirm with a website URL or additional details before starting research.
- **User asks for multiple competitors at once**: Run this instruction once per competitor. Save each as a separate file. Offer to create a comparison summary after all profiles are done.
- **Competitor is much larger or smaller than your company**: Note the size difference in the comparison and focus on the specific market segments where you actually compete.

## Notes
- Be objective. The goal is an honest assessment, not a sales pitch for your company. Knowing where competitors are genuinely strong helps us improve.
- Clearly separate facts (from their website, news, public data) from inferences (your analysis). Label opinions as such.
- If the user specifies a focus area, weight the analysis toward that topic but still include the full profile structure.
- Revisit and update competitor profiles quarterly. Add a note at the top if the profile is more than 3 months old.
