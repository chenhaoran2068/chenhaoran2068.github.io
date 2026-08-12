<div class="portal-home">

<header class="portal-home-header">
  <p class="portal-context">公开组件目录</p>
  <h1>科研协作组件</h1>
  <div class="portal-lead home-intro-lead"><p>这里会介绍一系列 Framework、System、Skills 等内容。</p><p>大家可以下载、配置这些材料。</p><p>结合它们的帮助，可以有效管理各种材料的存放，并合理推进研究。</p></div>
</header>

<section class="portal-section role-explainer" aria-labelledby="home-roles-title">
  <div class="section-header">
    <div><p class="section-context">基本概念</p><h2 id="home-roles-title">Framework、System 和 Skills 是什么？</h2></div>
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

<section class="portal-section home-workspace-section" aria-labelledby="home-current-title">
  <div class="section-header">
    <div><p class="section-context">当前公开维护</p><h2 id="home-current-title">配套使用这些 Framework、System 和 Skills，可以得到什么？</h2></div>
    <p>下面用一个工作区例子，说明 Framework、System 和 Skills 可以怎样放在一起使用。</p>
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
            <details class="workspace-node workspace-study-layout" open>
              <summary data-map-key="instances"><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Instances/</span><span class="tree-translation"># 项目实例</span></summary>
              <div class="workspace-children">
                <button class="workspace-file workspace-selectable" type="button" data-map-key="study-layout"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder workspace-system-tone">&lt;study-id&gt;/</span><span class="tree-translation"># 一项实际研究</span></button>
                <div class="workspace-children workspace-study-directories" aria-label="Study 内部目录">
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">00_state/</span><span class="tree-translation"># 当前状态与决定</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">01_intake/</span><span class="tree-translation"># 研究请求与 intake</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">02_registry/</span><span class="tree-translation"># 登记与合规证据</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">03_protocol/</span><span class="tree-translation"># 设计与当前方案</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">04_knowledge/</span><span class="tree-translation"># 本 Study 的知识与应用判断</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">05_memory/</span><span class="tree-translation"># 决策记忆与项目复盘</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">06_data/</span><span class="tree-translation"># 项目数据工作面</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">07_analysis/</span><span class="tree-translation"># 合同、环境、实现与运行</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">08_results/</span><span class="tree-translation"># 结果与当前结果权威</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">09_manuscript/</span><span class="tree-translation"># 手稿、表图与主张</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">10_submission/</span><span class="tree-translation"># 投稿、返修与录用</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">11_qa/</span><span class="tree-translation"># 运行 QA</span></p>
                  <p><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder workspace-system-tone">12_archive/</span><span class="tree-translation"># 最终归档</span></p>
                </div>
              </div>
            </details>
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

<p class="all-projects-link"><a href="catalog/">查看全部公开项目 <span aria-hidden="true">-></span></a></p>

<section class="portal-section home-setup-section" aria-labelledby="home-setup-title">
  <div class="section-header">
    <div><p class="section-context">第一次配置</p><h2 id="home-setup-title">一次配置当前公开核心组件</h2></div>
    <p>复制下面的内容给你的 AI。它会按顺序检查、下载、配置和核验当前的 Framework、System 与 Skills。</p>
  </div>
  <p>本次包含：Governed Research Workspace Framework、Governed Research Workflow、research-paper-reading、research-ethics，以及 Governed Engineering 技能包。历史项目、独立工具和 Zotero 等外部工具不在这次自动配置范围内。</p>
  <pre class="home-setup-prompt"><code>我想在一个新的工作区中，一次配置 Research Collaboration 当前公开维护的核心组件。

候选工作区根目录：[填入你的工作区绝对路径]
目标 AI 环境：[填入名称；不确定可先检查]
是否准备受管文献库：[暂不需要 / 先检测已有 Zotero 或其他文献管理器]

我授权你按以下顺序完成：
1. 先检查上述位置是否已经有工作区；若已有内容，不覆盖、不迁移，先报告实际情况并停止等待我的决定。
2. 检查当前 AI 环境能否安装并使用以下精确公开 Release；如有不兼容，说明差异后停止，不自行替换环境或已有组件：
   - Governed Research Workspace Framework v0.4.0
   - Governed Research Workflow v1.14.0
   - research-paper-reading v0.3.0
   - research-ethics v1.1.1
   - Governed Engineering v0.1.1（含其五项成员 Skill）
3. 按各 Release 的正式说明下载、配置并核验这些组件；建立 Framework 工作区骨架，并登记已配置的 System 与 Skills。
4. 论文阅读默认只配置当前对话阅读。若我选择检测文献管理器，只检查是否已有；没有我的后续明确同意，不安装 Zotero 或其他外部工具。
5. 运行各组件允许的本地验证；汇报实际安装位置、已采用版本、验证结果、尚缺条件和恢复方法。

不要创建实际 Study，不读取、复制或处理真实数据、论文、伦理材料或其他私有材料；不要自动进入伦理准备、研究分析或提交发布动作。</code></pre>
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
      shared: ["Shared/", "跨项目可共用但仍需治理的材料区域。其内容应有明确所有者、适用范围和访问边界。", "例如：跨项目可复用的模板，或已审查的公开安全衍生物。共享不表示可自由复制到任意项目，也不等同于公开材料。", "framework/", "查看 Framework 介绍"],
      knowledge: ["Knowledge/", "保存文献阅读、知识卡与可追溯的知识服务材料。它与项目记忆、经验治理和原始论文分别保持边界。", "例如：一篇论文的阅读档案，或可关联来源的知识卡。它们不会只因打上标签就成为正式规则或项目结论。", "integrations/", "查看知识与集成说明"],
      methods: ["Methods/", "放置可复用的方法、技术路线或特定领域工具的工作区域。", "例如：可复用的方法包、统计或建模脚本框架，或某个领域的工具说明。它不替代某个 Study 的方案、分析合同或结果权威。", "framework/", "查看 Framework 介绍"],
      instances: ["Instances/", "存放具体项目或实际工作实例。一项 Study 会在这里建立自己的目录，而不是把方案、数据、分析、结果与手稿混入 System。", "展开下方的 <study-id>/ 可以看到从 00_state/ 到 12_archive/ 的完整目录名称。", "systems/governed-research-workflow/#study-layout-title", "查看完整 Study 布局"],
      "study-layout": ["<study-id>/", "一项实际研究的根目录。它按 00_state/ 到 12_archive/ 分开保存状态、方案、治理资料、数据、分析、结果、手稿、投稿和归档材料。", "这个目录结构由 Governed Research Workflow 提供；它位于 Instances/，不属于 System 本身的规则文件。", "systems/governed-research-workflow/#study-layout-title", "查看完整 Study 布局"],
      "data-raw": ["Data_Raw/", "受控原始材料的工作区区域。访问、复制、处理和保留均应遵守适用的数据权限与项目规则。", "例如：MIMIC-IV、TCGA 等公开数据源。这里只是来源命名示例，不表示数据已下载、获得访问权或可用于任何项目。", "framework/", "查看 Framework 介绍"],
      github: ["Github/", "本地仓库与公开衍生物的工作区域。公开内容仍需经过版本、边界、审查和发布流程。", "例如：governed-research-workflow、research-paper-reading 等公开组件仓库。在这里存在的材料不等于已公开或适合公开。", "releases/", "查看发布与兼容"],
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
