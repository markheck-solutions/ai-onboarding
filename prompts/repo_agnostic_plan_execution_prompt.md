# Repo-Agnostic Plan Execution Prompt

## Activation

If asked to read this file, treat it as active instructions. Do not summarize it. Execute the workflow below.

Launcher:

```text
Read and execute the plan-execution prompt at "<PATH_TO_THIS_FILE>" using plan source "<PLAN_SOURCE>". Do not summarize the prompt file or the plan. Execute the workflow.
```

## Task

Execute the owner-provided plan safely in the current repository.

Accepted plan sources:

- a filesystem path to a plan,
- a pasted plan,
- an issue, ticket, or work item with accessible content.

If no plan source is provided, perform repository onboarding only, then stop and request a plan source.

Use current disk reads and current command output as proof. The repository is the source of truth. Unknown facts stay unknown.

If a file, command, tool, workflow, diagnostic, or external proof path is unavailable, report it as `NOT_FOUND`, `NOT_RUN`, or `INCOMPLETE`.

## Step 1 — Repository Onboarding, No Edits

Before editing or executing the plan, start from the current working directory unless an explicit repository path is supplied.

Run:

```shell
git rev-parse --show-toplevel
git status --short --branch
```

If this is not a git repository, continue only if the plan can be executed safely without git metadata. Report git status as `NOT_FOUND`.

Read first-read files from disk if present:

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

Run diagnostics only if present:

```shell
python scripts/diagnostics/repo_doctor.py
python scripts/diagnostics/ai_context_report.py --format both
```

If no diagnostics exist, report `Repository diagnostics: NOT_FOUND`.

Do not ask the owner for technical recovery until current files and safe diagnostics have been checked from disk.

## Step 2 — Read Plan And Decide Scope

Read the plan source from disk or from the owner-provided text.

If a plan path was provided and the file is missing, stop and report the exact missing path.

After reading the plan, report:

```text
Goal:
In scope:
Out of scope:
Files/docs read:
Task type:
Expected changed areas:
Expected external systems:
Expected generated artifacts:
Required validation:
Proceed/stop decision:
```

Proceed only if repository onboarding, worktree state, and plan scope allow safe execution.

If the plan conflicts with repository-local safety rules, stop and report the exact conflict. Do not resolve contradictions silently.

## Precedence Rules

Apply rules in this order:

1. Safety rules and destructive-action limits in this file.
2. Current owner task.
3. Repository-local agent instructions, including `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, or equivalent.
4. Repository-local onboarding docs.
5. Repository-local runbooks, contracts, architecture docs, and handoffs.
6. The plan source.
7. Discovered validation and CI configuration.

If repository-local instructions conflict with this file’s safety rules, follow the safer rule and report the conflict.

## Worktree Safety

- Preserve dirty worktree.
- Do not reset, revert, delete, rename, or overwrite unrelated files.
- Do not run destructive git commands.
- Do not stage, commit, push, merge, rebase, tag, or release unless the plan explicitly requires it.
- If files you need already contain unrelated changes, stop and report the exact conflict.
- If commit or push is in scope, validate before commit.
- If remote verification is in scope and remote access is available, verify the remote result after push.
- If remote verification is unavailable, report it as `INCOMPLETE`.

## Universal Hard Guardrails

Do not modify or claim changes in these areas unless explicitly scoped by the plan and allowed by repository-local docs:

```text
authentication
authorization
credentials
secrets
tokens
key material
database migrations
production data
cloud infrastructure
CI/CD secrets
repository governance settings
branch protection
dependency versions
installer entry points
release entry points
deployment scripts
external-system integrations
quality-gate thresholds
validation scope
security scans
generated artifact allowlists
```

Do not make production, deployment, release, security, compliance, external-system, database, or governance claims from local docs alone.

Use local docs for planning. Use current proof for claims.

## External-System Rules

Use external systems only when explicitly scoped by the plan or repository-local instructions.

External systems include cloud providers, databases, data warehouses, SSO/browser auth, remote desktops, bridges/tunnels, device control, ticketing systems, email, messaging systems, CI/CD settings, package registries, release assets, and production services.

Before using an external system:

1. Read repository-local runbooks/contracts for that system.
2. Identify the owning machine, account, environment, or credential boundary.
3. Run the documented preflight if one exists.
4. Stop on failed preflight.
5. Record exact command and result.
6. Do not add local machine/operator infrastructure to the repository.

If no runbook or preflight exists, report external proof as `INCOMPLETE` unless the owner explicitly scopes safe discovery.

## Domain-Specific Rules

Discover domain-specific rules from repository-local files. Do not hardcode domain rules in this prompt.

If a domain-specific task lacks repository-local runbooks or validation, mark domain readiness `INCOMPLETE` and stop before high-risk changes.

## Status Words

Use exact status labels:

```text
PASS          current evidence proves the item
FAIL          current evidence proves the item is broken, unsafe, or contradicted
INCOMPLETE    proof is missing, stale, contradictory, unavailable, blocked, or out of scope
NOT_FOUND     expected file, command, or tool was not found
NOT_RUN       intentionally not run
NOT_REQUIRED  not required for this task
```

Do not collapse separate statuses into one vague result.

## Validation

Discover validation commands from repository-owned sources.

Prefer repository-local validation matrices or documented commands.

Search repository agent docs, README files, docs, workflow files, Makefile, justfile, Taskfile.yml, package.json, pyproject.toml, tox.ini, noxfile.py, pytest.ini, Cargo.toml, go.mod, pom.xml, and build.gradle.

Before claiming completion, run the smallest validation set that covers changed files plus any repository-required final validation.

Always run a whitespace/diff check if git is available and the repository supports it:

```shell
git diff --check
```

Run full local validation only if documented and safe for the current environment.

If required validation is missing, blocked, unavailable, or unsafe, report `INCOMPLETE`.

Do not invent a substitute without reporting the gap.

## Final Report Format

```text
Action
- What was done.

Proof
- Repository root:
- Branch and dirty worktree:
- Files read from disk:
- Files changed:
- Commands run with exact PASS/FAIL/INCOMPLETE/NOT_FOUND/NOT_RUN result:
- Key counts, artifacts, or outputs proving the change:
- Remote verification, if applicable:

Status Split
- Local repository readiness:
- Task implementation:
- Validation:
- External systems:
- Remote/repository governance:
- Domain-specific proof:

Risk
- Known caveats:
- Unresolved gaps:
- Stop conditions hit:
- What was intentionally not touched:

Next
- The next safe action, or `Waiting for scoped task`.

Unknowns
- List exact unknowns, or `None`.
```

Generated names must describe the work, not the agent.
