#!/usr/bin/python3

"""Module defining a function that prints a square with the character #."""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The length size of the square.

    Raises:
        TypeError: If size is not an int or if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
