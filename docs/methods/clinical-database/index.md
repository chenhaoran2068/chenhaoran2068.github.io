---
title: Clinical Database
---

<div class="portal-page clinical-database-overview database-access-guide" data-copy-label="复制" data-copied-label="已复制">

<header class="portal-header"><p class="portal-context">Method · 预览中</p><h1>Clinical Database</h1><p><strong>Clinical Database 是用于建设和维护标准化临床数据库的 Method。</strong><br>（1）公开仓库提供规则、代码和教程。<br>（2）获准使用的本地工作区还会保存数据处理材料和标准化结果。<br>（3）数据库部署并获得访问许可后，可以配置远端只读访问。</p></header>

<section class="portal-section" aria-labelledby="method-task-title">
  <div class="section-header"><div><p class="section-context">两个快捷使用方式</p><h2 id="method-task-title">你准备建设数据库，还是使用已有数据库？</h2></div></div>
  <div class="method-choice-list">
    <section class="method-choice" aria-labelledby="method-build-title">
      <div class="method-choice-intro"><span>01 · 建设数据库</span><h3 id="method-build-title">我想建设自己的临床数据库</h3></div>
      <div class="method-task-list method-choice-actions"><a href="https://github.com/chenhaoran2068/Clinical_Database"><span>公开方法仓库</span><strong>查看 Clinical_Database</strong><p>阅读来源接收、转换、校验和数据库建设材料。</p></a></div>
    </section>
    <section class="method-choice" aria-labelledby="method-use-title">
      <div class="method-choice-intro"><span>02 · 使用数据库</span><h3 id="method-use-title">我想使用管理员维护的数据库</h3></div>
      <nav class="method-task-list method-choice-actions database-step-links" aria-label="使用数据库步骤"><a href="#available-databases"><span>第一步</span><strong>选择数据库</strong></a><a href="#request-access"><span>第二步</span><strong>准备设备并申请</strong></a><a href="#configure-client"><span>第三步</span><strong>配置并验证</strong></a><a href="#database-other"><span>第四步</span><strong>排障与后续计划</strong></a></nav>
    </section>
  </div>
</section>

