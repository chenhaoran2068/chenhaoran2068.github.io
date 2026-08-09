# research-paper-reading

**Category:** Skill
**Current public release:** [v0.2.0](https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.2.0)

This Skill helps a human understand a scholarly paper's question, design, methods, results, figures, limitations, and claim boundaries. It is an independent entry, not a child step of the Research System.

## Two modes

### Session reading

The default is `session_only`: explain and discuss in the current conversation without saving a dossier, paper, or knowledge record.

### Managed reading and knowledge service

Only after the user explicitly configures a Framework-supported local knowledge service can this Skill enter managed mode. Before downloading, importing, or saving anything for a paper, it still requires confirmation of the source, permitted action, and retention scope.

The Skill does not scan a workspace, write a reference-manager database directly, or automatically promote knowledge into experience, rules, or research conclusions.

## Relationship to the System

The Research System does not launch this Skill automatically. A limited metadata handoff to one named Study requires an explicit user decision; it never transfers paper text or PDFs.

### Formal sources

- [v0.2.0 Release](https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.2.0)
- [Skill entry](https://github.com/chenhaoran2068/research-paper-reading/blob/v0.2.0/skill/research-paper-reading/SKILL.md)
- [Public boundary](https://github.com/chenhaoran2068/research-paper-reading/blob/v0.2.0/PUBLIC_BOUNDARY.md)
