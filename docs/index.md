<div class="portal-home">

<header class="portal-home-header">
  <p class="portal-context">Chenhaoran 公开科研协作组件</p>
  <h1>科研协作组件</h1>
  <p class="portal-lead">这里汇总当前公开维护的组件及其正式来源。门户用于了解结构和定位入口；规则、版本与安装信息仍以各组件的精确 Release 和正式文档为准。</p>
</header>

<section class="portal-section role-explainer" aria-labelledby="home-roles-title">
  <div class="section-header">
    <div><p class="section-context">组件如何分工</p><h2 id="home-roles-title">三类组件</h2></div>
  </div>
  <div class="role-terminal" role="group" aria-label="Framework、System 与 Skills 的分工说明">
    <article class="role-terminal-entry">
      <h3>Framework</h3>
      <p><span aria-hidden="true">|-</span> 为整个工作区规定稳定的结构、材料归属和组件边界。</p>
      <p><span aria-hidden="true">|-</span> 在首次配置、迁移材料或扩展工作区时使用。</p>
      <p><span aria-hidden="true">|_</span> 例如：确定 System、Skill、Method、Instance 与 Knowledge 等区域如何共存。</p>
    </article>
    <article class="role-terminal-entry">
      <h3>System</h3>
      <p><span aria-hidden="true">|-</span> 为一个工作领域提供可长期维护的流程、规则、正式入口和协作边界。</p>
      <p><span aria-hidden="true">|-</span> 当某类工作需要按一套可复用、受控的方式持续推进时进入。</p>
      <p><span aria-hidden="true">|_</span> 例如：Research System 组织 Study 的规划、分析、手稿、返修与归档路径。</p>
    </article>
    <article class="role-terminal-entry">
      <h3>Skills</h3>
      <p><span aria-hidden="true">|-</span> 为一个边界清楚的专项任务提供具体步骤、输入要求和停止条件。</p>
      <p><span aria-hidden="true">|-</span> 当任务已经明确、需要专项协助时使用。</p>
      <p><span aria-hidden="true">|_</span> 例如：research-paper-reading 用于逐步读懂论文；research-ethics 在条件满足后协助伦理准备。</p>
    </article>
  </div>
</section>

