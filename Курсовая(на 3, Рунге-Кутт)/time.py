#Метод Рунге-Кутта 2-го порядка: с усреднением по времени

import numpy as np
from math import e
def func(x, y1, y):

    #return np.asarray([y1, ((e ** (x - 1)) + y + y1) / 3])
    return np.asarray([y1, ((e ** x) + y + y1) / 3])

def func_1(x, y, h):
    y_l = y + h / 2 * func(x, y[1], y[0])
    y_1 = y + h * (func(x + h / 2, y_l[1], y_l[0]))
    return y_1

# h = 0.1
# x = 1
# y = np.asarray([1, 1])
# ht = [i for i in np.arange(1, 5/2, 0.2)]
# for i in range(0, 5):
#     res, y = func_1(ht[i], y, h)
#     print("\t", res)
#     print("\t", y)
#     print()

eps = 10 ** (-6)

h = 0.1
x = 0
n = 10
y = np.asarray([1, 1])

ht = [i for i in np.arange(0, n / 2, 0.1)]
print("\t\t", "x", "\t\t\t", "y", "\t\t\t\t\t\t", "y'")
print()

def call_print(c):
    h = (n/2)*c
    ht = [i for i in np.arange(0, h, 0.1)]
    y_r = [0] * n * c
    h = 0.1 / c
    y = np.asarray([1, 1])
    print("Шаг: ", h)
    # print("\t\t", '{:.1f}'.format(ht[0]), "\t\t", *y)
    for i in range(0, n * c):
        y_f = y
        y = func_1(ht[i] / c, y, h)
        y_h = y
        y_r[i] = y
        print("\t\t", '{:.2f}'.format(ht[i + 1] / c), "\t\t", *y)
    print("Точность при шаге: ", h)
    return y_r



mas_f = [0] * n
mas_s = [0] * n
mas = [0] * 2

i = 1
raz = 1

sh = 1

while ((3 * eps) < raz) == True:
    print(max(raz, (3 * eps)))
    print(raz, (3 * eps))

    mas_f[i] = call_print(sh)
    sh *= 2
    mas_s[i] = call_print(sh)

    a = mas_f[i][-1][0]
    b = mas_s[i][-1][0]
    raz = b - a

    if ((3 * eps) < raz) == False:
        print("END")

    mas_f = [0] * n * sh
    mas_s = [0] * n * sh
    i += 1
