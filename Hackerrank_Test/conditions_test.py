import unittest
import conditions

class TestConditions(unittest.TestCase):
    def test_conditions1(self):
        self.assertEqual("Weird", conditions.weirdNumber(3))
        self.assertEqual("Not Weird", conditions.weirdNumber(4))

    def test_conditions2(self):
        self.assertEqual("Not Weird", conditions.weirdNumber(24))
        self.assertEqual("Weird", conditions.weirdNumber(10))
