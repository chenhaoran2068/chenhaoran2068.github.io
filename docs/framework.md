<div class="component-page">

<header class="component-header">
  <p class="component-kind">Framework</p>
  <h1>Governed Research Workspace Framework</h1>
  <p>工作区里放什么、放在哪里，先看这里。System、Skill、项目和共享材料各有清楚的归属位置。</p>
</header>

<section class="component-section framework-summary">
  <div>
    <p>Framework 给出稳定的工作区骨架：顶层区域、登记文件和绑定位置。</p>
  </div>
  <div class="release-stamp"><span>当前公开 Release</span><strong><a href="https://github.com/chenhaoran2068/governed-research-workspace-framework/releases/tag/v0.4.0">v0.4.0</a></strong></div>
</section>

<section class="component-section" aria-labelledby="framework-tree-title">
  <div class="section-header">
    <div><p class="section-context">v0.4.0 参考布局</p><h2 id="framework-tree-title">工作区从这里展开</h2></div>
    <p>点击目录查看说明；示例可按需展开。</p>
  </div>

  <div class="framework-reference-map" aria-label="Framework 工作区参考布局">
    <div class="framework-tree-toolbar">
      <div class="framework-tree-legend" aria-label="目录树颜色说明">
        <span><i class="framework-color-swatch framework-color-example" aria-hidden="true"></i>绿色：名称示例</span>
        <span><i class="framework-color-swatch framework-color-placeholder" aria-hidden="true"></i>金黄：替换用占位符</span>
        <span><i class="framework-color-swatch framework-color-category" aria-hidden="true"></i>蓝色：数据类别示例</span>
      </div>
      <button id="framework-examples-toggle" class="framework-examples-toggle" type="button" aria-expanded="false">显示示例</button>
    </div>
    <div class="framework-reference-layout">
      <div class="framework-reference-tree" aria-label="工作区目录树">
        <button class="framework-tree-entry" type="button" data-framework-key="workspace"><span class="tree-branch" aria-hidden="true"> </span><span class="tree-folder framework-placeholder framework-structural-name">&lt;workspace&gt;/</span><span class="tree-folder framework-example framework-example-name">chenhaoran/</span><span class="framework-tree-note framework-structure-note"># 工作区根目录</span><span class="framework-tree-note framework-example-note"># 示例工作区</span></button>
        <button class="framework-tree-entry" type="button" data-framework-key="workspace-manifest"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-file">WORKSPACE_MANIFEST.yaml</span><span class="framework-tree-note"># 工作区登记</span></button>

        <button class="framework-tree-entry" type="button" data-framework-key="systems"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Systems/</span><span class="framework-tree-note"># System 来源</span></button>
        <button class="framework-tree-entry framework-tree-depth-1" type="button" data-framework-key="system-example"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="tree-folder framework-placeholder framework-structural-name">&lt;system-id&gt;/</span><span class="tree-folder framework-example framework-example-name">governed-research-workflow/</span><span class="framework-tree-note framework-structure-note"># 一个已登记的 System</span><span class="framework-tree-note framework-example-note"># 当前研究 System</span></button>
        <button class="framework-tree-entry framework-tree-depth-2" type="button" data-framework-key="system-manifest"><span class="tree-branch" aria-hidden="true">|  |  |-</span><span class="tree-file">SYSTEM_MANIFEST.yaml</span></button>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span>…System 自己的文件…</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">example-method-system/</span><span class="framework-tree-note"># 方法 System 的示例</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">laboratory-workflow/</span><span class="framework-tree-note"># 其他领域的示例</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="skills"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Skills/</span><span class="framework-tree-note"># 专项能力来源</span></button>
        <button class="framework-tree-entry framework-tree-depth-1" type="button" data-framework-key="skill-example"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="tree-folder framework-placeholder framework-structural-name">&lt;skill-id&gt;/</span><span class="tree-folder framework-example framework-example-name">research-paper-reading/</span><span class="framework-tree-note framework-structure-note"># 一项专项 Skill</span><span class="framework-tree-note framework-example-note"># 论文精读</span></button>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span>…Skill 自己的文件…</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">research-ethics/</span><span class="framework-tree-note"># 伦理准备</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">governed-engineering/</span><span class="framework-tree-note"># 工程治理工具包</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="shared"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Shared/</span><span class="framework-tree-note"># 共享服务</span></button>
        <button class="framework-tree-entry framework-tree-depth-1" type="button" data-framework-key="shared-service"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="tree-folder framework-placeholder">&lt;shared-service-id&gt;/</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|     |-</span><span class="framework-example">experience-vocabulary/</span><span class="framework-tree-note"># 经验词典服务</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|     |-</span><span class="framework-example">reporting-guidelines/</span><span class="framework-tree-note"># 共享报告指南</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|     |_</span><span class="framework-example">source-pointers/</span><span class="framework-tree-note"># 来源索引</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="knowledge"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Knowledge/</span><span class="framework-tree-note"># 知识服务</span></button>
        <button class="framework-tree-entry framework-tree-depth-1" type="button" data-framework-key="knowledge-service"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="tree-folder framework-placeholder">&lt;knowledge-service-id&gt;/</span></button>
        <button class="framework-tree-entry framework-tree-depth-2" type="button" data-framework-key="knowledge-manifest"><span class="tree-branch" aria-hidden="true">|     |-</span><span class="tree-file">KNOWLEDGE_SERVICE_MANIFEST.yaml</span></button>
        <button class="framework-tree-entry framework-tree-depth-2" type="button" data-framework-key="reference-manager"><span class="tree-branch" aria-hidden="true">|     |_</span><span class="tree-folder">reference_manager/</span><span class="framework-tree-note"># 可选的本地文献库</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|        |-</span><span class="framework-example">scholarly-reading-knowledge/</span><span class="framework-tree-note"># 阅读知识服务</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|        |_</span><span class="framework-example">zotero-library/</span><span class="framework-tree-note"># 本地文献库</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="methods"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Methods/</span><span class="framework-tree-note"># 方法与工具</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">clinical-database/</span><span class="framework-tree-note"># 临床数据库工作台</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">molecular-docking/</span><span class="framework-tree-note"># 分子对接工具</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">machine-learning-workbench/</span><span class="framework-tree-note"># 模型开发工作台</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="instances"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Instances/</span><span class="framework-tree-note"># 项目实例</span></button>
        <button class="framework-tree-entry framework-tree-depth-1" type="button" data-framework-key="project-example"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="tree-folder framework-placeholder">&lt;project-id&gt;/</span></button>
        <button class="framework-tree-entry framework-tree-depth-2" type="button" data-framework-key="project-state"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span class="tree-folder">00_state/</span></button>
        <button class="framework-tree-entry framework-tree-depth-3" type="button" data-framework-key="project-binding"><span class="tree-branch" aria-hidden="true">|  |     |_</span><span class="tree-file">PROJECT_SYSTEM_BINDING.yaml</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">research001-retrospective-icu-cohort/</span><span class="framework-tree-note"># 回顾性 ICU 队列</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">research002-imaging-model-validation/</span><span class="framework-tree-note"># 影像模型验证</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">research003-molecular-target-study/</span><span class="framework-tree-note"># 分子靶点研究</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="data-raw"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Data_Raw/</span><span class="framework-tree-note"># 经许可保留的原始材料</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-data-category">clinical-records/</span><span class="framework-tree-note"># 临床记录</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |-</span><span class="framework-example">mimic-iv/</span><span class="framework-tree-note"># MIMIC-IV</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span class="framework-example">eicu-crd/</span><span class="framework-tree-note"># eICU-CRD</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-data-category">omics/</span><span class="framework-tree-note"># 组学资料</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |-</span><span class="framework-example">geo/</span><span class="framework-tree-note"># Gene Expression Omnibus</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span class="framework-example">tcga/</span><span class="framework-tree-note"># The Cancer Genome Atlas</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-data-category">medical-imaging/</span><span class="framework-tree-note"># 医学影像</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |-</span><span class="framework-example">tcia/</span><span class="framework-tree-note"># The Cancer Imaging Archive</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span class="framework-example">openneuro/</span><span class="framework-tree-note"># OpenNeuro</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-data-category">survey-and-field-data/</span><span class="framework-tree-note"># 调查与现场资料</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |-</span><span class="framework-example">nhanes/</span><span class="framework-tree-note"># National Health and Nutrition Examination Survey</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|  |  |_</span><span class="framework-example">world-values-survey/</span><span class="framework-tree-note"># World Values Survey</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-data-category">public-administrative-data/</span><span class="framework-tree-note"># 公共行政资料</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|     |-</span><span class="framework-example">world-bank-open-data/</span><span class="framework-tree-note"># World Bank Open Data</span></p>
        <p class="framework-tree-line framework-tree-depth-2"><span class="tree-branch" aria-hidden="true">|     |_</span><span class="framework-example">us-census/</span><span class="framework-tree-note"># United States Census Bureau</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="github"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Github/</span><span class="framework-tree-note"># 公开衍生物的工作树</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">governed-research-workflow/</span><span class="framework-tree-note"># System 仓库</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">research-paper-reading/</span><span class="framework-tree-note"># Skill 仓库</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">chenhaoran2068.github.io/</span><span class="framework-tree-note"># 门户仓库</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="ops"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Ops/</span><span class="framework-tree-note"># 本机运行与维护</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">runtime-adoption/</span><span class="framework-tree-note"># 本机采用记录</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span class="framework-example">workspace-hygiene/</span><span class="framework-tree-note"># 工作区卫生检查</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span class="framework-example">validation-receipts/</span><span class="framework-tree-note"># 验证回执</span></p>

        <button class="framework-tree-entry" type="button" data-framework-key="archive"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder">Archive/</span><span class="framework-tree-note"># 历史保留</span></button>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">   |-</span><span class="framework-example">retired-study-records/</span><span class="framework-tree-note"># 已结束项目材料</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">   |-</span><span class="framework-example">superseded-releases/</span><span class="framework-tree-note"># 被替代的版本材料</span></p>
        <p class="framework-tree-line framework-tree-depth-1"><span class="tree-branch" aria-hidden="true">   |_</span><span class="framework-example">legacy-system/</span><span class="framework-tree-note"># 历史 System</span></p>
      </div>

      <aside class="framework-reference-inspector" aria-live="polite" aria-label="当前目录说明">
        <p class="workspace-inspector-label">当前选择</p>
        <h3 id="framework-reference-title">&lt;workspace&gt;/</h3>
        <p id="framework-reference-body">这是工作区根目录的占位符。个人名、团队名或长期项目组名都可以；它不必等于某一个 Study 的名字。</p>
        <p id="framework-reference-detail" class="framework-reference-detail">展开示例后会显示 chenhaoran/。新建工作区时使用小写字母、数字和连字符。</p>
      </aside>
    </div>
    <p class="framework-reference-note"># 绿色是材料名称示例；金黄尖括号是要替换的占位符；蓝色是 Data_Raw/ 的示意分类。</p>
  </div>
