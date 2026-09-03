---
title: 申请远端只读访问
---

<div class="guide-page database-access-guide remote-access-page" data-copy-label="复制申请模板" data-copied-label="已复制">

<header class="guide-header"><p class="guide-kind">Clinical Database · 申请访问</p><h1>申请远端只读访问</h1><div class="guide-intro"><p>你可以自行建设和维护一套临床数据库，也可以申请只读使用由管理员维护的数据库。</p><p>本页讲第二种情况。如果你还没有个人只读账户和连接资料，从这里开始。</p><p>先向管理员说明用途、需要访问的数据范围、使用设备和预计期限；获批并收到连接资料后，再配置客户端。</p></div></header>

<nav class="database-guide-nav" aria-label="本页导航"><strong class="database-guide-nav-label">本页导航</strong><a href="#before-request"><span>01</span>申请前确认</a><a href="#request-template"><span>02</span>发送申请</a><a href="#outcomes"><span>03</span>管理员回复</a><a href="#after-approval"><span>04</span>批准以后</a></nav>

<section class="guide-section" id="before-request"><div class="section-header"><div><p class="section-context">申请前</p><h2>先确认这些信息</h2></div><p>申请的是一名用户、一台设备和一段明确的数据范围，不是整个数据库的通行权限。</p></div><ul class="database-checklist"><li>要访问哪个数据库，以及具体需要哪些 schema 或来源。</li><li>用于哪项研究或工作，为什么需要远端查询。</li><li>是否已经取得相应的数据使用许可。</li><li>准备使用哪台 Windows 或 macOS 电脑。</li><li>计划从什么时候开始，预计使用到什么时候。</li><li>准备使用 DBeaver、psql，或两者都用。</li></ul><h3 class="database-subheading">设备可以先准备到哪一步</h3><div class="access-preparation-steps"><article><span>申请前</span><div><h4>先记录设备和使用信息</h4><p>可以先安装 Tailscale、DBeaver Community 或 psql。此时只需记录操作系统、设备名称、准备使用的 Tailscale 登录身份和客户端；还不需要配置数据库连接。</p></div></article><article><span>受邀后</span><div><h4>再确认 Tailscale 设备身份</h4><p>管理员邀请你加入获准的 Tailscale 网络后再登录；如果该网络启用了设备审批，还要等待管理员批准设备。设备已经出现在获准网络中以后，再按管理员要求提供设备名称和 Tailscale IPv4。</p></div></article></div><div class="command-pair device-check-commands"><article><h4>Windows PowerShell</h4><pre data-copy data-copy-label="复制命令" data-copied-label="已复制"><code>hostname
tailscale version
tailscale status
tailscale ip -4</code></pre></article><article><h4>macOS shell</h4><pre data-copy data-copy-label="复制命令" data-copied-label="已复制"><code>scutil --get ComputerName
tailscale version
tailscale status
tailscale ip -4</code></pre></article></div><div class="db-notice"><strong>不需要提供普通网络 IP</strong><p>不要提交 Wi-Fi 局域网 IP 或公网 IP。它们不是本方法识别获准设备的依据。通常只提供设备名称、操作系统、Tailscale 登录身份，以及管理员要求时提供 <code>tailscale ip -4</code> 返回的单行地址。</p></div><div class="db-notice"><strong>当前已验证的实施方式需要 Tailscale IPv4</strong><p>IMP-DB-002 使用获准客户端的 Tailscale IPv4 收窄服务器防火墙允许范围。因此，设备加入获准网络后需要把这个地址交给管理员；不需要提交普通网络 IP。</p></div><div class="db-notice"><strong><code>tailscale status</code> 用来自己检查连接</strong><p>确认本机已经在线即可。不要默认把完整输出贴进申请，因为其中可能列出同一网络中的其他设备；排障时也只提交管理员明确要求的部分。</p></div><p class="database-source-note">Tailscale 的设备审批和访问规则由网络管理员维护。参见 <a href="https://tailscale.com/docs/features/access-control/device-management/device-approval">Tailscale Device approval</a> 与 <a href="https://tailscale.com/docs/reference/tailscale-cli">Tailscale CLI</a>。</p><div class="db-notice db-notice-warning"><strong>申请材料中不要放秘密或患者数据</strong><p>不要发送密码、私钥、患者记录或凭据文件。每位用户申请自己的账户，不借用他人账户。</p></div></section>

