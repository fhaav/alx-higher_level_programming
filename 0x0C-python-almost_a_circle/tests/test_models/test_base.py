#!/usr/bin/python3

"""
Contains Unittests for the Base class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ Test cases for the Base class """

    def test_single_instance(self):
        """ Test creation of a single instance without custom ID """
        b1 = Base()
        self.assertEqual(b1.id, 6)

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
        expect_json_string = '[{"id": 7, "width": 10, "height": 7, ' \
            '"x": 2, "y": 8}]'
        self.assertEqual(json_string, expect_json_string)


if __name__ == '__main__':
    unittest.main()
