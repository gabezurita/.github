# Repository Rules: .github

<!-- Repository-specific rules, architecture, constraints, and test commands go here. -->

## Standard Tooling Conventions

Follow the machine-wide tooling standards unless this repository specifies an explicit override:

- **Universal Baseline**: Respect `.editorconfig` (UTF-8, LF, 2-space indent default, 4-space indent for Python, trim trailing whitespace).
- **Python**: Use **Ruff** for formatting and linting (`[tool.ruff]` in `pyproject.toml` or `ruff.toml`) and Astral's `ruff-pre-commit` in `.pre-commit-config.yaml`. Use **Mypy** for static typing.
- **JavaScript / TypeScript / Web**: Use **Prettier** for formatting (`.prettierrc`) and **ESLint** for diagnostics (`.eslintrc.js` or `eslint.config.js`).
- **Shell**: Use **ShellCheck** for linting and **shfmt** for formatting.
- **Separation of Concerns**: Editor settings define IDE behavior; repository configs govern project style and CI verification. Local commands (`make lint`, `make format`, pre-commit hooks) must match CI checks.

## Test coverage

Measure coverage when the repository is scaffolded:

```bash
~/.agents/scripts/check-repo-layout --apply --repo <name> --lang python
```

`--lang` is `python`, `typescript`, `go`, or `rust`. The starter adds one tested function and `scripts/check-coverage.sh`, and the run fails under 90% coverage. Python uses pytest and pytest-cov. TypeScript uses Vitest with `@vitest/coverage-v8`. Go uses `go test -cover`. Rust uses `cargo llvm-cov`. An existing project manifest is left unchanged. The tool choice lives in gab0-system `docs/architecture/code-quality.md`.
