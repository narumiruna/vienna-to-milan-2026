# Quality Checklist & Best Practices

Verification steps, common pitfalls, and best practices for gourmet research.

## Pre-Research Checklist

Before starting research for a new city:

- [ ] Review city dates and accommodation in PROGRESS.md or AGENTS.md
- [ ] Understand city-specific food highlights and signature dishes
- [ ] Identify dietary constraints (e.g., no alcoholic beverages)
- [ ] Note any seasonal closures or holidays during visit dates
- [ ] Check hotel location for convenience scoring baseline

## During Research: Quality Standards

### Source Quality

**Minimum requirements**:
- [ ] 4+ independent sources per place
- [ ] At least one aggregator (Google Maps, Tripadvisor)
- [ ] At least one local/community source (Reddit, local blog)
- [ ] At least one professional guide (Michelin, TimeOut, food blog)

**Source hierarchy** (highest to lowest reliability):
1. Michelin Guide, established food critics
2. Local food blogs with track record
3. Reddit threads with detailed local discussions
4. Google Maps/Tripadvisor (aggregate patterns, not individual reviews)
5. General travel blogs
6. Social media mentions (use with caution)

**Red flags to avoid**:
- ❌ Single-source recommendations
- ❌ Sponsored/promotional content only
- ❌ Outdated sources (>2 years old without recent confirmation)
- ❌ Generic listicles without detail

### Evidence Documentation

**In notes.md, for each place**:
- [ ] Official website or Google Maps link provided
- [ ] Google Maps rating + review count with direct URL
- [ ] Tripadvisor or equivalent rating + review count
- [ ] Reddit sentiment summarized with thread links
- [ ] Food guide citations with URLs
- [ ] Recurring pros listed (minimum 2-3)
- [ ] Recurring cons listed (acknowledge weaknesses)
- [ ] Practical info: reservation, hours, queues, closures
- [ ] 50-point score breakdown with justification for each component
- [ ] Any uncertainty marked explicitly (unknown, conflicting, unverified)

**Evidence quality markers**:
- ✅ Specific examples: "Carbonara praised in 15+ reviews"
- ✅ Direct quotes from reliable sources
- ✅ Quantitative data: ratings, review counts, prices
- ✅ Temporal context: "2024 reviews consistent with 2022"
- ❌ Vague claims: "people say it's good"
- ❌ Unsourced assertions
- ❌ Fabricated reviews or facts

### Scoring Integrity

**For each scored place**:
- [ ] All 5 components scored (Taste, Value, Convenience, Consistency, Risk)
- [ ] Each component has explicit justification in notes.md
- [ ] Total score calculated correctly (sum of 5 components)
- [ ] Score interpretation applied correctly (40+, 35-39, 30-34, <30)
- [ ] Higher scores supported by strong evidence from multiple sources
- [ ] Lower scores have clear reasons documented

**Score calibration checks**:
- [ ] Michelin-starred venues generally score 38+ (unless major convenience/value issues)
- [ ] Tourist traps score <30 (high risk, low value despite convenience)
- [ ] Local favorites with strong reviews score 35-40 range
- [ ] Decent but unremarkable places score 30-34

## After Research: Completion Verification

### File Completeness Checks

Run these commands and verify results:

```bash
# Should return 0 (no inbox status remaining)
grep -E "\| inbox \||status:?\s*inbox" gourmet/[city]/candidates.md | wc -l

# Should return 0 (no pending decisions)
grep -E "^#.*待決定|^#.*[Uu]ndecided|TODO|PENDING" gourmet/[city]/excluded.md | wc -l

# Should return 4 (all required sections present)
grep -E "^## (Top Picks|Backups|Dining Strategy|To-Do)" gourmet/[city]/top-places.md | wc -l

# Should return 0 (all checklist items complete)
grep "\[ \]" gourmet/[city]/overview.md | wc -l
```

### Overview.md Completeness

