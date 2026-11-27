# Code Review Legend

Each comment in my PR reviews starts with a priority and an emoji. The priority (`P1`, `P2` or `P3`) says whether the comment blocks the merge. The emoji says what kind of comment it is. A footer at the end of each review says how the review was done.

## Priorities

| Label | Meaning | What to do |
| --- | --- | --- |
| `P1` | Blocker: a bug, a security problem, a broken contract or a missing test on a critical path. | Fix it before merging, or reply if you think I'm wrong. |
| `P2` | Should fix in this PR, but doesn't block the merge on its own. | Fix it, or reply with why not. A follow-up issue is fine. |
| `P3` | Optional: a nit (a minor or stylistic point), an idea for later or a small cleanup. | Your call. No reply needed. |

Comments without a priority are questions, notes or praise.

## Emoji

The emoji come from the [Code Review Emoji Guide](https://github.com/erikthedeveloper/code-review-emoji-guide) by Erik Aybar. A comment can carry two: `:wrench: :question:` is a P2 change request phrased as a question.

| Emoji | Shortcode | Meaning | Priority |
| --- | --- | --- | --- |
| 🚫 | `:no_entry_sign:` | Blocker: must fix before merge | P1 |
| 🔧 | `:wrench:` | Change request: should fix, not strictly blocking | P2 |
| ♻️ | `:recycle:` | Refactor suggestion | P2 |
| ⛏ | `:pick:` | Nit: safe to ignore | P3 |
| 🌱 | `:seedling:` | Future consideration: out of scope, worth noting | P3 |
| 🏕 | `:camping:` | Boy-scout opportunity: leave the code cleaner than you found it | P3 |
| 🤔 | `:thinking:` | Thinking out loud: an alternative or a concern | None |
| ❓ | `:question:` | Question: please answer | None |
| 📝 | `:memo:` | Note: context only, no action needed | None |
| 📌 | `:pushpin:` | Follow-up: out of scope, worth an issue | None |
| 😃 | `:smiley:` | Praise | None |

## Verdicts

I approve once a change clearly improves the code, even if it isn't perfect, following [Google's code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html).

- Approve: the PR makes the code better and nothing blocks it. Any comments are suggestions.
- Comment: nothing blocks it, but some concerns are worth a look before merging.
- Request changes: at least one P1. A review never requests changes without one.

## Review footer

Each review ends with a line like this:

```text
Legend · Depth: light (docs-only change) · Lenses: single pass · Reviewer: claude-opus-5-5 · Commit: f6dca50 · Checks: source reads, CI status
```

| Field | Meaning |
| --- | --- |
| Depth | Light covers the full diff and the code around it, for small or low-risk changes. Heavy also checks each claim against the source, finds the real cause of any failing CI job and verifies every commented line before posting. Heavy is for security, auth, data, API, deployment, concurrency or broad changes. |
| Lenses | The specialist reviewers that read the diff, such as `ce-security-sentinel`, `ce-performance-oracle` or `ce-architecture-strategist` from the [Compound Engineering plugin](https://github.com/EveryInc/compound-engineering-plugin). Single pass means one reviewer covered everything. |
| Reviewer | The AI model that drafted the review. I check the findings and publish them myself. |
| Commit | The commit I reviewed. Anything pushed after it hasn't been reviewed. |
| Checks | What was actually run or read: tests, linters, CI status or source reads. Anything not listed wasn't checked. |
