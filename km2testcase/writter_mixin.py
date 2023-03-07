class CsvMixin:
    @classmethod
    def csv_header(cls):
        raise NotImplementedError

    def csv_format(self):
        raise NotImplementedError
