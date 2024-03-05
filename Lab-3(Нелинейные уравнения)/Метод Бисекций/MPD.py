def get_average(interval):
    return (interval[0] + interval[1]) / 2
def get_epsilon(interval):
    return abs(interval[1] - interval[0]) / 2
def get_f(a, b, c, x):
    return a * x * x + b * x + c
interval = [1, 2]
a = None
b = None
c = None
file = open("uravnenie.txt", "r")
equation = file.readline()
file.close()
for i in range(len(equation)):
    if equation[i] == "x":
        a = equation[0:i]
        equation = equation[i+3:]
        break
for i in range(len(equation)):
    if equation[i] == "x":
        b = equation[0:i]
        equation = equation[i+1:]
        break
c = equation
equation = None
n = 1
if a == "" or a == "-":
    a += "1"
a = int(a)
if b == "+" or b == "-":
    b += "1"
b = int(b)
if c == "+" or c == "-":
    c += "1"
c = int(c)
fa = get_f(a, b, c, interval[0])
fb = get_f(a, b, c, interval[1])
average = get_average(interval)
epsilon = get_epsilon(interval)
while True:
    fC = get_f(a, b, c, average)
    multiply1 = fa * fC
    multiply2 = fC * fb
    if multiply1 < 0:
        if abs(average - interval[0]) <= epsilon:
            pass
        elif abs(average - interval[0]) / 2 <= epsilon:
            break
    else:
        if abs(interval[1] - average) <= epsilon:
            pass
        elif abs(interval[1] - average) / 2 <= epsilon:
            break
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Шаг {n}:")
    if multiply1 < 0:
        text1 = f"f(a) * f(C) = {multiply1} < 0"
        text2 = f"({interval[0]}, {average})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        text1 = f"f(C) * f(b) = {multiply2}"
        text2 = f"({average}, {interval[1]})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        interval[1] = average
    else:
        text1 = f"f(a) * f(C) = {multiply1}"
        text2 = f"({interval[0]}, {average})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        text1 = f"f(C) * f(b) = {multiply2} < 0"
        text2 = f"({average}, {interval[1]})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        interval[0] = average
    fa = get_f(a, b, c, interval[0])
    fb = get_f(a, b, c, interval[1])
    average = get_average(interval)
    epsilon = get_epsilon(interval)
    n += 1
print("---------------------------------------------------------------------------------------------------------")
print(f"Точное решение x = {average}")