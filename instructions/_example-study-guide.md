# Instruction: Study Guide

## Goal
Create a comprehensive study guide for a given subject or topic. The guide should cover key concepts, definitions, practice questions, and common exam topics to help prepare for tests and reinforce understanding.

## Inputs
- `subject` (string): The course or subject (e.g., "Distributed Systems", "Linear Algebra")
- `topic` (string, optional): A specific topic within the subject (e.g., "Consensus Algorithms", "Eigenvalues"). If not provided, create a broad guide for the full subject.
- `exam_focus` (string, optional): Specific areas the exam will cover, if known (e.g., "midterm covers chapters 1-6")
- `difficulty` (string, optional): "introductory", "intermediate", or "advanced" (default: "intermediate")

## Steps

### 1. Clarify the Scope
- Ask the user what subject and topic they need a study guide for.
- Ask if there's a specific exam coming up and what it covers.
- Determine depth: Is this a quick review or a deep dive?

### 2. Gather Key Concepts
- Identify the core concepts for the topic. Use web search if needed to confirm coverage and terminology.
- Organize concepts from foundational to advanced, so the guide builds understanding progressively.

### 3. Write the Study Guide
Structure the guide with these sections:

#### Overview
- 2-3 sentence summary of the topic and why it matters.

#### Key Concepts
- List each concept with:
  - **Definition**: Clear, concise explanation
  - **Why it matters**: How it connects to the bigger picture
  - **Example**: A concrete example or analogy to make it stick

#### Important Formulas / Theorems / Rules
- List any formulas, theorems, or rules that need to be memorized.
- Include when and how to use each one.

#### Common Patterns and Relationships
- Explain how concepts relate to each other.
- Include comparison tables where helpful (e.g., "CAP Theorem: Consistency vs. Availability").

#### Practice Questions
- Create 8-12 practice questions, mixing:
  - **Conceptual questions** (test understanding, not just memorization)
  - **Short answer** (define, compare, explain)
  - **Problem-solving** (apply concepts to scenarios)
  - **Exam-style** (formatted like typical test questions for this subject)
- Put answers in a separate section at the end so the user can self-test.

#### Common Exam Topics
- List topics that frequently appear on exams for this subject.
- Note common mistakes and traps to watch out for.

#### Further Reading
- Suggest 2-3 resources for deeper understanding (textbook chapters, online references, video lectures).

### 4. Save the Guide
- Save the completed guide as `outputs/study-guide-[topic].md` (e.g., `outputs/study-guide-consensus-algorithms.md`).
- Use lowercase and hyphens in the filename.

## Script
No script required. This is a writing-focused task handled directly by Claude.

## Output
- `outputs/study-guide-[topic].md` — the complete study guide

## Requirements
- Web search access (optional, for verifying concepts and finding supplementary resources)
- No paid APIs needed

## Edge Cases
- **Topic is too broad** (e.g., "all of computer science"): Ask the user to pick a specific course or unit. Suggest breaking it into multiple guides.
- **Topic is very niche**: Do your best with available knowledge. Flag any areas where the user should verify with their course materials.
- **User provides lecture notes or slides**: Use them as the primary source for the guide. Organize and expand on the notes rather than generating from scratch.
- **Multiple topics requested at once**: Create separate guide files for each topic rather than one giant document.
- **User wants flashcard format instead**: Adapt the output to a list of Q&A pairs, one per line, saved as `outputs/flashcards-[topic].md`.

## Notes
- Match the terminology and depth to the user's course level. A "Distributed Systems" guide for a junior CS student should be more practical and example-driven than one for a graduate seminar.
- Always include practice questions with answers. Self-testing is one of the most effective study techniques.
- If the user mentions a specific textbook, align the guide's structure and terminology with that textbook when possible.
- After each run, update this file with any lessons learned (e.g., which formats the user found most helpful, topics that needed more depth).
