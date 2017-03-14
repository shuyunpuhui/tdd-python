DELIMITER = ","


def add(input_numbers):
    if not input_numbers:
        return 0

    if DELIMITER in input_numbers:
        numbers = input_numbers.split(DELIMITER)
        return reduce(lambda x, y: int(x) + int(y), numbers)

    return int(input_numbers)
