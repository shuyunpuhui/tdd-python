import unittest

import string1


class stringTest(unittest.TestCase):
    def test_should_return_0_if_input_is_empty(self):
        self.assertEqual(0, string1.calculate(""))

    def test_should_return_this_number_if_input_is_number(self):
        self.assertEqual(1, string1.calculate("1"))

    def test_should_return_add_number_if_input_is_two_number_single(self):
        self.assertEqual(3, string1.calculate("1,2"))

    def test_should_return_add_number_if_input_is_two_number_double(self):
        self.assertEqual(33, string1.calculate("11,22"))

    def test_should_return_add_number_if_input_is_three_number_contain_special_characters(self):
        self.assertEqual(6, string1.calculate("1\n2,3"))

    def test_should_return_add_number_if_input_is_three_number_contain_special_characters2(self):
        self.assertEqual(3, string1.calculate("//;\n1;2"))

    def test_should_return_add_number_if_input_is_three_number_contain_special_characters3(self):
        try:
            self.assertEqual(1, string1.calculate("-2"))
        except Exception, e:
            print Exception, ":", e




