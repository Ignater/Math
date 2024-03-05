def swap(ind1, ind2):
    for k in range(m):
        matrix[ind1][k], matrix[ind2][k] = matrix[ind2][k], matrix[ind1][k]
def output():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] < 0:
                if matrix[i][j] > -10:
                    print(f"{matrix[i][j]:.{4}f}", end = "     ")
                else:
                    print(f"{matrix[i][j]:.{3}f}", end = "     ")
            else:
                if matrix[i][j] < 10:
                    print(f"{matrix[i][j]:.{5}f}", end = "     ")
                else:
                    print(f"{matrix[i][j]:.{4}f}", end = "     ")
        print(end = "\n")
def straight():
    for k in range(n - 1):
        maximal = k
        max = matrix[0][k]
        for l in range(k + 1, n):
            if abs(max) < abs(matrix[l][k]):
                max = matrix[l][k]
                maximal = l
        swap(k, maximal)
        for i in range(k + 1, n):
            number = -matrix[i][k] / matrix[k][k]
            for j in range(k, m):
                matrix[i][j] += matrix[k][j] * number
    output()
def reverse():
    mas = []
    for i in range(n):
        mas.append(0)
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, i - 1, -1):
            if j == m - 1:
                mas[i] += matrix[i][j]
            elif j != i:
                mas[i] -= mas[j] * matrix[i][j]
            else:
                mas[i] /= matrix[i][j]
    for i in range(n):
        print(f"x{i + 1} = {int(mas[i])}")
n = 3
m = 4
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(m):
        matrix[i].append(0)
file = open("matritsa.txt", "r")
i = 0
j = 0
for num in file:
    matrix[i][j] = float(num)
    j += 1
    if j == m:
        j = 0
        i += 1
file.close()
print("-------------------------------------------")
print("Матрица:")
output()
print("-------------------------------------------")
print("Прямой ход:")
straight()
print("-------------------------------------------")
print("Обратный ход:")
reverse()