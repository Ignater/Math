import numpy as np
def etken(pi, pj, xi, xj, x):
    # print((pi * (x - xj) - pj * (x - xi))/(xi - xj))
    return (pi * (x - xj) - pj * (x - xi))/(xi - xj)

def num(x,y,xn):
    p = y.copy()
    p = list(p)
    print()
    for i in range(len(x) - 1):
        p1 = []
        for j in range(len(x) - i - 1):
            print(f"{etken(p[j], p[j+1], x[j], x[j+1+i], xn):.5f}", end = " ")
            p1.append(etken(p[j], p[j+1], x[j], x[j+1+i], xn))
        print()
        p.clear()
        p = p1
    print()
    return p[0]

if __name__=="__main__":
    x = np.array([1.2, 1.5, 1.8, 2.1])
    y = np.array([0.1823, 0.4054, 0.5878, 0.7419])
    x0 = [i for i in np.arange(0, 5, 0.3)]
    i = 1.6
    num(x, y, i)
