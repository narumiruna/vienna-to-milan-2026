# Embedding SVG in Marpit Slides

Complete guide for embedding SVG illustrations in Marp/Marpit Markdown presentations.

---

## Embedding Methods

**RECOMMENDED: Use `bg` (background) syntax for most images to avoid manual sizing.**

**Background Syntax (Preferred):**
```markdown
![bg fit](diagram.svg)              # Full-page background
![bg right fit](architecture.svg)   # Split layout - image on right
![bg left fit](workflow.svg)        # Split layout - image on left
![bg right:40% fit](detail.svg)     # Custom split ratio
```

**Pros**: `fit` modifier auto-scales, no manual adjustments, consistent sizing, better for split layouts

**External File (Legacy - for small inline images only):**
```markdown
![width:800px](diagram.svg)
```

**Use only for**: Small inline icons (e.g., `![width:40px](icon.svg)`)

**Base64 Inline (For production):**
```markdown
![](data:image/svg+xml;base64,PHN2Zy...)
```

**Pros**: Self-contained, single file distribution
**Generate with**: `base64 -w 0 diagram.svg`

---

## Placement Patterns

**Full-Page Background:**
```markdown
![bg fit](diagram.svg)
```

**Split Layout - Text and Image:**
```markdown
![bg right:40% fit](diagram.svg)
# Title
Content on left
```

**Multiple Images:**
```markdown
![bg left:50%](before.svg)
![bg right:50%](after.svg)
```

---

## Responsive Considerations

**Maintain aspect ratio**: SVG automatically maintains aspect ratio when only width or height specified

**Percentage widths**: Can use in layouts (`width: 50%`) for responsive sizing

---

## Common Embedding Issues

**Issue 1: SVG Too Small** - Solution: Use `bg fit` syntax or increase width specification
**Issue 2: SVG Pixelated** - Solution: Ensure SVG is vector-only (no embedded raster images)
**Issue 3: Colors Look Different** - Solution: Test in actual HTML export, define all colors explicitly
**Issue 4: SVG Not Showing** - Solution: Check file path, verify xmlns attribute, embed all resources inline
**Issue 5: Base64 Too Long** - Solution: Simplify SVG or use external file

---

## Best Practices

1. **Use bg syntax by default** for diagrams and illustrations
2. **Consistent sizing** within presentation (e.g., all centered diagrams at 1200px)
3. **Use alt text** for accessibility

---

## Production Workflow

**Development**: Use external files (`.svg`) for fast iteration
**Distribution**: Convert to base64 for self-contained Markdown

**Convert command**: `base64 -w 0 diagram.svg`

---

## Quick Reference

**Syntax Cheatsheet:**
- `![bg fit](file.svg)` - Full-page background
- `![bg right fit](file.svg)` - Split right
- `![bg left fit](file.svg)` - Split left
- `![w:1200](file.svg)` - Fixed width (legacy)

**Sizing Guidelines:**
- Centered diagrams: 1200px
- Two-column graphics: 720px
- Icons: 40-60px

---

## Placement Patterns

**Prefer `bg` syntax for all these patterns.**

### Pattern 1: Full-Page Background (Most Common)

```markdown
![bg fit](architecture.svg)

# Optional Overlay Title

Optional text overlays on the image.
```

**Result**: SVG fills entire slide, auto-sized with `fit`.

**When to use**: Showing a complete diagram without much text.

---

### Pattern 2: Split Layout - Text and Image

**Image on right, text on left:**

```markdown
![bg right fit](process-flow.svg)

## Process Flow

1. Initialize system
2. Load configuration
3. Start services
4. Monitor health
```

**Image on left, text on right:**

```markdown
![bg left fit](architecture.svg)

# System Architecture

Explanation of the architecture appears on the right side.
```

**Custom split ratio:**

```markdown
![bg left:60% fit](main-diagram.svg)

# Details

Diagram takes 60%, text takes 40%.
```

**Result**: Side-by-side layout with automatic image sizing.

**When to use**: Explaining a diagram with text.

---

### Pattern 3: Multiple Images Comparison

```markdown
![bg left:50% fit](before.svg)
![bg right:50% fit](after.svg)

# Before → After
```

**Result**: Two images side-by-side.

**When to use**: Comparisons, before/after.

---

### Pattern 4: Legacy Centered on Slide (Avoid)

**Only use for small inline images:**

```markdown
## Architecture Overview

![width:60px](icon.svg) Component A
![width:60px](icon.svg) Component B
```

**Use bg syntax instead for diagrams:**

```markdown
![bg fit](architecture.svg)
```

---

## Responsive Considerations

### Maintain Aspect Ratio

**Good**:
```markdown
![width:800px](diagram.svg)  <!-- Height auto-calculated -->
```

**Bad**:
```markdown
![w:800px h:400px](diagram.svg)  <!-- May distort if aspect ratio doesn't match -->
```

### Percentage Widths

Works inside containers:

```markdown
<div style="width: 80%; margin: 0 auto;">

![width:100%](diagram.svg)

</div>
```

**Result**: SVG fills 80% of slide width, centered.

---

## Theme-Specific Adjustments

### Default Theme

- Clean, minimal background
- Use any SVG colors
- Good contrast required

### Gaia Theme