<section class="portal-section guide-section" id="available-databases" aria-labelledby="available-databases-title">
  <div class="section-header"><div><p class="section-context database-step-label">第一步</p><h2 id="available-databases-title">了解管理员当前维护的数据库</h2></div><p>点选左侧名称，在右侧查看说明。</p></div>
  <div class="database-selector" data-db-tabs>
    <div class="database-selector-list" role="tablist" aria-label="管理员当前维护的数据库" aria-orientation="vertical">
      <button type="button" role="tab" aria-selected="true" aria-controls="db-amsterdam" id="db-amsterdam-tab" data-tab-target="db-amsterdam">AmsterdamUMCdb 1.0.2</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-eicu" id="db-eicu-tab" data-tab-target="db-eicu">eICU-CRD 2.0</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-jmdc" id="db-jmdc-tab" data-tab-target="db-jmdc">JMDC</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-lianyungang" id="db-lianyungang-tab" data-tab-target="db-lianyungang">Lianyungang 2019–2024</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-mimic" id="db-mimic-tab" data-tab-target="db-mimic">MIMIC-IV 3.1</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-mimic-ed" id="db-mimic-ed-tab" data-tab-target="db-mimic-ed">MIMIC-IV-ED 2.2</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-nwicu" id="db-nwicu-tab" data-tab-target="db-nwicu">NWICU 0.1.0</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-sicdb" id="db-sicdb-tab" data-tab-target="db-sicdb">SICdb 1.0.8</button>
      <button type="button" role="tab" aria-selected="false" aria-controls="db-zigong" id="db-zigong-tab" data-tab-target="db-zigong">Zigong 1.1</button>
    </div>
    <div class="database-selector-panels">
      <section id="db-amsterdam" role="tabpanel" aria-labelledby="db-amsterdam-tab" data-tab-panel><p class="database-selector-kicker">AmsterdamUMCdb 1.0.2</p><h3>来自荷兰学术医疗中心的重症监护数据库</h3><p>主要材料围绕 ICU/MCU 入院、生命体征、实验室检查、用药和结局。适合重症监护相关研究；具体可读取的表仍以个人获批范围为准。</p></section>
      <section id="db-eicu" role="tabpanel" aria-labelledby="db-eicu-tab" data-tab-panel hidden><p class="database-selector-kicker">eICU-CRD 2.0</p><h3>多中心重症监护数据库</h3><p>包含多个医疗中心的 ICU 就诊、诊断、监测、治疗和结局材料。使用时需要注意不同中心之间的记录方式和缺失情况。</p></section>
      <section id="db-jmdc" role="tabpanel" aria-labelledby="db-jmdc-tab" data-tab-panel hidden><p class="database-selector-kicker">JMDC</p><h3>日本医疗索赔与健康检查相关数据</h3><p>可用于基于就诊、诊疗和健康检查记录的研究。具体交付版本、覆盖年份、字段和可用人群取决于当前授权，申请前应向管理员确认。</p></section>
      <section id="db-lianyungang" role="tabpanel" aria-labelledby="db-lianyungang-tab" data-tab-panel hidden><p class="database-selector-kicker">Lianyungang 2019–2024</p><h3>2019–2024 年临床数据</h3><p>这是按当前本地交付范围维护的临床数据库。申请时应写清研究用途和所需内容；可以读取哪些 schema、表和年份，以管理员批准结果为准。</p></section>
      <section id="db-mimic" role="tabpanel" aria-labelledby="db-mimic-tab" data-tab-panel hidden><p class="database-selector-kicker">MIMIC-IV 3.1</p><h3>医院与重症监护电子病历数据库</h3><p>包括住院、ICU、实验室检查、用药、操作和结局等材料。不同模块的时间轴和就诊标识需要在研究设计中分别核对。</p></section>
      <section id="db-mimic-ed" role="tabpanel" aria-labelledby="db-mimic-ed-tab" data-tab-panel hidden><p class="database-selector-kicker">MIMIC-IV-ED 2.2</p><h3>急诊就诊数据库</h3><p>重点覆盖急诊分诊、生命体征、诊断和急诊流程，可与获准的 MIMIC-IV 材料配合使用。申请时应单独写明需要 ED 数据。</p></section>
      <section id="db-nwicu" role="tabpanel" aria-labelledby="db-nwicu-tab" data-tab-panel hidden><p class="database-selector-kicker">NWICU 0.1.0</p><h3>重症监护数据库</h3><p>包含入院、监测、实验室检查、诊断及 ICU 事件等材料。当前页面只说明数据库已被维护，不代表所有表已向每位用户开放。</p></section>
      <section id="db-sicdb" role="tabpanel" aria-labelledby="db-sicdb-tab" data-tab-panel hidden><p class="database-selector-kicker">SICdb 1.0.8</p><h3>重症监护数据库</h3><p>包含病例、实验室检查、用药和高频数值记录等材料。研究时需要先确认病例时间轴、采样频率和获准使用的范围。</p></section>
      <section id="db-zigong" role="tabpanel" aria-labelledby="db-zigong-tab" data-tab-panel hidden><p class="database-selector-kicker">Zigong 1.1</p><h3>临床与随访结局数据库</h3><p>包含基线、诊断、用药、实验室检查、护理记录和随访结局等材料。具体字段和可用范围以当前交付及个人授权为准。</p></section>
    </div>
  </div>
</section>

<section class="portal-section guide-section" id="request-access" aria-labelledby="request-access-title">
  <div class="section-header"><div><p class="section-context database-step-label">第二步</p><h2 id="request-access-title">准备设备并申请个人只读访问</h2></div></div>
  <div class="guide-sequence">
    <article><span>01</span><div><h3>安装 Tailscale 和数据库查询工具</h3><ul class="step-software-list"><li><strong>必须安装：</strong>Tailscale</li><li><strong>图形化查询：</strong>DBeaver Community</li><li><strong>命令行查询（可选）：</strong>psql；macOS 可以通过 libpq 安装</li></ul><div class="os-tabs application-os-tabs" data-os-tabs><div class="os-tab-list" role="tablist" aria-label="选择安装软件的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="install-windows-panel" id="install-windows-tab" data-tab-target="install-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="install-macos-panel" id="install-macos-tab" data-tab-target="install-macos-panel">macOS</button></div><div class="os-tab-panels"><section id="install-windows-panel" role="tabpanel" aria-labelledby="install-windows-tab" data-tab-panel><h4>Windows</h4><p>按 <kbd>Win</kbd> 键。<br>输入“PowerShell”，打开 Windows PowerShell 或终端。<br>运行以下命令：</p><pre data-copy><code>winget install --id Tailscale.Tailscale --exact
