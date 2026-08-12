<div class="component-page ethics-page">

<header class="component-header">
  <p class="component-kind">Skill · research-ethics</p>
  <h1>我想准备伦理与备案材料</h1>
  <p>把已经确定的中国大陆医学观察性研究，整理成研究计划书、伦理或登记材料的准备稿。</p>
</header>

<section class="component-section component-summary">
  <p>它对应 Research System 的第 05 阶段：先把研究想清楚，再准备进入伦理、备案或登记流程所需的材料。刚有一个研究想法时，不会自动进入这里。</p>
  <div class="release-stamp"><span>当前公开 Release</span><strong><a href="https://github.com/chenhaoran2068/research-ethics/releases/tag/v1.1.1">v1.1.1</a></strong></div>
</section>

<section class="component-section" aria-labelledby="ethics-start-title">
  <div class="section-header"><div><p class="section-context">开始前</p><h2 id="ethics-start-title">先给出这几件事</h2></div></div>
  <dl class="facts-grid ethics-input-grid">
    <div><dt>适用的研究路线</dt><dd>当前版本支持中国大陆研究者发起的医学观察性研究。干预性研究、药品或器械注册，以及未核验的平台流程，需要另走专门路线。</dd></div>
    <div><dt>一个明确的 Study</dt><dd>给出准确 Study 根目录，不能由 Skill 自己扫描工作区后猜测要处理哪项研究。</dd></div>
    <div><dt>当前模式</dt><dd>说明是 <code>actual_submission</code> 的实际申报，还是 <code>test_public</code> 的测试或公开演示。</dd></div>
    <div><dt>允许读取的材料</dt><dd>说清本次可以使用哪些方案和合规材料；一次允许不自动扩大为持续访问。</dd></div>
    <div><dt>这次要做什么</dt><dd>明确是准备研究计划书、科学性审查、伦理、备案、登记、数据访问材料，还是其中的一部分。</dd></div>
    <div><dt>希望得到什么</dt><dd>例如计划书骨架、方案缺口审查、伦理或登记填写稿、附件清单，或需要配对的中英文内容。</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-prompt-title">
  <div class="section-header"><div><p class="section-context">进入第 05 阶段时可直接使用</p><h2 id="ethics-prompt-title">复制这段话给 AI</h2></div></div>
  <p>填入实际 Study、材料模式和本次允许读取的范围。AI 先核对是否属于当前支持路线，再整理材料；它不会替你提交申请、认定批准，或推断数据访问状态。</p>
  <pre class="ethics-setup-prompt"><code>我想准备伦理、备案或登记材料。&#10;&#10;Study 根目录：[填入准确路径]&#10;材料模式：[actual_submission / test_public]&#10;本次允许读取的材料：[列出方案、合规材料或其他允许范围]&#10;希望得到的交付物：[例如研究计划书骨架、缺口清单、伦理填写稿、登记填写稿或附件清单]&#10;&#10;我授权你：&#10;1. 先判断本请求是否属于 research-ethics v1.1.1 当前支持的路线；若不属于，说明应进入什么专门路线后停止。&#10;2. 只在上述允许范围内读取材料，核对研究计划书、科学性论证、伦理、备案、登记和数据访问准备中的缺口。&#10;3. 在明确缺口与待确认事实后，生成我点名的准备稿和清单，并说明它们应放在 Study 的什么位置。&#10;&#10;不要提交、上传或发送材料；不要把准备稿写成实际批准、登记完成或数据访问已获授权。</code></pre>
</section>

<section class="component-section" aria-labelledby="ethics-stage-title">
  <div class="section-header"><div><p class="section-context">在第 05 阶段</p><h2 id="ethics-stage-title">从研究计划书到可提交材料</h2></div></div>
  <ol class="ethics-preparation-flow">
    <li><span>01</span><div><h3>完成研究计划书</h3><p>把研究问题、对象、设计、变量、时间线和分析思路写完整。Skill 可以据此生成计划书骨架，或指出还缺哪些内容。</p></div></li>
    <li><span>02</span><div><h3>准备科学性论证</h3><p>说明问题为什么值得做、设计能否回答问题，以及风险和预期价值是否相称。Skill 可以帮助整理研究计划书中的相关内容；正式科学性审查按实际机构流程进行。</p></div></li>
    <li><span>03</span><div><h3>核对并生成伦理、登记准备稿</h3><p>先由用户确认研究事实、结构选择和未决项；再形成逐项填写稿、附件清单，必要时生成可配对的中英文内容。</p></div></li>
    <li><span>04</span><div><h3>按机构与平台流程办理</h3><p>研究者根据本机构、数据方和平台的要求送审、备案或登记。实际伦理意见、登记状态和数据访问状态，以正式回执为准。</p></div></li>
  </ol>
</section>

<section class="component-section" aria-labelledby="ethics-scope-title">
  <div class="section-header"><div><p class="section-context">当前 v1.1.1</p><h2 id="ethics-scope-title">适用范围</h2></div></div>
  <dl class="facts-grid ethics-scope-grid">
    <div><dt>当前支持</dt><dd>中国大陆研究者发起的医学观察性研究；可按研究实际情况处理诊断试验相关选择。</dd></div>
    <div><dt>可形成的材料</dt><dd>中国通用研究计划书骨架、材料缺口清单、平台逐项填写稿和附件准备清单。</dd></div>
    <div><dt>两种材料模式</dt><dd><code>actual_submission</code> 只在用户授权的私有工作区使用真实材料；<code>test_public</code> 用于测试或公开演示，保存前先去标识化。</dd></div>
    <div><dt>需要另走路线</dt><dd>干预性研究、药品或器械等产品注册，以及尚未核验的平台流程，等待对应专门模块后再处理。</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-storage-title">
  <div class="section-header"><div><p class="section-context">与 Study 的关系</p><h2 id="ethics-storage-title">准备稿和正式事实分开保留</h2></div></div>
  <div class="ethics-storage-map">
    <div class="ethics-storage-tree" aria-label="伦理准备材料在 Study 中的位置">
      <p><span class="tree-branch" aria-hidden="true">|-</span><code>03_protocol/derived/ethics_preparation/&lt;package_id&gt;/</code><span># Skill 生成的准备稿</span></p>
      <p><span class="tree-branch" aria-hidden="true">|_</span><code>02_registry/compliance/</code><span># 实际伦理、登记与访问相关证据</span></p>
      <p class="ethics-storage-child"><span class="tree-branch" aria-hidden="true">|_</span><code>01_ethics_and_consent/</code><span># 伦理意见与知情同意相关材料</span></p>
    </div>
    <div class="ethics-storage-copy">
      <p>准备稿不会覆盖当前研究方案。伦理意见、备案或登记状态，以及数据访问状态，都由实际材料和回执证明。</p>
      <p>具体医院模板、附件和流程可以在私有工作区补充；不能把一家机构的格式当作普遍规则。</p>
    </div>
  </div>
</section>

</div>
