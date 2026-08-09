<div class="portal-document-page">

<header class="portal-document-header">
  <p class="map-context">GOVERNANCE &amp; RELEASES</p>
  <h1>版本与兼容</h1>
  <p>门户只展示经过人工复核的公开 Release。安装、启用和本机 runtime 状态不由本页推断。</p>
</header>

<section class="portal-document-section release-directory" aria-labelledby="release-directory-title">
  <h2 id="release-directory-title">当前公开组件</h2>
  <table>
    <thead><tr><th>类别</th><th>组件</th><th>当前审查公开版本</th><th>用途</th></tr></thead>
    <tbody>
      <tr><td>Framework</td><td>Governed Research Workspace Framework</td><td><a href="https://github.com/chenhaoran2068/governed-research-workspace-framework/releases/tag/v0.3.0">v0.3.0</a></td><td>工作区结构、System 边界与通用知识服务注册</td></tr>
      <tr><td>System</td><td>Governed Research Workflow</td><td><a href="https://github.com/chenhaoran2068/governed-research-workflow/releases/tag/v1.11.0">v1.11.0</a></td><td>研究任务路由与治理；明确论文阅读的独立入口</td></tr>
      <tr><td>Skill</td><td>research-ethics</td><td><a href="https://github.com/chenhaoran2068/research-ethics/releases/tag/v1.1.1">v1.1.1</a></td><td>受限伦理与登记准备</td></tr>
      <tr><td>Skill</td><td>research-paper-reading</td><td><a href="https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.1.0">v0.1.0</a></td><td>人类主导的单篇论文理解与精读</td></tr>
    </tbody>
  </table>
</section>

<section class="portal-document-section" aria-labelledby="compatibility-title">
  <p class="map-kicker">CURRENT COMPATIBILITY</p>
  <h2 id="compatibility-title">当前关系</h2>
  <p>Framework v0.3.0 提供可选知识服务注册的通用边界。Research Workflow v1.11.0 只保留 research-paper-reading 的独立入口，不会自动调用该 Skill。research-ethics 与阅读 Skill 都保持独立合同、独立输入条件和独立 Release。</p>
</section>

<section class="portal-document-section" aria-labelledby="release-boundary-title">
  <p class="map-kicker">RELEASE BOUNDARY</p>
  <h2 id="release-boundary-title">门户显示什么</h2>
  <p>发布新的门户版本前，需逐项重新核对组件 tag、Release、正式文档链接和公开边界。门户链接到公开正式来源，但不替代组件各自的测试、发布控制或安装回执。</p>
</section>

</div>
