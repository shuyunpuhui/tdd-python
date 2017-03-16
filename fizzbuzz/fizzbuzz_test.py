# -*- coding:utf-8 -*-

import unittest

import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def setUp(self):
        pass

    # def test_should_return_1_if_input_is_1(self):
    #     self.assertEqual("1", fizzbuzz.calculate(1))

    def test_should_return_the_number_if_number_is_normal(self):
        args = 9
        self.assertEqual(args if (args % 3 == 0) or (args % 5 == 0) else None, fizzbuzz.calculate(args))