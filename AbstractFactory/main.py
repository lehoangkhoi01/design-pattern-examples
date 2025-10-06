from AbstractFactory.ClassicUIFactory import ClassicUIFactory
from AbstractFactory.ModernUIFactory import ModernUIFactory
from AbstractFactory.client_app import Application

if __name__ == "__main__":
    print("=== Modern Theme Application ===")
    modern_factory = ModernUIFactory()
    modern_app = Application(modern_factory)
    modern_app.render_ui()
    print("\nUser interactions:")
    modern_app.interact()

    # Demonstrate Modern-specific features
    print("\nModern-specific features:")
    modern_button = modern_app.button
    print(modern_button.set_elevation(4))
    print(modern_button.set_ripple(True))
    print(modern_button.click())

    modern_checkbox = modern_app.checkbox
    print(modern_checkbox.set_animation_speed(500))
    print(modern_checkbox.toggle())

    print("\n" + "=" * 40 + "\n")

    print("=== Classic Theme Application ===")
    classic_factory = ClassicUIFactory()
    classic_app = Application(classic_factory)
    classic_app.render_ui()
    print("\nUser interactions:")
    classic_app.interact()

    # Demonstrate Classic-specific features
    print("\nClassic-specific features:")
    classic_button = classic_app.button
    print(classic_button.set_tooltip("Click me for action!"))
    print(classic_button.get_tooltip())
    print(classic_button.set_border_style(True))
    print(classic_button.click())

    classic_checkbox = classic_app.checkbox
    print(classic_checkbox.enable_tristate(True))
    print(classic_checkbox.toggle())
    print(classic_checkbox.toggle())
    print(classic_checkbox.toggle())