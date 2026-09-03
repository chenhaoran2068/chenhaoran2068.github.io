# Research Collaboration Portal v0.5.4

## Added

- Adds the Clinical Database Method overview and a public, deidentified guide
  for requesting, configuring, validating, and troubleshooting read-only
  PostgreSQL access over Tailscale with TLS.
- Adds Windows and macOS instructions for DBeaver and psql, including root CA
  handling, copyable commands, request templates, and connection checks that
  do not read patient values.

## Updated

- Brings the English and Japanese pages into structural alignment with the
  reviewed Chinese pages across the homepage, component overviews, Skills,
  System guidance, getting-started routes, releases, governance, integrations,
  and roadmap.
- Adds detailed stage guidance to the English and Japanese Governed Research
  Workflow pages and updates all portal references to System v1.16.0.
- Reorganizes navigation so Frameworks, Systems, Skills, and Methods each have
  a clear overview entry.

## Fixed

- Improves dark-theme contrast for tables, details panels, inline code,
  directory trees, and Clinical Database examples.
- Prevents horizontal overflow and clipped text in desktop and mobile layouts.
- Keeps shared validation SQL outside operating-system tabs and uses a
  pre-approved ordinary object for the expected write-failure check.

## Boundaries

- This release changes public portal documentation, navigation, presentation,
  and non-sensitive examples only.
- It does not configure or modify any database, account, service, firewall,
  certificate, Tailscale network, local Study, patient data, or component
  runtime.
