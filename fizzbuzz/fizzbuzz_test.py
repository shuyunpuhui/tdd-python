import unittest

import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_1_if_input_is_1(self):
        self.assertEqual("1", fizzbuzz.calculate(1))