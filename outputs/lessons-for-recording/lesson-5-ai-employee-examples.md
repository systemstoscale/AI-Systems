# Lesson 5: AI Employee Examples
**Video length:** 20-25 min | **Format:** Screen share, running workflows + NEW proposal demo


> Watch complete workflows run from start to finish. Content creation, business operations, research, and client proposals. Each one shows the full pipeline: data in, AI processing, formatted output. Pick the one closest to your role and start using it today.

---

### Workflow 1: Content Creator

Content marketing agency example from `_examples.md`

```
INPUT                      INSTRUCTION                    OUTPUT
──────────────────────────────────────────────────────────────────────
"AI trends"           →    news-to-content           →    3 LinkedIn posts
                                                          6 tweets
                                                          1 newsletter snippet

"How to build a       →    write-blog-post           →    1,500-word SEO blog
 content calendar"                                        with metadata

blog post file        →    repurpose-content         →    3 LinkedIn posts
                                                          5 tweets
                                                          1 newsletter snippet
                                                          1 thread
```

This whole pipeline, news to content to repurposed social, takes about 5 minutes. Doing it manually takes 3+ hours.

---

### Workflow 2: Business Operations

Consulting firm ops manager example

```
INPUT                      INSTRUCTION                    OUTPUT
──────────────────────────────────────────────────────────────────────
Rough weekly notes    →    weekly-report              →    Formatted status report
                                                           with highlights, metrics,
                                                           priorities

Competitor name       →    competitor-analysis        →    Full competitor profile
                                                           with comparison table
                                                           and opportunities
```

This is exactly what our AI Fulfillment systems do at scale. Automated reporting, client status updates, competitive intelligence. We charge $60-120K to build these for enterprise clients. You're learning the same patterns for free.

---

### Workflow 3: Student / Researcher

CS student example

```
INPUT                      INSTRUCTION                    OUTPUT
──────────────────────────────────────────────────────────────────────
Research topic        →    research-paper             →    Annotated bibliography
                                                           Paper outline
                                                           Full draft
                                                           References

Course topic          →    study-guide                →    Key concepts
                                                           Practice questions
                                                           Exam topics
                                                           Answers
```

---

### Workflow 4: Automated Client Proposals (NEW — FROM LIVE CALL)

**This got multiple "wow" reactions during the live call.**

> "Max showed how he takes a call transcript and automatically generates a full proposal website with technical diagrams, project plans, and ROI breakdowns, hosted on Vercel. He uses this for a two-call close: discovery call → generate proposal → follow-up call with visual walkthrough."

```
INPUT                      INSTRUCTION                    OUTPUT
──────────────────────────────────────────────────────────────────────
Call transcript       →    generate-proposal          →    Full proposal website:
(from Zoom/Meet)                                           - Executive summary
                                                           - Technical diagrams
                                                           - Project plan
                                                           - Timeline
                                                           - ROI breakdown
                                                           - Hosted on Vercel

Use case: Two-call close
```

**How it works:**

1. Have your discovery call
2. Download the transcript (Zoom, Google Meet, or Otter.ai)
3. Drop the transcript in `inputs/`
4. Run: `/implement generate-proposal`
5. Claude:
   - Reads the transcript
   - Extracts client pain points, goals, tech stack
   - Generates a custom proposal site
   - Includes visual diagrams (system architecture, data flow)
   - Calculates ROI based on time saved
   - Deploys to Vercel
6. You get a shareable URL in 10 minutes

**Time saved:** 10-15 hours of manual proposal writing per client.

**Close rate impact:** Showing a live, custom-built system during the follow-up call dramatically increases close rates.

---

### Build Your Own

```
ANY REPEATING TASK YOU DO:

1. Identify it       →  "I write a weekly report every Monday"
2. /create-plan      →  Claude designs the workflow
3. /implement        →  Claude builds the instruction
4. Test it           →  Run the instruction, check the output
5. Iterate           →  Refine steps, add edge cases
6. Reuse forever     →  Same quality, every time, in minutes
```

Pick ONE task you do every week. Automate it before moving on to the next lesson.

---
---
