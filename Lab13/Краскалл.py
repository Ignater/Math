class Graph:
    def __init__(self):
        self.contacts = []
        self.distances = []
        self.n = 0

    def add_vertex(self, contacts, distances):
        self.contacts.append(contacts)
        self.distances.append(distances)
        self.n += 1

    def print(self, text, contacts=None, distances=None):
        print(text)

        if distances is None:
            contacts = self.contacts
            distances = self.distances

        print(contacts)
        print(distances)

    def draw_table(self, text, compact=False, contacts=None, distances=None):
        print(text)

        if distances is None:
            contacts = self.contacts.copy()
            distances = self.distances.copy()
            n = self.n

        else:
            n = len(contacts)

        table_massive = []

        for vertex1 in range(n):
            for vertex2 in range(n):
                if vertex2 in contacts[vertex1]:
                    number = distances[vertex1][contacts[vertex1].index(vertex2)]
                    table_massive.append(["       ", f" {number:5.2f} ", "       "])

                else:
                    if vertex1 == vertex2:
                        table_massive.append(["+++++++", "+++++++", "+++++++"])

                    else:
                        table_massive.append(["       ", "  inf  ", "       "])

        first_line = "|    "
        second_line = "|  0 "
        third_line = "|    "
        line = "|  0 "
        split = "--------" * n + "------"

        print(split)
        print("|    ", end = "")

        for i in range(n):
            print(f"|   {i:2}  ", end = "")

        print("|")

        for i in range(len(table_massive)):
            if compact:
                line += "|" + table_massive[i][1]

                if i % n == n - 1:
                    print(split)
                    print(f"{line}|")

                    line = f"| {(i // n + 1):2} "

            else:
                first_line += "|" + table_massive[i][0]
                third_line += "|" + table_massive[i][2]
                second_line += "|" + table_massive[i][1]

                if i % n == n - 1:
                    print(split)
                    print(f"{first_line}|")
                    print(f"{second_line}|")
                    print(f"{third_line}|")

                    first_line = "|    "
                    second_line = f"| {(i // n + 1):2} "
                    third_line = "|    "

        print(split)

    def quick_sort(self, distances, contacts, L, R):
        if L < R:
            i = L - 1
            pivot = distances[R]

            for j in range(L, R):
                if distances[j] <= pivot:
                    i += 1
                    contacts[i], contacts[j] = contacts[j], contacts[i]
                    distances[i], distances[j] = distances[j], distances[i]

            contacts[i + 1], contacts[R] = contacts[R], contacts[i + 1]
            distances[i + 1], distances[R] = distances[R], distances[i + 1]
            middle = i + 1

            self.quick_sort(distances, contacts, L, middle - 1)
            self.quick_sort(distances, contacts, middle + 1, R)

    def find_the_minimum_spanning_tree(self):
        contacts = []
        distances = []
        exceptions = []

        for i in range(self.n):
            exceptions.append(i)

            for j in range(len(self.distances[i])):
                if self.contacts[i][j] not in exceptions:
                    contacts.append([i, self.contacts[i][j]])
                    distances.append(self.distances[i][j])

        self.quick_sort(distances, contacts, 0, len(distances) - 1)

        new_contacts = []
        new_distances = []
        new_exceptions = []
        connected_contacts = exceptions.copy()

        print(end = "\n          ")
        print(*connected_contacts, sep = ", ")

        index = 0

        while len(connected_contacts) > 1:
            vertex1 = contacts[index][0]
            vertex2 = contacts[index][1]

            if vertex1 in connected_contacts and vertex2 in connected_contacts:
                connected_contacts.remove(vertex1)
                connected_contacts.remove(vertex2)
                connected_contacts.append(contacts[index])

                print(contacts[index], end = "    ")

            elif vertex1 not in connected_contacts and vertex2 in connected_contacts:
                connected_contacts.remove(vertex2)

                for i in range(len(connected_contacts)):
                    if type(connected_contacts[i]) == type([]):
                        if vertex1 in connected_contacts[i]:
                            connected_contacts[i].append(vertex2)
                            connected_contacts[i].sort()
                            break

                print(contacts[index], end = "    ")

            elif vertex1 in connected_contacts and vertex2 not in connected_contacts:
                connected_contacts.remove(vertex1)

                for i in range(len(connected_contacts)):
                    if type(connected_contacts[i]) == type([]):
                        if vertex2 in connected_contacts[i]:
                            connected_contacts[i].append(vertex1)
                            connected_contacts[i].sort()
                            break

                print(contacts[index], end = "    ")

            else:
                index1 = -1
                index2 = -1

                for i in range(len(connected_contacts)):
                    if type(connected_contacts[i]) == type([]):
                        if vertex1 in connected_contacts[i]:
                            index1 = i

                        if vertex2 in connected_contacts[i]:
                            index2 = i

                        if index1 != -1 and index2 != -1:
                            break

                if index1 != index2:
                    massive = connected_contacts[index1].copy()

                    for element in massive:
                        connected_contacts[index2].append(element)

                    connected_contacts[index2].sort()
                    connected_contacts.remove(connected_contacts[index1])

                    print(contacts[index], end="    ")

                else:
                    print(f"[̶{vertex1}̶,̶ ̶{vertex2}̶]̶", end = "    ")

            print(*connected_contacts, sep = ", ", end = "\n")

            index += 1

        print()

        for i in range(len(contacts)):
            vertex1 = contacts[i][0]
            vertex2 = contacts[i][1]

            if vertex1 in new_exceptions:
                if vertex2 not in new_exceptions:
                    new_contacts.append(contacts[i])
                    new_distances.append(distances[i])
                    new_exceptions.append(vertex2)

            else:
                if vertex2 in new_exceptions:
                    new_contacts.append(contacts[i])
                    new_distances.append(distances[i])
                    new_exceptions.append(vertex1)

                else:
                    new_contacts.append(contacts[i])
                    new_distances.append(distances[i])
                    new_exceptions.append(vertex1)
                    new_exceptions.append(vertex2)

        mst_contacts = []
        mst_distances = []

        for i in range(self.n):
            mst_contacts.append([])
            mst_distances.append([])

            for j in range(len(self.contacts[i])):
                flag = False

                for distance in new_distances:
                    if self.distances[i][j] == distance:
                        flag = True
                        break

                if flag:
                    mst_contacts[i].append(self.contacts[i][j])
                    mst_distances[i].append(self.distances[i][j])

        self.draw_table("Минимальный остов:", contacts=mst_contacts, distances=mst_distances)


graph = Graph()

graph.add_vertex([1, 5, 6], [20, 23, 1])
graph.add_vertex([0, 2, 6], [20, 5, 4])
graph.add_vertex([1, 3, 6], [5, 3, 9])
graph.add_vertex([2, 4, 6], [3, 17, 16])
graph.add_vertex([3, 5, 6], [17, 28, 25])
graph.add_vertex([0, 4, 6], [23, 28, 36])
graph.add_vertex([0, 1, 2, 3, 4, 5], [1, 4, 9, 16, 25, 36])

graph.draw_table("граф:")
graph.find_the_minimum_spanning_tree()