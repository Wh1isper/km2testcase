#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
import json
from pathlib import Path
from typing import List

import commonmark

from km2testcase.model import CaseModel


def parse_km(file_path: Path) -> List[CaseModel]:
    print(f"Parsing km file {file_path}")
    with open(file_path) as f:
        ast = json.load(f)
    return []
