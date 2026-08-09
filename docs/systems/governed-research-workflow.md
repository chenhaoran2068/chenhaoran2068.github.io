# Governed Research Workflow

**Category:** System
**Current public release:** [v1.12.0](https://github.com/chenhaoran2068/governed-research-workflow/releases/tag/v1.12.0)

This System provides governed routing for research tasks, lifecycle control, execution, manuscripts, and experience boundaries. It does not approve ethics, access data, submit work, or decide scientific conclusions.

## Reading and knowledge-service boundary

Reading a specific paper is an independent `research-paper-reading` Skill entry. The System does not start that Skill automatically.

Version 1.12.0 permits an optional, metadata-only Study handoff. It is available only after a user explicitly configures the managed service and makes a human decision for a specific Study. The System never receives a paper, PDF, reading dossier, knowledge card, or reference-manager database through this handoff.

The handoff is not evidence approval, a research conclusion, analysis approval, or a citation-compliance conclusion.

### Formal sources

- [v1.12.0 Release](https://github.com/chenhaoran2068/governed-research-workflow/releases/tag/v1.12.0)
- [System entry](https://github.com/chenhaoran2068/governed-research-workflow/blob/v1.12.0/SKILL.md)
- [Future Study lifecycle](https://github.com/chenhaoran2068/governed-research-workflow/blob/v1.12.0/references/future-study-lifecycle-design-governance-and-analysis-state.md)
- [Managed knowledge-service bridge](https://github.com/chenhaoran2068/governed-research-workflow/blob/v1.12.0/references/managed-reading-knowledge-service-bridge.md)
