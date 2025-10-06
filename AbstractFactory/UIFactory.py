# Abstract Factory
from abc import ABC, abstractmethod

from AbstractFactory.product.Button import Button
from AbstractFactory.product.Checkbox import Checkbox


class UIFactory(ABC):
    """Abstract factory for creating UI components"""

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass