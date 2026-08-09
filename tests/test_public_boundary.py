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
    "docs/architecture-map.md",
    "docs/framework.md",
    "docs/systems/governed-research-workflow.md",
    "docs/skills/research-ethics.md",
    "docs/user-paths/index.md",
    "docs/user-paths/possible-new-study.md",
    "docs/user-paths/existing-study-manuscript-revision.md",
    "docs/user-paths/ethics-preparation.md",
    "docs/releases.md",
    "docs/governance.md",
    "docs/roadmap.md",
    "docs/data/component_catalog.yaml",
    "docs/stylesheets/portal.css",
    "docs/assets/architecture-map.svg",
    "docs/release/RELEASE_NOTES_v0.1.0.md",
    "tests/test_component_catalog.py",
    "tests/test_public_boundary.py",
    "tests/test_site_navigation.py",
    "tests/test_release_links.py",
}


class PublicBoundaryTests(unittest.TestCase):
    def test_candidate_has_exactly_the_approved_public_files(self) -> None:
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
            and ".git" not in path.relative_to(ROOT).parts
            and "__pycache__" not in path.relative_to(ROOT).parts
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
