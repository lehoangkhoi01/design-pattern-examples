from abc import ABC, abstractmethod


# Product Interface
class Document(ABC):
    """Abstract base class for documents"""

    @abstractmethod
    def create(self):
        """Create the document"""
        pass

    @abstractmethod
    def open(self):
        """Open the document"""
        pass

    @abstractmethod
    def save(self):
        """Save the document"""
        pass