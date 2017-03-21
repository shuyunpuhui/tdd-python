
from __future__ import absolute_import

import unittest

import string_calculator


class StringCalculatorTest(unittest.TestCase):
    def test_should_0_if_input_empty_string(self):
        self.assertEqual(0, string_calculator.add(""))

    def test_should_self_if_single_input(self):
        self.assertEqual(1, string_calculator.add("1"))

    def test_should_return_sum_if_input_two(self):
        self.assertEqual(3, string_calculator.add("1,2"))