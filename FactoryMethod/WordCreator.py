from FactoryMethod.DocumentCreator import DocumentCreator
from FactoryMethod.models.Document import Document
from FactoryMethod.models.WordDocument import WordDocument


class WordCreator(DocumentCreator):
    """Factory for creating Word documents"""

    def __init__(self, template=None):
        self.template = template

    def factory_method(self) -> Document:
        return WordDocument()