#!/usr/bin/python3

"""This script defines a class called Square."""


class Square:
    """Represents a square object."""

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The current square area.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square using '#' character."""
        if self.__size == 0:
            print()
        elif self.__size > 0:
            for _ in range(self.__size):
                print("#" * self.__size)
