# Governance

## Stewardship

OpenCCF is maintained by **Murmurate** (Murmurate Digital Limited), a non-profit
climate-technology organisation, which holds the repository and the
`openccf.org` domain.

Custody is administrative, not proprietary. The model is CC0: anyone may use,
implement, adapt, redistribute or fork it without permission or attribution.
Murmurate holds no rights over implementations. If the project reaches a scale
where a vendor-neutral home is warranted, the intention is to transfer custody
to a neutral body; the repository and namespace are named after the project, not
the steward, so a transfer breaks no links.

## Decisions

Changes are proposed and discussed as GitHub issues, implemented as pull
requests referencing them, with the reasoning recorded in the schema
descriptions (where it affects interpretation) or the commit message. Where a
change alters how existing data is interpreted, implementing partners are
consulted directly rather than by absence of objection.

## Versioning

Semantic versioning, for a data model:

- **Major** - can invalidate previously valid data or code: removing/renaming a
  class, field or enum value; making an optional field required; narrowing a
  type or permitted values; changing how a field is interpreted.
- **Minor** - backwards compatible: adding an optional field; adding an enum
  value; relaxing required to optional.
- **Patch** - documentation, examples, generated artefacts; no change to what
  validates.

Breaking changes are announced before release.

## Scope

Corporate carbon footprints aligned to the GHG Protocol Corporate Standard and
its guidance. Out of scope: what must be reported (disclosure frameworks);
whether or how data is shared (sender and receiver); how emissions are
calculated (the GHG Protocol). A product carbon footprint model, if pursued,
would be a separate sister project.

OpenCCF adopts GHG Protocol wording and structure where it exists, and is not
affiliated with or endorsed by the GHG Protocol or the World Resources
Institute.

## Contact

<https://github.com/openccf/openccf-data-model/issues>, or <https://openccf.org>.