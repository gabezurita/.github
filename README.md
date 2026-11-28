# Shared GitHub workflows and templates

The Dependabot workflow requests auto-merge for patch and minor updates. The calling repository runs its own CI on `pull_request` and enforces required checks through its branch rules. A separate `pull_request_target` workflow reads Dependabot metadata and requests the merge without checking out PR code.

The [workflow guide](docs/dependabot-auto-merge.md) covers setup, required checks, and how to stop a pending merge.

## Community templates

GitHub supplies these defaults to repositories that inherit them:

- [Task form](.github/ISSUE_TEMPLATE/task.yml) for scope and acceptance criteria.
- [Bug form](.github/ISSUE_TEMPLATE/bug.yml) for expected behavior, reproduction steps, and evidence. [Blank issues](.github/ISSUE_TEMPLATE/config.yml) are also enabled.
- [Pull request template](.github/PULL_REQUEST_TEMPLATE.md) for the summary, verification, and follow-ups.

The [code review legend](docs/code-review-legend.md) explains priorities, emoji, verdicts, and review footers.
