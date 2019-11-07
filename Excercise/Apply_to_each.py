def addOne(a):
    return a + 1


def square(b):
    return b * b


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


testlist = [1, -4, 8, -9]

print(applyToEach(testlist, abs))
print(applyToEach(testlist, addOne))
print(applyToEach(testlist, square))