winget install --id DBeaver.DBeaver.Community --exact</code></pre><ul><li><strong>Tailscale：</strong>连接管理员维护的私有网络。</li><li><strong>DBeaver Community：</strong>图形化查询数据库。</li><li><strong>psql（可选）：</strong>需要命令行查询或验证时，再通过 <a href="https://www.postgresql.org/download/windows/">PostgreSQL 官方 Windows 安装程序</a>安装 Command Line Tools。</li></ul></section><section id="install-macos-panel" role="tabpanel" aria-labelledby="install-macos-tab" data-tab-panel hidden><h4>macOS</h4><p>按 <kbd>Command</kbd> + <kbd>Space</kbd>。<br>输入“终端”或“Terminal”并打开。<br>已经安装 Homebrew 时，运行以下命令：</p><pre data-copy><code>brew install --cask tailscale-app
brew install --cask dbeaver-community

# 只有需要 psql 时，删除后面三行开头的 # 后执行
# brew install libpq
# echo 'export PATH="$(brew --prefix libpq)/bin:$PATH"' &gt;&gt; ~/.zshrc
# source ~/.zshrc</code></pre><ul><li><strong>Tailscale：</strong>安装后打开应用并等待管理员邀请或批准。</li><li><strong>DBeaver Community：</strong>用于图形化查询。</li><li><strong>libpq（可选）：</strong>提供 psql 命令。</li></ul></section></div></div></div></article>
    <article><span>02</span><div><h3>准备访问申请</h3><p>这一步只收集申请所需的信息，还不会连接数据库。按下面的顺序完成即可。</p><div class="application-info-group"><h4>1. 查询设备名称和系统版本</h4><div class="os-tabs application-os-tabs" data-os-tabs><div class="os-tab-list" role="tablist" aria-label="选择申请设备的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="application-windows-panel" id="application-windows-tab" data-tab-target="application-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="application-macos-panel" id="application-macos-tab" data-tab-target="application-macos-panel">macOS</button></div><div class="os-tab-panels"><section id="application-windows-panel" role="tabpanel" aria-labelledby="application-windows-tab" data-tab-panel><h5>Windows PowerShell</h5><pre data-copy><code>hostname
Get-ComputerInfo |
  Select-Object WindowsProductName, WindowsVersion, OsBuildNumber</code></pre><p><strong>示例：</strong></p><pre><code>PS&gt; hostname
RESEARCH-LAPTOP

WindowsProductName  WindowsVersion  OsBuildNumber
Windows &lt;edition&gt;   &lt;version&gt;      &lt;build&gt;</code></pre></section><section id="application-macos-panel" role="tabpanel" aria-labelledby="application-macos-tab" data-tab-panel hidden><h5>macOS Terminal</h5><pre data-copy><code>scutil --get ComputerName
sw_vers</code></pre><p><strong>示例：</strong></p><pre><code>&lt;user&gt;@Research-Mac ~ % scutil --get ComputerName
Research-Mac

ProductName:       macOS
ProductVersion:    &lt;version&gt;
BuildVersion:      &lt;build&gt;</code></pre></section></div></div><p>把查询到的<strong>设备名称</strong>和<strong>操作系统及版本</strong>留作申请填写。<br>示例中的名称和版本只是格式示意。</p></div><div class="application-info-group"><h4>2. 检查 Tailscale 是否可用</h4><div class="os-tabs application-os-tabs" data-os-tabs><div class="os-tab-list" role="tablist" aria-label="选择检查 Tailscale 的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="tailscale-check-windows-panel" id="tailscale-check-windows-tab" data-tab-target="tailscale-check-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="tailscale-check-macos-panel" id="tailscale-check-macos-tab" data-tab-target="tailscale-check-macos-panel">macOS</button></div><div class="os-tab-panels"><section id="tailscale-check-windows-panel" role="tabpanel" aria-labelledby="tailscale-check-windows-tab" data-tab-panel><h5>Windows PowerShell</h5><pre data-copy><code>tailscale version  # 检查是否已经安装；不用发给管理员
tailscale status   # 检查登录状态和当前 tailnet；不要整段发送
tailscale ip -4    # 获批加入管理员的 tailnet 后，取得本机地址</code></pre></section><section id="tailscale-check-macos-panel" role="tabpanel" aria-labelledby="tailscale-check-macos-tab" data-tab-panel hidden><h5>macOS Terminal</h5><pre data-copy><code>tailscale version  # 检查是否已经安装；不用发给管理员
tailscale status   # 检查登录状态和当前 tailnet；不要整段发送
tailscale ip -4    # 获批加入管理员的 tailnet 后，取得本机地址</code></pre></section></div></div><p>尚未获得管理员邀请或批准时，首次申请中的 Tailscale IPv4 填写“待邀请或批准后补交”。</p></div><div class="application-info-group"><h4>3. 补充两项申请信息</h4><ul class="step-software-list"><li><strong>Tailscale 登录身份：</strong>填写登录 Tailscale 使用的邮箱或账户。</li><li><strong>查询客户端：</strong>填写 DBeaver、psql，或两者。</li></ul></div></div></article>
    <article><span>03</span><div><h3>第一次联系管理员</h3><p>把完整申请一次发给管理员。</p><pre data-copy><code>主题：申请 Clinical Database 个人只读访问

