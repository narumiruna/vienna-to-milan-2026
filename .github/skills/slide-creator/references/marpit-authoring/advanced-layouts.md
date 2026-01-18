# Advanced Layouts

Complex slide structures and multi-column techniques for Marpit.

---

## Split Layouts with Background Images

**Left-Right Split:**
```markdown
![bg left:40%](diagram.png)        # 40% left, 60% right
![bg right:40%](screenshot.png)    # 40% right, 60% left
```

**Variations:** `left:30%`, `left:50%`, `left:60%`, etc.

**Vertical Split:**
```markdown
![bg vertical](top-image.png)
![bg](bottom-image.png)            # Images stacked vertically
```

---

## Multiple Background Images

**Side-by-Side Comparison:**
```markdown
![bg left:50%](before.png)
![bg right:50%](after.png)

# Before and After
```

### Three-Image Layout

```markdown
![bg left:33%](img1.png)
![bg](img2.png)
![bg right:33%](img3.png)

# Three Perspectives
```

---

## Table-Based Layouts

### Two-Column Content

```markdown
# Comparison

| **Approach A** | **Approach B** |
|----------------|----------------|
| Pros: | Pros: |
| • Fast | • Reliable |
| • Simple | • Scalable |
| | |
| Cons: | Cons: |
| • Limited | • Complex |
```

---

### Three-Column Layout

```markdown
| Frontend | Backend | Database |
|----------|---------|----------|
| React | Node.js | PostgreSQL |
| TypeScript | Express | Redis |
| Vite | GraphQL | MongoDB |
```

**Tip:** Keep columns balanced for best appearance.

---

## Mixed Content Layouts

### Code + Explanation

````markdown
# Implementation

```python
def process(data):
    return transform(data)
```

**Key aspects:**
- Pure function (no side effects)
- Type-safe with annotations
- Easily testable
````

---

## Table-Based Layouts

**Two-Column Content:**
```markdown
| Column 1 | Column 2 |
|----------|----------|
| Content A | Content B |
```

**Multi-Column Lists:**
```markdown
| Core | Advanced |
|------|----------|
| • Feature 1 | • Feature A |
| • Feature 2 | • Feature B |
```

---

## List Layouts

**Nested Lists with Emphasis:**
```markdown
1. **Layer 1**
   - Detail a
   - Detail b
2. **Layer 2**
   - Detail c
```

---

## Quote Layouts

```markdown
> "Quote text here"
— Author

**Context:**
- Explanation
```

---

## Mixed Content Layouts

**Code + Image:**
```markdown
![bg right:45%](diagram.png)

```python
code_example()
```

Explanation text
```

**Dashboard/Metrics:**
```markdown
| Metric | Value | Trend |
|--------|-------|-------|
| Users | 1.2M | ↑ 15% |
```

**Hero Section:**
```markdown
<!-- _class: lead invert -->
<!-- _backgroundImage: url('bg.jpg') -->

# **BIG MESSAGE**
Subtitle
```

---

**Before:**
```python
def calc(a,b,c):
    return a+b*c
```

**After:**
```python
def calculate_total(base: int, rate: int, quantity: int) -> int:
    """Calculate total with rate and quantity."""
    return base + (rate * quantity)
```
````

---

## Icon/Emoji Lists

```markdown
# Workflow

✅ **Plan** - Define requirements
🔨 **Build** - Implement features
🧪 **Test** - Verify quality
🚀 **Deploy** - Release to production
```

**Note:** Use sparingly; ensure emojis display correctly in your environment.

---

## Timeline Layout

```markdown
# Project Phases

| Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 |
|---------|---------|---------|---------|
| Planning | Development | Testing | Launch |
| Research | Alpha | Beta | GA |
```

Or vertical:

```markdown
# Roadmap

**Phase 1: Foundation** (Jan-Mar)
- Core infrastructure

**Phase 2: Features** (Apr-Jun)
- User-facing functionality

**Phase 3: Scale** (Jul-Sep)
- Performance optimization
```

---

## Grid Layout (Pseudo)

```markdown
# Tech Stack

| Frontend | Backend | DevOps | Data |
|----------|---------|--------|------|
| React | Django | Docker | PostgreSQL |
| Next.js | FastAPI | K8s | Redis |
| Tailwind | Node | GitHub Actions | Elasticsearch |
```

---

## Highlight Box Pattern

Using tables for visual separation:

```markdown
# Key Takeaway

| 💡 Important Insight |
|----------------------|
| The most impactful optimization was caching at the edge, reducing latency by 85%. |
```

Or with quotes:

```markdown
> **📌 Remember:**
> Always validate user input at API boundaries, not just in the UI.
```

---

## Process Flow

```markdown
# Data Pipeline

```
User Input → Validation → Processing → Storage → Response
```

**Steps:**
1. **Validation** - Check format and constraints
2. **Processing** - Transform and enrich
3. **Storage** - Persist to database
4. **Response** - Return confirmation
```

---

## Comparison Matrix

```markdown
# Solution Comparison

|              | Solution A | Solution B | Solution C |
|--------------|------------|------------|------------|
| **Cost**     | Low        | Medium     | High       |
| **Speed**    | Fast       | Medium     | Slow       |
| **Scale**    | Limited    | Good       | Excellent  |
| **Ease**     | Easy       | Medium     | Complex    |
```

---

## Image Gallery

```markdown
![bg contain](image1.png)
![bg contain](image2.png)
![bg contain](image3.png)

# Portfolio Examples
```

**Effect:** Shows multiple images in a grid/sequence.

---

## Math-Heavy Slide

```markdown
# Algorithm Complexity

**Time complexity:**
$$
O(n \log n)
$$

**Space complexity:**
$$
O(n)
$$

Optimal for datasets < 1M records
```

---

## Mixed Media

```markdown
![bg right:50% fit](demo-screenshot.png)

# Live Demo

**Try it yourself:**
https://demo.example.com

**Features shown:**
- Real-time updates
- Drag and drop
- Auto-save
```

---

## Full-Screen Image with Caption

```markdown
<!-- _class: lead -->
<!-- _backgroundImage: url('impactful-image.jpg') -->
<!-- _backgroundSize: cover -->
<!-- _color: white -->

# Memorable Caption
```

---

## Source Code with Annotations

````markdown
# Key Implementation

```python
class UserService:
    def __init__(self, db: Database):        # ← Dependency injection
        self.db = db

    async def get_user(self, id: int):       # ← Async for performance
        return await self.db.fetch_one(...)  # ← Single query
```

**Design principles:**
- DI for testability
- Async for scalability
````

---

## Tips for Advanced Layouts

1. **Test across renderers** - Marp CLI, Marp VS Code, browsers may render differently
2. **Keep it simple** - Complex layouts can be fragile
3. **Use tables sparingly** - They're powerful but can be hard to maintain
4. **Background images** - Most reliable for splits
5. **Preview frequently** - Check rendering after each slide

---

## Troubleshooting

**Issue:** Images not splitting correctly
**Fix:** Ensure `![bg left:XX%]` comes before content

**Issue:** Text overlapping images
**Fix:** Adjust percentage or use solid background with opacity

**Issue:** Tables breaking layout
**Fix:** Reduce content or split across slides

**Issue:** Code blocks too wide
**Fix:** Shorten lines or use smaller font in `<style>` section
