import math

size = 4
x = [2, 3, 4, 5]
y = [-1, 2, 3, 1]
inter = 3.5

print("x\t\ty")
for i in range(size):
    print("{:.2f}\t{:10.2f}".format(x[i], y[i]))

lagrange = 0
bas = 1

for i in range(size):
    bas = 1
    for j in range(size - 1, -1, -1):
        if j == i:
            continue
        bas *= (inter - x[j])/(x[i] - x[j])
    lagrange += bas * y[i]

print("\nx({:.1f}) = {:.2f}".format(inter, lagrange))