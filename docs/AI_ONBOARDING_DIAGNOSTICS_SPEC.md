# AI Onboarding Diagnostics Spec

## Purpose

Define optional diagnostic scripts for target repos that need machine-readable
and human-readable AI orientation.

## Required Scripts

```text
scripts/diagnostics/repo_doctor.py
scripts/diagnostics/ai_context_report.py
```

Use the target repo runtime and dependency model. Keep diagnostics lightweight
and safe to run locally.

## `repo_doctor.py`

Required checks:

- repo root
- branch
- dirty worktree summary
- required docs presence
- required scripts presence
- quality gates presence
- key test files presence
- locally detectable governance config
- live GitHub governance status as `FAIL` unless current live proof exists
- overall summary

Required output shape:

```text
Repo doctor
Repo root:
Branch:
Dirty worktree:
Section summary:
- required_docs:
- required_scripts:
- quality_gates:
- key_test_files:
- known_governance_statuses:
Overall:
Governance:
- repo_config:
- caller_workflow:
- protected_branch_or_ruleset:
- required_checks:
- canary_pr:
- repo_github_governance:
```

Rules:

- Dirty tracked files make orientation `INCOMPLETE`.
- Missing required docs make required docs `FAIL`.
- Missing optional proof is `INCOMPLETE`.
- Local files cannot prove branch protection, required checks, deployments,
  databases, external systems, or live GitHub governance.

## `ai_context_report.py`

Required output:

- repo root
- branch
- dirty file count
- project name/version/description when detectable
- repo purpose
- first-read docs
- missing first-read docs
- danger areas
- validation commands
- stop rules
- status-reporting fields
- JSON payload for machine use

Supported commands:

```shell
python scripts/diagnostics/ai_context_report.py
python scripts/diagnostics/ai_context_report.py --format text
python scripts/diagnostics/ai_context_report.py --format json
python scripts/diagnostics/ai_context_report.py --format both
```

## Diagnostic Tests

Add tests when the target repo already has a compatible test pattern.

Required coverage:

- diagnostic scripts exist
- scripts execute from repo root
- expected headings appear
- status keys appear
- JSON mode parses
- missing generated docs are detected
- governance stays `FAIL` or `INCOMPLETE` when live proof is absent

Do not add a new test framework only for diagnostics unless the owner scopes it.
