import unittest
import calculator


class TestStringCalculator(unittest.TestCase):
    def test_should_return_0_when_input_is_empty(self):
        self.assertEqual(0, calculator.add(""))

    def test_should_return_the_number_if_input_has_only_one_number(self):
        self.assertEqual(1, calculator.add("1"))
        self.assertEqual(2, calculator.add("2"))
        self.assertEqual(1100, calculator.add("1100"))

    def test_should_return_the_sum_if_input_has_two_numbers(self):
        self.assertEqual(3, calculator.add("1,2"))

    def test_should_return_the_sum_if_input_has_three_numbers(self):
        self.assertEqual(6, calculator.add("1,2,3"))

    def test_should_consider_new_line_as_a_delimiter(self):
        self.assertEqual(10, calculator.add("1,2,3\n4"))
