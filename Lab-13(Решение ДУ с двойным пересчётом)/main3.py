import numpy as np
from math import e

def func(x, y1, y):

    #return np.asarray([y1, x * y1 - y])
    return np.asarray([y1, ((e**(x-1)) + y + y1)/3])


def func_1(x, y, h):
    y_l = y + h * func(x, y[1], y[0])
    y_1 = y + h * func(x, y[1], y[0])
    return y_l, y_1



y = [0]*5
ht = [i for i in np.arange(1, 5/2, 0.2)]

h = 0.2
x = 1
y = np.asarray([1, 1])
for i in range(0, 5):
    res, y = func_1(ht[i], y, h)
    print("\t", res)
    print()