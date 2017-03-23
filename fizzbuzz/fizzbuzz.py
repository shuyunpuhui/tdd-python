# -*- coding:utf-8 -*-


def calculate(input_number):
<<<<<<< HEAD

=======
>>>>>>> fd23adb974662d90cbb61ff763029b7a4e93a5d5
    if dividable_by(input_number, 3) and dividable_by(input_number, 5):
        return "fizzbuzz"
    if dividable_by(input_number, 3):
        return "fizz"
    if dividable_by(input_number, 5):
        return "buzz"
<<<<<<< HEAD
    else:
        return str(input_number)
=======
    return str(input_number)
>>>>>>> fd23adb974662d90cbb61ff763029b7a4e93a5d5


def dividable_by(number, divisor):
    return number % divisor == 0
<<<<<<< HEAD


# TODO Anybody help me, How can I test this function  ???????
def raw_input_range(begin_num, end_num):
    for i in range(begin_num, end_num + 1):
        print str(i) + '--->' + calculate(i)


if __name__ == "__main__":
    raw_input_range(1, 10)
=======
>>>>>>> fd23adb974662d90cbb61ff763029b7a4e93a5d5
