#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4

import pydantic

from km2testcase.writter_mixin import CsvMixin


class CaseModel(pydantic.BaseModel):
    pass


class PlatformModel(pydantic.BaseModel):
    @classmethod
    def from_case_model(cls, case_model: CaseModel, *, echo=False):
        raise NotImplementedError


class ZentaoModel(PlatformModel, CsvMixin):
    @classmethod
    def from_case_model(cls, case_model: CaseModel, *, echo=False):
        m = ZentaoModel()
        if echo:
            print(f"Converted {case_model} -> {m}")
        return m

    @classmethod
    def csv_header(cls):
        # TODO: imp for csv
        raise NotImplementedError

    def csv_format(self):
        # TODO: imp for csv
        raise NotImplementedError


p = {
    "zentao": ZentaoModel,
}


def convert(case_model: CaseModel, platform: str, *, echo=False) -> PlatformModel:
    return p[platform].from_case_model(case_model, echo=echo)
