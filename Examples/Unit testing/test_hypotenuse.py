# Run this using the command "python -m unittest test_hypotenuse" within this directory

import unittest
from hypotenuse import hypotenuse
import math

class TestHypotenuse(unittest.TestCase):
    # Tests an error is raised of a is negative
    def test_negative_a(self):
        with self.assertRaises(ValueError):
            hypotenuse(-1, 1)

    # Tests an error is raised if b is negative
    # This test should intially fail
    def test_negative_b(self):
        with self.assertRaises(ValueError):
            hypotenuse(1, -1)

    # Tests the correct value is returned when the arguments and return value are integers
    def test_whole_numbers(self):
        self.assertEqual(hypotenuse(3,4), 5)

    # Tests the correct value is returned when the arguments and return value are floats
    def test_non_whole_numbers(self):
        self.assertAlmostEqual(hypotenuse(8.5,10.5), math.sqrt(182.5))