def T(n):
    if n == 1:
        return 1
    return 3 * T(n // 2) + 3 * n

def print_output(number1, number2):
    n = len(str(number1))

    print(f"a = {number1}\nb = {number2}")
    print(f"Стандартное умножение a * b = {number1} * {number2} = {number1 * number2}")
    print(f"Быстрое умножение a * b = {number1} * {number2} = {fast_multiply(number1, number2, True)}")
    print("Трудоёмкость данного алгоритма T(n) = 3T(n/2) + 3n")
    print(f"n = {n}")
    print(f"T({n}) = {T(n)}\n")

    for i in range(len(number_of_multiplies[0])):
        number_of_multiplies[3][i] = number_of_multiplies[0][i] + number_of_multiplies[1][i] + number_of_multiplies[2][i]

    print(end = " ")

    for i in range(len(number_of_multiplies[0])):
        print(i + 1, end = "  ")

    print("\n-----------------------------------")

    text = ["без переполнения", "+", "++", "итого"]

    for i in range(len(number_of_multiplies)):
        for j in range(len(number_of_multiplies[0])):
            print(f"{number_of_multiplies[i][j]:2} ", end = "")
        print(" ", text[i])

def fast_multiply(number1, number2, flag):
    if number1 < 10 and number2 < 10:
        if flag:
            number_of_multiplies[0][0] += 1

        return number1 * number2

    n = max(len(str(number1)), len(str(number2)))
    k = round(n / 2)

    if n % 2 == 0:
        if flag:
            number_of_multiplies[0][n-1] += 1

        a = number1 // 10 ** k
        b = number1 % 10 ** k
        c = number2 // 10 ** k
        d = number2 % 10 ** k

        u = fast_multiply(a + b, c + d, flag)
        v = fast_multiply(a, c, flag)
        w = fast_multiply(b, d, flag)

        return v * 10 ** (2 * k) + (u - v - w) * 10 ** k + w

    else:
        a1 = number1 // 10 ** (n - 1)
        a2 = number1 % 10 ** (n - 1)
        b1 = number2 // 10 ** (n - 1)
        b2 = number2 % 10 ** (n - 1)

        if flag:
            if a1 and b1:
                number_of_multiplies[2][n-2] += 1

            else:
                number_of_multiplies[1][n-2] += 1

        answer = a1 * b1 * 10 ** (2 * k) + (a1 * b2 + a2 * b1) * 10 ** k + fast_multiply(a2, b2, False)

        return answer

number1 = 3871
number2 = 9211
number_of_multiplies = [[0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]

print_output(number1, number2)