<section class="portal-section" aria-labelledby="home-current-title">
  <div class="section-header">
    <div><p class="section-context">当前公开维护</p><h2 id="home-current-title">工作区组件地图</h2></div>
    <p>当前公开组件按 Framework 定义的工作区归属/安装位置模型列出，不表示其 Git 源码的实际路径。</p>
  </div>
  <div class="workspace-map" aria-label="可展开的工作区组件地图">
    <p class="workspace-tone-legend" aria-label="目录类型颜色标记"><span class="workspace-tone-key workspace-framework-key">Framework 骨架</span><span class="workspace-tone-key workspace-system-key">System</span><span class="workspace-tone-key workspace-skill-key">Skill</span></p>
    <div class="workspace-map-layout">
      <div class="workspace-tree" aria-label="工作区目录">
        <details class="workspace-node workspace-root" open>
          <summary data-map-key="workspace"><span class="tree-marker" aria-hidden="true">v</span><span class="tree-folder workspace-framework-tone">&lt;workspace&gt;/</span><span class="tree-translation"># 工作区框架</span></summary>
          <div class="workspace-children">
            <button class="workspace-file workspace-selectable" type="button" data-map-key="manifest"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-file workspace-framework-tone">WORKSPACE_MANIFEST.yaml</span></button>

            <details class="workspace-node" open>
              <summary data-map-key="systems"><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">Systems/</span><span class="tree-translation"># 工作流系统</span></summary>
              <div class="workspace-children">
                <button class="workspace-file workspace-selectable" type="button" data-map-key="research-system-folder"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder workspace-system-tone">research-orchestration-workflow/</span></button>
                <div class="workspace-children workspace-leaf-children">
                  <button class="workspace-file workspace-selectable" type="button" data-map-key="system-manifest"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-file workspace-system-tone">SYSTEM_MANIFEST.yaml</span></button>
                  <button class="workspace-component workspace-selectable" type="button" data-map-key="research-system"><span class="tree-branch" aria-hidden="true">|_</span><strong class="workspace-system-tone">Governed Research Workflow</strong><span class="tree-translation"># 研究工作流</span></button>
                </div>
              </div>
            </details>

            <details class="workspace-node" open>
              <summary data-map-key="skills"><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-skill-tone">Skills/</span><span class="tree-translation"># 专项能力</span></summary>
              <div class="workspace-children">
                <button class="workspace-file workspace-selectable" type="button" data-map-key="research-ethics-folder"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-skill-tone">research-ethics/</span></button>
                <button class="workspace-component workspace-selectable workspace-leaf-component" type="button" data-map-key="research-ethics"><span class="tree-branch" aria-hidden="true">|  |_</span><strong class="workspace-skill-tone">research-ethics</strong><span class="tree-translation"># 研究伦理准备</span></button>
                <button class="workspace-file workspace-selectable" type="button" data-map-key="paper-reading-folder"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-skill-tone">research-paper-reading/</span></button>
                <button class="workspace-component workspace-selectable workspace-leaf-component" type="button" data-map-key="paper-reading"><span class="tree-branch" aria-hidden="true">|  |_</span><strong class="workspace-skill-tone">research-paper-reading</strong><span class="tree-translation"># 论文精读</span></button>
                <details class="workspace-node workspace-skill-package" open>
                  <summary data-map-key="governed-engineering"><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder workspace-skill-tone">governed-engineering/</span><span class="tree-translation"># 工程治理工具包</span></summary>
                  <div class="workspace-children workspace-leaf-children">
                    <button class="workspace-component workspace-selectable" type="button" data-map-key="governed-code-change"><span class="tree-branch" aria-hidden="true">   |-</span><strong class="workspace-skill-tone">governed-code-change</strong><span class="tree-translation"># 受控代码变更</span></button>
                    <button class="workspace-component workspace-selectable" type="button" data-map-key="governed-database-change"><span class="tree-branch" aria-hidden="true">   |-</span><strong class="workspace-skill-tone">governed-database-change</strong><span class="tree-translation"># 受控数据库变更</span></button>
                    <button class="workspace-component workspace-selectable" type="button" data-map-key="governed-data-ingestion"><span class="tree-branch" aria-hidden="true">   |-</span><strong class="workspace-skill-tone">governed-data-ingestion</strong><span class="tree-translation"># 受控数据接收</span></button>
                    <button class="workspace-component workspace-selectable" type="button" data-map-key="governed-runtime-operation"><span class="tree-branch" aria-hidden="true">   |-</span><strong class="workspace-skill-tone">governed-runtime-operation</strong><span class="tree-translation"># 受控运行操作</span></button>
                    <button class="workspace-component workspace-selectable" type="button" data-map-key="audit-governed-delivery"><span class="tree-branch" aria-hidden="true">   |_</span><strong class="workspace-skill-tone">audit-governed-delivery</strong><span class="tree-translation"># 治理交付审查</span></button>
                  </div>
                </details>
              </div>
            </details>

            <button class="workspace-file workspace-selectable" type="button" data-map-key="shared"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Shared/</span><span class="tree-translation"># 共享材料</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="knowledge"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Knowledge/</span><span class="tree-translation"># 知识服务</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="methods"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Methods/</span><span class="tree-translation"># 方法与工具</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="instances"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Instances/</span><span class="tree-translation"># 项目实例</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="data-raw"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Data_Raw/</span><span class="tree-translation"># 原始数据</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="github"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Github/</span><span class="tree-translation"># Git 仓库</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="ops"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Ops/</span><span class="tree-translation"># 运行与维护</span></button>
            <button class="workspace-file workspace-selectable" type="button" data-map-key="archive"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder">Archive/</span><span class="tree-translation"># 归档</span></button>
          </div>
        </details>
      </div>
      <aside class="workspace-inspector" aria-live="polite" aria-label="当前目录说明">
        <p class="workspace-inspector-label">当前选择</p>
        <h3 id="workspace-inspector-title">&lt;workspace&gt;/</h3>
        <p id="workspace-inspector-body">整个工作区的顶层边界。它规定项目、方法、知识、共享材料与受控组件应如何归位，使其关系可以被稳定定位。</p>
        <p id="workspace-inspector-detail" class="workspace-inspector-detail">从左侧选择目录或组件，查看它在工作区中的职责。组件名称仍可进入对应的介绍页。</p>
        <a id="workspace-inspector-link" class="workspace-inspector-link" href="framework/">查看 Framework 介绍</a>
      </aside>
    </div>
    <p class="workspace-map-note"># 工作区归属/安装位置模型，不表示 Git 源码或 Codex runtime 的实际路径。</p>
  </div>
