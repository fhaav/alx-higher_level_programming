#!/usr/bin/python3

"""
Contains a Square class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A Square class extending the Rectangle class
    """

    def __init__(self, size):
        """ Initializes private attributes """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ Calculates the area of the square """
        return (self.__size * self.__size)