申请人：&lt;姓名或团队身份&gt;
用途：&lt;研究、核对或教学用途；不要写患者信息&gt;
申请数据库及版本：&lt;database-name-and-version&gt;
申请范围：&lt;需要的 schema 或表；不清楚时写拟查询内容&gt;
使用期限：&lt;开始日期至结束日期&gt;
操作系统及版本：&lt;Get-ComputerInfo 或 sw_vers 的结果&gt;
设备名称：&lt;hostname 或 ComputerName 的结果&gt;
Tailscale 登录身份：&lt;登录 Tailscale 使用的邮箱或账户&gt;
Tailscale IPv4：&lt;尚未加入管理员维护的 tailnet，待邀请或批准后补交&gt;
查询客户端：&lt;DBeaver、psql 或两者&gt;

我申请个人只读账户，并接受只访问获准范围、不得共享账户或凭据的要求。</code></pre><p>不要发送普通 Wi-Fi 地址、公网 IP、密码、证书私钥或患者数据。</p></div></article>
    <article class="administrator-handoff"><span>管理员</span><div><h3>管理员审核并开放网络入口</h3><p>管理员核对申请人、用途、数据库范围和期限。<br>决定是否批准，以及批准到哪些 schema 或表。<br>申请获批后，邀请或批准这台设备加入管理员维护的 Tailscale 网络。</p><div class="admin-message-example"><h4>管理员第一次回复示例</h4><pre><code>申请状态：&lt;已批准 / 需要补充信息 / 未批准&gt;
批准数据库：&lt;database-name-and-version&gt;
批准范围：&lt;approved-schema-or-tables&gt;
使用期限：&lt;start-date&gt; 至 &lt;end-date&gt;

Tailscale：已向 &lt;tailscale-login-identity&gt; 发送邀请或完成批准。
请接受邀请并登录，然后补交这台设备的 Tailscale IPv4。</code></pre><p>实际回复可能使用邮件或其他获准渠道，字段名称不必完全相同。</p></div><p>这期间，申请人等待管理员回复即可。<br>收到邀请或批准后，再进入第 04 步。</p></div></article>
    <article><span>04</span><div><h3>接受邀请并补交 Tailscale IPv4</h3><div class="os-tabs application-os-tabs" data-os-tabs><div class="os-tab-list" role="tablist" aria-label="选择接受 Tailscale 邀请的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="join-windows-panel" id="join-windows-tab" data-tab-target="join-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="join-macos-panel" id="join-macos-tab" data-tab-target="join-macos-panel">macOS</button></div><div class="os-tab-panels"><section id="join-windows-panel" role="tabpanel" aria-labelledby="join-windows-tab" data-tab-panel><h4>Windows</h4><p>打开任务栏右下角系统托盘中的 Tailscale 图标。<br>选择登录，并使用申请中填写的 Tailscale 身份完成浏览器验证或接受邀请。<br>看到 Tailscale 已连接后，再打开 Windows PowerShell，在 PowerShell 中运行：</p><pre data-copy><code>tailscale status
