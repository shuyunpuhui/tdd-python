def get_palindrome(num):
    return filter(is_palindrome, map(str, range(1, num)))


def is_palindrome(input_str):
    return input_str[::-1] == input_str
