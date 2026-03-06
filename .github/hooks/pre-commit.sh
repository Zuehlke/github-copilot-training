#!/bin/sh

set -u

if ! command -v task >/dev/null 2>&1; then
  echo "Error: 'task' is not on PATH. Install it from https://taskfile.dev and re-run your commit."
  exit 1
fi

echo "Running pre-commit checks..."

if ! task format; then
  echo "Formatting failed. Run 'task format' manually to fix formatting issues."
  exit 1
fi

if ! task lint; then
  echo "Lint check failed. Run 'task lint-fix' to fix lint issues."
  exit 1
fi

if ! task test; then
  echo "Tests failed. Fix failing tests before committing."
  exit 1
fi

echo "Pre-commit checks passed. Proceeding with commit."
exit 0

