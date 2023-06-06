#!/usr/bin/python3

"""This module defines a Rectangle class."""


class Rectangle:
    """
    Rectangle class represents a rectangle shape.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        number_of_instances (int): Number of Rectangle instances.
        print_symbol (any): Symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle (default is 0).
            height (int): Height of the rectangle (default is 0).
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): Width value to set.

        Raises:
            TypeError: If the width value is not an integer.
            ValueError: If the width value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the attribute height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the attribute height.

        Args:
            value (int): Height value to set.

        Raises:
            TypeError: Height value is not an integer.
            ValueError: Height value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        if self.width != 0 and self.height != 0:
            return 2 * (self.width + self.height)
        else:
            return 0

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        if self.width == 0 or self.height == 0:
            return ""
        rec_str = ""
        for _ in range(self.height):
            rec_str += "#" * self.width + "\n"
        return rec_str[:-1]

    def __repr__(self):
        """
        Returns a string representation of the rectangle
        that can be used to reconstruct the rectangle object.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message upon the deletion of a Rectangle instance.
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the biggest
        rectangle based on the area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new rectangle instance representing a square."""
        return cls(size, size)
