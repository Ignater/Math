#Усред по времени
import math
from math import *
import numpy as np
def func(x , y1 , y):

    return np.asarray([y1, (e**(x-1) + y + y1)/3])

def func_1(x , y , h):
    y_l = y + h / 2 * func(x , y[1] , y[0])
    y_1 = y + h * (func(x + h / 2, y_l[1],y_l[0]))
    return y_l , y_1

if __name__ == "__main__":
    ht = [i for i in np.arange(1, 5 / 2, 0.2)]
    h = 0.2
    x = 1
    y = np.asarray([1 , 1])
    for i in range(0,5):
        res , y = func_1(ht[i], y, h)
        print("y_ =",res ,"y =", y)