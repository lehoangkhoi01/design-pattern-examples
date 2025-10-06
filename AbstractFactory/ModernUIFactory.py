
from AbstractFactory.UIFactory import UIFactory
from AbstractFactory.product.Button import Button
from AbstractFactory.product.Checkbox import Checkbox
from AbstractFactory.product.ModernButton import ModernButton
from AbstractFactory.product.ModernCheckbox import ModernCheckbox


# Concrete Factories
class ModernUIFactory(UIFactory):
    """Factory for creating modern-themed UI components"""

    def create_button(self) -> Button:
        return ModernButton()

    def create_checkbox(self) -> Checkbox:
        return ModernCheckbox()