from functions import get_random_massive
def bubble_sort(massive, n):
    flag = True
    for i in range(n - 1):
        if not flag:
            break
        flag = False
        for j in range(n - 1, i, -1):
            if massive[j] < massive[j-1]:
                massive[j], massive[j-1] = massive[j-1], massive[j]
                flag = True
    print("Отсортированный массив:")
    print(*massive)
massive = get_random_massive(0, 100, 10)
n = len(massive)
print("Случайный массив:")
print(*massive)
bubble_sort(massive, n)