def calculate(input_num):
    dividable_by_3 = dividable_by(input_num, 3)
    dividable_by_5 = dividable_by(input_num, 5)
    if dividable_by_3 and dividable_by_5:
        return "fizzbuzz"
    if dividable_by_3:
        return "fizz"
    if dividable_by_5:
        return "buzz"
    return str(input_num)


def dividable_by(input_num, divider):
    return input_num % divider == 0
