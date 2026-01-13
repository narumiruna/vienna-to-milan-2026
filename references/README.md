# AGENTS.md Reference Documentation

This directory contains detailed reference material for AGENTS.md, following the **progressive disclosure** principle.

## Purpose

AGENTS.md provides core instructions and workflow overview. When you need deeper details, consult these reference files.

## Available References

### [workflow-detailed.md](workflow-detailed.md)
**Complete step-by-step workflow instructions**

- Step 0: Initialize City Research
- Step 1: Discovery — Candidate Collection  
- Step 2: Evidence Collection — Per Place
- Step 3: Scoring — Standard Rubric
- Step 4: Decision Rules
- Step 5: Triage — Exclusion with Reasons
- Step 6: Final Output — Top Picks
- Step 7: Post-Research Updates — Documentation Maintenance

**When to read**: When executing research tasks and you need specific guidance beyond the workflow summary in AGENTS.md.

**Key topics**:
- inbox.md lifecycle and cleanup procedures
- candidates.md required fields and Google Maps link requirements
- Evidence collection template and conflict handling
- Detailed scoring guidance per dimension (9-10, 7-8, 5-6, 3-4, 0-2 scales)
- Promotion/exclusion thresholds and decision documentation
- Verification commands for completion checks

---

### [quality-standards.md](quality-standards.md)
**Quality bar, audit framework, and best practices**

- Quality Bar (core principles, research standards)
- Audit Framework (preservation rules, audit trail requirements)
- Quality Assurance Checklist (what to verify before completion)
- Process Improvements (lessons learned, efficient patterns)
- Common Pitfalls to Avoid
- Research Questions Checklist

**When to read**: When validating research quality, conducting reviews, or ensuring completeness before marking a city as done.

**Key topics**:
- Minimum 4+ sources requirement
- Preservation rules (never delete from candidates.md)
- Tourist trap vs authentic signals
- Time allocation guidelines
- Geographic distribution and category balance

---

## How to Use These References

### Progressive Disclosure in Action

1. **Start with AGENTS.md** - Get the essential instructions and workflow overview (< 5 minutes)
2. **Execute with summaries** - Use the concise workflow steps in AGENTS.md for most tasks
3. **Dive deeper as needed** - Open reference files when you need:
   - Detailed field requirements and formats
   - Scoring guidance for edge cases
   - Conflict resolution procedures
   - Quality validation checklists

### Navigation Pattern

```
AGENTS.md (Quick Reference)
    ↓ Need workflow details?
workflow-detailed.md (Complete steps)
    ↓ Need quality validation?
quality-standards.md (Audit & best practices)
```

### Examples

**Scenario 1: Starting new city research**
- Read AGENTS.md Quick Reference
- Follow Step 0 summary in AGENTS.md
- If unclear about inbox.md lifecycle → Open workflow-detailed.md Step 1

**Scenario 2: Scoring a borderline candidate**
- Check scoring summary in AGENTS.md (40+, 35-39, 30-34, <30)
- Need detailed guidance per dimension → Open workflow-detailed.md Step 3
- See Taste/Quality 9-10 vs 7-8 criteria

**Scenario 3: Completing city research**
- Run verification commands from AGENTS.md Step 7
- If audit fails → Open quality-standards.md
- Review Quality Assurance Checklist section

---

## Benefits of This Structure

✅ **Faster onboarding**: New agents can start with Quick Reference in < 5 minutes  
✅ **Reduced cognitive load**: Don't read 500+ lines when you only need 50  
✅ **Better navigation**: Clear signposts for when to read more  
✅ **Full traceability**: All detailed info preserved in references  
✅ **Maintainability**: Update details in one place without bloating main doc

---

## Document Maintenance

When updating these references:

1. **Keep AGENTS.md lean**: Only essential workflow summaries
2. **Update references for details**: Full specifications, examples, edge cases
3. **Link clearly**: Always tell readers when/why to read reference files
4. **Avoid duplication**: Information lives in ONE place (prefer references for details)
5. **Test navigation**: Ensure references are discoverable from AGENTS.md

**Example of good linking** (from AGENTS.md):
```markdown
### 2. Evidence Collection

**What**: Research each candidate thoroughly with multiple sources.

**Key actions**: [concise bullet points]

**Time**: 15-20 minutes per place

📖 Full details: See [references/workflow-detailed.md - Step 2](references/workflow-detailed.md#step-2-evidence-collection--per-place)
```

---

## Related Documentation

- **AGENTS.md**: Main instructions (start here)
- **templates/README.md**: File templates and usage guide (295 lines)
- **PROGRESS.md**: Research completion standard and city status tracking
