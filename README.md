# Github Copilot Training

This training repo contains an API for managing flight delay information.

## Project Structure

```text
github-copilot-training/
├── .ruff.toml                    # Ruff linting/formatting config
├── uv.lock                       # Locked dependencies for reproducibility
├── pyproject.toml                # Project metadata and dependencies
├── README.md                     # This file
├── src/
│   └── flight_delays_api/     # Main application
│       ├── __init__.py           # FastAPI app setup
│       ├── models/               # Pydantic models
│       └── routers/              # API endpoints
├── tests/                        # Test suite
└── data/                         # Sample data
```
## Quick Start

### Prerequisites

- Python 3.12 or higher
- Package manager [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Command runner [task](https://taskfile.dev/)
- GitHub Copilot in your IDE of choice (e.g. [GitHub Copilot - Your AI Pair Programmer](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer) for PyCharm), or alternatively the [GitHub Copilot CLI](https://github.com/features/copilot/cli)

### Setup and Run

Install dependencies:
```bash
task setup
```

Start the development server:
```bash
task run
```

The API will be available at `http://localhost:8000` with Swagger UI at `http://localhost:8000/docs`.

### Tasks
[Task](https://taskfile.dev/) is used to run commands irrespective of the underlying OS.

You can see the list of available commands by running:
```bash
task
```

## Exercises

### LAB 1: Vibe Coding

**Context:** We are going to build an application that displays flight delays. You are given an initial Python project that starts successfully but does not yet expose the required REST endpoints. Familiarize yourself with the repo using GitHub Copilot and implement the endpoints described below.

**Task:** Implement the following endpoints:
- `GET /delays` → returns 200 OK or 404 Not Found
- `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

### LAB 2: Increasing Accuracy in a Probabilistic Solution Space

**Context:** In this exercise, you will configure your project so GitHub Copilot produces more consistent and accurate outputs. Your goal is to reduce ambiguity and improve output quality.

**Task:**
- Create a repository instruction file defining general architecture conventions
- Add path-specific instruction files for python and testing
- Implement the same endpoints again:
- `GET /delays` → returns 200 OK or 404 Not Found
- `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

**Files to create:**
- `.github/copilot-instructions.md`
- `.github/instructions/rest.md`
- `.github/instructions/tests.md`

### LAB 3: Agentic Workflow

**Context:** So far you've used Copilot to generate code directly. Now you will enforce an agentic workflow that separates refinement, planning, and implementation to improve quality and predictability.

**Task:**
- Prepare agents for refine → plan → implement in `.github/agents/`
- Prepare a directory `.github/handoff/` to store handoff documents
- Implement the same endpoints again using the workflow:
- `GET /delays` → returns 200 OK or 404 Not Found
- `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

**Files to create:**
- `.github/agents/refine.md`
- `.github/agents/plan.md`
- `.github/agents/implement.md`