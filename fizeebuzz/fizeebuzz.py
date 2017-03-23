
def calculate(n):
    result = str(n)
    if not not_dividable(n, 15):
        result = "FizzBuzz"
    elif not not_dividable(n, 3):
        result = "Fizz"
    elif not not_dividable(n, 5):
        result = "Buzz"

    return result


def not_dividable(n, d):
    return n % d
