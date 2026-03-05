---
module_id: partners
module_name: Partnership & Referral Program
module_number: 14
category: business
description: Referral tracking, testimonial collection, automated rewards
env_keys:
  required: []
  optional:
    - key: STRIPE_SECRET_KEY
      label: Stripe Secret Key
      get_url: https://dashboard.stripe.com/apikeys
      hint: "For payment tracking. Starts with sk_live_"
pip_packages: [python-dotenv, requests]
test_command: null
estimated_time: "25 minutes"
interactive_steps: true
---

# Instruction: Partnership & Referral Program Setup

## Goal
Build a referral and partnership system: affiliate tracking, testimonial collection, a public wins page, and automated referral rewards. End state: happy clients bring in new clients with minimal effort from the user.

## Inputs
- `business_model` (string): How the user charges — "subscription", "one_time", "retainer", "coaching"
- `commission_structure` (dict): Referral rewards (e.g., `{"type": "percentage", "amount": 20, "duration": "first_payment"}`)
- `payment_processor` (string): "stripe", "paypal", "other"
- `website_url` (string): Where the wins/testimonials page will live

## Steps

### 1. Design the referral program

Work with the user to define:

| Decision | Options | Recommended |
|----------|---------|-------------|
| Commission type | % of sale, flat fee, credit/discount | % for high-ticket, flat for low-ticket |
| Commission duration | First payment only, recurring, lifetime | First payment (simplest to manage) |
| Commission amount | 10-30% typical | 20% for high-ticket services |
| Payout method | Cash (Stripe), credit toward services, gift | Cash via Stripe Transfer |
| Tracking method | Referral codes, referral links, manual | Referral links + codes |
| Approval | Auto-approve, manual review | Manual review for high-ticket |

Document the program in `instructions/referral-program.md`.

### 2. Set up Stripe referral tracking

**Option A: Stripe built-in (simplest)**

Use Stripe metadata to track referrals:
1. When creating a payment link or checkout session, add metadata:
   ```json
   {
     "metadata": {
       "referrer_id": "client_123",
       "referrer_name": "John Smith",
       "referral_code": "JOHN20"
     }
   }
   ```
2. Create `scripts/track-referrals.py` that:
   - Listens for successful payments (webhook or daily scan)
   - Checks metadata for referral info
   - Logs referral in `data/referrals.json`
   - Calculates commission owed

**Option B: Stripe Connect (automated payouts)**

More setup but fully automated payouts:
1. Enable Stripe Connect on the user's Stripe account
2. Each referral partner gets a Connected Account
3. On successful payment, automatically transfer commission
4. Create `scripts/setup-partner.py` to onboard new partners

**Option C: Manual tracking (MVP)**

For getting started fast:
1. Partners share a unique discount code
2. User manually checks which sales used a code
3. Pays commission via Venmo/Zelle/wire monthly
4. Track in a spreadsheet or Airtable

**Recommendation:** Start with Option A. Graduate to Option B when volume justifies automation.

### 3. Set up referral codes and links

Create `scripts/create-referral-link.py` that:
1. Takes partner name and email
2. Generates a unique referral code (e.g., `JOHN20`)
3. Creates a tracking URL: `website.com/?ref=JOHN20`
4. Saves partner details to `data/partners.json`
5. Sends welcome email to new partner with their link and code

**Partner data structure:**
```json
{
  "partner_id": "ptr_abc123",
  "name": "John Smith",
  "email": "john@example.com",
  "referral_code": "JOHN20",
  "referral_link": "https://website.com/?ref=JOHN20",
  "commission_rate": 0.20,
  "status": "active",
  "total_referrals": 0,
  "total_earned": 0,
  "created_at": "2026-03-01"
}
```

### 4. Build the testimonial collection system

Automate collecting testimonials from happy clients:

**Trigger points:**
- After successful project delivery
- After 30/60/90 days of service
- After a milestone achievement
- After a positive reply or feedback

Create `scripts/request-testimonial.py` that:
1. Sends a personalized email requesting a testimonial
2. Includes specific prompts to get useful quotes:
   - "What was your situation before working with us?"
   - "What specific results have you seen?"
   - "Would you recommend us? Why?"
3. Optionally links to a short form (Google Form, Typeform)
4. Follows up once if no response after 5 days

**Email template:**
```
Subject: Quick favor — 2 minutes

Hey {{firstName}},

I loved working on [project/result]. Would you mind sharing a quick
testimonial about your experience?

Just reply to this email with a few sentences about:
- Where you were before
- What we built/achieved together
- Whether you'd recommend us

No pressure at all — but it would mean a lot.

[Your name]
```

