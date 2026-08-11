<div class="architecture-page">

<header class="architecture-header">
  <p class="portal-context">组件关系</p>
  <h1>架构地图</h1>
  <p>这张地图说明 Framework、Systems、Skills 和外部集成分别承担什么角色。具体组件、精确版本和正式来源仍由各自仓库维护。</p>
</header>

<section class="architecture-section" aria-labelledby="category-map-title">
  <div class="section-header"><div><p class="section-context">公开组件类别</p><h2 id="category-map-title">三类核心组件</h2></div><p>三者有受控关系，但不构成“System 自动调用 Skill”的层级链。</p></div>
  <div class="architecture-diagram">
    <article class="architecture-node"><span class="node-number">01</span><h3>Framework</h3><p>定义工作区骨架、所有权、System 注册与公共/私有边界。</p></article>
    <article class="architecture-node"><span class="node-number">02</span><h3>Systems</h3><p>定义一类任务的生命周期、路由、规则与治理。当前研究领域的 System 是 Governed Research Workflow。</p></article>
    <article class="architecture-node"><span class="node-number">03</span><h3>Skills</h3><p>独立的专门能力，可单独发布，也可打包分发。它们有各自的输入、输出和禁止边界，只在条件匹配时参与。</p></article>
  </div>
</section>

<section class="architecture-section" aria-labelledby="relationship-title">
  <div class="section-header"><div><p class="section-context">如何理解关系</p><h2 id="relationship-title">连接不是隶属</h2></div></div>
  <ul class="relationship-list">
    <li><strong>Framework 与 Systems</strong><span>Framework 提供通用工作区与绑定规则；每个 System 仍拥有自己的领域合同和项目内部结构。</span></li>
    <li><strong>Systems 与 Skills</strong><span>System 可以在明确条件下提示相关 Skill，但不能替该 Skill 自动作出输入确认、调用或结论。</span></li>
    <li><strong>Skills 与 Studies</strong><span>Skill 只在用户明确请求和其输入边界满足时工作；它不会自动创建 Study、访问材料或提升规则。</span></li>
  </ul>
</section>

<section class="architecture-external" aria-labelledby="external-title">
  <div><p class="section-context">独立类别</p><h2 id="external-title">外部集成</h2><p>外部工具不是 Framework、System 或 Skill。它们只在经过验证和明确配置后，按各自边界配合使用。</p></div>
  <a href="../integrations/" class="link-arrow">查看外部集成</a>
</section>

<section class="architecture-section" aria-labelledby="map-sources-title">
  <div class="section-header"><div><p class="section-context">当前入口</p><h2 id="map-sources-title">正式组件页</h2></div></div>
  <div class="guide-links">
    <a href="../framework/">Framework v0.4.0</a>
    <a href="../systems/governed-research-workflow/">Research System v1.13.0</a>
    <a href="../skills/">两个独立 Skill 与一个 Skill 包</a>
  </div>
</section>

</div>
