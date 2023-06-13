#!/usr/bin/python3

"""
Module containing BaseGeometry class
"""


class BaseGeometry:
    """
    Base class for geometry operations.
    """

    def area(self):
        """
        Calculates the area.
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value to be an integer greater than 0.
        Raises TypeError or ValueError if the validation fails.
        """

        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))

        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
