---
name: code-quality-and-testing
description: This skill defines the commands used to verify code quality and correctness in this repository.
---

# Code Quality and Testing
Agents must run these commands before considering implementation complete.


## Canonical Task Targets
Use Taskfile commands directly for all validation work:

- `task lint` - run lint checks
- `task lint-fix` - auto-fix lint issues where possible
- `task format` - format code
- `task test` - run tests
- `task test-coverage` - run tests with coverage output
- `task check` - run lint + tests

## Validation Requirements
Before completing implementation work, ensure:

- All tests pass
- No linting errors remain
- Code is formatted correctly
- Test coverage is maintained for new code