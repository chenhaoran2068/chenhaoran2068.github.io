from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class ReleaseLinkTests(unittest.TestCase):
    def test_release_and_rule_links_match_the_reviewed_tags(self) -> None:
        catalog = yaml.safe_load(
            (ROOT / "docs" / "data" / "component_catalog.yaml").read_text(
                encoding="utf-8"
            )
        )
        for component in catalog["components"]:
            if component["version"] is None:
                self.assertIsNone(component["release_url"])
                continue
            self.assertIn(component["version"], component["official_rule_url"])
            if component["release_url"] is not None:
                self.assertIn(component["version"], component["release_url"])


if __name__ == "__main__":
    unittest.main()
