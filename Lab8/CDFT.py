import numpy
from DFT import opposite_discrete_fourier_transform
from functions import print_massive
from functions import create_massive

def get_a_b(a, b, n):
    for _ in range(n):
        a.append(0)
        b.append(0)

def convolution_discrete_fourier_transform(a, b, n):
    T = 0
    c = []
    w = numpy.exp(-2j * numpy.pi / (2 * n))
    for k in range(2 * n):
        c.append(0)
        T += 1
        for m in range(2 * n):
            c1 = 0
            #T += 1
            for j in range(2 * n):
                c1 += a[j] * b[m-j]
                #T += 1
            c[k] += c1 * w ** (k * m)
        c[k] /= 2 * n
    print(T)
    return opposite_discrete_fourier_transform(c)

a = create_massive(100)
b = create_massive(100)
n = len(a)
get_a_b(a, b, n)

c = convolution_discrete_fourier_transform(a, b, n)


print_massive("Массив a:", a)
print_massive("\nМассив b:", b)
print_massive("\nСвёртка a и b:", c)