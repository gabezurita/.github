# gabezurita/.github

Shared GitHub Actions workflows and repository defaults for `gabezurita` repositories.

## Reusable Workflows

### `dependabot-auto-merge.yml`

Called on `pull_request_target` by downstream repositories to:

1. Verify `github.actor == 'dependabot[bot]'` without checking out untrusted PR code.
2. Fetch Dependabot metadata (`dependabot/fetch-metadata@v3`) and block major version bumps (`version-update:semver-major`).
3. Optionally approve the PR and enable auto-merge (`gh pr merge --auto`), relying on each repository's `main` ruleset required status checks as the merge gate.
