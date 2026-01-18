# Progressive Disclosure Principle

**Purpose**: Design philosophy for organizing research documentation to prevent information overload while maintaining traceability.

**When to use**: When creating or organizing documentation files, understanding the 6-file architecture.

---

## Core Idea

Reveal information gradually - show only what's needed at each stage, with clear paths to deeper detail.

## The Problem We're Solving

Users have different needs at different times:
- 🏃 **Quick decisions**: "Where should I eat tonight?" → Need: top-places.md (1 min)
- 🔍 **Research validation**: "Why this restaurant?" → Need: notes.md evidence (5 min)
- 📋 **Overview scan**: "What are all my options?" → Need: candidates.md table (2 min)
- ❓ **Audit trail**: "Why was X excluded?" → Need: excluded.md (30 sec)

**Progressive disclosure prevents information overload while maintaining traceability.**

## Our 6-File Layered Architecture

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

## Key Rules for Agents

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

## Examples

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

## Further Reading

For deeper understanding of progressive disclosure in documentation design:
- Anthropic Skills Guide: Three-level loading system (metadata → body → resources)
- See AGENTS.md structure as an example: Quick Reference → detailed sections
