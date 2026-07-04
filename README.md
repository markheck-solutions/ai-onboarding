# AI Onboarding Documentation Factory

This repository owns a repo-agnostic documentation system for adding an AI
self-orientation layer to any repository.

Goal: future AI sessions must be able to orient from current repo files and
commands without chat history or owner technical recovery.

## Start Here

1. Read [AGENTS.md](AGENTS.md).
2. Read [docs/AI_REPO_ONBOARDING_FACTORY.md](docs/AI_REPO_ONBOARDING_FACTORY.md).
3. Read [docs/AI_ONBOARDING_PACKAGE_SPEC.md](docs/AI_ONBOARDING_PACKAGE_SPEC.md).
4. Read [docs/AI_ONBOARDING_DIAGNOSTICS_SPEC.md](docs/AI_ONBOARDING_DIAGNOSTICS_SPEC.md).
5. Read [docs/AI_ONBOARDING_VALIDATION.md](docs/AI_ONBOARDING_VALIDATION.md).
6. Read [docs/AI_ONBOARDING_PROMPTS.md](docs/AI_ONBOARDING_PROMPTS.md).
7. Read [docs/AI_ONBOARDING_GOVERNANCE.md](docs/AI_ONBOARDING_GOVERNANCE.md).
8. Use [docs/AI_ONBOARDING_HANDOFF_TEMPLATE.md](docs/AI_ONBOARDING_HANDOFF_TEMPLATE.md)
   for restart-safe handoffs.

## Prompt Files

- [prompts/repo_agnostic_onboarding_prompt.md](prompts/repo_agnostic_onboarding_prompt.md):
  read-only repository orientation.
- [prompts/repo_agnostic_plan_execution_prompt.md](prompts/repo_agnostic_plan_execution_prompt.md):
  onboarding plus safe plan execution.

Use the prompt files as launcher artifacts. Use the `docs/` files as the
maintained specification for the onboarding package.

## What This Repo Provides

- A factory process for building repo-owned AI onboarding layers.
- A package specification for first-read docs, diagnostics, validation, and
  handoff artifacts.
- A diagnostics specification for repo status, file discovery, validation
  discovery, and governance status reporting.
- Prompt templates for read-only onboarding and scoped plan execution.
- Governance rules for evidence-first claims and GitHub enforcement proof.

## Status Words

Use these exact status words in docs, diagnostics, and reports:

```text
PASS
FAIL
INCOMPLETE
NOT_FOUND
NOT_RUN
NOT_REQUIRED
```

## Local Validation

Run:

```shell
python scripts/validate_docs.py
git diff --check
```

No GitHub governance claim is valid from local files alone. See
[docs/AI_ONBOARDING_GOVERNANCE.md](docs/AI_ONBOARDING_GOVERNANCE.md).
