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
