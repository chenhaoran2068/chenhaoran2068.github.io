from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseLinkTests(unittest.TestCase):
    def test_release_and_rule_links_match_the_reviewed_tags(self) -> None:
        catalog = (ROOT / "docs" / "data" / "component_catalog.yaml").read_text(encoding="utf-8")
        expected = (
            "governed-research-workspace-framework/releases/tag/v0.3.0",
            "governed-research-workflow/releases/tag/v1.11.0",
            "research-ethics/releases/tag/v1.1.1",
            "research-paper-reading/releases/tag/v0.1.0",
            "/blob/v0.3.0/",
            "/blob/v1.11.0/",
            "/blob/v1.1.1/",
            "/blob/v0.1.0/",
        )
        for value in expected:
            self.assertIn(value, catalog)


if __name__ == "__main__":
    unittest.main()
