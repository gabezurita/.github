# Repository Agent Instructions

Generic across repositories. Repository-specific rules belong in `.agents/REPO_RULES.md`.

## Agent Context

At session start, read `.agents/README.md` for context hierarchy and `.agents/LEARNING_LOG.md` for verified discoveries. Keep discoveries in their owning repository and follow the guide when promoting them into durable documentation.

## Releases

A release is one semver tag for what has shipped on `main`, cut when you deploy. It is not one tag per commit on a feature branch.

Pull requests squash onto `main`, so a merged pull request is one commit. `npm run deploy` from `main` looks at every commit since the last tag and moves the number once:

- `feat` raises the minor version, so `2.1.0` becomes `2.2.0`.
- `fix` and `perf` raise the patch version.
- A `!` after the type, or a `BREAKING CHANGE` footer, raises the major version.
- `docs` and `chore` do not raise it.

When several of those commits are waiting, the number still moves once, by the highest rule that applies.

## Repository Rules

@.agents/REPO_RULES.md
