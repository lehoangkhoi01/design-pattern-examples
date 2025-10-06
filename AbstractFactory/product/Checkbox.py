from abc import ABC, abstractmethod


class Checkbox(ABC):
    """Abstract Checkbox interface"""

    @abstractmethod
    def render(self) -> str:
        pass

    @abstractmethod
    def toggle(self) -> str:
        pass