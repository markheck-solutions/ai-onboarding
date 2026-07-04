# ai-onboarding

Repo-agnostic onboarding and plan-execution prompts for AI coding agents.

## Files

- `prompts/repo_agnostic_onboarding_prompt.md` — read-only repository orientation.
- `prompts/repo_agnostic_plan_execution_prompt.md` — onboarding plus safe plan execution.

## Usage

For onboarding only, paste the full onboarding prompt into a new agent chat.

For plan execution, paste the full plan-execution prompt into a new agent chat and provide the plan source.

These prompts are designed to discover repository rules from disk instead of relying on repo-specific assumptions.

## Status labels

- `PASS` — current evidence proves the item.
- `FAIL` — current evidence proves the item is broken or unsafe.
- `INCOMPLETE` — proof is missing, blocked, stale, contradictory, or out of scope.
- `NOT_FOUND` — expected file, command, or tool was not found.
- `NOT_RUN` — intentionally not run.
- `NOT_REQUIRED` — not required for the current task.
