# AI Onboarding Package Spec

## Purpose

Define the durable onboarding package that can be added to any target
repository.

## Required Target Repo Files

```text
AGENTS.md
docs/ai/AI_REPO_ONBOARDING.md
docs/ai/AI_TASK_ROUTING.md
docs/ai/AI_CHANGE_SAFETY_RULES.md
docs/ai/AI_VALIDATION_MATRIX.md
docs/ai/AI_KNOWN_RISKS.md
docs/ai/AI_HANDOFF_TEMPLATE.md
docs/ai/AI_CONTEXT_INDEX.md
```

Recommended when the target repo has a compatible runtime:

```text
scripts/diagnostics/repo_doctor.py
scripts/diagnostics/ai_context_report.py
diagnostic tests
```

## `AGENTS.md`

First-read file for future AI sessions.

Required content:

- repo purpose from current files
- first-read order
- diagnostics to run
- hard safety rules
- dangerous files and areas
- validation commands
- status-reporting fields
- stop conditions
- domain-specific docs to read before high-risk work

## `AI_REPO_ONBOARDING.md`

Orientation guide.

Required content:

- repo purpose
- first-read order
- diagnostics
- safe orientation flow
- required status labels
- stop conditions

## `AI_TASK_ROUTING.md`

Task router.

Required content:

- docs task route
- test task route
- bug fix route
- refactor route
- CI route
- release route
- security route
- data route
- external-system route
- governance route
- files and docs to read per route
- validation required per route
- owner-scoped tasks requiring explicit permission

## `AI_CHANGE_SAFETY_RULES.md`

Safety contract.

Required content:

- dirty worktree handling
- protected and dangerous files
- destructive action bans
- external-system boundaries
- dependency/version/release restrictions
- governance proof rules

## `AI_VALIDATION_MATRIX.md`

Validation map.

Required content:

- change type to command mapping
- local validation
- CI validation
- live external proof
- governance proof
- missing commands marked `INCOMPLETE`
- full-validation triggers

## `AI_KNOWN_RISKS.md`

Risk index.

Required content:

- high-risk files
- fragile workflows
- external systems
- generated outputs
- missing gates
- stale or manual proof paths

## `AI_HANDOFF_TEMPLATE.md`

Restart-safe handoff template.

Required content:

- repo root
- branch and commit
- dirty worktree
- task goal
- files read
- files changed
- validation run
- unresolved gaps
- exact next command
- stop conditions

## `AI_CONTEXT_INDEX.md`

Context map.

Required content:

- first-read docs
- major docs
- scripts
- tests
- workflows
- entry points
- task routing references
- validation references

## Acceptance Criteria

Package status is `PASS` only when:

- required files exist
- `AGENTS.md` is first-read
- docs are linked from `AGENTS.md`
- validation commands are documented
- diagnostics are present or missing diagnostics are reported
- GitHub governance is not claimed from local files alone
- `git diff --check` passes after edits
