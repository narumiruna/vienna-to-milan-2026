# Instructions for Agents

> **New to this project?** Start with the [Quick Reference](#quick-reference-) below for essential information, then explore detailed sections as needed.

## Table of Contents

### Essential (Start Here)
- [Quick Reference](#quick-reference-) ⭐ **START HERE**
- [Main Purpose (Immutable)](#main-purpose-immutable)
- [Agent Mission](#agent-mission)
- [Getting Started](#getting-started) 🚀

### Core Documentation
- [Project Scope](#project-scope)
- [Required Repository Structure](#required-repository-structure-per-city)
- [Documentation Templates](#documentation-templates)
- [Workflow (Must Follow)](#workflow-must-follow)

### Guidelines & Standards
- [Progressive Disclosure Principle](#progressive-disclosure-principle)
- [Quality Bar](#quality-bar)
- [Research Completion Standard](#research-completion-standard)

### Reference & Troubleshooting
- [Working with Agents](#working-with-agents-ensuring-task-completion)
- [Documentation & Naming Rules](#documentation--naming-rules)

---

## Quick Reference ⭐

**Read this first.** Everything you need for 80% of tasks.

### Mission
Build **evidence-based food recommendations** (restaurants, cafes, desserts) for a 2026-02-10 to 2026-02-28 trip across 5 cities in Austria and Italy.

### Key Constraints (IMMUTABLE)
- ✈️ Flights, trains, and hotels are **already booked** - do NOT suggest changes
- 🗓️ Cities and dates are **fixed** - see [Main Purpose](#main-purpose-immutable) for full itinerary
- 🍽️ Focus **only on food** - not accommodations, transport, or attractions
- 🚫 **No alcoholic beverages** - exclude wine bars, cocktail bars, and alcohol-focused venues

### File Structure (Per City)
```
gourmet/YYYY-MM-DD-city/
├── overview.md       (5min)  - Context & strategy → START HERE for new city
├── top-places.md     (10min) - Final picks → For users planning their trip
├── candidates.md     (5min)  - Summary table → Quick scan of all options
├── notes.md          (30min) - Evidence → Full research details
├── inbox.md          (work)  - Raw notes → Temporary workspace
└── excluded.md       (5min)  - Rejected → Audit trail
```

### Research Workflow
- **Initialize**: Create overview.md → Use web_search for 20+ candidates
- **Discover**: Add top 3-5 to candidates.md table
- **Research**: Document evidence in notes.md (4+ sources minimum)
- **Score**: Apply 50-point rubric (Taste + Value + Convenience + Consistency + Risk)
- **Decide**: Promote (35+) or exclude (<30) based on thresholds
- **Triage**: Mark rejected, document reasons in excluded.md
- **Finalize**: Update top-places.md with Top Picks and Dining Strategy
- **Verify**: Run completion checks, update PROGRESS.md

### Scoring System (50 points)
- **40+**: Excellent, highly recommended (Top Pick)
- **35-39**: Very good, solid choice (Top Pick)
- **30-34**: Good, acceptable (Backup)
- **<30**: Consider exclusion

Components: Taste/Quality (10) + Value (10) + Convenience (10) + Consistency (10) + Risk (10)

### Required Sources (Minimum 4)
1. Google Maps (rating + review count)
2. Tripadvisor or similar aggregator
3. Reddit (local sentiment)
4. Food/travel guide (Michelin, TimeOut, blogs)

### Completion Criteria (All Required)
✅ No `status: inbox` in candidates.md  
✅ No pending decisions in excluded.md  
✅ top-places.md has: Top Picks + Backups + Dining Strategy + To-Do  
✅ overview.md checklist fully checked `[x]`  

### When You Need More Detail
- **Workflow details** → See [Workflow](#workflow-must-follow) section, or [references/workflow-detailed.md](references/workflow-detailed.md) for complete step-by-step instructions
- **Scoring guidance** → See [Scoring — Standard Rubric](#scoring--standard-rubric)
- **Quality standards** → See [Quality Bar](#quality-bar--standards), or [references/quality-standards.md](references/quality-standards.md) for audit framework and checklists
- **Template usage** → See [Documentation Templates](#documentation-templates)
- **Troubleshooting** → See [Working with Agents](#working-with-agents-ensuring-task-completion)
- **Detailed references** → See [references/](references/) directory for comprehensive guides on workflow, quality standards, and best practices

---

## Getting Started 🚀

**First time working on a city? Follow this minimal path:**

### Step 1: Understand Context (5 minutes)
1. Read [Main Purpose](#main-purpose-immutable) - Know what's fixed
2. Check [Project Scope](#project-scope) - Know what's in/out of scope
3. Review city dates and hotel in PROGRESS.md

### Step 2: Initialize City (30 minutes)
1. Create `overview.md` first (see [Initialize City Research](#initialize-city-research))
2. Run 3-4 web searches to collect 20+ candidates
3. Add candidates to `inbox.md` (fast capture)

### Step 3: Research Top Priorities (2-3 hours)
1. Pick top 3-5 candidates from inbox
2. Add to `candidates.md` table with `status: inbox`
3. Research each thoroughly (see [Evidence Collection](#evidence-collection--per-place))
4. Score using 50-point rubric (see [Scoring](#scoring--standard-rubric))
5. Promote to `top-places.md` if score ≥35

### Step 4: Report Progress
- Use `report_progress` tool after completing each city section
- Update PROGRESS.md status when city research complete

### What's Next?
Continue researching additional candidates or move to [Workflow](#workflow-must-follow) for complete details.

---

## Main Purpose (Immutable)

- The main purpose of this project is to plan a trip from 2026-02-10 to 2026-02-28, especially focusing on food.
- All flights, trains, and accommodations have already been booked and are FINAL.

Agents MUST NOT:
- Suggest changing flights, trains, accommodations, or travel dates
- Suggest alternative hotels or rebooking transport
- Reorder cities or modify the travel route
- Recommend alcoholic beverages or alcohol-focused venues (wine bars, cocktail bars, etc.)

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

**Exclusions:**
- 🚫 No alcoholic beverages (wine, beer, cocktails)
- 🚫 No alcohol-focused venues (wine bars, cocktail bars, breweries)

**Quality Standards - All recommendations must be:**
- ✅ **Traceable**: Sources linked with URLs
- ✅ **Comparable**: Shared 50-point scoring rubric
- ✅ **Auditable**: Decisions and exclusions documented
- ✅ **Actionable**: Clear top picks (35+) and backups (30-34)

---

## Project Scope

### In Scope

**Primary Objective**: Build evidence-based food recommendations for a trip from 2026-02-10 to 2026-02-28.

**Target Cities**:
- Vienna (2026-02-11 to 2026-02-13)
- Rome (2026-02-13 to 2026-02-19)
- Florence (2026-02-19 to 2026-02-22)
- Venice (2026-02-22 to 2026-02-25)
- Milan (2026-02-25 to 2026-02-27)

**Categories Covered**:
- Restaurants (all cuisine types including fine dining, traditional, casual)
- Cafes (coffee, tea, light meals)
- Dessert shops (gelato, pastries, tiramisu, traditional sweets)

**Research Deliverables**:
- Scored candidate list with evidence (candidates.md + notes.md)
- Top picks and backup recommendations (top-places.md)
- Practical constraints (reservations, hours, closures, queues)
- Exclusion rationale for rejected candidates (excluded.md)
- Dining strategy per city (timing, budget, logistics)

### Out of Scope

**Not Researched**:
- Accommodations (already booked, see Main Purpose)
- Transportation between cities (already booked)
- Non-food activities or tourist attractions
- Shopping (unless food-related like markets)
- Nightlife (bars, clubs) unless food-focused
- **Alcoholic beverages and alcohol-focused venues** (wine bars, cocktail bars, breweries, wine tastings)
- Cities outside the five target cities

**Fixed Constraints** (not modifiable by research):
- Travel dates: 2026-02-10 to 2026-02-28
- Flight itinerary (TPE→VIE, VIE→FCO, MXP→TPE)
- Train itinerary (Roma→Firenze, Firenze→Venezia, Venezia→Milano)
- Hotel locations (see Main Purpose for details)
- No alcoholic beverages preference

**Scope Management**:
- Research must stay focused on food recommendations
- Avoid mission creep into general travel planning
- When uncertain if something is in scope, refer back to Primary Objective

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

## Documentation Templates

**Location**: `/templates/` directory at repository root

The project provides standardized templates for all 6 required documentation files to ensure consistency across cities.

### Available Templates

1. **overview.md** - Travel info, food highlights, research strategy, progress tracking
2. **candidates.md** - Structured table with required fields (name, category, area, type, google_maps_url, status, sources, notes)
3. **notes.md** - Detailed evidence sections with 50-point scoring rubric
4. **top-places.md** - Final recommendations (Top Picks 35+, Backups 30-34), dining strategy, to-do lists
5. **inbox.md** - Quick capture workspace for initial discovery
6. **excluded.md** - Audit trail of rejected places with documented reasons

### Usage

When starting research for a new city:

```bash
# Copy all templates to the new city directory
cp templates/*.md gourmet/YYYY-MM-DD-cityname/
```

Then customize each file following the workflow steps (0-6) and guidelines in this document.

### Template Features

- **Pre-structured sections**: All required sections with placeholder text
- **Field requirements**: Clear specifications for required and optional fields
- **Bilingual support**: English structured fields, Traditional Chinese content areas
- **Scoring rubric**: Built-in 50-point system (Taste/Quality + Value + Convenience + Consistency + Risk)
- **Research standards**: Minimum 4 sources requirement, Google Maps link formats, practical information checklist

### Complete Documentation

For detailed usage instructions, workflow guidance, and examples, see:
- **templates/README.md** - Comprehensive usage guide (295 lines)
  - Per-file purposes and structures
  - Research workflow (Steps 0-6)
  - Completion criteria
  - Quality standards and common pitfalls

---

## Progressive Disclosure Principle

**Core Idea**: Reveal information gradually - show only what's needed at each stage, with clear paths to deeper detail.

### The Problem We're Solving

Users have different needs at different times:
- 🏃 **Quick decisions**: "Where should I eat tonight?" → Need: top-places.md (1 min)
- 🔍 **Research validation**: "Why this restaurant?" → Need: notes.md evidence (5 min)
- 📋 **Overview scan**: "What are all my options?" → Need: candidates.md table (2 min)
- ❓ **Audit trail**: "Why was X excluded?" → Need: excluded.md (30 sec)

**Progressive disclosure prevents information overload while maintaining traceability.**

### Our 6-File Layered Architecture

Each file = a distinct information layer. Users enter at the layer they need:

| File | Purpose | Read Time | When to Use |
|------|---------|-----------|-------------|
| **overview.md** | Context & strategy | 5 min | Starting research on new city |
| **top-places.md** | Final recommendations | 10 min | Planning actual trip, making reservations |
| **candidates.md** | Summary table | 5 min | Quick scan of all options |
| **notes.md** | Full evidence | 30+ min | Validating scores, deep research |
| **inbox.md** | Working notes | N/A | During initial discovery phase |
| **excluded.md** | Rejection reasons | 5 min | Understanding what was filtered out |

**Information flow**: overview → top-places → candidates → notes → excluded

### Key Rules for Agents

**✅ DO:**
- Start with conclusions, then provide evidence (inverted pyramid style)
- Use summaries in higher layers (top-places.md, candidates.md)
- Keep full details in lower layers (notes.md)
- Link between layers: "See notes.md for full evidence"
- Maintain traceability: every decision documented somewhere

**❌ DON'T:**
- Duplicate information across files
- Mix abstraction levels (summaries with detailed evidence)
- Hide critical information too deep
- Create files beyond the required 6

### Examples

**Good** - Progressive disclosure:
```markdown
## top-places.md
**Trattoria Da Enzo** (38/50) - Authentic Roman cuisine, excellent cacio e pepe
- Location: Trastevere
- Reservation: Required, book 1 week ahead
- See notes.md for detailed scoring rationale

## notes.md - Trattoria Da Enzo
[Full research: sources, scoring breakdown, pros/cons]
```

**Bad** - Information overload:
```markdown
## top-places.md
**Trattoria Da Enzo** (38/50)
[200 lines of reviews, source citations, detailed scoring, all pros/cons]
```

### Further Reading

For deeper understanding of progressive disclosure in documentation design:
- Anthropic Skills Guide: Three-level loading system (metadata → body → resources)
- See this document's structure as an example: Quick Reference → detailed sections

---

## Workflow (Must Follow)

**Complete research process from start to finish.** Follow these steps in order for each city.

> **💡 Quick Start**: Most critical steps are Initialize, Evidence, Scoring, and Finalize. Discovery, Decision, Triage, and Verify are supporting processes.

### Overview of Steps

| Step | Purpose | Time | Critical? |
|------|---------|------|-----------|
| Initialize | Set up city research | 30 min | ⭐ Yes |
| Discovery | Collect candidates | 20 min | Medium |
| Evidence | Research each place | 15-20 min/place | ⭐ Yes |
| Scoring | Apply 50-point rubric | 10 min/place | ⭐ Yes |
| Decision | Apply thresholds | 5 min/place | Medium |
| Triage | Document exclusions | 5 min/place | Medium |
| Finalize | Create top-places.md | 30 min | ⭐ Yes |
| Verify | Completion checks | 10 min | ⭐ Yes |

**Iteration pattern**: After Initialize, loop through Discovery-Triage for each candidate. Complete with Finalize and Verify.

---

### Initialize City Research

**What**: Set up city research foundation with overview.md and initial candidate collection.

**Key actions**:
1. Create overview.md with travel info, food highlights, strategy, progress checklist
2. Run 3-4 web searches to collect 20+ candidates  
3. Record findings in inbox.md (fast capture)

**Time**: 30 minutes

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#initialize-city-research)

---

### Discovery — Candidate Collection

**What**: Collect and organize candidate places into structured format.

**Key actions**:
- Transfer top 3-5 candidates from inbox.md to candidates.md table
- Set `status: inbox` for each new candidate
- Include: name, category, area, type, google_maps_url, sources, brief notes

**Required fields in candidates.md table**: name | category | area | type | google_maps_url | status | sources | notes

**Time**: 20 minutes

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#discovery--candidate-collection)

---

### Evidence Collection — Per Place

**What**: Research each candidate thoroughly with multiple sources.

**Key actions**:
- Add detailed evidence section to notes.md for each place
- Collect from 4+ sources: Google Maps, Tripadvisor, Reddit, Food Guide
- Document: ratings, pros/cons, practical info (reservation, hours, queues)
- Handle conflicts and mark uncertainty explicitly

**Template**: See workflow-detailed.md for evidence section template

**Time**: 15-20 minutes per place

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#evidence-collection--per-place)

---

### Scoring — Standard Rubric

**What**: Apply 50-point scoring rubric to each researched place.

**Components** (0-10 each):
- **Taste/Quality**: Food quality, authenticity, execution
- **Value**: Price vs quality, portion size
- **Convenience**: Location, ease of reservation/access
- **Consistency**: Reliability across reviews
- **Risk** (10=low): Likelihood of disappointment

**Score interpretation**:
- **40+**: Excellent → Top Pick
- **35-39**: Very good → Top Pick
- **30-34**: Good → Backup
- **<30**: Consider exclusion

**Time**: 10 minutes per place

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#scoring--standard-rubric)

---

### Decision Rules

**What**: Apply promotion/exclusion thresholds systematically.

**Promotion thresholds**:
- Score ≥35 → Top Pick (promote to top-places.md)
- Score 30-34 → Backup (promote to top-places.md)

**Exclusion triggers**:
- Score <25 → Automatic exclusion
- Hard triggers: Tourist trap evidence, hygiene concerns, severe service issues, practical impossibility

**Time**: 5 minutes per place

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#decision-rules)

---

### Triage — Exclusion with Reasons

**What**: Mark rejected candidates and document reasons.

**Key actions**:
- Update candidates.md: `status: rejected`
- Add entry to excluded.md with clear reason
- Never delete entries - always document why excluded

**Time**: 5 minutes per rejected place

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#triage--exclusion-with-reasons)

---

### Final Output — Top Picks

**What**: Create finalized top-places.md with recommendations and strategy.

**Required sections**:
1. **Top Picks** (score 35+): Name, score, area, type, google_maps_url, justification, constraints
2. **Backups** (score 30-34): Same format as Top Picks
3. **Dining Strategy**: Time planning, reservation strategy, budget, transportation
4. **To-Do**: Confirm closures, make reservations, plan schedule

**Organization**: List in descending score order within each section

**Time**: 30 minutes

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#final-output--top-picks)

---

### Post-Research Updates — Documentation Maintenance

**What**: Verify completion and update project-wide documentation.

**Verification steps**:
1. Run completion verification commands (see below)
2. Update PROGRESS.md status (⏳ → 📝 → 🔄 → ✅)
3. Sync README.md with PROGRESS.md
4. Clean up inbox.md
5. Update AGENTS.md if workflow improved

**Completion verification commands**:
```bash
# All should return 0 except top-places sections (should return 4)
grep -E "\| inbox \||status:?\s*inbox" gourmet/[city]/candidates.md | wc -l
grep -E "^#.*待決定|^#.*[Uu]ndecided|TODO|PENDING" gourmet/[city]/excluded.md | wc -l
grep -E "^## (Top Picks|Backups|Dining Strategy|To-Do)" gourmet/[city]/top-places.md | wc -l  # Should = 4
grep "\[ \]" gourmet/[city]/overview.md | wc -l
```

**Time**: 10 minutes

**📖 Full details**: See [references/workflow-detailed.md](references/workflow-detailed.md#post-research-updates--documentation-maintenance)

---

## Quality Bar & Standards

**Core principles**: Fewer, high-confidence picks | Multiple sources | Full traceability

**Research standards**:
- Minimum 4+ sources per place (Google Maps, Tripadvisor, Reddit, Food Guide)
- Every score must be justifiable with documented evidence
- Document uncertainty explicitly (use labels: unknown, conflicting, unverified, seasonal, outdated)

**📖 Complete quality standards**: See [references/quality-standards.md](references/quality-standards.md) for:
- Audit framework and preservation rules
- Quality assurance checklist
- Process improvements and lessons learned
- Common pitfalls to avoid
- Research questions checklist

---

## Documentation & Naming Rules

- `AGENTS.md`, `PROGRESS.md` and `references/*.md` MUST be written in English.
- Other documents in this repo MUST be primarily in Traditional Chinese (Taiwan).
- Use English for structured fields and keys (table headers, status values, etc.)
- Dates must follow ISO format (YYYY-MM-DD)
- Unknown information must be labeled as `unknown`
- City directory names MUST follow: `YYYY-MM-DD-city/` (e.g., `2026-02-11-vienna/`)

---

## Further Reading

**End of AGENTS.md** - For detailed guides, see the `references/` directory:
- **[references/README.md](references/README.md)** - Navigation guide and progressive disclosure explanation
- **[references/workflow-detailed.md](references/workflow-detailed.md)** - Complete step-by-step workflow instructions
- **[references/quality-standards.md](references/quality-standards.md)** - Quality bar, audit framework, and best practices
