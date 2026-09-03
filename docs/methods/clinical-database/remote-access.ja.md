---
title: リモート読み取り専用アクセスを申請する
---

<div class="guide-page database-access-guide remote-access-page" data-copy-label="申請テンプレートをコピー" data-copied-label="コピー済み">

<header class="guide-header"><p class="guide-kind">Clinical Database · アクセス申請</p><h1>リモート読み取り専用アクセスを申請する</h1><div class="guide-intro"><p>自分で臨床データベースを構築・管理することも、管理者が保守するデータベースの読み取り専用利用を申請することもできます。</p><p>本ページは後者を説明します。個人用の読み取り専用アカウントと接続資料がまだない場合は、ここから始めます。</p><p>用途、必要なデータ範囲、使用端末、予定期間を管理者に伝えます。承認され、接続資料を受け取ってからクライアントを設定します。</p></div></header>

<nav class="database-guide-nav" aria-label="このページの案内"><strong class="database-guide-nav-label">このページ</strong><a href="#before-request"><span>01</span>申請前の確認</a><a href="#request-template"><span>02</span>申請を送る</a><a href="#outcomes"><span>03</span>管理者の返信</a><a href="#after-approval"><span>04</span>承認後</a></nav>

<section class="guide-section" id="before-request"><div class="section-header"><div><p class="section-context">申請前</p><h2>必要な情報を確認する</h2></div><p>申請対象は一人の利用者、一台の端末、明確なデータ範囲です。データベース全体への無制限アクセスではありません。</p></div><ul class="database-checklist"><li>必要なデータベースと schema または情報源。</li><li>どの Study または作業で、なぜリモート検索が必要か。</li><li>必要なデータ利用許可を取得済みか。</li><li>使用する Windows または macOS 端末。</li><li>利用開始日と終了予定日。</li><li>DBeaver、psql、または両方のどれを使うか。</li></ul><h3 class="database-subheading">申請前に端末をどこまで準備できるか</h3><div class="access-preparation-steps"><article><span>申請前</span><div><h4>端末と利用情報を記録する</h4><p>Tailscale、DBeaver Community、psql は先にインストールできます。OS、端末名、使用予定の Tailscale ログイン ID、クライアントを記録します。データベース接続はまだ設定しません。</p></div></article><article><span>招待後</span><div><h4>Tailscale の端末 ID を確認する</h4><p>管理者から承認済み Tailscale ネットワークへ招待された後にログインします。端末承認が有効な場合は、その承認も待ちます。承認済みネットワークに端末が表示された後、管理者の指示に従って端末名と Tailscale IPv4 を伝えます。</p></div></article></div><div class="command-pair device-check-commands"><article><h4>Windows PowerShell</h4><pre data-copy data-copy-label="コマンドをコピー" data-copied-label="コピー済み"><code>hostname
tailscale version
tailscale status
tailscale ip -4</code></pre></article><article><h4>macOS Terminal</h4><pre data-copy data-copy-label="コマンドをコピー" data-copied-label="コピー済み"><code>scutil --get ComputerName
tailscale version
tailscale status
tailscale ip -4</code></pre></article></div><div class="db-notice"><strong>通常のネットワーク IP は提出しない</strong><p>Wi-Fi の LAN IP や公開 IP は送りません。この方法では通常、端末名、OS、Tailscale ログイン ID と、求められた場合に <code>tailscale ip -4</code> が返す一行のアドレスを使います。</p></div><div class="db-notice"><strong>検証済み実装では Tailscale IPv4 を使う</strong><p>IMP-DB-002 は、サーバーの firewall allowlist を承認済みクライアントの Tailscale IPv4 に限定しました。端末が承認済みネットワークへ参加した後、このアドレスを管理者に伝えます。通常のネットワーク IP は不要です。</p></div><div class="db-notice"><strong><code>tailscale status</code> は自分で接続を確認するために使う</strong><p>端末が online であることを確認します。出力には同じネットワークの他端末が含まれる場合があるため、全文を申請に貼りません。問題調査でも、管理者が求めた部分だけを送ります。</p></div><p class="database-source-note">端末承認とアクセス規則はネットワーク管理者が管理します。<a href="https://tailscale.com/docs/features/access-control/device-management/device-approval">Tailscale Device approval</a> と <a href="https://tailscale.com/docs/reference/tailscale-cli">Tailscale CLI</a> を参照してください。</p><div class="db-notice db-notice-warning"><strong>申請に秘密情報や患者データを入れない</strong><p>パスワード、秘密鍵、患者記録、資格情報ファイルを送りません。各利用者が個人アカウントを申請し、他人のアカウントを借りません。</p></div></section>

