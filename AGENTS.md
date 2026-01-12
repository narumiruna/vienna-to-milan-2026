# Instructions for Agents

## Table of Contents

1. [Main Purpose (Immutable)](#main-purpose-immutable)
2. [Agent Mission](#agent-mission)
3. [Working with Agents: Ensuring Task Completion](#working-with-agents-ensuring-task-completion)
4. [Research Completion Standard](#research-completion-standard)
5. [Required Repository Structure (Per City)](#required-repository-structure-per-city)
6. [Progressive Disclosure Principle](#progressive-disclosure-principle)
7. [Workflow (Must Follow)](#workflow-must-follow)
   - [0. Initialize City Research](#0-initialize-city-research)
   - [1. Discovery — Candidate Collection](#1-discovery--candidate-collection)
   - [2. Evidence Collection — Per Place](#2-evidence-collection--per-place)
   - [3. Scoring — Standard Rubric](#3-scoring--standard-rubric)
   - [4. Triage — Exclusion with Reasons](#4-triage--exclusion-with-reasons)
   - [5. Final Output — Top Picks](#5-final-output--top-picks)
   - [6. Post-Research Updates — Documentation Maintenance](#6-post-research-updates--documentation-maintenance)
8. [Process Improvements (Lessons Learned)](#process-improvements-lessons-learned)
9. [Documentation & Naming Rules](#documentation--naming-rules)
10. [Quality Bar](#quality-bar)
11. [Common Pitfalls to Avoid](#common-pitfalls-to-avoid)
12. [Research Questions Checklist](#research-questions-checklist)
13. [Quick Reference](#quick-reference) ⭐

---

## Main Purpose (Immutable)

- The main purpose of this project is to plan a trip from 2026-02-10 to 2026-02-28, especially focusing on food.
- All flights, trains, and accommodations have already been booked and are FINAL.

Agents MUST NOT:
- Suggest changing flights, trains, accommodations, or travel dates
- Suggest alternative hotels or rebooking transport
- Reorder cities or modify the travel route

### Flight Itinerary (Immutable)
- TPE→VIE BR61
  - 2/10 22:30 TPE
  - 2/11 08:25 VIE
- VIE→FCO OS557
  - 2/13 17:40 VIE
  - 2/13 19:15 FCO
- MXP→TPE BR96
  - 2/27 11:00 MXP
  - 2/28 05:55 TPE

### Train Itinerary (Immutable)
- 2/19 Roma Tiburtina → Firenze S. M. Novella
- 2/22 Firenze S. M. Novella → Venezia Mestre
- 2/25 Venezia Mestre → Milano Centrale

### Accommodation (Immutable)
- Vienna: Hilton Vienna Park
- Rome: Mercure Roma Piazza Bologna
- Firenze: Hotel Delle Nazioni
- Venice: Hotel Plaza Venice
- Milano: Hotel ibis Milano Centro

## Agent Mission

Build and maintain a **high-quality, evidence-based food shortlist** for each city.

**Coverage:**
- 🍽️ Restaurants
- ☕ Cafes
- 🍰 Dessert shops

**Quality Standards - All recommendations must be:**
- ✅ **Traceable**: Sources linked with URLs
- ✅ **Comparable**: Shared 50-point scoring rubric
- ✅ **Auditable**: Decisions and exclusions documented
- ✅ **Actionable**: Clear top picks (35+) and backups (30-34)

---

## Working with Agents: Ensuring Task Completion

### How to Keep Agents Working Until Completion

**Problem**: Agents may stop mid-task, leaving research incomplete.

**Solutions**:

1. **Break large tasks into clear, atomic steps**
   - ✅ "Research and score Pompi tiramisu" (specific, achievable)
   - ❌ "Research all tiramisu in Italy" (too broad, likely to stop mid-way)

2. **Set clear completion criteria in instructions**
   - Define what "done" means (e.g., "score must be in candidates.md AND notes.md")
   - Agent will work toward the defined end state

3. **Use progress tracking tools**
   - Agent should call `report_progress` after each meaningful unit of work
   - This creates checkpoints and shows what's left

4. **Provide task checklists**
   - Include a checklist in your request (e.g., "Research 3 restaurants: A, B, C")
   - Agent can track progress and know when complete

5. **Avoid ambiguous scope**
   - ✅ "Add top 3 tiramisu places to Rome candidates" (clear boundary)
   - ❌ "Research tiramisu" (unclear when to stop)

### When Agent Stops Unexpectedly

**If agent stops mid-research**:
- Check the last commit to see what was completed
- Verify files in git status to confirm progress

**If agent repeatedly stops**:
- Break the task into smaller chunks
- Ask agent to complete one specific file at a time
- Use "complete X, then Y, then Z" format

---

## Research Completion Standard

For detailed completion criteria, status definitions, and verification checklists, see [PROGRESS.md - Research Completion Standard](PROGRESS.md#-研究完成標準).

**Quick Reference:**
- A city is marked "✅ 已完成" when ALL of the following are met:
  1. All candidates triaged (no `status: inbox` in candidates.md)
  2. No pending decisions in excluded.md
  3. top-places.md finalized (Top Picks, Backups, Dining Strategy, To-Do)
  4. overview.md checklist fully checked `[x]`

**Status Indicators:**
- ⏳ 未開始 (Not Started) → 📝 研究中 (In Progress) → 🔄 待完成 (Needs Finalization) → ✅ 已完成 (Completed)

---

## Required Repository Structure (Per City)

Each city directory under `gourmet/` MUST be prefixed with the arrival date (ISO), e.g. `2026-02-11-vienna/`, and MUST contain:

- overview.md  
- inbox.md  
- candidates.md  
- notes.md  
- top-places.md  
- excluded.md  

Agents MUST respect this structure and naming.

**All documentation must follow the Progressive Disclosure Principle** (see dedicated section below for details).

---

## Progressive Disclosure Principle

**Progressive disclosure** is a design principle where information is revealed gradually, showing only what's necessary at each stage while providing paths to deeper detail when needed.

### Why This Matters

In this project:
- **Travelers need quick answers** (e.g., "What are the top 3 places for dinner?")
- **But decisions require justification** (e.g., "Why did you exclude Restaurant X?")
- **Research depth varies** (quick scan → detailed investigation → deep dive)

Progressive disclosure prevents:
- ❌ Overwhelming users with all details upfront
- ❌ Hiding critical information too deeply
- ❌ Making quick decisions difficult
- ❌ Losing traceability of research rationale

### How We Apply It

#### File Structure (Layered Information)

```
overview.md       ← START HERE: Context, strategy, progress (5 min read)
    ↓
top-places.md     ← ACTIONABLE: Final recommendations (10 min read)
    ↓
candidates.md     ← SUMMARY: Quick scan table (5-10 min read)
    ↓
notes.md          ← EVIDENCE: Detailed research (30+ min read)
    ↓
inbox.md          ← RAW DATA: Working notes (exploratory)
    ↓
excluded.md       ← REJECTED: What was excluded and why (5 min read)
```

**Each file serves a distinct purpose**:
- **overview.md**: Quick orientation (5-minute read)
- **top-places.md**: Decision-making (10-minute read, includes dining strategy)
- **candidates.md**: Summary table (quick scan, 5-10 minutes, shows all candidates with scores and status)
- **notes.md**: Detailed evidence (deep dive, 30+ minutes, full research trail for each place)
- **inbox.md**: Working space (exploratory, always in flux)
- **excluded.md**: Audit trail (transparency, prevents re-research)

#### Within-Document Disclosure

**In candidates.md**:
1. **Summary table only** (see "Discovery — Candidate Collection" section for complete field list) → quick scan
2. **No detailed sections** - these belong in notes.md
3. **Brief notes column** - one-line summary per place (Traditional Chinese)
4. **English headers required** - table column names must be in English (e.g., "name", "status", "notes") even though content is in Traditional Chinese

**In notes.md**:
1. **Detailed evidence sections** per place → deep research trail
2. **Source citations** with URLs → full traceability
3. **Scoring rationale** → justification for each score component
4. **Practical information** → reservation, queues, closed days, etc.

**In top-places.md**:
1. **Top Picks** first (35+ scores) → immediate action
2. **Backups** second (30-34 scores) → alternatives if needed
3. **Dining Strategy** → logistics and planning
4. **To-Do items** → execution checklist

**In overview.md**:
1. **Travel info** → immediate context
2. **Food highlights** → city-specific focus
3. **Strategy** → research approach
4. **Progress checklist** → current status

### Guidelines for Agents

When creating or updating documentation:

1. **Start with the answer, then justify**
   - ✅ "Top Pick: Restaurant X (42/50) - Exceptional pasta, reliable service"
   - ❌ "After reviewing 15 sources and analyzing 200 reviews... Restaurant X"

2. **Use visual hierarchy**
   - Headers, scores, and key facts should stand out
   - Details should be scannable (bullets, short paragraphs)
   - Full evidence goes in expandable sections or separate files

3. **Link, don't duplicate**
   - overview.md references top-places.md
   - top-places.md links to candidates.md for quick scan
   - candidates.md table rows can reference notes.md for detailed evidence
   - Avoid copying the same information into multiple files

4. **Respect the reader's journey**
   - Someone planning their day → starts at top-places.md
   - Someone wanting a quick overview → checks candidates.md table
   - Someone questioning a score → digs into notes.md for evidence
   - Someone auditing research → checks excluded.md

5. **Maintain traceability without overwhelming**
   - Every score must be justifiable (in notes.md)
   - Every top pick must have evidence (sources in notes.md)
   - But candidates.md and top-places.md stay concise with summary info only

### Anti-Patterns to Avoid

- ❌ Putting all research in one massive file
- ❌ Mixing summary tables with detailed evidence in candidates.md
- ❌ Hiding final recommendations deep in notes
- ❌ Forcing readers to read everything to find actionable info
- ❌ Removing audit trails (deleted places, score changes)
- ❌ Creating too many layers (more than 6 files per city)

### Example Flow

**Quick Trip Planning (5 minutes)**:
```
README.md → [select city] → top-places.md → Done
```

**Quick Candidate Scan (10 minutes)**:
```
candidates.md → Scan table with scores and status → Identify priorities
```

**Reservation Planning (15 minutes)**:
```
top-places.md → Check constraints → Make reservations → Update To-Do
```

**Deep Research Review (1 hour)**:
```
overview.md → top-places.md → candidates.md → notes.md → Check all sources → Validate scores
```

**Investigating an Exclusion (5 minutes)**:
```
excluded.md → Find place → Read reason → (Optional: check notes.md for full details)
```

---

## Workflow (Must Follow)

**This section defines the complete research workflow from start to finish. Follow these steps in order for each city.**

> **💡 Tip:** Start with step 0 for a new city, then iterate through steps 1-5 for each candidate. Complete with step 6 before marking the city as done.

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

**Required fields per candidate in candidates.md table:**
- name
- category (restaurant | cafe | dessert)
- area / neighborhood
- type (e.g. pasta, steak, espresso, gelato)
- google_maps_url (see Google Maps Link Requirement below)
- status: inbox | researching | shortlisted | rejected | top
- sources (brief: e.g., "Tripadvisor, Reddit, Michelin")
- notes (Traditional Chinese, brief summary)

**Optional fields:**
- score (e.g., "39/50" or "TBD") - can be included for quick reference, though detailed scoring should always be in notes.md

**Google Maps Link Requirement**:
- ✅ Acceptable formats:
  - Direct Google Maps links: `https://maps.app.goo.gl/...`
  - Search API links: `https://www.google.com/maps/search/?api=1&query=[Place+Name+City]`
- ⚠️ Avoid using:
  - `https://www.google.com/maps/place/...` (place page URL)
- ❌ NOT acceptable:
  - Generic placeholders like `[查看地圖]` or `[View Map]` without proper URLs
- **How to get direct links**:
  1. Search for the place on Google Maps
  2. Click on the specific place to open its info panel
  3. Click "Share" button
  4. Copy the short link (maps.app.goo.gl format) OR use search API format
- Links MUST be tested/verified to point to the correct location

**Prioritization**: Focus on 3-5 top candidates first, then expand. Don't try to research everything at once.

**⚠️ CRITICAL: Preserving candidates.md Table Entries**

**DO NOT delete or remove entries from the candidates.md summary table** unless absolutely necessary for one of the following reasons:

**Acceptable reasons to modify/remove table entries:**
1. **Duplicate entries**: Same restaurant appears multiple times in table (merge into one entry with combined information)
2. **Incorrect information**: Restaurant name, location, or category is wrong and needs correction
3. **Restaurant permanently closed**: Confirmed closure (must note in excluded.md)
4. **Explicit instruction**: User specifically requests removal

**NEVER remove entries because:**
- ❌ They are not yet researched (keep as `status: inbox`)
- ❌ They seem lower priority (move to excluded.md with reason instead)
- ❌ There are already enough candidates (document decision in excluded.md)
- ❌ You think they won't be needed (let user decide; move to excluded.md if appropriate)

**Correct workflow for unwanted candidates:**
1. Keep entry in candidates.md table with `status: rejected`
2. Add detailed reason to excluded.md under "未進一步研究的候選 (Not Researched Further)" or similar section
3. Explain why it was not researched (e.g., "已有足夠推薦", "優先級較低", "地點過遠")

**Why this matters:**
- Preserves research trail and avoids duplicate work
- Maintains audit trail of all candidates considered
- Prevents accidental loss of potentially valuable options
- Allows user to see full scope of research

**When recovering deleted entries:**
- If entries were accidentally deleted, restore them to the table
- Add detailed research sections if available
- Update excluded.md to remove them from "未進一步研究" if they are now researched

---

### 2 Evidence Collection — Per Place

For each candidate promoted to research:
- Add a detailed evidence section in `notes.md` (keep it skimmable; link sources).
- Update the candidates.md table row with brief summary in notes column.
- Summarize evidence from multiple independent sources.

**Efficient research pattern**:
1. Use web_search with specific queries: "[Restaurant Name] [City] reviews rating reservation Reddit"
2. One search often provides Google Maps rating, Tripadvisor reviews, and Reddit sentiment together
3. Extract key information systematically
4. Document full evidence in notes.md, update candidates.md table with status and brief summary

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

**Evidence section template (for notes.md)**:
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
- excluded.md (primary location for all exclusion reasons)
- Update candidates.md table with `status: rejected`

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

**Google Maps Link Requirement**:
- Every place in top-places.md MUST have a valid, working Google Maps link
- See [Section 1: Google Maps Link Requirement](#1-discovery--candidate-collection) for acceptable formats and how to obtain links
- **Consistency**: Use the same link format from candidates.md to maintain traceability

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

### 6 Post-Research Updates — Documentation Maintenance

**After completing research for a city, MUST do the following**:

1. **Verify Research Completion Standard** (see [PROGRESS.md - Research Completion Standard](PROGRESS.md#-研究完成標準)):
   - ✅ All candidates triaged (no `status: inbox` remaining)
   - ✅ No pending decisions in excluded.md
   - ✅ top-places.md finalized with Top Picks and Dining Strategy
   - ✅ overview.md checklist fully marked `[x]`
   - Run the verification commands from PROGRESS.md

2. **Update progress tracking**:
   - Update PROGRESS.md with current status (primary source of truth)
   - Sync README.md progress table to match PROGRESS.md
   - Use accurate status icon based on completion criteria:
     - ⏳ 未開始 → 📝 研究中 → 🔄 待完成 → ✅ 已完成
   - Only use ✅ when ALL completion criteria are met
   - Update 重點推薦 count
   - Add relevant notes about research completion

3. **Update AGENTS.md if workflow improved**:
   - If you discovered a more efficient research method, document it in "Process Improvements (Lessons Learned)"
   - If you found common patterns or pitfalls, add them to relevant sections
   - Keep the workflow documentation current with actual practices

**Why this matters**:
- PROGRESS.md serves as the project progress dashboard - it must reflect current reality
- README.md provides a quick overview that syncs with PROGRESS.md
- Completion standards ensure consistency across all cities
- AGENTS.md captures institutional knowledge - improvements benefit future research
- Consistent updates prevent confusion and duplicate work

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

- **Aim for 5-10 top picks** per city (enough variety, not overwhelming)
- **Include 3-5 backups** (alternatives if top picks unavailable)
- **Balance categories**: At least one casual option, one special occasion, one dessert/gelato
- **Geographic spread**: Cover different neighborhoods to match daily itinerary

---

## Documentation & Naming Rules

- `AGENTS.md` and `PROGRESS.md` MUST be written in English.
- Other documents in this repo MUST be primarily in Traditional Chinese (Taiwan).
- Use English for structured fields and keys (table headers, status values, etc.)
- Dates must follow ISO format (YYYY-MM-DD)
- Unknown information must be labeled as `unknown`
- City directory names MUST follow: `YYYY-MM-DD-city/` (e.g., `2026-02-11-vienna/`)

---

## Quality Bar

**Core Principles:**
- ✅ Prefer fewer, higher-confidence picks
- ✅ Avoid relying on a single platform
- ✅ Preserve traceability at all times

**Research Standards:**
- **Minimum 4+ sources per place**: Google Maps + Tripadvisor + Reddit + Food Guide
- **Every score must be justifiable**: Document evidence in notes.md
- **Document uncertainty**: If information conflicts or is unavailable, note it explicitly

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

---

## Quick Reference

### File Structure (Per City)
```
gourmet/YYYY-MM-DD-city/
├── overview.md       (5min)  - Context & strategy
├── top-places.md     (10min) - Final recommendations
├── candidates.md     (5min)  - Summary table
├── notes.md          (30min) - Detailed evidence
├── inbox.md          (working) - Raw capture
└── excluded.md       (5min)  - Rejected with reasons
```

### Scoring Rubric (50 points total)
- **Taste/Quality** (0-10): Food quality, authenticity, execution
- **Value** (0-10): Price vs quality, portion size
- **Convenience** (0-10): Location, ease of access/reservation
- **Consistency** (0-10): Reliability across reviews
- **Risk** (0-10): Low risk = 10, high risk = 0

**Score Ranges:**
- 40+: Excellent, highly recommended (Top Pick)
- 35-39: Very good, solid choice (Top Pick)
- 30-34: Good, acceptable (Backup)
- <30: Consider exclusion

### Required Sources (Minimum 4)
1. Google Maps (rating + review count)
2. Tripadvisor or similar aggregator
3. Reddit (threads/comments)
4. Food/travel guide (Michelin, TimeOut, local blogs)

### Completion Criteria (All Required)
✅ No `status: inbox` items in candidates.md
✅ No pending decisions in excluded.md
✅ top-places.md finalized (Top Picks + Dining Strategy)
✅ overview.md checklist fully checked `[x]`

### Key Workflow Steps
0. **Initialize**: Create overview.md → Use web_search for candidates
1. **Discover**: Add to candidates.md table (focus on top 3-5 first)
2. **Research**: Add detailed evidence to notes.md (4+ sources)
3. **Score**: Apply 50-point rubric, document in notes.md
4. **Triage**: Reject <30 scores, document in excluded.md
5. **Finalize**: Update top-places.md with Top Picks (35+) and Backups (30-34)
6. **Update**: Sync PROGRESS.md and README.md when complete

### Common Commands
```bash
# Check for inbox items
grep -E "\| inbox \||status:?\s*inbox" candidates.md | wc -l

# Check for pending exclusions
grep -E "^#.*待決定|^#.*[Uu]ndecided" excluded.md | wc -l

# Check for incomplete overview tasks
grep "\[ \]" overview.md | wc -l
```
