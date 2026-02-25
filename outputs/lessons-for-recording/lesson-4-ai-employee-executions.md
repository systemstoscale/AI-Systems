# Lesson 4: AI Employee Executions
**Video length:** 15-20 min | **Format:** Screen share, connecting a real business tool live


> Scripts are how your AI employee connects to the outside world, pulling real-time data from APIs, scraping websites, fetching analytics. You don't write the code. Claude does. In this lesson, you'll add a new data source and connect a real business tool.

---

### What Scripts Do

```
┌────────────────┐    ┌────────────────┐    ┌────────────────┐
│  EXTERNAL      │    │  SCRIPT        │    │  YOUR          │
│  DATA          │    │                │    │  WORKSPACE     │
│                │    │ fetch-news.py  │    │                │
│  NewsAPI ──────│───→│ pulls data,    │───→│  outputs/      │
│  YouTube       │    │ formats it,    │    │  latest-       │
│  CRM           │    │ saves to       │    │  news.md       │
│  Analytics     │    │ outputs/       │    │                │
│  Any API       │    │                │    │  Claude        │
│                │    │                │    │  reads this    │
└────────────────┘    └────────────────┘    └────────────────┘
```

Pattern: Script fetches → saves to outputs/ → instruction processes it.

You don't write the code. You tell Claude what data you want. It figures out how to get it.

---

### Demo 1: Add a New News Source (Hacker News)

1. Type: `/create-plan I want a script that fetches the top 10 Hacker News posts and saves them to outputs/`

2. Claude will:
   - Research the Hacker News API
   - Design the script
   - Write the plan

3. Type: `/implement`

4. Claude will:
   - Write the script
   - Save it to scripts/
   - Test it
   - If it fails → read error → fix → retest

5. Run the script manually: `python3 scripts/fetch-hackernews.py`

---

### Demo 2: Connect a Real Business Tool

**Example: GoHighLevel (CRM)**

> "From the live call: Users asked how to connect their CRM to pull lead counts, call data, and client metrics automatically."

**The 3-step process:**

1. **Find the API settings in your tool**
   - In GoHighLevel: Settings → API → Create New Key
   - Copy the API key

2. **Add the key to your workspace**
   - Open `.env` in VS Code
   - Add a new line:
     ```
     GHL_API_KEY=your_key_here
     ```
   - Save the file

3. **Tell Claude what data you want**
   - In Claude Code, type:
     ```
     Create a script that pulls my lead count, call count, and active client count from GoHighLevel and saves it to outputs/daily-metrics.md
     ```
   - Claude will:
     - Research the GoHighLevel API documentation
     - Figure out the correct endpoints
     - Write the script
     - Test it
     - Save the output

**That's it.** No coding required.

---

### Tools You Can Connect

```
TOOL                 WHAT IT DOES                     HOW TO CONNECT
──────────────────────────────────────────────────────────────────────
NewsAPI              Latest news on any topic         Free (100/day)
Serper               Google search results            Free (2,500 credits)
Apify                Web scraping (YouTube, etc.)     Free tier
Scrape Creators      Social media scraping            Paid (from live call demo)
GoHighLevel          CRM data (leads, calls)          Find Settings → API
Notion               Knowledge base content           Settings → Integrations → API
Stripe               Revenue, subscriptions           Dashboard → Developers → API Keys
Airtable             Custom databases                 Account → API
HubSpot              Sales pipeline                   Settings → Integrations → API Key
──────────────────────────────────────────────────────────────────────
ANY API:  Add key to .env → tell Claude what you want → it builds the script
```

---

### Free APIs You Can Try Right Now

```
API                  WHAT IT DOES                     COST
──────────────────────────────────────────────────────────────
NewsAPI              Latest news on any topic         Free (100/day)
Serper               Google search results            Free (2,500 credits)
Apify                Web scraping (YouTube, etc.)     Free tier
OpenWeatherMap       Weather data                     Free (1,000/day)
Hacker News          Top tech posts                   Free (unlimited)
Reddit JSON          Subreddit posts                  Free (no key needed)
──────────────────────────────────────────────────────────────
```

At Skalers, we use Apify to scrape competitor data, LinkedIn profiles, and YouTube channels, then feed that into AI systems that generate reports and outreach. Same pattern, bigger scale. The building block is always: script pulls data → AI processes it.

---

### Key Takeaway from Live Call

> "Any tool with an API can be connected in 3 steps. The AI figures out the endpoints, writes the code, and handles errors. You just need the API key and a clear description of what data you want."

---
---