<section class="guide-section" id="request-template"><div class="section-header"><div><p class="section-context">管理者へ送る</p><h2>この申請をコピーして補完する</h2></div><p>山括弧内を置き換えます。該当しない項目は「該当なし」と記載できます。</p></div><pre data-copy><code>Clinical Database へのリモート読み取り専用アクセスを申請します。

申請者：&lt;氏名&gt;
所属：&lt;チームまたは研究グループ&gt;
連絡先：&lt;管理者が認める連絡方法&gt;
研究または作業の用途：&lt;用途&gt;
データ利用許可：&lt;取得済みの許可、または確認中の状態&gt;
必要なデータベース：&lt;データベース名&gt;
必要な schema または情報源：&lt;必要最小限の範囲&gt;
使用端末：&lt;Windows または macOS。管理者指定の端末識別情報&gt;
端末名：&lt;hostname または ComputerName&gt;
Tailscale ログイン ID：&lt;承認済みネットワークへ参加するアカウント&gt;
Tailscale IPv4：&lt;端末参加の承認後に記入。参加前は「割当待ち」&gt;
利用予定期間：&lt;開始日から終了日&gt;
使用予定クライアント：&lt;DBeaver、psql、または両方&gt;

追加で必要な資料と、現在の申請が承認、追加情報待ち、保留、承認不可のどれかを教えてください。</code></pre><p class="database-source-note">管理者が指定した経路で送ります。公開ページ、Git、スクリーンショット、共有スクリプトは、パスワードや資格情報の受け渡しに使いません。</p></section>

<section class="guide-section" id="outcomes"><div class="section-header"><div><p class="section-context">管理者の返信</p><h2>申請が取り得る状態</h2></div><p>「追加情報待ち」と「保留」は承認ではなく、必ず経由する固定手順でもありません。</p></div><div class="permission-layers"><article><span>承認</span><div><h3>個人用読み取り専用アクセスを準備できる</h3><p>管理者が個人アカウントを作り、schema と期間を限定し、Tailscale と TLS の接続資料を準備します。</p></div></article><article><span>追加情報</span><div><h3>申請情報が不足している</h3><p>管理者が示した用途、許可、端末、アクセス範囲の不足を補い、再度確認を依頼します。</p></div></article><article><span>保留</span><div><h3>必要な条件がまだ整っていない</h3><p>サーバー、承認、証明書、情報源の許可が未準備です。申請を残し、条件が整ってから再開します。</p></div></article><article><span>拒否</span><div><h3>現在の申請は承認できない</h3><p>管理者が理由と代替案を説明します。TLS の無効化、公開 port の開放、アカウント共有で回避しません。</p></div></article></div></section>

<section class="guide-section" id="after-approval"><div class="section-header"><div><p class="section-context">承認後</p><h2>接続資料がそろってから設定する</h2></div><p>サーバー、アカウント、証明書、権限範囲は管理者が保守します。研究者は承認された自分の端末だけを設定します。</p></div><div class="evidence-split"><div><h3>管理者が安全に渡す</h3><p>MagicDNS 名、port、database 名、個人 user 名、root CA、許可済み schema、利用期間を渡します。パスワードは別の安全な経路で渡します。</p></div><div><h3>研究者が設定・検証する</h3><p>承認済み Tailscale ネットワークへログインし、root CA を保存し、DBeaver または psql を設定して、TLS、アカウント、schema、読み取り専用権限を確認します。</p></div></div><div class="db-notice db-notice-warning"><strong>承認は永久アクセスではない</strong><p>期限終了、端末紛失、担当者変更、許可範囲変更の際は、管理者へ連絡して Tailscale 端末と database アカウントを失効させます。</p></div><div class="guide-next-links"><a href="../client-setup/"><strong>クライアントを設定・検証する</strong><span>Windows、macOS、DBeaver、psql、読み取り専用検証</span></a><a href="../troubleshooting/"><strong>接続問題と安全性</strong><span>network、TLS、認証、権限に問題がある場合</span></a></div></section>

</div>
