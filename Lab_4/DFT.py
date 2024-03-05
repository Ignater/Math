import numpy
from functions import create_massive
def discrete_fourier_transform(f):
    T = 0
    N = len(f)
    A = []
    for k in range(N):
        A.append(0)
        for n in range(N):
            A[k] += numpy.exp(-2j * numpy.pi * k * n / N) * f[n]
            T += 1
        A[k] /= N ** 2
    print(T)
    return A

def opposite_discrete_fourier_transform(A):
    T = 0
    N = len(A)
    f = []
    for k in range(N):
        f.append(0)
        for n in range(N):
            f[k] += numpy.exp(2j * numpy.pi * k * n / N) * A[n]
            T += 1
        f[k] = round(f[k].real)
    #print(T/2)
    return f

if __name__ == "__main__":
    f = create_massive(1600)
    dft = discrete_fourier_transform(f)
    opposite_dft = opposite_discrete_fourier_transform(dft)
    #print(dft)
    # print(opposite_dft)