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
    echo=False,
):
    if not case.children:
        # invalid, skip
        if echo:
            print(f"Cannot parse case {case}")
        return

    for child in case.children:
        child = KNode(child)
        if not child.children:
            # invalid, skip
            if echo:
                print(f"No expect result for case: {case}, skipped")
            continue

        if any(KNode(g).children for g in child.children):
            # child is a subcase, step into
            child.add_parent_content(case.content)
            child.add_parent_note(case.note)
            if echo:
                print(f"Found subcase: {child}")
            _recursive_case(child, project_name, model_name, case_models, echo=echo)

    # Collect steps in this case
    steps = []
    for step in case.children:
        step = KNode(step)
        for expect in step.children:
            expect = KNode(expect)
            if not expect.children:
                steps.append(Step.from_node(step))
    if steps:
        m = CaseModel(
            project_name=project_name,
            model_name=model_name,
            case_name=case.content,
            priority=case.priority,
            prepare=case.note,
            steps=steps,
        )
        if echo:
            print(f"Collect case: {m}")
        case_models.append(m)


def parse_km(file_path: Path, echo=False, encoding="utf-8") -> List[CaseModel]:
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
            _recursive_case(case, project_name, model_name, case_models, echo=echo),
    return case_models