tailscale ip -4</code></pre></section><section id="join-macos-panel" role="tabpanel" aria-labelledby="join-macos-tab" data-tab-panel hidden><h4>macOS</h4><p>打开屏幕右上角菜单栏中的 Tailscale 图标。<br>选择登录，并使用申请中填写的 Tailscale 身份完成浏览器验证或接受邀请。<br>看到 Tailscale 已连接后，再打开 Terminal（终端），在终端中运行：</p><pre data-copy><code>tailscale status
tailscale ip -4</code></pre></section></div></div><p>确认设备已经加入管理员维护的 tailnet，并且处于在线状态。<br>然后向管理员补发：</p><pre data-copy><code>申请人：&lt;姓名或团队身份&gt;
设备名称：&lt;设备名称&gt;
Tailscale 登录身份：&lt;登录邮箱或账户&gt;
Tailscale IPv4：&lt;tailscale ip -4 的实际结果&gt;</code></pre></div></article>
  </div>
</section>

<section class="portal-section guide-section" id="configure-client" aria-labelledby="configure-client-title">
  <div class="section-header"><div><p class="section-context database-step-label">第三步</p><h2 id="configure-client-title">配置客户端并确认连接可用</h2></div></div>
  <div class="handoff-checklist"><h3>管理员应交付这些内容</h3><ul><li>服务器的 MagicDNS 名称</li><li>PostgreSQL 端口和数据库名</li><li>你的个人只读用户名</li><li>根 CA 证书文件，不是任何私钥</li><li>获准读取的 schema、表和使用期限</li><li>单独安全交付的初始密码或设密方式</li></ul><div class="admin-message-example"><h4>管理员最终交付示例</h4><pre><code>Host：&lt;server-magicdns-name&gt;
Port：&lt;postgresql-port&gt;
Database：&lt;database-name&gt;
Username：&lt;read-only-user&gt;
Root CA：root-ca.crt
获准范围：&lt;approved-schema-or-tables&gt;
使用期限：&lt;start-date&gt; 至 &lt;end-date&gt;
密码：通过单独的安全渠道交付或由用户自行设置</code></pre><p>这里只展示交付格式。页面不会保存真实地址、账户、密码或证书内容。</p></div></div>
  <h3>先确认 Tailscale 已经连通</h3>
  <p>复制管理员交付内容中的 <strong>Host</strong>。<br>只把第三行的 <code>&lt;server-magicdns-name&gt;</code> 替换为该名称，尖括号也要一起删除。</p>
  <div class="os-tabs application-os-tabs" data-os-tabs><div class="os-tab-list" role="tablist" aria-label="选择检查 Tailscale 链路的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="link-windows-panel" id="link-windows-tab" data-tab-target="link-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="link-macos-panel" id="link-macos-tab" data-tab-target="link-macos-panel">macOS</button></div><div class="os-tab-panels"><section id="link-windows-panel" role="tabpanel" aria-labelledby="link-windows-tab" data-tab-panel><h4>Windows PowerShell</h4><pre data-copy><code>tailscale status&#10;tailscale ip -4&#10;tailscale ping &lt;server-magicdns-name&gt;</code></pre></section><section id="link-macos-panel" role="tabpanel" aria-labelledby="link-macos-tab" data-tab-panel hidden><h4>macOS Terminal</h4><pre data-copy><code>tailscale status&#10;tailscale ip -4&#10;tailscale ping &lt;server-magicdns-name&gt;</code></pre></section></div></div>
  <div class="handoff-checklist"><h3>满足这三项再继续</h3><ul><li><code>tailscale status</code> 中能找到自己的设备和管理员给出的数据库服务器。</li><li><code>tailscale ip -4</code> 返回本机的 Tailscale IPv4。</li><li><code>tailscale ping</code> 能收到服务器响应。</li></ul><p>任一项不满足时，先停止配置数据库连接，进入<a href="#database-other">常见问题和解决方法</a>。不要改用公网地址，也不要关闭 TLS 验证。</p></div>
  <h3>保存管理员交付的根 CA 证书</h3>
  <p>管理员提供的是根 CA 证书文件，通常以 <code>.crt</code> 或 <code>.pem</code> 结尾。它用于验证 PostgreSQL 服务器证书，不是密码，也不是服务器或客户端私钥。</p>
  <div class="os-tabs application-os-tabs" data-os-tabs>
    <div class="os-tab-list" role="tablist" aria-label="选择保存根 CA 证书的操作系统"><button type="button" role="tab" aria-selected="true" aria-controls="ca-windows-panel" id="ca-windows-tab" data-tab-target="ca-windows-panel">Windows</button><button type="button" role="tab" aria-selected="false" aria-controls="ca-macos-panel" id="ca-macos-tab" data-tab-target="ca-macos-panel">macOS</button></div>
    <div class="os-tab-panels">
      <section id="ca-windows-panel" role="tabpanel" aria-labelledby="ca-windows-tab" data-tab-panel>
        <h4>Windows</h4>
        <p>在 PowerShell 创建个人证书目录：</p>
        <pre data-copy><code>New-Item -ItemType Directory -Force -Path "$HOME\DatabaseAccess"</code></pre>
        <p>继续在 PowerShell 打开该目录：</p>
        <pre data-copy><code>explorer "$HOME\DatabaseAccess"</code></pre>
        <p>将管理员提供的证书文件复制到打开的目录中，并确认或统一命名为 <code>root-ca.crt</code>。最终路径应为：</p>
        <pre><code>C&#58;\Users\&lt;你的用户名&gt;\DatabaseAccess\root-ca.crt</code></pre>
        <p>回到 PowerShell，检查指定位置是否存在该文件：</p>
        <pre data-copy><code>Test-Path "$HOME\DatabaseAccess\root-ca.crt"</code></pre>
        <p>返回 <code>True</code> 只表示指定位置存在该文件，不代表证书来源和内容已经核验。如果管理员同时提供了证书指纹，应在使用前核对。</p>
      </section>
      <section id="ca-macos-panel" role="tabpanel" aria-labelledby="ca-macos-tab" data-tab-panel hidden>
        <h4>macOS</h4>
        <p>在 Terminal（终端）创建个人证书目录并限制目录权限：</p>
        <pre data-copy><code>mkdir -p "$HOME/Library/Application Support/DatabaseAccess"
