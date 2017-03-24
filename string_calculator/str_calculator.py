# coding=utf-8
def add(input_str):
    # 转换为数字数组
    numbers = convert_to_numbers(input_str)
    # 求和
    return sum(numbers)


def convert_to_numbers(input_str):
    if not input_str:
        return []
    numbers = input_str.split(",")
    numbers = map(convert_to_int, numbers)
    return numbers


def convert_to_int(number_str):
    return int(number_str)
