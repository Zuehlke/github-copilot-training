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
│   └── flight_delays_api/        # Main application
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

**Task:** Implement the following endpoint:
- `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

### LAB 2: Prompt Template

**Context:** You will generate project documentation for this repository using the prepared `create-project-documentation` prompt template.

**Task:** Create the documentation in chat using `/create-project-documentation`.

### LAB 3: Setup IDE to increase the likelihood of acceptable output

**Context:** In this exercise, you will configure your project so GitHub Copilot produces more consistent and probabilistic outputs. Your goal is to reduce ambiguity and improve output quality.

**Task:**
- Create a repository instruction file defining general behavior and constraints for Copilot in this repository
- Add path-specific instruction files for python and testing
- Implement the same endpoint again:
  - `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

**Files to create:**
- `.github/copilot-instructions.md`
- `.github/instructions/python.instructions.md`
- `.github/instructions/testing.instructions.md`

### LAB 4: Agentic Workflow

**Context:** So far you've used Copilot to generate code directly. Now you will enforce an agentic workflow that separates refinement, planning, and implementation to improve quality and predictability.

**Task:**
- Prepare agents for refine → plan → implement in `.github/agents/`
- You can reuse the existing handoff-writing and code-and-quality-testing skills in `.github/skills/`.
- Implement the same endpoint again using the workflow:
  - `GET /delays/?airline_code=AA&limit=50` → returns 200 OK or 404 Not Found

**Files to create:**
- `.github/agents/refine.agent.md`
- `.github/agents/plan.agent.md`
- `.github/agents/implement.agent.md`