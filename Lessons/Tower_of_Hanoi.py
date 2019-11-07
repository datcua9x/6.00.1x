def printMove(first, third):
    print(" Move from " + str(first) + " to " + str(third))


def Tower(n, first, second, third):
    if n == 1:
        printMove(first, third)
    else:
        Tower(n - 1, first, third, second)
        Tower(1, first, second, third)
        Tower(n - 1, second, first, third)


print(Tower(3, 'A', 'B', 'C'))
