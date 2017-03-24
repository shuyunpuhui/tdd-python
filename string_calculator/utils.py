from argparse import ArgumentError


def get_sum(input_list):
    if not input_list[0]:
        return 0
    input_list = map(int, input_list)
    return sum(input_list)


def get_list_from_str(input_string):
    if '\\' in input_string:
        delimiter = input_string[1]
        ret = ("".join((input_string[2:]).split())).split(delimiter)
    else:
        ret = input_string.replace("\n", ',').strip().split(",")
    is_fushu_in_list(ret)
    return ret


def is_fushu_in_list(input_list):
    ret = []
    for i in input_list:
        if '-' in i:
            ret.append(int(i))
    if ret:
        raise ArgumentError(None, "negatives not allowed {0}".format(ret))