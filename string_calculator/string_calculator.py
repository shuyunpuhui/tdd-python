# coding=utf-8

from argparse import ArgumentError


def add(input_string):
    delimiter = ","
    if input_string.startswith("//"):
        delimiter_index = input_string.rfind('//')
        delimiter = input_string[delimiter_index+2:delimiter_index+3]
        input_string = input_string[delimiter_index+4:]
    input_list = convert_to_int(input_string, delimiter)

    return sum(input_list)


def convert_to_int(input_string, delimiter):
    input_list = []
    if input_string:
        input_list = input_string.replace("\n", delimiter).strip().split(delimiter)
        input_list = map(convert_str_to_int, input_list)

    return input_list


def convert_str_to_int(input_str):
    number = int(input_str)
    if number < 0:
        raise ArgumentError(None, "negatives:%s not allowed" % number)

    return number