<section class="guide-section" id="request-template"><div class="section-header"><div><p class="section-context">发送给管理员</p><h2>复制后补全这段申请</h2></div><p>尖括号中的内容需要替换；不适用的项目可以写“不适用”。</p></div><pre data-copy><code>我申请从远端电脑只读访问临床数据库。

申请人：&lt;姓名&gt;
所属团队：&lt;团队或课题组&gt;
联系方式：&lt;管理员认可的联系方式&gt;
研究或工作用途：&lt;用途&gt;
数据使用许可：&lt;已有许可或待核对状态&gt;
需要访问的数据库：&lt;数据库名称&gt;
需要访问的 schema 或来源：&lt;最小必要范围&gt;
使用设备：&lt;Windows 或 macOS；按管理员要求填写设备标识&gt;
设备名称：&lt;hostname 或 ComputerName&gt;
Tailscale 登录身份：&lt;用于加入获准网络的账户&gt;
Tailscale IPv4：&lt;设备获准加入后填写；尚未加入时写“待分配”&gt;
预计使用期限：&lt;开始日期至结束日期&gt;
计划使用的客户端：&lt;DBeaver、psql 或两者&gt;

请核对我还需要补充哪些材料，以及当前申请是批准、需要补充、暂缓还是不能批准。</code></pre><p class="database-source-note">通过管理员指定的渠道发送。公开网页、Git、截图和共享脚本都不适合传递密码或凭据。</p></section>

<section class="guide-section" id="outcomes"><div class="section-header"><div><p class="section-context">管理员回复</p><h2>申请会进入哪种状态</h2></div><p>“补充”和“暂缓”不是批准，也不是必须经历的固定步骤。</p></div><div class="permission-layers"><article><span>批准</span><div><h3>可以准备个人只读访问</h3><p>管理员建立个人账户、限定 schema 和期限，并准备 Tailscale 与 TLS 所需的连接资料。</p></div></article><article><span>补充</span><div><h3>申请信息还不完整</h3><p>按管理员指出的缺口补充用途、许可、设备或访问范围，然后重新核对。</p></div></article><article><span>暂缓</span><div><h3>当前条件尚未满足</h3><p>服务器、审批、证书或来源许可还没准备好。保留申请，条件成立后再继续。</p></div></article><article><span>拒绝</span><div><h3>当前请求不能批准</h3><p>管理员说明原因和可选方案；不能通过关闭 TLS、开放公网端口或借用账户绕过要求。</p></div></article></div></section>

<section class="guide-section" id="after-approval"><div class="section-header"><div><p class="section-context">批准以后</p><h2>拿到完整资料后再配置</h2></div><p>服务器、账户、证书和授权范围由管理员维护；研究人员只配置自己的电脑。</p></div><div class="evidence-split"><div><h3>管理员安全交付</h3><p>MagicDNS 名称、端口、数据库名、个人用户名、根 CA、允许访问的 schema 和使用期限。密码通过单独的安全渠道交付。</p></div><div><h3>研究人员配置并验证</h3><p>安装并登录获准的 Tailscale 网络，保存根 CA，配置 DBeaver 或 psql，然后核对 TLS、账户、schema 和只读权限。</p></div></div><div class="db-notice db-notice-warning"><strong>批准不代表永久权限</strong><p>期限结束、设备丢失、人员变更或许可范围变化时，应联系管理员撤销 Tailscale 设备和数据库账户。</p></div><div class="guide-next-links"><a href="../client-setup/"><strong>配置并验证客户端</strong><span>Windows、macOS、DBeaver、psql 和只读验证</span></a><a href="../troubleshooting/"><strong>连接排障与安全</strong><span>网络、TLS、认证或权限出现问题时查看</span></a></div></section>

</div>
