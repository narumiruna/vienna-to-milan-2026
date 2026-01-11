# Instructions for Agents

---   DO NOT EDIT  ---
- The main purpose of this project is to plan a trip from 2026-02-10 to 2026-02-28, especially focusing on food and sightseeing.
- All flights, trains, and accommodations have already been booked and are FINAL.

Agents MUST NOT:
- Suggest changing flights, trains, accommodations, or travel dates
- Suggest alternative hotels or rebooking transport
- Reorder cities or modify the travel route

## Flight Itinerary (Immutable)
- TPE→VIE BR61
  - 2/10 22:30 TPE
  - 2/11 08:25 VIE
- VIE→FCO OS557
  - 2/13 17:40 VIE
  - 2/13 19:15 FCO
- MXP→TPE BR96
  - 2/27 11:00 MXP
  - 2/28 05:55 TPE

## Train Itinerary (Immutable)
- 2/19 Roma Tiburtina → Firenze S. M. Novella
- 2/22 Firenze S. M. Novella → Venezia Mestre
- 2/25 Venezia Mestre → Milano Centrale

## Accommodation (Immutable)
- Vienna: Hilton Vienna Park
- Rome: Mercure Roma Piazza Bologna
- Firenze: Hotel Delle Nazioni
- Venice: Hotel Plaza Venice
- Milano: Hotel ibis Milano Centro

--- END DO NOT EDIT---

## Agent Mission

Build and maintain a **high-quality, evidence-based food shortlist** for each city, covering:
- Restaurants
- Cafes
- Dessert shops

All recommendations must be:
- Traceable (sources linked)
- Comparable (shared scoring rubric)
- Auditable (decisions and exclusions recorded)
- Actionable (clear top picks and backups)

---

## Required Repository Structure (Per City)

Each city directory under `gourmet/` MUST be prefixed with the arrival date (ISO), e.g. `2026-02-11-vienna/`, and MUST contain:

- overview.md  
- inbox.md  
- candidates.md  
- top-places.md  
- excluded.md  

Agents MUST respect this structure and naming.

---

## Workflow (Must Follow)

### 0 Initialize City Research

When starting research for a new city:

1. **Create overview.md first** with:
   - Travel dates and accommodation
   - Food highlights specific to the city (e.g., Roman pasta, Viennese schnitzel)
   - Research strategy and priorities
   - Current progress checklist
   - Important notes (business hours, holidays, transportation from hotel)

2. **Use web_search to gather initial candidates**:
   - Search for "best [city cuisine] restaurants [year]"
   - Search for specific dishes (e.g., "best carbonara Rome")
   - Search for "best pizza/gelato/dessert in [city]"
   - Focus on recent guides (2024-2026) and local recommendations

3. **Batch similar searches** to save time:
   - Do one search for restaurants
   - One search for pizza/casual dining
   - One search for desserts/gelato

---

### 1 Discovery — Candidate Collection

- Search broadly for food, coffee, and dessert places in the city.
- Record raw findings in:
  - inbox.md (unstructured, fast capture with quick notes)
  - and/or candidates.md (structured table)

**inbox.md structure recommendation**:
```
## Category (e.g., 傳統羅馬餐廳)
1. **Place Name**
   - 位置：area
   - 特色：key dishes/unique features
   - 注意：constraints
   - 來源：source type
```

Minimum fields per candidate in candidates.md table:
- name
- category (restaurant | cafe | dessert)
- area / neighborhood
- type (e.g. pasta, steak, espresso, gelato)
- google_maps_url (use search link initially, replace with exact link when researched)
- status: inbox | researching | shortlisted | rejected | top
- sources (brief: e.g., "Tripadvisor, Reddit, Michelin")
- notes (Traditional Chinese, brief summary)

**Prioritization**: Focus on 3-5 top candidates first, then expand. Don't try to research everything at once.

---

### 2 Evidence Collection — Per Place

For each candidate promoted to research:
- Add a detailed evidence section in `candidates.md` (keep it skimmable; link sources).
- Summarize evidence from multiple independent sources.

**Efficient research pattern**:
1. Use web_search with specific queries: "[Restaurant Name] [City] reviews rating reservation Reddit"
2. One search often provides Google Maps rating, Tripadvisor reviews, and Reddit sentiment together
3. Extract key information systematically

Required source types:
- Google Maps (rating, review count, recurring pros/cons)
- Tripadvisor or similar aggregator (rating, review count)
- Reddit (threads/comments; summarize patterns)
- One or more reputable food or travel guides (Michelin, TimeOut, local blogs)

Optional sources:
- PTT / Dcard / Chinese-language travel blogs (cite clearly if used)
- Social media mentions (TikTok, Instagram) if aggregated

Rules:
- Do NOT fabricate facts or reviews
- Clearly distinguish:
  - What sources report (use bullet points with source citations)
  - Your synthesis or inference (clearly marked)
- Include actual URLs in sources section
- Note if information is unavailable (use `unknown`)

**Evidence section template**:
```
### [Place Name]

**Official**: [website URL or "無官方網站"]

**Google Maps**: X.X/5 (Y reviews)

**Tripadvisor**: X.X/5 (Y reviews)
- [URL]

**Other ratings**: [Restaurant Guru, Foursquare, etc.]

**Guide sources**:
- [URLs with brief description]

**Reddit sentiment**:
- [Summarize patterns from multiple threads]

**Recurring pros**:
- [List from multiple sources]

**Recurring cons**:
- [List from multiple sources]

**Practical**:
- reservation requirement: 
- best visiting time: 
- closed days:
- queue:

**Score (50-point rubric)**:
- [breakdown]
```

