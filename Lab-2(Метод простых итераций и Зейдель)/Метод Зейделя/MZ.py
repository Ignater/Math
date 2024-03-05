import math
def init():
    for i in range(0, n, 1):
        A.append([])
        E.append([])
        C.append([])
        B.append(0)
        X.append(0)
        for j in range(0, m, 1):
            A[i].append(0)
            if j != m - 1:
                if i == j:
                    E[i].append(1)
                else:
                    E[i].append(0)
                C[i].append(0)
    file = open("matritsa.txt", "r")
    i = 0
    j = 0
    for num in file:
        A[i][j] = int(num)
        j += 1
        if j == m:
            j = 0
            i += 1
    file.close()
    for i in range(0, n, 1):
        for j in range(0, m, 1):
            if j == m - 1:
                B[i] = A[i][j] / A[i][i]
            else:
                C[i][j] = A[i][j] / A[i][i]
            if i == j:
                C[i][i] = 0
def get_X():
    for i in range(0, n, 1):
        X[i] = 0
        for j in range(0, n, 1):
            X[i] += C[i][j] * X[j]
        X[i] = B[i] - X[i]
def get_max_b():
    return max(max(abs(B[0]), abs(B[1])), abs(B[2]))
def get_max_c():
    return max(max(abs(C[0][0]) + abs(C[0][1]) + abs(C[0][2]), abs(C[1][0]) + abs(C[1][1]) + abs(C[1][2])), abs(C[2][0]) + abs(C[2][1]) + abs(C[2][2]))
def ln(x):
    return math.log(x, math.e)
n = 3
m = 4
A = []
E = []
C = []
B = []
X = []
init()
step = 1
epsilon = 10 ** -3
c = get_max_c()
b = get_max_b()
N = (ln(epsilon * (1 - c) / b) / ln(c)) + 1
while step <= N:
    print("-----------------------------------------------------------------------")
    print(f"Шаг {step}:")
    get_X()
    print(f"X({step}) = [{X[0]:.{16}f}, {X[1]:.{16}f}, {X[2]:.{16}f}]")
    step += 1