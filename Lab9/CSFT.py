from functions import print_massive
from SFT import semi_fast_fourier
from DFT import opposite_discrete_fourier_transform

def get_a_b(a, b, n):
    for _ in range(n):
        a.append(0)
        b.append(0)

def convolution_semi_fast_fourier(a, b):
    a_length = len(a)
    b_length = len(b)

    a = semi_fast_fourier(a)
    b = semi_fast_fourier(b)

    c = []

    for i in range(a_length):
        c.append(0)

        for k in range(a_length):
            l = i - k

            if 0 <= l < b_length:
                c[i] += a[int(k//a_length**(1/2))][int(k % a_length**(1/2))] * b[int(l//b_length**(1/2))][int(l % b_length**(1/2))]

    return opposite_discrete_fourier_transform(c)

a = [5, 6, 2, 3, 4, 8, 2, 4]
b = [8, 5, 3, 7, 6, 4, 6, 3]
n = len(a)
get_a_b(a, b, n)

c = convolution_semi_fast_fourier(a, b)

print_massive("Массив a:", a)
print_massive("\nМассив b:", b)
print_massive("\nСвёртка a и b:", c)