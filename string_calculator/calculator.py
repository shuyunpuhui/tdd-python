# coding=utf-8
# 计算字符串里各个数字之和
from argparse import ArgumentError

PREFIX = "//"


def add(input_string):
    # 转换为数字的数组
    numbers = convert_to_numbers(input_string)
    # 求和
    return sum(numbers)


def convert_to_numbers(input_string):
    if input_string:
        normalized_string = normalize(input_string)
        numbers = normalized_string.split(",")
    else:
        numbers = []
    return map(convert_to_int, numbers)


def convert_to_int(str):
    result = int(str)
    if result < 0:
        raise ArgumentError(None, "%s is a negative number!" % str)
    return result


def normalize(input_numbers):
    if input_numbers.startswith(PREFIX):
        delimiter_index_end = input_numbers.index("\n")
        delimiter = input_numbers[len(PREFIX):delimiter_index_end]
        normalized = input_numbers[delimiter_index_end + 1:].replace(delimiter, ",")
    else:
        normalized = input_numbers.replace("\n", ",")
    return normalized
