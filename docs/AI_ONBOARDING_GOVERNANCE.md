# AI Onboarding Governance

## Purpose

Define proof rules for AI onboarding work.

## Agent Behavior Governance

- Read applicable repo contracts before editing.
- Read the active supportability standard when the task involves
  supportability, refactor, package/runtime, architecture cleanup, test
  hardening, repo maintainability, or completion gates.
- Treat required evidence as pass/fail.
- Do not claim completion when evidence is missing.
- Preserve owner-declared local infrastructure.
- Do not change branch protection, repository settings, secrets, releases,
  deployments, databases, or external systems unless explicitly scoped.

## Status Words

```text
PASS          current evidence proves the item
FAIL          current evidence proves the item is broken or unsafe
INCOMPLETE    proof is missing, stale, contradictory, unavailable, blocked, or out of scope
NOT_FOUND     expected file, command, or tool was not found
NOT_RUN       intentionally not run
NOT_REQUIRED  not required for this repo or task
```

## GitHub Enforcement Governance

Agent behavior governance is not GitHub enforcement. A repository is not
governed by GitHub checks until current live evidence proves the protected merge
path is active.

Required status split:

```text
Repo config: PASS|FAIL
Caller workflow: PASS|FAIL
Protected branch/ruleset: PASS|FAIL
Required checks: PASS|FAIL
Canary PR: PASS|FAIL
Repo GitHub governance: PASS|FAIL
```

`Repo GitHub governance: PASS` requires:

- local governance config exists and validates
- adopted supportability standard exists at the configured source and matches
  the configured hash
- caller workflow invokes reusable governance workflows at an exact commit SHA
- protected branch or ruleset requires governance checks before merge
- harmless canary pull request proves checks attach, run, and merge only through
  the protected pull request path

Missing config, workflow, protected branch or ruleset, required checks, artifact
evidence, receipt evidence, or canary proof is `FAIL`.

Waivers, approvals, allowlists, known debt, baseline debt, and override metadata
are evidence only. They never convert `FAIL` to `PASS`.

## SQL Supportability Governance

For any repository with SQL-like sources, require separate SQL supportability
status:

```text
Gate implementation: PASS|FAIL
Repo SQL supportability: PASS|FAIL
SQL behavior proof: PASS|FAIL|NOT_REQUIRED
```

Missing, non-blocking, unscanned, unresolved, unparsable, or unverifiable SQL is
`FAIL` until the target repo has a blocking repository-local gate and behavior
proof where required.

`SQL behavior proof: NOT_REQUIRED` is allowed only when current evidence proves
executable SQL, canonical SQL, execution-sink hash, role metadata hash, and
dependency graph hash match the prior baseline.
