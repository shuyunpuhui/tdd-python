# -*- coding: utf-8 -*-

import unittest

import stringcalulator


class StingCalculatorTest(unittest.TestCase):
    def test_should_return_0_if_input_is_null(self):
        self.assertEqual(0, stringcalulator.calculate(''))

    def test_should_return_1_if_input_is_1(self):
        self.assertEqual(1, stringcalulator.calculate('1'))

    def test_should_return_int_number_if_input_is_string_number(self):
        self.assertEqual(2, stringcalulator.calculate('2'))

    def test_should_return_sum_if_input_is_two_string_number(self):
        self.assertEqual(5, stringcalulator.calculate('2,3'))


