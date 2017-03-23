
def add(input_string):
    cnt = 0
    if input_string:
        input_list = input_string.replace("\n", ',').strip().split(",")
        if len(input_list) == 1:
            cnt = int(input_list[0])
        else:
            cnt = reduce(lambda x, y: int(x) + int(y), input_list)

    return cnt