chmod 700 "$HOME/Library/Application Support/DatabaseAccess"</code></pre>
        <p>继续在 Terminal 中打开该目录：</p>
        <pre data-copy><code>open "$HOME/Library/Application Support/DatabaseAccess"</code></pre>
        <p>将管理员提供的证书文件复制到打开的目录中，并确认或统一命名为 <code>root-ca.crt</code>。最终路径应为：</p>
        <pre><code>/Users/&lt;你的用户名&gt;/Library/Application Support/DatabaseAccess/root-ca.crt</code></pre>
        <p>回到 Terminal，限制文件权限并检查指定位置是否存在该文件：</p>
        <pre data-copy><code>chmod 600 "$HOME/Library/Application Support/DatabaseAccess/root-ca.crt"
test -f "$HOME/Library/Application Support/DatabaseAccess/root-ca.crt" &amp;&amp; echo "root CA exists"</code></pre>
        <p>看到 <code>root CA exists</code> 只表示指定位置存在该文件，不代表证书来源和内容已经核验。如果管理员同时提供了证书指纹，应在使用前核对。</p>
      </section>
    </div>
  </div>
  <div class="security-note"><h4>这个目录里不要保存什么</h4><p>不要保存数据库密码、服务器私钥、客户端私钥、包含私钥的证书、患者数据或无关凭据。</p><p>不要从群聊、公开网页或不明邮件附件中自行寻找根 CA，也不要用网上下载的同名文件替代管理员交付的文件。</p></div>
  <h3>选择操作系统和查询软件</h3>
  <p>选择当前使用的电脑和查询软件，只查看对应的配置。</p>
  <div class="os-tabs application-os-tabs client-configuration-tabs" data-os-tabs>
    <div class="os-tab-list client-option-list" role="tablist" aria-label="选择操作系统和查询软件"><button type="button" role="tab" aria-selected="true" aria-controls="client-windows-dbeaver-panel" id="client-windows-dbeaver-tab" data-tab-target="client-windows-dbeaver-panel">Windows · DBeaver</button><button type="button" role="tab" aria-selected="false" aria-controls="client-windows-psql-panel" id="client-windows-psql-tab" data-tab-target="client-windows-psql-panel">Windows · psql</button><button type="button" role="tab" aria-selected="false" aria-controls="client-macos-dbeaver-panel" id="client-macos-dbeaver-tab" data-tab-target="client-macos-dbeaver-panel">macOS · DBeaver</button><button type="button" role="tab" aria-selected="false" aria-controls="client-macos-psql-panel" id="client-macos-psql-tab" data-tab-target="client-macos-psql-panel">macOS · psql</button></div>
    <div class="os-tab-panels">
      <section id="client-windows-dbeaver-panel" role="tabpanel" aria-labelledby="client-windows-dbeaver-tab" data-tab-panel>
        <h3>在 DBeaver 新建 PostgreSQL 连接</h3>
        <div class="database-table-wrap"><table class="database-config-table"><thead><tr><th>项目</th><th>填写内容</th><th>说明</th></tr></thead><tbody><tr><td>Host</td><td><code>&lt;server-magicdns-name&gt;</code></td><td>必须与服务器证书中的主机名一致</td></tr><tr><td>Port</td><td><code>&lt;postgresql-port&gt;</code></td><td>使用管理员提供的端口</td></tr><tr><td>Database</td><td><code>&lt;database-name&gt;</code></td><td>不要自行改用其他数据库</td></tr><tr><td>Username</td><td><code>&lt;read-only-user&gt;</code></td><td>每人使用自己的账户</td></tr><tr><td>Password</td><td>连接时自行输入</td><td>不写进网页、脚本、截图或 Git</td></tr><tr><td>SSL mode</td><td><code>verify-full</code></td><td>同时验证 CA 和服务器主机名</td></tr><tr><td>Root certificate</td><td><code>$HOME\DatabaseAccess\root-ca.crt</code></td><td>选择上一节保存的根 CA</td></tr><tr><td>Client certificate / key</td><td>留空</td><td>除非以后明确启用 mTLS</td></tr><tr><td>Skip hostname validation</td><td>关闭</td><td>不要改成 <code>require</code> 规避主机名检查</td></tr></tbody></table></div>
      </section>
      <section id="client-windows-psql-panel" role="tabpanel" aria-labelledby="client-windows-psql-tab" data-tab-panel hidden>
        <h3>使用 psql 连接</h3>
        <p>在 PowerShell 中运行。命令不包含密码，psql 会在连接时要求输入。</p>
        <pre data-copy><code>$env:PGSSLMODE = 'verify-full'
