from __future__ import annotations

import re
import unittest
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


if __name__ == "__main__":
    unittest.main()
