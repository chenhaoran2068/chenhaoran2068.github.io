<div class="portal-home">

<header class="portal-home-header"><p class="portal-context">公開研究協働コンポーネント</p><h1>Research Collaboration</h1><div class="portal-lead home-intro-lead"><p>このサイトでは、これから増えていく Framework、System、Skill と関連資料を紹介します。</p><p>公開コンポーネントをダウンロードし、対応する AI 環境に設定できます。</p><p>組み合わせて使うと、資料を決まった場所に保ち、研究作業を順序立てて審査可能な形で進めやすくなります。</p></div></header>

<section class="portal-section role-explainer"><div class="section-header"><div><p class="section-context">基本概念</p><h2>Framework、System、Skills とは何か</h2></div></div><div class="role-terminal"><article class="role-terminal-entry"><h3>Framework</h3><p><span aria-hidden="true">|-</span> 作業空間の骨格と、資料の種類ごとの配置規則を提供します。</p><p><span aria-hidden="true">|-</span> 作業空間、共有サービス、プロジェクト、公開派生物を認識・維持しやすくします。</p><p><span aria-hidden="true">|_</span> 例：Systems、Skills、Methods、Instances、Knowledge に別々の場所を与えます。</p></article><article class="role-terminal-entry"><h3>System</h3><p><span aria-hidden="true">|-</span> 範囲のある作業を、ルート、記録、審査点として整理します。</p><p><span aria-hidden="true">|-</span> 作業が進む間、資料と決定を追跡可能に保ちます。</p><p><span aria-hidden="true">|_</span> 例：Research System は Study を依頼からアーカイブまで整理します。</p></article><article class="role-terminal-entry"><h3>Skills</h3><p><span aria-hidden="true">|-</span> 論文読解や限定された倫理資料準備など、名前のある作業に集中した支援を提供します。</p><p><span aria-hidden="true">|-</span> ユーザーが明示して条件がそろった時だけ入ります。</p><p><span aria-hidden="true">|_</span> 例：<code>research-paper-reading</code>、<code>research-ethics</code>、Governed Engineering。</p></article></div></section>

