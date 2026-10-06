---
title: Clinical Deidentifier
---

<div class="portal-page method-page">

<header class="portal-header"><p class="portal-context">METHOD / TOOL</p><h1>Clinical Deidentifier</h1><p>構造化された臨床研究データを不可逆かつ安定的に仮名化する、Windows向けローカルツールです。</p></header>

<section class="portal-section"><div class="section-header"><div><p class="section-context">VERSION 0.2.0</p><h2>複数テーブルの関連識別子を保ったまま処理</h2></div><p>作者：Chen Haoran · Apache License 2.0</p></div><p>Excel、CSV、CSV.gz、Parquetに対応します。大規模表は分割入出力と一時ディスク検証索引を使用し、列処理の提案は利用者の確認後にのみ適用されます。進捗表示と安全なキャンセルにも対応します。</p><div class="component-actions"><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier">ソースを見る</a><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier/releases/tag/v0.2.0">version 0.2.0をダウンロード</a></div></section>

<section class="portal-section"><div class="section-header"><div><p class="section-context">PUBLIC BOUNDARY</p><h2>現在の制約</h2></div></div><ul><li>合成データのみで検証済みです。</li><li>自由記載文中の個人情報は識別・仮名化しません。</li><li>安定仮名はレコード間の連結可能性を保つため、自動的に完全匿名とはなりません。</li><li>実患者データを使用する前に、所属機関のプライバシー、セキュリティ、倫理、データガバナンスの審査が必要です。</li><li>Windows EXEは未署名で「不明な発行元」と表示される場合があります。GitHub Releaseから取得し、SHA-256を確認してください。</li></ul></section>

</div>
