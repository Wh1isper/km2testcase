import os
from pathlib import Path
from typing import List

import pytest
from case import cases

from km2testcase.model import CaseModel
from km2testcase.parser import parse_km


def assert_convert(case_models: List[CaseModel], expected_models: List[CaseModel]):
    assert len(case_models) == len(expected_models)
    c = sorted([c.json() for c in case_models])
    e = sorted([e.json() for e in expected_models])
    assert c == e


@pytest.mark.parametrize("case", cases)
def test_convert_case_model(
    case,
):
    markdown_file_path, expects = case
    case_models = parse_km(Path(markdown_file_path))
    assert_convert(case_models, expects)


if __name__ == "__main__":
    pytest.main(["-vvv"])
