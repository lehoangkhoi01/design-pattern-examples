# Concrete Creators
from FactoryMethod.DocumentCreator import DocumentCreator
from FactoryMethod.models.Document import Document
from FactoryMethod.models.PDFDocument import PDFDocument


class PDFCreator(DocumentCreator):
    """Factory for creating PDF documents"""

    def __init__(self, encrypted=False, compression=5):
        self.encrypted = encrypted
        self.compression = compression

    def factory_method(self) -> Document:
        return PDFDocument()