- [ ] Travel dates and accommodation documented
- [ ] City food highlights summarized
- [ ] Research strategy documented
- [ ] Progress checklist shows all items completed [x]
- [ ] Important notes section filled (hours, holidays, transport)

### Candidates.md Table Integrity

- [ ] All entries have status field (no missing statuses)
- [ ] Google Maps URLs are real links (not placeholders)
- [ ] No duplicate entries (same restaurant listed twice)
- [ ] Status values are valid: inbox | researching | shortlisted | rejected | top
- [ ] Rejected entries also documented in excluded.md
- [ ] No entries deleted without documentation

### Notes.md Evidence Quality

- [ ] Each researched place has dedicated section
- [ ] Section headers match place names in candidates.md
- [ ] 50-point score present for each researched place
- [ ] Score breakdown with 5 components documented
- [ ] Evidence from 4+ sources cited with URLs
- [ ] Practical information documented
- [ ] Conflicts/uncertainties explicitly noted

### Top-places.md Finalization

- [ ] "Top Picks" section with score 35+ entries
- [ ] "Backups" section with score 30-34 entries
- [ ] All entries sorted by descending score within sections
- [ ] Each entry includes: name, score, area, type, google_maps_url
- [ ] Justifications provided for each pick
- [ ] Practical constraints noted (reservation, hours, etc.)
- [ ] "Dining Strategy" section with time/budget/logistics planning
- [ ] "To-Do" section with pre-trip and during-trip tasks

### Excluded.md Documentation

- [ ] All rejected candidates documented
- [ ] Clear reason provided for each exclusion
- [ ] Categorized appropriately (low score, tourist trap, practical impossibility, etc.)
- [ ] No pending decisions marked with "待決定" or "TODO"

## Common Pitfalls & How to Avoid

### Pitfall 1: Insufficient Research Depth
**Problem**: Single-source recommendations or minimal evidence

**Solution**:
- Always collect 4+ independent sources
- Spend 15-20 minutes per place on thorough research
- Use web_search with specific queries: "[Place Name] [City] reviews Reddit Michelin"

### Pitfall 2: Deleting Candidate Entries
**Problem**: Removing entries from candidates.md table without documentation

**Solution**:
- Never delete entries; use `status: rejected` instead
- Document all rejections in excluded.md with clear reasons
- Maintain audit trail for all candidates considered

### Pitfall 3: Placeholder Google Maps Links
**Problem**: Using "[查看地圖]" or invalid URLs

**Solution**:
- Get real links from Google Maps (maps.app.goo.gl format)
- Use search API format: `https://www.google.com/maps/search/?api=1&query=[Place+Name+City]`
- Test all links before finalizing

### Pitfall 4: Score Without Justification
**Problem**: Numbers in candidates.md but no breakdown in notes.md

**Solution**:
- Always document 5-component breakdown in notes.md
- Provide brief justification for each component score
- Link evidence to specific sources

### Pitfall 5: Ignoring Practical Constraints
**Problem**: High scores for inconvenient or impossible-to-visit places

**Solution**:
- Factor convenience into scoring (location, reservation, hours)
- Document practical constraints explicitly
- Adjust risk score for booking difficulties or seasonal closures

### Pitfall 6: Inconsistent Scoring Calibration
**Problem**: All places scored 35-40, or scores don't reflect quality differences

**Solution**:
- Use full scale 0-50
- Tourist traps should score <30
- Excellent but inconvenient places might score 35-38
- Outstanding convenient places score 40+
- Compare scores across places for relative calibration

### Pitfall 7: Copying Generic Descriptions
**Problem**: Vague summaries without specific details

**Solution**:
- Include specific dishes mentioned in reviews
- Note recurring themes (e.g., "carbonara praised in 15+ reviews")
- Provide concrete examples of pros/cons

### Pitfall 8: Not Marking Uncertainty
**Problem**: Treating uncertain information as fact

**Solution**:
- Use explicit labels: unknown, conflicting, unverified, seasonal, outdated
- Document source disagreements
- Adjust consistency score when evidence conflicts

