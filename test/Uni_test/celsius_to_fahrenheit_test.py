import unittest

from Uni.celsius_to_fahrenheit import celsius_to_fahrenheit


class TestCelsiusToFahrenheit(unittest.TestCase):
    def test_celsiusToFahrenheit1(self):
        self.assertEqual(32.0, celsius_to_fahrenheit(0))
        self.assertEqual(59.18, celsius_to_fahrenheit(15.1))
        self.assertEqual(122, celsius_to_fahrenheit(50))
        self.assertEqual(14, celsius_to_fahrenheit(-10))

