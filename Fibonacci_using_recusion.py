def Fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


for n in range(20):
    n += 1
    print(Fibonacci(n))
