# Quality Standards and Best Practices

**Purpose**: Detailed quality bar, audit framework, and best practices for maintaining research quality.

**When to use**: When validating research quality, conducting reviews, or ensuring completeness before marking a city as done.

---

## Table of Contents

1. [Quality Bar](#quality-bar)
2. [Audit Framework](#audit-framework)
3. [Quality Assurance Checklist](#quality-assurance-checklist)
4. [Process Improvements](#process-improvements-lessons-learned)
5. [Common Pitfalls to Avoid](#common-pitfalls-to-avoid)
6. [Research Questions Checklist](#research-questions-checklist)

---

## Quality Bar

### Core Principles

- ✅ Prefer fewer, higher-confidence picks
- ✅ Avoid relying on a single platform
- ✅ Preserve traceability at all times

### Research Standards

- **Minimum 4+ sources per place**: Google Maps + Tripadvisor + Reddit + Food Guide
- **Every score must be justifiable**: Document evidence in notes.md
- **Document uncertainty**: If information conflicts or is unavailable, note it explicitly

---

## Audit Framework

**Audit trail requirements** - Every research action must leave a trace:

### 1. Candidate Addition

- Entry in candidates.md with `status: inbox`
- Timestamp captured in git commit

### 2. Research Conducted

- Evidence section created in notes.md
- Source URLs with descriptions
- Status updated to `researching` in candidates.md

### 3. Scoring

- Score breakdown with justification in notes.md
- Total score added to candidates.md
- All five components documented with evidence

### 4. Triage Decision

- Status updated to `shortlisted`, `top`, or `rejected`
- If rejected: entry in excluded.md with reason
- If promoted: entry in top-places.md

### 5. Changes After Initial Decision

- Document reason for change in notes.md
- Update all affected files (candidates.md, notes.md, top-places.md, excluded.md)
- Note reason in git commit message

### Preservation Rules

- ❌ NEVER delete candidates from candidates.md (see workflow-detailed.md Step 1 for details)
- ❌ NEVER remove evidence from notes.md
- ❌ NEVER hide exclusion reasons
- ✅ Mark as rejected and document reason instead
- ✅ Preserve historical scores if recalculated (note the change and reason)

---

## Quality Assurance Checklist

**Before marking a city as complete, verify:**

- [ ] All candidates have scores or exclusion reasons documented
- [ ] Every score has evidence justification in notes.md
- [ ] **All top picks (35+) have negative review research documented** with ⚠️ flags for serious issues
- [ ] All sources have working URLs (test links)
- [ ] No unsupported claims or fabricated data
- [ ] Conflicts documented and resolved (or marked as conflicting)
- [ ] Uncertainty explicitly marked with appropriate labels
- [ ] top-places.md has all required sections (Top Picks, Backups, Dining Strategy, To-Do)
- [ ] Dining Strategy is practical and complete
- [ ] All verification commands pass (see workflow-detailed.md Step 7)
- [ ] PROGRESS.md and README.md updated with current status
- [ ] Geographic distribution considered (not all in same neighborhood)
- [ ] Category balance achieved (mix of casual, special occasion, dessert)

### Review Focus Areas

- Score consistency across similar candidates
- Evidence quality and sufficiency (4+ sources minimum)
- **Negative review coverage for all top picks (35+)** - ensures balanced risk assessment
- Exclusion reason clarity and justification
- Practical constraint accuracy (check official websites for hours/closures)

### Why Negative Reviews Matter

Even highly-rated restaurants can have serious issues that only appear in negative reviews:

**Critical risks hidden in negative reviews**:
- 🚫 **Health/Safety**: Allergy handling failures, food poisoning, hygiene violations
- 🚫 **Discrimination**: Prejudiced treatment, nationality-based service disparities
- 🚫 **Tourist Traps**: Locals warning to avoid, quality decline, overpricing consensus
- ⚠️ **Service Patterns**: Consistent rudeness, aggressive tipping, poor treatment of non-regulars
- ⚠️ **Value Issues**: Price-quality mismatch not apparent from high ratings alone

**Real examples from this project**:
- Mraz & Sohn (39/50): "DON'T EAT HERE IF YOU HAVE A FOOD ALLERGY" - critical safety warning
- Roscioli (39/50): "A review from an actual Roman: AVOID! This is a tourist trap"
- Gasthaus Pöschl (39/50): "Shockingly discriminatory and aggressive experience"

**Without negative review research, users might**:
- Book restaurants with serious allergy handling issues (health risk)
- Experience discrimination or rude treatment (emotional distress)
- Overpay for tourist trap establishments (financial + experience loss)
- Have unrealistic expectations leading to disappointment

**Best practice**: Research negative reviews AFTER initial scoring (35+) to:
1. Validate high scores with balanced perspective
2. Identify and flag serious red flags with ⚠️
3. Set realistic expectations for users
4. Provide context for known issues

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

- **Aim for 5-10 top picks per category** for each city (enough variety, not overwhelming)
- **Include 3-5 backups** (alternatives if top picks unavailable)
- **Balance categories**: At least one casual option, one special occasion, one dessert/gelato
- **Geographic spread**: Cover different neighborhoods to match daily itinerary

---

## Common Pitfalls to Avoid

1. **Don't research everything at once** - focus on top candidates first
2. **Don't skip overview.md** - context is crucial for prioritization
3. **Don't rely on single sources** - cross-reference at least 3-4 sources
4. **Don't forget practical constraints** - reservation policies, closed days, queue times matter
5. **Don't over-optimize scores** - a 35-40 range is realistic for good places; not everything is 45+
6. **Don't neglect geographic distribution** - consider travel time from hotel

---

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
