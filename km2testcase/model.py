#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import os
from typing import List, Optional

import pydantic

from km2testcase.writter_mixin import CsvMixin

PREPARE_SEP = "-----------------------------"


class KNode:
    def __init__(self, node):
        self.node = node

    @property
    def content(self):
        return self.node["data"].get("text") or ""

    @property
    def priority(self):
        return self.node["data"].get("priority") or 2

    @property
    def note(self):
        return self.node["data"].get("note")

    @property
    def children(self):
        return self.node.get("children", [])

    def add_parent_content(self, s):
        self.node["data"]["text"] = "-".join([s, self.content])

    def add_parent_note(self, s):
        if not self.note:
            self.node["data"]["note"] = s
        else:
            self.node["data"]["note"] = f"\n{PREPARE_SEP}\n".join([s, self.note])

    def __repr__(self):
        return self.content


class Step(pydantic.BaseModel):
    step: str
    expect: str

    @classmethod
    def from_node(cls, node: KNode):
        return Step(
            step=node.content,
            expect="\n".join([KNode(expect).content for expect in node.children]).rstrip("\n"),
        )


class CaseModel(pydantic.BaseModel):
    project_name: str
    model_name: str
    case_name: str
    priority: int
    prepare: Optional[str]
    steps: List[Step]

    def concat_step(self):
        steps = []
        for index, step in enumerate(self.steps):
            steps.append(f"{index+1}. {step.step}")

        return "\n".join(steps).strip()

    def concat_except(self):
        excepts = []
        for index, step in enumerate(self.steps):
            excepts.append(f"{index+1}. {step.expect}")

        return "\n".join(excepts).strip()


class PlatformModel(pydantic.BaseModel):
    @classmethod
    def from_case_model(cls, case_model: CaseModel, *, echo=False):
        raise NotImplementedError


class ZentaoModel(PlatformModel, CsvMixin):
    model_name: str
    case_name: str
    priority: str
    prepare: str = ""
    step: str = ""
    expect: str = ""
    case_type: str = os.getenv("ZENTAO_CASE_TYPE", "功能测试")
    stage: str = os.getenv("ZENTAO_STAGE", "功能测试阶段")

    @classmethod
    def from_case_model(cls, case_model: CaseModel, *, echo=False):
        m = ZentaoModel(
            model_name=case_model.model_name,
            case_name=case_model.case_name,
            priority=cls._convert_priority(case_model.priority),
            prepare=case_model.prepare or "",
            step=case_model.concat_step(),
            expect=case_model.concat_except(),
        )
        if echo:
            print(f"Converted {case_model} -> {m}")
        return m

    @classmethod
    def _convert_priority(cls, priority: int):
        m = {1: "高", 2: "中", 3: "低"}
        if priority <= 3:
            return m[priority]
        else:
            return "低"

    @classmethod
    def csv_header(cls):
        return ["所属模块", "用例标题", "前置条件", "步骤", "预期", "关键词", "优先级", "用例类型", "适用阶段"]

    def csv_format(self):
        return [
            self.model_name,
            self.case_name,
            self.prepare,
            self.step,
            self.expect,
            "",
            self.priority,
            self.case_type,
            self.stage,
        ]


p = {
    "zentao": ZentaoModel,
}


def convert(case_model: CaseModel, platform: str, *, echo=False) -> PlatformModel:
    return p[platform].from_case_model(case_model, echo=echo)
