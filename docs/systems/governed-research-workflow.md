<div class="component-page system-page">

<header class="component-header">
  <p class="component-kind">System</p>
  <h1>Governed Research Workflow</h1>
  <p>帮助把一项 Study 从研究想法、设计、执行和结果，一直整理到手稿、返修与归档。</p>
</header>

<section class="component-section component-summary system-summary">
  <p>当一项研究需要持续保存方案、运行、结果、手稿和返修材料时，使用这个 System。它规定这些材料在 Study 内怎样组织，也保留关键决定的来处。</p>
  <div class="release-stamp"><span>当前公开 Release</span><strong><a href="https://github.com/chenhaoran2068/governed-research-workflow/releases/tag/v1.18.1">v1.18.1</a></strong></div>
</section>

<section class="component-section" aria-labelledby="study-status-title">
  <div class="section-header">
    <div><p class="section-context">v1.18 新增</p><h2 id="study-status-title">一眼看清 Study 现在在哪里</h2></div>
    <p>在 <code>00_state/study_status_snapshot.json</code> 留下一份简短、可核对的当前状态。</p>
  </div>
  <div class="boundary-grid">
    <div><h3>先记录运行状态</h3><p><code>queued</code> 表示等待开始，<code>active</code> 表示正在推进，<code>paused</code> 表示暂时搁置但可以恢复，<code>stopped</code> 表示当前路线已经终止，<code>archived</code> 表示材料已经收口归档。</p></div>
    <div><h3>正在推进时写清位置</h3><p>处于 <code>active</code> 时，还要记录当前在 01–11 的哪个阶段、正在处理什么，以及下一步要做的事或等待哪项人工决定。暂停或停止时，要保留原因和恢复条件。</p></div>
    <div><h3>状态必须由人和项目证据确认</h3><p>模板与校验器只检查字段是否完整、彼此是否矛盾，不会扫描目录猜测状态，也不会证明阶段正确、关卡已通过或某项决定已经获批。</p></div>
  </div>
</section>

<section class="component-section" aria-labelledby="paper-repository-title">
  <div class="section-header">
    <div><p class="section-context">v1.18.1 补充</p><h2 id="paper-repository-title">为一篇论文准备可公开的材料仓库</h2></div>
    <p>默认一篇论文或一项可独立引用的研究产出对应一个仓库；先在 Study 内准备，再由人决定是否发布。</p>
  </div>
  <div class="boundary-grid">
    <div><h3>先选择真实的公开方式</h3><p>根据权利和数据条件，选择合成示例、可再分发数据、仅提供数据获取说明，或只发布研究材料。公开仓库不是完整 Study 的复制品，也不自动包含真实数据和真实结果。</p></div>
    <div><h3>仓库名只保留稳定的识别信息</h3><p>根据研究类型，从研究对象或领域、核心问题、暴露或干预、结局、方法和产出类型中选两到三个稳定元素。完整研究问题与适用的 PICOS 或其他设计信息留在 README 和 Study 摘要中。</p></div>
    <div><h3>从允许清单建立干净候选</h3><p>使用模板记录纳入和排除的材料、代码与数据许可、运行方法、预期输出、引用信息和版本。候选必须建在新的干净目录，不能直接把 Study 根目录初始化成 Git 仓库。</p></div>
    <div><h3>通过审查后再进入 Github/</h3><p>发布记录和审查证据留在 Study 内。名称、范围和候选经人工确认后，只把核验过的干净候选放入 <code>Github/&lt;repository-name&gt;/</code>；不复制整个 Study，也不做双向同步。</p></div>
  </div>
</section>

<section class="component-section" aria-labelledby="joint-review-title">
  <div class="section-header">
    <div><p class="section-context">v1.15 新增</p><h2 id="joint-review-title">把联合审查的顺序写清楚</h2></div>
    <p>适合观察性实证原始研究的默认审查配置。</p>
  </div>
  <div class="boundary-grid">
    <div><h3>先由人选配置</h3><p>先确认这项研究适用哪一种审查配置。当前默认配置只面向观察性实证原始研究；试验、因果效应、预测模型、系统综述、定性或方法学研究等，需要另定专项配置。</p></div>
    <div><h3>再写出审查顺序</h3><p>把设计与治理事实、数据定义与执行、结果权威、Results、Methods、Discussion、Introduction、摘要和投稿材料依次列入审查计划。后面的修改影响前面已确认的部分时，记录重新审查，而不是静默沿用旧结论。</p></div>
    <div><h3>它只管理计划记录</h3><p>v1.15 只提供空模板、结构校验和重新打开审查的记录方式。它不自动选择配置，不读取 Study、数据、代码、结果或手稿，也不判断审查是否通过。</p></div>
  </div>
