<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# OpenCCF - Open Corporate Carbon Footprint Data Model

An open, interoperable data model for exchanging GHG Protocol-aligned corporate
carbon footprints between systems. It defines how a corporate footprint is
structured for exchange - not what must be reported, calculated, or shared.

**Status:** v0.3, release candidate for v1.0.

- Schema reference: <https://openccf.github.io/openccf>
- Concept, white paper, information model: <https://openccf.org>

## Structure

Two core objects:

- **EmissionsReport** - a company's footprint for a reporting period (identity,
  period, net totals, GWP horizon, status).
- **EmissionsLine** - one quantified source or category. A report contains one
  or more. Lines are flat; subtotals are derived by grouping, not nesting.

Optional nested detail on a line: `emissionFactor`, `dataQuality`,
`gasBreakdown`, `activityData`, `landSectorData`. Optional context on a report:
`sectors`, `companyIdentifiers`, `intensityDenominators`.

A single figure is exchanged as a report containing one line.

## Things to know before implementing

1. **Quantities are non-negative magnitudes.** Direction is set by
   `accountingType`: `EMISSION` adds, `REMOVAL` subtracts, `REVERSAL` adds;
   `GROSS_CO2_FLUX` and `OTHER_LAND_SECTOR_DISCLOSURE` are excluded from the net.
   Emissions and removals are reported gross, not netted.

2. **Two net totals.** `totalNetEmissionsLocationBasedKgCO2e` is always present
   and excludes `ELECTRICITY_MARKET_BASED` lines.
   `totalNetEmissionsMarketBasedKgCO2e` is present only when market-based
   electricity lines exist, and excludes `ELECTRICITY_LOCATION_BASED` lines.
   Both electricity lines stay in the payload; summing all lines double-counts.
   Worked example: `tests/data/valid/EmissionsReport-dual-scope2.yaml`.

3. **Absence means "not provided"** - never zero, never poor quality. A zero
   source is a line with quantity `0` and `lineStatus: COMPLETE`. Coverage is
   inferred from lines present plus each line's `lineStatus`.

4. **Not machine-comparable across senders:** `subcategory`,
   `dataQualityInformation`, `activityData.description`. `subcategory` is
   reliable for grouping within one sender's data only.

5. **Rules not enforced by schema validation** (they aggregate over lines):
   each net total equals the signed sum of its contributing lines; where a
   `gasBreakdown` is present, contributions sum to the line total within 0.1%.
   Checked by the test suite; implementations should check them too.

## Repository layout

The schema is the single source of truth; everything else is generated from it,
so JSON Schema, SHACL, OWL, Python and an Excel view are outputs of the model
rather than part of it.

* [src/openccf/schema/](src/openccf/schema) - LinkML schema **(edit this)**
* [src/openccf/datamodel/](src/openccf/datamodel) - generated Python datamodel
* [docs/](docs/) - mkdocs documentation ([elements/](docs/elements/) is generated)
* [examples/](examples/) - usage examples
* [project/](project/) - generated project files (do not edit)
* [tests/data/](tests/data) - example data (`valid/` validates, `invalid/` must fail)

## Use

Requires [uv](https://docs.astral.sh/uv/) and
[just](https://github.com/casey/just). Run `just --list` for all recipes.

```sh
git clone https://github.com/openccf/openccf-data-model.git
cd openccf-data-model
just setup
just test
```

Validate your own file:

```sh
uv run linkml-validate -s src/openccf/schema/openccf.yaml your-report.yaml
```

## Feedback

Via [GitHub Issues](https://github.com/openccf/openccf-data-model/issues). See
[CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md).

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier)
template.

## Licence

Public domain under [CC0 1.0](LICENSE). No attribution required.

Maintained by [Murmurate](https://www.murmurate.digital), a non-profit, with
input from partners including the Carbon Accounting Alliance, SME Climate Hub, Equipoise Earth, Mycelium Networks and RoundArc.
