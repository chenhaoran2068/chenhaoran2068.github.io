<div class="component-page system-page">

<header class="component-header">
  <p class="component-kind">System</p>
  <h1>Governed Research Workflow</h1>
  <p>把一项 Study 从研究想法、方案和分析，推进到结果、手稿、返修与归档的一套工作路径。</p>
</header>

<section class="component-section component-summary system-summary">
  <p>当一项研究需要持续整理方案、执行、结果、手稿和返修材料时，使用这个 System。它把材料放到可追溯的位置，并在关键节点保留人类确认。</p>
  <div class="release-stamp"><span>当前公开 Release</span><strong><a href="https://github.com/chenhaoran2068/governed-research-workflow/releases/tag/v1.14.0">v1.14.0</a></strong></div>
</section>

<section class="component-section" aria-labelledby="study-layout-title">
  <div class="section-header">
    <div><p class="section-context">Study 目录</p><h2 id="study-layout-title">一项 Study 从这里展开</h2></div>
    <p>这里展示的是 <code>Instances/&lt;study-id&gt;/</code> 内部的 System 布局；它和 Framework 的整个工作区布局不是同一层级。</p>
  </div>

  <div class="system-layout-map" aria-label="Study 内部目录布局">
    <div class="system-layout-tree" aria-label="Study 目录树">
      <p class="system-tree-context">Instances/</p>
      <button class="system-tree-entry system-tree-root" type="button" data-study-key="study-root"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder">&lt;study-id&gt;/</span><span class="system-tree-note"># 一项实际研究</span></button>
      <div class="system-tree-children">
        <button class="system-tree-entry" type="button" data-study-key="state"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">00_state/</span><span class="system-tree-note"># 当前状态与决定</span></button>
        <button class="system-tree-entry" type="button" data-study-key="intake"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">01_intake/</span><span class="system-tree-note"># 研究请求与 intake</span></button>
        <button class="system-tree-entry" type="button" data-study-key="registry"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">02_registry/</span><span class="system-tree-note"># 登记与合规证据</span></button>
        <button class="system-tree-entry" type="button" data-study-key="protocol"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">03_protocol/</span><span class="system-tree-note"># 设计与当前方案</span></button>
        <button class="system-tree-entry" type="button" data-study-key="knowledge"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">04_knowledge/</span><span class="system-tree-note"># 本 Study 的知识与应用判断</span></button>
        <button class="system-tree-entry" type="button" data-study-key="memory"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">05_memory/</span><span class="system-tree-note"># 决策记忆与项目复盘</span></button>
        <button class="system-tree-entry" type="button" data-study-key="data"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">06_data/</span><span class="system-tree-note"># 项目数据工作面</span></button>
        <button class="system-tree-entry" type="button" data-study-key="analysis"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">07_analysis/</span><span class="system-tree-note"># 合同、环境、实现与运行</span></button>
        <p class="system-tree-line system-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span>00_contract/analysis_execution_contract.json</span></p>
        <p class="system-tree-line system-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span>05_runs/&lt;run-id&gt;/formal_run_manifest.json</span></p>
        <button class="system-tree-entry" type="button" data-study-key="results"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">08_results/</span><span class="system-tree-note"># 结果与当前结果权威</span></button>
        <p class="system-tree-line system-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |-</span><span>_manifests/current_result_authority.json</span></p>
        <p class="system-tree-line system-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span>runs/&lt;run-id&gt;/result_manifest.json</span></p>
        <button class="system-tree-entry" type="button" data-study-key="manuscript"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">09_manuscript/</span><span class="system-tree-note"># 手稿、表图与主张</span></button>
        <button class="system-tree-entry" type="button" data-study-key="submission"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">10_submission/</span><span class="system-tree-note"># 投稿、返修与录用</span></button>
        <button class="system-tree-entry" type="button" data-study-key="qa"><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">11_qa/</span><span class="system-tree-note"># 运行 QA</span></button>
        <p class="system-tree-line system-tree-depth-1"><span class="tree-branch" aria-hidden="true">|  |_</span><span>analysis_runs/&lt;run-id&gt;/analysis_run_qa_record.json</span></p>
        <button class="system-tree-entry" type="button" data-study-key="archive"><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder">12_archive/</span><span class="system-tree-note"># 最终归档</span></button>
      </div>
    </div>

    <aside class="system-inspector" aria-live="polite" aria-label="Study 目录说明">
      <p class="system-inspector-label">当前目录</p>
      <h3 id="study-inspector-title">&lt;study-id&gt;/</h3>
      <p id="study-inspector-body">一个实际 Study 的根目录。研究相关的方案、数据、运行、结果、手稿和投稿材料都留在这里，而不是混入 System 本身。</p>
      <p id="study-inspector-detail" class="system-inspector-detail">点击左侧目录查看它保存什么，以及它在研究推进中的位置。</p>
    </aside>
  </div>
