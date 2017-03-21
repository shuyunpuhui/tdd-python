# -*- coding: utf-8 -*-

def calculate(input_number):
    if input_number == '':
        return 0
    return sum(int(i) for i in input_number.split(','))