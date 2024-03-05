def get_f(a, b, c, x):
    return a * x * x + b * x + c
def get_df(a, b, x):
    return 2 * a * x + b
def get_x(a, b, c, old_x):
    return old_x - get_f(a, b, c, old_x) / get_df(a, b, old_x)
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
eps = 10 ** -8
interval = [1, 2]
old_x = interval[1]
x = get_x(a, b, c, old_x)
print("-----------------------")
print(f"x0 = {old_x}")
n = 1
while get_f(a, b, c, x) > eps:
    print("-----------------------")
    print(f"x{n} = {x}")
    x = get_x(a, b, c, x)
    n += 1
print("-----------------------")
print(f"x{n} = {x}")