# Abstract Products
from abc import ABC, abstractmethod


class Button(ABC):
    """Abstract Button interface"""

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def click(self) -> str:
        pass