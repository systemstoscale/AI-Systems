---
module_id: prospecting
module_name: Prospecting Pipeline
module_number: 9
category: business
description: Automated outbound pipeline — scrape, enrich, send, classify replies
env_keys:
  required:
    - key: ANTHROPIC_API_KEY
      label: Anthropic API Key
      get_url: https://console.anthropic.com/settings/keys
      hint: "For reply classification. Starts with sk-ant-"
  optional:
    - key: APOLLO_API_KEY
      label: Apollo API Key
      get_url: https://app.apollo.io/#/settings/integrations/api-keys
      hint: "For B2B lead search"
    - key: BETTERCONTACT_API_KEY
      label: BetterContact API Key
      get_url: https://app.bettercontact.rocks/settings/api
      hint: "For email enrichment/verification"
    - key: INSTANTLY_API_KEY
      label: Instantly API Key
      get_url: https://app.instantly.ai/settings/integrations
      hint: "For cold email sending"
pip_packages: [python-dotenv, requests]
test_command: null
estimated_time: "30 minutes"
interactive_steps: true
---

# Instruction: Prospecting Pipeline Setup

## Goal
Build an automated outbound prospecting pipeline: scrape leads from a source, enrich with verified emails, load into cold email campaigns, and classify replies for follow-up. End state: leads flow in automatically and replies get routed to the right follow-up sequence.

## Inputs
- `lead_source` (string): Where to find leads — "apollo", "skool", "facebook_ads", "linkedin", "website_scrape", or custom
- `niche` (string): Target audience description (e.g., "e-commerce brands doing $1M+/yr")
- `sending_accounts` (list): Email accounts for sending (ideally 3+ across 2+ domains)
- `offer` (string): What you're offering in the cold email (1 sentence)
- `calendar_link` (string): Booking link for interested replies

## Steps

### 1. Choose your lead source

Pick one to start. You can layer more sources later.

| Source | Best For | Script Needed |
|--------|----------|---------------|
| Apollo | B2B by job title, company size, industry | `scripts/apollo-search.py` |
| Skool | Community owners, course creators | `scripts/scrape-skool.py` |
| Facebook Ads | Active advertisers in a niche | `scripts/meta-ad-scraper.py` |
| LinkedIn | Specific roles at specific companies | Manual export or PhantomBuster |
| Website scrape | Businesses listed on directories | `scripts/scrape-website.py` |

Ask the user which source fits their audience best. If unsure, start with Apollo — it has the broadest coverage for B2B.

### 2. Build the lead scraper

Create a script in `scripts/` that:
1. Connects to the chosen source API
2. Searches with the user's niche criteria
3. Extracts: `first_name`, `last_name`, `email` (if available), `company_name`, `company_domain`, `title`, `source_url`
4. Saves to `outputs/leads-raw-[YYYY-MM-DD].csv`

**Apollo example:**
```python
# Search for marketing directors at e-commerce companies
params = {
    "person_titles": ["Marketing Director", "VP Marketing", "CMO"],
    "organization_num_employees_ranges": ["50,200"],
    "per_page": 100
}
```

**Important:** Always check `scripts/` for existing scrapers before building new ones.

### 3. Set up email enrichment

Raw leads often have missing or unverified emails. Set up a verification step:

**Option A: BetterContact (recommended for waterfall enrichment)**
1. Get API key at bettercontact.rocks
2. Add `BETTERCONTACT_API_KEY` to `.env`
3. Create `scripts/enrich-leads.py` that:
   - Reads raw leads CSV
   - Submits batch to BetterContact async API
   - Polls for results (takes 10-20 minutes per batch)
   - Filters to `deliverable` and `catch_all_safe` emails only
   - Saves to `outputs/leads-enriched-[YYYY-MM-DD].csv`

**Option B: Apollo built-in (if using Apollo as source)**
- Apollo returns emails directly, but verify status
- Filter to `verified` and `guessed` statuses only

**Option C: Anymailfinder / Hunter / other single-source**
- Faster but lower match rates than waterfall
- Good for quick tests

### 4. Set up cold email sending

**Instantly.ai setup:**
1. Get API key from Instantly dashboard
2. Add `INSTANTLY_API_KEY` to `.env`
3. Connect sending accounts in Instantly UI (DNS warmup takes 2 weeks)
4. Create `scripts/launch-campaign.py` that:
   - Creates a campaign via API
   - Uploads enriched leads
   - Sets email sequence (3-step minimum)
   - Activates campaign