$env:PGSSLROOTCERT = (Join-Path $HOME 'DatabaseAccess\root-ca.crt')
$env:PGCONNECT_TIMEOUT = '10'
$env:PGREQUIREAUTH = 'scram-sha-256'
$env:PGCHANNELBINDING = 'require'
psql -h '&lt;server-magicdns-name&gt;' -p '&lt;postgresql-port&gt;' -d '&lt;database-name&gt;' -U '&lt;read-only-user&gt;' -W</code></pre>
        <p><code>PGREQUIREAUTH</code> 和 <code>PGCHANNELBINDING</code> 需要客户端版本支持；不支持时应升级客户端，不要降低 TLS 验证。</p>
      </section>
      <section id="client-macos-dbeaver-panel" role="tabpanel" aria-labelledby="client-macos-dbeaver-tab" data-tab-panel hidden>
        <h3>在 DBeaver 新建 PostgreSQL 连接</h3>
        <div class="database-table-wrap"><table class="database-config-table"><thead><tr><th>项目</th><th>填写内容</th><th>说明</th></tr></thead><tbody><tr><td>Host</td><td><code>&lt;server-magicdns-name&gt;</code></td><td>必须与服务器证书中的主机名一致</td></tr><tr><td>Port</td><td><code>&lt;postgresql-port&gt;</code></td><td>使用管理员提供的端口</td></tr><tr><td>Database</td><td><code>&lt;database-name&gt;</code></td><td>不要自行改用其他数据库</td></tr><tr><td>Username</td><td><code>&lt;read-only-user&gt;</code></td><td>每人使用自己的账户</td></tr><tr><td>Password</td><td>连接时自行输入</td><td>不写进网页、脚本、截图或 Git</td></tr><tr><td>SSL mode</td><td><code>verify-full</code></td><td>同时验证 CA 和服务器主机名</td></tr><tr><td>Root certificate</td><td><code>$HOME/Library/Application Support/DatabaseAccess/root-ca.crt</code></td><td>选择上一节保存的根 CA</td></tr><tr><td>Client certificate / key</td><td>留空</td><td>除非以后明确启用 mTLS</td></tr><tr><td>Skip hostname validation</td><td>关闭</td><td>不要改成 <code>require</code> 规避主机名检查</td></tr></tbody></table></div>
      </section>
      <section id="client-macos-psql-panel" role="tabpanel" aria-labelledby="client-macos-psql-tab" data-tab-panel hidden>
        <h3>使用 psql 连接</h3>
        <p>在 Terminal 中运行。命令不包含密码，psql 会在连接时要求输入。</p>
        <pre data-copy><code>export PGSSLMODE='verify-full'
