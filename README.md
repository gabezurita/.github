# gabezurita/.github

Shared GitHub Actions workflows and repository defaults for `gabezurita` repositories.

## Reusable Workflows

### `dependabot-auto-merge.yml`

Called on `pull_request_target` by downstream repositories to auto-merge non-major Dependabot PRs behind `pull_request` CI and `main` ruleset checks. See [docs/dependabot-auto-merge.md](docs/dependabot-auto-merge.md) for caller snippets, repository prerequisites, and the weekly vs. event-driven security update policy.
