"""Validate the AI onboarding documentation baseline."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "AGENTS.md",
    "docs/AI_REPO_ONBOARDING_FACTORY.md",
    "docs/AI_ONBOARDING_PACKAGE_SPEC.md",
    "docs/AI_ONBOARDING_DIAGNOSTICS_SPEC.md",
    "docs/AI_ONBOARDING_VALIDATION.md",
    "docs/AI_ONBOARDING_PROMPTS.md",
    "docs/AI_ONBOARDING_GOVERNANCE.md",
    "docs/AI_ONBOARDING_HANDOFF_TEMPLATE.md",
    "prompts/repo_agnostic_onboarding_prompt.md",
    "prompts/repo_agnostic_plan_execution_prompt.md",
]

STATUS_WORDS = [
    "PASS",
    "FAIL",
    "INCOMPLETE",
    "NOT_FOUND",
    "NOT_RUN",
    "NOT_REQUIRED",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require_file(relative_path: str, failures: list[str]) -> None:
    if not (ROOT / relative_path).is_file():
        failures.append(f"FAIL missing required file: {relative_path}")


def require_text(haystack: str, needle: str, label: str, failures: list[str]) -> None:
    if needle not in haystack:
        failures.append(f"FAIL missing {label}: {needle}")


def main() -> int:
    failures: list[str] = []

    for relative_path in REQUIRED_FILES:
        require_file(relative_path, failures)

    if failures:
        for failure in failures:
            print(failure)
        return 1

    readme = read_text("README.md")
    agents = read_text("AGENTS.md")

    for relative_path in REQUIRED_FILES[1:]:
        require_text(readme, relative_path, "README link/reference", failures)

    require_text(agents, "This is the first-read file", "AGENTS first-read contract", failures)
    require_text(agents, "docs/AI_REPO_ONBOARDING_FACTORY.md", "AGENTS factory reference", failures)
    require_text(agents, "docs/AI_ONBOARDING_GOVERNANCE.md", "AGENTS governance reference", failures)

    combined = readme + "\n" + agents
    for word in STATUS_WORDS:
        require_text(combined, word, "status word", failures)

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("PASS documentation baseline")
    print(f"PASS required files: {len(REQUIRED_FILES)}")
    print("PASS README links required docs")
    print("PASS AGENTS first-read contract")
    print("PASS status words")
    return 0


if __name__ == "__main__":
    sys.exit(main())
