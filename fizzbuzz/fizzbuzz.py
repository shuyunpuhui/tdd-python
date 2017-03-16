def calculate(input_number):
    if dividable_by(input_number, 3) and dividable_by(input_number, 5):
        return "fizzbuzz"
    if dividable_by(input_number, 3):
        return "fizz"
    if dividable_by(input_number, 5):
        return "buzz"
    return str(input_number)


def dividable_by(number, divisor):
    return number % divisor == 0
