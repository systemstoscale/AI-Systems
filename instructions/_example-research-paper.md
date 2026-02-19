# Instruction: Research Paper

## Goal
Guide the user through writing an academic research paper, from defining the research question through final draft. Produce a well-structured, properly cited paper saved to `outputs/`.

## Inputs
- `topic` (string): The broad subject area or specific research question
- `course` (string, optional): The course this paper is for (helps tailor depth and format)
- `page_count` (number, optional): Target length (default: 8-10 pages)
- `citation_style` (string, optional): APA, IEEE, ACM, etc. (default: IEEE)
- `deadline` (string, optional): When the paper is due

## Steps

### 1. Define the Research Question
- Ask the user for their topic if not provided.
- If the topic is broad (e.g., "distributed systems"), help narrow it to a specific research question (e.g., "How do consistency models impact performance in distributed databases?").
- Confirm the finalized research question with the user before proceeding.

### 2. Search for Relevant Papers
- Use web search to find relevant academic papers, survey articles, and conference proceedings.
- Search using specific terms: the research question keywords, author names from known work in the field, and related terminology.
- Target 10-15 sources. Prioritize:
  - Peer-reviewed journal and conference papers
  - Recent publications (last 5 years when possible)
  - Foundational/seminal papers in the area
  - A mix of survey papers and specific studies

### 3. Create an Annotated Bibliography
- For each source, record:
  - Full citation (in the chosen citation style)
  - 2-3 sentence summary of the paper's contribution
  - How it relates to the user's research question
  - Key findings or data points to reference
- Save as `outputs/annotated-bibliography.md`

### 4. Build the Paper Outline
- Create a structured outline with the user:
  - **Abstract** (write last)
  - **Introduction** — problem statement, motivation, thesis
  - **Background / Related Work** — summarize the landscape from the bibliography
  - **Methodology** (if applicable) — approach, framework, or analysis method
  - **Discussion / Analysis** — main argument, supported by sources
  - **Conclusion** — summary of findings, limitations, future work
  - **References**
- Save outline as `outputs/paper-outline.md`

### 5. Draft Each Section
- Write one section at a time, starting with Introduction.
- After each section, pause and ask the user if they want to review or adjust before moving on.
- Use inline citations throughout (e.g., [1], [2] for IEEE style).
- Keep language clear and academic but not overly dense. Match the user's course level.

### 6. Write the Abstract
- Write the abstract last, after all sections are drafted.
- Keep it to 150-250 words. Summarize the problem, approach, findings, and significance.

### 7. Compile and Save
- Combine all sections into a single document.
- Add the references list at the end.
- Save the full paper as `outputs/research-paper.md`
- Save a separate references file as `outputs/references.md`

## Script
No script required. This is a writing-focused task handled directly by Claude.

## Output
- `outputs/annotated-bibliography.md` — annotated source list
- `outputs/paper-outline.md` — structural outline
- `outputs/research-paper.md` — complete paper draft
- `outputs/references.md` — full reference list

## Requirements
- Web search access (for finding academic sources)
- No paid APIs needed

## Edge Cases
- **Topic is too broad**: Help the user narrow it down. Ask clarifying questions: "What aspect interests you most?" "Is there a specific problem or debate within this topic?" Suggest 2-3 narrower angles to choose from.
- **Topic is too narrow / not enough sources**: If fewer than 5 relevant sources can be found, suggest broadening the scope slightly or including related adjacent topics.
- **User provides sources they already have**: Incorporate them into the bibliography first, then search for additional sources to fill gaps.
- **User wants to change direction mid-paper**: Save current progress as a separate draft (e.g., `outputs/research-paper-v1.md`), then start the new direction.
- **Citation style is unfamiliar**: Default to IEEE format. If the user requests a style you're less certain about, note the formatting and flag it for the user to double-check.

## Notes
- **Never fabricate references.** Every citation must come from a real paper found through search. If you cannot find a source to support a claim, say so and suggest the user verify it manually.
- **Never invent authors, titles, or publication details.** If you're unsure of exact citation details (volume, page numbers), include what you know and mark the rest with [verify] for the user to confirm.
- Academic integrity matters. This tool helps with research and drafting, but the user is responsible for their own original analysis and for verifying all sources.
- After each run, update this file with any lessons learned (e.g., which search terms worked best, common formatting issues).
