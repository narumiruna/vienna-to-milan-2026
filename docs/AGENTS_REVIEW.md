# AGENTS.md Review and Evaluation

**Date**: 2026-01-12  
**Reviewer**: AI Assistant  
**Purpose**: Comprehensive review of AGENTS.md for accuracy, consistency, and completeness

---

## Executive Summary

AGENTS.md is a well-structured document that provides comprehensive guidance for AI agents working on food research. However, several issues were identified during this review:

### Critical Issues
1. **Venice completion status mismatch**: PROGRESS.md claims Venice is "✅ 已完成" with "已處理所有 inbox 項目", but `gourmet/2026-02-22-venice/candidates.md` contains **9 inbox items** (lines 20-28)
2. **Incomplete syntax at line 541-542**: Documentation rule for place filenames is cut off mid-sentence

### Minor Issues
3. **Inconsistent table schema**: Venice uses a `score` column in candidates.md that is not documented in AGENTS.md
4. **Milan uses Chinese headers**: Milan's candidates.md uses Chinese column names (名稱, 類別, etc.) instead of English, violating AGENTS.md section "Documentation & Naming Rules"

### Recommendations
- Fix the incomplete line 541-542 in AGENTS.md
- Update AGENTS.md to document the optional `score` column in candidates.md
- Either fix Venice's completion status or process the 9 inbox items
- Standardize Milan's candidates.md to use English headers
- Add clarification about when `score` column should be used vs. keeping scores in notes.md only

---

## Detailed Findings

### 1. Critical Issue: Venice Completion Status Mismatch

**Location**: PROGRESS.md line 14 vs. gourmet/2026-02-22-venice/candidates.md

**What PROGRESS.md says**:
```
| 威尼斯 | ✅ 已完成 | 9 個推薦地點 | 已完成詳細評分，包含海鮮餐廳、bacaro/cicchetti、gelato、咖啡館、糕點店。已處理所有 inbox 項目與待決定候選。 |
```

**What the verification shows**:
```bash
$ grep -E "\| inbox \||status:?\s*inbox" gourmet/2026-02-22-venice/candidates.md | wc -l
9
```

**The 9 inbox items are**:
- Osteria Alla Staffa
- Il Ridotto
- CoVino
- Cantina Do Mori
- Bacareto da Lele
- Paradiso Perduto
- Caffè Florian
- Gelateria Alaska
- Rosa Salva

**According to AGENTS.md section "Research Completion Standard"**:
> A city is marked "✅ 已完成" when ALL of the following are met:
> 1. All candidates triaged (no `status: inbox` in candidates.md)

**Impact**: High - This violates the completion standard defined in AGENTS.md

**Recommendation**: Either:
- Change Venice status to 🔄 待完成 until inbox items are processed
- Process the 9 inbox items (research or move to excluded.md with reasons)

---

### 2. Critical Issue: Incomplete Documentation Rule (Line 541-542)

**Location**: AGENTS.md lines 541-542

**Current text**:
```markdown
- Place filenames MUST follow:
  <city>-<normalized-place-name>.md
```

**Problem**: This appears to be an incomplete rule. The format `<city>-<normalized-place-name>.md` is shown but:
1. No context about what "place filenames" refers to
2. Looking at the repository, there are no files matching this pattern
3. The rule seems unrelated to the actual file structure used (e.g., `2026-02-11-vienna/`)

**Hypothesis**: This may be:
- A leftover from an earlier naming convention
- An incomplete sentence that should specify something else
- A rule that was never implemented

**Recommendation**: Either:
- Complete the rule with proper context and examples
- Remove it if it's obsolete
- Clarify what files this applies to (if any)

---

### 3. Minor Issue: Undocumented `score` Column in candidates.md

**Location**: Venice candidates.md has a `score` column not mentioned in AGENTS.md

**AGENTS.md says** (lines 263-271):
```markdown
Minimum fields per candidate in candidates.md table:
- name
- category (restaurant | cafe | dessert)
- area / neighborhood
- type (e.g. pasta, steak, espresso, gelato)
- google_maps_url (use search link initially, replace with exact link when researched)
- status: inbox | researching | shortlisted | rejected | top
- sources (brief: e.g., "Tripadvisor, Reddit, Michelin")
- notes (Traditional Chinese, brief summary)
```

**Venice actually uses**:
```markdown
| name | category | area | type | google_maps_url | status | score | sources | notes |
```

**Other cities use**:
- Vienna: name | category | area | type | google_maps_url | status | sources | notes
- Rome: name | category | area | type | google_maps_url | status | sources | notes
- Florence: name | category | area | type | google_maps_url | status | sources | notes
- Milan: 名稱 | 類別 | 區域 | 特色 | 評分 | 狀態 | 備註 (Chinese headers)

**Impact**: Low - The `score` column is a useful addition but inconsistent across cities

