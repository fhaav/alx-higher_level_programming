#!/usr/bin/python3

"""
Contains the MyInt class
"""


class MyInt(int):
    """
    A class that inherits from int and inverts == and != operators
    """

    def __eq__(self, other):
        """Override the == operator."""
        if isinstance(other, MyInt):
            return self != other
        return False

    def __ne__(self, other):
        """Override the != operator."""
        return not self.__eq__(other)
