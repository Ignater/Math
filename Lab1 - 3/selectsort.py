from functions import get_random_massive
def select_sort(massive, n):
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if massive[j] < massive[k]:
                k = j
        massive[i], massive[k] = massive[k], massive[i]
    print("Отсортированный массив:")
    print(*massive)
massive = get_random_massive(0, 100, 10)
n = len(massive)
print("Случайный массив:")
print(*massive)
select_sort(massive, n)