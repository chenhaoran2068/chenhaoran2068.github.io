from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READING_PAGE = ROOT / "docs" / "skills" / "research-paper-reading.md"
ROUTE_PAGE = ROOT / "docs" / "user-paths" / "paper-reading.md"
SYSTEM_PAGE = ROOT / "docs" / "systems" / "governed-research-workflow.md"


class ReadingSkillRouteTests(unittest.TestCase):
    def test_reading_skill_is_explicit_and_session_only_by_default(self) -> None:
        text = READING_PAGE.read_text(encoding="utf-8")
        self.assertIn("session_only", text)
        self.assertIn("不自动下载", text)
        self.assertIn("不自动保存", text)

    def test_system_boundary_preserves_a_separate_reading_entry(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")
        self.assertIn("不应被误当作新 Study", text)
        self.assertIn("不会自动调用", text)

    def test_reading_route_does_not_start_a_study(self) -> None:
        text = ROUTE_PAGE.read_text(encoding="utf-8")
        self.assertIn("不是新 Study intake", text)
        self.assertIn("不会自动下载、复制、保存、同步", text)


if __name__ == "__main__":
    unittest.main()
