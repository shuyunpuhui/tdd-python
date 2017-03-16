# -*- coding:utf-8 -*-


def calculate(input_number):
    if not input_number % 3:
        return "fizz"
    elif not input_number % 5:
        return "buzz"
    else:
        return str(input_number)
