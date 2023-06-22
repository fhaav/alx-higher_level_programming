#!/usr/bin/python3

"""
Contains Unittests for the Base class
"""


import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Test cases for the Base class """

    def test_single_instance(self):
        """ Test creation of a single instance without custom ID """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_multiple_instances(self):
        """ Test creation of multiple instances without custom ID """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, 5)

    def test_custom_id(self):
        """ Test creation of instances with custom ID """
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_increment_id(self):
        """ Test the incrementing behavior of IDs """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        """
        Test the to_json_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expect_json_string = '[{"id": 2, "width": 10, "height": 7, ' \
            '"x": 2, "y": 8}]'
        self.assertEqual(json_string, expect_json_string)

    def test_from_json_string(self):
        """ Test the from_json_string method """
        json_string = Base.from_json_string(None)
        self.assertEqual(json_string, [])

        json_string = Base.from_json_string("")
        self.assertEqual(json_string, [])

        json_string = (
            '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
            '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
        )
        expected_list = [
            {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8},
            {"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}
        ]
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, expected_list)

    def test_save_to_file(self):
        """ Test the save_to_file method """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            json_string = file.read()
            obj_list = json.loads(json_string)
            expected_list = [
                {"id": 6, "width": 10, "height": 7, "x": 2, "y": 8},
                {"id": 7, "width": 2, "height": 4, "x": 0, "y": 0}
            ]
            self.assertEqual(obj_list, expected_list)

        # Clean the created file
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