</section>

<section class="component-section" aria-labelledby="collaboration-route-title">
  <div class="section-header">
    <div><p class="section-context">人机协作路线</p><h2 id="collaboration-route-title">研究如何推进</h2></div>
  </div>

  <div class="system-route-map" aria-label="研究阶段与专项 Skill 的关系图">
    <div class="system-route-board">
      <div class="system-route-trunk">
        <button type="button" class="system-route-primary" data-stage-key="1"><span>01</span><strong>研究请求</strong><small>开一个新对话，在对话框发送“我想开始一个新研究”</small></button>
        <span class="system-route-down" aria-hidden="true">↓</span>
        <button type="button" class="system-route-primary" data-stage-key="2"><span>02</span><strong>协作与工作区确认</strong><small>在对话框选择协作模式，再确认 Study、工作区和材料范围</small></button>
      </div>

      <div class="system-mode-branches" aria-label="研究协作模式">
        <details class="system-mode-branch system-mode-autonomous">
          <summary><span>需授权</span><span class="system-mode-copy"><strong>受限自主执行</strong><small>只限经批准范围内的一段连续工作</small></span></summary>
          <div class="system-mode-future"><p>先说明范围、允许输入和动作、输出位置、QA、停止条件、人类关卡和复核点；获得精确授权后，AI 才能在该范围内连续执行。它不是把整项研究自动交给 AI，也不替代研究、合规、结论或投稿决定。</p></div>
        </details>

        <details class="system-mode-branch system-mode-collaborative" open>
          <summary><span>默认方式</span><span class="system-mode-copy"><strong>人机交互研究</strong><small>你与 AI 逐步确认、推进、复核和收口</small></span></summary>
          <div class="system-route-flow system-flowchart" data-system-flow aria-label="人机交互研究流程图">
            <svg class="system-flow-connectors" aria-hidden="true" focusable="false">
              <defs>
                <marker id="system-flow-arrow-forward" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path fill="#61afef" d="M0,0 L0,6 L6,3 z"></path></marker>
                <marker id="system-flow-arrow-return" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path fill="#e5c07b" d="M0,0 L0,6 L6,3 z"></path></marker>
                <marker id="system-flow-arrow-stop" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path fill="#9aa5af" d="M0,0 L0,6 L6,3 z"></path></marker>
              </defs>
              <g data-system-flow-paths></g>
            </svg>
            <div class="system-flow-return-labels" aria-hidden="true"></div>

            <section class="system-flow-phase system-flow-phase-design" aria-labelledby="system-phase-design-title">
              <header><span>03–05</span><strong id="system-phase-design-title">确定研究思路</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="3" data-flow-node="3"><span>03</span><strong>确认研究问题</strong><small>把想研究什么、为什么值得研究先说清</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="4" data-flow-node="4"><span>04</span><strong>确认研究设计</strong><small>把研究对象、比较方式、结局、观察时间等关键设计事项定下来</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="5" data-flow-node="5"><span>05</span><strong>写研究计划书，准备伦理、登记与数据访问材料</strong><small>完成详细研究设计，按适用要求办理伦理与备案</small><span class="system-flow-skill-hint">满足条件时可联动 Skill：<b>research-ethics</b></span></button>
              </div>
            </section>

            <section class="system-flow-phase system-flow-phase-decision" aria-labelledby="system-phase-decision-title">
              <header><span>06</span><strong id="system-phase-decision-title">判断研究是否值得继续</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-key-part" data-stage-key="6" data-flow-node="key-part"><span>检查</span><strong>关键部分检查</strong><small>用研究核心部分，以较小范围判断研究是否值得继续。<br>也看它能否发展成一篇有价值、可诚实报告的论文；不以阳性或显著为唯一条件。</small></button>
              </div>
              <div class="system-flow-stage-row system-flow-decision-row">
                <div class="system-flow-decision" data-flow-node="feasibility-decision"><span>人类决定</span><strong>继续 / 附条件继续 / 重构 / 停止</strong><small>附条件继续时，列明每项条件及其最迟解决关卡；不能把初步检查写成最终研究结论。</small></div>
                <div class="system-flow-stop" data-flow-node="stop"><span>暂停 / 停止</span><small>保留判断、理由和未解风险；不再作为当前论文候选继续推进。</small></div>
              </div>
              <div class="system-flow-stage-row">
                <div class="system-flow-continuation" data-flow-node="6"><span>继续后</span><strong>锁定方案并开展正式分析</strong><small>声明分析性质，冻结正式运行版本；正式运行不覆盖旧版本</small><span class="system-flow-skill-hint">按具体任务可联动 Skill：<b>governed-engineering</b></span></div>
              </div>
            </section>

            <section class="system-flow-phase system-flow-phase-analysis" aria-labelledby="system-phase-analysis-title">
              <header><span>07–08</span><strong id="system-phase-analysis-title">形成可整体审查的研究材料</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="7" data-flow-node="7"><span>07</span><strong>完成结果与手稿</strong><small>先完成 Results，再按顺序完成其他章节</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="8" data-flow-node="8"><span>08</span><strong>联合审查全部材料</strong><small>把方案、运行、结果、手稿和声明一起核对</small></button>
              </div>
            </section>

            <section class="system-flow-phase system-flow-phase-submission" aria-labelledby="system-phase-submission-title">
              <header><span>09–11</span><strong id="system-phase-submission-title">从投稿到归档</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="9" data-flow-node="9"><span>09</span><strong>准备投稿包</strong><small>给出目标期刊和文章类型，整理投稿包</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="10" data-flow-node="10"><span>10</span><strong>处理编辑意见与返修</strong><small>提供意见，逐条决定并同步修改</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="11" data-flow-node="11"><span>11</span><strong>完成归档与复盘</strong><small>处理校样、权利和最终材料，再归档复盘</small></button>
              </div>
            </section>
          </div>
        </details>
      </div>
    </div>

    <aside class="system-route-inspector" aria-live="polite" aria-label="当前阶段说明">
      <p class="system-inspector-label">当前阶段</p>
      <h3 id="stage-inspector-title">01 研究请求</h3>
      <dl>
        <div><dt>从这里开始</dt><dd id="stage-inspector-start">新研究：开一个新对话，在对话框发送“我想开始一个新研究”。已有项目：给出 Study 名称或根目录，再说明当前任务。</dd></div>
        <div><dt>一起完成</dt><dd id="stage-inspector-work">先把目前知道的情况说出来即可。题目、数据或方法还不清楚也没关系；AI 会先帮你分清这是新研究、已有项目，还是先讨论一个想法。</dd></div>
        <div><dt>完成以后</dt><dd id="stage-inspector-next">你可以说“按这个方向继续”“我想换一种做法”或“先暂停”。确认继续后，才进入工作区、Study 名称和协作方式的讨论。</dd></div>
      </dl>
      <details id="stage-inspector-examples" class="system-route-examples" hidden>
        <summary id="stage-inspector-examples-title"></summary>
        <ol id="stage-inspector-examples-list"></ol>
      </details>
      <p class="system-route-boundary">绿色提示表示：此步骤可联动对应的 Skill。独立组件若进入 Study，只保留 <code>metadata-only</code> 信息；需要明确点名，Research System 不会自动启动它。</p>
    </aside>
  </div>
