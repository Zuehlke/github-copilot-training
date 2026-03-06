---
name: handoff-writing
description: This skill standardizes how agents persist results as handoff files between phases in the refine → plan → implement pipeline.
---

# Handoff Writing
Agents must write structured handoff files so the next agent can continue work without additional context.

## File Location
All handoffs must be written to:

.github/handoff/

## File Naming Convention
YYYY-MM-DD_<phase>_<slug>.md

Where:

- phase = refine | plan | implement
- slug = short kebab-case description of the feature

## Templates
Use the templates located in the `templates/` directory:

- `refine-handoff.md`
- `plan-handoff.md`
- `implement-handoff.md`

Copy the appropriate template when creating a new handoff document.

## General Rules
- Handoff files must be Markdown
- Keep them concise and structured
- Do not include unnecessary explanation
- Each handoff must allow the next agent to proceed without extra context
