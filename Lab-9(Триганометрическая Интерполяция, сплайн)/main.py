from math import *
import cmath as cm
import numpy as np
from numpy import *
import matplotlib.pyplot as plt


def A_fun(y: list, n: int, j: int):
    A =  sum([y[k] * cm.exp(complex(0, -2 * pi * k * j / n)) for k in range(0, n)])
    return A


def Y_fun(n: int, x0: float, x: float, y: list, h: float):
    Y = 1/n * sum([A_fun(y, n, j) * cm.exp(complex(0, 2 * pi * j * (x - x0) / (n * h)))
                   for j in range(-1, n//2 + 1)])
    return Y


def xy(count, h, xn_, name):
    x_ = np.zeros(count)
    x_[0] = xn_
    for i in range(1, count):
        x_[i] = x_[i - 1] + h
    y_ = fun(x_, name)
    return x_,y_


def fun(x: np.ndarray, fun_name: str):
    if fun_name == "sqrt x":
        return np.sqrt(np.abs(x))
    if fun_name == "x**2":
        return x**2
    if fun_name == "exp x":
        return np.exp(x)


if __name__ == "__main__":
    count = int(input("Vvedite tochki: "))
    xn_ = double(input("Vvedite x0: "))
    h = double(input("Vvedite shag: "))
    name = input("Vvedite func: ")

    start = -5
    stop = 5
    shag = 0.05

    # name = "sqrt x"

    x,y = xy(count, h, xn_, name)
    graf = np.asarray([i for i in np.arange(start,stop + shag,shag)])
    spis = []
    for i in graf:
        spis.append(Y_fun(count, xn_, i, y, h))
    print(spis)
    spisdev = [j.real for j in spis]
    spismnim = [j.imag for j in spis]
    # spissum = [sqrt(j.real**2 + j.imag**2) for j in spis]
    # spissum = [j.real + j.imag for j in spis]

    # plt.plot(graf, spisdev, color="red")
    plt.plot(graf, spisdev, color="green")
    plt.plot(graf, spismnim, color="black")
    plt.plot(graf, spismnim)

    # xz = [i for i in range(0, 5)]
    # yz = [0, 0, 0, 0, 0]
    # plt.scatter(xz, yz)
    # plt.plot(graf, spissum, color="green")

    if name == "sqrt x":
        plt.plot(graf[graf.shape[0]//2:], fun(graf[graf.shape[0]//2:],name), color = "red")
    else:
        plt.plot(graf, fun(graf, name), color="red")

    plt.xlim(start, stop)

    #ax = plt.gca()
    #ax.axvline(x=0, color='k')
    #ax.axhline(y=0, color='k')
    plt.plot(x, y, "o", color = "black")

    yy = np.zeros(count)
    print(yy)
    plt.plot(x, yy, "o", color="blue")
    #plt.minorticks_on()
   # plt.grid(which='major', color='#444', linewidth=0.3)
    #plt.grid(which='minor', color='#aaa', ls=':')

    plt.show()
