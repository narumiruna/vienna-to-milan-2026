# AGENTS.md Reference Documentation

This directory contains detailed reference material for AGENTS.md, following the **progressive disclosure** principle.

## Purpose

AGENTS.md provides core instructions and workflow overview. When you need deeper details, consult these reference files.

## Available References

### [workflow-detailed.md](workflow-detailed.md)
**Complete step-by-step workflow instructions**

- Initialize City Research
- Discovery — Candidate Collection  
- Evidence Collection — Per Place
- Scoring — Standard Rubric
- Decision Rules
- Triage — Exclusion with Reasons
- Final Output — Top Picks
- Post-Research Updates — Documentation Maintenance

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

### [progressive-disclosure.md](progressive-disclosure.md)
**Design philosophy for organizing research documentation**

- Core Idea
- The Problem We're Solving
- 6-File Layered Architecture
- Key Rules for Agents
- Examples (Good vs Bad)

**When to read**: When creating or organizing documentation files, understanding the 6-file architecture and information flow.

**Key topics**:
- Progressive disclosure prevents information overload
- Each file serves a distinct purpose and information layer
- Information flow: overview → top-places → candidates → notes → excluded
- DO: Start with conclusions, use summaries in higher layers
- DON'T: Duplicate information, mix abstraction levels

---

### [working-with-agents.md](working-with-agents.md)
**Practical guidance for managing agent behavior**

- How to Keep Agents Working Until Completion
- When Agent Stops Unexpectedly

**When to read**: When delegating tasks to agents and encountering incomplete work or premature stopping.

**Key topics**:
- Break large tasks into clear, atomic steps
- Set clear completion criteria
- Provide task checklists
- Avoid ambiguous scope
- Use "complete X, then Y, then Z" format for sequential tasks

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
- Follow Initialize summary in AGENTS.md
- If unclear about inbox.md lifecycle → Open workflow-detailed.md Discovery section

**Scenario 2: Scoring a borderline candidate**
- Check scoring summary in AGENTS.md (40+, 35-39, 30-34, <30)
- Need detailed guidance per dimension → Open workflow-detailed.md Scoring section
- See Taste/Quality 9-10 vs 7-8 criteria

**Scenario 3: Completing city research**
- Run verification commands from AGENTS.md
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

📖 Full details: See [references/workflow-detailed.md](references/workflow-detailed.md#evidence-collection--per-place)
```

---

## Related Documentation

- **AGENTS.md**: Main instructions (start here)
- **templates/README.md**: File templates and usage guide (295 lines)
- **PROGRESS.md**: Research completion standard and city status tracking
