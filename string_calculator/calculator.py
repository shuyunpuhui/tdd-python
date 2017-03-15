# coding=utf-8
# 计算字符串里各个数字之和


def add(input_string):
    # 转换为数字的数组
    numbers = convert_to_numbers(input_string)
    # 求和
    return sum(numbers)


def convert_to_numbers(input_numbers):
    if input_numbers:
        numbers = input_numbers.split(",")
    else:
        numbers = []
    return map(int, numbers)
