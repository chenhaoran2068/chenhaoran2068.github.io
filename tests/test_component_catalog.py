from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "data" / "component_catalog.yaml"


class ComponentCatalogTests(unittest.TestCase):
    def test_catalogue_has_only_reviewed_components(self) -> None:
        data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
        components = data["components"]
        self.assertEqual(
            [component["component_id"] for component in components],
            ["workspace-framework", "governed-research-workflow", "research-ethics"],
        )

    def test_required_fields_and_tagged_public_links(self) -> None:
        data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
        for component in data["components"]:
            for field in (
                "display_name",
                "kind",
                "version",
                "repository_url",
                "release_url",
                "official_rule_url",
                "purpose",
                "entry_conditions",
                "non_goals",
            ):
                self.assertTrue(component[field], f"missing {field}")
            self.assertIn(component["version"], component["release_url"])
            self.assertIn(component["version"], component["official_rule_url"])


if __name__ == "__main__":
    unittest.main()
