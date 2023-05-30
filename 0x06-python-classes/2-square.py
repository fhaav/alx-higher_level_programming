#!/usr/bin/python3

"""This script defines a class called Square."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """

        if size >= 0:
            self.__size = size
        else:
            raise TypeError("size must be an integer.")
        if size < 0:
            raise ValueError("size must be >= 0.")
