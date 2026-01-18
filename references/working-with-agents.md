# Working with Agents: Ensuring Task Completion

**Purpose**: Practical guidance for managing agent behavior and ensuring research tasks complete successfully.

**When to use**: When delegating tasks to agents and encountering incomplete work or premature stopping.

---

## How to Keep Agents Working Until Completion

**Problem**: Agents may stop mid-task, leaving research incomplete.

**Solutions**:

1. **Break large tasks into clear, atomic steps**
   - ✅ "Research and score Pompi tiramisu" (specific, achievable)
   - ❌ "Research all tiramisu in Italy" (too broad, likely to stop mid-way)

2. **Set clear completion criteria in instructions**
   - Define what "done" means (e.g., "score must be in candidates.md AND notes.md")
   - Agent will work toward the defined end state

3. **Use progress tracking tools**
   - Agent should call `report_progress` after each meaningful unit of work
   - This creates checkpoints and shows what's left

4. **Provide task checklists**
   - Include a checklist in your request (e.g., "Research 3 restaurants: A, B, C")
   - Agent can track progress and know when complete

5. **Avoid ambiguous scope**
   - ✅ "Add top 3 tiramisu places to Rome candidates" (clear boundary)
   - ❌ "Research tiramisu" (unclear when to stop)

## When Agent Stops Unexpectedly

**If agent stops mid-research**:
- Check the last commit to see what was completed
- Verify files in git status to confirm progress

**If agent repeatedly stops**:
- Break the task into smaller chunks
- Ask agent to complete one specific file at a time
- Use "complete X, then Y, then Z" format
