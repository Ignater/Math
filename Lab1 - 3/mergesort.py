from functions import get_random_massive
def print_massive(massive, k):
    for i in range(len(massive)):
        if i % k == 0:
            print("|  ", end = "")
        else:
            print(end = "   ")
        print(f"{massive[i]:2}", end = "  ")
    print("|")
def merge(massive1, massive2):
    if len(massive1) == 0:
        return massive2
    if len(massive2) == 0:
        return massive1
    k = 0
    l = 0
    massive = []
    while True:
        if k == len(massive1):
            for i in range(l, len(massive2)):
                massive.append(massive2[i])
            return massive
        if l == len(massive2):
            for i in range(k, len(massive1)):
                massive.append(massive1[i])
            return massive
        if massive1[k] < massive2[l]:
            massive.append(massive1[k])
            k += 1
        else:
            massive.append(massive2[l])
            l += 1
def append_merged_massive(massive, merged_massive):
    for elem in merged_massive:
        massive.append(elem)
def merge_sort(massive, n):
    k = 1
    step = 1
    new_massive = []
    while k < n:
        j = 0
        while 2 * j * k < n:
            if n < 2 * j * k + k:
                massive1 = massive[2*j*k:n]
                massive2 = []
            else:
                massive1 = massive[2*j*k:2*j*k+k]
                if n < 2 * j * k + 2 * k:
                    massive2 = massive[2*j*k+k:n]
                else:
                    massive2 = massive[2*j*k+k:2*j*k+2*k]
            merged_massive = merge(massive1, massive2)
            append_merged_massive(new_massive, merged_massive)
            j += 1
        massive = new_massive.copy()
        print(f"Шаг {step}:")
        print_massive(massive, k)
        new_massive = []
        k *= 2
        step += 1
    print("Отсортированный массив:")
    print(*massive)
massive = get_random_massive(0, 100, 10)
n = len(massive)
print("Случайный массив:")
print(*massive)
merge_sort(massive, n)