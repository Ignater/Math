from math import *
import numpy as np

def func_1(x , x1 , y , y1):
    return (x1 - x) * (1/2 * y + 1/2 * y1)

def trap(x:list, y:list):
    res = []
    for i in range(0 , len(x) - 1):
        res.append(func_1(x[i], x[i+1], y[i], y[i+1]))
    return res

def func_2(x, x2, y, y1, y2):
    return (x2 - x) * (1/6 * y + 2/3 * y1 + 1/6 * y2)

def simps(x:list,y:list):
    res = []
    for i in range(0 , len(x) - 2 , 2):
        res.append(func_2(x[i], x[i + 2], y[i], y[i + 1], y[i + 2]))
    return res

def intg(x:list):
    y = []
    for i in x:
        y.append(1/i)
    return y
if __name__ == "__main__":
    h = 0.1
    x = [i for i in np.arange(1,2+h,h)]
    # x = [1]
    # e = 10 ** (-8)
    # i = 0
    # while h > e:
    #     x.append(x[i] + h)
    #     i += 1
    #     h /= 2
    y = intg(x)
    print(x)
    print(y)
    while True:
        flag = int(input("1:Формула трапеций\n"
                     "2:Формула Симпсона\n"
                         "0:Выход\n"))
        if flag == 0:
            exit()
        if flag == 1:
            print("Формула трапеций")
            restrap = trap(x , y)
            sum_res = sum(restrap)
            for i in range(0,len(x)-1):
                print("Интеграл:", restrap[i])
                print("h:", h)
                if(restrap[i] - restrap[i-1] > e):
                    print("Точность достигнута")
                else:
                    print("Точность не достигнута")
                h /= 2
        print("Конечный Интеграл")
        print(sum_res)
        if flag == 2:
            print("Формула Симпсона")
            ressimp = simps(x , y)
            sum_res1 = sum(ressimp)
            print(sum_res1)