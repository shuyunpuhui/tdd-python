
from __future__ import absolute_import

import unittest

import fizeebuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_1_if_input_is_1(self):
        self.assertEquals("1", fizeebuzz.calculate(1))

    def test_should_return_number_if_input_is_normal(self):

        self.assertEqual(str(16), fizeebuzz.calculate(16))

    def test_should_return_fizz_if_input_is_3(self):
        self.assertEqual("Fizz", fizeebuzz.calculate(3))

    def test_should_return_buzz_if_input_is_5(self):
        self.assertEqual("Buzz", fizeebuzz.calculate(5))

    def test_should_return_fizzbuzz_if_dividable_by_3_and_5(self):
        self.assertEqual("FizzBuzz", fizeebuzz.calculate(15))
