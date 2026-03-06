# Coding Guidelines

These are the coding guidelines for a Python project using GitHub Copilot.
You MUST adhere to the following coding guidelines when contributing to this project.

## Versioning

### Version pinning
Referenced python libraries in `pyproject.toml` should be pinned to ensure better compatibility, reproducibility and stability:

**`==` strict version pinning**
Use for highly critical libraries or libraries known for breaking changes. Bear in mind that useful updates like security patches and bug fixes won't be installed either.

**`~=` compatible version pinning**
Use when your library should benefit from minor updates within that version like bug fixes and non-breaking feature updates. Bear in mind that you depend on the library producer to manage non-breaking updates accordingly. 
Note that the behaviour depends on whether patch version is specified, it is important to consider official Python documentation on [Version specifiers - Python Packaging User Guide](https://packaging.python.org/en/latest/specifications/version-specifiers/).

## Command Execution

Use Taskfile tasks in `Taskfile.yaml` as the canonical project commands.

## Quality Checks

Before completing any task:
- [ ] Code follows style guide
- [ ] All functions have type hints
- [ ] Tests are written and passing (`task lint`)
- [ ] No linting errors (`task lint`)
- [ ] Code is formatted (`task format`)
- [ ] API returns appropriate status codes
- [ ] Error cases are handled
- [ ] Dependencies are in `pyproject.toml`
- [ ] `uv.lock` is committed if dependencies changed