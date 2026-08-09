<div class="component-category-page skills-category-page">

<header class="component-category-header">
  <div>
    <p class="map-context">PUBLIC SKILL</p>
    <h1>research-paper-reading</h1>
    <p>一个人类主导的单篇论文阅读 Skill：协助理解研究问题、方法、图表、论证、限制和未掌握点，但不把阅读会话误当作研究立项或知识库写入。</p>
  </div>
  <aside class="component-category-count" aria-label="当前公开版本">
    <strong>CURRENT RELEASE</strong>
    <span>v0.1.0</span>
  </aside>
</header>

<section class="component-category-section component-facts" aria-labelledby="reading-facts-title">
  <div class="component-category-section-heading">
    <p class="map-kicker">ENTRY AND BOUNDARY</p>
    <h2 id="reading-facts-title">何时使用</h2>
  </div>
  <dl>
    <div>
      <dt>进入条件</dt>
      <dd>用户明确要求阅读、理解、批判性审阅、图表解读或讨论一篇具体学术论文。</dd>
    </div>
    <div>
      <dt>默认模式</dt>
      <dd><code>session_only</code>：会话内解释与讨论，不自动保存笔记、不创建阅读档案，也不承诺后续导入。</dd>
    </div>
    <div>
      <dt>不会做</dt>
      <dd>不自动下载或复制论文、同步 Zotero 等文献管理器、创建知识记录、自动打标签，或启动新的 Study。</dd>
    </div>
  </dl>
</section>

<section class="component-category-section component-category-relationship" aria-labelledby="reading-relationship-title">
  <div class="component-category-section-heading">
    <p class="map-kicker">RELATIONSHIP</p>
    <h2 id="reading-relationship-title">与 Research System 的关系</h2>
  </div>
  <p>它是独立 Skill，不是 Governed Research Workflow 的下级。Research Workflow v1.11.0 只规定：明确阅读一篇论文的请求不应被误路由为“可能的新研究”。这保留了阅读 Skill 的独立入口，不会自动调用它、读取论文或创建记录。</p>
  <p>若用户同时明确要求从论文出发启动或规划新 Study，则应先进入 Research System 的新研究导航；阅读工作与研究立项仍是不同任务。</p>
</section>

<section class="component-category-section component-sources" aria-labelledby="reading-sources-title">
  <div class="component-category-section-heading">
    <p class="map-kicker">OFFICIAL SOURCES</p>
    <h2 id="reading-sources-title">正式来源</h2>
  </div>
  <ul>
    <li><a href="https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.1.0">v0.1.0 Release</a></li>
    <li><a href="https://github.com/chenhaoran2068/research-paper-reading/blob/v0.1.0/skill/research-paper-reading/SKILL.md">Skill entry</a></li>
    <li><a href="https://github.com/chenhaoran2068/research-paper-reading/blob/v0.1.0/PUBLIC_BOUNDARY.md">Public boundary</a></li>
  </ul>
</section>

</div>
