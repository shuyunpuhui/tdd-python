def calculate(input_str):
    numbers = convert_to_numbers(input_str)
    return sum(numbers)


def convert_to_numbers(input_str):
    if not input_str:
        return []
    if "-" in input_str:
        print input_str
        raise Exception("negatives not allowed")
    if len(input_str)!=1:
        if "//" in input_str:
            if input_str.index("//") == 0:
                str1 = input_str[2]
                str2 = input_str[input_str.index("\n")+1:]
                input_str = str2.replace(str1,",")
    if '\n' in input_str:
        input_str = input_str.replace("\n",",")
    numbers = input_str.split(",")
    numbers = map(convert_to_int, numbers)
    return numbers


def convert_to_int(number_str):
    return int(number_str)