<section class="portal-section home-workspace-section" aria-labelledby="home-current-title-ja">
  <div class="section-header"><div><p class="section-context">現在公開・保守中</p><h2 id="home-current-title-ja">Framework、System、Skills を組み合わせると何が得られるか</h2></div><p>以下の作業空間は、現在のコンポーネントを組み合わせて使う一例です。</p></div>
  <div class="workspace-map" aria-label="展開できる作業空間コンポーネント図">
    <p class="workspace-tone-legend"><span class="workspace-tone-key workspace-framework-key">Framework の骨格</span><span class="workspace-tone-key workspace-system-key">System</span><span class="workspace-tone-key workspace-skill-key">Skill</span><span class="workspace-tone-key workspace-method-key">Method</span></p>
    <div class="workspace-map-layout">
      <div class="workspace-tree" aria-label="作業空間ディレクトリ">
        <details class="workspace-node workspace-root" open><summary><span class="tree-marker" aria-hidden="true">v</span><span class="tree-folder workspace-framework-tone">&lt;workspace&gt;/</span><span class="tree-translation"># 作業空間 Framework</span></summary><div class="workspace-children">
          <p class="framework-tree-line">|- <strong class="workspace-framework-tone">WORKSPACE_MANIFEST.yaml</strong></p>
          <details class="workspace-node" open><summary><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-system-tone">Systems/</span><span class="tree-translation"># ワークフロー System</span></summary><div class="workspace-children"><p class="framework-tree-line">|_ <a href="systems/governed-research-workflow/"><strong class="workspace-system-tone">Governed Research Workflow</strong></a></p></div></details>
          <details class="workspace-node" open><summary><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder workspace-skill-tone">Skills/</span><span class="tree-translation"># 専門機能</span></summary><div class="workspace-children"><p class="framework-tree-line">|- <a href="skills/research-ethics/"><strong class="workspace-skill-tone">research-ethics</strong></a></p><p class="framework-tree-line">|- <a href="skills/research-paper-reading/"><strong class="workspace-skill-tone">research-paper-reading</strong></a></p><details class="workspace-node workspace-skill-package" open><summary><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|_</span><span class="tree-folder workspace-skill-tone">governed-engineering/</span></summary><div class="workspace-children"><p class="framework-tree-line">|- <strong class="workspace-skill-tone">governed-code-change</strong></p><p class="framework-tree-line">|- <strong class="workspace-skill-tone">governed-database-change</strong></p><p class="framework-tree-line">|- <strong class="workspace-skill-tone">governed-data-ingestion</strong></p><p class="framework-tree-line">|- <strong class="workspace-skill-tone">governed-runtime-operation</strong></p><p class="framework-tree-line">|_ <strong class="workspace-skill-tone">audit-governed-delivery</strong></p></div></details></div></details>
          <p class="framework-tree-line">|- <strong>Shared/</strong> # 共有資料</p>
          <p class="framework-tree-line">|- <strong>Knowledge/</strong> # Knowledge サービス</p>
          <details class="workspace-node" open><summary><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><a href="methods/"><span class="tree-folder">Methods/</span></a><span class="tree-translation"># 方法とツール</span></summary><div class="workspace-children"><p class="framework-tree-line">|_ <a href="methods/clinical-database/"><strong class="workspace-method-tone">Clinical_Database/</strong></a></p></div></details>
          <details class="workspace-node workspace-study-layout" open><summary><span class="tree-marker" aria-hidden="true">&gt;</span><span class="tree-branch" aria-hidden="true">|-</span><span class="tree-folder">Instances/</span><span class="tree-translation"># プロジェクト実体</span></summary><div class="workspace-children"><p class="framework-tree-line">|_ <a href="systems/governed-research-workflow/#study-layout-title"><strong class="workspace-system-tone">&lt;study-id&gt;/</strong></a></p><div class="workspace-children workspace-study-directories"><p>|- <span class="workspace-system-tone">00_state/</span> # 現在の状態と決定</p><p>|- <span class="workspace-system-tone">01_intake/</span> # 依頼と intake</p><p>|- <span class="workspace-system-tone">02_registry/</span> # 登録と compliance の根拠</p><p>|- <span class="workspace-system-tone">03_protocol/</span> # デザインと現在の protocol</p><p>|- <span class="workspace-system-tone">04_knowledge/</span> # Study の知識と適用判断</p><p>|- <span class="workspace-system-tone">05_memory/</span> # 決定と振り返り</p><p>|- <span class="workspace-system-tone">06_data/</span> # 許可されたデータ作業</p><p>|- <span class="workspace-system-tone">07_analysis/</span> # 契約、コード、実行</p><p>|- <span class="workspace-system-tone">08_results/</span> # 結果と結果権威</p><p>|- <span class="workspace-system-tone">09_manuscript/</span> # 原稿、図表、主張</p><p>|- <span class="workspace-system-tone">10_submission/</span> # 投稿と改訂</p><p>|- <span class="workspace-system-tone">11_qa/</span> # 実行 QA</p><p>|_ <span class="workspace-system-tone">12_archive/</span> # 最終アーカイブ</p></div></div></details>
          <p class="framework-tree-line">|- <strong>Data_Raw/</strong> # 許可に基づくソースデータ</p><p class="framework-tree-line">|- <strong>Github/</strong> # Git 作業ツリー</p><p class="framework-tree-line">|- <strong>Ops/</strong> # runtime と保守</p><p class="framework-tree-line">|_ <strong>Archive/</strong> # 保持する履歴</p>
        </div></details>
      </div>
      <aside class="workspace-inspector"><p class="workspace-inspector-label">例と境界</p><h3>各領域に置けるもの</h3><p><strong>Shared/</strong>：プロジェクト間テンプレートや、審査済みの公開可能な派生物。</p><p><strong>Knowledge/</strong>：論文読解記録や、出典を追跡できる知識カード。</p><p><strong>Methods/</strong>：現在の Clinical Database を含む再利用可能な方法。</p><p><strong>Data_Raw/</strong>：MIMIC-IV や TCGA などは情報源名の例にすぎず、download やアクセス許可を意味しません。</p><p class="workspace-inspector-detail"><strong>Ops/</strong> は保守資料、<strong>Archive/</strong> は廃止済み履歴を置きます。どちらも現在のコンポーネント権威ではありません。</p><a class="workspace-inspector-link" href="framework/">Framework の参考レイアウトを開く</a></aside>
    </div>
    <p class="workspace-map-note"># 作業空間の所有・導入位置モデルであり、Git source や AI runtime の物理パスではありません。</p>
  </div>
</section>

<section class="portal-section home-setup-section"><div class="section-header"><div><p class="section-context">初回設定</p><h2>現在の公開中核を一度設定する</h2></div><p>以下の指示を対応する AI 環境にコピーします。空の候補ワークスペースを求めるもので、設定中に実際の研究作業は始めません。</p></div><pre class="home-setup-prompt"><code>新しい空の候補ワークスペースに、現在の公開 Research Collaboration 中核を設定してください。

何かを作る前に、提案するワークスペースパスを示し、私の確認を待ってください。既存ワークスペースの上書き、移行、読み取り、複製、推測はしないでください。

確認後、この AI 環境が次の正確な公開 Release を使えるか確認してください。
- Governed Research Workspace Framework v0.4.0
- Governed Research Workflow v1.18.1
- research-paper-reading v0.3.0
- research-ethics v1.1.1
- Governed Engineering v0.1.1

候補ワークスペースには、この公開コンポーネントだけを導入または設定してください。実際の Study を作成しない、実データ・論文・倫理資料・私有ファイルを読まない、Zotero など外部ツールを導入しない、事実としての倫理結論を作らない、分析・提出・公開を行わないでください。

設定完了後、正確な導入版、候補ワークスペースパス、満たせない環境要件、次に私が選ぶべきことを報告してください。</code></pre></section>

</div>