</section>

</div>

<script>
  (() => {
    const descriptions = {
      workspace: ["<workspace>/", "这是工作区根目录的占位符。个人名、团队名或长期项目组名都可以；它不必等于某一个 Study 的名字。", "展开示例后会显示 chenhaoran/。新建工作区时使用小写字母、数字和连字符。"],
      "workspace-manifest": ["WORKSPACE_MANIFEST.yaml", "工作区的登记文件。已配置的 System 和共享服务从这里被识别。", "它不保存项目结果、原始数据或手稿内容。"],
      systems: ["Systems/", "放 System 的来源目录。这里用 Governed Research Workflow 演示一个已经放入工作区的 System。", "System 的内部文件由它自己定义，Framework 只关心它如何被登记和绑定。"],
      "system-example": ["<system-id>/", "这是一个已登记 System 的目录位置。实际目录使用该 System 自己声明的 system id。", "展开示例后会显示 governed-research-workflow/。它不是所有工作区都必须安装的 System。"],
      "system-manifest": ["SYSTEM_MANIFEST.yaml", "System 的身份与兼容性文件。一个 System 要被登记使用，需要有这份文件。", "具体的模板、脚本、规则和项目工具仍归该 System 自己管理。"],
      skills: ["Skills/", "放可独立使用的专项 Skill。System 可以在合适的任务中引用 Skill，但目录位置不表示自动调用。", "一个 Skill 也可以不属于任何 System 的日常流程。"],
      "skill-example": ["<skill-id>/", "这是一个可独立使用的 Skill 目录位置。", "展开示例后会显示 research-paper-reading/。它不是 Framework 要求的固定目录。"],
      shared: ["Shared/", "放有明确所有者和共享范围的服务或材料。", "共享不等于公开，也不表示任何项目都能直接复制使用。"],
      "shared-service": ["<shared-service-id>/", "这是共享服务目录的占位符。真正需要一个已批准的共享服务时，再用它自己的标识替换。", "尖括号里的文字不是要照抄的目录名。"],
      knowledge: ["Knowledge/", "放经过明确登记的知识服务，例如受控文献阅读与知识卡服务。", "Framework 不替知识服务规定内部笔记、词典或文献分类方式。"],
      "knowledge-service": ["<knowledge-service-id>/", "这是知识服务目录的占位符。只有工作区和使用它的 System 都明确登记后，才会出现具体服务。", "不同知识服务可以有不同的内部结构。"],
      "knowledge-manifest": ["KNOWLEDGE_SERVICE_MANIFEST.yaml", "知识服务的登记文件。它说明服务的身份、边界和可被哪些 System 使用。", "它不是论文原文、阅读档案或项目结论。"],
      "reference-manager": ["reference_manager/", "可选的本地文献管理器资料位置，例如由 Zotero 管理的库。", "只有知识服务明确采用时才使用；其中的私有原始材料默认不进入公开衍生物。"],
      methods: ["Methods/", "放方法工作台、工具或长期维护的技术区域。", "某个 Study 的方案、运行和结果仍放在它自己的项目区域。"],
      instances: ["Instances/", "放真实项目。每个项目从自己的目录开始，由绑定的 primary System 继续安排内部结构。", "Framework 不替项目预先造出分析、手稿或投稿目录。"],
      "project-example": ["<project-id>/", "这是项目目录的占位符。创建真实项目时，用项目自己的标识替换。", "项目名称和研究题目可以相关，但不必完全相同。"],
      "project-state": ["00_state/", "项目的当前状态与关键登记位置。具体文件由该项目绑定的 primary System 决定。", "这里不是所有项目内容的总目录。"],
      "project-binding": ["PROJECT_SYSTEM_BINDING.yaml", "记录这个项目由哪个 primary System 管理，以及是否有其他 System 参与。", "它只记录绑定关系，不表示获得数据访问、伦理批准或分析授权。"],
      "data-raw": ["Data_Raw/", "经许可才保留的原始材料区域。这里按临床记录、组学、影像、调查和公共行政资料列出真实数据库示例。", "这些二级分类和数据库名称只是帮助理解，不是 Framework 规定的固定目录。每个来源仍按它自己的访问条件、版本和项目规则处理。"],
      github: ["Github/", "放经过审查的公开衍生物工作树。", "本地有一份 Git 工作树，不代表其中内容已经公开或适合公开。"],
      ops: ["Ops/", "放本机安装、验证与维护所需的操作性材料。", "它不替代组件的正式规则，也不是项目数据区。"],
      archive: ["Archive/", "放明确退役或保留的历史材料。", "历史材料仍需先确认版本和当前性，不能直接当作现行依据。"]
    };
    const title = document.getElementById("framework-reference-title");
    const body = document.getElementById("framework-reference-body");
    const detail = document.getElementById("framework-reference-detail");
    const entries = document.querySelectorAll("[data-framework-key]");
    const referenceMap = document.querySelector(".framework-reference-map");
    const exampleToggle = document.getElementById("framework-examples-toggle");
    const selectEntry = (key) => {
      const entry = descriptions[key];
      if (!entry) return;
      title.textContent = entry[0];
      body.textContent = entry[1];
      detail.textContent = entry[2];
      entries.forEach((element) => element.classList.toggle("is-selected", element.dataset.frameworkKey === key));
    };
    entries.forEach((element) => {
      element.addEventListener("click", () => selectEntry(element.dataset.frameworkKey));
      element.addEventListener("focus", () => selectEntry(element.dataset.frameworkKey));
    });
    exampleToggle.addEventListener("click", () => {
      const expanded = referenceMap.classList.toggle("examples-visible");
      exampleToggle.setAttribute("aria-expanded", String(expanded));
      exampleToggle.textContent = expanded ? "收起示例" : "显示示例";
    });
    selectEntry("workspace");
  })();
</script>
