import unittest

import StringCalculator


class StringCalculatorTest(unittest.TestCase):

    def test_should_return_0_if_input_is_empty(self):
        self.assertEqual(0, StringCalculator.calculator(""))

    def test_should_return_self_if_input_is_single(self):
        self.assertEqual(1, StringCalculator.calculator("1"))

    def test_should_return_sum_if_input_is_more_than_one_number(self):
        self.assertEqual(3, StringCalculator.calculator("1,2"))

    def test_should_return_sum_if_input_contains_newline_char(self):
        self.assertEqual(6, StringCalculator.calculator("1\n2,3"))
