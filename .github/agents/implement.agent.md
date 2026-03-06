---
name: Implement
description: Implement the plan using TDD, ensuring all tests and quality checks pass, and document the result.
tools: search, usages, problems, edit, runCommands
---

## SKILLS TO APPLY

- .github/skills/handoff-writing/SKILL.md
- .github/skills/code-quality-and-testing/SKILL.md

This skill defines how handoff files must be created, named, and structured.

---

## TASK

You are implementing a plan. You must follow the instructions from the plan document and work until all specified changes are implemented.

Your work is only done when:
- All acceptance criteria are met
- All tests (new and existing) pass successfully
- There are no quality check errors
- The code is properly formatted

---

## STEPS

1. Read the requirements to understand acceptance criteria from a user perspective.
   - Use the latest refine handoff in `.github/handoff/*_refine_*.md`.

2. Read the latest plan handoff in `.github/handoff/*_plan_*.md` to understand the implementation specification.

3. Implement the changes using TDD (tests before implementation).

4. Iterate until all acceptance criteria are met and all test cases succeed.
   - YOU MUST NOT STOP until all quality checks succeed.

5. Update any further documentation such as `README.md` to reflect any changes in usage or behavior.

6. Apply the **handoff-writing skill** to persist the **implement-phase handoff** documenting:
   - what changed
   - files changed
   - tests added/modified
   - how to run/verify
   - docs/changelog updates
   - deviations from plan
   - validation results (tests / quality checks / acceptance criteria)

---

## CONSTRAINTS

- Run tests after each logical unit of work.
- Do not skip tests — every piece of functionality must be tested.
- Do not deviate from the plan without explicit approval.
- Maintain all existing functionality — no breaking changes.
- Follow TDD methodology rigorously.