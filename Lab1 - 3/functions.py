from random import randint
def get_random_massive(minimal, maximal, n):
    massive = []
    for i in range(n):
        massive.append(randint(minimal, maximal))
    return massive