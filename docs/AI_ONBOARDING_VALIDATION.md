# AI Onboarding Validation

## Purpose

Define validation for this documentation factory and for target repositories that
adopt an AI onboarding package.

## This Repository

Run:

```shell
python scripts/validate_docs.py
git diff --check
```

Current validation scope:

```text
Documentation presence:
README links:
AGENTS first-read contract:
Prompt launcher presence:
Status words:
Whitespace:
```

No build, package, lint, typecheck, or unit-test framework exists in this repo.
Those statuses are `NOT_REQUIRED` until code beyond the docs validator is added.

## Target Repositories

Discover validation from repo-owned files:

```text
AGENTS.md
README*
CONTRIBUTING*
DEVELOPMENT*
docs/
.github/workflows/
.gitlab-ci.yml
Makefile
justfile
Taskfile.yml
package.json
pyproject.toml
tox.ini
noxfile.py
pytest.ini
Cargo.toml
go.mod
pom.xml
build.gradle
```

Classify validation:

```text
format
lint
typecheck
unit tests
integration tests
build/package
security scan
secret scan
repository hygiene
domain-specific validation
local full validation
CI-only validation
external-system validation
```

## Minimum Checks

Always run when Git is available:

```shell
git diff --check
```

Run diagnostics when present:

```shell
python scripts/diagnostics/repo_doctor.py
python scripts/diagnostics/ai_context_report.py --format both
```

Run diagnostic tests when the target repo has a compatible test pattern.

## Gate Coverage Report

Report:

```text
Changed files:
Gate names:
Gate scope:
High-risk production files:
Excluded production files:
Threshold changes:
Scope changes:
Commands run:
Command results:
```

Missing gate coverage proof means validation is `INCOMPLETE`.

## GitHub Governance Validation

Report separately:

```text
Repo config: PASS|FAIL
Caller workflow: PASS|FAIL
Protected branch/ruleset: PASS|FAIL
Required checks: PASS|FAIL
Canary PR: PASS|FAIL
Repo GitHub governance: PASS|FAIL
```

`Repo GitHub governance: PASS` requires current live proof for every line. Local
files, waivers, approvals, allowlists, and known-debt records do not convert a
failure to a pass.
