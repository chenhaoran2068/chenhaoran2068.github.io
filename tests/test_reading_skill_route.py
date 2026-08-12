from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READING_PAGE = ROOT / "docs" / "skills" / "research-paper-reading.md"
STUDY_START_PAGE = ROOT / "docs" / "user-paths" / "start-a-study.md"
SYSTEM_PAGE = ROOT / "docs" / "systems" / "governed-research-workflow.md"


class ReadingSkillRouteTests(unittest.TestCase):
    def test_reading_skill_is_explicit_and_session_only_by_default(self) -> None:
        text = READING_PAGE.read_text(encoding="utf-8")
        self.assertIn("session_only", text)
        self.assertIn("不会扫描工作区", text)
        self.assertIn("直接写入文献管理器数据库", text)
        self.assertIn("full_close_reading", text)
        self.assertIn("closeout triage", text)
        self.assertIn("只在当前对话读懂一篇论文", text)
        self.assertIn("长期保留论文与阅读结果", text)
        self.assertIn("阅读模式：[session_only / managed_reading]", text)
        self.assertIn("除非我对这一篇来源明确确认下载、导入或长期保留", text)

    def test_managed_retention_stays_with_the_reading_skill(self) -> None:
        text = READING_PAGE.read_text(encoding="utf-8")
        self.assertIn("只处理这一次点名的论文", text)
        self.assertIn("下载、导入或长期保留", text)
        self.assertIn("不会扫描工作区", text)
        self.assertIn("04_knowledge/", text)
        self.assertIn("05_memory/", text)

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
            "05</span><strong>完成研究计划书，办理研究开始前的审查",
            "06</span><strong id=\"system-phase-decision-title\">判断研究是否值得继续",
            "07</span><strong>完成结果与手稿",
        ]
        positions = [text.index(item) for item in expected_order]
        self.assertEqual(positions, sorted(positions))

        self.assertIn("科学性论证、伦理、备案或登记、数据访问及其他所需材料", text)
        self.assertIn("常见的准备主线", text)
        self.assertIn("它与伦理审查不是同一件事", text)
        self.assertIn("选择继续时，才锁定当前方案", text)
        self.assertIn("阳性或显著不是唯一标准", text)
        self.assertIn("预测、预后或诊断研究如果来自一个队列", text)
        self.assertIn("当前官方要求，不只沿用旧模板", text)
        self.assertIn("有价值、可诚实报告的论文", text)

    def test_design_inspector_separates_selection_design_from_research_purpose(self) -> None:
        text = SYSTEM_PAGE.read_text(encoding="utf-8")

        self.assertIn("先分清五个方面", text)
        self.assertIn("对象怎样进入研究", text)
        self.assertIn("研究要回答什么", text)
        self.assertIn("预后或预测", text)
        self.assertIn("诊断准确性", text)
        self.assertIn("对象选择规则仍来自上面的设计", text)
        self.assertIn("stageGuides.open = false;", text)

    def test_study_start_page_keeps_entry_separate_from_the_full_system_route(self) -> None:
        text = STUDY_START_PAGE.read_text(encoding="utf-8")
        self.assertIn("我想开始一个新研究", text)
        self.assertIn("人机交互模式", text)
        self.assertIn("AI 自主模式", text)
        self.assertIn("不会因此自动创建 Study、读取数据或替你定研究设计", text)
        self.assertIn("开始研究前需要什么", text)
        self.assertIn("在我接受新研究的路线建议前", text)
        self.assertIn("Governed Research Workflow", text)


if __name__ == "__main__":
    unittest.main()