### Pitfall 9: Incomplete top-places.md
**Problem**: Missing sections or thin dining strategy

**Solution**:
- Ensure all 4 required sections present (Top Picks, Backups, Dining Strategy, To-Do)
- Dining strategy should address: time planning, reservations, budget, geography
- To-Do should list specific pre-trip and during-trip actions

### Pitfall 10: Skipping Verification Commands
**Problem**: Assuming completion without verification

**Solution**:
- Run all 4 verification commands before marking city complete
- Fix any issues found (inbox entries, pending decisions, missing sections)
- Update PROGRESS.md only after all checks pass

## Quality Improvement Process

### When Reviewing Existing Research

If reviewing/improving existing city research:

1. **Run verification commands** to identify gaps
2. **Check candidates.md**: Any inbox/researching status? Research those first
3. **Review notes.md scores**: Consistent? Justified? All 5 components documented?
4. **Validate top-places.md**: All required sections? Dining strategy complete?
5. **Check excluded.md**: Clear reasons? No pending decisions?
6. **Verify links**: All Google Maps URLs working?

### Red Flag Audit

Review for these quality issues:

- **Single-source recommendations**: Add 3+ more sources
- **Scores without justification**: Add 5-component breakdown
- **Placeholder links**: Replace with real Google Maps URLs
- **Deleted candidates**: Restore to table with status: rejected, add to excluded.md
- **Incomplete sections**: Fill in missing content
- **Uncertainty not marked**: Add explicit labels where appropriate

## Best Practices for Efficiency

### Efficient Web Search Patterns

**Good queries** (specific, comprehensive):
- "[Restaurant Name] [City] reviews Reddit Michelin Tripadvisor"
- "best [dish type] in [City] 2024 2025"
- "[City] [neighborhood] restaurant recommendations Reddit"

**Poor queries** (too broad or vague):
- "restaurants in [City]"
- "[Restaurant Name]" (too generic)
- "food in [City]" (overwhelming results)

### Batch Similar Tasks

- Research 3-5 places at once, then score all together
- Do all evidence collection before scoring phase
- Update all files (candidates, notes, top-places) in one pass

### Use Templates Efficiently

- Copy templates at city initialization
- Fill in structure gradually as research progresses
- Use template sections as checklists

### Document As You Go

- Add to notes.md immediately after finding evidence (avoid losing sources)
- Update candidates.md status field after each phase
- Mark uncertainties when discovered, not later

## Lessons Learned

### What Works Well

- ✅ Starting with overview.md sets clear research strategy
- ✅ Inbox.md for fast initial capture (20+ candidates quickly)
- ✅ Focused research on top 3-5 priorities first
- ✅ 50-point rubric provides objective comparison
- ✅ Progressive disclosure keeps files scannable
- ✅ Explicit completion criteria prevents premature closure

### What to Avoid

- ❌ Trying to research everything at once (focus on priorities)
- ❌ Perfectionism in initial scoring (can always refine)
- ❌ Deleting instead of documenting exclusions
- ❌ Skipping practical constraints in scoring
- ❌ Generic descriptions without specific examples
- ❌ Assuming completion without running verification

## Emergency Recovery

### If Research Gets Messy

1. **Run verification commands** to quantify issues
2. **Prioritize fixes**:
   - Critical: Missing scores, broken links, deleted candidates
   - Important: Incomplete evidence, thin justifications
   - Nice-to-have: Minor formatting issues
3. **Fix systematically**: One file at a time, one issue type at a time
4. **Re-verify** after fixes

### If Scores Don't Make Sense

1. **Recalibrate** by finding outliers (too high or too low)
2. **Re-read evidence** for those places
3. **Compare** to similar places in same city
4. **Adjust** component scores based on evidence
5. **Document** reasoning for changes in notes.md

### If Files Are Inconsistent

1. **Use candidates.md as source of truth** for place names and status
2. **Sync notes.md** to match candidates.md place names
3. **Rebuild top-places.md** from scored entries in notes.md
4. **Update excluded.md** to match rejected entries in candidates.md
