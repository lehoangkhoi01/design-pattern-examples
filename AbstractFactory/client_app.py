# Client Code
from AbstractFactory.UIFactory import UIFactory


class Application:
    """Client that uses the abstract factory"""

    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        print(self.button.render())
        print(self.checkbox.render())

    def interact(self):
        print(self.button.click())
        print(self.checkbox.toggle())
