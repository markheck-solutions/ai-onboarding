# AGENTS.md

This is the first-read file for future AI agents working in this repository.

## Start Here

1. Read this file.
2. Read `README.md`.
3. Read `docs/AI_REPO_ONBOARDING_FACTORY.md`.
4. Read `docs/AI_ONBOARDING_PACKAGE_SPEC.md`.
5. Read `docs/AI_ONBOARDING_DIAGNOSTICS_SPEC.md`.
6. Read `docs/AI_ONBOARDING_VALIDATION.md`.
7. Read `docs/AI_ONBOARDING_PROMPTS.md`.
8. Read `docs/AI_ONBOARDING_GOVERNANCE.md`.
9. Use `docs/AI_ONBOARDING_HANDOFF_TEMPLATE.md` for handoffs.

## What This Repo Does

This repository documents how to add an AI self-orientation layer to any
repository. The output must be repo-owned, repo-agnostic in design, and based on
current files and commands in the target repository.

## Hard Safety Rules

- Trust but verify. Read current files from disk.
- Preserve dirty worktrees.
- Do not reset, revert, delete, rename, or overwrite unrelated files.
- Do not infer repo purpose, validation, CI, branch protection, deployments,
  database behavior, or GitHub governance from chat history or local docs alone.
- Stop when evidence is missing, stale, contradictory, unavailable, or unsafe.
- Use status words exactly: `PASS`, `FAIL`, `INCOMPLETE`, `NOT_FOUND`,
  `NOT_RUN`, `NOT_REQUIRED`.

## Documentation Map

- `docs/AI_REPO_ONBOARDING_FACTORY.md`: end-to-end factory process.
- `docs/AI_ONBOARDING_PACKAGE_SPEC.md`: required output package for target repos.
- `docs/AI_ONBOARDING_DIAGNOSTICS_SPEC.md`: diagnostic script behavior and output.
- `docs/AI_ONBOARDING_VALIDATION.md`: local and remote validation rules.
- `docs/AI_ONBOARDING_PROMPTS.md`: starter prompts for future AI sessions.
- `docs/AI_ONBOARDING_GOVERNANCE.md`: supportability and GitHub proof rules.
- `docs/AI_ONBOARDING_HANDOFF_TEMPLATE.md`: restart-safe handoff format.
- `prompts/repo_agnostic_onboarding_prompt.md`: read-only onboarding launcher.
- `prompts/repo_agnostic_plan_execution_prompt.md`: scoped plan execution launcher.

## Before Editing

Report:

```text
Repo root:
Branch:
Remote URL:
Dirty worktree:
Current tracked files:
Required files found:
Required files missing:
Planned changes:
```

If the repo is not a Git repository, report Git metadata as `NOT_FOUND` and do
not initialize Git unless the owner explicitly scopes it.

## Validation

Run after edits:

```shell
python scripts/validate_docs.py
git diff --check
```

If a future change adds repo-native test, lint, build, or CI validation, update
`docs/AI_ONBOARDING_VALIDATION.md` and this file.

## GitHub Governance

Report GitHub governance separately:

```text
Repo config: PASS|FAIL
Caller workflow: PASS|FAIL
Protected branch/ruleset: PASS|FAIL
Required checks: PASS|FAIL
Canary PR: PASS|FAIL
Repo GitHub governance: PASS|FAIL
```

`Repo GitHub governance: PASS` requires current live proof for every line above.
Local files alone are not proof.

## Stop Conditions

Stop and report exact blocker when:

- Required source files or prompts are missing.
- Git root or remote does not match the requested repo.
- Dirty files overlap needed edits and are not owned by the current task.
- Validation command fails.
- GitHub proof is requested but live proof is unavailable.
- Any instruction would require destructive or unrelated changes.
