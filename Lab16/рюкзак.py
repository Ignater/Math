class Backpack:
    def __init__(self):
        self.m = [3, 5, 8]
        self.c = [8, 14, 23]
        self.n = len(self.m)
        self.negative_infinity = -10 ** 1000
        self.results = [[], []]

    def quick_sort(self, L, R):
        if L < R:
            i = L - 1
            pivot = self.results[0][R]

            for j in range(L, R):
                if self.results[0][j] <= pivot:
                    i += 1
                    self.results[1][i], self.results[1][j] = self.results[1][j], self.results[1][i]
                    self.results[0][i], self.results[0][j] = self.results[0][j], self.results[0][i]

            self.results[1][i+1], self.results[1][R] = self.results[1][R], self.results[1][i+1]
            self.results[0][i+1], self.results[0][R] = self.results[0][R], self.results[0][i+1]
            middle = i + 1

            self.quick_sort(L, middle - 1)
            self.quick_sort(middle + 1, R)

    def unlimited_backpack(self, M, flag = False):
        if M < 0:
            return self.negative_infinity

        maximal = 0

        if flag:
            print(f"Рюкзак неограниченный при M = {M}\n")
            print(end = f"f({M}) = max(")

        for i in range(self.n):
            if flag:
                if i != self.n - 1:
                    print(end = f"f({M} - {self.m[i]}) + {self.c[i]}; ")

                else:
                    print(end = f"f({M} - {self.m[i]}) + {self.c[i]})")

            maximal = max(maximal, self.unlimited_backpack(M - self.m[i]) + self.c[i])

        if M not in self.results[0]:
            self.results[0].append(M)
            self.results[1].append(maximal)

        if flag:
            n = len(self.results[0])

            self.quick_sort(0, n - 1)

            for i in range(n):
                print(end = f"\nf({self.results[0][i]}) = {self.results[1][i]}")

        return maximal

backpack = Backpack()
backpack.unlimited_backpack(13, True)