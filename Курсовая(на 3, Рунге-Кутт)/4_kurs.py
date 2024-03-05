import numpy as np
from math import e


def func(x, y1, y):
    return ((e ** x) + y + y1) / 3


def func_1(x, y, h):
    k1 = np.ndarray(shape=(2,))
    k2 = np.ndarray(shape=(2,))
    k3 = np.ndarray(shape=(2,))
    k4 = np.ndarray(shape=(2,))

    k1[0] = y[1]
    k1[1] = func(x, y[1], y[0])

    matr = y + h / 2 * k1
    k2[0] = matr[1]
    k2[1] = func(x + h / 2, matr[1], matr[0])

    matr1 = y + h / 2 * k2
    k3[0] = matr1[1]
    k3[1] = func(x + h / 2, matr1[1], matr1[0])

    matr2 = y + h * k3
    k4[0] = matr2[1]
    k4[1] = func(x + h, matr2[1], matr2[0])

    y_f = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_f


eps = 10 ** (-8)

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

    for i in range(0, n * c):
        y = func_1(ht[i] / c, y, h)
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
while ((15 * eps) < raz) == True:

    mas_f[i] = call_print(sh)
    sh *= 2
    mas_s[i] = call_print(sh)

    a = mas_f[i][-1][0]
    b = mas_s[i][-1][0]
    raz = b - a

    if ((15 * eps) < raz) == False:
        print("END")

    mas_f = [0] * n * sh
    mas_s = [0] * n * sh




