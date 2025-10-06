# Concrete Products - Classic Theme
from AbstractFactory.product.Button import Button


class ClassicButton(Button):
    def __init__(self):
        self.tooltip_text = ""
        self.has_border = True

    def render(self) -> str:
        return "Rendering classic 3D button with beveled edges"

    def click(self) -> str:
        return "Classic button clicked with press effect"

    # Special additional features in Classic Button
    def set_tooltip(self, text: str):
        """Classic-specific feature: Traditional tooltip"""
        self.tooltip_text = text
        return f"Tooltip set: '{text}'"

    def set_border_style(self, enabled: bool):
        """Classic-specific feature: Toggle 3D border effect"""
        self.has_border = enabled
        return f"3D border {'enabled' if enabled else 'disabled'}"

    def get_tooltip(self) -> str:
        """Classic-specific feature: Retrieve tooltip"""
        return self.tooltip_text if self.tooltip_text else "No tooltip set"