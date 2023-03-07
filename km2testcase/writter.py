#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
from pathlib import Path
from typing import List

from km2testcase.model import PlatformModel
from km2testcase.writter_mixin import CsvMixin


def write(models: List[PlatformModel], output_path: Path, output_type: str):
    s = {"csv": write_to_csv}
    print(f"Writing testcases to {output_path}")
    s[output_type](models, output_path)
    print(f"All testcases written")


def write_to_csv(models: List[CsvMixin], output_path: Path):
    # header = models[0].csv_header()
    pass
