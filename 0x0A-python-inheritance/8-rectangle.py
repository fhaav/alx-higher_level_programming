#!/usr/bin/python3

"""
Rectangle Class
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns
        int: The calculated area of the rectangle
        """
        return self.__width * self.__height