- Modern, colorful slides
- Match SVG colors to theme (blues, teals)
- Consider theme's existing accent colors

### Uncover Theme

- Bold, high-contrast
- Use strong colors in SVGs
- Ensure visibility on theme's backgrounds

**Tip**: Test SVGs on all intended themes.

---

## Common Embedding Issues

### Issue 1: SVG Too Small on Slide

**Cause**: ViewBox too large (e.g., 1920×1080 for small content)

**Solution**: Adjust viewBox to match actual content bounds.

```xml
<!-- Before (wrong) -->
<svg viewBox="0 0 1920 1080">
  <rect x="800" y="400" width="320" height="280"/>  <!-- Small in huge canvas -->
</svg>

<!-- After (correct) -->
<svg viewBox="0 0 320 280">
  <rect x="0" y="0" width="320" height="280"/>
</svg>
```

### Issue 2: SVG Pixelated

**Cause**: Raster image embedded in SVG, or bitmap export

**Solution**: Use vector shapes only, export as SVG (not PNG).

### Issue 3: Colors Look Different

**Cause**: Color profile issues, display calibration

**Solution**: Use web-safe hex colors, test on target device.

### Issue 4: SVG Not Showing

**Causes**:
- Wrong file path
- Missing `xmlns` attribute
- Invalid SVG syntax

**Solutions**:
```xml
<!-- Ensure namespace -->
<svg xmlns="http://www.w3.org/2000/svg" ...>

<!-- Validate syntax (close all tags) -->
```

### Issue 5: Base64 Too Long

**Cause**: Complex SVG with many elements

**Solutions**:
- Simplify SVG (remove unnecessary details)
- Use external file instead of base64
- Optimize with SVGO tool

See [troubleshooting.md](troubleshooting.md) for more issues and solutions.

---

## Best Practices

### 1. Use bg syntax by default

**ALWAYS prefer `bg` syntax for diagrams and illustrations:**

```markdown
<!-- DO THIS -->
![bg fit](diagram.svg)
![bg right fit](architecture.svg)

<!-- NOT THIS (unless it's a tiny icon) -->
![width:800px](diagram.svg)
```

**Exceptions**: Only use regular syntax for very small inline icons:
```markdown
![width:40px](check-icon.svg) Feature enabled
```

### 2. Consistent Sizing Within Presentation

When using `bg fit`, sizing is automatic and consistent. No manual adjustments needed!

### 3. Use Alt Text

```markdown
![bg fit Microservices architecture diagram](architecture.svg)
```

**Benefits**:
- Accessibility
- Fallback description if SVG doesn't load

---

## Production Workflow

### Development Phase

1. Create SVG files separately (`diagram1.svg`, `diagram2.svg`, etc.)
2. Reference externally in Markdown:
   ```markdown
   ![width:800px](diagram1.svg)
   ```
3. Iterate quickly (edit SVG, reload Marpit preview)

### Distribution Phase

**Option A: Bundle Files**
- Keep SVGs as separate files
- Distribute folder with `.md` + SVG files
- Easy for others to edit

**Option B: Embed as Base64**
- Convert all SVGs to base64
- Inline in Markdown
- Self-contained single file

**Recommended**: Option A during collaboration, Option B for final export.

---

## Advanced: Dynamic SVG with Variables

Use CSS custom properties for theming:

```xml
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      :root {
        --primary-color: #0891b2;
        --bg-color: #f0f9ff;
      }
    </style>
  </defs>

  <rect fill="var(--bg-color)" stroke="var(--primary-color)" stroke-width="3"/>
</svg>
```

**Benefit**: Change colors globally by updating CSS variables.

---

## Quick Reference

### Syntax Cheatsheet

```markdown
<!-- PREFERRED: bg syntax with fit -->
![bg fit](full-page.svg)
![bg right fit](side-image.svg)
![bg left fit](main-diagram.svg)
![bg right:40% fit](detail.svg)

<!-- Comparison -->
![bg left:50% fit](before.svg)
![bg right:50% fit](after.svg)

<!-- LEGACY: Only for small inline icons -->
![width:40px](icon.svg)

<!-- External file (for development) -->
![bg fit](diagram.svg)

<!-- Base64 inline (for distribution) -->
![bg fit](data:image/svg+xml;base64,PHN2Zy4uLg==)
```

### Sizing Guidelines

| Use Case | Recommended Syntax | Notes |
|----------|-------------------|-------|
| Full-page diagram | `![bg fit]` | Auto-sized, fills slide |
| Split layout | `![bg right/left fit]` | Auto-sized, 50/50 split |
| Custom split | `![bg right:40% fit]` | Image takes specified % |
| Small inline icon | `![width:40px]` | Only for tiny images |
| Comparison | `![bg left:50% fit]` + `![bg right:50% fit]` | Side-by-side |

**Rule of thumb**: If it's a diagram or illustration, use `bg fit` syntax.

---

## See Also

- [core-rules.md](core-rules.md) - SVG creation basics
- [pattern-examples.md](pattern-examples.md) - Common diagram patterns
- [troubleshooting.md](troubleshooting.md) - Solving embedding issues
- [../marpit-authoring/syntax-guide.md](../marpit-authoring/syntax-guide.md) - Marpit image syntax
