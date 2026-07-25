# Contributing to OpenCCF

Thank you for your interest in contributing.

All participation is subject to the [Code of Conduct](CODE_OF_CONDUCT.md).

## Where to go

- **Questions and ideas** → [GitHub Discussions](https://github.com/openccf/openccf-data-model/discussions)
- **Bugs, gaps, and change requests** → [GitHub Issues](https://github.com/openccf/openccf-data-model/issues)

No code is needed to help. The most useful contributions right now:

- data you cannot represent in the model;
- fields that are required but which your systems will not reliably have;
- points where two implementers could read the spec differently.

When raising an issue, include what you were trying to represent, what the model
does instead, and a few lines of example YAML if relevant. State the problem
before any proposed fix.

## Changing the schema

1. Open an issue or discussion first, unless the change is trivial.
2. Edit `src/openccf/schema/openccf.yaml` only — the Python datamodel and all
   other artefacts are generated from it and overwritten on build.
3. Add a fixture: `tests/data/valid/` if it should now pass,
   `tests/data/invalid/` if it should now fail. Check it fails for the intended
   reason, not incidentally.
4. Run `just test` and `just lint`.
5. Open a pull request referencing the issue. A rendered docs preview builds
   automatically.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and
[just](https://github.com/casey/just) (on Windows, use WSL2). Run `just` or
`just --list` for all recipes.

```sh
git clone https://github.com/<your-fork>/openccf-data-model.git
cd openccf-data-model
just setup
pre-commit install
```

| Command | Does |
|---|---|
| `just test` | Regenerate artefacts, run tests |
| `just lint` | LinkML linter |
| `just testdoc` | Preview docs locally |

`just test` prints OWL and Excel generator warnings; these are expected. The
pytest summary is the signal.

## Conventions

- Field `description`s are published as the specification — write them for
  implementers.
- Prefer optional: relaxing a required field later is compatible; tightening is
  breaking.
- Quote enum descriptions containing commas or colons (the inline
  `{description: ...}` form breaks otherwise).
- Fixtures are named `<ClassName>-<anything>.yaml`; text before the first hyphen
  selects the class to validate against.

Contributions are released under [CC0 1.0](LICENSE).