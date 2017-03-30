# coding=utf-8
import unittest
import palindrome


class PalindromeTest(unittest.TestCase):
    def test_should_return_all_palindrome_frome_1_to_1000(self):
        self.assertIn("1", palindrome.get_palindrome(1000))
        self.assertIn("11", palindrome.get_palindrome(1000))
        self.assertIn("121", palindrome.get_palindrome(1000))
        self.assertIn("929", palindrome.get_palindrome(1000))

        # 实现一个方法，验证是否是回文

    def test_shoud_return_true_if_empty(self):
        self.assertTrue(palindrome.is_palindrome(""))

    def test_should_return_false_if_not_palindrome(self):
        self.assertFalse(palindrome.is_palindrome("12"))

    def test_should_return_true_if_only_one_letter(self):
        self.assertTrue(palindrome.is_palindrome("1"))

    def test_should_return_true_if_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("1221"))
