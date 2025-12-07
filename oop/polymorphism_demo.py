# polymorphism_demo.py

import math

class Shape:
    """
    Base class for geometric shapes.
    The area method is meant to be overridden by all subclasses.
    """

    def area(self):
        """
        Base method that must be overridden.
        Raising NotImplementedError ensures subclasses must implement this.
        """
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    """
    Rectangle class derived from Shape.
    Demonstrates polymorphism by overriding the area method.
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return area of rectangle: length × width."""
        return self.length * self.width


class Circle(Shape):
    """
    Circle class derived from Shape.
    Overrides the area method using π × radius².
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of circle: π × radius²."""
        return math.pi * (self.radius ** 2)
