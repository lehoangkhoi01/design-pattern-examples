from AbstractFactory.product.Checkbox import Checkbox


class ClassicCheckbox(Checkbox):
    def __init__(self):
        self.state = False
        self.tristate_enabled = False
        self.indeterminate = False

    def render(self) -> str:
        return "Rendering classic checkbox with simple border"

    def toggle(self) -> str:
        if self.tristate_enabled:
            if not self.state and not self.indeterminate:
                self.state = True
                return "Classic checkbox checked instantly"
            elif self.state and not self.indeterminate:
                self.indeterminate = True
                self.state = False
                return "Classic checkbox set to indeterminate state"
            else:
                self.indeterminate = False
                self.state = False
                return "Classic checkbox unchecked instantly"
        else:
            self.state = not self.state
            return f"Classic checkbox {'checked' if self.state else 'unchecked'} instantly"

    def enable_tristate(self, enabled: bool):
        """Classic-specific feature: Enable tri-state checkbox (checked/unchecked/indeterminate)"""
        self.tristate_enabled = enabled
        return f"Tri-state mode {'enabled' if enabled else 'disabled'}"

