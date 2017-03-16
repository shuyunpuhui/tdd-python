import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_should_return_1_if_input_is_1(self):
        self.assertEqual("1", fizzbuzz.calculate(1))

    def test_should_return_the_number_if_input_is_normal(self):
        self.assertEqual("13", fizzbuzz.calculate(13))

    def test_should_return_fizz_if_dividable_by_3(self):
        self.assertEqual("fizz", fizzbuzz.calculate(3))
        self.assertEqual("fizz", fizzbuzz.calculate(12))

    def test_should_return_buzz_if_dividable_by_5(self):
        self.assertEqual("buzz", fizzbuzz.calculate(5))
        self.assertEqual("buzz", fizzbuzz.calculate(10))

    def test_should_return_buzz_if_dividable_by_5_and_by_3(self):
        self.assertEqual("fizzbuzz", fizzbuzz.calculate(15))
        self.assertEqual("fizzbuzz", fizzbuzz.calculate(60))
