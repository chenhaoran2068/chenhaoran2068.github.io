<div class="component-page ethics-page">

<header class="component-header">
  <p class="component-kind">Skill · research-ethics</p>
  <h1>倫理審査・届出・登録資料を準備したい</h1>
  <p>内容が定まった中国本土の観察医学研究を、研究計画書、倫理審査、届出、登録のための準備稿に整理します。</p>
</header>

<section class="component-section component-summary">
  <p>Research System の第 05 段階で使う Skill です。研究内容を先に固め、その後で倫理審査、届出、登録に必要な資料を準備します。研究のアイデアだけでは自動的にこの Skill へ入りません。</p>
  <div class="release-stamp"><span>現在の公開 Release</span><strong><a href="https://github.com/chenhaoran2068/research-ethics/releases/tag/v1.1.1">v1.1.1</a></strong></div>
</section>

<section class="component-section" aria-labelledby="ethics-start-title">
  <div class="section-header"><div><p class="section-context">開始前</p><h2 id="ethics-start-title">先に示す情報</h2></div></div>
  <dl class="facts-grid ethics-input-grid">
    <div><dt>適用する研究ルート</dt><dd>現行版は中国本土の研究者主導観察医学研究に対応します。介入研究、医薬品・医療機器の登録、未検証のプラットフォーム手続には専門ルートが必要です。</dd></div>
    <div><dt>特定済みの Study</dt><dd>正確な Study ルートを示します。Skill がワークスペースを走査して対象を推測してはいけません。</dd></div>
    <div><dt>資料モード</dt><dd>実際の申請に使う <code>actual_submission</code> か、テスト・公開デモ用の <code>test_public</code> かを示します。</dd></div>
    <div><dt>読み取りを許可する資料</dt><dd>今回使ってよい研究計画書とコンプライアンス資料を指定します。一度の許可は継続的なアクセス許可ではありません。</dd></div>
    <div><dt>今回準備する内容</dt><dd>研究計画書、科学性審査、倫理、届出、登録、データアクセス資料、またはその一部を指定します。</dd></div>
    <div><dt>希望する成果物</dt><dd>研究計画書の骨格、不足項目の確認、倫理・登録の記入稿、添付資料一覧、中英対照内容などを指定します。</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-prompt-title">
  <div class="section-header"><div><p class="section-context">第 05 段階へ入る時に使えます</p><h2 id="ethics-prompt-title">この文章を AI にコピーする</h2></div></div>
  <p>実際の Study、資料モード、読み取り許可範囲を記入してください。AI は最初に対応範囲を確認します。申請の提出、承認済みという判断、データアクセス状態の推測は行いません。</p>
  <pre class="ethics-setup-prompt"><code>倫理審査、届出、登録資料を準備したいです。&#10;&#10;Study ルート：[正確なパス]&#10;資料モード：[actual_submission / test_public]&#10;今回読み取りを許可する資料：[研究計画書、コンプライアンス資料など許可範囲を列記]&#10;希望する成果物：[研究計画書の骨格、不足一覧、倫理記入稿、登録記入稿、添付資料一覧など]&#10;&#10;次の作業を許可します。&#10;1. この依頼が research-ethics v1.1.1 の現行対応範囲に入るか先に判断してください。範囲外なら必要な専門ルートを示して停止してください。&#10;2. 上記で許可した資料だけを読み、研究計画書、科学性審査、倫理、届出、登録、データアクセス準備の不足を確認してください。&#10;3. 不明点と確認が必要な事実を示した後、指定した準備稿とチェックリストを作り、Study 内の保存先を説明してください。&#10;&#10;資料を提出、アップロード、送信しないでください。準備稿を承認済み、登録済み、またはデータアクセス許可済みと表現しないでください。</code></pre>
</section>

<section class="component-section" aria-labelledby="ethics-stage-title">
  <div class="section-header"><div><p class="section-context">第 05 段階</p><h2 id="ethics-stage-title">研究計画書から提出可能な資料まで</h2></div></div>
  <ol class="ethics-preparation-flow">
    <li><span>01</span><div><h3>研究計画書を完成させる</h3><p>研究課題、対象、デザイン、変数、時間線、解析方針を書きそろえます。Skill は計画書の骨格を作るか、不足内容を示します。</p></div></li>
    <li><span>02</span><div><h3>科学的妥当性の説明を準備する</h3><p>研究する価値、デザインが問いに答えられるか、リスクと期待価値が釣り合うかを説明します。正式な科学性審査は各機関の手続に従います。</p></div></li>
    <li><span>03</span><div><h3>倫理・登録の準備稿を確認して作る</h3><p>研究事実、構成上の選択、未決事項を利用者が先に確認します。その後、項目別記入稿、添付資料一覧、必要な中英対照内容を作ります。</p></div></li>
    <li><span>04</span><div><h3>機関とプラットフォームの手続を進める</h3><p>研究者が所属機関、データ保有者、プラットフォームの要件に従って審査、届出、登録を行います。実際の状態は正式な記録と受領証で確認します。</p></div></li>
  </ol>
</section>

<section class="component-section" aria-labelledby="ethics-scope-title">
  <div class="section-header"><div><p class="section-context">現行 v1.1.1</p><h2 id="ethics-scope-title">対応範囲</h2></div></div>
  <dl class="facts-grid ethics-scope-grid">
    <div><dt>現在対応</dt><dd>中国本土の研究者主導観察医学研究。診断研究に関する選択は実際の研究デザインに応じて扱います。</dd></div>
    <div><dt>作成できる資料</dt><dd>中国向け一般研究計画書の骨格、不足一覧、プラットフォーム項目別記入稿、添付資料チェックリスト。</dd></div>
    <div><dt>二つの資料モード</dt><dd><code>actual_submission</code> は許可された非公開ワークスペースだけで実資料を使います。<code>test_public</code> はテスト・公開デモ用で、保存前に匿名化します。</dd></div>
    <div><dt>別ルートが必要</dt><dd>介入研究、医薬品・医療機器の製品登録、未検証のプラットフォーム手続は、対応する専門モジュールを待って扱います。</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-storage-title">
  <div class="section-header"><div><p class="section-context">Study との関係</p><h2 id="ethics-storage-title">準備稿と正式な事実を分けて保管する</h2></div></div>
  <div class="ethics-storage-map">
    <div class="ethics-storage-tree" aria-label="Study 内の倫理準備資料の保存先">
      <p><span class="tree-branch" aria-hidden="true">|-</span><code>03_protocol/derived/ethics_preparation/&lt;package_id&gt;/</code><span># Skill が作成した準備稿</span></p>
      <p><span class="tree-branch" aria-hidden="true">|_</span><code>02_registry/compliance/</code><span># 実際の倫理、登録、アクセス証拠</span></p>
      <p class="ethics-storage-child"><span class="tree-branch" aria-hidden="true">|_</span><code>01_ethics_and_consent/</code><span># 倫理判断と同意関連資料</span></p>
    </div>
    <div class="ethics-storage-copy"><p>準備稿は現在の研究計画書を上書きしません。倫理判断、届出・登録状態、データアクセス状態は、実際の資料と受領記録で裏付けます。</p><p>機関固有の様式、添付資料、手続は非公開ワークスペースで追加できます。一機関の形式を一般規則として扱ってはいけません。</p></div>
  </div>
</section>

</div>