</section>

<section class="component-section" aria-labelledby="system-guides-title">
  <div class="section-header"><div><p class="section-context">继续进入</p><h2 id="system-guides-title">两条常见路线</h2></div></div>
  <div class="guide-links"><a href="../../user-paths/possible-new-study/">可能的新 Study</a><a href="../../user-paths/existing-study-manuscript-revision/">已有 Study、手稿与返修</a></div>
</section>

</div>

<script>
  (() => {
    const studyDescriptions = {
      "study-root": ["<study-id>/", "一个实际 Study 的根目录。研究相关的方案、数据、运行、结果、手稿和投稿材料都留在这里，而不是混入 System 本身。", "点击左侧目录查看它保存什么，以及它在研究推进中的位置。"],
      state: ["00_state/", "保存当前状态、生命周期决定、分析状态和冻结记录。它让后续审查能知道目前处于哪个阶段、什么决定仍有效。", "分析状态与冻结决定放在 00_state/lifecycle/；它们引用方案和治理记录，而不替代这些记录。"],
      intake: ["01_intake/", "保存研究请求、范围讨论和 intake 形成的当前材料。它是从不成熟想法走向可确认研究路径的工作面。", "仅在用户确认开始受控准备后建立；讨论中的口头想法不自动变成正式方案。"],
      registry: ["02_registry/", "保存登记、合规、访问和外部支持证据的工作面。治理事实应由真实来源支持，并与人类决定保持可追溯关系。", "02_registry/compliance/ 保存治理准备记录与相关材料；它不因有模板或字段就证明伦理、访问或登记已经完成。"],
      protocol: ["03_protocol/", "保存研究设计、五维分类和当前方案。time zero、测量窗、随访和行政截尾等具体设计问题在这里说明。", "需要伦理准备时，派生草稿可放在 03_protocol/derived/；当前方案本身不被草稿覆盖。"],
      knowledge: ["04_knowledge/", "保存本 Study 使用的知识、来源说明和应用判断。它把文献或知识的使用与项目结论、经验和正式规则分开。", "论文阅读 Skill 只有在用户明确选择阅读和后续保留时，才可能为这里形成受控交接。"],
      memory: ["05_memory/", "保存项目决策记忆、未解决问题和项目局部 retrospective。它帮助同一 Study 在修订、交接和归档时恢复上下文。", "项目经验默认留在这个 Study；是否成为共享经验或正式规则需要后续单独审查。"],
      data: ["06_data/", "保存项目授权范围内的数据工作材料、来源映射或项目快照。它的具体内容受数据权限、许可与本项目规则约束。", "建立目录不授予数据访问权，也不表示真实数据可被 System 自动读取。"],
      analysis: ["07_analysis/", "保存分析执行合同、环境、配置、实现、测试、正式运行和开发材料。正式运行使用不覆盖的 run 目录保留身份和输入配置。", "00_contract/ 中的 execution contract 引用方案、治理与分析状态；05_runs/<run-id>/ 保存一次正式运行的 manifest。"],
      results: ["08_results/", "保存各次运行的结果 manifest，以及指向当前可用结果的 authority 记录。表、图和手稿主张应从已审查的结果包形成。", "_manifests/current_result_authority.json 指向相关运行、结果、QA 和人类决定；它不能只凭自身证明结论正确。"],
      manuscript: ["09_manuscript/", "保存手稿源、表图、补充材料、主张登记和声明材料。它引用当前方案与结果，而不是重新定义它们。", "方法应回到方案和执行记录；结果应回到结果 manifest；讨论再解释证据强度与限制。"],
      submission: ["10_submission/", "保存目标期刊要求、投稿包、审稿意见、逐条回复、修订追踪和录用相关材料。", "每项回复都应能回到实际修改的位置；涉及方法、结果或主张的变更应重新核对受影响材料。"],
      qa: ["11_qa/", "保存分析运行和材料检查的 QA 记录、问题与修复后复核。", "analysis_runs/<run-id>/ 中的 QA 记录服务于运行与结果审查，不自动构成科学正确性或投稿许可。"],
      archive: ["12_archive/", "保存完成阶段需要保留的最终材料、版本和项目收尾记录。", "归档不等于公开；公开代码、材料或数据说明仍取决于实际权利和人类决定。"]
    };

    const stageDescriptions = {
      "1": {
        title: "01 研究请求",
        start: "新研究：开一个新对话，在对话框发送“我想开始一个新研究”。已有项目：给出 Study 名称或根目录，再说明当前任务。",
        work: "先把目前知道的情况说出来即可。题目、数据或方法还不清楚也没关系；AI 会先分清这是新研究、已有项目，还是先讨论一个想法，再告诉你还缺哪些关键信息。",
        next: "你可以说“按这个方向继续”“我想换一种做法”或“先暂停”。确认继续后，才进入工作区、Study 名称和协作方式的讨论。"
      },
      "2": {
        title: "02 协作与工作区确认",
        start: "在对话框发送“人机交互模式”，或发送“申请受限自主执行：<范围>”。随后给出候选工作区位置、Study 名称和预计材料范围。",
        work: "人机交互是默认方式：你决定研究方向、准入与结论，AI 协助整理、查验和执行已确认的任务。受限自主执行只适用于一段明确范围内的工作；申请本身不会启动它，还需要写清允许输入和动作、输出、QA、停止条件、人类关卡和复核点。",
        next: "确认候选 System、工作区位置、Study 名称、材料范围和停止边界后，才建立空工作区并进入问题与环境。申请受限自主执行时，先设计并取得该范围的精确授权；未获批准前，仍按人机交互方式推进。"
      },
      "3": {
        title: "03 确认研究问题",
        start: "先从你关心的现象或问题说起：你发现了什么、想弄清什么、为什么认为它值得研究。题目还不完整也可以。",
        work: "题目还不完整没有关系。需要查文献、指南或数据库时，先说明希望查什么、允许查到什么范围。",
        next: "讨论清楚后，再把它收成一个可以设计的研究问题。如果发现条件不合适，就换方向，或者先停在这里。"
      },
      "4": {
        title: "04 确认研究设计",
        start: "把第 03 阶段的问题落到一个可以执行的设计：研究谁、怎样比较、看什么结局、从何时开始观察、跟多久。",
        work: "设计要能说明时间线、资料和主要偏倚。因果或治疗效应问题会另行进入因果设计或目标试验模拟审查，不会只靠“数据库研究”这个名称下结论。",
        next: "设计能站住后，把当前做法写入方案草案，进入第 05 阶段准备研究计划书和治理材料。",
        examplesTitle: "确认设计时，顺手看四件事",
        examples: [
          "研究谁、比较什么、看什么结局。",
          "从什么时候开始观察，指标在什么时候测，结局跟多久。",
          "计划使用的资料是否可能提供需要的变量、时间信息和足够对象。",
          "是否会遇到选择偏倚、混杂、暴露发生在结局之后或 time zero 不一致。"
        ]
      },
      "5": {
        title: "05 写研究计划书，准备伦理、登记与数据访问材料",
        start: "把第 04 阶段的设计写成详细研究计划书；再按研究类型、机构和所在地要求，准备伦理审查、备案和数据访问所需材料。",
        work: "伦理、备案和访问要求不会完全相同，要以实际机构和数据方的要求为准。要使用 `research-ethics` 时，明确点名它，并提供 Study 根目录、允许读取的材料和希望生成的内容。",
        next: "先分清第 06 阶段的关键检查是否会读取真实材料。会读取的，先完成对应的访问与治理准备；不会读取的，可以保留已知缺口并进入第 06 阶段。"
      },
      "6": {
        title: "06 判断研究是否值得继续",
        start: "先选研究核心部分：用较小范围的检查，判断结果、数据和设计是否支持继续投入。",
        work: "先写下继续、附条件继续、重构或停止的判断标准；再在已允许范围内完成检查。它也会帮助判断这项研究能否发展成一篇有价值、可诚实报告的论文；阳性或显著不是唯一标准。",
        next: "看完后，由你决定继续、附条件继续、重构或停止。只有继续后，才锁定方案，记录分析状态和冻结正式运行版本，再开展正式分析。"
      },
      "7": {
        title: "07 完成结果与手稿",
        start: "在已有受控运行和结果包后，可以说“请先把这项 Study 的 Results 部分做完整，再按顺序完成其他章节”。",
        work: "先完成 Results 的图、表、文字和主张之间的核对；再依次完成 Methods、Discussion 与 Conclusion、Introduction、Abstract 或 Summary，以及声明、补充材料、投稿信和回复材料。期刊最终排版可以不同。",
        next: "当结果、手稿、图表、结果包和 QA 能够一起审查时，进入第 08 阶段；不要只留下单独的文字草稿或图片。",
        examplesTitle: "展开查看 Results 怎样逐层完成",
        examples: [
          "先定 Results 的结构：主要结果、次要结果、敏感性或探索性结果分别放在哪里；每个表和图负责说明什么。",
          "每个结果单元可先做图表、图文并行，或先写有限的结果文字。默认可图文并行，但在人工审查前必须把文字、图表和对应结果核对完整。",
          "按顺序复核：Results 整体目的 → 小节顺序 → 每段要说明什么 → 句子和主张 → 对应结果与图表 → 句子、图表和证据是否对应 → 段落、小节和整个 Results 是否连贯。",
          "Results 定下来后，Methods 回到方案和实际执行记录；Discussion 与 Conclusion 解释已经确定的结果和限制；Introduction、Abstract 或 Summary 最后与整篇文章核对。",
          "方法学论文、系统综述、定性研究或期刊采用特殊章节结构时，可以另行说明为什么换顺序；但不能借此改变结果事实或把探索写成预先验证。"
        ]
      },
      "8": {
        title: "08 联合审查全部材料",
        start: "可以说“请对这项 Study 的方案、运行、结果、手稿、声明和投稿材料做联合审查”。",
        work: "把方案、治理记录、运行、结果、手稿、声明和投稿材料放在一起核对。AI 会找出版本不一致、材料缺口和需要重新审查的地方；你来决定哪些必须修，哪些应当作为限制保留。",
        next: "没有与投稿相冲突的问题时，进入投稿包；若发现问题，就回到受影响的阶段修订后再审。"
      },
      "9": {
        title: "09 准备投稿包",
        start: "给出目标期刊和文章类型，并请求按该期刊当前要求整理投稿包。",
        work: "按一个明确的期刊和文章类型整理投稿路线。获得许可后，AI 会核对当前官方要求，把手稿、声明、图表、补充材料和必要记录组成一个版本化投稿包。",
        next: "投稿包准备好后，由你核对并决定是否实际提交；提交后，这条路线进入编辑决定、技术退回或审稿阶段。"
      },
      "10": {
        title: "10 处理编辑意见与返修",
        start: "提供编辑或审稿意见、Study 根目录和当前投稿路线，并说明希望先讨论还是直接规划逐条回应。",
        work: "把编辑或审稿意见逐条拆开：哪些接受、哪些部分接受、哪些解释后不改。每一个决定都要对应到实际修改的位置；若牵动方法、结果或主张，就一起判断是否补分析并重新审查。",
        next: "当修订稿、逐条回复和所有受影响材料已经同步更新，就可以再次联合审查，并按期刊路线决定重投或提交返修。"
      },
      "11": {
        title: "11 完成归档与复盘",
        start: "提供录用、校样、权利或发表后更正任务，并说明是否希望同时建立项目局部复盘。",
        work: "处理校样、版权或开放获取、最终材料和可能的发表后更正。若要复盘，AI 可以帮你整理这一项 Study 的经验；它默认仍只属于该项目，不会自动变成共享规则。",
        next: "最终材料、权利和归档状态清楚后，这个 Study 就可以收口。若出现值得推广的经验，之后再单独决定是否进入共享审查。"
      }
    };

    const studyTitle = document.getElementById("study-inspector-title");
    const studyBody = document.getElementById("study-inspector-body");
    const studyDetail = document.getElementById("study-inspector-detail");
    const studyEntries = document.querySelectorAll("[data-study-key]");
    const stageTitle = document.getElementById("stage-inspector-title");
    const stageStart = document.getElementById("stage-inspector-start");
    const stageWork = document.getElementById("stage-inspector-work");
    const stageNext = document.getElementById("stage-inspector-next");
    const stageExamples = document.getElementById("stage-inspector-examples");
    const stageExamplesTitle = document.getElementById("stage-inspector-examples-title");
    const stageExamplesList = document.getElementById("stage-inspector-examples-list");
    const stageEntries = document.querySelectorAll("[data-stage-key]");
    const systemFlow = document.querySelector("[data-system-flow]");

    const drawSystemFlow = () => {
      if (!systemFlow) return;
      const canvas = systemFlow.querySelector(".system-flow-connectors");
      const paths = systemFlow.querySelector("[data-system-flow-paths]");
      const labelLayer = systemFlow.querySelector(".system-flow-return-labels");
      const rootBox = systemFlow.getBoundingClientRect();
      if (!canvas || !paths || !labelLayer || rootBox.width === 0 || rootBox.height === 0) return;

      const getNodeBox = (key) => {
        const node = systemFlow.querySelector(`[data-flow-node="${key}"]`);
        if (!node) return null;
        const box = node.getBoundingClientRect();
        return {
          left: box.left - rootBox.left,
          right: box.right - rootBox.left,
          top: box.top - rootBox.top,
          bottom: box.bottom - rootBox.top,
          centerX: box.left - rootBox.left + box.width / 2,
          centerY: box.top - rootBox.top + box.height / 2
        };
      };

      const svgNamespace = "http://www.w3.org/2000/svg";
      const addPath = (className, d) => {
        const path = document.createElementNS(svgNamespace, "path");
        path.setAttribute("class", className);
        path.setAttribute("d", d);
        paths.appendChild(path);
      };
      const addLabel = (label, x, y) => {
        const text = document.createElement("span");
        text.className = "system-flow-return-label";
        text.style.left = `${Math.max(2, x)}px`;
        text.style.top = `${Math.max(2, y)}px`;
        text.textContent = label;
        labelLayer.appendChild(text);
      };
      const forward = (fromKey, toKey) => {
        const from = getNodeBox(fromKey);
        const to = getNodeBox(toKey);
        if (!from || !to) return;
        const sameLane = Math.abs(to.centerY - from.centerY) < 18;
        if (sameLane) {
          const movingRight = to.centerX >= from.centerX;
          const startX = movingRight ? from.right : from.left;
          const endX = movingRight ? to.left : to.right;
          const gap = Math.max(12, Math.abs(endX - startX) / 2);
          addPath(
            "system-flow-path-forward",
            `M ${startX} ${from.centerY} C ${startX + (movingRight ? gap : -gap)} ${from.centerY} ${endX - (movingRight ? gap : -gap)} ${to.centerY} ${endX} ${to.centerY}`
          );
          return;
        }

        const movingDown = to.centerY >= from.centerY;
        const startY = movingDown ? from.bottom : from.top;
        const endY = movingDown ? to.top : to.bottom;
        const gap = Math.max(16, Math.abs(endY - startY) / 2);
        addPath(
          "system-flow-path-forward",
          `M ${from.centerX} ${startY} C ${from.centerX} ${startY + (movingDown ? gap : -gap)} ${to.centerX} ${endY - (movingDown ? gap : -gap)} ${to.centerX} ${endY}`
        );
      };
      const returnTo = (fromKey, toKey, railIndex, label) => {
        const from = getNodeBox(fromKey);
        const to = getNodeBox(toKey);
        if (!from || !to) return;
        const rail = 8 + railIndex * 9;
        addPath(
          "system-flow-path-return",
          `M ${from.left} ${from.centerY} H ${rail} V ${to.centerY} H ${to.left}`
        );
        addLabel(label, rail + 3, (from.centerY + to.centerY) / 2 - 8);
      };
      const stopAt = (fromKey, toKey) => {
        const from = getNodeBox(fromKey);
        const to = getNodeBox(toKey);
        if (!from || !to) return;
        addPath(
          "system-flow-path-stop",
          `M ${from.right} ${from.centerY} H ${to.left}`
        );
      };

      paths.replaceChildren();
      labelLayer.replaceChildren();
      canvas.setAttribute("viewBox", `0 0 ${rootBox.width} ${rootBox.height}`);
      canvas.setAttribute("width", String(rootBox.width));
      canvas.setAttribute("height", String(rootBox.height));

      [["3", "4"], ["4", "5"], ["5", "key-part"], ["key-part", "feasibility-decision"], ["feasibility-decision", "6"], ["6", "7"], ["7", "8"], ["8", "9"], ["9", "10"], ["10", "11"]].forEach(([fromKey, toKey]) => forward(fromKey, toKey));
      returnTo("4", "3", 0, "重构");
      returnTo("feasibility-decision", "3", 1, "重构");
      returnTo("8", "6", 2, "修正");
      returnTo("10", "4", 3, "改方案");
      returnTo("10", "6", 4, "补分析");
      returnTo("10", "8", 5, "重审");
      stopAt("feasibility-decision", "stop");
    };

    const selectStudyEntry = (key) => {
      const entry = studyDescriptions[key];
      if (!entry) return;
      studyTitle.textContent = entry[0];
      studyBody.textContent = entry[1];
      studyDetail.textContent = entry[2];
      studyEntries.forEach((element) => element.classList.toggle("is-selected", element.dataset.studyKey === key));
    };

    const selectStage = (key) => {
      const entry = stageDescriptions[key];
      if (!entry) return;
      stageTitle.textContent = entry.title;
      stageStart.textContent = entry.start;
      stageWork.textContent = entry.work;
      stageNext.textContent = entry.next;
      const examples = entry.examples ?? [];
      stageExamples.hidden = examples.length === 0;
      stageExamplesTitle.textContent = entry.examplesTitle ?? "";
      stageExamples.open = false;
      stageExamplesList.replaceChildren(...examples.map((example) => {
        const item = document.createElement("li");
        item.textContent = example;
        return item;
      }));
      stageEntries.forEach((element) => element.classList.toggle("is-selected", element.dataset.stageKey === key));
    };

    studyEntries.forEach((element) => {
      element.addEventListener("click", () => selectStudyEntry(element.dataset.studyKey));
      element.addEventListener("focus", () => selectStudyEntry(element.dataset.studyKey));
    });
    stageEntries.forEach((element) => {
      element.addEventListener("click", () => selectStage(element.dataset.stageKey));
      element.addEventListener("focus", () => selectStage(element.dataset.stageKey));
    });
    window.addEventListener("resize", drawSystemFlow);
    document.querySelector(".system-mode-collaborative")?.addEventListener("toggle", () => requestAnimationFrame(drawSystemFlow));
    selectStudyEntry("study-root");
    selectStage("1");
    requestAnimationFrame(drawSystemFlow);
  })();
</script>
