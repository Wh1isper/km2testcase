from typing import List


class CsvMixin:
    @classmethod
    def csv_header(cls) -> List[str]:
        raise NotImplementedError

    def csv_format(self) -> List[str]:
        raise NotImplementedError
