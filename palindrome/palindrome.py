def is_palindrome(input_str):
    return input_str[::-1] == input_str


def get_palindrome(num):
    return filter(is_palindrome, map(str, range(0, num)))