</section>

<section class="component-section" aria-labelledby="style-profile-title">
  <div class="section-header">
    <div><p class="section-context">v1.16 新增</p><h2 id="style-profile-title">手稿要求怎样进入 Study</h2></div>
    <p>把一般写作要求、研究类型的报告指南和目标期刊要求分开记录，再按明确顺序使用。</p>
  </div>
  <div class="boundary-grid">
    <div><h3>先放入当前写作配置</h3><p>手稿阶段在 <code>09_manuscript/drafting_requirement_stack.yaml</code> 记录当前使用的要求。常规医学健康研究可把 <code>ama_11_default</code> 作为一般写作起点；它只采用公开可核对的 AMA 衍生原则，不表示已逐条核对完整 AMA Manual。</p></div>
    <div><h3>再补研究类型与期刊要求</h3><p>根据研究类型补充适用的报告指南。确定目标期刊后，再加入该期刊当前的作者、图表、参考文献和声明要求；期刊要求与一般写作配置冲突时，以期刊当前要求为准。</p></div>
    <div><h3>冲突要重新交回给人</h3><p>目标期刊不能被用来静默删去报告指南要求。要求来源、当前性或冲突不清时，先指出缺口，由人确认后再改手稿、图表、引用或声明。</p></div>
  </div>
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
                <button type="button" class="system-flow-node" data-stage-key="5" data-flow-node="5"><span>05</span><strong>完成研究计划书，办理研究开始前的审查</strong><small>科学性论证、伦理、备案或登记、数据访问及其他所需材料</small><span class="system-flow-skill-hint">满足条件时可联动 Skill：<b>research-ethics</b></span></button>
              </div>
            </section>

            <section class="system-flow-phase system-flow-phase-decision" aria-labelledby="system-phase-decision-title">
              <header><span>06</span><strong id="system-phase-decision-title">判断研究是否值得继续</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-key-part" data-stage-key="6" data-flow-node="key-part"><span>检查</span><strong>关键部分检查</strong><small>用较小范围先看数据、定义和结果，判断是否值得继续投入。<br>也看能否发展成一篇有价值、可诚实报告的论文；不只看阳性或显著。</small></button>
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
                <button type="button" class="system-flow-node" data-stage-key="8" data-flow-node="8"><span>08</span><strong>联合审查全部材料</strong><small>把方案、运行、结果、手稿和投稿材料放在一起核对</small></button>
              </div>
            </section>

            <section class="system-flow-phase system-flow-phase-submission" aria-labelledby="system-phase-submission-title">
              <header><span>09–11</span><strong id="system-phase-submission-title">从投稿到归档</strong></header>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="9" data-flow-node="9"><span>09</span><strong>准备投稿包</strong><small>确定目标期刊和文章类型，按当前要求准备投稿材料</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="10" data-flow-node="10"><span>10</span><strong>处理编辑意见与返修</strong><small>提供意见，逐条决定并同步修改</small></button>
              </div>
              <div class="system-flow-stage-row">
                <button type="button" class="system-flow-node" data-stage-key="11" data-flow-node="11"><span>11</span><strong>完成归档与复盘</strong><small>处理校样、版权、开放获取和最终材料，再归档复盘</small></button>
              </div>
            </section>
          </div>
        </details>
      </div>
    </div>

    <aside class="system-route-inspector" aria-live="polite" aria-label="当前阶段说明">
      <p class="system-inspector-label">当前阶段</p>
      <h3 id="stage-inspector-title">01 研究请求</h3>
      <p id="stage-inspector-precondition" class="stage-inspector-precondition" hidden></p>
      <dl>
        <div><dt id="stage-inspector-start-label">先做什么</dt><dd id="stage-inspector-start">新研究：开一个新对话，在对话框发送“我想开始一个新研究”。已有项目：给出 Study 名称或根目录，再说明当前任务。</dd></div>
        <div><dt id="stage-inspector-work-label">这一步看什么</dt><dd id="stage-inspector-work">先把目前知道的情况说出来即可。题目、数据或方法还不清楚也没关系；AI 会先帮你分清这是新研究、已有项目，还是先讨论一个想法。</dd></div>
        <div id="stage-inspector-next-row"><dt id="stage-inspector-next-label">接下来</dt><dd id="stage-inspector-next">你可以说“按这个方向继续”“我想换一种做法”或“先暂停”。确认继续后，才进入工作区、Study 名称和协作方式的讨论。</dd></div>
      </dl>
      <details id="stage-inspector-guides" class="system-route-examples" hidden>
        <summary id="stage-inspector-guides-title"></summary>
        <div id="stage-inspector-guides-body" class="system-route-guide-groups"></div>
      </details>
      <p class="system-route-boundary">绿色提示表示：此步骤可联动对应的 Skill。独立组件若进入 Study，只保留 <code>metadata-only</code> 信息；需要明确点名，Research System 不会自动启动它。</p>
    </aside>
  </div>
