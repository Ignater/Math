from math import *
import numpy as np

def f(x:float):
    return 1/x

def trap(a:float, b:float, h:float):
    sum = 0
    n1 = (int)((b - a) / h + 1)
    n = n1
    y = np.zeros(n1)

    for i in range(0, n):
        y[i] = f(a + i * h)
    for i in range(1, n-1):
        sum += y[i]
    sum2 = 0.5 * (y[0] + y[n - 1])

    return h * (sum + sum2)

def Simpsom(a:float, b:float, h:float):
    sum3 = 0
    sum4 = 0
    n1 =(int)((b - a) / h + 1)
    n = n1
    y = np.zeros(n1)

    for i in range(0,n):
        y[i] = f(a + i * h)
    for i in range(1,n-1):
        if(i % 2 != 0):
            sum3 += y[i]
        else:
            sum4 += y[i]

    sum5 = y[0] + y[n - 1]
    return ((h / 3) * (sum5 + 4 * sum3 + 2 * sum4))

eps = 0
h = 0.1
a = 1
b = 2
k = 1
z = 0
epss = 1 * 10**(-8)

print("\n\tФ. ТРАПЕЦИИ\n")
while True:
    print()
    print()
    print(" Шаг:", z)
    z += 1
    a1 = trap(a, b, h / k)
    a2 = trap(a, b, h / (k * 2))
    print("IH =", a1)
    print("IH/2 =", a2)
    print("")
    k *= 2
    print("H = ", h/k)
    print("",fabs(a1 - a2))
    print("", 3 * epss)
    if(fabs(a1 - a2) < 3 * epss):
        break
z = 0
k = 1

print("------------------------------------------------------------")
print("\n\tФ. СИМПСОН\n")
while True:
    print()
    print()
    print(" Шаг:", z)
    z += 1
    a1 = Simpsom(a, b, h / k)
    a2 = Simpsom(a, b, h / (k * 2))
    print("IH =", a1)
    print("IH/2 =", a2)
    print("")
    k *= 2
    print("H = ", h / k)
    print("", fabs(a1 - a2))
    #print("", 15 * epss)
    if (fabs(a1 - a2) < 15 * epss):
        break