### 5. Build the wins page

Create a public-facing page that showcases results and testimonials.

**Page structure:**
```
/wins or /results or /testimonials

HERO: "[X] businesses scaled with [Company Name]"

STATS BAR:
- Total clients served
- Average result metric (e.g., "3.2x ROI average")
- Client satisfaction rate

TESTIMONIALS GRID:
- Client photo/logo
- Quote (2-3 sentences)
- Name, title, company
- Key metric/result (bold)

CASE STUDIES (optional):
- Before/after with specific numbers
- Process description
- Timeline
```

Create `scripts/build-wins-page.py` that:
1. Reads testimonials from `data/testimonials.json`
2. Generates the page content (HTML or markdown)
3. Can be embedded in existing website or deployed standalone

### 6. Automate the referral workflow

Create `instructions/referral-workflow.md`:

**When a new client signs up with a referral code:**
1. Log the referral in `data/referrals.json`
2. Send confirmation to the referrer: "Great news — [Name] just signed up using your link!"
3. Set a reminder to pay commission after payment clears (7-day hold)
4. After payment clears: process commission
5. Send payout confirmation to referrer with updated stats

**Monthly partner report:**
1. Generate report for each active partner:
   - Referrals this month
   - Commission earned
   - Total lifetime earnings
   - Pending payouts
2. Save to `outputs/partner-reports/`
3. Email to each partner

### 7. Set up partner onboarding

Create `instructions/partner-onboarding.md`:

When someone wants to become a referral partner:
1. Collect: name, email, how they'll promote (social, email, word of mouth)
2. Create their referral code and link
3. Send welcome email with:
   - Their unique link and code
   - Commission structure
   - Marketing assets (logo, one-liner descriptions, sample posts)
   - FAQ (how tracking works, when they get paid, etc.)
4. Add to partner tracking system

### 8. Test the system

1. [ ] Referral code generates correctly
2. [ ] Referral link tracks to the right partner
3. [ ] Payment with referral metadata logs correctly
4. [ ] Commission calculates accurately
5. [ ] Testimonial request email sends and looks good
6. [ ] Wins page displays testimonials correctly
7. [ ] Partner report generates with correct numbers

## Script
- `scripts/create-referral-link.py` — Generate partner referral codes/links
- `scripts/track-referrals.py` — Track referral conversions and commissions
- `scripts/request-testimonial.py` — Automated testimonial collection
- `scripts/build-wins-page.py` — Generate wins/testimonials page
- `scripts/setup-partner.py` — Stripe Connect partner onboarding (optional)

## Output
- `data/partners.json` — Partner directory
- `data/referrals.json` — Referral transaction log
- `data/testimonials.json` — Collected testimonials
- `outputs/partner-reports/` — Monthly partner reports
- `instructions/referral-program.md` — Program documentation
- `instructions/referral-workflow.md` — Automated workflow
- `instructions/partner-onboarding.md` — Partner onboarding guide

## Requirements
- `STRIPE_SECRET_KEY` in `.env` (for payment tracking)
- Email sending capability (SMTP, Resend, or Loops integration)
- Website for wins page (or standalone deployment)
- Python 3, `requests`, `stripe` library

## Edge Cases
- **No Stripe**: Track referrals manually via referral codes. Use a spreadsheet or Airtable until volume justifies automation.
- **Recurring revenue model**: Decide upfront — commission on first payment only, or recurring? Recurring is more attractive to partners but more complex to track.
- **Partner disputes**: Always log the referral timestamp and source. If two partners claim the same lead, first referral code used wins.
- **Testimonial ghosting**: Most people need 2-3 asks. Space follow-ups 5-7 days apart. Offer to write a draft they can edit — much higher conversion rate.
- **International partners**: Stripe Connect handles multi-currency payouts. For manual payouts, agree on currency upfront.
- **Low-ticket products**: Flat fee referral ($50-100) works better than percentage for products under $500.

## Notes
- The #1 driver of referrals is great results, not a great referral program. Focus on client outcomes first.
- Ask for testimonials when energy is high — right after a win, not 6 months later.
- Video testimonials are 10x more powerful than text. Offer to do a 5-minute Zoom recording.
- Start the referral program with 3-5 best clients. Don't announce publicly until you've validated it works.
- After each quarter, update this file with conversion rates and top-performing partners.
