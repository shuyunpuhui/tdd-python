
# from __future__ import absolute_import

import unittest
from argparse import ArgumentError
import string_calculator


class StringCalculatorTest(unittest.TestCase):
    def test_should_0_if_input_empty_string(self):
        self.assertEqual(0, string_calculator.add(""))

    def test_should_self_if_single_input(self):
        self.assertEqual(1, string_calculator.add("1"))

    def test_should_return_sum_if_input_two(self):
        self.assertEqual(3, string_calculator.add("1,2"))

    def test_should_return_sum_if_input_more_then_tow(self):
        self.assertEqual(10, string_calculator.add("1,             2, 3, 4"))

    def test_should_return_sum_if_input_has_space_inside_numbers(self):
        self.assertEqual(6, string_calculator.add("1\n2,3"))

    def test_should_return_sum_if_input_has_selfdefined_delimiter(self):
        self.assertEqual(9, string_calculator.add("\\`\n3`3`3"))

    def test_should_raise_exception_when_has_number_which_is_fushu(self):
        self.assertRaises(ArgumentError, string_calculator.add, "\\%\n7%-9%8%9%-88")
