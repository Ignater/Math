import numpy as np
import matplotlib.pyplot as plt

def lagrange(x:list, y:list, xn:float):
    l = 0
    for i in range(len(y)):
        p1 = 1
        p2 = 1
        for j in range(len(x)):
            if j != i:
                p1 *= (xn - x[j])
                p2 *= (x[i] - x[j])
        l= l + y[i] * p1 / p2
    return l

x = [i+1 for i in range(0,2)]
y = [i**(1/2) for i in x]
# print('%.4f' % lagrange(x, y, 2.56))

x0 = [i for i in range(0,3)]
y0 = [i**(1/2) for i in x0]

spis = []
for i in np.arange(0, 1.6, 0.3):
    spis.append(lagrange(x, y, i))
print(spis)
plt.plot(x0, y0, color = "black")
plt.plot(x, y, "o", color = "black")
plt.plot(np.arange(0, 1.6, 0.3), spis, color = "red")
plt.show()