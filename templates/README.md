# Food Research Documentation Templates

This directory contains standardized templates for documenting food research across all cities in the trip planning project.

## Overview

Each city's food research follows a consistent 6-file structure designed around the **Progressive Disclosure Principle** - revealing information gradually from quick answers to deep evidence.

## Required Files (Per City)

Each city directory under `gourmet/YYYY-MM-DD-city/` must contain these 6 files:

### 1. overview.md (5-minute read)
**Purpose**: Quick orientation - context, strategy, and progress

**Use when**: Starting research for a city, understanding the food landscape

**Key sections**:
- Travel dates and accommodation
- City-specific food highlights
- Research strategy and priorities
- Progress checklist
- Important notes (hours, holidays, transport)

[📄 Template](overview.md)

---

### 2. candidates.md (5-10 minute scan)
**Purpose**: Summary table of all candidates with scores and status

**Use when**: Quick scanning, checking research coverage, prioritizing next steps

**Structure**: Single table with required fields:
- name, category, area, type
- google_maps_url (required format)
- status (inbox | researching | shortlisted | rejected | top)
- sources (brief)
- notes (Traditional Chinese, one-line summary)

**Important**: Table headers must be in English; content can be Traditional Chinese

[📄 Template](candidates.md)

---

### 3. notes.md (30+ minute deep dive)
**Purpose**: Detailed evidence, source citations, scoring rationale

**Use when**: Deep research, justifying scores, validating recommendations

**Per-place sections include**:
- Official website
- Google Maps rating (with URL)
- Tripadvisor rating
- Other review platforms
- Food guide sources
- Reddit sentiment summary
- Recurring pros/cons
- Practical info (reservation, hours, queue)
- **50-point score breakdown** with justification

[📄 Template](notes.md)

---

### 4. top-places.md (10-minute read)
**Purpose**: Final recommendations and actionable dining strategy

**Use when**: Planning actual meals, making reservations, deciding what to eat

**Structure**:
- **Top Picks** (35+ points) - organized by category
- **Backups** (30-34 points) - alternatives
- **Dining Strategy** - time planning, reservations, budget, geography
- **To-Do List** - pre-trip and during-trip tasks

**Important**: All entries must have working Google Maps links

[📄 Template](top-places.md)

---

### 5. inbox.md (exploratory, working notes)
**Purpose**: Fast capture of candidates during discovery phase

**Use when**: Initial web searches, collecting recommendations, brainstorming

**Structure**: Categorized lists with quick facts:
- 傳統餐廳 (Traditional Restaurants)
- 現代/創新餐廳 (Modern/Creative)
- 咖啡館 (Cafes)
- 甜點/冰淇淋 (Desserts/Gelato)
- 快速補給 (Quick Food)

**Workflow**: Capture here → Move to candidates.md → Research in notes.md

[📄 Template](inbox.md)

---

### 6. excluded.md (5-minute read)
**Purpose**: Audit trail of rejected places with reasons

**Use when**: Understanding why something wasn't recommended, avoiding re-research

**Categories**:
- **Soft Exclusion** (score < 30/50)
- **Hard Exclusion** (severe quality/safety issues)
- **Not Researched Further** (lower priority, sufficient alternatives)
- **Permanently Closed** (confirmed closures)

**Important**: Don't delete from candidates.md; mark as `rejected` and document here

[📄 Template](excluded.md)

---

## Information Flow

```
inbox.md (raw capture)
    ↓
candidates.md (structured table)
    ↓
notes.md (detailed research)
    ↓
top-places.md OR excluded.md (final decision)
    ↑
overview.md (context & progress tracking)
```

---

## Scoring System (50 Points Total)

Every researched place must have a score breakdown in notes.md:

- **Taste / Quality** (0-10): Food quality, authenticity, execution
- **Value** (0-10): Price vs quality, portion size
- **Convenience** (0-10): Location, ease of reservation/access, opening hours
- **Consistency** (0-10): Reliability across reviews, time, visits
- **Risk** (0-10, where 10 = low risk): Likelihood of disappointment, queue uncertainty, service issues

### Score Interpretation
- **40+**: Excellent, highly recommended (Top Pick)
- **35-39**: Very good, solid choice (Top Pick)
- **30-34**: Good, acceptable (Backup)
- **< 30**: Consider exclusion (document in excluded.md)

---

## Research Requirements

