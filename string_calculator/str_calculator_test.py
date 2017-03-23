import unittest
import str_calculator


class StrCalculatorTest(unittest.TestCase):
    def test_should_return_0_when_input_is_empty(self):
        self.assertEqual(0, str_calculator.add(""))

    def test_should_return_the_number_when_input_has_only_one_number(self):
        self.assertEqual(1, str_calculator.add("1"))
        self.assertEqual(50, str_calculator.add("50"))
    #
    def test_should_return_sum_when_input_has_2_numbers(self):
        self.assertEqual(3, str_calculator.add("1,2"))

    def test_should_return_sum_when_input_has_more_numbers(self):
        self.assertEqual(15, str_calculator.add("1,2,3,4,5"))

    def test_should_return_sum_when_input_has_more_numbers(self):
        self.assertEqual(6, str_calculator.add("1\n2,3"))

    def test_should_return_user_separator(self):
        self.assertEqual(3, str_calculator.add("//;\n1;2"))
    # ;1-1;
    def test_should_return_negatives_not_allowed_when_input_negative(self):
        self.assertEqual("negatives not allowed", str_calculator.add("//;\n1;-2"))
