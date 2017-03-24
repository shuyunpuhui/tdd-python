# -*- coding:utf-8 -*-


def calculate(input_number):
    if dividable_by(input_number, 3) and dividable_by(input_number, 5):
        return "fizzbuzz"
    if dividable_by(input_number, 3):
        return "fizz"
    if dividable_by(input_number, 5):
        return "buzz"
    else:
        return str(input_number)


def dividable_by(number, divisor):
    return number % divisor == 0


# TODO Anybody help me, How can I test this function  ???????
def raw_input_range(begin_num, end_num):
    for i in range(begin_num, end_num + 1):
        print str(i) + '--->' + calculate(i)

if __name__ == "__main__":
    raw_input_range(1, 10)
