from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_TEXT_FILES = [
    ROOT / "README.md",
    ROOT / "PUBLIC_BOUNDARY.md",
    ROOT / "SECURITY.md",
    ROOT / "RELEASE_CONTROL.md",
    ROOT / "mkdocs.yml",
    ROOT / ".github" / "workflows" / "ci.yml",
    ROOT / ".github" / "workflows" / "pages.yml",
    *sorted((ROOT / "docs").rglob("*.md")),
    *sorted((ROOT / "docs").rglob("*.yaml")),
    *sorted((ROOT / "docs").rglob("*.svg")),
    *sorted((ROOT / "docs").rglob("*.css")),
]
PROHIBITED = (
    r"(?i)[a-z]:\\",
    r"(?i)\.codex",
    r"\bSRC-[A-Z0-9-]+\b",
    r"\bM(?:48|54)\b",
    r"local_evaluation_records",
    r"Shared/Human_Overview",
    r"Research\d+_",
)
ALLOWED_PUBLIC_FILES = {
    ".gitattributes",
    ".gitignore",
    ".github/workflows/ci.yml",
    ".github/workflows/pages.yml",
    "LICENSE",
    "README.md",
    "PUBLIC_BOUNDARY.md",
    "SECURITY.md",
    "RELEASE_CONTROL.md",
    "requirements-docs.in",
    "requirements-docs.lock.txt",
    "mkdocs.yml",
    "docs/index.md",
    "docs/index.en.md",
    "docs/index.ja.md",
    "docs/catalog.md",
    "docs/catalog.en.md",
    "docs/catalog.ja.md",
    "docs/framework.md",
    "docs/framework.en.md",
    "docs/framework.ja.md",
    "docs/frameworks/index.md",
    "docs/frameworks/index.en.md",
    "docs/frameworks/index.ja.md",
    "docs/systems/index.md",
    "docs/systems/index.en.md",
    "docs/systems/index.ja.md",
    "docs/systems/governed-research-workflow.md",
    "docs/systems/governed-research-workflow.en.md",
    "docs/systems/governed-research-workflow.ja.md",
    "docs/skills/index.md",
    "docs/skills/index.en.md",
    "docs/skills/index.ja.md",
    "docs/skills/research-ethics.md",
    "docs/skills/research-ethics.en.md",
    "docs/skills/research-ethics.ja.md",
    "docs/skills/research-paper-reading.md",
    "docs/skills/research-paper-reading.en.md",
    "docs/skills/research-paper-reading.ja.md",
    "docs/user-paths/index.md",
    "docs/user-paths/index.en.md",
    "docs/user-paths/index.ja.md",
    "docs/user-paths/start-a-study.md",
    "docs/user-paths/start-a-study.en.md",
    "docs/user-paths/start-a-study.ja.md",
    "docs/integrations.md",
    "docs/integrations.en.md",
    "docs/integrations.ja.md",
    "docs/releases.md",
    "docs/releases.en.md",
    "docs/releases.ja.md",
    "docs/governance.md",
    "docs/governance.en.md",
    "docs/governance.ja.md",
    "docs/roadmap.md",
    "docs/roadmap.en.md",
    "docs/roadmap.ja.md",
    "docs/data/component_catalog.yaml",
    "docs/overrides/main.html",
    "docs/stylesheets/portal.css",
    "docs/release/RELEASE_NOTES_v0.5.0.md",
    "docs/release/RELEASE_NOTES_v0.1.0.md",
    "docs/release/RELEASE_NOTES_v0.2.0.md",
    "docs/release/RELEASE_NOTES_v0.3.0.md",
    "docs/release/RELEASE_NOTES_v0.4.0.md",
    "docs/release/RELEASE_NOTES_v0.4.1.md",
    "docs/release/RELEASE_NOTES_v0.4.2.md",
    "tests/test_component_catalog.py",
    "tests/test_ci_workflows.py",
    "tests/test_public_boundary.py",
    "tests/test_site_navigation.py",
    "tests/test_release_links.py",
    "tests/test_reading_skill_route.py",
}
LOCAL_BUILD_DIRECTORIES = {".git", "__pycache__", ".venv-docs", "site"}


def is_local_build_output(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    return bool(LOCAL_BUILD_DIRECTORIES & set(parts)) or any(
        part.startswith("site-validation-") for part in parts
    )


class PublicBoundaryTests(unittest.TestCase):
    def test_candidate_has_exactly_the_approved_public_files(self) -> None:
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
            and not is_local_build_output(path)
            and path.suffix != ".pyc"
        }
        self.assertEqual(actual, ALLOWED_PUBLIC_FILES)

    def test_public_content_has_no_private_identifiers_or_paths(self) -> None:
        for path in PUBLIC_TEXT_FILES:
            text = path.read_text(encoding="utf-8")
            for expression in PROHIBITED:
                self.assertIsNone(
                    re.search(expression, text),
                    f"{path.relative_to(ROOT)} contains prohibited content: {expression}",
                )


if __name__ == "__main__":
    unittest.main()
