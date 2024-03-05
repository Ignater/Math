from random import randint

def create_random_massive(minimal, maximal, n):
    massive = []
    for i in range(n):
        massive.append(randint(minimal, maximal))
    return massive

def create_massive(n):
    massive = []
    for i in range(n):
        massive.append(i)
    return massive

def print_matrix_for_sff(matrix):
    n = len(matrix[0])
    for i in range(n):
        for j in range(n):
            print(f"({matrix[i][j].real:.1f} {matrix[i][j].imag:.1f}i) ", end = "")
        print()
    print("\n\n")

def print_massive(text, massive):
    print(text)
    print("[", end = "")
    print(*massive, sep = "  ", end = "")
    print("]")