---

### 3 Scoring — Standard Rubric

Each researched place MUST include a 50-point total score:

- Taste / Quality (0–10): Food quality, authenticity, execution
- Value (0–10): Price vs quality, portion size
- Convenience (0–10): Location, ease of reservation/access, opening hours
- Consistency (0–10): Reliability across reviews, time, visits
- Risk (0–10; 10 = low risk): Likelihood of disappointment, queue uncertainty, service issues

**Scoring guidelines**:
- 40+ = excellent, highly recommended
- 35-39 = very good, solid choice
- 30-34 = good, acceptable backup
- <30 = consider exclusion

Also record:
- reservation requirement (required | recommended | optional | none | unknown)
- best visiting time (specific times or "off-peak" etc.)
- closed days (especially Sunday/Monday)
- queue expectations (if no reservation)

---

### 4 Triage — Exclusion with Reasons

- Do NOT delete entries silently.
- Mark excluded places with:
  - status: rejected
  - a documented reason

Record exclusions in:
- excluded.md
- and/or `candidates.md` (if keeping all notes in one file)

Hard exclusion triggers:
- Strong multi-source signals of tourist traps
- Repeated hygiene or safety concerns
- Repeated severe service issues

Soft exclusion trigger:
- Total score < 30 / 50 (justification required)

---

### 5 Final Output — Top Picks

Maintain top-places.md with:
- Top Picks (high-confidence, score 35+)
- Backups (good alternatives, score 30-34)
- Researching (in-progress candidates)

**Organization by score**:
- List in descending score order within each section
- Clearly show total score for each place

Each entry MUST include:
- name
- type
- area
- total score (prominently displayed)
- google maps link
- one-line justification (why recommended)
- constraints (reservation, queues, closed days, price level)

**Additional sections to include**:
- Dining Strategy:
  - Time planning (lunch/dinner hours, local customs)
  - Reservation strategy (which places need booking, how far in advance)
  - Budget allocation (price ranges per category)
  - Transportation from hotel (how to reach different areas)
- To-Do:
  - Confirm closed days
  - Make reservations (with timing)
  - Plan daily dining schedule

---

## Process Improvements (Lessons Learned)

### Efficient Research Workflow

1. **Start with overview.md** - gives context for all other work
2. **Batch web searches** - do 3-4 searches to gather 20+ candidates quickly
3. **Prioritize ruthlessly** - research top 3-5 candidates first with full detail
4. **Use targeted searches** - "[Place] [City] reviews rating reservation Reddit" gets most info in one query
5. **Document as you go** - update files incrementally and commit frequently

### Common Patterns to Look For

When researching restaurants:
- **Tourist trap signals**: Only near major attractions, overly positive generic reviews, no locals mentioned
- **Authentic signals**: Reddit locals recommend, mixed tourist/local clientele, family-owned, specific dishes praised
- **Red flags**: Inconsistent service complaints, hygiene issues mentioned multiple times, closed unexpectedly
- **Green flags**: Michelin/guide mentions, specific dish recommendations, reservation difficulty (shows popularity)

### Time Allocation

For a new city:
- Overview + inbox collection: 30 minutes
- Detailed research per place: 15-20 minutes each
- Target: 5 detailed researches = solid foundation
- Can expand later with medium-priority candidates

### Top-places.md Strategy

- **Aim for 4-6 top picks** per city (enough variety, not overwhelming)
- **Include 2-3 backups** (alternatives if top picks unavailable)
- **Balance categories**: At least one casual option, one special occasion, one dessert/gelato
- **Geographic spread**: Cover different neighborhoods to match daily itinerary

---

## Documentation & Naming Rules

- `AGENTS.md` is written in English.
- Other documents in this repo MUST be primarily in Traditional Chinese (Taiwan).
- Use English for structured fields and keys
- Dates must follow ISO format (YYYY-MM-DD)
- Unknown information must be labeled as `unknown`
- Place filenames MUST follow:
  <city>-<normalized-place-name>.md

---

## Quality Bar

- Prefer fewer, higher-confidence picks
- Avoid relying on a single platform
- Preserve traceability at all times
- **Aim for evidence from 4+ sources per place** (Google Maps + Tripadvisor + Reddit + Guide)
- **Every score must be justifiable** from the evidence collected
- **Document uncertainty** - if information conflicts or is unavailable, note it

## Common Pitfalls to Avoid

1. **Don't research everything at once** - focus on top candidates first
2. **Don't skip overview.md** - context is crucial for prioritization
3. **Don't rely on single sources** - cross-reference at least 3-4 sources
4. **Don't forget practical constraints** - reservation policies, closed days, queue times matter
5. **Don't over-optimize scores** - a 35-40 range is realistic for good places; not everything is 45+
6. **Don't neglect geographic distribution** - consider travel time from hotel

## Research Questions Checklist

For each researched place, ensure you can answer:
- ✓ What is the exact rating and review count?
- ✓ What do Reddit users say about it?
- ✓ What are the signature dishes?
- ✓ Do I need a reservation? How far in advance?
- ✓ When is it closed? (day of week)
- ✓ What is the expected wait time without reservation?
- ✓ What is the approximate price range?
- ✓ What are the most common complaints?
- ✓ Is it touristy or more local?

## MCP

- You will leverage MCP tools to search for the information you need.
- Document design will consider progressive disclosure.
- If rate limits are hit, then try another tool or wait before retrying.
- The rate limits of firecrawl search is 5 times per minute.
