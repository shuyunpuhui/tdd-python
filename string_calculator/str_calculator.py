# coding=utf-8
from argparse import ArgumentError


def add(input_str):
    # 转换为数字数组
    numbers = convert_to_numbers(input_str)
    # 求和
    return sum(numbers)


def convert_to_numbers(input_str):
    if not input_str:
        return []
    if '//' in input_str and "\n" in input_str and input_str.index("//") == 0:
        separator = input_str[input_str.index("\n") - 1]
        numbers = input_str.replace("//" + separator + "\n", "").replace("\n", ",").replace(separator, ",").split(",")
    else:
        numbers = input_str.replace("\n", ",").split(",")
    numbers = map(convert_to_int, numbers)
    return numbers


def convert_to_int(number_str):
    if (int(number_str) < 0):
        print "错误参数 " + number_str
        raise ArgumentError(None, "negatives not allowed")
    return int(number_str)
