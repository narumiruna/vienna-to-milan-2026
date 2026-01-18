# Troubleshooting

Common issues and solutions when embedding SVG in Marp slides.

---

## Issue: Emoji Not Rendering in SVG

**Symptoms:** Emoji appear as boxes, blank spaces, or inconsistent across platforms

**Cause:** Emoji in `<text>` elements not reliably supported across SVG renderers

**Solution:** **NEVER use emoji in SVG `<text>`.** Use pure SVG paths and shapes instead.

**Correct:** Create simple geometric icons from circles, rects, and paths

---

## Issue: SVG Not Rendering

**Symptoms:** Blank space, broken image icon, or works locally but not in export

**Causes & Solutions:**

### 1. Incorrect File Path

**Problem:** Path doesn't match actual file location

**Fix:**
```markdown
<!-- Wrong -->
![w:1200](diagram.svg)

<!-- Correct -->
![w:1200](assets/diagram.svg)
```

Verify file structure:
```
presentation/
├── slides.md
└── assets/
    └── diagram.svg
```

### 2. Missing `xmlns` Attribute

**Problem:** SVG missing XML namespace declaration

**Common causes:**
1. Incorrect file path
2. Missing `xmlns` attribute: `<svg xmlns="http://www.w3.org/2000/svg">`
3. External dependencies: Embed all resources inline

---

## Issue: SVG Clipped or Cropped

**Symptoms:** Parts cut off, content extends beyond visible area

**Solutions:**
1. Content outside viewBox: Ensure all content within bounds (120-1800 horizontal, 120-960 vertical)
2. Missing viewBox: Always include `viewBox="0 0 1920 1080"`
3. Transform issues: Review all `transform` attributes

---

## Issue: Text Not Displaying

**Solutions:**
1. Use system font stack: `font-family="ui-sans-serif, system-ui, -apple-system"`
2. Add explicit font-size: `<text font-size="24">`
3. Verify color contrast with background

---

## Issue: SVG Too Small or Too Large

**Solutions:**
1. Adjust width based on placement: `![w:1200](file.svg)` or `<img width="720">`
2. Always include width/height: `<svg viewBox="0 0 1920 1080" width="1920" height="1080">`

---

## Issue: Inconsistent Rendering Across Browsers

**Solutions:**
1. Specify all dimensions explicitly: `<rect x="100" y="100" width="200" height="100" />`
2. Avoid `foreignObject` (inconsistent support): Use native SVG elements

---

## Issue: Blurry or Pixelated SVG

**Solutions:**
1. Use vector shapes only (avoid embedded raster images)
2. Ensure viewBox and dimensions match

---

## Issue: Colors Not Matching

**Solutions:**
1. Define all colors explicitly
2. Verify gradient references are correct

---

## Issue: Performance Problems

**Solutions:**
1. Simplify complex paths
2. Reduce total element count (group when possible)

---

## Issue: Alignment Issues

**Solutions:**
1. Use consistent grid system
2. Apply uniform spacing values

---

## Issue: Arrows Not Appearing

**Solutions:**
1. Verify marker definition exists in `<defs>`
2. Check marker reference: `marker-end="url(#arrowhead)"`

---

## Issue: GitHub Actions Build Fails

**Solutions:**
1. Verify file committed to repository
2. Check path correctness in CI config

---

## SVG Validation Tools

**svglint** - Command-line SVG linter:
```bash
npm install -g svglint
svglint diagram.svg
```

---

## Debugging Workflow

1. Check syntax errors in SVG file
2. Verify xmlns attribute present
3. Test in browser directly
4. Check console for errors
5. Validate with svglint

---

## Quick Fixes Checklist

- [ ] `xmlns="http://www.w3.org/2000/svg"` present
- [ ] ViewBox defined: `viewBox="0 0 1920 1080"`
- [ ] Width/height attributes present
- [ ] No emoji in `<text>` elements
- [ ] All paths closed properly
- [ ] Font sizes specified
- [ ] System fonts used
- [ ] No external resources

---

## Still Having Issues?

1. Simplify SVG progressively until it works
2. Compare with working examples from pattern-examples.md
3. Check browser console for specific errors
