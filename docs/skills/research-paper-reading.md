# research-paper-reading

**Category:** Skill
**Current public release:** [v0.3.0](https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.3.0)

This Skill helps a human understand a scholarly paper's question, design, methods, results, figures, limitations, and claim boundaries. It is an independent entry, not a child step of the Research System.

## Guided close reading

Before explaining the paper, the Skill states the authorized source, reader goal,
reading level, and a coverage map. It then explains in source order:

- every in-scope section and substantive paragraph;
- definitions, methods, numerical claims, limitations, and logical transitions
  at the level the reader selected; and
- every in-scope table or figure, including its components, reading order,
  uncertainty, interpretation boundary, and likely misreadings.

The three reading levels are `full_close_reading` for every available in-scope
detail, `structured_close_reading` for ordinary guided reading, and
`focused_reading` for user-named content only. A session ends with an
understanding check and a recommendation-only closeout triage. The triage can
recommend a retained output, but it does not create, tag, import, or promote
anything automatically.

## Two modes

### Session reading

The default is `session_only`: explain and discuss in the current conversation without saving a dossier, paper, or knowledge record.

### Managed reading and knowledge service

Only after the user explicitly configures a Framework-supported local knowledge service can this Skill enter managed mode. Before downloading, importing, or saving anything for a paper, it still requires confirmation of the source, permitted action, and retention scope.

The Skill does not scan a workspace, write a reference-manager database directly, or automatically promote knowledge into experience, rules, or research conclusions.

## Relationship to the System

The Research System does not launch this Skill automatically. A limited metadata handoff to one named Study requires an explicit user decision; it never transfers paper text or PDFs.

### Formal sources

- [v0.3.0 Release](https://github.com/chenhaoran2068/research-paper-reading/releases/tag/v0.3.0)
- [Skill entry](https://github.com/chenhaoran2068/research-paper-reading/blob/v0.3.0/skill/research-paper-reading/SKILL.md)
- [Public boundary](https://github.com/chenhaoran2068/research-paper-reading/blob/v0.3.0/PUBLIC_BOUNDARY.md)
