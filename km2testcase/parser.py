#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import json
from pathlib import Path
from typing import List

from km2testcase.model import CaseModel, KNode, Step


def _recursive_case(case: KNode, project_name, model_name, case_models):
    if (
        not case.children
        or not KNode(case.children[0]).children
        or not KNode(KNode(case.children[0]).children[0]).children
    ):
        case_models.append(
            CaseModel(
                project_name=project_name,
                model_name=model_name,
                case_name=case.content,
                priority=case.priority,
                prepare=case.note,
                steps=[Step.from_node(KNode(step)) for step in case.children],
            )
        )
    else:
        for sub_case in case.children:
            sub_case = KNode(sub_case)
            sub_case.add_parent_content(case.content)
            _recursive_case(sub_case, project_name, model_name, case_models)


def parse_km(file_path: Path) -> List[CaseModel]:
    print(f"Parsing km file {file_path}")
    with open(file_path) as f:
        ast = json.load(f)

    case_models = []
    root = KNode(ast["root"])
    project_name = root.content
    for model in root.children:
        model = KNode(model)
        model_name = model.content
        for case in model.children:
            case = KNode(case)
            _recursive_case(case, project_name, model_name, case_models),
    return case_models
