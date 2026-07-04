# AI Onboarding Prompts

## Maintained Prompt Files

This repository also keeps paste-ready launcher files:

```text
prompts/repo_agnostic_onboarding_prompt.md
prompts/repo_agnostic_plan_execution_prompt.md
```

Keep these files aligned with the prompt patterns below.

## Read-Only Onboarding Prompt

Use when the task is orientation only.

```text
$governance

Goal:
Onboard to the current repository. Do not edit files.

Core rule:
Trust but verify. Use current disk reads and current command output as proof.
The repository is the source of truth.

Required actions:
1. Resolve repo root.
2. Report branch, remote URL, dirty worktree, and current tracked files.
3. Read first-read files from disk when present.
4. Inspect docs, scripts, tools, tests, and workflow directories when present.
5. Discover diagnostics and validation commands from repo-owned files.
6. Do not run destructive, release, deploy, migration, credential, or
   external-system commands.
7. Report missing proof as NOT_FOUND, NOT_RUN, or INCOMPLETE.

Final report:
- repo root
- branch
- dirty worktree
- files read
- diagnostics found
- diagnostics run
- validation discovered
- validation run
- external proof not attempted
- unresolved gaps
- next safe action
```

## Scoped Plan Execution Prompt

Use when the owner provides a plan and wants execution.

```text
$governance

Goal:
Execute the owner-provided plan safely in the current repository.

Plan source:
Use the provided path, issue, ticket, or pasted plan. If no plan source exists,
perform onboarding only, then stop.

Required phase 0:
1. Resolve repo root.
2. Report branch, remote URL, dirty worktree, and current tracked files.
3. Read first-read files from disk.
4. Run diagnostics only when present.
5. Discover validation from repo-owned files.

Required phase 1:
Report:
- goal
- in scope
- out of scope
- files/docs read
- task type
- expected changed areas
- expected external systems
- expected generated artifacts
- required validation
- proceed/stop decision

Rules:
- Preserve dirty worktree.
- Do not reset, revert, delete, rename, or overwrite unrelated files.
- Do not stage, commit, push, merge, rebase, tag, or release unless scoped.
- Stop on conflicting instructions.
- Do not claim GitHub governance, branch protection, CI, deployment, database,
  or external-system behavior without current live proof.

Final report:
- files changed
- files read
- validation commands and exact results
- unresolved gaps
- GitHub governance status split
- next safe action
```

## Status Words

```text
PASS          current evidence proves the item
FAIL          current evidence proves the item is broken or unsafe
INCOMPLETE    proof is missing, stale, contradictory, unavailable, blocked, or out of scope
NOT_FOUND     expected file, command, or tool was not found
NOT_RUN       intentionally not run
NOT_REQUIRED  not required for this repo or task
```
