#!/usr/bin/python3

"""
Contains a Square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class inheriting from Rectangle
    """

    def __init__(self, size):
        """ Initializes private attribute """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Calculates the area of the Square """
        return (self.__size * self.__size)

    def __str__(self):
        """ Returns string representation of the square """
        return f"[Square] {self.__size}/{self.__size}"