### Minimum Sources (4+ per place)
1. Google Maps (rating + review count)
2. Tripadvisor or similar aggregator
3. Reddit (sentiment from multiple threads)
4. Food/travel guide (Michelin, TimeOut, local blogs)

### Google Maps Link Requirements
✅ **Acceptable formats**:
- Direct links: `https://maps.app.goo.gl/...`
- Search API: `https://www.google.com/maps/search/?api=1&query=[Place+Name+City]`

❌ **Not acceptable**:
- Placeholder text like `[查看地圖]` or `[View Map]`
- Unverified links

---

## Research Workflow

### Initialize City Research
1. Create overview.md with travel info and city food highlights
2. Use web_search to gather initial candidates
3. Batch similar searches (restaurants, cafes, desserts)

### Discovery (candidates.md + inbox.md)
- Fast capture in inbox.md or directly in candidates.md table
- Focus on 3-5 top candidates first
- Status: `inbox`

### Evidence Collection (notes.md)
- Add detailed evidence section per place
- Minimum 4 sources required
- Update candidates.md with status: `researching` → `shortlisted`

### Scoring (notes.md)
- Apply 50-point rubric with justification
- Record practical info (reservation, hours, queue)
- Update candidates.md with score

### Triage (excluded.md)
- Score < 30: Document in excluded.md
- Severe issues: Hard exclusion with reasons
- Update candidates.md status to `rejected`

### Finalize (top-places.md)
- Top Picks: 35+ points
- Backups: 30-34 points
- Add dining strategy and to-do list
- Update candidates.md status to `top`

### Update Progress
- Complete overview.md checklist
- Update PROGRESS.md and README.md
- Verify completion criteria met

---

## Completion Criteria

A city is marked "✅ 已完成" when ALL of:
1. ✅ No `status: inbox` in candidates.md
2. ✅ No pending decisions in excluded.md
3. ✅ top-places.md finalized (Top Picks, Backups, Dining Strategy, To-Do)
4. ✅ overview.md checklist fully checked `[x]`

---

## Using the Templates

### For a New City

1. **Copy all 6 templates** to `gourmet/YYYY-MM-DD-cityname/`
2. **Start with overview.md**: Fill in travel info, food highlights
3. **Use inbox.md or candidates.md**: Capture initial candidates
4. **Research systematically**: Follow Steps 1-6 above
5. **Track progress**: Update overview.md checklist regularly

### Directory Naming Convention
Format: `YYYY-MM-DD-cityname/`
Example: `2026-02-11-vienna/`

The date represents the arrival date in the city.

---

## Language Guidelines

- **AGENTS.md & PROGRESS.md**: English only
- **All other documentation**: Primarily Traditional Chinese (Taiwan)
- **Structured fields**: English (table headers, status values, field names)
- **Free text content**: Traditional Chinese (notes, descriptions, rationale)

---

## Quality Standards

### Core Principles
✅ Prefer fewer, higher-confidence picks
✅ Cross-reference multiple sources (never rely on just one)
✅ Preserve traceability at all times
✅ Document uncertainty explicitly

### Common Pitfalls to Avoid
❌ Don't research everything at once (focus on top 3-5 first)
❌ Don't skip overview.md (context is crucial)
❌ Don't delete entries from candidates.md silently
❌ Don't rely on single sources
❌ Don't forget practical constraints (reservations, closed days)
❌ Don't over-optimize scores (realistic ranges are good)

---

## Progressive Disclosure Principle

The 6-file structure implements progressive disclosure:

**Level 1** (Quick): README.md → top-places.md (10 min)
**Level 2** (Scan): candidates.md table (5-10 min)
**Level 3** (Context): overview.md (5 min)
**Level 4** (Evidence): notes.md (30+ min)
**Level 5** (Audit): excluded.md (5 min)
**Level 6** (Working): inbox.md (exploratory)

Each level provides increasing detail while maintaining clear paths to deeper information when needed.

---

## References

- **Full Guidelines**: See `/AGENTS.md` for complete workflow and requirements
- **Progress Tracking**: See `/PROGRESS.md` for completion standards and verification
- **Project Overview**: See `/README.md` for trip context and city summaries

---

## Questions or Issues?

If templates need updates based on lessons learned:
1. Update templates in `gourmet/templates/`
2. Document changes in AGENTS.md "Process Improvements" section
3. Ensure consistency across existing city directories
