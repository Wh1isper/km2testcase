#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import json
from pathlib import Path
from typing import List

from km2testcase.model import CaseModel, KNode, Step


def _recursive_case(
    case: KNode,
    project_name,
    model_name,
    case_models,
):
    if not case.children:
        # invalid, skip
        return

    for child in case.children:
        child = KNode(child)
        if not child.children:
            # invalid, skip
            continue

        for grandson in child.children:
            grandson = KNode(grandson)
            if grandson.children:
                # child is not a step, but a subcase
                child.add_parent_content(case.content)
                child.add_parent_note(case.note)
                _recursive_case(child, project_name, model_name, case_models)
                break
            else:
                # child is a Step, collect all step
                steps = []
                for step in case.children:
                    step = KNode(step)
                    for expect in step.children:
                        expect = KNode(expect)
                        if not expect.children:
                            steps.append(Step.from_node(step))

                case_models.append(
                    CaseModel(
                        project_name=project_name,
                        model_name=model_name,
                        case_name=case.content,
                        priority=case.priority,
                        prepare=case.note,
                        steps=steps,
                    )
                )
                return


def parse_km(file_path: Path, encoding="utf-8") -> List[CaseModel]:
    print(f"Parsing km file {file_path}")
    with open(file_path, encoding=encoding) as f:
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