</section>

</div>

<script>
  (() => {
    const descriptions = {
      workspace: ["<workspace>/", "整个工作区的顶层边界。它规定项目、方法、知识、共享材料与受控组件应如何归位，使其关系可以被稳定定位。", "左侧展示的是 Framework 的归属/安装位置模型，不是每个组件的实际 Git 源码或 Codex runtime 路径。", "framework/", "查看 Framework 介绍"],
      manifest: ["WORKSPACE_MANIFEST.yaml", "工作区的身份与 System 绑定记录。它用于说明某个项目由哪个 System 负责，而不保存项目数据或研究结果。", "变更绑定或迁移工作区前，应以当前 Framework 合同核对这一记录。", "framework/", "查看 Framework 介绍"],
      systems: ["Systems/", "存放能够在一个工作领域中长期复用的 System。System 提供该领域的流程、正式入口、规则和协作边界。", "一个 System 可以引用合适的 Skill，但 Skill 并不自动成为它的下级步骤。", "systems/governed-research-workflow/", "查看当前 Research System"],
      "research-system-folder": ["research-orchestration-workflow/", "当前 Research System 在工作区中的来源位置。这里是其正式合同、模板、验证器和公开规则的归属点。", "Study 的具体材料仍保留在各自 Instance；System 不接管其真实数据、决定或结果。", "systems/governed-research-workflow/", "查看当前 Research System"],
      "system-manifest": ["SYSTEM_MANIFEST.yaml", "System 的机器可读身份和兼容性声明。它帮助 Framework 识别 System 的所有者、支持范围和安装关系。", "它不是研究方案、运行日志或结果权威。", "systems/governed-research-workflow/", "查看当前 Research System"],
      "research-system": ["Governed Research Workflow", "面向研究工作的 System：组织 Study 的规划、分析、结果治理、手稿、返修与归档路径。", "它提供工作流与边界，不自动批准伦理、访问数据、得出结论或提交投稿。", "systems/governed-research-workflow/", "打开组件页"],
      skills: ["Skills/", "存放边界清楚、可独立进入的专项协助模块，包括独立 Skill 和由多个相关 Skill 组成的 Skill 包。", "Skill 的位置表示来源归属，不表示它会被某个 System 自动调用。", "skills/", "查看 Skills 总览"],
      "research-ethics-folder": ["research-ethics/", "用于伦理与登记准备的专项 Skill 来源位置。只有任务明确进入其适用范围、并给出所需输入后才可使用。", "它不能确认伦理已获批准、代替平台提交或读取未许可的真实材料。", "skills/research-ethics/", "查看 research-ethics"],
      "research-ethics": ["research-ethics", "在条件满足后，协助整理伦理与登记准备所需的结构、缺口和填写内容。", "它不是 Research System 的自动下级步骤，也不作出批准或提交决定。", "skills/research-ethics/", "打开组件页"],
      "paper-reading-folder": ["research-paper-reading/", "用于逐步理解一篇论文的专项 Skill 来源位置。它服务于阅读、解释、图表理解与批判性讨论。", "它不会因普通研究对话自动读取论文或建立知识记录。", "skills/research-paper-reading/", "查看 research-paper-reading"],
      "paper-reading": ["research-paper-reading", "带领用户按章节、段落、图、表和主张边界理解一篇指定论文。", "阅读档案、知识卡或经验候选均需用户后续明确决定，不能由一次阅读自动生成。", "skills/research-paper-reading/", "打开组件页"],
      "governed-engineering": ["governed-engineering/", "一个包含五项工程治理 Skill 的公开插件包：代码变更、数据库变更、数据接收、运行操作与交付审计。", "它不是 Research System 的子模块，不管理凭据，也不执行无人值守的生产操作。", "https://github.com/chenhaoran2068/governed-engineering/releases/tag/v0.1.1", "查看 v0.1.1 Release"],
      "governed-code-change": ["governed-code-change", "用于有明确范围、接口、测试证据、恢复方案和人工授权门槛的代码或配置变更。", "它不替代数据库专用、数据接收专用、运行操作专用或没有边界的普通编程请求。", "https://github.com/chenhaoran2068/governed-engineering/blob/v0.1.1/skills/governed-code-change/SKILL.md", "查看 Skill 规则"],
      "governed-database-change": ["governed-database-change", "用于数据库结构、SQL、迁移、权限、锁、事务和回滚等受控变更。", "它不授予数据库访问权限，也不因命令成功就推断语义或授权。", "https://github.com/chenhaoran2068/governed-engineering/blob/v0.1.1/skills/governed-database-change/SKILL.md", "查看 Skill 规则"],
      "governed-data-ingestion": ["governed-data-ingestion", "用于来源接收、清单、校验、解析、隔离、重放和异常隔离等数据接收工作。", "它不绕过数据访问、许可、隐私或项目授权要求。", "https://github.com/chenhaoran2068/governed-engineering/blob/v0.1.1/skills/governed-data-ingestion/SKILL.md", "查看 Skill 规则"],
      "governed-runtime-operation": ["governed-runtime-operation", "用于有明确授权的命令行、服务、路径、环境、端点、恢复或回滚操作。", "它不用于无人值守控制，也不发现、请求或保存秘密信息。", "https://github.com/chenhaoran2068/governed-engineering/blob/v0.1.1/skills/governed-runtime-operation/SKILL.md", "查看 Skill 规则"],
      "audit-governed-delivery": ["audit-governed-delivery", "用于审查工程候选或交付物的可追溯性、测试证据、版本、发布门槛、保留与退役提案。", "它只能报告发现，不能自行批准、发布、安装、删除或提升任何材料。", "https://github.com/chenhaoran2068/governed-engineering/blob/v0.1.1/skills/audit-governed-delivery/SKILL.md", "查看 Skill 规则"],
      shared: ["Shared/", "跨项目可共用但仍需治理的材料区域。其内容应有明确所有者、适用范围和访问边界。", "共享不表示可自由复制到任意项目，也不等同于公开材料。", "framework/", "查看 Framework 介绍"],
      knowledge: ["Knowledge/", "保存文献阅读、知识卡与可追溯的知识服务材料。它与项目记忆、经验治理和原始论文分别保持边界。", "知识可以服务多个项目，但不能仅因有标签就变成正式规则或项目结论。", "integrations/", "查看知识与集成说明"],
      methods: ["Methods/", "放置可复用的方法、技术路线或特定领域工具的工作区域。", "它不替代某个 Study 的方案、分析合同或结果权威。", "framework/", "查看 Framework 介绍"],
      instances: ["Instances/", "存放具体项目或实际工作实例。Study 的方案、数据、分析、结果与手稿应在其自身边界内管理。", "项目局部材料不会因位于这里而自动成为共享经验或公开内容。", "framework/", "查看 Framework 介绍"],
      "data-raw": ["Data_Raw/", "受控原始材料的工作区区域。访问、复制、处理和保留均应遵守适用的数据权限与项目规则。", "它不是普通的临时文件夹，也不应被公开组件自动读取。", "framework/", "查看 Framework 介绍"],
      github: ["Github/", "本地仓库与公开衍生物的工作区域。公开内容仍需经过版本、边界、审查和发布流程。", "在这里存在的材料不等于已公开或适合公开。", "releases/", "查看发布与兼容"],
      ops: ["Ops/", "用于维护、安装、验证和运行层面的操作性材料。", "操作记录不等于组件规则，也不应被当作用户任务的正式输入。", "governance/", "查看治理边界"],
      archive: ["Archive/", "用于明确退役或保留历史的材料。历史存在不等于它仍是当前规则、当前版本或可复用依据。", "使用历史材料前，需要先确认其当前性与权威状态。", "governance/", "查看治理边界"]
    };
    const title = document.getElementById("workspace-inspector-title");
    const body = document.getElementById("workspace-inspector-body");
    const detail = document.getElementById("workspace-inspector-detail");
    const link = document.getElementById("workspace-inspector-link");
    const entries = document.querySelectorAll("[data-map-key]");

    const selectEntry = (key) => {
      const entry = descriptions[key];
      if (!entry) return;
      title.textContent = entry[0];
      body.textContent = entry[1];
      detail.textContent = entry[2];
      link.href = entry[3];
      link.textContent = entry[4];
      entries.forEach((element) => element.classList.toggle("is-selected", element.dataset.mapKey === key));
    };

    entries.forEach((element) => {
      element.addEventListener("click", () => selectEntry(element.dataset.mapKey));
      element.addEventListener("focus", () => selectEntry(element.dataset.mapKey));
    });
    selectEntry("workspace");
  })();
</script>
