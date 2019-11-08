def first_N(n):
    """
    n : positive integer
    returns :  first n perfect squares that are not even numbers
    """
    if n == 1:
        return 1
    else:
        return first_N(n - 1) + 2


n = input("enter the number of perfect square you wanted = ")

for i in range(int(n)):
    i += 1
    ans = first_N(i)**2
    print(ans)



