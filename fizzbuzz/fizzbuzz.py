def calculate(input_number):
    if input_number % 3 == 0:
        return "fizz"
    if input_number % 5 == 0:
        return 'buzz'
    else:
        return str(input_number)
