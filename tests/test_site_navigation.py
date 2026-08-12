from __future__ import annotations

import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "mkdocs.yml"
DOCS_ROOT = ROOT / "docs"
LOCALIZED_PORTAL_PAGES = (
    "index.md",
    "catalog.md",
    "framework.md",
    "frameworks/index.md",
    "systems/index.md",
    "systems/governed-research-workflow.md",
    "skills/index.md",
    "skills/research-ethics.md",
    "skills/research-paper-reading.md",
    "user-paths/index.md",
    "user-paths/start-a-study.md",
    "integrations.md",
    "releases.md",
    "governance.md",
    "roadmap.md",
)


def flatten_nav(value: object) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value for item in flatten_nav(item)]
    if isinstance(value, dict):
        return [item for item in value.values() for item in flatten_nav(item)]
    raise TypeError(f"unsupported nav item: {value!r}")


class SiteNavigationTests(unittest.TestCase):
    def test_every_current_portal_page_has_explicit_english_and_japanese_counterparts(self) -> None:
        for relative_path in LOCALIZED_PORTAL_PAGES:
            source = DOCS_ROOT / relative_path
            self.assertTrue(source.is_file(), relative_path)
            for locale in ("en", "ja"):
                localized = source.with_name(f"{source.stem}.{locale}.md")
                self.assertTrue(
                    localized.is_file(),
                    f"{relative_path} needs an explicit {locale} counterpart",
                )

    def test_i18n_configuration_disables_chinese_fallback_and_exposes_same_page_switching(self) -> None:
        config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        i18n = next(
            plugin["i18n"]
            for plugin in config["plugins"]
            if isinstance(plugin, dict) and "i18n" in plugin
        )
        self.assertEqual(i18n["docs_structure"], "suffix")
        self.assertFalse(i18n["fallback_to_default"])
        self.assertTrue(i18n["reconfigure_search"])
        self.assertEqual(
            [language["locale"] for language in i18n["languages"]],
            ["zh", "en", "ja"],
        )

        override = (DOCS_ROOT / "overrides" / "main.html").read_text(
            encoding="utf-8"
        )
        for expected in (
            "page.file.alternates",
            "portal-language-switcher",
            "portal-language-switcher-desktop",
            "portal-language-switcher-mobile",
            "'中文'",
            "'EN'",
            "'日本語'",
        ):
            self.assertIn(expected, override)

        self.assertIn('<li class="nav-item portal-language-switcher', override)
        self.assertEqual(
            override.count("language_switcher('portal-language-switcher-desktop')"),
            1,
        )
        self.assertLess(
            override.index("{{ super() }}", override.index("{% block search_button %}")),
            override.index("language_switcher('portal-language-switcher-desktop')"),
        )

        stylesheet = (DOCS_ROOT / "stylesheets" / "portal.css").read_text(
            encoding="utf-8"
        )
        for expected in (
            "@media (min-width: 992px)",
            "@media (max-width: 991px)",
            ".portal-language-switcher-desktop",
            ".portal-language-switcher-mobile",
            ".navbar .portal-language-switcher-mobile {\n    display: flex;",
        ):
            self.assertIn(expected, stylesheet)
        self.assertNotIn(
            ".navbar .ms-md-auto li:not(:first-child)",
            stylesheet,
        )

    def test_localized_start_pages_keep_versions_and_setup_boundaries(self) -> None:
        for locale in ("en", "ja"):
            page = (
                DOCS_ROOT / "user-paths" / f"start-a-study.{locale}.md"
            ).read_text(encoding="utf-8")
            for version in ("v0.4.0", "v1.14.0", "v0.3.0", "v1.1.1", "v0.1.1"):
                self.assertIn(version, page)

        english = (DOCS_ROOT / "user-paths" / "start-a-study.en.md").read_text(
            encoding="utf-8"
        )
        japanese = (DOCS_ROOT / "user-paths" / "start-a-study.ja.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Do not create a real Study", english)
        self.assertIn("実際の Study を作成しない", japanese)

    def test_every_nav_page_exists(self) -> None:
        config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        for entry in flatten_nav(config["nav"]):
            self.assertTrue((ROOT / "docs" / entry).is_file(), entry)

    def test_global_navigation_is_a_directory_not_a_reading_sequence(self) -> None:
        config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
        menus = {
            label: entries
            for item in config["nav"]
            if isinstance(item, dict)
            for label, entries in item.items()
        }

        self.assertEqual(
            [label for item in menus["组件"] for label in item],
            ["Framework 总览", "System 总览", "Skills 总览"],
        )
        self.assertEqual(
            [label for item in menus["版本与治理"] for label in item],
            ["发布与兼容", "治理边界", "路线图"],
        )
        self.assertIsNone(config["edit_uri"])

        override = ROOT / "docs" / "overrides" / "main.html"
        self.assertTrue(override.is_file())
        override_source = override.read_text(encoding="utf-8")
        self.assertIn("block next_prev", override_source)
        self.assertIn("block repo", override_source)

    def test_component_overviews_link_to_current_component_detail_pages(self) -> None:
        framework_overview = (DOCS_ROOT / "frameworks" / "index.md").read_text(
            encoding="utf-8"
        )
        system_overview = (DOCS_ROOT / "systems" / "index.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("用 Framework 搭建一个工作区", framework_overview)
        self.assertIn('href="../framework/"', framework_overview)
        self.assertIn("用 System 组织一类持续工作", system_overview)
        self.assertIn('href="governed-research-workflow/"', system_overview)

    def test_framework_reference_map_marks_every_visible_example_and_its_legend(self) -> None:
        page = (DOCS_ROOT / "framework.md").read_text(encoding="utf-8")
        stylesheet = (DOCS_ROOT / "stylesheets" / "portal.css").read_text(
            encoding="utf-8"
        )

        for expected in (
            "framework-legend-example-word",
            "framework-legend-placeholder-word",
            "framework-legend-category-word",
            'class="framework-tree-note framework-example-note"',
        ):
            self.assertIn(expected, page)

        self.assertIn(
            ".framework-example ~ .framework-example-note::after",
            stylesheet,
        )
        self.assertIn('content: "【示例】"', stylesheet)

    def test_release_page_retains_historical_release_notes_outside_global_navigation(self) -> None:
        page = (DOCS_ROOT / "releases.md").read_text(encoding="utf-8")
        for version in ("v0.5.2", "v0.5.1", "v0.5.0", "v0.4.2", "v0.4.1", "v0.4.0", "v0.3.0", "v0.2.0", "v0.1.0"):
            self.assertIn(f"RELEASE_NOTES_{version}", page)
            self.assertIn(f">{version}</a>", page)

    def test_skills_overview_uses_task_scenarios_and_lists_engineering_members(self) -> None:
        page = (DOCS_ROOT / "skills" / "index.md").read_text(encoding="utf-8")

        self.assertIn("按手头的任务选择", page)
        self.assertNotIn("两个独立 Skill 与一个 Skill 包", page)
        self.assertNotIn("共同边界", page)
        self.assertIn('class="skills-directory"', page)
        for member in (
            "governed-code-change",
            "governed-database-change",
            "governed-data-ingestion",
            "governed-runtime-operation",
            "audit-governed-delivery",
        ):
            self.assertIn(member, page)

    def test_user_guides_start_from_concrete_tasks(self) -> None:
        index = (DOCS_ROOT / "user-paths" / "index.md").read_text(encoding="utf-8")
        ethics = (DOCS_ROOT / "skills" / "research-ethics.md").read_text(
            encoding="utf-8"
        )
        reading = (DOCS_ROOT / "skills" / "research-paper-reading.md").read_text(
            encoding="utf-8"
        )
        study_start = (DOCS_ROOT / "user-paths" / "start-a-study.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("我现在要做什么？", index)
        for href in (
            'href="start-a-study/"',
            'href="../skills/research-paper-reading/"',
        ):
            self.assertIn(href, index)
        self.assertIn("我想做一个研究", index)
        self.assertNotIn('href="managed-reading-knowledge/"', index)
        self.assertIn("我想准备伦理与备案材料", ethics)
        self.assertIn("适用的研究路线", ethics)
        self.assertIn("复制这段话给 AI", ethics)
        self.assertIn("不要提交、上传或发送材料", ethics)
        self.assertIn("我想读懂一篇论文", reading)
        self.assertIn("开始前需要配置什么", reading)
        self.assertIn("只在当前对话读懂一篇论文", reading)
        self.assertIn("长期保留论文与阅读结果", reading)
        self.assertIn("复制这段话给 AI", reading)
        self.assertIn("阅读模式：[session_only / managed_reading]", reading)
        self.assertIn("PDF、链接、题目、引文", reading)
        self.assertNotIn("managed-reading-knowledge/", reading)
        self.assertIn("只处理这一次点名的论文", reading)
        self.assertIn("来源支撑知识可以提出经验候选", reading)
        self.assertIn("我想做一个研究", study_start)
        self.assertIn("开始研究前需要什么", study_start)
        self.assertIn("Governed Research Workspace Framework v0.4.0", study_start)
        self.assertIn("Governed Research Workflow v1.14.0", study_start)
        self.assertIn("复制这段话给 AI", study_start)
        self.assertIn("在我接受新研究的路线建议前", study_start)
        self.assertIn("人机交互模式", study_start)
        self.assertIn("AI 自主模式", study_start)
        self.assertIn('href="../../systems/governed-research-workflow/"', study_start)

    def test_secondary_pages_keep_current_integration_and_release_positions(self) -> None:
        integrations = (DOCS_ROOT / "integrations.md").read_text(encoding="utf-8")
        releases = (DOCS_ROOT / "releases.md").read_text(encoding="utf-8")
        governance = (DOCS_ROOT / "governance.md").read_text(encoding="utf-8")
        roadmap = (DOCS_ROOT / "roadmap.md").read_text(encoding="utf-8")

        self.assertIn("Zotero", integrations)
        self.assertIn("目前不宣称已支持", integrations)
        for version in ("v0.4.0", "v1.14.0", "v0.3.0", "v1.1.1", "v0.1.1"):
            self.assertIn(version, releases)
        self.assertIn("网站只是组件入口", governance)
        self.assertIn("尚未承诺的方向", roadmap)

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
            "docs/index.md": {
                "catalog/",
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

    def test_deep_skill_pages_keep_their_task_instructions_with_the_component(self) -> None:
        ethics = (DOCS_ROOT / "skills" / "research-ethics.md").read_text(
            encoding="utf-8"
        )
        reading = (DOCS_ROOT / "skills" / "research-paper-reading.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("ethics-preparation/", ethics)
        self.assertIn("复制这段话给 AI", ethics)
        self.assertIn("复制这段话给 AI", reading)

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

    def test_homepage_introduces_component_value_before_component_terms(self) -> None:
        homepage = (DOCS_ROOT / "index.md").read_text(encoding="utf-8")

        self.assertIn("公开组件目录", homepage)
        self.assertIn("这里会介绍一系列 Framework、System、Skills 等内容。", homepage)
        self.assertIn("大家可以下载、配置这些材料。", homepage)
        self.assertIn("可以有效管理各种材料的存放，并合理推进研究。", homepage)
        self.assertIn('class="portal-lead home-intro-lead"', homepage)
        self.assertEqual(homepage.count("<p>大家可以下载、配置这些材料。</p>"), 1)
        self.assertIn("Framework、System 和 Skills 是什么？", homepage)
        self.assertIn(
            "配套使用这些 Framework、System 和 Skills，可以得到什么？",
            homepage,
        )
        self.assertIn("一次配置当前公开核心组件", homepage)
        self.assertIn("Governed Research Workspace Framework v0.4.0", homepage)
        self.assertIn("Governed Research Workflow v1.14.0", homepage)
        self.assertIn("research-paper-reading v0.3.0", homepage)
        self.assertIn("research-ethics v1.1.1", homepage)
        self.assertIn("Governed Engineering v0.1.1", homepage)
        self.assertIn("不要创建实际 Study", homepage)
        for expected in (
            "跨项目可复用的模板",
            "一篇论文的阅读档案",
            "可复用的方法包",
            "MIMIC-IV、TCGA",
            "governed-research-workflow、research-paper-reading",
        ):
            self.assertIn(expected, homepage)
        self.assertNotIn("门户用于了解结构和定位入口", homepage)

    def test_system_workflow_page_exposes_the_results_first_work_sequence(self) -> None:
        page = (DOCS_ROOT / "systems" / "governed-research-workflow.md").read_text(
            encoding="utf-8"
        )

        for expected in (
            "完成结果与手稿",
            "开始条件：已有受控运行和结果包。",
            "01 完成 Results",
            "02 完成其余手稿与提交材料",
            "03 进入联合审查",
            "先安排主要、次要、敏感性和探索性结果分别放在哪里",
            "从 Results 整体到小节、段落、句子和主张，再到图表和证据",
            "Results 定下来后，Methods 回到方案和实际执行记录",
            "stagePrecondition.hidden = !entry.precondition;",
        ):
            self.assertIn(expected, page)

        self.assertNotIn('examplesTitle: "Results 逐层完成"', page)
        self.assertIn(
            'window.matchMedia("(max-width: 760px)").matches',
            page,
        )
        self.assertIn(
            '(stageInspector || stageTitle).scrollIntoView({ block: "start", behavior: "auto" })',
            page,
        )
        self.assertIn("const stageInspector = document.querySelector", page)
        self.assertIn(
            'window.scrollBy({ top: currentTop - stickyTop, behavior: "auto" })',
            page,
        )
        self.assertIn("如果已经清楚自己的研究问题", page)
        self.assertIn("如果尚不清楚自己的研究问题", page)
        self.assertIn("stageNextRow.hidden = !entry.next;", page)
        self.assertIn("按研究类型查看要确定什么", page)
        self.assertIn("system-route-guide-group", page)

    def test_system_route_inspector_stays_compact_in_the_two_column_layout(self) -> None:
        stylesheet = (DOCS_ROOT / "stylesheets" / "portal.css").read_text(
            encoding="utf-8"
        )

        inspector_rule = re.search(
            r"\.system-inspector,\s*\.system-route-inspector\s*\{(?P<body>.*?)\n\}",
            stylesheet,
            re.DOTALL,
        )
        self.assertIsNotNone(inspector_rule)
        self.assertIn("align-self: start;", inspector_rule.group("body"))
        self.assertIn("position: sticky;", inspector_rule.group("body"))

    def test_research_ethics_page_matches_the_stage_five_preparation_chain(self) -> None:
        page = (DOCS_ROOT / "skills" / "research-ethics.md").read_text(
            encoding="utf-8"
        )

        for expected in (
            "它对应 Research System 的第 05 阶段",
            "我想准备伦理与备案材料",
            "从研究计划书到可提交材料",
            "完成研究计划书",
            "准备科学性论证",
            "核对并生成伦理、登记准备稿",
            "按机构与平台流程办理",
            "一个明确的 Study",
            "actual_submission",
            "test_public",
            "03_protocol/derived/ethics_preparation/&lt;package_id&gt;/",
            "02_registry/compliance/",
            "等待对应专门模块后再处理",
            "适用的研究路线",
            "不要提交、上传或发送材料",
        ):
            self.assertIn(expected, page)

        self.assertNotIn("准备，不推进", page)
        self.assertNotIn("不产生批准事实", page)
        self.assertNotIn("查看正式规则", page)

    def test_research_paper_reading_page_exposes_the_actual_reading_and_closeout_flow(self) -> None:
        page = (DOCS_ROOT / "skills" / "research-paper-reading.md").read_text(
            encoding="utf-8"
        )

        for expected in (
            "请带我读这篇论文",
            "full_close_reading",
            "structured_close_reading",
            "focused_reading",
            "先弄清整篇研究最后得出什么结论",
            "再按节理解文章",
            "再按段理解每一节",
            "最后读关键句",
            "再逐项读图、表和补充材料",
            "作者的主张，不把它直接当成已经被证明的事实",
            "决定要不要留下什么",
            "知识—经验派生候选",
            "Knowledge/&lt;service-id&gt;/",
            "只处理这一次点名的论文",
            "来源支撑知识可以提出经验候选",
            "<code>&lt;Study&gt;/04_knowledge/</code>",
            "普通 <code>session_only</code> 阅读不需要这些配置",
            "不会扫描工作区",
        ):
            self.assertIn(expected, page)

        self.assertNotIn("不自动保存或提升", page)
        self.assertNotIn("查看这个版本的正式说明", page)


if __name__ == "__main__":
    unittest.main()
