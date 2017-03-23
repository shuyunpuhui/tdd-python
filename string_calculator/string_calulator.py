# -*- coding: utf-8 -*-
import re
def calculate(input_number):

    if not input_number:
        return 0
    number_list = []
    negatives_list = []
    if input_number.startswith('//') and '\n' in input_number:
        input_number = input_number.split('\n')
        delimiter = input_number[0][-1]
        number_list = input_number[1].split(delimiter)
    elif '\n' in input_number:
        input_number = input_number.replace('\n', ',')
        number_list = input_number.split(',')
    if not number_list:
        number_list = input_number.split(',')
    for i in number_list:
        if int(i) < 0:
            negatives_list.append(i)
    if negatives_list:
        raise Exception('negatives not allowed:%s' % ','.join(negatives_list))
    number_list = map(lambda x: int(x), number_list)
    return sum(number_list)
