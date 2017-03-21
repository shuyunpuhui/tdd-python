import unittest

import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_1_if_input_is_1(self):
        self.assertEqual("1", fizzbuzz.calculate(1))

    def test_should_return_the_number_if_number_is_normal(self):
        self.assertEqual('2', fizzbuzz.calculate(2))

    def test_should_return_fizz_if_number_is_3(self):
        self.assertEqual('fizz', fizzbuzz.calculate(3))
        self.assertEqual('buzz', fizzbuzz.calculate(5))
