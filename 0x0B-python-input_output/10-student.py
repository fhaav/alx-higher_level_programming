#!/usr/bin/python3

"""
Module containing Student class
"""


class Student:
    """ Class representing a student. """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student instance.
        """
        if isinstance(attrs, list):
            return {key: self.__dict__[key]
                    for key in self.__dict__ if key in attrs}
        return self.__dict__
