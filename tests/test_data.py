"""Data test."""

import os
import glob
import pytest
from pathlib import Path

import openccf.datamodel.openccf
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        openccf.datamodel.openccf,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj

from linkml.validator import validate_file


@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_files(filepath):
    """Each invalid data file must fail schema validation."""
    schema_path = Path(__file__).parent.parent / "src" / "openccf" / "schema" / "openccf.yaml"
    target_class_name = Path(filepath).stem.split("-")[0]
    report = validate_file(
        filepath,
        str(schema_path),
        target_class_name,
    )
    assert report.results, f"Expected validation errors for {filepath}, but it passed"