<div class="architecture-page">

<header class="architecture-page-header">
  <p class="map-context">COMPONENT RELATIONSHIP MAP</p>
  <h1>架构地图</h1>
  <p>本页说明 Frameworks、Systems 与 Skills 三类公开组件怎样连接，以及连接不意味着什么。具体组件和正式来源仍在各自分类页维护。</p>
</header>

<figure class="component-map component-map-page">
  <ol class="component-map-mobile" aria-label="移动端组件关系">
    <li><span>01</span><strong>Frameworks</strong><small>工作区边界、System 注册与项目绑定</small></li>
    <li><span>02</span><strong>Systems</strong><small>面向一类任务的生命周期、路由和正式规则控制</small></li>
    <li><span>03</span><strong>Skills</strong><small>可独立使用的专门能力；可在特定 System 路线中受控引用</small></li>
  </ol>
  <img src="../assets/architecture-map.svg" alt="Frameworks 为 Systems 提供工作区边界；Systems 仅能在特定模式或阶段受控引用独立 Skills 的类别关系图。">
  <figcaption>实线表示工作区与绑定关系；虚线表示满足特定条件后的受控引用。两者均不表示自动调用、从属关系、权限继承或事实性批准。</figcaption>
</figure>

<div class="map-reference-strip" aria-label="当前组件示例">
  <span>当前公开示例</span>
  <a href="framework/">Framework v0.3.0</a>
  <a href="systems/governed-research-workflow/">Research System v1.11.0</a>
  <a href="skills/">两个独立 Skills</a>
  <span>阅读 Skill 可直接因明确请求进入，不是 System 的下级。</span>
</div>

<section class="architecture-reading" aria-labelledby="reading-title">
  <div>
    <p class="map-kicker">HOW TO READ THE MAP</p>
    <h2 id="reading-title">连接的含义</h2>
  </div>
  <dl>
    <div><dt>Frameworks → Systems</dt><dd>Frameworks 提供工作区结构、注册与绑定边界；每个 System 在该边界内拥有其任务路线、生命周期和规则引用。</dd></div>
    <div><dt>Systems ··· Skills</dt><dd>Skills 不是 Systems 的下级。只有某个 System 的特定模式或阶段满足条件，且用户明确请求并确认输入范围时，才可受控引用相应 Skill。</dd></div>
    <div><dt>类别之间</dt><dd>类别连接不共享研究结论、伦理状态、数据访问权或投稿决定。每项事实仍需相应人类决定和真实证据。</dd></div>
  </dl>
</section>

<section class="architecture-boundaries" aria-labelledby="boundary-title">
  <p class="map-kicker">BOUNDARY</p>
  <h2 id="boundary-title">地图不代表什么</h2>
  <ul>
    <li>Frameworks 不决定某项研究的科学结论、伦理状态或投稿。</li>
    <li>Systems 不自动调用任何 Skill，也不自行批准伦理、数据访问或注册。</li>
    <li>Skills 不因被某条 System 路线引用而继承 Study、数据、平台或批准权限。</li>
  </ul>
</section>

<section class="architecture-scope" aria-labelledby="scope-title">
  <p class="map-kicker">PUBLIC SCOPE</p>
  <h2 id="scope-title">可见范围</h2>
  <p>本门户只列出公开维护的组件和公开版本。私有控制材料、本机安装状态、真实 Study、经验来源和未来模块均不在地图中。</p>
</section>

</div>
