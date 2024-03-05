import math
import numpy as np
from math import *
def func(x , y1 , y):
    return (e**(x-1) + y + y1)/3

def func_1(x , y , h):
    k1 = np.ndarray(shape = (2,))
    k2 = np.ndarray(shape = (2,))
    k3 = np.ndarray(shape = (2,))
    k4 = np.ndarray(shape = (2,))

    k1[0] = y[1]
    k1[1] = func(x,y[1],y[0])

    matr = y + h/2 * k1
    k2[0] = matr[1]
    k2[1] = func(x + h / 2,matr[1],matr[0])

    matr1 = y + h/2 * k2
    k3[0] = matr1[1]
    k3[1] = func(x + h / 2, matr1[1], matr1[0])

    matr2 = y + h * k3
    k4[0] = matr2[1]
    k4[1] = func(x + h, matr2[1], matr2[0])

    y_f = y + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return y_f

if __name__ == "__main__":
    ht = [i for i in np.arange(1, 5 / 2, 0.2)]
    h = 0.2
    x = 1
    y = np.asarray([1 , 1])
    for i in range(0,5):
        y_f = y
        y = func_1(ht[i],y,h)
        print("y #",i,"=",y)

