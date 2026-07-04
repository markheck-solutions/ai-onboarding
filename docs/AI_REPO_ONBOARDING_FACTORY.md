# AI Repo Onboarding Factory

## Purpose

Create a repo-owned AI onboarding layer for any repository. The layer teaches
future AI sessions how to orient from current repo files and commands without
chat history or owner technical recovery.

## Core Rule

Trust but verify. Repository files and current command output are the source of
truth. Missing proof is `INCOMPLETE`, not success.

## Factory Flow

### Phase 0: Safety Preflight

Run from the target repo:

```shell
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git ls-files
```

Report repo root, branch, remote URL, dirty worktree, and current files before
editing.

If the target path is not a Git repository, report Git metadata as `NOT_FOUND`.
Do not initialize, clone, reset, or overwrite without explicit owner scope.

### Phase 1: Read Current Repo Files

Read first-read and control files when present:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
README.md
README.rst
README.txt
CONTRIBUTING.md
DEVELOPMENT.md
docs/
.github/
.gitlab/
scripts/
tools/
tests/
```

Discover from repo-owned evidence:

- repo purpose
- primary workflows
- package/runtime entry points
- validation commands
- CI commands
- dangerous paths
- external systems
- governance rules
- known gaps
- high-risk production files
- stop conditions

### Phase 2: Classify Missing Onboarding Infrastructure

Report:

```text
First-read docs:
Task routing docs:
Change safety docs:
Validation matrix:
Known risk docs:
Context index:
Handoff template:
Diagnostics:
Diagnostic tests:
GitHub governance:
```

Use `PASS`, `FAIL`, `INCOMPLETE`, `NOT_FOUND`, `NOT_RUN`, or `NOT_REQUIRED`.

### Phase 3: Build Repo-Owned Package

Create the package defined in `AI_ONBOARDING_PACKAGE_SPEC.md`. Keep names
descriptive and repo-neutral. Put target-repo-specific facts only in the target
repo package, backed by current disk reads and command output.

### Phase 4: Add Diagnostics

Add diagnostics only when safe for the target repo. Diagnostics must read current
state and report missing proof as `INCOMPLETE` or `FAIL`; they must not make
remote, CI, deployment, database, or governance claims from local files alone.

### Phase 5: Validate

Run target repo validation discovered from repo-owned files. At minimum, run:

```shell
git diff --check
```

When diagnostics are created, run them. When diagnostic tests are supported by
the target repo, run them. Report every skipped or missing gate.

### Phase 6: Handoff

Write a restart-safe handoff using `AI_ONBOARDING_HANDOFF_TEMPLATE.md`. Include
exact repo root, branch, commit, files read, files changed, validation output,
gaps, and next command.

## Required Final Status Split

```text
Onboarding docs:
Diagnostic scripts:
Diagnostic tests:
Local validation:
CI validation:
External systems:
Repo GitHub governance:
```
