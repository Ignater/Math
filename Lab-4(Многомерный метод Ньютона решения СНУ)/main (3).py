import numpy as np
import matplotlib.pyplot as plt
import math

x = [1.2, 1.5, 1.8]
y = [[1.2214, 0, 0, 0], [1.6487, 0, 0, 0], [2.2255, 0, 0, 0]]


def q_sum(q, step):
    temp = 1
    for i in range(2, step + 1):
        temp = temp * (q - (i - 1))
    return temp


def First_Nyton(x_st, x, y, h):
    N = len(x)
    temp = 0
    q = (x_st - x[0]) / h
    for j in range(2, len(y)):
        temp = temp + ((y[0][j] / math.factorial(j)) * q * q_sum(q, j))
    temp += y[0][0]
    temp += +y[0][1] * q
    return temp



X_Length = len(x)
Y_Length = len(y)

print("x len = ", X_Length)
point = 1000
x_st = []
y_st = []
y_0 = []
count = 0

h = x[1] - x[0]

for i in range(0, point):
    x_st.append(count)
    count += 0.0025

for j in range(1, len(y)):
    for i in range(len(y) - j):
        y[i][j] = y[i + 1][j - 1] - y[i][j - 1]

for i in range(len(y)):
    for j in range(len(y[i])):
        print(y[i][j], end=' ')
    print()

for i in range(point):
    count = (First_Nyton(x_st[i], x, y, h))
    y_st.append(count)

for i in range(point):
    y_0.append(math.sqrt(x_st[i]))

plt.plot(x_st, y_st, color="red")
for i in range(len(x)):
    plt.plot(x[i], y[i][0], 'o')
plt.plot(x_st, y_0, color="black")
plt.show()