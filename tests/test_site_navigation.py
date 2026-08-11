from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mkdocs.yml"
DOCS_ROOT = ROOT / "docs"


def flatten_nav(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value for item in flatten_nav(item)]
    if isinstance(value, dict):
        return [item for item in value.values() for item in flatten_nav(item)]
    raise TypeError(f"unsupported nav item: {value!r}")


class SiteNavigationTests(unittest.TestCase):
    def test_every_nav_page_exists(self) -> None:
        config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        for entry in flatten_nav(config["nav"]):
            self.assertTrue((ROOT / "docs" / entry).is_file(), entry)

    def test_markdown_relative_links_resolve(self) -> None:
        for page in (ROOT / "docs").rglob("*.md"):
            for target in re.findall(r"\[[^\]]+\]\(([^)#]+)", page.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("mailto:"):
                    continue
                self.assertTrue(
                    (page.parent / target).resolve().is_file(),
                    f"{page.relative_to(ROOT)} has unresolved link: {target}",
                )

    def test_raw_html_anchors_do_not_link_to_markdown_source_files(self) -> None:
        class AnchorCollector(HTMLParser):
            def __init__(self) -> None:
                super().__init__()
                self.hrefs: list[str] = []

            def handle_starttag(
                self, tag: str, attrs: list[tuple[str, str | None]]
            ) -> None:
                if tag != "a":
                    return
                for name, value in attrs:
                    if name == "href" and value is not None:
                        self.hrefs.append(value)

        for page in (ROOT / "docs").rglob("*.md"):
            collector = AnchorCollector()
            collector.feed(page.read_text(encoding="utf-8"))
            for href in collector.hrefs:
                if "://" in href or href.startswith("mailto:"):
                    continue
                self.assertFalse(
                    href.split("#", 1)[0].split("?", 1)[0].endswith(".md"),
                    f"{page.relative_to(ROOT)} raw HTML anchor links to Markdown source: {href}",
                )

    def test_new_raw_html_component_links_resolve_from_published_pages(self) -> None:
        expected = {
            "docs/architecture-map.md": {
                "../integrations/",
                "../framework/",
                "../systems/governed-research-workflow/",
                "../skills/",
            },
            "docs/catalog.md": {
                "../framework/",
                "../systems/governed-research-workflow/",
                "../skills/research-ethics/",
                "../skills/research-paper-reading/",
            },
        }
        for relative_path, expected_hrefs in expected.items():
            page = ROOT / relative_path
            content = page.read_text(encoding="utf-8")
            hrefs = set(re.findall(r'<a[^>]+href="([^"]+)"', content))
            self.assertTrue(
                expected_hrefs <= hrefs,
                f"{relative_path} must use published-page relative paths",
            )

    def test_deep_component_pages_link_to_guides_from_their_published_depth(self) -> None:
        expected = {
            "docs/systems/governed-research-workflow.md": {
                "../../user-paths/possible-new-study/",
                "../../user-paths/existing-study-manuscript-revision/",
            },
            "docs/skills/research-ethics.md": {
                "../../user-paths/ethics-preparation/",
            },
            "docs/skills/research-paper-reading.md": {
                "../../user-paths/paper-reading/",
                "../../user-paths/managed-reading-knowledge/",
            },
        }
        for relative_path, expected_hrefs in expected.items():
            page = ROOT / relative_path
            hrefs = set(re.findall(r'<a[^>]+href="([^"]+)"', page.read_text(encoding="utf-8")))
            self.assertTrue(
                expected_hrefs <= hrefs,
                f"{relative_path} must use published-page relative guide links",
            )

    def test_homepage_exposes_the_study_layout_under_instances(self) -> None:
        homepage = (DOCS_ROOT / "index.md").read_text(encoding="utf-8")

        self.assertIn('data-map-key="instances"', homepage)
        self.assertIn('data-map-key="study-layout"', homepage)
        self.assertIn("00_state/", homepage)
        self.assertIn("06_data/", homepage)
        self.assertIn("12_archive/", homepage)
        self.assertNotIn("00_state/ … 12_archive/", homepage)
        self.assertIn(
            "systems/governed-research-workflow/#study-layout-title", homepage
        )

    def test_system_workflow_page_exposes_the_results_first_work_sequence(self) -> None:
        page = (DOCS_ROOT / "systems" / "governed-research-workflow.md").read_text(
            encoding="utf-8"
        )

        for expected in (
            "完成结果与手稿",
            "先完成 Results，再按顺序完成其他章节",
            "Methods、Discussion 与 Conclusion、Introduction、Abstract 或 Summary",
            "展开查看 Results 怎样逐层完成",
            "<details id=\"stage-inspector-examples\"",
            "默认可图文并行",
            "不能借此改变结果事实或把探索写成预先验证",
        ):
            self.assertIn(expected, page)


if __name__ == "__main__":
    unittest.main()
