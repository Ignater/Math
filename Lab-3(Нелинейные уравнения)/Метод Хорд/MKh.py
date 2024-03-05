def get_f(a, b, c, x):
    return a * x * x + b * x + c
def get_C(interval, fa, fb):
    return (interval[0] * fb - interval[1] * fa) / (fb - fa)
file = open("uravnenie.txt", "r")
equation = file.readline()
file.close()
a = None
b = None
c = None
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
if a == "" or a == "-":
    a += "1"
a = int(a)
if b == "+" or b == "-":
    b += "1"
b = int(b)
if c == "+" or c == "-":
    c += "1"
c = int(c)
n = 1
eps = 10 ** -3
interval = [1, 2]
old_C = interval[1] + eps
fa = get_f(a, b, c, interval[0])
fb = get_f(a, b, c, interval[1])
C = get_C(interval, fa, fb)
while abs(C - old_C) >= eps:
    fC = get_f(a, b, c, C)
    multiply1 = fa * fC
    multiply2 = fC * fb
    print("---------------------------------------------------------------------------------------------------------")
    print(f"Шаг {n}:")
    if multiply1 < 0:
        text1 = f"f(a) * f(C) = {multiply1} < 0"
        text2 = f"({interval[0]}, {C})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        text1 = f"f(C) * f(b) = {multiply2}"
        text2 = f"({C}, {interval[1]})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        interval[1] = C
    else:
        text1 = f"f(a) * f(C) = {multiply1}"
        text2 = f"({interval[0]}, {C})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        text1 = f"f(C) * f(b) = {multiply2} < 0"
        text2 = f"({C}, {interval[1]})"
        text = text1 + " " * (105 - len(text1) - len(text2)) + text2
        print(text)
        interval[0] = C
    old_C = C
    fa = get_f(a, b, c, interval[0])
    fb = get_f(a, b, c, interval[1])
    C = get_C(interval, fa, fb)
    n += 1
print("---------------------------------------------------------------------------------------------------------")
print(f"Приближённое значение x = {old_C}")