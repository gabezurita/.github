# Dependabot Auto-Merge Workflow

The workflow approves eligible Dependabot PRs when approval is enabled and asks GitHub to merge them when the calling repository’s requirements pass.

## How the merge decision works

1. The caller tests PR code on `pull_request` with read access. A separate `pull_request_target` job has merge permissions and reads Dependabot metadata without checking out the PR.
2. Only `version-update:semver-patch` and `version-update:semver-minor` qualify. For any other value, including missing metadata, the workflow records the skip in the run summary and leaves the PR open for review.
3. GitHub enforces the target branch’s required checks and reviews. The workflow requests auto-merge. If that request fails, it tries a direct merge only when GitHub reports `CLEAN` or `HAS_HOOKS`. Configure required checks before enabling the caller, and ensure the merge actor is subject to the rules.

## Update schedule

Set routine version updates to weekly in `.github/dependabot.yml`. Dependabot security updates are triggered separately by eligible alerts when security updates are enabled. Both kinds of PR use the same merge policy.

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
2. **Required CI status check on `main`:** Active branch ruleset requiring the exact `pull_request` job name(s) from GitHub Actions (`integration_id: 15368`). Verify on an ordinary PR that the merge box shows the required job and blocks merging while it is pending.
3. **Dependabot alerts and security updates:** Enable `PUT /repos/{owner}/{repo}/vulnerability-alerts` and `PUT /repos/{owner}/{repo}/automated-security-fixes`.
4. **Weekly version schedule:** Set `schedule.interval: weekly` in `.github/dependabot.yml`.

## Troubleshooting

- **A run succeeded and the PR is still open.** Check the run summary for the update type and dependency names. A skipped update needs manual review. For an eligible update, check the PR’s merge box for outstanding requirements.
- **Approval failed.** Open the “Approve and enable auto-merge” step log. Approval is best effort, so the workflow still requests auto-merge. If the branch requires a review, check the merge box and obtain an eligible review. If using the default token, check the caller’s Actions setting for permission to approve pull requests.
- **A required check stays pending.** Compare the exact job name and source app in the target branch’s active ruleset with the checks on the PR’s latest commit. Confirm that CI runs on `pull_request` for that branch and that path filters allow it to start.

### Pause or resume auto-merge

Run these commands from the calling repository, using its caller workflow filename:

1. Disable new runs with `gh workflow disable dependabot-auto-merge.yml`. Inspect the workflow’s Actions page and cancel queued or running jobs that could still request a merge.
2. Find open PRs with auto-merge enabled using `gh pr list --state open --limit 1000 --json number,autoMergeRequest --jq '.[] | select(.autoMergeRequest != null) | .number'`. Inspect the PRs you intend to stop and run `gh pr merge <number> --disable-auto` for each. Confirm in the merge box that auto-merge is off. If the repository uses a merge queue, also check the queue and remove the PR if it has already entered.
3. Before resuming, verify that CI reports the required job on a recent PR and that the active branch rule requires it. Run `gh workflow enable dependabot-auto-merge.yml` and check the next eligible PR’s run summary and merge box.
