# Shared GitHub workflows and templates

This is where I keep the tools and conventions I use to maintain my projects on GitHub. You’ll find issue forms, a pull request template, a guide to my review comments, and a reusable workflow for dependency updates.

## Dependency updates

The [Dependabot auto-merge workflow](.github/workflows/dependabot-auto-merge.yml) asks GitHub to merge patch and minor updates once the calling repository’s required checks pass. The caller tests PR code on `pull_request`. A separate `pull_request_target` job reads Dependabot metadata and requests the merge without checking out PR code.

The [workflow guide](docs/dependabot-auto-merge.md) covers setup, required checks, and how to stop a pending merge.

## Community templates

GitHub supplies these defaults to repositories that inherit them:

- [Task form](.github/ISSUE_TEMPLATE/task.yml) for scope and acceptance criteria.
- [Bug form](.github/ISSUE_TEMPLATE/bug.yml) for expected behavior, reproduction steps, and evidence. [Blank issues](.github/ISSUE_TEMPLATE/config.yml) are also enabled.
- [Pull request template](.github/PULL_REQUEST_TEMPLATE.md) for the summary, verification, and follow-ups.

The [code review legend](docs/code-review-legend.md) explains priorities, emoji, verdicts, and review footers.