**Email sequence template (customize with user's offer):**

```
Step 1 (Day 0): Introduction + value prop
Step 2 (Day 3): Follow-up with case study or proof
Step 3 (Day 7): Breakup email — last chance, different angle
```

**Writing the emails:**
- Read `context/business.md` for offer details and voice
- Keep emails under 100 words
- One clear CTA per email (usually: reply or book a call)
- Use personalization: `{{firstName}}`, `{{companyName}}`
- Use spintax for variation: `{{RANDOM | Hey | Hi}} {{firstName}},`
- No images, no HTML formatting, no links in first email (deliverability)

### 5. Set up reply classification

When leads reply, classify them automatically:

| Category | Signal | Action |
|----------|--------|--------|
| Interested | Asks questions, wants to learn more | Send more info or book call |
| Schedule | Wants to meet, asks for times | Send calendar link |
| Not Now | Busy, maybe later, timing wrong | Add to follow-up-later sequence |
| Not Interested | No thanks, not relevant | Remove from campaign |
| Referral | "Talk to my colleague..." | Add referral to new campaign |
| Out of Office | Auto-reply, OOO | Retry in 2 weeks |
| Unsubscribe | Remove me, stop emailing | Remove immediately |

Create `scripts/classify-reply.py` that:
1. Receives reply text (from webhook or manual input)
2. Uses Claude to classify into one of the categories above
3. Suggests or executes the appropriate action

**Optional: Webhook automation**
- Set up Instantly webhook → n8n or custom endpoint
- Auto-classify and route replies to subsequences
- This is Phase 2 — start with manual classification first

### 6. Create the daily workflow

Document the daily prospecting routine in `instructions/daily-prospecting.md`:

```
Morning (10 min):
1. Check reply classifications from overnight
2. Handle "Interested" and "Schedule" replies personally
3. Review campaign metrics (open rate, reply rate)

Weekly (30 min):
1. Scrape new leads (run lead source script)
2. Enrich new batch (run enrichment script)
3. Load into active campaign or create new one
4. Review and update email copy based on reply patterns
```

### 7. Test the full pipeline

Before going live:
1. [ ] Scraper pulls leads with correct fields
2. [ ] Enrichment returns verified emails (>30% match rate is healthy)
3. [ ] Campaign creates successfully in Instantly
4. [ ] Test emails land in inbox (send to yourself first)
5. [ ] Reply classifier correctly categorizes sample replies
6. [ ] Calendar link works and books correctly

## Script
- `scripts/apollo-search.py` (or chosen source scraper)
- `scripts/enrich-leads.py`
- `scripts/launch-campaign.py`
- `scripts/classify-reply.py`

## Output
- `outputs/leads-raw-[YYYY-MM-DD].csv` — Raw scraped leads
- `outputs/leads-enriched-[YYYY-MM-DD].csv` — Verified, ready to send
- `instructions/daily-prospecting.md` — Daily workflow doc

## Requirements
- Lead source API key (Apollo, BetterContact, etc.) in `.env`
- `INSTANTLY_API_KEY` in `.env` (or alternative sending platform)
- `ANTHROPIC_API_KEY` in `.env` (for reply classification)
- 3+ warmed sending accounts (2-week warmup before live sends)
- Python 3, `requests` library

## Edge Cases
- **Low enrichment match rate (<20%)**: The niche may be too small or companies lack web presence. Try a different lead source or broaden criteria.
- **Emails landing in spam**: Check DNS (SPF, DKIM, DMARC), reduce daily send volume, simplify email copy (no links, no images in first touch).
- **Apollo rate limits**: 100 requests/minute on most plans. Add 1-second delays between calls.
- **BetterContact slow processing**: Batches of 5 leads take 10-20 minutes. Submit larger batches and poll periodically. Set timeout to 1200s.
- **Instantly campaign not sending**: Check that sending accounts are connected, warmed up, and campaign is activated. New accounts need 14 days warmup.
- **Too many unsubscribe/negative replies**: Email copy needs work. Review messaging, make it more relevant, less salesy.

## Notes
- Start with ONE lead source and ONE campaign. Get it working end-to-end before adding complexity.
- Send 20-30 emails/day per account max during warmup. Scale to 50/day after 2 weeks.
- Best subject lines are 3-5 words, look like a personal email.
- Track reply rate as the key metric. Industry average is 2-5%. Above 5% means your targeting and copy are strong.
- After each run, update this file with what worked and what didn't.
