from AbstractFactory.product.Checkbox import Checkbox


# Concrete Products - Modern Theme
class ModernCheckbox(Checkbox):
    def __init__(self):
        self.animation_duration = 300  # milliseconds

    def render(self) -> str:
        return "Rendering modern checkbox with material design"

    def toggle(self) -> str:
        return "Modern checkbox toggled with fade effect"

    # Special additional features in Modern Checkbox
    def set_animation_speed(self, duration_ms: int):
        """Modern-specific feature: Configurable animation speed"""
        self.animation_duration = duration_ms
        return f"Animation speed set to {duration_ms}ms"