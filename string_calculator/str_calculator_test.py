import unittest
import str_calculator


class StrCalculatorTest(unittest.TestCase):
    def test_should_return_0_when_input_is_empty(self):
        self.assertEqual(0, str_calculator.add(""))
