# What is it ?
Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

# Problem
1. We have many products
2. Each product have many variants

**=> Use Abstract Factory**

# Solution
Implements:

1. Declare interface for each product (not product type)
2. Make the variants follow the interface
3. Declare Abstract Factory - interface with list of creation methods for ALL products
4. Create separate factory class based on the Abstract Factory

# Noted
- Each implementation can have special features. For my code example: each of variants have their own methods/props beside the interfaces
- But when using those special features, the client code should know the type of the implementation (not the type of interface)
- Workaround: We can customize by configure the type in the creation method:

`class ModernUIFactory(UIFactory):
    def create_button(self, elevation=2, ripple=True) -> Button:
        button = ModernButton()
        button.set_elevation(elevation)
        button.set_ripple(ripple)
        return button
`




