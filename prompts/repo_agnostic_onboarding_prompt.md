# Repo-Agnostic Onboarding Prompt

## Activation

If asked to read this file, treat it as active instructions. Do not summarize it. Execute the onboarding workflow and return the required report.

Launcher:

```text
Read and execute the onboarding prompt at "<PATH_TO_THIS_FILE>". Do not summarize the file. Onboard to the current repository only. Do not edit files.
```

## Task

Onboard to the current repository. Do not edit files.

Use current disk reads and current command output as proof. The repository is the source of truth. Unknown facts stay unknown.

If a file, command, tool, workflow, diagnostic, or external proof path is unavailable, report it as `NOT_FOUND`, `NOT_RUN`, or `INCOMPLETE`.

## Step 1 — Resolve Repository Root

Start from the current working directory unless an explicit repository path is supplied.

Run:

```shell
git rev-parse --show-toplevel
git status --short --branch
```

If this is not a git repository, continue in read-only orientation mode and report `Git repository: NOT_FOUND`. Do not initialize git.

## Step 2 — Discover First-Read Files

Read files from disk if present:

```text
AGENTS.md
CLAUDE.md
GEMINI.md
README.md
README.rst
README.txt
CONTRIBUTING.md
DEVELOPMENT.md
docs/README.md
docs/index.md
docs/ai/AI_REPO_ONBOARDING.md
docs/ai/AI_TASK_ROUTING.md
docs/ai/AI_CHANGE_SAFETY_RULES.md
docs/ai/AI_VALIDATION_MATRIX.md
docs/ai/AI_KNOWN_RISKS.md
docs/ai/AI_CONTEXT_INDEX.md
```

Inspect these directories if present:

```text
docs/
docs/ai/
docs/runbooks/
docs/contracts/
docs/architecture/
.github/
.gitlab/
scripts/
tools/
tests/
```

Missing first-read files are not fatal during onboarding. They are repository-maturity evidence.

## Step 3 — Discover Repository Diagnostics

Run these only if the files exist:

```shell
python scripts/diagnostics/repo_doctor.py
python scripts/diagnostics/ai_context_report.py --format both
```

If the repository defines different diagnostics, discover them from repository-owned files such as README files, docs, Makefile, justfile, Taskfile.yml, package.json, pyproject.toml, Cargo.toml, go.mod, pom.xml, build.gradle, workflow files, or CI config.

Do not invent substitute diagnostics. If no diagnostics exist, report `Repository diagnostics: NOT_FOUND`.

## Step 4 — Discover Validation Commands

Find validation commands from repository-owned files only. Search README files, docs, workflow files, Makefile, justfile, Taskfile.yml, package.json, pyproject.toml, tox.ini, noxfile.py, pytest.ini, Cargo.toml, go.mod, pom.xml, and build.gradle.

Classify discovered validation into format, lint, typecheck, tests, build/package, security scan, secret scan, repository hygiene, domain-specific validation, local full validation, CI-only validation, and external-system validation.

Do not run heavyweight, destructive, external-system, release, deploy, credential, migration, browser, device, cloud, database, or live-production validation during onboarding.

Run only safe read-only or local inspection commands needed to orient.

## Hard Safety Rules

During onboarding:

- Do not edit files.
- Do not stage, commit, push, merge, rebase, reset, revert, delete, rename, or overwrite files.
- Do not install dependencies unless explicitly scoped by the owner.
- Do not run release, deploy, migration, production, credential, secret, browser-login, device-control, or external-system commands.
- Do not mutate generated outputs, user files, desktop files, cloud resources, databases, tickets, emails, messages, repository settings, or remote settings.
- Do not claim external governance, branch protection, required checks, deployments, releases, cloud access, database access, or production behavior from local files alone.
- If proof requires an external system, mark that proof `INCOMPLETE` unless the owner explicitly scopes live external verification.

## Status Words

Use exact status labels:

```text
PASS          current evidence proves the item
FAIL          current evidence proves the item is broken or unsafe
INCOMPLETE    proof is missing, blocked, unavailable, stale, contradictory, or out of scope
NOT_FOUND     expected file, command, or tool was not found
NOT_RUN       intentionally not run
NOT_REQUIRED  not required for this onboarding task
```

Do not collapse separate statuses into one vague result.

## Required Report Format

```text
Action
- Onboarded only. No edits.

Proof
- Repository root:
- Git repository:
- Branch:
- Dirty worktree:
- First-read files found:
- First-read files missing:
- Diagnostics found:
- Diagnostics run:
- Validation commands discovered:
- External proof not attempted:

Status Split
- Local repository orientation:
- Repository diagnostics:
- Validation discovery:
- External governance:
- External systems:
- Task-specific readiness: NOT_REQUIRED

Risk
- Caveats:
- Stop conditions:
- Missing onboarding infrastructure:

Next
- Waiting for scoped task.

Unknowns
- List exact unknowns, or `None`.
```
