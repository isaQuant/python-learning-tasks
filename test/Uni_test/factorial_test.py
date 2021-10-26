import unittest

from Uni.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(1, factorial(1))
        self.assertEqual(720, factorial(6))
        self.assertEqual(20922789888000, factorial(16))


