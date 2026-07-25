"""Semantic rule tests.

These cover constraints stated in the schema descriptions that schema
validation cannot enforce, because they aggregate over the lines in a report:

  1. Each net total equals the signed sum of its contributing lines, under the
     correct Scope 2 electricity exclusion.
  2. Where a gas breakdown is present, the gas contributions sum to the line
     total.

They read the example YAML directly rather than through the generated classes,
because that is what an implementation in any language would do. Any file under
tests/data/valid/ is checked.
"""

import glob
import math
import os
from pathlib import Path

import pytest
import yaml

VALID_DIR = Path(__file__).parent / "data" / "valid"
VALID_FILES = sorted(glob.glob(os.path.join(VALID_DIR, "*.yaml")))

MARKET = "totalNetEmissionsMarketBasedKgCO2e"
LOCATION = "totalNetEmissionsLocationBasedKgCO2e"

# Disclosure-only lines are excluded from every net total.
DISCLOSURE_ONLY = {"GROSS_CO2_FLUX", "OTHER_LAND_SECTOR_DISCLOSURE"}

# Contribution of each accounting type to the net.
SIGNS = {"EMISSION": 1, "REMOVAL": -1, "REVERSAL": 1}

# Rounding tolerance: 0.1% relative, small absolute floor for near-zero values.
REL_TOL = 0.001
ABS_TOL = 0.01


def load(filepath):
    with open(filepath) as f:
        return yaml.safe_load(f)


def close(a, b):
    return math.isclose(a, b, rel_tol=REL_TOL, abs_tol=ABS_TOL)


def net_total(report, exclude_category):
    """Signed sum of lines, excluding disclosure-only lines and the electricity
    category belonging to the method not being computed."""
    total = 0.0
    for line in report.get("emissionsLines", []):
        acct = line.get("accountingType", "EMISSION")  # schema ifabsent default
        if acct in DISCLOSURE_ONLY:
            continue
        if line.get("category") == exclude_category:
            continue
        total += SIGNS[acct] * float(line["emissionsQuantityKgCO2e"])
    return total


@pytest.mark.parametrize("filepath", VALID_FILES)
def test_net_totals_match_lines(filepath):
    """Each stated net total equals the signed sum of its contributing lines."""
    report = load(filepath)
    name = Path(filepath).name

    location = net_total(report, exclude_category="ELECTRICITY_MARKET_BASED")
    assert close(float(report[LOCATION]), location), (
        f"{name}: location-based total is {report[LOCATION]}, "
        f"lines sum to {location}"
    )

    if MARKET in report:
        market = net_total(report, exclude_category="ELECTRICITY_LOCATION_BASED")
        assert close(float(report[MARKET]), market), (
            f"{name}: market-based total is {report[MARKET]}, "
            f"lines sum to {market}"
        )


@pytest.mark.parametrize("filepath", VALID_FILES)
def test_gas_breakdown_sums_to_line_total(filepath):
    """Where a gas breakdown is present, contributions sum to the line total."""
    report = load(filepath)
    name = Path(filepath).name

    for i, line in enumerate(report.get("emissionsLines", [])):
        breakdown = line.get("gasBreakdown")
        if not breakdown:
            continue
        contributions = sum(
            float(entry["gasCO2eContribution"])
            for entry in breakdown
            if entry.get("gasCO2eContribution") is not None
        )
        line_total = float(line["emissionsQuantityKgCO2e"])
        assert close(contributions, line_total), (
            f"{name} line {i}: gas contributions sum to {contributions}, "
            f"line total is {line_total}"
        )