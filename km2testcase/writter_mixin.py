#  Copyright (c) 2023 Wh1isper
#  Licensed under the BSD 3-Clause License
#  Created by @Wh1isper 2023/1/4
from typing import List


class CsvMixin:
    @classmethod
    def csv_header(cls) -> List[str]:
        raise NotImplementedError

    def csv_format(self) -> List[str]:
        raise NotImplementedError
