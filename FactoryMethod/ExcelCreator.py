from FactoryMethod.DocumentCreator import DocumentCreator
from FactoryMethod.models.Document import Document
from FactoryMethod.models.ExcelDocument import ExcelDocument


class ExcelCreator(DocumentCreator):
    """Factory for creating Excel documents"""

    def __init__(self, sheets=1, macros=False):
        self.sheets = sheets
        self.macros = macros

    def factory_method(self) -> Document:
        return ExcelDocument()