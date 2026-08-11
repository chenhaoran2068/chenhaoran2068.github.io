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
        self.assertIn("不会扫描工作区", text)
        self.assertIn("直接写入文献管理器数据库", text)
        self.assertIn("full_close_reading", text)
        self.assertIn("closeout triage", text)

    def test_managed_route_requires_explicit_source_confirmation(self) -> None:
        text = MANAGED_ROUTE_PAGE.read_text(encoding="utf-8")
        self.assertIn("指定一份来源", text)
        self.assertIn("确认下载、导入或保留的授权", text)
        self.assertIn("不会扫描现有文件", text)

    def test_system_receives_metadata_only_and_no_automatic_skill_call(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")
        self.assertIn("metadata-only", text)
        self.assertIn("不会自动启动它", text)

    def test_system_route_keeps_design_governance_and_value_separate(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")

        self.assertIn("03–05</span><strong id=\"system-phase-design-title\">确定研究思路", text)
        expected_order = [
            "03</span><strong>确认研究问题",
            "04</span><strong>确认研究设计",
            "05</span><strong>写研究计划书，准备伦理、登记与数据访问材料",
            "06</span><strong id=\"system-phase-decision-title\">判断研究是否值得继续",
            "07</span><strong>完成结果与手稿",
        ]
        positions = [text.index(item) for item in expected_order]
        self.assertEqual(positions, sorted(positions))

        self.assertIn("每项条件及其最迟解决关卡", text)
        self.assertIn("锁定方案并开展正式分析", text)
        self.assertIn("阳性或显著不是唯一标准", text)
        self.assertIn("观察时间等关键设计事项", text)
        self.assertIn("按适用要求办理伦理与备案", text)
        self.assertIn("有价值、可诚实报告的论文", text)

    def test_design_inspector_has_concrete_feasibility_examples(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")

        self.assertIn("确认设计时，顺手看四件事", text)
        self.assertIn("研究谁、比较什么、看什么结局。", text)
        self.assertIn("time zero 不一致", text)

    def test_reading_route_does_not_start_a_study(self) -> None:
        text = ROUTE_PAGE.read_text(encoding="utf-8")
        self.assertIn("Study", text)


if __name__ == "__main__":
    unittest.main()
