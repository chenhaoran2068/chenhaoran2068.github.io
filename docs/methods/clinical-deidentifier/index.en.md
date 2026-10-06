---
title: Clinical Deidentifier
---

<div class="portal-page method-page">

<header class="portal-header"><p class="portal-context">METHOD / TOOL</p><h1>Clinical Deidentifier</h1><p>A local Windows tool for irreversible, stable pseudonymization of structured clinical research data.</p></header>

<section class="portal-section"><div class="section-header"><div><p class="section-context">VERSION 0.2.0</p><h2>Process multiple tables while preserving linked identifiers</h2></div><p>Author: Chen Haoran · Apache License 2.0</p></div><p>Supports Excel, CSV, CSV.gz, and Parquet. Large tables use chunked I/O and a temporary disk-backed validation index; field suggestions require user confirmation, and the interface shows progress with safe cancellation. Source files remain read-only; outputs are written as new files with an audit report.</p><div class="component-actions"><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier">View source</a><a class="component-entry-link" href="https://github.com/chenhaoran2068/clinical-deidentifier/releases/tag/v0.2.0">Download version 0.2.0</a></div></section>

<section class="portal-section"><div class="section-header"><div><p class="section-context">PUBLIC BOUNDARY</p><h2>Current limitations</h2></div></div><ul><li>Validated with synthetic data only.</li><li>Does not identify or de-identify personal information in free text.</li><li>Stable pseudonyms preserve linkability and do not automatically make data anonymous.</li><li>Institutional privacy, security, ethics, and data-governance review is required before real-patient-data use.</li><li>The Windows executable is unsigned and may show an unknown-publisher warning; download from GitHub Releases and verify SHA-256.</li></ul></section>

</div>
