def calculator(input_string):
    if len(input_string) == 0:
        return 0
    elif "," not in input_string:
        return int(input_string)
    else:
        temp = input_string.split(",")
        temp = map(lambda x: int(x), temp)
        return sum(temp)