</section>

</div>

<script>
  (() => {
    const studyDescriptions = {
      "study-root": ["<study-id>/", "这是一个实际 Study 的根目录。与这项研究有关的方案、数据、运行、结果、手稿和投稿材料都留在这里，不混进 System 本身。", "左侧目录按研究推进的顺序展开；点开任一项可以看它放什么、什么时候用。"],
      state: ["00_state/", "记录这项 Study 现在做到哪一步、已经作过的决定、分析状态和冻结版本。", "分析状态和冻结决定放在 00_state/lifecycle/；它们会引用方案和治理记录。"],
      intake: ["01_intake/", "放研究刚开始时的请求、范围讨论和 intake 材料。", "只有确认要开始受控准备后才建立；随口讨论的想法不直接变成正式方案。"],
      registry: ["02_registry/", "放伦理、登记、访问等相关材料，以及能说明当前状态的回执或记录。", "02_registry/compliance/ 用来保留治理准备和证据；只有实际材料和人类决定能说明这些事项目前到了哪一步。"],
      protocol: ["03_protocol/", "放研究设计、研究分类和当前方案；time zero、测量窗、随访和行政截尾等细节也在这里写清。", "伦理准备生成的草稿可单独放在 03_protocol/derived/，不覆盖当前方案。"],
      knowledge: ["04_knowledge/", "放这项 Study 会用到的知识、来源说明和应用判断。", "从阅读或知识服务转入的内容，先作为本 Study 的知识和应用判断，不等于共享规则。"],
      memory: ["05_memory/", "记录项目决定、还没解决的问题和项目复盘，方便修订、交接或归档时找回上下文。", "项目经验先留在这个 Study；是否值得成为共享经验或正式规则，之后再单独讨论。"],
      data: ["06_data/", "放在授权范围内可用于这项研究的数据工作材料、来源映射和项目快照。", "目录本身不带数据访问权限；能放什么取决于来源许可和项目决定。"],
      analysis: ["07_analysis/", "放分析怎样运行，以及开发和正式运行留下的设置、代码、测试和记录。", "00_contract/ 写正式执行合同；05_runs/<run-id>/ 为一次正式运行留下 manifest。"],
      results: ["08_results/", "放每次运行得到的结果，以及说明哪一份是当前可用结果的记录。", "表、图和手稿主张应从已审查的结果包形成；current_result_authority.json 会连回相关运行、QA 和决定。"],
      manuscript: ["09_manuscript/", "放手稿源、表图、补充材料、主张登记和声明材料。", "Methods 回到方案和实际执行记录；Results 回到结果 manifest；Discussion 再解释证据强度和限制。"],
      submission: ["10_submission/", "放期刊要求、投稿文件、审稿意见、逐条回复、修订记录和录用材料。", "每项回复都应能找到实际修改的位置；改到方法、结果或主张时，要重新看受影响材料。"],
      qa: ["11_qa/", "放分析运行和材料检查的 QA 记录，以及发现问题后怎样修复、怎样复核。", "QA 记录说明检查做了什么，不代替对研究结论或投稿的最后决定。"],
      archive: ["12_archive/", "放研究结束后还需要保留的最终材料、版本和收尾记录。", "归档不等于公开；是否公开代码、材料或数据说明，还要看实际权利和人类决定。"]
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
        start: "在对话框发送“人机交互模式”或“AI 自主模式”，再一起确认 Study 名称、候选工作区和准备处理的材料。",
        work: "人机交互是当前默认路线：研究方向、是否准入、怎样解释结果，都由你来定；AI 帮你把已经确认的事情往下做。AI 自主模式仍需先讨论适用范围和授权方式，不会因为选中它就直接开始自主执行。",
        next: "选择人机交互后，确认 System、Study 名称、工作区位置、准备处理的材料和暂停边界，再建立空工作区。选择 AI 自主模式时，先完成该模式的路线和授权设计；在此之前，不创建或运行任何研究工作。"
      },
      "3": {
        title: "03 确认研究问题",
        startLabel: "如果已经清楚自己的研究问题",
        start: "直接说明“我想研究……”，再补充研究对象或场景、想弄清的关系或现象，以及为什么值得研究。需要外查时，同时说明允许查什么。AI 会帮你把这个想法收成可以进入设计讨论的问题，并指出还要核实的地方。",
        workLabel: "如果尚不清楚自己的研究问题",
        work: "先说你所在的领域、关心的现象、已有经历或资源，以及希望解决什么实际或学术问题。可以授权 AI 查已有研究、指南和公开数据说明，比较几个可能的研究问题；再由你选择、合并或放弃其中一个方向。",
        next: ""
      },
      "4": {
        title: "04 确认研究设计",
        startLabel: "先分清五个方面",
        start: "分别说明：研究者是否分配干预；对象怎样进入研究；资料是前瞻、回顾还是双向；数据从哪里来；研究要回答描述、关联、因果、预后、预测还是诊断问题。不要把这些不同问题合并成一个“研究类型”标签。",
        workLabel: "再按两个方向写细",
        work: "先按对象怎样进入研究，确定纳入/排除、病例和对照选择或抽样等规则，并写清 time zero、测量窗口、随访和行政截尾。再按研究目的补足专门要求。预测、预后或诊断研究如果来自一个队列，仍要先写对象选择规则和时间线。",
        nextLabel: "设计清楚后",
        next: "把当前做法写成方案草案，再到第 05 阶段准备研究计划书和治理材料。",
        guidesTitle: "按研究类型查看要确定什么",
        guides: [
          {
            title: "对象怎样进入研究",
            items: [
              ["队列研究", "目标人群与来源、纳入/排除、队列起点或 time zero、测量窗口、随访和行政截尾。"],
              ["病例对照研究", "病例定义、病例如何确认、对照来自哪里、对照选择方式、参考时间，以及匹配规则（如有）。"],
              ["横断面研究", "目标人群、资格条件、抽样框或参与者来源、抽样或招募方式，以及测量时点。"],
              ["常规数据或数据库二次分析", "使用哪个数据源、时间范围、记录单位、识别、链接和去重规则；再说明它实际采用上面的哪一种对象选择方式。"]
            ]
          },
          {
            title: "研究要回答什么",
            items: [
              ["描述或关联", "暴露、结局、主要比较和可能影响比较的因素分别是什么。"],
              ["因果或治疗效应", "不按普通路线直接推进；另行进入因果设计或目标试验模拟审查，说明治疗策略、time zero、目标效应和混杂处理。"],
              ["预后或预测", "说明模型给谁用、何时使用、预测什么结局或时间窗、预测因子何时可得，以及是模型开发、内部验证还是独立验证。对象选择规则仍来自上面的设计。"],
              ["诊断准确性", "说明检测在临床上怎样使用、index test、reference standard、阈值、两者的时间间隔，以及不确定或缺失结果怎样处理。对象选择规则仍来自上面的设计。"]
            ]
          }
        ]
      },
      "5": {
        title: "05 完成研究计划书，办理研究开始前的审查",
        startLabel: "先做什么",
        start: "把第 04 阶段确定的设计写成完整研究计划书。研究想清楚后，不直接开始真实研究；先按实际机构和政策要求办完需要的审查、备案或登记和访问手续。",
        workLabel: "需要时可以点名",
        work: "准备中国大陆医学观察性研究的伦理或登记材料时，已经明确 Study 根目录、允许读取范围和目标交付物，就可以点名 `research-ethics` 协助整理和核对材料。实际的审查意见、备案或登记状态、数据访问权，以机构、数据方或平台回执为准。",
        nextLabel: "进入第 06 前",
        next: "第 06 阶段如果要读取真实材料，先核对伦理意见、备案或登记状态和数据访问条件是否已满足。没有满足时，继续完善材料，或只做非真实材料的准备与检查。",
        guidesTitle: "通常需要完成什么",
        guides: [
          {
            title: "常见的准备主线",
            items: [
              ["完整研究计划书", "把第 04 阶段定下来的研究问题、对象、设计、变量、时间线和分析思路写完整。"],
              ["科学性论证或审查", "说明问题为什么值得做、设计能否回答问题，以及风险和预期价值是否相称。有的机构会把它作为独立审查，有的会要求形成意见后随伦理申请提交。"],
              ["伦理审查", "按机构要求提交研究计划书、知情同意或豁免说明、数据来源证明等材料，并取得实际审查意见。"],
              ["备案或登记", "按研究类型、机构和所在地的要求办理；它与伦理审查不是同一件事。"],
              ["其他材料与访问手续", "视项目需要准备数据访问申请、隐私与安全说明、利益冲突、人员资质、经费说明或招募材料等。"]
            ]
          }
        ]
      },
      "6": {
        title: "06 判断研究是否值得继续",
        start: "选出研究最核心的一部分，用较小范围先看数据、定义和结果能否支撑后续投入。",
        work: "开始前，和 AI 约好这次检查要回答什么、什么情况算继续、需要补什么，什么情况应当回到前面重做或先停止。它也可以帮助判断研究是否值得做成论文；但阳性或显著不是唯一标准。",
        next: "检查结束后，由你决定继续、附条件继续、重构或停止。选择继续时，才锁定当前方案、记录分析状态并冻结正式运行版本，然后开始完整分析。"
      },
      "7": {
        title: "07 完成结果与手稿",
        precondition: "开始条件：已有受控运行和结果包。",
        startLabel: "01 完成 Results",
        start: "先安排主要、次要、敏感性和探索性结果分别放在哪里，并决定每张图表要说明什么。每个结果可先做图表、图文并行，或先写有限文字。完成后，从 Results 整体到小节、段落、句子和主张，再到图表和证据，一层层看它们是否对应、是否连贯。",
        workLabel: "02 完成其余手稿与提交材料",
        work: "Results 定下来后，Methods 回到方案和实际执行记录；Discussion 与 Conclusion 解释结果和限制；再完成 Introduction、Abstract 或 Summary。最后准备声明、补充材料、投稿信和回复材料。特殊研究或期刊需要调整章节时，说明调整原因。",
        nextLabel: "03 进入联合审查",
        next: "把全文、图表、结果包和 QA 放在一起核对；准备好后进入第 08 阶段。",
      },
      "8": {
        title: "08 联合审查全部材料",
        start: "把方案、运行、结果、手稿和准备投稿的材料放在一起看。",
        work: "对照同一个 Study 的当前版本，一项项核对：方案和实际执行是否一致；结果、图表、文字和主张是否对应；声明和投稿材料有没有漏项。发现问题就列出该回到哪个阶段；哪些只是限制，也明确写下来。",
        next: "需要处理的问题已经修好，或已明确作为限制保留后，再进入第 09 阶段。"
      },
      "9": {
        title: "09 准备投稿包",
        start: "确定目标期刊和文章类型，再按该期刊当前要求准备需要提交的材料。",
        work: "把手稿、声明、图表、补充材料和必要记录整理成这一次投稿对应的一套文件。期刊要求会变，核对时看当前官方要求，不只沿用旧模板。",
        next: "准备好后，由你核对并决定是否实际提交；提交后，这条路线进入编辑决定、技术退回或审稿阶段。"
      },
      "10": {
        title: "10 处理编辑意见与返修",
        start: "提供编辑或审稿意见、Study 根目录和当前投稿路线，并说明希望先讨论还是直接规划逐条回应。",
        work: "把编辑或审稿意见逐条拆开：哪些接受、哪些部分接受、哪些解释后不改。每一个决定都要对应到实际修改的位置；若牵动方法、结果或主张，就一起判断是否补分析并重新审查。",
        next: "当修订稿、逐条回复和所有受影响材料已经同步更新，就可以再次联合审查，并按期刊路线决定重投或提交返修。"
      },
      "11": {
        title: "11 完成归档与复盘",
        start: "录用、校样、版权、开放获取或发表后更正等事情，集中在这里处理；需要时再决定是否做项目复盘。",
        work: "核对校样和最终版本，处理版权或开放获取安排，保留之后还需要找得到的材料。复盘时，可以把这一个 Study 做过什么、遇到什么问题整理下来；它先留在项目里。",
        next: "该留下的最终材料和记录都齐全后，Study 就可以归档收口。某条项目经验是否值得成为共享经验，之后再单独讨论。"
      }
    };

    const studyTitle = document.getElementById("study-inspector-title");
    const studyBody = document.getElementById("study-inspector-body");
    const studyDetail = document.getElementById("study-inspector-detail");
    const studyEntries = document.querySelectorAll("[data-study-key]");
    const stageTitle = document.getElementById("stage-inspector-title");
    const stagePrecondition = document.getElementById("stage-inspector-precondition");
    const stageStartLabel = document.getElementById("stage-inspector-start-label");
    const stageStart = document.getElementById("stage-inspector-start");
    const stageWorkLabel = document.getElementById("stage-inspector-work-label");
    const stageWork = document.getElementById("stage-inspector-work");
    const stageNextLabel = document.getElementById("stage-inspector-next-label");
    const stageNext = document.getElementById("stage-inspector-next");
    const stageNextRow = document.getElementById("stage-inspector-next-row");
    const stageGuides = document.getElementById("stage-inspector-guides");
    const stageGuidesTitle = document.getElementById("stage-inspector-guides-title");
    const stageGuidesBody = document.getElementById("stage-inspector-guides-body");
    const stageInspector = document.querySelector(".system-route-inspector");
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

    const selectStage = (key, revealInspector = false) => {
      const entry = stageDescriptions[key];
      if (!entry) return;
      stageTitle.textContent = entry.title;
      stagePrecondition.textContent = entry.precondition || "";
      stagePrecondition.hidden = !entry.precondition;
      stageStartLabel.textContent = entry.startLabel || "先做什么";
      stageStart.textContent = entry.start;
      stageWorkLabel.textContent = entry.workLabel || "这一步看什么";
      stageWork.textContent = entry.work;
      stageNextLabel.textContent = entry.nextLabel || "接下来";
      stageNext.textContent = entry.next;
      stageNextRow.hidden = !entry.next;
      const guides = entry.guides ?? [];
      stageGuides.hidden = guides.length === 0;
      stageGuidesTitle.textContent = entry.guidesTitle ?? "";
      stageGuides.open = false;
      stageGuidesBody.replaceChildren(...guides.map((guide) => {
        const group = document.createElement("section");
        group.className = "system-route-guide-group";
        const heading = document.createElement("h4");
        heading.textContent = guide.title;
        const list = document.createElement("ul");
        list.replaceChildren(...guide.items.map(([label, detail]) => {
          const item = document.createElement("li");
          const term = document.createElement("strong");
          term.textContent = label;
          item.append(term, document.createTextNode("："), detail);
          return item;
        }));
        group.append(heading, list);
        return group;
      }));
      stageEntries.forEach((element) => element.classList.toggle("is-selected", element.dataset.stageKey === key));
      if (revealInspector) {
        requestAnimationFrame(() => {
          if (window.matchMedia("(max-width: 760px)").matches) {
            (stageInspector || stageTitle).scrollIntoView({ block: "start", behavior: "auto" });
            return;
          }
          if (!stageInspector) return;
          const stickyTop = Number.parseFloat(getComputedStyle(stageInspector).top) || 0;
          const currentTop = stageInspector.getBoundingClientRect().top;
          if (currentTop < stickyTop) {
            window.scrollBy({ top: currentTop - stickyTop, behavior: "auto" });
          }
        });
      }
    };

    studyEntries.forEach((element) => {
      element.addEventListener("click", () => selectStudyEntry(element.dataset.studyKey));
      element.addEventListener("focus", () => selectStudyEntry(element.dataset.studyKey));
    });
    stageEntries.forEach((element) => {
      element.addEventListener("click", () => selectStage(element.dataset.stageKey, true));
      element.addEventListener("focus", () => selectStage(element.dataset.stageKey));
    });
    window.addEventListener("resize", drawSystemFlow);
    document.querySelector(".system-mode-collaborative")?.addEventListener("toggle", () => requestAnimationFrame(drawSystemFlow));
    selectStudyEntry("study-root");
    selectStage("1");
    requestAnimationFrame(drawSystemFlow);
  })();
</script>
