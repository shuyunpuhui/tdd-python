# -*- coding: utf-8 -*-

import unittest

import string_calulator


class StingCalculatorTest(unittest.TestCase):
    def test_should_return_0_if_input_is_null(self):
        self.assertEqual(0, string_calulator.calculate(''))

    def test_should_return_1_if_input_is_1(self):
        self.assertEqual(1, string_calulator.calculate('1'))

    def test_should_return_int_number_if_input_is_string_number(self):
        self.assertEqual(2, string_calulator.calculate('2'))

    def test_should_return_sum_if_input_is_two_string_number(self):
        self.assertEqual(5, string_calulator.calculate('2,3'))

    def test_should_return_sum_if_input_is_more_string_number(self):
        self.assertEqual(14, string_calulator.calculate('2,3,4,5'))

    def test_should_return_sum_if_input_is_more_string_number_with_delimiter_n(self):
        self.assertEqual(6, string_calulator.calculate('1\n2,3'))

    def test_should_return_sum_if_input_is_more_string_number_with_self_define_delimiter(self):
        self.assertEqual(3, string_calulator.calculate('//;\n1;2'))

    def test_should_show_the_number_when_if_negative(self):
        with self.assertRaises(Exception) as context:
            string_calulator.calculate('//;\n-1;2;-9')
        self.assertIn('-1', context.exception.message)
        self.assertIn('-9', context.exception.message)
        self.assertIn('-91', context.exception.message)

