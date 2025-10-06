# Creator (Factory) Interface
from abc import ABC, abstractmethod

from FactoryMethod.models.Document import Document


class DocumentCreator(ABC):
    """Abstract factory class"""

    @abstractmethod
    def factory_method(self) -> Document:
        """Factory method to be implemented by subclasses"""
        pass

    def new_document(self):
        """Common operation using the factory method"""
        doc = self.factory_method()
        result = [
            doc.create(),
            doc.open()
        ]
        return "\n".join(result)