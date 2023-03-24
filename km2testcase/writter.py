#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import csv
from pathlib import Path
from typing import List

from km2testcase.model import PlatformModel
from km2testcase.writter_mixin import CsvMixin


def write(
    models: List[PlatformModel], output_path: Path, output_type: str, encoding: str = "utf-8"
):
    s = {"csv": write_to_csv}
    print(f"Writing testcases to {output_path}")
    s[output_type](models, output_path, encoding=encoding)
    print(f"All testcases written")


def write_to_csv(models: List[CsvMixin], output_path: Path, encoding="utf-8"):
    if not models:
        print("No models to write!")
        return
    header = models[0].csv_header()
    with open(output_path, "w", encoding=encoding) as csvfile:
        w = csv.writer(csvfile)
        w.writerow(header)
        w.writerows((r.csv_format() for r in models))
