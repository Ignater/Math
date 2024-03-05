# массивы: 100 400 1600 2500 (целочисленный тип), p1 = p2
import numpy
from functions import *

T = 0
def complex_mul(complex_number, number):
    global T

    T += 1
    return complex(complex_number.real * float(number), complex_number.imag * float(number))

def semi_fast_fourier(f):
    N = len(f)
    p1 = p2 = numpy.sqrt(N)
    A1 = []

    for j2 in range(int(p2)):
        A1.append([])
        for k1 in range(int(p1)):
            A1[j2].append(0)
            for j1 in range(int(p1)):
                # A1[j2][k1] += f[int(j2 + p2 * j1)] * numpy.exp(-2j * numpy.pi * (j1 * k1 / p1))
                A1[j2][k1] += f[int(j2+p2*j1)] * numpy.exp(complex_mul(complex_mul(complex_mul((-1) ** 0.5, -2), numpy.pi), (j1 * k1 / p1)))
            A1[j2][k1] /= p1
    A2 = []
    for k2 in range(int(p2)):
        A2.append([])
        for k1 in range(int(p1)):
            A2[k2].append(0)
            for j2 in range(int(p2)):
                # A2[k2][k1] += A1[j2][k1] * numpy.exp(-2j * numpy.pi * (j2 * (k1 + p1 * k2) / (p1 * p2)))
                A2[k2][k1] += A1[j2][k1] * numpy.exp(complex_mul(complex_mul(complex_mul((-1) ** 0.5, -2), numpy.pi), (j2 * (k1 + p1 * k2) / (p1 * p2))))
            A2[k2][k1] /= p2
    print("Трудоёмкость:", int(N ** 1.5))
    # print(T)
    return A2

f1 = create_massive(100)
f2 = create_massive(400)
f3 = create_massive(1600)
f4 = create_massive(2500)
sff1 = semi_fast_fourier(f1)
sff2 = semi_fast_fourier(f2)
sff3 = semi_fast_fourier(f3)
sff4 = semi_fast_fourier(f4)
print_matrix_for_sff(sff1)
print_matrix_for_sff(sff2)
print_matrix_for_sff(sff3)
print_matrix_for_sff(sff4)