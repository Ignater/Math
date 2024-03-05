class Graph:
    def __init__(self, n):
        self.distances = []
        self.n = n
        self.infinity = 10 ** 1000

        for i in range(n):
            self.distances.append([self.infinity] * n)
            self.distances[i][i] = 0

    def add(self, vertex1, vertex2, distance):
        if vertex1 == vertex2:
            return

        self.distances[vertex1][vertex2] = distance
        self.distances[vertex2][vertex1] = distance

    def print(self, text):
        print(text)

        for i in range(self.n):
            for j in range(self.n):
                if self.distances[i][j] == self.infinity:
                    print("  inf ", end = "")

                else:
                    print(f"{self.distances[i][j]:5.2f} ", end = "")

            print()

    def draw_table(self, text, compact = False):
        print(text)

        table_massive = []

        for i in range(self.n):
            for j in range(self.n):
                number = self.distances[i][j]
                if i == j:
                    table_massive.append(["+++++++", "+++++++", "+++++++"])
                elif number == self.infinity:
                    table_massive.append(["       ", "  inf  ", "       "])
                else:
                    table_massive.append(["       ", f" {number:5.2f} ", "       "])

        first_line = "|    "
        second_line = "|  0 "
        third_line = "|    "
        line = "|  0 "
        split = "--------" * self.n + "------"

        print(split)
        print("|    ", end = "")

        for i in range(self.n):
            print(f"|   {i:2}  ", end = "")

        print("|")

        for i in range(len(table_massive)):
            if compact:
                line += "|" + table_massive[i][1]

                if i % self.n == self.n - 1:
                    print(split)
                    print(f"{line}|")

                    line = f"| {(i // self.n + 1):2} "

            else:
                first_line += "|" + table_massive[i][0]
                third_line += "|" + table_massive[i][2]
                second_line += "|" + table_massive[i][1]

                if i % self.n == self.n - 1:
                    print(split)
                    print(f"{first_line}|")
                    print(f"{second_line}|")
                    print(f"{third_line}|")

                    first_line = "|    "
                    second_line = f"| {(i // self.n + 1):2} "
                    third_line = "|    "

        print(split)

    def print_output(self, D):
        print("\nКратчайшие пути от вершины 0:")

        for i in range(self.n):
            print(f"До вершины {i}: {D[i]}")

    def print_S_D(self, S, D):
        print(S, end = " " * (25 - 3 * len(S) - 4))

        for elem in D:
            if elem == self.infinity:
                print(end = "  | inf")

            else:
                print(end = f"  |{elem:4}")

        print()

    def deikstra(self, i):
        D = self.distances[i].copy()
        D1 = [0] * self.n
        V = list(range(self.n))
        S = [i]
        S_not_sorted = S.copy()

        w = -1
        minimal = max(D)

        print(end = "\nS                     ")

        for i in range(self.n):
            print(end = f" | D[{i}]")

        print("\n------------------------------------------------------------")
        self.print_S_D(S_not_sorted, D)

        while S != V:
            V_without_S = []

            for i in range(self.n):
                if i not in S:
                    V_without_S.append(i)

                    if D[i] < minimal:
                        w = i
            print(V_without_S)
            S.append(w)
            S.sort()
            S_not_sorted.append(w)

            for v in V_without_S:
                D1[w] = "   -"

                D[v] = min(D[v], D[w] + self.distances[w][v])

                if D1[v] != "   -":
                    D1[v] = D[v]

            self.print_S_D(S_not_sorted, D1)

        self.print_output(D)


graph = Graph(5)

graph.add(0, 1, 25)
graph.add(0, 2, 15)
graph.add(0, 3, 7)
graph.add(0, 4, 2)
graph.add(1, 2, 6)
graph.add(2, 3, 4)
graph.add(3, 4, 3)

graph.draw_table("Граф:")
graph.deikstra(0)