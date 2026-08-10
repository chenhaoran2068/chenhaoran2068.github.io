from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READING_PAGE = ROOT / "docs" / "skills" / "research-paper-reading.md"
ROUTE_PAGE = ROOT / "docs" / "user-paths" / "paper-reading.md"
MANAGED_ROUTE_PAGE = ROOT / "docs" / "user-paths" / "managed-reading-knowledge.md"
SYSTEM_PAGE = ROOT / "docs" / "systems" / "governed-research-workflow.md"


class ReadingSkillRouteTests(unittest.TestCase):
    def test_reading_skill_is_explicit_and_session_only_by_default(self) -> None:
        text = READING_PAGE.read_text(encoding="utf-8")
        self.assertIn("session_only", text)
        self.assertIn("does not scan a workspace", text)
        self.assertIn("reference-manager database directly", text)
        self.assertIn("full_close_reading", text)
        self.assertIn("closeout triage", text)

    def test_managed_route_requires_explicit_source_confirmation(self) -> None:
        text = MANAGED_ROUTE_PAGE.read_text(encoding="utf-8")
        self.assertIn("Name one source", text)
        self.assertIn("authorize", text)
        self.assertIn("does not scan existing files", text)

    def test_system_receives_metadata_only_and_no_automatic_skill_call(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")
        self.assertIn("metadata-only", text)
        self.assertIn("does not start that Skill automatically", text)

    def test_reading_route_does_not_start_a_study(self) -> None:
        text = ROUTE_PAGE.read_text(encoding="utf-8")
        self.assertIn("Study", text)


if __name__ == "__main__":
    unittest.main()
