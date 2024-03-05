import math

def f(x):
    return x**2 - 6 * x

if __name__ == "__main__":
    fi = 1.618
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    x1 = b - ((b - a) / fi)
    x2 = a + ((b - a) / fi)
    y1 = f(x1)
    y2 = f(x2)
    eps = float(input("Input eps: "))


    print("Метод золотого сечения:")
    print(f"[{a};{b}]")
    flag = True
    i = 1
    while flag:
        if y1 < y2:
            b = x2
            x2 = x1
            x1 = b - ((b - a) / fi)
            y2 = y1
            y1 = f(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + ((b - a) / fi)
            y1 = y2
            y2 = f(x2)
        print(f"Шаг {i}, интервал [{a};{b}]")
        i += 1
        if (b - a) < eps:
            flag = False
            x = (a + b) / 2

    print(f"x = {x}, f({x}) = {f(x)}")