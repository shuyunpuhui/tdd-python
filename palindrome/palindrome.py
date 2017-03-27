def is_palindrome(input_str):
    return input_str[::-1] == input_str


def get_palindrome(num):
    return filter(is_palindrome, range(1, num))
