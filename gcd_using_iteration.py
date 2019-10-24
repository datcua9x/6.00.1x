def gcdIter(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    print(a)


gcdIter(110, 115)
