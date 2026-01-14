---
name: gourmet-research
description: Expert workflow for conducting evidence-based food research (restaurants, cafes, desserts) with systematic scoring, multi-source validation, and structured documentation. Use when researching dining options for a city, evaluating food venues, conducting systematic food recommendations, or managing progressive disclosure documentation (overview.md, candidates.md, notes.md, top-places.md, inbox.md, excluded.md).
---

# Gourmet Research

Expert workflow for building high-quality, evidence-based food recommendations through systematic research, scoring, and documentation.

## When to Use This Skill

- Researching dining options for a new city
- Creating structured food recommendations
- Evaluating restaurants, cafes, or dessert venues systematically
- Managing food research documentation with 6-file progressive disclosure structure
- Applying standardized 50-point scoring rubric to food venues

## Core Workflow

Follow these steps sequentially for each city:

### 1. Initialize City Research

Create `overview.md` with:
- Travel dates, accommodation info
- City-specific food highlights (signature dishes, local specialties)
- Research strategy and priorities
- Progress checklist

Run 3-4 web searches to collect 20+ initial candidates. Record in `inbox.md` for fast capture.

**Time**: 30 minutes

### 2. Discover Candidates

Transfer top 3-5 candidates from inbox to `candidates.md` table with status: `inbox`.

**Required table fields**:
- name, category (restaurant|cafe|dessert), area, type
- google_maps_url (must be real link: maps.app.goo.gl or search API format)
- status (inbox | researching | shortlisted | rejected | top)
- sources, notes (Traditional Chinese)

**Time**: 20 minutes

### 3. Collect Evidence

For each candidate, research thoroughly and add detailed section to `notes.md`:

**Required sources (minimum 4)**:
1. Google Maps (rating + review count)
2. Tripadvisor or aggregator
3. Reddit (local sentiment)
4. Food/travel guide (Michelin, TimeOut, blogs)

**Document**:
- Ratings from each source with URLs
- Recurring pros/cons
- Practical info: reservation requirements, hours, queue times, closures
- Handle conflicts/uncertainty explicitly (mark: unknown, conflicting, unverified)

**Time**: 15-20 minutes per place

### 4. Score with Rubric

Apply 50-point scoring system in notes.md for each researched place:

**Components (0-10 each)**:
- **Taste/Quality**: Food quality, authenticity, execution
- **Value**: Price vs quality, portion size
- **Convenience**: Location, reservation ease, access
- **Consistency**: Reliability across reviews, time periods
- **Risk** (10=low risk): Likelihood of disappointment

**Interpretation**:
- 40+: Excellent → Top Pick
- 35-39: Very good → Top Pick
- 30-34: Good → Backup
- <30: Consider exclusion

Add total score to candidates.md table for quick reference.

**Time**: 10 minutes per place

### 5. Make Decisions

Apply promotion/exclusion thresholds:

**Promote to top-places.md**:
- Score ≥35 → Top Pick
- Score 30-34 → Backup

**Exclude (mark rejected)**:
- Score <25 → Automatic exclusion
- Hard triggers: tourist trap evidence, hygiene concerns, severe service issues, practical impossibility

Update candidates.md: `status: top` or `status: rejected`

**Time**: 5 minutes per place

### 6. Triage Rejections

For rejected candidates:
- Update candidates.md: `status: rejected`
- Add entry to `excluded.md` with clear reason
- Never delete entries - always document exclusions

**Time**: 5 minutes per rejected place

### 7. Finalize Recommendations

Create/update `top-places.md` with:

**Required sections**:
1. **Top Picks** (35+): Name, score, area, type, google_maps_url, justification, constraints
2. **Backups** (30-34): Same format
3. **Dining Strategy**: Time planning, reservation strategy, budget, transportation
4. **To-Do**: Confirm closures, make reservations, plan schedule

List in descending score order within each section.

**Time**: 30 minutes

### 8. Verify Completion

Run completion checks:

```bash
# All should return 0 except top-places (should return 4)
grep -E "\| inbox \||status:?\s*inbox" gourmet/[city]/candidates.md | wc -l
grep -E "^#.*待決定|^#.*[Uu]ndecided|TODO|PENDING" gourmet/[city]/excluded.md | wc -l
grep -E "^## (Top Picks|Backups|Dining Strategy|To-Do)" gourmet/[city]/top-places.md | wc -l
grep "\[ \]" gourmet/[city]/overview.md | wc -l
```

**Completion criteria (all required)**:
- ✅ No `status: inbox` in candidates.md
- ✅ No pending decisions in excluded.md
- ✅ top-places.md has: Top Picks + Backups + Dining Strategy + To-Do
- ✅ overview.md checklist fully checked `[x]`

Update PROGRESS.md status accordingly.

**Time**: 10 minutes

## Progressive Disclosure Architecture

The 6-file structure provides layered information access:

| File | Purpose | Read Time | When Used |
|------|---------|-----------|-----------|
| overview.md | Context & strategy | 5 min | Starting research |
| top-places.md | Final picks | 10 min | Planning trip |
| candidates.md | Summary table | 5 min | Quick scan |
| notes.md | Full evidence | 30+ min | Validation |
| inbox.md | Working notes | N/A | Discovery |
| excluded.md | Audit trail | 5 min | Understanding rejections |

**Key principles**:
- Start with conclusions, then provide evidence (inverted pyramid)
- Use summaries in higher layers (top-places, candidates)
- Keep full details in lower layers (notes)
- Link between layers: "See notes.md for evidence"
- Never duplicate information across files

## Quality Standards

**Research requirements**:
- Minimum 4+ sources per place
- Every score justifiable with documented evidence
- Document uncertainty explicitly (use labels: unknown, conflicting, unverified, seasonal, outdated)
- Fewer, high-confidence picks over many uncertain ones
- Full traceability from recommendation to evidence

**Critical rules**:
- Never delete candidates.md entries (use `status: rejected` + excluded.md)
- Never fabricate facts or reviews
- Clearly distinguish source reports vs. your synthesis
- Test all Google Maps links
- Use Traditional Chinese for content; English for structured fields

## File Structure Per City

Required directory structure:
```
gourmet/YYYY-MM-DD-city/
├── overview.md
├── inbox.md
├── candidates.md
├── notes.md
├── top-places.md
└── excluded.md
```

Templates available at repository root: `/templates/*.md`

## References

For detailed guidance on specific aspects:

- **scoring-guide.md**: Comprehensive rubric with examples for each component
- **quality-checklist.md**: Verification steps, common pitfalls, best practices

## Quick Examples

**Example query**: "Research dining options for Florence, February 19-22"

**Response**:
1. Create overview.md with Florence context (Tuscan cuisine highlights: bistecca, ribollita, lampredotto)
2. Run web searches for top restaurants, trattorias, gelaterias
3. Add 5 priority candidates to candidates.md
4. Research each with 4+ sources, document in notes.md
5. Apply 50-point scoring
6. Promote 35+ to top-places.md with dining strategy
7. Verify completion criteria met
