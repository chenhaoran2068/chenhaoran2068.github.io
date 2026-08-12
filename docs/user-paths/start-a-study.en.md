<div class="portal-page guide-page study-start-page">

<header class="guide-header"><p class="section-context">GOVERNED RESEARCH WORKFLOW</p><h1>I want to do a research Study</h1><p>Start with an idea, an existing project, or a topic that is not yet clear. This page explains what to configure and what to send to an AI environment first.</p></header>

<section class="portal-section"><div class="section-header"><div><p class="section-context">Before you begin</p><h2>What you need</h2></div></div><div class="boundary-grid"><div><h3>A compatible AI environment</h3><p>It must be able to install and use the listed public components.</p></div><div><h3>A new workspace path</h3><p>Use an empty candidate directory. Do not overwrite or migrate an existing workspace while setting up.</p></div><div><h3>Your starting point</h3><p>It can be an incomplete idea, a named Study, or a narrow task in an existing Study.</p></div></div></section>

<section class="portal-section"><div class="section-header"><div><p class="section-context">Copy and send</p><h2>Configure first, then start</h2></div></div><pre class="study-setup-prompt"><code>Please set up a new candidate workspace for research collaboration. Before creating anything, show me the proposed empty workspace path and wait for my confirmation. Do not overwrite, migrate, read, copy, or infer from an existing workspace.

After I confirm, check whether this AI environment can use these exact public releases and configure them in the candidate workspace:
- Governed Research Workspace Framework v0.4.0
- Governed Research Workflow v1.15.0
- research-paper-reading v0.3.0
- research-ethics v1.1.1
- Governed Engineering v0.1.1

Do not create a real Study, read data or private files, download papers, prepare factual ethics conclusions, run analyses, submit anything, or publish anything during setup.

When setup is verified, I will tell you whether I want to start a new Study, continue an existing Study, or discuss an idea.</code></pre></section>

<section class="portal-section"><div class="section-header"><div><p class="section-context">Then begin</p><h2>What to send in the conversation</h2></div></div><div class="boundary-grid"><div><h3>A new Study</h3><p>Send: “I want to start a new research Study.” You may add the topic, data, or methods later.</p></div><div><h3>An existing Study</h3><p>Provide the Study name or root directory, then describe the task: revise a protocol, review results, write a manuscript, or address reviewer comments.</p></div><div><h3>Choose a mode</h3><p>Use human-AI collaboration by default. Use autonomous execution only for a bounded, explicitly approved segment of work.</p></div></div><p>For the full lifecycle, Study layout, and the point at which <code>research-ethics</code> may be named, see <a href="../../systems/governed-research-workflow/">Governed Research Workflow</a>.</p></section>

</div>
