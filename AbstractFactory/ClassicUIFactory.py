from AbstractFactory.UIFactory import UIFactory
from AbstractFactory.product.Button import Button
from AbstractFactory.product.Checkbox import Checkbox
from AbstractFactory.product.ClassicButton import ClassicButton
from AbstractFactory.product.ClassicCheckbox import ClassicCheckbox

# Concrete Factories
class ClassicUIFactory(UIFactory):
    """Factory for creating classic-themed UI components"""

    def create_button(self) -> Button:
        return ClassicButton()

    def create_checkbox(self) -> Checkbox:
        return ClassicCheckbox()