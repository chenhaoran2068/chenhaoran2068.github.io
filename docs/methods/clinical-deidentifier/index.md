---
title: Clinical Deidentifier
---

<div class="portal-page method-page">

<header class="portal-header"><p class="portal-context">METHOD / TOOL</p><h1>Clinical Deidentifier</h1><p>Windows 本地运行的结构化临床研究数据不可逆稳定假名化工具。</p></header>

<section class="portal-section"><div class="section-header"><div><p class="section-context">VERSION 0.2.0</p><h2>处理多个表格，同时保持关联编号一致</h2></div><p>作者：Chen Haoran · Apache License 2.0</p></div><p>支持 Excel、CSV、CSV.gz 和 Parquet。大表采用分批流式处理和临时磁盘验证索引；软件提供需人工确认的字段建议，并显示进度、支持安全取消。原始文件保持只读，结果写入新文件并生成审计报告。</p><div class="component-actions"><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier">查看源代码</a><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier/releases/tag/v0.2.0">下载 version 0.2.0</a></div></section>

<section class="portal-section"><div class="section-header"><div><p class="section-context">PUBLIC BOUNDARY</p><h2>当前使用边界</h2></div></div><ul><li>仅使用合成数据完成验证。</li><li>不识别或处理自由文本中的身份信息。</li><li>稳定假名仍可连接同一患者的多条记录，不自动等于完全匿名。</li><li>未经机构隐私、安全、伦理和数据治理审查，不得直接用于真实患者数据。</li><li>Windows EXE 尚未代码签名，可能显示“未知发布者”；请从GitHub Release下载并核对SHA-256。</li></ul></section>

</div>
