import unittest
import palindrome


class PalindromeTest(unittest.TestCase):

    def test_should_return_palindrome_of_first_1000_numbers(self):
        self.assertIn("1", palindrome.get_palindrome(1000))
        self.assertIn("11", palindrome.get_palindrome(1000))
        self.assertIn("121", palindrome.get_palindrome(1000))
        self.assertIn("989", palindrome.get_palindrome(1000))

    def test_should_return_true_if_empty(self):
        self.assertTrue(palindrome.is_palindrome(""))

    def test_should_return_false_if_two_different_letters(self):
        self.assertFalse(palindrome.is_palindrome("ad"))

    def test_should_return_true_if_only_one_letter(self):
        self.assertTrue(palindrome.is_palindrome("a"))

    def test_should_return_true_if_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("aba"))

    def test_should_return_false_if_not(self):
        self.assertFalse(palindrome.is_palindrome("sdlkfj"))
