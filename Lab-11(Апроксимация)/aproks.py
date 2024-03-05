import math
import numpy as np
import matplotlib.pyplot as plt


def g0(x):
    return 1

def g1(x):
    return x

def g2(x):
    return x**2


def fill_C(C, x):
    for i in range(0, len(x)):
        C[0][0] += g0(x[i]) * g0(x[i])
        C[0][1] += g0(x[i]) * g1(x[i])
        C[0][2] += g0(x[i]) * g2(x[i])
        C[1][0] += g1(x[i]) * g0(x[i])
        C[1][1] += g1(x[i]) * g1(x[i])
        C[1][2] += g1(x[i]) * g2(x[i])
        C[2][0] += g2(x[i]) * g0(x[i])
        C[2][1] += g2(x[i]) * g1(x[i])
        C[2][2] += g2(x[i]) * g2(x[i])


def fill_Y(Y, y, x):
    for j in range(0, len(y)):
        Y[0] += y[j] * g0(x[j])
    for j in range(0, len(y)):
       Y[1] += y[j] * g1(x[j])
    for j in range(0, len(y)):
        Y[2] += y[j] * g2(x[j])


def func(x, O):
    # count = O[0] * x + O[1] + O[2] * math.sqrt(x)
    return O[0] + O[1] * x + O[2] * x**2

if __name__ == "__main__":
    x = [0.000, 1.0000, 2.0000, 3.0000]
    y = [0.000, 1.0000, 4.00000, 9.0000]

    C = [0.0000, 0.0000, 0.0000], [0.0000, 0.0000, 0.0000], [0.000, 0.000, 0.000]

    Y = [0.000, 0.000, 0.000]

    P = []

    fill_C(C, x)
    fill_Y(Y, y, x)

    print("C = ", C)
    print()
    print("Y = ", Y)
    P = np.linalg.solve(C, Y) #решение методом Гаусса
    print()
    print("P = ", P)

    x_graf = []
    y_graf = []
    y_graf1 = []

    point = 1000
    start = 0
    interval = 0.006
    for i in range(0, point):
        x_graf.append(start)
        start += interval
    for i in range(0, len(x_graf)):
        y_graf.append(func(x_graf[i], P))

    plt.plot(x_graf, y_graf, color=(1, 0, 0))

    plt.plot(x, y, 'o')
    plt.show()