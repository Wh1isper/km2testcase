import os
from pathlib import Path
from typing import List

import pytest

from km2testcase.model import PREPARE_SEP, CaseModel, Step
from km2testcase.parser import parse_km

_here = os.path.dirname(os.path.abspath(__file__))

cases = [
    (
        os.path.join(_here, "./case1.km"),
        [
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例-子用例1",
                priority=2,
                prepare=f"\n{PREPARE_SEP}\n".join(["前置步骤", "前置步骤2"]),
                steps=[Step(step="步骤1", expect="期望1")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例",
                priority=2,
                prepare="前置步骤",
                steps=[Step(step="步骤2", expect="期望2")],
            ),
        ],
    ),
    (
        os.path.join(_here, "../EXAMPLE.km"),
        [
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例1",
                priority=1,
                prepare="前置步骤",
                steps=[Step(step="步骤1", expect="期望1")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例2-子用例1",
                priority=2,
                prepare=f"\n{PREPARE_SEP}\n".join(["前置步骤", "子用例前置条件1"]),
                steps=[Step(step="步骤1", expect="期望1"), Step(step="步骤2", expect="期望2")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例2-子用例2",
                priority=1,
                prepare="前置步骤",
                steps=[Step(step="步骤1", expect="期望1")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例3",
                priority=3,
                prepare="前置步骤",
                steps=[Step(step="步骤1", expect="期望1")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例4",
                priority=2,
                steps=[Step(step="步骤1", expect="期望1")],
            ),
            CaseModel(
                project_name="产品名称",
                model_name="模块1",
                case_name="测试用例5",
                priority=2,
                steps=[Step(step="步骤1", expect="期望1")],
            ),
        ],
    ),
]


def assert_node(case_models: List[CaseModel], expected_models: List[CaseModel]):
    assert sorted(case_models) == sorted(expected_models)


@pytest.mark.parametrize("case", cases)
def test_convert_case_model(
    case,
):
    markdown_file_path, result = case
    case_models = parse_km(Path(markdown_file_path))
    assert case_models == result


if __name__ == "__main__":
    pytest.main(["-vvv"])
