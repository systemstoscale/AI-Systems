---
module_id: analyze-sales-call
module_name: Sales Call Analyzer
category: sales
description: Analyzes a sales call transcript from Google Meet and outputs deal intelligence, follow-up email drafts, content ideas, and a close strategy.
env_keys:
  required: []
  optional: []
pip_packages: []
test_command: "# Paste a short transcript excerpt into outputs/test-transcript.md and run the instruction"
---

# Sales Call Analyzer

## Goal

Turn a sales call transcript into actionable intelligence: extract objections, buying signals, and decision criteria — then generate follow-up emails, content ideas, and a specific close strategy.

## Inputs

- `outputs/transcript-[date].md` — the raw Google Meet transcript (fetched by `scripts/fetch-google-doc.py`)

## Steps

### 1. Load the Transcript

Read the transcript file from `outputs/`. If multiple transcript files exist, use the most recently modified one unless the user specifies otherwise.

### 2. Extract Deal Intelligence

Go through the transcript and pull out:

**Objections**
- What explicit objections did they raise? (price, timing, trust, fit, competition)
- What was the real underlying concern behind each objection?
- How did the objection get handled on the call — and did it land?

**Buying Signals**
- What moments showed genuine interest? (leaning in, asking implementation questions, mentioning urgency)
- What did they say that suggests they see value?

**Decision Criteria**
- What do they need to believe before buying?
- Who else is involved in the decision?
- What timeline are they working with?

**Competitor / Alternative Mentions**
- Did they mention other solutions they're considering?
- What were they comparing us against?

**Momentum Gaps**
- Where did the energy drop in the call?
- What question or topic caused confusion or resistance?
- What was left unresolved at the end?

### 3. Generate Follow-Up Emails

Write 3 follow-up email drafts. Each should be under 150 words, direct, and end with one clear CTA.

**Email 1 — Send within 24 hours**
- Address the primary objection head-on
- Don't restate everything from the call — move the conversation forward
- CTA: a specific next step (link, reply, document)

**Email 2 — Send 3 days later**
- Add new value (case study, result, resource relevant to their situation)
- Reduce friction on the main hesitation
- CTA: book a follow-up call or reply with their question

**Email 3 — Send 7 days later**
- Final touchpoint — close or refer
- If they're not ready: ask for a referral or a future check-in date
- CTA: binary choice (yes/not now)

### 4. Generate Content Ideas

Extract 3 YouTube video ideas from the call. These should be based on:
- Questions they asked that show confusion about something obvious to you
- Objections that other prospects probably share
- Topics they got excited about

For each idea:
- **Title:** Specific, outcome-focused (not "How AI Works" — "Why Your AI Chatbot Isn't Getting You Clients")
- **Angle:** The insight or counterintuitive point the video makes
- **Hook line:** First sentence of the video that grabs the viewer who has this exact problem

### 5. Close Strategy

One specific recommendation for the next touchpoint with this prospect.

Format:
- **Lead with:** (what angle or topic to open with)
- **Reframe:** (how to reposition the main objection)
- **Ask:** (the exact close question to use)

## Output

Save the full report to `outputs/call-analysis-[prospect-name]-[date].md`.

Structure:
```
# Call Analysis — [Name] — [Date]

## Deal Intelligence
### Objections
### Buying Signals
### Decision Criteria
### Competitors / Alternatives
### Momentum Gaps

## Follow-Up Emails
### Email 1 (Send: within 24h)
### Email 2 (Send: day 3)
### Email 3 (Send: day 7)

## Content Ideas
### Idea 1
### Idea 2
### Idea 3

## Close Strategy
```

## Requirements

- Be specific. Don't write generic follow-ups — pull actual language from the transcript.
- Email drafts should sound like Max wrote them, not like a template.
- Content ideas should be titles you'd actually click on, not vague topics.
- Close strategy should be one concrete play, not a list of options.

## Edge Cases

- **No clear objection:** Note that the prospect may not be a fit, and flag what to probe on the next call.
- **Very short transcript:** Do your best with what's available. Flag that the analysis may be incomplete.
- **Multiple prospects on the call:** Distinguish between decision-maker and influencer signals.
