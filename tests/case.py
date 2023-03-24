import os

import pytest

from km2testcase.model import PREPARE_SEP, CaseModel, Step

_here = os.path.dirname(os.path.abspath(__file__))

CASE_MODEL_1 = [
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
]

cases = [
    (os.path.join(_here, "./case1-1.km"), CASE_MODEL_1),
    (os.path.join(_here, "./case1-2.km"), CASE_MODEL_1),
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
