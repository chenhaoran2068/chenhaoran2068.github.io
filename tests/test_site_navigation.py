from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mkdocs.yml"


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


if __name__ == "__main__":
    unittest.main()
