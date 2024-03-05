from random import randint

def print_split(line_length):
    print("-" * line_length)

def get_length(number):
    return len(str(number))

def print_multiply(results, number1, number2):
    max_length = 0
    lengths = []
    multiply_sum = 0

    for i, number in enumerate(results):
        multiply_sum += number * 10 ** i
        length = get_length(results[i]) + i
        lengths.append(length)
        if length > max_length:
            max_length = length

    length = get_length(multiply_sum)
    if length > max_length:
        max_length = length

    print(f"{' ' * (max_length - get_length(number1))}{number1}")
    print(f"{' ' * (max_length - get_length(number2))}{number2}")
    print_split(max_length)

    for i, number in enumerate(results):
        print(f"{' ' * (max_length - lengths[i])}{number}")

    print_split(max_length)
    print(f"{multiply_sum}\n")
    print(f"Умножение столбиком a * b = {number1} * {number2} = {multiply_sum}")

def multiply(number1, number2):
    print(f"a = {number1}\nb = {number2}")
    print(f"Стандартное умножение a * b = {number1} * {number2} = {number1 * number2}")
    print("Умножение столбиком\n")

    multiply_with_digit = []
    temp_number2 = number2
    while temp_number2 != 0:
        multiply_with_digit.append((temp_number2 % 10) * number1)
        temp_number2 //= 10

    print_multiply(multiply_with_digit, number1, number2)

number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

multiply(number1, number2)