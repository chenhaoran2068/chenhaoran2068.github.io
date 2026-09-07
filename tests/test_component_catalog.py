from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "data" / "component_catalog.yaml"


class ComponentCatalogTests(unittest.TestCase):
    def test_catalogue_has_the_reviewed_component_set(self) -> None:
        data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
        components = data["components"]
        self.assertEqual(
            [component["component_id"] for component in components],
            [
                "workspace-framework",
                "governed-research-workflow",
                "research-ethics",
                "research-paper-reading",
                "governed-engineering",
                "clinical-database",
                "four-layer-oced-m-framework",
                "research-workflow-legacy",
                "llmpet-cat",
            ],
        )

    def test_catalogue_models_type_lifecycle_ownership_and_relation(self) -> None:
        data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
        self.assertEqual(data["catalog_version"], "0.2.6")
        kinds = {"framework", "system", "skill", "method", "tool", "other"}
        lifecycles = {
            "current",
            "preview",
            "historical",
            "unreviewed",
            "external",
            "excluded",
        }
        ownerships = {"first_party", "external"}
        relationships = {
            "core_component",
            "optional_companion",
            "method_support",
            "historical_related",
            "independent_project",
            "external_integration",
            "skill_package",
        }
        home_ids: list[str] = []
        for component in data["components"]:
            for field in (
                "display_name",
                "kind",
                "lifecycle",
                "ownership",
                "relationship",
                "version",
                "repository_url",
                "official_rule_url",
                "purpose",
                "entry_conditions",
                "non_goals",
                "show_on_home",
                "show_in_catalog",
                "last_reviewed",
            ):
                self.assertIn(field, component, f"missing {field}")
            self.assertIn(component["kind"], kinds)
            self.assertIn(component["lifecycle"], lifecycles)
            self.assertIn(component["ownership"], ownerships)
            self.assertIn(component["relationship"], relationships)
            self.assertTrue(component["repository_url"])
            self.assertTrue(component["official_rule_url"])
            if component["version"] is not None:
                self.assertIn(component["version"], component["official_rule_url"])
            if component["release_url"] is not None:
                self.assertIn(component["version"], component["release_url"])
            if component["show_on_home"]:
                home_ids.append(component["component_id"])
                self.assertEqual(component["lifecycle"], "current")
                self.assertEqual(component["ownership"], "first_party")
                self.assertTrue(component["show_in_catalog"])
        self.assertEqual(
            home_ids,
            [
                "workspace-framework",
                "governed-research-workflow",
                "research-ethics",
                "research-paper-reading",
                "governed-engineering",
            ],
        )

        engineering = next(
            component
            for component in data["components"]
            if component["component_id"] == "governed-engineering"
        )
        self.assertEqual(engineering["kind"], "skill")
        self.assertEqual(engineering["relationship"], "skill_package")
        self.assertEqual(
            engineering["member_skills"],
            [
                "governed-code-change",
                "governed-database-change",
                "governed-data-ingestion",
                "governed-runtime-operation",
                "audit-governed-delivery",
            ],
        )

        research_system = next(
            component
            for component in data["components"]
            if component["component_id"] == "governed-research-workflow"
        )
        self.assertEqual(research_system["version"], "v1.18.0")

    def test_catalogue_page_lists_only_catalogue_components(self) -> None:
        data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
        page = (ROOT / "docs" / "catalog.md").read_text(encoding="utf-8")
        for component in data["components"]:
            marker = f'data-component-id="{component["component_id"]}"'
            self.assertEqual(marker in page, component["show_in_catalog"])

        self.assertIn('class="catalog-tree"', page)
        self.assertNotIn('class="catalog-jump-links"', page)
        self.assertIn("包含的 Skills", page)
        self.assertIn("governed-database-change", page)
        self.assertIn("audit-governed-delivery", page)


if __name__ == "__main__":
    unittest.main()
