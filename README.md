# gabezurita/.github

Shared GitHub Actions workflows and repository defaults for `gabezurita` repositories.

## Reusable Workflows

### `dependabot-auto-merge.yml`

Called on `pull_request_target` by downstream repositories to auto-merge non-major Dependabot PRs behind `pull_request` CI and `main` ruleset checks. See [docs/dependabot-auto-merge.md](docs/dependabot-auto-merge.md) for caller snippets, repository prerequisites, and the weekly vs. event-driven security update policy.

## Community Health Templates

Default Issue and Pull Request templates inherited by repositories without local overrides:

- `.github/ISSUE_TEMPLATE/task.yml` — lightweight bounded task contract (problem/context, scope/constraints, acceptance criteria).
- `.github/ISSUE_TEMPLATE/bug.yml` — concise bug report (repro, expected vs actual, evidence).
- `.github/ISSUE_TEMPLATE/config.yml` — keeps blank issues enabled.
- `.github/PULL_REQUEST_TEMPLATE.md` — evidence-first PR summary (`Summary`, `Verification`, `Risks / Follow-ups`, `Closes #`).

## Code Review Legend

[docs/code-review-legend.md](docs/code-review-legend.md) explains the priorities (`P1`–`P3`), emoji, verdicts and footer fields used in my PR reviews.
