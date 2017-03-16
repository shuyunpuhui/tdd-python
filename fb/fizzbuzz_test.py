import unittest

from fizzbuzz import calculate


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_0_when_input_is_0(self):
        self.assertEqual("0", calculate(0))

    def test_should_return_the_number_if_it_is_normal(self):
        self.assertEqual("1", calculate(1))
