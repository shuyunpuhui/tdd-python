# -*- coding:utf-8 -*-

from unittest import TestCase

import fizzbuzz


class FizzBuzzTest(TestCase):

    def test_should_return_1_if_input_is_1(self):
        self.assertEqual("1", fizzbuzz.calculate(1))

    def test_should_return_the_number_if_number_is_normal(self):
        self.assertEqual("11", fizzbuzz.calculate(11))

    def test_should_return_fizz_if_input_is_3(self):
        self.assertEqual("fizz", fizzbuzz.calculate(3))

<<<<<<< HEAD
    def test_should_return_buzz_if_input_is_5(self):
        self.assertEqual("buzz", fizzbuzz.calculate(10))

    def test_should_return_fizzbuzz_if_diviable_by_3_and_5(self):
        self.assertEqual("fizzbuzz", fizzbuzz.calculate(15))
=======
    def test_should_return_fizz_if_input_is_dividable_by_3(self):
        self.assertEqual("fizz", fizzbuzz.calculate(9))

    def test_should_return_buzz_if_input_is_dividable_by_5(self):
        self.assertEqual("buzz", fizzbuzz.calculate(10))

    def test_should_return_fizzbuzz_if_dividable_by_3_and_5(self):
        self.assertEqual("fizzbuzz", fizzbuzz.calculate(15))


>>>>>>> fd23adb974662d90cbb61ff763029b7a4e93a5d5
