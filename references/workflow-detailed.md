# Detailed Workflow Guide

**Purpose**: Complete step-by-step instructions for each workflow stage. Read this when you need full details beyond the overview in AGENTS.md.

**When to use**: When executing research tasks and you need specific guidance on how to complete each step.

---

## Table of Contents

1. [Step 0: Initialize City Research](#step-0-initialize-city-research)
2. [Step 1: Discovery — Candidate Collection](#step-1-discovery--candidate-collection)
3. [Step 2: Evidence Collection — Per Place](#step-2-evidence-collection--per-place)
4. [Step 3: Scoring — Standard Rubric](#step-3-scoring--standard-rubric)
5. [Step 4: Decision Rules](#step-4-decision-rules)
6. [Step 5: Triage — Exclusion with Reasons](#step-5-triage--exclusion-with-reasons)
7. [Step 6: Final Output — Top Picks](#step-6-final-output--top-picks)
8. [Step 7: Post-Research Updates — Documentation Maintenance](#step-7-post-research-updates--documentation-maintenance)

---

## Step 0: Initialize City Research

When starting research for a new city:

### Required Actions

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

## Step 1: Discovery — Candidate Collection

### Overview

- Search broadly for food, coffee, and dessert places in the city.
- Record raw findings in:
  - inbox.md (unstructured, fast capture with quick notes)
  - and/or candidates.md (structured table)

### inbox.md Structure Recommendation

```
## Category (e.g., 傳統羅馬餐廳)
1. **Place Name**
   - 位置：area
   - 特色：key dishes/unique features
   - 注意：constraints
   - 來源：source type
```

### inbox.md Lifecycle

inbox.md is the initial exploration workspace with a clear lifecycle:

1. **Exploration Phase** (Research Start → Collection Complete)
   - Quickly record web_search results
   - Freely organize by categories (Traditional restaurants, Pizza, Desserts, etc.)
   - Include brief notes (location, features, constraints, sources)
   - No need for immediate structuring

2. **Transfer Phase** (Collection Complete → Research In Progress)
   - Transfer priority candidates (top 3-5) to candidates.md
   - Set `status: inbox` in candidates.md
   - Keep other candidates in inbox.md as "pending evaluation list"

3. **Cleanup Phase** (Research Complete → Before Marking Complete)
   - Confirm all relevant candidates transferred to:
     - candidates.md (researched or pending research)
     - excluded.md (explicitly excluded)
   - Option A: Clear inbox.md, add note at top: "已轉移至 candidates.md"
   - Option B: Keep inbox.md as historical record, add note at top: "歷史記錄（已轉移）"
   - **NOT acceptable**: Leaving unprocessed candidates in inbox.md

### inbox.md vs candidates.md

| Feature | inbox.md | candidates.md |
|---------|----------|---------------|
| Format | Free-form notes | Structured table |
| Purpose | Initial exploration & collection | Candidate summary & status tracking |
| Timing | Research beginning | Throughout research |
| State | Temporary | Permanent |
| When complete | Clear or mark as historical | Keep all records |

### Required Fields in candidates.md Table

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

### Google Maps Link Requirement

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

### Prioritization

Focus on 3-5 top candidates first, then expand. Don't try to research everything at once.

### ⚠️ CRITICAL: Preserving candidates.md Table Entries

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

## Step 2: Evidence Collection — Per Place

For each candidate promoted to research:
- Add a detailed evidence section in `notes.md` (keep it skimmable; link sources).
- Update the candidates.md table row with brief summary in notes column.
- Summarize evidence from multiple independent sources.

### Efficient Research Pattern

1. Use web_search with specific queries: "[Restaurant Name] [City] reviews rating reservation Reddit"
2. One search often provides Google Maps rating, Tripadvisor reviews, and Reddit sentiment together
3. Extract key information systematically
4. Document full evidence in notes.md, update candidates.md table with status and brief summary

### Required Source Types

- Google Maps (rating, review count, recurring pros/cons)
- Tripadvisor or similar aggregator (rating, review count)
- Reddit (threads/comments; summarize patterns)
- One or more reputable food or travel guides (Michelin, TimeOut, local blogs)

### Optional Sources

- PTT / Dcard / Chinese-language travel blogs (cite clearly if used)
- Social media mentions (TikTok, Instagram) if aggregated

### Rules

- Do NOT fabricate facts or reviews
- Clearly distinguish:
  - What sources report (use bullet points with source citations)
  - Your synthesis or inference (clearly marked)
- Include actual URLs in sources section
- Note if information is unavailable (use `unknown`)

### Evidence Section Template (for notes.md)

```markdown
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

### Conflict Handling

**When sources disagree**, follow this resolution process:

1. **Document the conflict explicitly**:
   ```markdown
   **Conflict noted**:
   - Source A (Google Maps): Claims 4.5/5
   - Source B (Tripadvisor): Claims 3.5/5
   - Source C (Reddit): Generally positive mentions
   ```

2. **Resolution strategy** (in order of preference):
   - **Recency**: Prefer more recent information (check review dates)
   - **Majority consensus**: Use most common finding across sources
   - **Detail level**: Prefer source with more specific information
   - **Review scale**: Weight by review count/authority (1000+ reviews > 50 reviews)

3. **When unresolvable**:
   - Mark as `conflicting` in notes.md
   - Document both sides
   - Note in scoring rationale that evidence is conflicting
   - Consider slightly reducing Consistency score (by 1-2 points)

**Common conflict types**:
- **Hours of operation**: Check official website first, then Google Maps
- **Reservation requirements**: Call restaurant if critical; otherwise document uncertainty
- **Price ranges**: Use most recent source; note if prices may have changed
- **Service quality**: Look for trends over time (recent 6-month pattern vs older reviews)

### Uncertainty Documentation

**Mark information as uncertain when**:
- Only one source provides the information
- Sources conflict without clear resolution
- Information is outdated (>1 year old for restaurants)
- Seasonal variation is possible

**Uncertainty labels to use**:
- `unknown`: No reliable source found
- `conflicting`: Sources disagree, no clear resolution (see Conflict Handling above)
- `unverified`: Single source only, not confirmed elsewhere
- `seasonal`: May vary by season (note which season applies)
- `outdated`: Based on information >1 year old (note the date)

**Example usage**:
```markdown
**Practical**:
- reservation requirement: required (per Tripadvisor, unverified on official site)
- best visiting time: conflicting (some sources say lunch is best, others prefer dinner)
- closed days: unknown (no clear information found across sources)
- queue: 30-60 min (based on 2024 reviews, possibly outdated)
```

**Impact on scoring**:
- High uncertainty should be noted in Risk score rationale
- Conflicting information about quality → reduce Consistency score
- Unknown practical information → may reduce Convenience score

---

## Step 3: Scoring — Standard Rubric

Each researched place MUST include a 50-point total score:

- Taste / Quality (0–10): Food quality, authenticity, execution
- Value (0–10): Price vs quality, portion size
- Convenience (0–10): Location, ease of reservation/access, opening hours
- Consistency (0–10): Reliability across reviews, time, visits
- Risk (0–10; 10 = low risk): Likelihood of disappointment, queue uncertainty, service issues

### Scoring Guidelines

- 40+ = excellent, highly recommended
- 35-39 = very good, solid choice
- 30-34 = good, acceptable backup
- <30 = consider exclusion

### Also Record

- reservation requirement (required | recommended | optional | none | unknown)
- best visiting time (specific times or "off-peak" etc.)
- closed days (especially Sunday/Monday)
- queue expectations (if no reservation)

### Detailed Scoring Guidance Per Dimension

**Taste/Quality (0-10)**:
- **9-10**: Exceptional. Michelin-starred or equivalent recognition, consistently outstanding
- **7-8**: Excellent. Strong reviews, specific dishes highly praised
- **5-6**: Good. Generally positive, solid execution
- **3-4**: Acceptable. Mixed reviews, some quality concerns
- **0-2**: Poor. Multiple quality complaints

**Value (0-10)**:
- **9-10**: Outstanding value. High quality at low/moderate price
- **7-8**: Good value. Fair pricing for quality delivered
- **5-6**: Acceptable. Slightly expensive but justified
- **3-4**: Poor value. Overpriced for quality
- **0-2**: Very poor value. Significantly overpriced

**Convenience (0-10)**:
- **9-10**: Highly convenient. Central location, walk-in friendly, flexible hours
- **7-8**: Convenient. Accessible, easy reservation, reasonable hours
- **5-6**: Moderate. Requires some planning, standard hours
- **3-4**: Inconvenient. Difficult access, complex reservation
- **0-2**: Very inconvenient. Remote location, very limited hours

**Consistency (0-10)**:
- **9-10**: Highly consistent. Stable ratings, minimal complaints, long-established
- **7-8**: Consistent. Reliable quality, few negative reviews
- **5-6**: Moderately consistent. Some variation, generally reliable
- **3-4**: Inconsistent. Mixed experiences, hit-or-miss
- **0-2**: Unreliable. Frequent complaints, significant variation

**Risk (0-10, where 10 = low risk)**:
- **9-10**: Very low risk. Reliable, predictable, reservation possible
- **7-8**: Low risk. Generally safe choice, minor uncertainties
- **5-6**: Moderate risk. Some factors could lead to disappointment
- **3-4**: Higher risk. Significant potential issues
- **0-2**: High risk. Multiple red flags or major concerns

### Scoring Consistency Rules

- Compare within category (restaurants to restaurants, cafes to cafes)
- Don't penalize casual places for not being fine dining
- Reserve 9-10 scores for truly exceptional experiences
- A score of 35-38 is very good; not everything needs to be 40+
- Document reasoning for every component score

---

## Step 4: Decision Rules

**This section defines clear thresholds and criteria for promoting or excluding candidates.**

### Promotion Thresholds

**Automatic promotion**:
- Score ≥35: Promote to Top Pick in top-places.md
- Score 30-34: Promote to Backup in top-places.md

**Requires justification** (document in notes.md):
- Score <30 but promoting anyway (explain why)
- Score ≥35 but NOT promoting (explain why - e.g., category oversaturation, geographic redundancy)

### Exclusion Thresholds

**Automatic exclusion** (mark as `status: rejected`, document in excluded.md):
- Score <25: Below quality standard
- Hard exclusion triggers (regardless of score):
  - Multi-source evidence of tourist trap (inflated prices, low quality, targets tourists)
  - Multiple hygiene or safety concerns across sources
  - Consistent severe service issues (rude staff, frequent errors)
  - Practical impossibility (always closed during trip, location truly inaccessible)

**Requires consideration** (borderline cases):
- Score 25-29: Marginal quality. Document decision either way.
- Score 30-34 with red flags: May exclude despite acceptable score if concerns are significant

### Decision Documentation

**Every decision must be documented**:

1. **Promoted to Top Pick/Backup**:
   - Total score with component breakdown in notes.md
   - Brief justification in top-places.md (one-line)
   - Update candidates.md: `status: top` or `status: shortlisted`

2. **Rejected/Excluded**:
   - Score (if calculated) in notes.md or brief note why not scored
   - Exclusion reason category in excluded.md
   - Supporting evidence (which sources, what they said)
   - Update candidates.md: `status: rejected`

3. **Deprioritized** (not researched):
   - Brief reason in excluded.md under "未進一步研究的候選"
   - Why not researched (e.g., "已有足夠同類推薦", "優先級較低", "地點較遠")
   - Keep in candidates.md: `status: rejected`

**Traceability principle**: Every decision must trace back to documented evidence or explicit human judgment.

---

## Step 5: Triage — Exclusion with Reasons

Apply the Decision Rules (Step 4) to each researched candidate.

- Do NOT delete entries silently.
- Mark excluded places with:
  - status: rejected
  - a documented reason

Record exclusions in:
- excluded.md (primary location for all exclusion reasons)
- Update candidates.md table with `status: rejected`

**Refer to Step 4 (Decision Rules) for**:
- Automatic exclusion thresholds (score <25, hard triggers)
- Borderline case handling (score 25-29)
- Documentation requirements

---

## Step 6: Final Output — Top Picks

Maintain top-places.md with:
- Top Picks (high-confidence, score 35+)
- Backups (good alternatives, score 30-34)
- Researching (in-progress candidates)

### Organization by Score

- List in descending score order within each section
- Clearly show total score for each place

### Each Entry MUST Include

- name
- type
- area
- total score (prominently displayed)
- google maps link
- one-line justification (why recommended)
- constraints (reservation, queues, closed days, price level)

### Google Maps Link Requirement

- Every place in top-places.md MUST have a valid, working Google Maps link
- See Step 1 for acceptable formats and how to obtain links
- **Consistency**: Use the same link format from candidates.md to maintain traceability

### Additional Sections to Include

**Dining Strategy**:
- Time planning (lunch/dinner hours, local customs)
- Reservation strategy (which places need booking, how far in advance)
- Budget allocation (price ranges per category)
- Transportation from hotel (how to reach different areas)

**To-Do**:
- Confirm closed days
- Make reservations (with timing)
- Plan daily dining schedule

---

## Step 7: Post-Research Updates — Documentation Maintenance

**After completing research for a city, MUST do the following**:

### 1. Verify Research Completion Standard

See PROGRESS.md for detailed criteria:
- ✅ All candidates triaged (no `status: inbox` remaining)
- ✅ No pending decisions in excluded.md
- ✅ top-places.md finalized with Top Picks and Dining Strategy
- ✅ overview.md checklist fully marked `[x]`
- ✅ inbox.md cleaned up

### 2. Run Verification Commands

```bash
# Should return nothing (no inbox entries)
grep -E "\| inbox \||status:?\s*inbox" gourmet/[city]/candidates.md | wc -l

# Should return nothing (no pending decisions)
grep -E "^#.*待決定|^#.*[Uu]ndecided|TODO|PENDING" gourmet/[city]/excluded.md | wc -l

# Should find all 4 required sections
grep -E "^## (Top Picks|Backups|Dining Strategy|To-Do)" gourmet/[city]/top-places.md | wc -l

# Should return nothing (no unchecked items)
grep "\[ \]" gourmet/[city]/overview.md | wc -l
```

**Expected results for completed city**:
- No inbox entries found ✓
- No pending decisions found ✓
- All 4 sections found in top-places.md (count = 4) ✓
- No unchecked items in overview.md ✓

### 3. Update Progress Tracking

- Update PROGRESS.md with current status (primary source of truth)
- Sync README.md progress table to match PROGRESS.md
- Use accurate status icon based on completion criteria:
  - ⏳ 未開始 → 📝 研究中 → 🔄 待完成 → ✅ 已完成
- Only use ✅ when ALL verification commands pass
- Update 重點推薦 count
- Add relevant notes about research completion

### 4. Update AGENTS.md if Workflow Improved

- If you discovered a more efficient research method, document it in "Process Improvements (Lessons Learned)"
- If you found common patterns or pitfalls, add them to relevant sections
- Keep the workflow documentation current with actual practices

### 5. Clean Up inbox.md

- Confirm all candidates transferred to candidates.md or excluded.md
- Choose one approach:
  - Option A: Clear inbox.md content, add note at top: "已轉移至 candidates.md (YYYY-MM-DD)"
  - Option B: Keep as historical record, add note at top: "歷史記錄（已轉移至 candidates.md, YYYY-MM-DD）"
- Mark this task complete in overview.md checklist

### Why This Matters

- PROGRESS.md serves as the project progress dashboard - it must reflect current reality
- README.md provides a quick overview that syncs with PROGRESS.md
- Verification commands provide objective completion criteria
- Completion standards ensure consistency across all cities
- AGENTS.md captures institutional knowledge - improvements benefit future research
- Consistent updates prevent confusion and duplicate work