**Recommendation**:
- Document the `score` column as optional in AGENTS.md
- Clarify when to use inline scores vs. keeping them only in notes.md
- Consider standardizing all cities to include or exclude the score column

---

### 4. Minor Issue: Milan Uses Chinese Headers

**Location**: gourmet/2026-02-25-milan/candidates.md

**AGENTS.md says** (line 538):
> - Use English for structured fields and keys

**Milan uses**:
```markdown
| 名稱 | 類別 | 區域 | 特色 | 評分 | 狀態 | 備註 |
```

Instead of:
```markdown
| name | category | area | type | score | status | notes |
```

**Impact**: Low - Functional but violates the documentation standard

**Recommendation**: Update Milan's candidates.md to use English headers to match other cities

---

## Verification Against AGENTS.md Standards

### ✅ Passed Checks

1. **File Structure**: All cities have the required 6 files:
   - overview.md ✓
   - inbox.md ✓
   - candidates.md ✓
   - notes.md ✓
   - top-places.md ✓
   - excluded.md ✓

2. **Directory Naming**: All cities use ISO date prefix format:
   - 2026-02-11-vienna/ ✓
   - 2026-02-13-rome/ ✓
   - 2026-02-19-florence/ ✓
   - 2026-02-22-venice/ ✓
   - 2026-02-25-milan/ ✓

3. **Progressive Disclosure**: File separation between candidates.md (summary) and notes.md (details) is implemented correctly

4. **Overview Checklists**: All cities have completed checklists (no `[ ]` items remaining)

5. **No Pending Exclusions**: No excluded.md files have "待決定" or "Undecided" section headers

### ❌ Failed Checks

1. **Venice Inbox Items**: 9 items with `status: inbox` remain
2. **Milan Headers**: Uses Chinese instead of English for table headers

---

## Documentation Quality Assessment

### Strengths

1. **Comprehensive Coverage**: AGENTS.md covers all major aspects of the research workflow
2. **Clear Structure**: Well-organized with progressive sections (0-6)
3. **Progressive Disclosure Principle**: Excellent explanation with examples and anti-patterns
4. **Practical Guidance**: Includes time estimates, common patterns, and pitfalls
5. **Verification Commands**: Includes specific bash commands for checking completion status
6. **Cross-References**: Good linking to PROGRESS.md for detailed criteria

### Areas for Improvement

1. **Examples Consistency**: Some examples in AGENTS.md don't match actual implementation (e.g., score column)
2. **Completion Standard Enforcement**: Venice violates completion standard but is marked complete
3. **Incomplete Rules**: Line 541-542 needs completion or removal
4. **Schema Variations**: Need to either standardize or document allowed variations in table schemas

---

## Recommendations Summary

### High Priority (Must Fix)

1. **Fix Venice Status**:
   - Option A: Change status to 🔄 待完成 in PROGRESS.md and README.md
   - Option B: Process the 9 inbox items to completion
   
2. **Fix Line 541-542**:
   - Complete the incomplete rule or remove it if obsolete

### Medium Priority (Should Fix)

3. **Standardize Milan Headers**:
   - Update candidates.md to use English column names

4. **Document Score Column**:
   - Add `score` as an optional field in AGENTS.md
   - Clarify when to use it vs. keeping scores only in notes.md

### Low Priority (Consider)

5. **Standardize Table Schemas**:
   - Consider adding a "Schema Variations" section to AGENTS.md
   - Document which columns are required vs. optional
   - Consider migrating all cities to the same schema

6. **Add Schema Examples**:
   - Include actual table format examples in AGENTS.md
   - Show both with and without score column

---

## Alignment with PROGRESS.md and README.md

### PROGRESS.md
- ✅ Structure matches AGENTS.md completion standards (mostly)
- ❌ Venice status incorrectly marked as complete
- ✅ Verification commands match AGENTS.md specifications
- ✅ Status progression clearly defined (⏳ → 📝 → 🔄 → ✅)

### README.md
- ✅ Progress table syncs with PROGRESS.md
- ❌ Venice also marked as complete in README.md
- ✅ Brief overview appropriate for top-level document
- ✅ Links to PROGRESS.md for details

---

## Conclusion

AGENTS.md is a high-quality, comprehensive guide that has clearly been refined through actual use. The document structure is excellent, the progressive disclosure principle is well-implemented, and the workflow guidance is practical.

The main issues are:
1. **Enforcement gap**: Venice marked complete despite not meeting standards
2. **Minor documentation gaps**: Incomplete line 541-542, undocumented score column
3. **Minor inconsistencies**: Milan's Chinese headers, schema variations

**Overall Rating**: 8.5/10
- Excellent content and structure
- Minor issues that should be addressed for consistency
- One critical issue (Venice status) that violates the completion standard

**Recommended Actions**:
1. Process Venice inbox items or update status
2. Fix incomplete line 541-542
3. Document optional score column
4. Standardize Milan headers
