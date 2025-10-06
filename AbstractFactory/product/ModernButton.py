# Concrete Products - Modern Theme
from AbstractFactory.product.Button import Button


class ModernButton(Button):
    def __init__(self):
        self.ripple_enabled = True
        self.elevation = 2

    def render(self) -> str:
        return "Rendering modern flat button with rounded corners"

    def click(self) -> str:
        return "Modern button clicked with smooth animation"

    # Special additional features in Modern Button
    def set_ripple(self, enabled: bool):
        """Modern-specific feature: Material Design ripple effect"""
        self.ripple_enabled = enabled
        return f"Ripple effect {'enabled' if enabled else 'disabled'}"

    def set_elevation(self, level: int):
        """Modern-specific feature: Shadow elevation"""
        self.elevation = level
        return f"Elevation set to level {level}"
