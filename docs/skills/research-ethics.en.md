<div class="component-page ethics-page">

<header class="component-header">
  <p class="component-kind">Skill · research-ethics</p>
  <h1>I want to prepare ethics and registration materials</h1>
  <p>Turn a defined mainland-China observational medical study into working drafts for the protocol, ethics review, filing, or registration.</p>
</header>

<section class="component-section component-summary">
  <p>This Skill belongs at stage 05 of the Research System: define the study first, then prepare the materials needed for ethics review, filing, or registration. A research idea alone does not enter this Skill automatically.</p>
  <div class="release-stamp"><span>Current public Release</span><strong><a href="https://github.com/chenhaoran2068/research-ethics/releases/tag/v1.1.1">v1.1.1</a></strong></div>
</section>

<section class="component-section" aria-labelledby="ethics-start-title">
  <div class="section-header"><div><p class="section-context">Before starting</p><h2 id="ethics-start-title">Provide these details first</h2></div></div>
  <dl class="facts-grid ethics-input-grid">
    <div><dt>Applicable study route</dt><dd>This version supports researcher-initiated observational medical studies in mainland China. Interventional studies, drug or device registration, and unverified platform routes need a specialist route.</dd></div>
    <div><dt>A specific Study</dt><dd>Provide the exact Study root. The Skill must not scan the workspace and guess which Study to use.</dd></div>
    <div><dt>Material mode</dt><dd>State whether this is <code>actual_submission</code> for a real submission or <code>test_public</code> for testing or public demonstration.</dd></div>
    <div><dt>Materials it may read</dt><dd>Name the protocol and compliance materials allowed for this task. One permission does not create continuing access.</dd></div>
    <div><dt>What to prepare</dt><dd>Specify the protocol, scientific review, ethics, filing, registration, data-access materials, or a selected subset.</dd></div>
    <div><dt>Expected deliverable</dt><dd>For example: a protocol skeleton, gap review, form-ready ethics or registry draft, attachment list, or paired Chinese and English content.</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-prompt-title">
  <div class="section-header"><div><p class="section-context">Use this when entering stage 05</p><h2 id="ethics-prompt-title">Copy this prompt to your AI</h2></div></div>
  <p>Fill in the actual Study, material mode, and permitted reading scope. The AI should first check whether the request fits the supported route. It must not submit materials, claim approval, or infer data-access status.</p>
  <pre class="ethics-setup-prompt"><code>I want to prepare ethics, filing, or registration materials.&#10;&#10;Study root: [enter the exact path]&#10;Material mode: [actual_submission / test_public]&#10;Materials permitted for this task: [list the protocol, compliance materials, or other approved scope]&#10;Requested deliverable: [for example, a protocol skeleton, gap list, ethics draft, registry draft, or attachment list]&#10;&#10;I authorize you to:&#10;1. First decide whether this request is within the current scope of research-ethics v1.1.1. If it is not, identify the specialist route and stop.&#10;2. Read only the permitted materials above and identify gaps in the protocol, scientific review, ethics, filing, registration, and data-access preparation.&#10;3. After listing unknowns and facts that need confirmation, prepare the requested drafts and checklists and state where they belong in the Study.&#10;&#10;Do not submit, upload, or send materials. Do not describe a preparation draft as approved, registered, or authorized for data access.</code></pre>
</section>

<section class="component-section" aria-labelledby="ethics-stage-title">
  <div class="section-header"><div><p class="section-context">At stage 05</p><h2 id="ethics-stage-title">From protocol to submission-ready materials</h2></div></div>
  <ol class="ethics-preparation-flow">
    <li><span>01</span><div><h3>Complete the protocol</h3><p>Write out the question, population, design, variables, timeline, and analysis approach. The Skill can build a protocol skeleton or identify what is still missing.</p></div></li>
    <li><span>02</span><div><h3>Prepare the scientific rationale</h3><p>Explain why the question matters, whether the design can answer it, and whether risks are proportionate to expected value. Formal scientific review follows the institution's actual process.</p></div></li>
    <li><span>03</span><div><h3>Check and draft ethics and registration materials</h3><p>The user first confirms study facts, structural choices, and unresolved items. Then prepare field-by-field drafts, attachment lists, and paired Chinese and English content where needed.</p></div></li>
    <li><span>04</span><div><h3>Follow the institution and platform process</h3><p>The researcher submits for review, filing, or registration under the applicable institutional, data-holder, and platform requirements. Formal receipts determine the actual status.</p></div></li>
  </ol>
</section>

<section class="component-section" aria-labelledby="ethics-scope-title">
  <div class="section-header"><div><p class="section-context">Current v1.1.1</p><h2 id="ethics-scope-title">Scope</h2></div></div>
  <dl class="facts-grid ethics-scope-grid">
    <div><dt>Currently supported</dt><dd>Mainland-China researcher-initiated observational medical studies, with diagnostic-study choices handled according to the actual design.</dd></div>
    <div><dt>Materials it can prepare</dt><dd>A general Chinese protocol skeleton, coverage-gap list, field-by-field platform drafts, and an attachment checklist.</dd></div>
    <div><dt>Two material modes</dt><dd><code>actual_submission</code> uses real materials only in an authorized private workspace. <code>test_public</code> is for testing or public demonstration and must be de-identified before saving.</dd></div>
    <div><dt>Needs another route</dt><dd>Interventional research, drug or device product registration, and unverified platform processes wait for their specialist modules.</dd></div>
  </dl>
</section>

<section class="component-section" aria-labelledby="ethics-storage-title">
  <div class="section-header"><div><p class="section-context">Relationship to a Study</p><h2 id="ethics-storage-title">Keep working drafts separate from formal facts</h2></div></div>
  <div class="ethics-storage-map">
    <div class="ethics-storage-tree" aria-label="Where ethics-preparation materials belong in a Study">
      <p><span class="tree-branch" aria-hidden="true">|-</span><code>03_protocol/derived/ethics_preparation/&lt;package_id&gt;/</code><span># drafts prepared by the Skill</span></p>
      <p><span class="tree-branch" aria-hidden="true">|_</span><code>02_registry/compliance/</code><span># actual ethics, registration, and access evidence</span></p>
      <p class="ethics-storage-child"><span class="tree-branch" aria-hidden="true">|_</span><code>01_ethics_and_consent/</code><span># ethics decisions and consent materials</span></p>
    </div>
    <div class="ethics-storage-copy"><p>Working drafts do not overwrite the current protocol. Ethics decisions, filing or registration status, and data-access status must be supported by actual records and receipts.</p><p>Institution-specific templates, attachments, and processes may be added in the private workspace. One institution's format must not be presented as a universal rule.</p></div>
  </div>
</section>

</div>