export PGSSLROOTCERT="$HOME/Library/Application Support/DatabaseAccess/root-ca.crt"
export PGCONNECT_TIMEOUT='10'
export PGREQUIREAUTH='scram-sha-256'
export PGCHANNELBINDING='require'
psql -h '&lt;server-magicdns-name&gt;' -p '&lt;postgresql-port&gt;' -d '&lt;database-name&gt;' -U '&lt;read-only-user&gt;' -W</code></pre>
        <p><code>PGREQUIREAUTH</code> 和 <code>PGCHANNELBINDING</code> 需要客户端版本支持；不支持时应升级客户端，不要降低 TLS 验证。</p>
      </section>
    </div>
  </div>
  <h3>连接后做一次不读取患者值的验证</h3>
  <pre data-copy><code>SELECT current_database(), current_user,
       current_setting('transaction_read_only') AS transaction_read_only;

SELECT ssl, version, cipher
FROM pg_stat_ssl
WHERE pid = pg_backend_pid();

SELECT has_schema_privilege(current_user, '&lt;approved-schema&gt;', 'USAGE')
       AS can_use_schema;

SELECT has_table_privilege(
  current_user,
  '&lt;approved-schema&gt;.&lt;approved-table&gt;',
  'SELECT'
) AS can_select_table;</code></pre>
  <p>成功连接只说明网络和认证可用；还要分别确认 TLS、schema 的 <code>USAGE</code> 和表的 <code>SELECT</code> 权限。不要用患者记录作为连接测试。</p>
  <h3>预期失败的写入探针</h3>
  <p>只有管理员事先批准 schema 和探针对象名称时才运行。先确认对象不存在，再在只读事务中尝试创建普通表；创建应直接失败。不要用临时表作为这项检查。</p>
  <pre data-copy><code>SELECT to_regclass('&lt;approved-schema&gt;.&lt;approved-write-probe&gt;') IS NULL
       AS safe_to_test;

BEGIN READ ONLY;
CREATE TABLE &lt;approved-schema&gt;.&lt;approved-write-probe&gt; (probe_id integer);
ROLLBACK;

SELECT to_regclass('&lt;approved-schema&gt;.&lt;approved-write-probe&gt;') IS NULL
       AS probe_absent;</code></pre>
  <div class="success-criteria"><h3>连接成功的判定标准</h3><ul><li>MagicDNS 服务器名称能够通过 Tailscale 到达。</li><li>DBeaver 或 psql 使用 <code>verify-full</code> 成功连接。</li><li>当前数据库和当前用户与管理员交付内容一致。</li><li>当前连接启用了 SSL，账户处于只读状态。</li><li>获准 schema 和表可以查询，未批准范围不可读取。</li><li>CREATE、INSERT、UPDATE、DELETE、TRUNCATE 和扩权操作不能成功。</li></ul></div>
</section>

<section class="portal-section guide-section" id="database-other" aria-labelledby="database-other-title">
  <div class="section-header"><div><p class="section-context database-step-label">第四步</p><h2 id="database-other-title">遇到问题，或希望增加数据库</h2></div></div>
  <div class="database-other-grid"><article><p class="database-option-kicker">连接没有成功</p><h3>常见问题和解决方法</h3><p>从设备在线状态开始，依次检查 MagicDNS、端口、TLS、认证和授权。</p><p>不要通过关闭 TLS 验证来绕过错误。</p><a class="database-option-action" href="troubleshooting/">查看排障步骤</a></article><article><p class="database-option-kicker">希望维护新数据库</p><h3>规划未来维护的数据库</h3><p>向管理员提交数据库正式名称、版本、官方来源和计划用途。</p><p>同时说明预计使用人群和需要的更新时间，供管理员评估许可、标准化工作量、存储和维护责任。</p></article></div>
</section>

</div>
