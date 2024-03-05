import math

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

def lagrange(x, y, t):
    l = 0
    for i in range(len(y)):
        p1 = 1
        p2 = 1
        for j in range(len(x)):
            if j != i:
                p1 = p1 * (t - x[j])
                p2 = p2 * (x[i] - x[j])
        l = l + y[i] * p1 / p2
    return l

#--Две точки с шагом 2 :
# x = np.array([i+1 for i in np.arange(0, 4, 2)], dtype=float)
# y = np.array([i**(1/2) for i in x], dtype=float)
# x0 = np.array([i for i in np.arange(0, 10, 0.005)], dtype=float)
# y0 = np.array([i**(1/2) for i in x0], dtype=float)
#---

x = np.array([i+1 for i in np.arange(0, 4, 1)], dtype=float)
y = np.array([i**(1/2) for i in x], dtype=float)

x0 = np.array([i for i in np.arange(0, 10, 0.005)], dtype=float)
y0 = np.array([i**(1/2) for i in x0], dtype=float)



#-----
# Значения из контроши
# x = np.array([1.2, 1.5, 1.8], dtype=float)
# y = np.array([1.2214, 1.6487, 2.2255], dtype=float)
# x0 = np.array([i for i in np.arange(0, 4, 0.005)], dtype=float)
# y0 = np.array([math.exp(i-1) for i in x0], dtype=float)
# xn = [i for i in np.arange(0, 4, 0.005)]
# yn = [lagrange(x, y, i) for i in xn]
#-----


print(x0)
print(y0)

v = 2.56
mas = lagrange(x, y, v)
print("\n")
print("C абциссой искомой точки - ", v, "Результат = ", "%.4f" % mas)


plt.plot(x0, y0, lw=1, color="black")
plt.plot(x, y, 'o', lw=1, color="black")

xn = [i for i in np.arange(0, 10, 1)]
yn = [lagrange(x, y, i) for i in xn]
print(xn)
print(yn)
plt.plot(xn, yn, lw=1, color="red")


#plt.text(1.2, 3.5, r'$Интерполирующая$', fontsize=12, color="red", bbox={'facecolor':'yellow','alpha':0.2})
#plt.text(4.5, 0.5, r'$Интерполируемая$', fontsize=12, bbox={'facecolor':'yellow','alpha':0.2})
plt.grid(True)
plt.show()
