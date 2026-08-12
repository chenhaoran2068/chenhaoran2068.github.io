from __future__ import annotations

import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class CiWorkflowTests(unittest.TestCase):
    def test_public_workflows_use_node_24_action_runtimes(self) -> None:
        for name in ("ci.yml", "pages.yml"):
            workflow = yaml.safe_load(
                (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
            )
            steps = workflow["jobs"][next(iter(workflow["jobs"]))]["steps"]
            actions = [step["uses"] for step in steps if "uses" in step]
            self.assertIn("actions/checkout@v5", actions, name)
            self.assertIn("actions/setup-python@v6", actions, name)


if __name__ == "__main__":
    unittest.main()
