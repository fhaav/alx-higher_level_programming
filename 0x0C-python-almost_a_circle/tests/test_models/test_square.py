#!/usr/bin/python3

""" Contains the SquareTest class """


import unittest
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):
    """ Testing Square Class """
    def setUp(self):
        """Sets up the Square instances for testing"""
        self.s1 = Square(7)
        self.s2 = Square(4, 4)
        self.s3 = Square(6, 1, 6)

    @property
    def size(self):
        """ Getter method for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter method for size """
        self.width = value
        self.height = value

    def test_inheritance(self):
        """Tests if Square inherits from Rectangle"""
        self.assertIsInstance(self.s1, Square)
        self.assertIsInstance(self.s1, Rectangle)

    def test_attributes(self):
        """Tests the attributes of Square instances"""
        self.assertEqual(self.s1.width, 7)
        self.assertEqual(self.s1.height, 7)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.width, 4)
        self.assertEqual(self.s2.height, 4)
        self.assertEqual(self.s2.x, 4)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.width, 6)
        self.assertEqual(self.s3.height, 6)
        self.assertEqual(self.s3.x, 1)
        self.assertEqual(self.s3.y, 6)

    def test_area_calculation(self):
        """Tests the area() method of Square instances"""
        self.assertEqual(self.s1.area(), 49)
        self.assertEqual(self.s2.area(), 16)
        self.assertEqual(self.s3.area(), 36)

    def test_display_output(self):
        """Tests the display() method of Square instances"""
        expected_output_s1 = "#####\n#####\n#####\n#####\n#####\n"
        expected_output_s2 = "  ##\n  ##\n"
        expected_output_s3 = "\n\n\n ###\n ###\n ###\n"
        self.s1.display()
        self.s2.display()
        self.s3.display()

    def test_str_representation(self):
        """Tests the __str__() method of Square instances"""
        expected_output_s1 = "[Square] ({}) {}/{} - {}".format(
            self.s1.id, self.s1.x, self.s1.y, self.s1.width
        )
        expected_output_s2 = "[Square] ({}) {}/{} - {}".format(
            self.s2.id, self.s2.x, self.s2.y, self.s2.width
        )
        expected_output_s3 = "[Square] ({}) {}/{} - {}".format(
            self.s3.id, self.s3.x, self.s3.y, self.s3.width
        )
        self.assertEqual(str(self.s1), expected_output_s1)
        self.assertEqual(str(self.s2), expected_output_s2)
        self.assertEqual(str(self.s3), expected_output_s3)

    def update_args_test(self):
        self.rect.update(10)
        self.rect.update(10, 8)
        self.rect.update(10, 8, 5)
        self.rect.update(10, 8, 5, 7)

        expected_results = [
            "[Rectangle] (10) 2/3 - 4/6",
            "[Rectangle] (10) 2/3 - 8/6",
            "[Rectangle] (10) 5/3 - 8/6",
            "[Rectangle] (10) 5/7 - 8/6"
        ]

        for expected_result in expected_results:
            self.assertEqual(str(self.rect), expected_result)

    def update_kwargs_test(self):
        self.rect.update(id=10)
        self.rect.update(id=10, width=8)
        self.rect.update(id=10, width=8, height=5)
        self.rect.update(id=10, width=8, height=5, x=7)
        self.rect.update(id=10, width=8, height=5, x=7, y=9)

        expected_outputs = [
            "[Rectangle] (10) 2/3 - 4/6",
            "[Rectangle] (10) 2/3 - 8/6",
            "[Rectangle] (10) 2/3 - 8/5",
            "[Rectangle] (10) 7/3 - 8/5",
            "[Rectangle] (10) 7/9 - 8/5"
        ]

        for expected_output in expected_outputs:
            self.assertEqual(str(self.rect), expected_output)

    def test_to_dictionary(self):
        """
        Test for the to_dictionary method of the Square class.
        """
        s1 = Square(20, 4, 1)
        s2 = Square(1, 1)

        expected_dict = {'id': 19, 'size': 20, 'x': 4, 'y': 1}
        self.assertEqual(s1.to_dictionary(), expected_dict)
        expected_dict = {'id': 20, 'size': 1, 'x': 1, 'y': 0}
        self.assertEqual(s2.to_dictionary(), expected_dict)


if __name__ == '__main__':
    unittest.main()
