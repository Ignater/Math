def simple_convolution(a, b):
    a_length = len(a)
    b_length = len(b)
    c_length = a_length + b_length - 1
    c = []
    for i in range(c_length):
        print(f"c{i} = ", end = "")
        flag = False
        c.append(0)
        for k in range(a_length):
        #for k in range(a_length - 1, -1, -1):
            l = i - k

            if 0 <= l < b_length:
                if flag:
                    print("+ ", end="")
                c[i] += a[k] * b[l]
                print(f"{a[k]} * {b[l]} ", end = "")
                flag = True
        print(f"= {c[i]}")
    return c

a = [1, 2, 3, 4]
b = [0.5, 0.2]
print("a = [", end = "")
print(*a, sep = "  ", end = "")
print("]")
print("b = [", end = "")
print(*b, sep = "  ", end = "")
print("]\n")
c = simple_convolution(a, b)
print("\nc = [", end = "")
print(*c, sep = "  ", end = "")
print("]")