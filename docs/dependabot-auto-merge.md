# Dependabot Auto-Merge Workflow

## Summary

Use `gabezurita/.github/.github/workflows/dependabot-auto-merge.yml@main` to auto-merge minor and patch Dependabot PRs without checking out untrusted PR code in a privileged workflow. Pair it with a `pull_request` CI workflow, a `main` ruleset requiring that CI check, a `weekly` `dependabot.yml` schedule, and repository-level Dependabot alerts and security updates.

## Security architecture

GitHub Actions splits CI verification from merge privileges across two triggers:

1. **Test on `pull_request` (unprivileged):** Each repository's CI workflow (`ci.yml` or equivalent) checks out the PR merge commit with `contents: read` and no write or deployment secrets exposed to package install scripts.
2. **Merge on `pull_request_target` (no checkout):** The caller delegates to `dependabot-auto-merge.yml` without running `actions/checkout`, preventing PR-controlled lockfiles or install scripts from executing with `pull-requests: write` or `contents: write`.
3. **Semver gating:** `dependabot/fetch-metadata@v3` inspects the PR before any merge action. Updates with an empty `update-type` or `version-update:semver-major` exit cleanly and remain open for human review.
4. **Ruleset enforcement:** The workflow calls `gh pr merge --auto` (falling back to an immediate `gh pr merge` only when `mergeStateStatus` is `CLEAN` or `HAS_HOOKS`). A `main` ruleset requiring the `pull_request` CI check guarantees GitHub blocks merging until tests pass.

## Weekly version updates vs. event-driven security updates

| Mechanism | Trigger | Scope | Controlled by |
| --- | --- | --- | --- |
| Dependabot version updates | Scheduled (`weekly`) | All new package versions | `.github/dependabot.yml` (`schedule.interval`) |
| Dependabot security updates | Event-driven (immediate on advisory) | Known vulnerable dependencies only | Repo settings (`vulnerability-alerts` and `automated-security-fixes`) |

- `schedule.interval` in `.github/dependabot.yml` controls routine version bumps only; switching from `daily` to `weekly` does not delay CVE fixes.
- Security updates open immediately when a GitHub Advisory is published and still flow through the auto-merge workflow (`!= version-update:semver-major`).
- Running routine auto-merged bumps `daily` pulls newly published npm and PyPI releases within hours, before registries or maintainers yank compromised versions. A `weekly` schedule narrows that supply-chain window and cuts CI and notification volume roughly sevenfold.

## Repository onboarding

### 1. Add the caller workflow

Standard caller (`.github/workflows/dependabot-auto-merge.yml`):

```yaml
name: Dependabot Auto-merge

on:
  pull_request_target:
    types: [opened, synchronize, reopened]

permissions:
  pull-requests: write
  contents: write

jobs:
  auto-merge:
    if: ${{ github.actor == 'dependabot[bot]' }}
    uses: gabezurita/.github/.github/workflows/dependabot-auto-merge.yml@main
```

Caller with a GitHub App token (for repositories whose rulesets require an app or non-`github-actions[bot]` approval/merge actor):

```yaml
jobs:
  auto-merge:
    if: ${{ github.actor == 'dependabot[bot]' }}
    uses: gabezurita/.github/.github/workflows/dependabot-auto-merge.yml@main
    with:
      use-app-token: true
    secrets:
      app-id: ${{ secrets.BOT_APP_ID }}
      app-private-key: ${{ secrets.BOT_PRIVATE_KEY }}
```

### 2. Workflow inputs and secrets

| Parameter | Kind | Default | Purpose |
| --- | --- | --- | --- |
| `approve` | input (`boolean`) | `true` | Attempts `gh pr review --approve` before merging |
| `merge-method` | input (`string`) | `squash` | Merge strategy: `squash`, `merge`, or `rebase` |
| `use-app-token` | input (`boolean`) | `false` | Generates a token from `app-id` and `app-private-key` via `actions/create-github-app-token@v3` |
| `app-id` | secret | optional | GitHub App ID when `use-app-token` is `true` |
| `app-private-key` | secret | optional | GitHub App private key when `use-app-token` is `true` |

### 3. Repository prerequisites

Enable these repository settings before relying on auto-merge:

1. **Auto-merge enabled:** `allow_auto_merge: true` (`gh api -X PATCH repos/{owner}/{repo} -F allow_auto_merge=true`).
2. **Required CI status check on `main`:** Active branch ruleset requiring the exact `pull_request` job name(s) from GitHub Actions (`integration_id: 15368`). Without a required status check, `gh pr merge --auto` or a clean fallback can merge before CI completes.
3. **Dependabot alerts and security updates:** Enable `PUT /repos/{owner}/{repo}/vulnerability-alerts` and `PUT /repos/{owner}/{repo}/automated-security-fixes`.
4. **Weekly version schedule:** Set `schedule.interval: weekly` in `.github/dependabot.yml`.
