# Marpit Authoring Best Practices

## Table of Contents

- [HTML Usage Policy](#html-usage-policy)
  - [Why Avoid HTML](#why-avoid-html)
  - [Recommended Alternatives to HTML](#recommended-alternatives-to-html)
  - [When HTML is Acceptable](#when-html-is-acceptable)
  - [HTML Enablement (If Required)](#html-enablement-if-required)
- [Design Principles](#design-principles)
  - [Visual Consistency: The Golden Rule](#visual-consistency-the-golden-rule)
- [Consistency Checklist](#consistency-checklist)
  - [1. Color Palette](#1-color-palette)
- [Content Slide](#content-slide)
  - [2. Spacing System](#2-spacing-system)
  - [3. Layout Patterns](#3-layout-patterns)
  - [4. Typography](#4-typography)
- [Main Section (H2 - major points)](#main-section-h2-major-points)
  - [Subsection (H3 - details)](#subsection-h3-details)
  - [Sometimes H3 for title](#sometimes-h3-for-title)
- [Inconsistent usage](#inconsistent-usage)
  - [5. Directives Usage](#5-directives-usage)
- [Design System Template](#design-system-template)
- [When to Break Consistency](#when-to-break-consistency)
- [Content Best Practices](#content-best-practices)
  - [Slide Density](#slide-density)
- [Benefits of Microservices](#benefits-of-microservices)
- [Architecture Overview](#architecture-overview)
  - [Title Guidelines](#title-guidelines)
  - [Code Slides](#code-slides)
- [User Authentication](#user-authentication)
- [Code](#code)
- [Visual Hierarchy](#visual-hierarchy)
  - [Importance Levels](#importance-levels)
  - [Example Hierarchy](#example-hierarchy)
- [Key Concept (Secondary - Medium, Bold)](#key-concept-secondary-medium-bold)
- [Common Mistakes to Avoid](#common-mistakes-to-avoid)
  - [1. Inconsistent Section Dividers](#1-inconsistent-section-dividers)
- [Section 2  <!-- Missing lead class -->](#section-2-missing-lead-class-)
  - [Section 3  <!-- Wrong heading level -->](#section-3-wrong-heading-level-)
  - [2. Random Color Changes](#2-random-color-changes)
  - [3. Overusing Styling](#3-overusing-styling)
- [**🎨 AMAZING** *Feature* ✨ **LAUNCH** 🚀](#-amazing-feature-launch-)
  - [WOW SUCH DESIGN VERY PROFESSIONAL](#wow-such-design-very-professional)
- [New Feature Launch](#new-feature-launch)
  - [4. Ignoring Whitespace](#4-ignoring-whitespace)
- [Workflow Checklist](#workflow-checklist)
  - [Before Starting](#before-starting)
  - [During Creation](#during-creation)
  - [After Completion](#after-completion)
- [Performance Tips](#performance-tips)
  - [Keep Files Manageable](#keep-files-manageable)
  - [Rendering Optimization](#rendering-optimization)
- [Accessibility](#accessibility)
  - [Color Contrast](#color-contrast)
  - [Text Legibility](#text-legibility)
  - [Structure](#structure)
- [Testing Your Presentation](#testing-your-presentation)
  - [Pre-Presentation Checklist](#pre-presentation-checklist)
  - [Common Issues](#common-issues)
- [See Also](#see-also)

Guidelines for creating professional, consistent, and effective slide presentations.

---

## HTML Usage Policy

**CRITICAL: Avoid HTML in Marpit slides whenever possible.**

### Why Avoid HTML

1. **Security** - Disabled by default, requires explicit enablement (`--html` flag)
2. **Portability** - Breaks viewing in non-Marp Markdown editors
3. **Maintainability** - Pure Markdown easier to edit and version control
4. **Philosophy** - Defeats purpose of Markdown-first tool

### Recommended Alternatives to HTML

**Instead of `<div>` layouts:** Use tables, `![bg left:40%]()` split layouts, custom theme CSS, or background images with text overlay

**Instead of inline styles:** Use directives (`backgroundColor`, `backgroundImage`, `color`), `<style scoped>` blocks, or custom theme CSS with `class` directive

### When HTML is Acceptable

Only when: (1) No Marpit alternative exists, (2) Visual complexity justifies cost, (3) You control rendering environment, (4) Requirement documented clearly

**Enablement:** VS Code: Settings → "Marp: Enable HTML" | CLI: `marp slides.md --html`

---

## Design Principles

### Visual Consistency: The Golden Rule

**CRITICAL: Consistency from beginning to end is paramount.**

A presentation with inconsistent styling appears unprofessional and distracts from content. Before starting, establish a design system and apply it uniformly.

---

## Consistency Checklist

### 1. Color Palette

- ✅ Choose ONE accent color for all section dividers
- ✅ Use background shades with intentional hierarchy (darkest for leads, medium for content, lightest for emphasis)
- ✅ Maintain consistent text colors for similar content types
- ❌ Avoid: Different colors for each section without pattern

### 2. Spacing System

- ✅ Use ONE standard gap size for all grid layouts (e.g., 48px)
- ✅ Use ONE standard margin-top value (e.g., 32px)
- ✅ Maintain consistent padding around content blocks
- ❌ Avoid: Mixing gap sizes randomly (32px, 40px, 48px)

### 3. Layout Patterns

- ✅ Reuse same grid template for similar content
- ✅ Keep two-column splits at same proportions
- ✅ Use consistent border radius, stroke width
- ❌ Avoid: Different layout structures for similar content types

### 4. Typography

- ✅ Use consistent font weights (e.g., 700 for all section titles)
- ✅ Maintain heading hierarchy (H1 for titles, H2 for subtitles, H3 for sections)
- ✅ Keep emoji/icon usage consistent in position and style
- ❌ Avoid: Random font weight changes, inconsistent heading levels

**Good hierarchy**:
```markdown
# Slide Title (H1 - once per slide)
## Main Section (H2 - major points)
### Subsection (H3 - details)
```

**Bad hierarchy**:
```markdown
# Sometimes H1
### Sometimes H3 for title
## Inconsistent usage
```

### 5. Directives Usage

- ✅ Apply `<!-- _class: lead -->` to ALL section dividers or NONE
- ✅ Use consistent background colors for lead slides
- ✅ Apply pagination consistently (show on all or hide on specific slides)
- ❌ Avoid: Some section dividers with lead class, others without

---

## Design System Template

Before creating slides, define these constants:

```markdown
Design System:
- Primary accent: #0891b2 (all section dividers)
- Background: #f8fafc (all content slides)
- Text color: #1e293b (all body text)
- Gap size: 48px (all grid layouts)
- Margin-top: 32px (all section spacing)
- Border radius: 12px (all rounded elements)
- Section divider pattern: lead class, primary accent, white text
```

Then apply consistently throughout.

---

## When to Break Consistency

Only break consistency for intentional emphasis:

**Acceptable exceptions**:
- Final "thank you" or "contact" slide may use different color
- Warning/alert slides may use red/orange intentionally
- Before/after comparisons may use contrasting styles
- Q&A slide may have unique styling

**Example (Acceptable)**:
```markdown
<!-- Standard section divider -->
<!-- _backgroundColor: #0891b2 -->
# Section 1
---
<!-- ... content ... -->
---
<!-- Special warning slide -->
<!-- _backgroundColor: #dc2626 -->
<!-- _class: lead -->
# ⚠️ Important Notice
---
<!-- Back to standard -->
<!-- _backgroundColor: #0891b2 -->
# Section 2
```

---

## Content Best Practices

### Slide Density

**One idea per slide**: Each slide focuses on one key message, use 3-5 bullets max. Avoid wall of text, 10+ bullets, or multiple topics.

### Title Guidelines

**Be specific and descriptive**: ✅ "Authentication Flow with OAuth 2.0" | ❌ "Authentication"

### Code Slides

**Keep code minimal**: Show only relevant portions, use syntax highlighting, add brief comments, split complex code across multiple slides.

### Image Usage

**CRITICAL: Always use `bg` (background) syntax for diagrams and large images.**

**Why:** Automatic sizing with `fit` modifier, consistent appearance, better split layouts, reduces maintenance.

**Good**: `![bg right fit](diagrams/architecture.svg)` | **Bad**: Regular image syntax requiring manual sizing

# System Architecture

- Component A
- Component B
- Component C
```

**Good - full-page background**:
```markdown
![bg fit](diagrams/detailed-workflow.svg)

# Optional Overlay Title
```

**Acceptable - small icons only**:
```markdown
![width:40px](icons/check.svg) Feature enabled
```

**Bad - regular syntax for diagrams**:
```markdown
![width:800px](diagrams/architecture.svg)
<!-- Manual sizing required, inconsistent across slides -->
```

**Split layout patterns**:
- `![bg right fit]` - Image on right, text on left
- `![bg left fit]` - Image on left, text on right  
- `![bg right:40% fit]` - Image takes 40% on right
- `![bg left:60% fit]` - Image takes 60% on left

**When to use each:**
- **Diagram with explanation**: Split layout (`![bg right/left fit]`)
- **Full-page diagram**: Full background (`![bg fit]`)
- **Icon/logo inline**: Regular syntax only for very small images (`width:40px`)
- **Comparison**: Side-by-side (`![bg left:50% fit]` + `![bg right:50% fit]`)

---

## Visual Hierarchy

### Importance Levels

1. **Primary**: Slide title (H1 or H2)
2. **Secondary**: Section headings (H2 or H3)
3. **Tertiary**: Body text, lists
4. **Quaternary**: Captions, footnotes

**Use visual weight to reinforce hierarchy**:
- Larger font size = more important
- Bold weight = emphasis
- Color accent = key point
- White space = separate sections

### Example Hierarchy

```markdown
# Main Topic (Primary - Largest, Bold)

## Key Concept (Secondary - Medium, Bold)

Important details in body text (Tertiary - Normal)

- Supporting point 1
- Supporting point 2

<small style="color: #64748b;">Source: Research 2024</small> (Quaternary - Smallest, Muted)
```

---

## Common Mistakes to Avoid

### 1. Inconsistent Section Dividers

❌ **Don't**:
```markdown
<!-- _class: lead -->
# Section 1
---
## Section 2  <!-- Missing lead class -->
---
<!-- _class: lead -->
### Section 3  <!-- Wrong heading level -->
```

✅ **Do**:
```markdown
<!-- _class: lead -->
# Section 1
---
<!-- _class: lead -->
# Section 2
---
<!-- _class: lead -->
# Section 3
```

### 2. Random Color Changes

❌ **Don't**: Change colors without reason

✅ **Do**: Establish one palette and stick to it

### 3. Overusing Styling

❌ **Don't**:
```markdown
## **🎨 AMAZING** *Feature* ✨ **LAUNCH** 🚀

<div style="background: linear-gradient(45deg, red, orange, yellow, green, blue, indigo, violet); padding: 50px; border: 10px dotted gold; box-shadow: 0 0 50px magenta; transform: rotate(5deg); animation: spin 2s infinite;">

### WOW SUCH DESIGN VERY PROFESSIONAL

</div>
```

✅ **Do**:
```markdown
## New Feature Launch

Key benefits...
```

### 4. Ignoring Whitespace

❌ **Don't**: Cram everything together

✅ **Do**: Use generous spacing between sections

---

## Workflow Checklist

### Before Starting

- [ ] Define design system (colors, spacing, patterns)
- [ ] Choose theme (default/gaia/uncover)
- [ ] Decide on section divider style
- [ ] Plan content outline

### During Creation

- [ ] Apply design system consistently
- [ ] One idea per slide
- [ ] Use proper heading hierarchy
- [ ] Keep code examples minimal
- [ ] Test rendering periodically

### After Completion

- [ ] Review all slides for consistency
- [ ] Check color uniformity
- [ ] Verify spacing is consistent
- [ ] Test on projector/presentation mode
- [ ] Proofread all text

---

## Performance Tips

### Keep Files Manageable

- Avoid embedding huge images
- Use external image files when possible
- Keep SVGs optimized
- Test export time (HTML/PDF)

### Rendering Optimization

- Minimize complex CSS in `<style>` tags
- Avoid excessive HTML divs
- Use theme features when available
- Test on target presentation device

---

## Accessibility

### Color Contrast

- Ensure text has sufficient contrast (≥ 4.5:1)
- Test with colorblind simulators
- Don't rely solely on color to convey meaning

### Text Legibility

- Use readable font sizes (H1 ≥ 48px, body ≥ 24px)
- Avoid light gray text on white backgrounds
- Use high-contrast for code blocks

### Structure

- Use semantic heading hierarchy
- Add alt text to images
- Keep content scannable

---

## Testing Your Presentation

### Pre-Presentation Checklist

- [ ] Render in Marp preview
- [ ] Test on actual projector
- [ ] Check legibility from back of room
- [ ] Verify animations/transitions (if any)
- [ ] Test on target device (laptop/tablet)
- [ ] Have backup (PDF export)

### Common Issues

1. **Colors look different on projector**
   - Solution: Test beforehand, avoid subtle color differences

2. **Text too small**
   - Solution: Minimum font sizes (see Accessibility above)

3. **Layout breaks on different screen size**
   - Solution: Use relative units (%, fr) instead of fixed pixels

---

## See Also

- [syntax-guide.md](syntax-guide.md) - Marpit syntax reference
- [patterns.md](patterns.md) - Common slide patterns
- [themes.md](themes.md) - Theme-specific features
- [advanced-layouts.md](advanced-layouts.md) - Complex layouts
