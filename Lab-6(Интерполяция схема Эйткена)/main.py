import numpy as np
def etken(pi, pj, xi, xj, x):
    return (pi * (x - xj) - pj * (x - xi))/(xi - xj)

def num(x,y,xn):
    p = y.copy()
    p = list(p)
    for i in range(len(x) - 1):
        p1 = []
        for j in range(len(x) - i - 1):
            p1.append(etken(p[j], p[j+1], x[j], x[j+1+i], xn))
        p.clear()
        p = p1
    return p[0]

if __name__=="__main__":
    x = np.array([1.2, 1.5, 1.8, 2.1])
    y = np.array([1.2214, 1.6487, 2.2255, 3.0041])
    x0 = [i for i in np.arange(0, 5, 0.3)]
    spis = []
    for i in np.arange(0, 5, 0.3):
        spis.append(num(x, y, i))
    print(spis)
