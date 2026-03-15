# Github Copilot Training

This training repo contains an API for managing flight delay information.

## Project Structure

```text
github-copilot-training/
├── .ruff.toml                    # Ruff linting/formatting config
├── Taskfile.yml                  # Task runner commands
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
The exercises will be available during the training.